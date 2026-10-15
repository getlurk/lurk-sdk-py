import asyncio
import json
import threading
import unittest

from getlurk import AsyncLurk, LurkError

from tests.test_client import KEY, Fake, error_response, json_response


def client(fake: Fake, **options) -> AsyncLurk:
    return AsyncLurk(KEY, transport=fake, sleep=lambda _s: None, **options)


class AsyncClientTest(unittest.IsolatedAsyncioTestCase):
    async def test_awaits_the_same_calls_with_the_same_behaviour(self):
        fake = Fake(json_response(200, {"receipts": []}))
        out = await client(fake).events.send({"event": "checkin.scanned", "user": "maya@example.com"})
        self.assertEqual(out, {"receipts": []})
        method, url, headers, body, _ = fake.calls[0]
        self.assertEqual((method, url), ("POST", "https://api.getlurk.com/v1/events"))
        self.assertEqual(headers["authorization"], f"Bearer {KEY}")
        self.assertRegex(json.loads(body)["idempotency_key"], r"^[0-9a-f-]{36}$")

    async def test_does_not_block_the_event_loop(self):
        started = threading.Event()
        release = threading.Event()

        def slow(method, url, headers, body, timeout):
            started.set()
            release.wait(5)
            return json_response(200, {"data": [], "has_more": False, "next_cursor": None})

        pending = asyncio.ensure_future(client(slow).rules.list())  # type: ignore[arg-type]
        for _ in range(100):
            if started.is_set():
                break
            await asyncio.sleep(0.01)
        # The loop is free while the call waits: this line runs before the call is answered.
        self.assertTrue(started.is_set())
        self.assertFalse(pending.done())
        release.set()
        self.assertEqual((await pending)["data"], [])

    async def test_raises_the_same_typed_errors(self):
        fake = Fake(error_response(422, "validation_failed", "Bad.", param="key", next_step="Fix it."))
        with self.assertRaises(LurkError) as caught:
            await client(fake, max_retries=0).units.create({"name": "Beans", "group": "points"})
        self.assertEqual((caught.exception.code, caught.exception.param, caught.exception.next_step), ("validation_failed", "key", "Fix it."))

    async def test_pages_as_you_go(self):
        fake = Fake(
            json_response(200, {"data": [{"key": "a"}, {"key": "b"}], "has_more": True, "next_cursor": "p2"}),
            json_response(200, {"data": [{"key": "c"}], "has_more": False, "next_cursor": None}),
        )
        seen = [r["key"] async for r in client(fake).paginate("rules.list", {"limit": 2})]
        self.assertEqual(seen, ["a", "b", "c"])
        self.assertIn("cursor=p2", fake.calls[1][1])

    async def test_never_shows_the_key(self):
        self.assertNotIn(KEY, repr(client(Fake(json_response(200, {})))))

    async def test_an_unknown_resource_is_an_attribute_error(self):
        with self.assertRaises(AttributeError):
            client(Fake(json_response(200, {}))).nothing_here
