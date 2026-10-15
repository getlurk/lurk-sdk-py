import json
import unittest
from typing import List, Optional, Tuple

from getlurk import Lurk, LurkConnectionError, LurkError, RequestOptions, Response

KEY = "lurk_sk_test_abc"


def json_response(status: int, body: object, headers: Optional[dict] = None) -> Response:
    return Response(status, {"content-type": "application/json", **(headers or {})}, json.dumps(body).encode())


def error_response(status: int, code: str, message: str = "No.", **extra: object) -> Response:
    return json_response(
        status,
        {"error": {"status": status, "code": code, "message": message, "request_id": "req_1", **extra}},
        {"request-id": "req_1"},
    )


class Fake:
    """A transport that answers from a list, and remembers what it was asked."""

    def __init__(self, *answers: object) -> None:
        self.answers = list(answers)
        self.calls: List[Tuple[str, str, dict, Optional[bytes], float]] = []

    def __call__(self, method, url, headers, body, timeout):
        self.calls.append((method, url, dict(headers), body, timeout))
        answer = self.answers.pop(0) if len(self.answers) > 1 else self.answers[0]
        if isinstance(answer, Exception):
            raise answer
        return answer


def client(fake: Fake, **options) -> Lurk:
    waits: List[float] = []
    lurk = Lurk(KEY, transport=fake, sleep=waits.append, **options)
    lurk.waits = waits  # type: ignore[attr-defined]
    return lurk


