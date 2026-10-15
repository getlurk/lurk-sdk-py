"""Errors the SDK raises."""

from __future__ import annotations

from typing import Optional


class LurkError(Exception):
    """The API answered with an error.

    ``code`` is the stable part to branch on; ``message`` is a sentence you can show. ``request_id`` is what to quote to support,
    and ``doc_url`` explains the code; ``next_step`` is one sentence on what to do about it. For ``rate_limited``, ``retry_after_seconds`` is how long the API asked you to wait.
    """

    def __init__(
        self,
        *,
        status: int,
        code: str,
        message: str,
        param: Optional[str] = None,
        request_id: Optional[str] = None,
        doc_url: Optional[str] = None,
        next_step: Optional[str] = None,
        retry_after_seconds: Optional[float] = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message
        self.param = param
        self.request_id = request_id
        self.doc_url = doc_url
        self.next_step = next_step
        self.retry_after_seconds = retry_after_seconds

    @property
    def is_retryable(self) -> bool:
        """Whether sending the same request again, with the same idempotency key, can work: Lurk did not take it and may next time."""
        return self.code in ("rate_limited", "internal", "unavailable")

    def __repr__(self) -> str:
        return f"LurkError(status={self.status}, code={self.code!r}, message={self.message!r}, param={self.param!r})"


class LurkConnectionError(Exception):
    """The request never got an answer: no connection, or a timeout."""


class WebhookVerificationError(Exception):
    """The webhook's signature did not check out, or its timestamp is too old. Do not trust the body."""
