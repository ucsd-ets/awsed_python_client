from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.api_error_result import ApiErrorResult
from ...models.pool_account_result import PoolAccountResult
from ...types import Response


def _get_kwargs(
    pool_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/pools/{poolName}".format(client.base_url, poolName=pool_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ApiErrorResult, PoolAccountResult]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ApiErrorResult.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.OK:
        response_200 = PoolAccountResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ApiErrorResult.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ApiErrorResult, PoolAccountResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pool_name: str,
    *,
    client: Client,
) -> Response[Union[ApiErrorResult, PoolAccountResult]]:
    """List assigned user and team accounts for a pool

    Args:
        pool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResult, PoolAccountResult]]
    """

    kwargs = _get_kwargs(
        pool_name=pool_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pool_name: str,
    *,
    client: Client,
) -> Optional[Union[ApiErrorResult, PoolAccountResult]]:
    """List assigned user and team accounts for a pool

    Args:
        pool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResult, PoolAccountResult]
    """

    return sync_detailed(
        pool_name=pool_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    pool_name: str,
    *,
    client: Client,
) -> Response[Union[ApiErrorResult, PoolAccountResult]]:
    """List assigned user and team accounts for a pool

    Args:
        pool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiErrorResult, PoolAccountResult]]
    """

    kwargs = _get_kwargs(
        pool_name=pool_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pool_name: str,
    *,
    client: Client,
) -> Optional[Union[ApiErrorResult, PoolAccountResult]]:
    """List assigned user and team accounts for a pool

    Args:
        pool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiErrorResult, PoolAccountResult]
    """

    return (
        await asyncio_detailed(
            pool_name=pool_name,
            client=client,
        )
    ).parsed
