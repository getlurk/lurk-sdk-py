import base64
import hashlib
import hmac
import json
import unittest

from getlurk import WebhookVerificationError, construct_event

SECRET_BYTES = b"0123456789abcdef0123456789abcdef"
SECRET = "whsec_" + base64.b64encode(SECRET_BYTES).decode()
BODY = json.dumps({"id": "whd_1", "type": "activity.created", "created_at": "2026-10-13T10:00:00Z", "data": {}})
NOW = 1_791_000_000


def sign(body: str, delivery_id: str = "whd_1", timestamp: int = NOW, key: bytes = SECRET_BYTES) -> dict:
    digest = hmac.new(key, f"{delivery_id}.{timestamp}.{body}".encode(), hashlib.sha256).digest()
    return {
        "Webhook-Id": delivery_id,
        "Webhook-Timestamp": str(timestamp),
        "Webhook-Signature": "v1," + base64.b64encode(digest).decode(),
    }


class WebhookTest(unittest.TestCase):
    def test_returns_the_event_when_the_signature_checks_out(self):
        event = construct_event(BODY, sign(BODY), SECRET, now=lambda: NOW)
        self.assertEqual(event["type"], "activity.created")

    def test_takes_bytes_and_header_names_in_any_case(self):
        headers = {k.lower(): v for k, v in sign(BODY).items()}
        self.assertEqual(construct_event(BODY.encode(), headers, SECRET, now=lambda: NOW)["id"], "whd_1")

    def test_accepts_one_good_signature_among_several(self):
        headers = sign(BODY)
        headers["Webhook-Signature"] = "v1,AAAA " + headers["Webhook-Signature"]
        self.assertEqual(construct_event(BODY, headers, SECRET, now=lambda: NOW)["id"], "whd_1")

    def test_refuses_a_changed_body_a_wrong_secret_and_missing_headers(self):
        with self.assertRaisesRegex(WebhookVerificationError, "does not match"):
            construct_event(BODY.replace("whd_1", "whd_2"), sign(BODY), SECRET, now=lambda: NOW)
        with self.assertRaisesRegex(WebhookVerificationError, "does not match"):
            construct_event(BODY, sign(BODY, key=b"x" * 32), SECRET, now=lambda: NOW)
        with self.assertRaisesRegex(WebhookVerificationError, "missing"):
            construct_event(BODY, {}, SECRET, now=lambda: NOW)

    def test_refuses_a_timestamp_too_far_off(self):
        with self.assertRaisesRegex(WebhookVerificationError, "too old"):
            construct_event(BODY, sign(BODY, timestamp=NOW - 301), SECRET, now=lambda: NOW)
        self.assertEqual(
            construct_event(BODY, sign(BODY, timestamp=NOW - 299), SECRET, now=lambda: NOW)["id"], "whd_1"
        )


if __name__ == "__main__":
    unittest.main()
