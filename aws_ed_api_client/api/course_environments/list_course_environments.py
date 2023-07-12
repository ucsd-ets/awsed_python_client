from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.list_course_environments_request_body import ListCourseEnvironmentsRequestBody
from ...models.list_course_environments_result_json import ListCourseEnvironmentsResultJson
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    request: "ListCourseEnvironmentsRequestBody",
) -> Dict[str, Any]:
    url = "{}/api/course-environments".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_request = request.to_dict()

    params.update(json_request)

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ListCourseEnvironmentsResultJson, str]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(str, response.json())
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ListCourseEnvironmentsResultJson.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = ListCourseEnvironmentsResultJson.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ListCourseEnvironmentsResultJson, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    request: "ListCourseEnvironmentsRequestBody",
) -> Response[Union[ListCourseEnvironmentsResultJson, str]]:
    """List course environments

    Args:
        request (ListCourseEnvironmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListCourseEnvironmentsResultJson, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        request=request,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    request: "ListCourseEnvironmentsRequestBody",
) -> Optional[Union[ListCourseEnvironmentsResultJson, str]]:
    """List course environments

    Args:
        request (ListCourseEnvironmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListCourseEnvironmentsResultJson, str]
    """

    return sync_detailed(
        client=client,
        request=request,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    request: "ListCourseEnvironmentsRequestBody",
) -> Response[Union[ListCourseEnvironmentsResultJson, str]]:
    """List course environments

    Args:
        request (ListCourseEnvironmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListCourseEnvironmentsResultJson, str]]
    """

    kwargs = _get_kwargs(
        client=client,
        request=request,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    request: "ListCourseEnvironmentsRequestBody",
) -> Optional[Union[ListCourseEnvironmentsResultJson, str]]:
    """List course environments

    Args:
        request (ListCourseEnvironmentsRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListCourseEnvironmentsResultJson, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            request=request,
        )
    ).parsed
