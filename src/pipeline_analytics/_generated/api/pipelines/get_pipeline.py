from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pipeline_detail import PipelineDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pipeline_id: str,
    *,
    window: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["window"] = window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/pipelines/{pipeline_id}".format(
            pipeline_id=quote(str(pipeline_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PipelineDetail | None:
    if response.status_code == 200:
        response_200 = PipelineDetail.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PipelineDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pipeline_id: str,
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
) -> Response[Error | PipelineDetail]:
    """Duration and failure-rate trend for one pipeline

    Args:
        pipeline_id (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineDetail]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        window=window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pipeline_id: str,
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
) -> Error | PipelineDetail | None:
    """Duration and failure-rate trend for one pipeline

    Args:
        pipeline_id (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineDetail
    """

    return sync_detailed(
        pipeline_id=pipeline_id,
        client=client,
        window=window,
    ).parsed


async def asyncio_detailed(
    pipeline_id: str,
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
) -> Response[Error | PipelineDetail]:
    """Duration and failure-rate trend for one pipeline

    Args:
        pipeline_id (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PipelineDetail]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        window=window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pipeline_id: str,
    *,
    client: AuthenticatedClient | Client,
    window: str | Unset = UNSET,
) -> Error | PipelineDetail | None:
    """Duration and failure-rate trend for one pipeline

    Args:
        pipeline_id (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PipelineDetail
    """

    return (
        await asyncio_detailed(
            pipeline_id=pipeline_id,
            client=client,
            window=window,
        )
    ).parsed
