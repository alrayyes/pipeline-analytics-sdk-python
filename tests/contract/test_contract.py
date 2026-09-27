"""Runs the client against a Prism mock server generated from
pipeline-analytics's own pinned spec (see .github/workflows/ci.yml's
"contract" job) — never a hand-rolled stub. See
rules/sdk-generation.md's "Testing against the spec, not a hand-written
stub": this proves the client's requests/responses conform to the spec,
nothing more.
"""

from __future__ import annotations

import asyncio
import os

import pytest

from pipeline_analytics import PipelineAnalyticsClient

pytestmark = pytest.mark.contract


@pytest.fixture
def client() -> PipelineAnalyticsClient:
    base_url = os.environ.get("PIPELINE_ANALYTICS_BASE_URL")
    if not base_url:
        pytest.fail("PIPELINE_ANALYTICS_BASE_URL must point at a running Prism mock (see ci.yml's contract job)")
    return PipelineAnalyticsClient(base_url, session_cookie="prism-does-not-check-this")


def test_get_version(client: PipelineAnalyticsClient) -> None:
    client.get_version()


def test_aget_version(client: PipelineAnalyticsClient) -> None:
    asyncio.run(client.aget_version())
