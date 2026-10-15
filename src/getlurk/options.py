"""Per-call settings."""

from __future__ import annotations

from typing import Mapping, NamedTuple, Optional


class RequestOptions(NamedTuple):
    """Anything left as ``None`` uses the client's."""

    #: Overrides the client's retry count for this call.
    max_retries: Optional[int] = None
    #: Overrides the client's timeout (seconds) for this call.
    timeout: Optional[float] = None
    #: Your own idempotency key for this call. Left out, the SDK makes one and reuses it on every retry.
    idempotency_key: Optional[str] = None
    #: Extra headers, such as ``traceparent`` to join your trace to ours.
    headers: Optional[Mapping[str, str]] = None
