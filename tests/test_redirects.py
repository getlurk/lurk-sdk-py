"""Real loopback redirects must never send the SDK's bearer to a second request."""

import io
import threading
import unittest
import urllib.response
from email.message import Message
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from unittest.mock import patch

from getlurk import Lurk, LurkError
from getlurk.client import urllib_transport


class RedirectTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seen = []
        cls.location = ""
        cls.code = 302

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                # Drain POST bodies before closing: unread bytes can reset the socket on macOS.
                length = int(self.headers.get("Content-Length", "0"))
                if length:
                    self.rfile.read(length)
                cls.seen.append((self.path, self.headers.get("Authorization")))
                if self.path == "/redirect":
                    self.send_response(cls.code)
                    self.send_header("Location", cls.location)
                else:
                    self.send_response(200)
                self.end_headers()
                self.wfile.write(b"{}")

            do_POST = do_GET

            def log_message(self, *args):
                pass

        cls.servers = [ThreadingHTTPServer(("127.0.0.1", 0), Handler) for _ in range(2)]
        cls.threads = [threading.Thread(target=s.serve_forever, daemon=True) for s in cls.servers]
        for thread in cls.threads:
            thread.start()
        cls.source = f"http://127.0.0.1:{cls.servers[0].server_port}"
        cls.destination = f"http://127.0.0.1:{cls.servers[1].server_port}"

    @classmethod
    def tearDownClass(cls):
        for server in cls.servers:
            server.shutdown()
            server.server_close()
        for thread in cls.threads:
            thread.join()

    def test_redirects_are_not_followed_for_reads_or_writes(self):
        for code in (301, 302, 303, 307, 308):
            for target in (self.source, self.destination, self.destination.replace("127.0.0.1", "localhost")):
                for method in ("GET", "POST"):
                    with self.subTest(code=code, target=target, method=method):
                        type(self).seen.clear()
                        type(self).code = code
                        type(self).location = target + "/capture"
                        response = urllib_transport(method, self.source + "/redirect",
                                                    {"authorization": "Bearer synthetic-test-key"},
                                                    b"{}" if method == "POST" else None, 3)
                        self.assertEqual(response.status, code)
                        self.assertEqual(self.seen, [("/redirect", "Bearer synthetic-test-key")])

    def test_https_downgrade_does_not_reach_the_http_destination(self):
        # Simulate only the TLS response; urllib's real redirect machinery and the HTTP destination remain live.
        type(self).seen.clear()
        headers = Message()
        headers["Location"] = self.destination + "/capture"

        def tls_response(handler, request):
            self.assertEqual(request.get_header("Authorization"), "Bearer synthetic-test-key")
            response = urllib.response.addinfourl(io.BytesIO(b"{}"), headers, request.full_url, 302)
            response.msg = "Found"
            return response

        with patch("urllib.request.HTTPSHandler.https_open", tls_response):
            response = urllib_transport("GET", "https://source.example.test/redirect",
                                        {"authorization": "Bearer synthetic-test-key"}, None, 3)
        self.assertEqual(response.status, 302)
        self.assertEqual(self.seen, [])

    def test_normal_calls_work_and_redirects_surface_as_sdk_errors(self):
        self.assertEqual(urllib_transport("GET", self.source + "/ok", {}, None, 3).status, 200)
        type(self).code = 302
        type(self).location = self.destination + "/capture"
        # Point a real SDK read at a route that always redirects.
        def redirect_transport(method, url, headers, body, timeout):
            return urllib_transport(method, self.source + "/redirect", headers, body, timeout)

        with self.assertRaises(LurkError) as caught:
            Lurk("lurk_sk_test_synthetic", transport=redirect_transport).units.list()
        self.assertEqual(caught.exception.status, 302)
