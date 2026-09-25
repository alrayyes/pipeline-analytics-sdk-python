from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.mcp_endpoint_body import McpEndpointBody
from ...models.mcp_endpoint_response_200 import McpEndpointResponse200
from typing import cast



def _get_kwargs(
    *,
    body: McpEndpointBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/mcp",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | McpEndpointResponse200 | None:
    if response.status_code == 200:
        response_200 = McpEndpointResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | McpEndpointResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: McpEndpointBody,

) -> Response[Error | McpEndpointResponse200]:
    """ MCP server (Streamable HTTP transport)

     Serves an MCP server over the Streamable HTTP transport (mcp-endpoint/spec.md), exposing the same
    pipeline health, trend, flaky-step, and usage data as read-only MCP tools. The request and response
    bodies are MCP's own JSON-RPC 2.0 envelope, not a REST payload -- this entry documents the endpoint
    for discoverability and auth, not for REST client generation.

    Args:
        body (McpEndpointBody): An MCP JSON-RPC 2.0 request or notification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | McpEndpointResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: McpEndpointBody,

) -> Error | McpEndpointResponse200 | None:
    """ MCP server (Streamable HTTP transport)

     Serves an MCP server over the Streamable HTTP transport (mcp-endpoint/spec.md), exposing the same
    pipeline health, trend, flaky-step, and usage data as read-only MCP tools. The request and response
    bodies are MCP's own JSON-RPC 2.0 envelope, not a REST payload -- this entry documents the endpoint
    for discoverability and auth, not for REST client generation.

    Args:
        body (McpEndpointBody): An MCP JSON-RPC 2.0 request or notification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | McpEndpointResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: McpEndpointBody,

) -> Response[Error | McpEndpointResponse200]:
    """ MCP server (Streamable HTTP transport)

     Serves an MCP server over the Streamable HTTP transport (mcp-endpoint/spec.md), exposing the same
    pipeline health, trend, flaky-step, and usage data as read-only MCP tools. The request and response
    bodies are MCP's own JSON-RPC 2.0 envelope, not a REST payload -- this entry documents the endpoint
    for discoverability and auth, not for REST client generation.

    Args:
        body (McpEndpointBody): An MCP JSON-RPC 2.0 request or notification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | McpEndpointResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: McpEndpointBody,

) -> Error | McpEndpointResponse200 | None:
    """ MCP server (Streamable HTTP transport)

     Serves an MCP server over the Streamable HTTP transport (mcp-endpoint/spec.md), exposing the same
    pipeline health, trend, flaky-step, and usage data as read-only MCP tools. The request and response
    bodies are MCP's own JSON-RPC 2.0 envelope, not a REST payload -- this entry documents the endpoint
    for discoverability and auth, not for REST client generation.

    Args:
        body (McpEndpointBody): An MCP JSON-RPC 2.0 request or notification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | McpEndpointResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
