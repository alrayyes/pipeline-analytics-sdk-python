from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.forge import Forge
from ...models.list_repo_identifiers_response_200 import ListRepoIdentifiersResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    forge: Forge,
    forgejo_instance_url: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_forge = forge.value
    params["forge"] = json_forge

    params["forgejoInstanceUrl"] = forgejo_instance_url


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/repos/identifiers",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListRepoIdentifiersResponse200 | None:
    if response.status_code == 200:
        response_200 = ListRepoIdentifiersResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListRepoIdentifiersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge,
    forgejo_instance_url: str | Unset = UNSET,

) -> Response[Error | ListRepoIdentifiersResponse200]:
    """ List every tracked identifier for a forge, unpaginated

     Backs Discover's "already tracked" check, which needs to see every tracked repo regardless of how
    many are tracked, not just whatever page a paginated GET /api/repos happens to be showing (see
    forge-ingestion/spec.md's "Repo tracking registration").

    Args:
        forge (Forge):
        forgejo_instance_url (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListRepoIdentifiersResponse200]
     """


    kwargs = _get_kwargs(
        forge=forge,
forgejo_instance_url=forgejo_instance_url,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge,
    forgejo_instance_url: str | Unset = UNSET,

) -> Error | ListRepoIdentifiersResponse200 | None:
    """ List every tracked identifier for a forge, unpaginated

     Backs Discover's "already tracked" check, which needs to see every tracked repo regardless of how
    many are tracked, not just whatever page a paginated GET /api/repos happens to be showing (see
    forge-ingestion/spec.md's "Repo tracking registration").

    Args:
        forge (Forge):
        forgejo_instance_url (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListRepoIdentifiersResponse200
     """


    return sync_detailed(
        client=client,
forge=forge,
forgejo_instance_url=forgejo_instance_url,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge,
    forgejo_instance_url: str | Unset = UNSET,

) -> Response[Error | ListRepoIdentifiersResponse200]:
    """ List every tracked identifier for a forge, unpaginated

     Backs Discover's "already tracked" check, which needs to see every tracked repo regardless of how
    many are tracked, not just whatever page a paginated GET /api/repos happens to be showing (see
    forge-ingestion/spec.md's "Repo tracking registration").

    Args:
        forge (Forge):
        forgejo_instance_url (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListRepoIdentifiersResponse200]
     """


    kwargs = _get_kwargs(
        forge=forge,
forgejo_instance_url=forgejo_instance_url,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge,
    forgejo_instance_url: str | Unset = UNSET,

) -> Error | ListRepoIdentifiersResponse200 | None:
    """ List every tracked identifier for a forge, unpaginated

     Backs Discover's "already tracked" check, which needs to see every tracked repo regardless of how
    many are tracked, not just whatever page a paginated GET /api/repos happens to be showing (see
    forge-ingestion/spec.md's "Repo tracking registration").

    Args:
        forge (Forge):
        forgejo_instance_url (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListRepoIdentifiersResponse200
     """


    return (await asyncio_detailed(
        client=client,
forge=forge,
forgejo_instance_url=forgejo_instance_url,

    )).parsed
