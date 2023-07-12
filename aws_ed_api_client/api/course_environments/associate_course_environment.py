from http import HTTPStatus
from typing import Any, Dict, Optional, cast

import httpx

from ... import errors
from ...client import Client
from ...models.associate_course_environment_request_body import AssociateCourseEnvironmentRequestBody
from ...types import Response


def _get_kwargs(
    course: str,
    *,
    client: Client,
    json_body: AssociateCourseEnvironmentRequestBody,
) -> Dict[str, Any]:
    url = "{}/api/courses/{course}/environments".format(client.base_url, course=course)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[str]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(str, response.json())
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(str, response.json())
        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course: str,
    *,
    client: Client,
    json_body: AssociateCourseEnvironmentRequestBody,
) -> Response[str]:
    """Associate a course with an environment

    Args:
        course (str):
        json_body (AssociateCourseEnvironmentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        course=course,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course: str,
    *,
    client: Client,
    json_body: AssociateCourseEnvironmentRequestBody,
) -> Optional[str]:
    """Associate a course with an environment

    Args:
        course (str):
        json_body (AssociateCourseEnvironmentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        course=course,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    course: str,
    *,
    client: Client,
    json_body: AssociateCourseEnvironmentRequestBody,
) -> Response[str]:
    """Associate a course with an environment

    Args:
        course (str):
        json_body (AssociateCourseEnvironmentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        course=course,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course: str,
    *,
    client: Client,
    json_body: AssociateCourseEnvironmentRequestBody,
) -> Optional[str]:
    """Associate a course with an environment

    Args:
        course (str):
        json_body (AssociateCourseEnvironmentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            course=course,
            client=client,
            json_body=json_body,
        )
    ).parsed
