"""Unit tests for the hand-written error decoding
(rules/sdk-generation.md's "unit-test only the hand-written parts")."""

from __future__ import annotations

import httpx

from pipeline_analytics.errors import APIError, decode_error


def _response(status_code: int, body: bytes = b"", headers: dict[str, str] | None = None) -> httpx.Response:
    return httpx.Response(status_code, content=body, headers=headers or {})


def test_decode_error_returns_none_below_400() -> None:
    assert decode_error(_response(200)) is None
    assert decode_error(_response(399)) is None


def test_decode_error_treats_400_as_an_error() -> None:
    # The exact boundary: 400 is an error, 399 (above) is not.
    error = decode_error(_response(400, b'{"code": "bad_request", "message": "nope"}'))
    assert error is not None
    assert error.status_code == 400


def test_decode_error_parses_code_and_message() -> None:
    body = b'{"code": "not_found", "message": "repo not found"}'
    error = decode_error(_response(404, body))

    assert isinstance(error, APIError)
    assert error.status_code == 404
    assert error.code == "not_found"
    assert error.message == "repo not found"
    assert error.request_id is None


def test_decode_error_reads_request_id_header() -> None:
    body = b'{"code": "internal", "message": "boom"}'
    error = decode_error(_response(500, body, headers={"X-Request-Id": "req-123"}))

    assert error is not None
    assert error.request_id == "req-123"


def test_decode_error_tolerates_non_json_body() -> None:
    error = decode_error(_response(502, b"<html>Bad Gateway</html>"))

    assert error is not None
    assert error.status_code == 502
    assert error.code == ""
    assert error.message == ""


def test_decode_error_defaults_code_when_missing() -> None:
    error = decode_error(_response(404, b'{"message": "not found"}'))
    assert error is not None
    assert error.code == ""
    assert error.message == "not found"


def test_decode_error_defaults_message_when_missing() -> None:
    error = decode_error(_response(404, b'{"code": "not_found"}'))
    assert error is not None
    assert error.code == "not_found"
    assert error.message == ""


def test_api_error_str_with_and_without_request_id() -> None:
    without = APIError(404, "not_found", "nope")
    assert str(without) == "pipeline-analytics: 404 not_found: nope"

    with_id = APIError(404, "not_found", "nope", request_id="req-1")
    assert str(with_id) == "pipeline-analytics: 404 not_found: nope (request req-1)"


def test_api_error_args_reflect_str() -> None:
    error = APIError(404, "not_found", "nope")
    assert error.args == (str(error),)
