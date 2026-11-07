"""A response whose body is cut short must follow the same retry rules as a dropped connection (LUR-153)."""

import http.client
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import List, Optional, Tuple

from getlurk import Lurk, LurkConnectionError, LurkError
from getlurk.client import urllib_transport


class InterruptedBodyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seen: List[Tuple[str, str, bytes]] = []
        cls.plan: List[Tuple[int, bool]] = []  # (status, cut the body short) for each request, the last one repeats

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                length = int(self.headers.get("Content-Length", "0"))
                body = self.rfile.read(length) if length else b""
                cls.seen.append((self.command, self.path, body))
                status, cut = cls.plan.pop(0) if len(cls.plan) > 1 else cls.plan[0]
                payload = json.dumps({"receipts": [], "data": [], "has_more": False, "id": "key_1"}).encode()
                if status >= 400:
                    payload = json.dumps({"error": {"code": "internal", "message": "No."}}).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                # Promise the whole body, send half, and close: the client reads an IncompleteRead.
                self.wfile.write(payload[: len(payload) // 2] if cut else payload)
                self.close_connection = True

            do_POST = do_GET

            def log_message(self, *args):
                pass

        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        type(self).seen.clear()

    def lurk(self) -> Lurk:
        self.waits: List[float] = []
        return Lurk("lurk_sk_test", base_url=self.url, sleep=self.waits.append)

    def test_the_transport_raises_an_os_error_for_a_truncated_body(self):
        type(self).plan = [(200, True)]
        with self.assertRaises(OSError) as caught:
            urllib_transport("GET", self.url + "/v1/rules", {}, None, 3)
        self.assertIsInstance(caught.exception.__cause__, http.client.IncompleteRead)

    def test_a_read_is_retried(self):
        type(self).plan = [(200, True), (200, False)]
        out = self.lurk().rules.list()
        self.assertEqual(out["data"], [])
        self.assertEqual(len(self.seen), 2)
        self.assertEqual(len(self.waits), 1)

    def test_a_write_with_a_key_is_retried_with_the_same_key_and_body(self):
        type(self).plan = [(200, True), (200, False)]
        self.lurk().events.send({"event": "e", "user": "u"})
        self.assertEqual(len(self.seen), 2)
        self.assertEqual(self.seen[0][2], self.seen[1][2])
        self.assertIn("idempotency_key", json.loads(self.seen[0][2]))

    def test_a_write_without_a_key_is_not_repeated_and_is_a_connection_error(self):
        # api_keys.create returns a secret shown once: repeating it could make two.
        type(self).plan = [(200, True), (200, False)]
        with self.assertRaises(LurkConnectionError):
            self.lurk().api_keys.create({"name": "x"})
        self.assertEqual(len(self.seen), 1)

    def test_a_read_that_keeps_breaking_ends_as_a_connection_error(self):
        type(self).plan = [(200, True)]
        with self.assertRaises(LurkConnectionError):
            self.lurk().rules.list()
        self.assertEqual(len(self.seen), 3)  # the first try and two retries

    def test_an_error_answer_with_a_cut_body_keeps_its_status(self):
        type(self).plan = [(503, True), (200, False)]
        self.lurk().rules.list()
        self.assertEqual(len(self.seen), 2)
        type(self).plan = [(422, True)]
        with self.assertRaises(LurkError) as caught:
            self.lurk().rules.list()
        self.assertEqual(caught.exception.status, 422)
