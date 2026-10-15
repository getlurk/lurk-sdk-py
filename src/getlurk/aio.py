"""An async client with the same shape as the sync one: ``await lurk.events.send(...)`` and ``async for rule in lurk.paginate(...)``.

It runs the sync client's calls on a worker thread (``asyncio.to_thread``), so a call never blocks the event loop and the behaviour that
matters (idempotency keys, retries only where safe, typed errors) is exactly the sync client's, written once. A native ``asyncio``
transport can replace the thread later without changing anything you call.
"""

from __future__ import annotations

import asyncio
import functools
from typing import Any, AsyncIterator, Callable, Mapping, Optional

from .client import Lurk
from .options import RequestOptions


class _AsyncResource:
    """``lurk.events``, ``lurk.rules`` and so on: each method is the sync one, awaited."""

    def __init__(self, resource: Any) -> None:
        self._resource = resource

    def __getattr__(self, name: str) -> Callable[..., Any]:
        method = getattr(self._resource, name)
        if not callable(method):
            raise AttributeError(name)

        @functools.wraps(method)
        async def call(*args: Any, **kwargs: Any) -> Any:
            return await asyncio.to_thread(method, *args, **kwargs)

        return call


class AsyncLurk:
    """The Lurk API for ``asyncio``. Takes the same arguments as :class:`getlurk.Lurk`."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._sync = Lurk(*args, **kwargs)

    def __getattr__(self, name: str) -> _AsyncResource:
        if name.startswith("_"):
            raise AttributeError(name)
        return _AsyncResource(getattr(self._sync, name))

    def __repr__(self) -> str:
        return f"Async{self._sync!r}"  # never the key

    async def paginate(
        self,
        operation: str,
        params: Optional[Mapping[str, Any]] = None,
        options: Optional[RequestOptions] = None,
    ) -> AsyncIterator[Any]:
        """Every item of a paged list, fetching the next page as you go: ``async for rule in lurk.paginate("rules.list")``."""
        query = dict(params or {})
        while True:
            page = await asyncio.to_thread(self._sync._call, operation, query, options)
            for item in page["data"]:
                yield item
            if not page.get("has_more") or not page.get("next_cursor"):
                return
            query["cursor"] = page["next_cursor"]
