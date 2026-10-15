"""The client: keys, retries, errors and timeouts. The methods on it are generated; this part is written by hand."""

from __future__ import annotations

import json
import os
import random
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any, Callable, Dict, Iterator, Mapping, NamedTuple, Optional

from ._generated.operations import OPERATIONS
from ._generated.resources import Resources
from .errors import LurkConnectionError, LurkError
from .options import RequestOptions

SDK_VERSION = "0.2.1"
DEFAULT_BASE_URL = "https://api.getlurk.com"
# If the API asks for a longer wait than this, the call fails with ``rate_limited`` instead of hanging.
MAX_RETRY_AFTER_SECONDS = 60.0


class Response(NamedTuple):
    status: int
    headers: Mapping[str, str]
    body: bytes


# A transport sends one request and returns the answer, or raises OSError (including TimeoutError) when there is none.
# Replace it to use another HTTP library, a proxy, or a test double.
Transport = Callable[[str, str, Mapping[str, str], Optional[bytes], float], Response]


def urllib_transport(
    method: str, url: str, headers: Mapping[str, str], body: Optional[bytes], timeout: float
) -> Response:
    request = urllib.request.Request(url, data=body, method=method, headers=dict(headers))
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 (https URLs only, from the client's base_url)
            return Response(response.status, {k.lower(): v for k, v in response.headers.items()}, response.read())
    except urllib.error.HTTPError as error:
        return Response(error.code, {k.lower(): v for k, v in error.headers.items()}, error.read())
    except urllib.error.URLError as error:
        raise OSError(str(error.reason)) from error


def _backoff(attempt: int) -> float:
    """Half a second, doubling, never more than eight, with jitter so clients do not retry in step."""
    return min(8.0, 0.5 * 2**attempt) * (0.5 + random.random() / 2)


class Lurk(Resources):
    """The Lurk API. Every method is generated from the OpenAPI file, so it matches the API exactly.

    >>> lurk = Lurk()  # reads the key from LURK_KEY
    >>> receipt = lurk.events.send({"event": "checkin.scanned", "user": "maya@example.com"})
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        max_retries: int = 2,
        timeout: float = 30.0,
        transport: Optional[Transport] = None,
        sleep: Optional[Callable[[float], None]] = None,
    ) -> None:
        key = api_key if api_key is not None else os.environ.get("LURK_KEY")
        if not key or not key.startswith("lurk_sk_"):
            raise ValueError(
                "Lurk: no project key. Pass api_key or set LURK_KEY to a key that starts with lurk_sk_."
            )
        self._api_key = key
        self._base_url = base_url.rstrip("/")
        self._max_retries = max_retries
        self._timeout = timeout
        self._transport = transport or urllib_transport
        self._sleep = sleep or time.sleep
        super().__init__(self._call)

    def __repr__(self) -> str:
        return f"Lurk(base_url={self._base_url!r})"  # never the key

    def paginate(
        self,
        operation: str,
        params: Optional[Mapping[str, Any]] = None,
        options: Optional[RequestOptions] = None,
    ) -> Iterator[Any]:
        """Every item of a paged list, fetching the next page as you go: ``for rule in lurk.paginate("rules.list")``."""
        query: Dict[str, Any] = dict(params or {})
        while True:
            page = self._call(operation, query, options)
            yield from page["data"]
            if not page.get("has_more") or not page.get("next_cursor"):
                return
            query["cursor"] = page["next_cursor"]

    def _call(
        self, operation: str, params: Optional[Mapping[str, Any]], options: Optional[RequestOptions] = None
    ) -> Any:
        op = OPERATIONS[operation]
        options = options or RequestOptions()
        rest: Dict[str, Any] = dict(params or {})

        path = op.path
        for name in op.path_params:
            path = path.replace("{" + name + "}", urllib.parse.quote(str(rest.pop(name)), safe=""))
        query = {}
        for name in op.query_params:
            value = rest.pop(name, None)
            if value is not None:
                query[name] = str(value).lower() if isinstance(value, bool) else str(value)

        # One key per call, reused on every retry: that is what makes a retry safe.
        key: Optional[str] = None
        if op.idempotency is not None:
            existing = rest.get("idempotency_key")
            key = options.idempotency_key or (existing if isinstance(existing, str) else None) or str(uuid.uuid4())
            if op.idempotency == "body":
                rest["idempotency_key"] = key

        headers: Dict[str, str] = {
            "authorization": f"Bearer {self._api_key}",
            "accept": "application/json",
            "x-lurk-sdk": f"python/{SDK_VERSION}",
            **{k.lower(): v for k, v in (options.headers or {}).items()},
        }
        if op.idempotency == "header" and key:
            headers["idempotency-key"] = key
        body: Optional[bytes] = None
        if op.body:
            headers["content-type"] = "application/json"
            body = json.dumps(rest).encode()
        url = f"{self._base_url}{path}" + (f"?{urllib.parse.urlencode(query)}" if query else "")

        # A retry is safe when repeating the call cannot do the thing twice: reads, and writes that carry a key.
        # A rate-limit answer is always safe to retry, because the API refuses before it does anything.
        safe = op.method == "GET" or op.idempotency is not None
        max_retries = options.max_retries if options.max_retries is not None else self._max_retries
        timeout = options.timeout if options.timeout is not None else self._timeout

        attempt = 0
        while True:
            try:
                response = self._transport(op.method, url, headers, body, timeout)
            except OSError as error:
                if safe and attempt < max_retries:
                    self._sleep(_backoff(attempt))
                    attempt += 1
                    continue
                message = "The API did not answer in time." if isinstance(error, TimeoutError) else "Could not reach the API."
                raise LurkConnectionError(message) from error

            if 200 <= response.status < 300:
                return _parse(response)

            error = _to_error(response)
            retryable = response.status == 429 or (safe and (response.status == 408 or response.status >= 500))
            if retryable and attempt < max_retries:
                asked = error.retry_after_seconds
                if asked is None or asked <= MAX_RETRY_AFTER_SECONDS:
                    self._sleep(asked if asked is not None else _backoff(attempt))
                    attempt += 1
                    continue
            raise error


def _parse(response: Response) -> Any:
    if response.status == 204 or not response.body:
        return None
    try:
        return json.loads(response.body)
    except ValueError as error:
        raise LurkError(
            status=response.status,
            code="internal",
            message="The API answered with something that isn't JSON.",
            request_id=response.headers.get("request-id"),
        ) from error


def _to_error(response: Response) -> LurkError:
    request_id = response.headers.get("request-id")
    try:
        retry_after = float(response.headers.get("retry-after", ""))
    except ValueError:
        retry_after = None
    retry_after_seconds = retry_after if retry_after is not None and retry_after > 0 else None
    try:
        error = json.loads(response.body)["error"]
        return LurkError(
            status=response.status,
            code=error["code"],
            message=error["message"],
            param=error.get("param"),
            request_id=error.get("request_id") or request_id,
            doc_url=error.get("doc_url"),
            next_step=error.get("next_step"),
            retry_after_seconds=retry_after_seconds,
        )
    except (ValueError, KeyError, TypeError):
        # Not our envelope: a proxy or an outage in front of the API.
        return LurkError(
            status=response.status,
            code="rate_limited" if response.status == 429 else "internal",
            message=f"The API answered {response.status}.",
            request_id=request_id,
            retry_after_seconds=retry_after_seconds,
        )
