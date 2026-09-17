"""A Python client for pipeline-analytics's REST API
(github.com/alrayyes/pipeline-analytics), generated from its OpenAPI spec
with openapi-python-client.

Every operation except ``get_version`` and the two webhook receivers
requires an authenticated session -- see :class:`PipelineAnalyticsClient`
for the WebAuthn-only auth story.
"""

from .client import SESSION_COOKIE_ENV_VAR, PipelineAnalyticsClient
from .errors import APIError, decode_error
from .pagination import DEFAULT_PAGE_SIZE, aiter_repos, iter_repos
from .retry import DEFAULT_RETRY_CONFIG, AsyncRetryTransport, RetryConfig, RetryTransport

__all__ = [
    "DEFAULT_PAGE_SIZE",
    "DEFAULT_RETRY_CONFIG",
    "SESSION_COOKIE_ENV_VAR",
    "APIError",
    "AsyncRetryTransport",
    "PipelineAnalyticsClient",
    "RetryConfig",
    "RetryTransport",
    "aiter_repos",
    "decode_error",
    "iter_repos",
]
