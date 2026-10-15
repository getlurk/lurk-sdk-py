"""Checking a webhook delivery's signature (Standard Webhooks: HMAC-SHA-256 over ``<id>.<timestamp>.<body>``)."""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import json
import time
from typing import Any, Callable, Dict, List, Literal, Mapping, Optional, TypedDict, Union

from .errors import WebhookVerificationError

DEFAULT_TOLERANCE_SECONDS = 300

ActivityCreatedEvent = TypedDict(
    "ActivityCreatedEvent",
    {
        # The delivery id (whd_...). The same on every retry: use it to ignore repeats.
        "id": str,
        "type": Literal["activity.created"],
        "created_at": str,
        "data": Dict[str, Any],
    },
)

RuleLiveEvent = TypedDict(
    "RuleLiveEvent",
    {"id": str, "type": Literal["rule.live"], "created_at": str, "data": Dict[str, Any]},
)

WebhookEvent = Union[ActivityCreatedEvent, RuleLiveEvent]


def _header(headers: Mapping[str, Any], name: str) -> Optional[str]:
    for key, value in headers.items():
        if key.lower() == name:
            return value[0] if isinstance(value, (list, tuple)) else value
    return None


def construct_event(
    body: Union[str, bytes],
    headers: Mapping[str, Any],
    secret: str,
    *,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: Optional[Callable[[], float]] = None,
) -> WebhookEvent:
    """Checks a webhook delivery and returns the event.

    Pass the raw body (not parsed JSON), the request headers and the endpoint's secret (``whsec_...``). Raises
    ``WebhookVerificationError`` if the signature does not match or the timestamp is more than five minutes off.
    """
    raw = body.encode() if isinstance(body, str) else body
    delivery_id = _header(headers, "webhook-id")
    signatures = _header(headers, "webhook-signature")
    try:
        timestamp = int(_header(headers, "webhook-timestamp") or "")
    except ValueError:
        timestamp = None
    if not delivery_id or not signatures or timestamp is None:
        raise WebhookVerificationError("The webhook headers are missing.")
    current = int((now or time.time)())
    if abs(current - timestamp) > tolerance_seconds:
        raise WebhookVerificationError("The webhook timestamp is too old or too new.")

    try:
        key = base64.b64decode(secret[6:] if secret.startswith("whsec_") else secret)
    except (binascii.Error, ValueError) as error:
        raise WebhookVerificationError("The webhook secret is not valid.") from error
    signed = f"{delivery_id}.{timestamp}.".encode() + raw
    expected = base64.b64encode(hmac.new(key, signed, hashlib.sha256).digest()).decode()
    for candidate in signatures.split(" "):
        version, _, value = candidate.partition(",")
        # Constant-time comparison.
        if version == "v1" and value and hmac.compare_digest(value, expected):
            try:
                return json.loads(raw)
            except ValueError as error:
                raise WebhookVerificationError("The webhook body isn't JSON.") from error
    raise WebhookVerificationError("The webhook signature does not match.")
