from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.branch_list import BranchList
from ...models.error import Error
from ...models.forge import Forge
from ...models.list_branches_window import ListBranchesWindow
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    window: ListBranchesWindow | Unset = ListBranchesWindow.VALUE_1,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["repoId"] = repo_id

    json_forge: str | Unset = UNSET
    if not isinstance(forge, Unset):
        json_forge = forge.value

    params["forge"] = json_forge

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/branches",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BranchList | Error | None:
    if response.status_code == 200:
        response_200 = BranchList.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BranchList | Error]:
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
    window: ListBranchesWindow | Unset = ListBranchesWindow.VALUE_1,

) -> Response[BranchList | Error]:
    """ The branches that have runs in a window, busiest first

     What a branch selector offers: every branch with at least one run that started in the trailing
    window, with how many. A run with no recorded branch is not a branch. Ordered by `runCount`
    descending, then name. Pass a name as `branch` to the failure insights, the run list or the flaky
    steps to scope them.

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        window (ListBranchesWindow | Unset):  Default: ListBranchesWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchList | Error]
     """


    kwargs = _get_kwargs(
        repo_id=repo_id,
forge=forge,
window=window,

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
    window: ListBranchesWindow | Unset = ListBranchesWindow.VALUE_1,

) -> BranchList | Error | None:
    """ The branches that have runs in a window, busiest first

     What a branch selector offers: every branch with at least one run that started in the trailing
    window, with how many. A run with no recorded branch is not a branch. Ordered by `runCount`
    descending, then name. Pass a name as `branch` to the failure insights, the run list or the flaky
    steps to scope them.

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        window (ListBranchesWindow | Unset):  Default: ListBranchesWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchList | Error
     """


    return sync_detailed(
        client=client,
repo_id=repo_id,
forge=forge,
window=window,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    window: ListBranchesWindow | Unset = ListBranchesWindow.VALUE_1,

) -> Response[BranchList | Error]:
    """ The branches that have runs in a window, busiest first

     What a branch selector offers: every branch with at least one run that started in the trailing
    window, with how many. A run with no recorded branch is not a branch. Ordered by `runCount`
    descending, then name. Pass a name as `branch` to the failure insights, the run list or the flaky
    steps to scope them.

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        window (ListBranchesWindow | Unset):  Default: ListBranchesWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BranchList | Error]
     """


    kwargs = _get_kwargs(
        repo_id=repo_id,
forge=forge,
window=window,

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
    window: ListBranchesWindow | Unset = ListBranchesWindow.VALUE_1,

) -> BranchList | Error | None:
    """ The branches that have runs in a window, busiest first

     What a branch selector offers: every branch with at least one run that started in the trailing
    window, with how many. A run with no recorded branch is not a branch. Ordered by `runCount`
    descending, then name. Pass a name as `branch` to the failure insights, the run list or the flaky
    steps to scope them.

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        window (ListBranchesWindow | Unset):  Default: ListBranchesWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BranchList | Error
     """


    return (await asyncio_detailed(
        client=client,
repo_id=repo_id,
forge=forge,
window=window,

    )).parsed
