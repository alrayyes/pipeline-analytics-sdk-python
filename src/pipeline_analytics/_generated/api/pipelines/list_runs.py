from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.forge import Forge
from ...models.list_runs_status import ListRunsStatus
from ...models.run_list import RunList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    status: ListRunsStatus | Unset = ListRunsStatus.ALL,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["repoId"] = repo_id

    json_forge: str | Unset = UNSET
    if not isinstance(forge, Unset):
        json_forge = forge.value

    params["forge"] = json_forge

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/runs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RunList | None:
    if response.status_code == 200:
        response_200 = RunList.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | RunList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    status: ListRunsStatus | Unset = ListRunsStatus.ALL,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> Response[Error | RunList]:
    """ A page of runs, newest first, each with its steps for a stage progression bar

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        status (ListRunsStatus | Unset):  Default: ListRunsStatus.ALL.
        limit (int | Unset):
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RunList]
     """


    kwargs = _get_kwargs(
        repo_id=repo_id,
forge=forge,
status=status,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    status: ListRunsStatus | Unset = ListRunsStatus.ALL,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> Error | RunList | None:
    """ A page of runs, newest first, each with its steps for a stage progression bar

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        status (ListRunsStatus | Unset):  Default: ListRunsStatus.ALL.
        limit (int | Unset):
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RunList
     """


    return sync_detailed(
        client=client,
repo_id=repo_id,
forge=forge,
status=status,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    status: ListRunsStatus | Unset = ListRunsStatus.ALL,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> Response[Error | RunList]:
    """ A page of runs, newest first, each with its steps for a stage progression bar

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        status (ListRunsStatus | Unset):  Default: ListRunsStatus.ALL.
        limit (int | Unset):
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RunList]
     """


    kwargs = _get_kwargs(
        repo_id=repo_id,
forge=forge,
status=status,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    status: ListRunsStatus | Unset = ListRunsStatus.ALL,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> Error | RunList | None:
    """ A page of runs, newest first, each with its steps for a stage progression bar

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        status (ListRunsStatus | Unset):  Default: ListRunsStatus.ALL.
        limit (int | Unset):
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RunList
     """


    return (await asyncio_detailed(
        client=client,
repo_id=repo_id,
forge=forge,
status=status,
limit=limit,
offset=offset,

    )).parsed
