from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.import_roster_result_json import ImportRosterResultJson
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: str,
    dry_run: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/api/enrollments".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["dryRun"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ImportRosterResultJson, str]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(str, response.json())
        return response_403
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ImportRosterResultJson.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.OK:
        response_200 = ImportRosterResultJson.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ImportRosterResultJson, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: str,
    dry_run: Union[Unset, None, bool] = False,
) -> Response[Union[ImportRosterResultJson, str]]:
    """importEnrollments

    Args:
        dry_run (Union[Unset, None, bool]):
        json_body (str): CSV

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImportRosterResultJson, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        dry_run=dry_run,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: str,
    dry_run: Union[Unset, None, bool] = False,
) -> Optional[Union[ImportRosterResultJson, str]]:
    """importEnrollments

    Args:
        dry_run (Union[Unset, None, bool]):
        json_body (str): CSV

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImportRosterResultJson, str]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: str,
    dry_run: Union[Unset, None, bool] = False,
) -> Response[Union[ImportRosterResultJson, str]]:
    """importEnrollments

    Args:
        dry_run (Union[Unset, None, bool]):
        json_body (str): CSV

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImportRosterResultJson, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        dry_run=dry_run,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: str,
    dry_run: Union[Unset, None, bool] = False,
) -> Optional[Union[ImportRosterResultJson, str]]:
    """importEnrollments

    Args:
        dry_run (Union[Unset, None, bool]):
        json_body (str): CSV

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImportRosterResultJson, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            dry_run=dry_run,
        )
    ).parsed
