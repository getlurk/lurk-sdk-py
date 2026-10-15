"""The Lurk API for Python.

>>> from getlurk import Lurk
>>> lurk = Lurk()  # reads the key from LURK_KEY
>>> receipt = lurk.events.send({"event": "checkin.scanned", "user": "maya@example.com"})
"""

from ._generated import schema, types
from .aio import AsyncLurk
from .client import DEFAULT_BASE_URL, SDK_VERSION, Lurk, Response, Transport
from .errors import LurkConnectionError, LurkError, WebhookVerificationError
from .options import RequestOptions
from .webhooks import ActivityCreatedEvent, RuleLiveEvent, WebhookEvent, construct_event

__all__ = [
    "ActivityCreatedEvent",
    "AsyncLurk",
    "DEFAULT_BASE_URL",
    "Lurk",
    "LurkConnectionError",
    "LurkError",
    "RequestOptions",
    "Response",
    "RuleLiveEvent",
    "SDK_VERSION",
    "Transport",
    "WebhookEvent",
    "WebhookVerificationError",
    "construct_event",
    "schema",
    "types",
]
