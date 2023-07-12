from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.list_courses_result_json import ListCoursesResultJson
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    tag: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/courses".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["tag"] = tag

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ListCoursesResultJson, str]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(str, response.json())
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ListCoursesResultJson.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ListCoursesResultJson.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.OK:
        response_200 = ListCoursesResultJson.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ListCoursesResultJson, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    tag: Union[Unset, None, str] = UNSET,
) -> Response[Union[ListCoursesResultJson, str]]:
    """List active courses

    Args:
        tag (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListCoursesResultJson, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        tag=tag,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    tag: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ListCoursesResultJson, str]]:
    """List active courses

    Args:
        tag (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListCoursesResultJson, str]
    """

    return sync_detailed(
        client=client,
        tag=tag,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    tag: Union[Unset, None, str] = UNSET,
) -> Response[Union[ListCoursesResultJson, str]]:
    """List active courses

    Args:
        tag (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListCoursesResultJson, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        tag=tag,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    tag: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ListCoursesResultJson, str]]:
    """List active courses

    Args:
        tag (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListCoursesResultJson, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            tag=tag,
        )
    ).parsed
