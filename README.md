# pipeline-analytics-sdk-python

[![CI](https://github.com/alrayyes/pipeline-analytics-sdk-python/actions/workflows/ci.yml/badge.svg)](https://github.com/alrayyes/pipeline-analytics-sdk-python/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/pipeline-analytics-sdk.svg)](https://pypi.org/project/pipeline-analytics-sdk/)
[![Codecov](https://codecov.io/gh/alrayyes/pipeline-analytics-sdk-python/graph/badge.svg)](https://codecov.io/gh/alrayyes/pipeline-analytics-sdk-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://alrayyes.github.io/pipeline-analytics-sdk-python/)

A Python client for [pipeline-analytics](https://github.com/alrayyes/pipeline-analytics)'s
REST API, generated from its OpenAPI spec with
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
It saves you from hand-rolling HTTP requests, retries and pagination
against the API yourself.

## Requirements

- Python 3.12 or later.
- A running pipeline-analytics instance.
- A session cookie for that instance (see "Authentication" below) — every
  endpoint except `get_version` and the two webhook receivers needs one.

## Installation

```sh
pip install pipeline-analytics-sdk
```

Pin an exact version in your own `pyproject.toml`/`requirements.txt` rather
than tracking the latest release in anything but a quick trial.

## Authentication

pipeline-analytics authenticates browsers with
[WebAuthn](https://webauthn.guide/), not an API token — there's no headless
credential-grant flow in its spec (a real token flow is requested in
[alrayyes/pipeline-analytics#178](https://github.com/alrayyes/pipeline-analytics/issues/178)),
so this SDK can't log in for you. Get a session cookie by logging into the
dashboard in a browser, opening dev tools, and copying the `session`
cookie's value. Pass it to `PipelineAnalyticsClient` or set
`PIPELINE_ANALYTICS_SESSION` in the environment:

```python
import os
from pipeline_analytics import PipelineAnalyticsClient

client = PipelineAnalyticsClient(
    "https://pipeline-analytics.example.com",
    session_cookie=os.environ.get("PIPELINE_ANALYTICS_SESSION"),
)
```

A session cookie expires the same way it would in a browser; there's
nothing in this SDK to refresh it automatically.

## Usage

`get_version` needs no session and is a good first call to prove the client
reaches the server at all:

```python
from pipeline_analytics import PipelineAnalyticsClient

with PipelineAnalyticsClient("https://pipeline-analytics.example.com") as client:
    version = client.get_version()
    print("server version:", version.version)
```

Listing tracked repos needs a session, and demonstrates the pagination
iterator and error handling:

```python
import os
from pipeline_analytics import APIError, PipelineAnalyticsClient, iter_repos

client = PipelineAnalyticsClient(
    "https://pipeline-analytics.example.com",
    session_cookie=os.environ.get("PIPELINE_ANALYTICS_SESSION"),
)

try:
    for repo in iter_repos(client.raw):
        print(repo.identifier, repo.ingestion_status)
except APIError as e:
    if e.status_code == 401:
        raise SystemExit("session cookie expired or invalid") from e
    raise
```

An async equivalent, `aiter_repos`, is available for `async`/`await` code.

Every other operation follows the generated client's pattern —
`pipeline_analytics._generated.api.<tag>.<operation>.sync_detailed(client=client.raw, ...)`
(or `asyncio_detailed` for async) returns a typed `Response` whose `.parsed`
field holds the decoded body for a documented status code. Use
`decode_error` to turn any error response into a `pipeline_analytics.APIError`
uniformly:

```python
from pipeline_analytics import decode_error
from pipeline_analytics._generated.api.repos import get_repo_usage

response = get_repo_usage.sync_detailed(client=client.raw, repo_id=repo_id)
if error := decode_error(response):
    raise error
usage = response.parsed
```

The client retries a `429` or `5xx` response with exponential backoff and
jitter (honoring a server-sent `Retry-After`), and never retries any other
`4xx`. Tune it by passing a `pipeline_analytics.RetryConfig` as `retry=`, or
swap the underlying `httpx.Client`/`httpx.AsyncClient` entirely with
`httpx_client=`/`httpx_async_client=`.

## Regenerating the client

See [CONTRIBUTING.md](CONTRIBUTING.md) — the generated code is pinned to a
specific pipeline-analytics commit and shouldn't drift from it silently.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for building, testing and the release
process.

## License

[MIT](LICENSE) — a permissive license for the client, independent of
pipeline-analytics' own AGPL-3.0.
