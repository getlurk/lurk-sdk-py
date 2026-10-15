# lurk (Python SDK)

The official Lurk API client for Python 3.11 and newer, with no dependencies.

```bash
pip install getlurk
```

```python
from getlurk import Lurk

lurk = Lurk()  # reads the key from LURK_KEY
receipt = lurk.events.send({"event": "checkin.scanned", "user": "maya@example.com"})
```

Pass the input as a dict (typed by `getlurk.types.EventsSendInput`) or as keywords: `lurk.events.send(event="checkin.scanned", user="maya@example.com")`.

**Keep the key on your server.** A secret key (`lurk_sk_…`) must never reach a browser or an app. Start in a Staging project so nothing reaches
real people until you mean it. See [docs.getlurk.com](https://docs.getlurk.com) for the guides.

## What it does for you

- **Idempotency keys.** Every write that can carry one gets one, made once per call and sent again on every retry. Pass your own with `options=RequestOptions(idempotency_key=...)`.
- **Retries, only where they are safe.** Reads and writes with a key are retried on a connection error, `408` and `5xx`, twice by default, with jittered backoff. A rate-limit answer (`429`) is
  retried after the `Retry-After` it gives (up to 60 seconds; longer raises so you can decide). A write with no key (`api_keys.create`, `webhook_endpoints.create`) is never repeated.
- **Typed errors.** `LurkError` has `status`, `code`, `param`, `request_id`, `doc_url` and `retry_after_seconds`; `LurkConnectionError` means there was no answer.
- **Pages.** `for rule in lurk.paginate("rules.list")` fetches the next page as you go.
- **asyncio.** `AsyncLurk` takes the same arguments and has the same methods, awaited: `await lurk.events.send(...)` and `async for rule in lurk.paginate("rules.list")`. Calls run on a worker thread, so they never block your event loop, and idempotency keys, retries and typed errors are the sync client's.
- **Webhook checks.** `construct_event(body, headers, secret)` verifies a delivery's signature and returns the event.
- **Your own transport.** `Lurk(transport=...)` replaces the HTTP call (a proxy, another library, a test double).

## Versions and changes

The SDK follows [semantic versioning](https://semver.org). The API's changes and the SDK's are in the [changelog](https://docs.getlurk.com/changelog).
Only the latest major version receives fixes.

## Help

Open an [issue](https://github.com/getlurk/lurk-sdk-py/issues) (never include a key; the `request_id` of an error is enough), or read
[CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Licensed under the Apache License 2.0 (see [LICENSE](LICENSE) and [NOTICE](NOTICE)).