class ClientTest(unittest.TestCase):
    def test_needs_a_project_key(self):
        with self.assertRaises(ValueError):
            Lurk("nope")
        with self.assertRaises(ValueError):
            Lurk(None)

    def test_never_shows_the_key(self):
        self.assertNotIn(KEY, repr(Lurk(KEY)))

    def test_sends_an_event_with_a_key_in_the_body_and_the_bearer_token(self):
        fake = Fake(json_response(200, {"receipts": []}))
        out = client(fake).events.send({"event": "checkin.scanned", "user": "maya@example.com"})
        self.assertEqual(out, {"receipts": []})
        method, url, headers, body, _ = fake.calls[0]
        self.assertEqual((method, url), ("POST", "https://api.getlurk.com/v1/events"))
        self.assertEqual(headers["authorization"], f"Bearer {KEY}")
        self.assertTrue(headers["x-lurk-sdk"].startswith("python/"))
        sent = json.loads(body)
        self.assertEqual(sent["event"], "checkin.scanned")
        self.assertRegex(sent["idempotency_key"], r"^[0-9a-f-]{36}$")

    def test_takes_fields_as_keywords_too(self):
        fake = Fake(json_response(200, {}))
        client(fake).events.send(event="checkin.scanned", user="maya@example.com", idempotency_key="mine")
        self.assertEqual(json.loads(fake.calls[0][3])["idempotency_key"], "mine")

    def test_a_key_of_your_own_in_the_options_wins(self):
        fake = Fake(json_response(200, {}))
        client(fake).events.send({"event": "e", "user": "u"}, options=RequestOptions(idempotency_key="abc"))
        self.assertEqual(json.loads(fake.calls[0][3])["idempotency_key"], "abc")

    def test_fills_the_path_and_the_query(self):
        fake = Fake(json_response(200, {"data": [], "has_more": False}))
        client(fake).rules.get({"id": "morning regular/1"})
        self.assertEqual(fake.calls[0][1], "https://api.getlurk.com/v1/rules/morning%20regular%2F1")
        fake = Fake(json_response(200, {"data": [], "has_more": False}))
        client(fake).rules.list({"limit": 5, "status": "live"})
        url = fake.calls[0][1]
        self.assertIn("limit=5", url)
        self.assertIn("status=live", url)
        self.assertEqual(fake.calls[0][3], None)

    def test_retries_a_server_error_on_a_read_and_on_a_write_with_a_key_using_the_same_key(self):
        fake = Fake(error_response(500, "internal"), json_response(200, {"receipts": []}))
        lurk = client(fake)
        lurk.events.send({"event": "e", "user": "u"})
        self.assertEqual(len(fake.calls), 2)
        self.assertEqual(fake.calls[0][3], fake.calls[1][3])
        self.assertEqual(len(lurk.waits), 1)  # type: ignore[attr-defined]
        fake = Fake(error_response(503, "internal"), json_response(200, {"data": [], "has_more": False}))
        client(fake).rules.list()
        self.assertEqual(len(fake.calls), 2)

    def test_never_repeats_a_write_that_has_no_key(self):
        # api_keys.create returns a secret shown once: repeating it could make two.
        fake = Fake(error_response(500, "internal"), json_response(200, {"id": "key_1"}))
        with self.assertRaises(LurkError) as caught:
            client(fake).api_keys.create({"name": "x"})
        self.assertEqual(caught.exception.status, 500)
        self.assertEqual(len(fake.calls), 1)

    def test_waits_for_a_rate_limit_and_gives_up_on_a_long_one(self):
        fake = Fake(error_response(429, "rate_limited"), json_response(200, {"data": [], "has_more": False}))
        fake.answers[0] = Response(429, {"retry-after": "3", "request-id": "req_1"}, fake.answers[0].body)
        lurk = client(fake)
        lurk.rules.list()
        self.assertEqual(lurk.waits, [3.0])  # type: ignore[attr-defined]
        fake = Fake(Response(429, {"retry-after": "600"}, error_response(429, "rate_limited").body))
        with self.assertRaises(LurkError) as caught:
            client(fake).rules.list()
        self.assertEqual(caught.exception.code, "rate_limited")
        self.assertEqual(caught.exception.retry_after_seconds, 600)
        self.assertEqual(len(fake.calls), 1)

    def test_a_validation_error_is_not_retried_and_says_what_was_wrong(self):
        fake = Fake(error_response(422, "validation_failed", "A unit with key beans already exists.", param="key"))
        with self.assertRaises(LurkError) as caught:
            client(fake).units.create({"name": "Beans", "group": "points"})
        e = caught.exception
        self.assertEqual((e.status, e.code, e.param, e.request_id), (422, "validation_failed", "key", "req_1"))
        self.assertEqual(str(e), "A unit with key beans already exists.")
        self.assertEqual(len(fake.calls), 1)

    def test_an_error_carries_what_to_do_next_and_says_whether_a_retry_can_work(self):
        fake = Fake(
            error_response(422, "validation_failed", "Bad.", param="key", next_step="Fix the field in param."),
            error_response(429, "rate_limited", "Slow down.", next_step="Wait for Retry-After."),
        )
        with self.assertRaises(LurkError) as refused:
            client(fake, max_retries=0).units.create({"name": "Beans", "group": "points"})
        self.assertEqual(refused.exception.next_step, "Fix the field in param.")
        self.assertFalse(refused.exception.is_retryable)
        with self.assertRaises(LurkError) as limited:
            client(fake, max_retries=0).rules.list()
        self.assertTrue(limited.exception.is_retryable)

    def test_a_proxy_page_is_an_error_too(self):
        fake = Fake(Response(502, {}, b"<html>Bad gateway</html>"))
        with self.assertRaises(LurkError) as caught:
            client(fake, max_retries=0).rules.list()
        self.assertEqual((caught.exception.status, caught.exception.code), (502, "internal"))

    def test_no_answer_is_a_connection_error_after_the_retries(self):
        fake = Fake(OSError("refused"))
        with self.assertRaises(LurkConnectionError):
            client(fake).rules.list()
        self.assertEqual(len(fake.calls), 3)  # the first try and two retries
        fake = Fake(TimeoutError())
        with self.assertRaises(LurkConnectionError) as caught:
            client(fake, max_retries=0).rules.list()
        self.assertIn("in time", str(caught.exception))

    def test_options_override_the_clients(self):
        fake = Fake(error_response(500, "internal"))
        with self.assertRaises(LurkError):
            client(fake).rules.list(options=RequestOptions(max_retries=0, timeout=5, headers={"traceparent": "00-x"}))
        self.assertEqual(len(fake.calls), 1)
        self.assertEqual(fake.calls[0][4], 5)
        self.assertEqual(fake.calls[0][2]["traceparent"], "00-x")

    def test_paginates_through_every_page(self):
        pages = [
            json_response(200, {"data": [1, 2], "has_more": True, "next_cursor": "c1"}),
            json_response(200, {"data": [3], "has_more": False, "next_cursor": None}),
        ]
        fake = Fake(*pages)
        self.assertEqual(list(client(fake).paginate("rules.list", {"limit": 2})), [1, 2, 3])
        self.assertIn("cursor=c1", fake.calls[1][1])

    def test_a_group_of_operations_is_an_attribute(self):
        lurk = Lurk(KEY, transport=Fake(json_response(200, {})))
        for group in ("events", "rules", "units", "audiences", "views", "dashboards", "promotions"):
            self.assertTrue(hasattr(lurk, group), group)


if __name__ == "__main__":
    unittest.main()
