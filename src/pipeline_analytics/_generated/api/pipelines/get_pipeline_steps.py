from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.step import Step
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
        "url": "/api/pipelines/{pipeline_id}/steps".format(
            pipeline_id=quote(str(pipeline_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[Step] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Step.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[Step]]:
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
) -> Response[Error | list[Step]]:
    """Step breakdown -- duration ranking, queue/exec split, failure rate, flaky flag

    Args:
        pipeline_id (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[Step]]
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
) -> Error | list[Step] | None:
    """Step breakdown -- duration ranking, queue/exec split, failure rate, flaky flag

    Args:
        pipeline_id (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[Step]
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
) -> Response[Error | list[Step]]:
    """Step breakdown -- duration ranking, queue/exec split, failure rate, flaky flag

    Args:
        pipeline_id (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[Step]]
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
) -> Error | list[Step] | None:
    """Step breakdown -- duration ranking, queue/exec split, failure rate, flaky flag

    Args:
        pipeline_id (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[Step]
    """

    return (
        await asyncio_detailed(
            pipeline_id=pipeline_id,
            client=client,
            window=window,
        )
    ).parsed
