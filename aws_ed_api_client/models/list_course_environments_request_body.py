from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication import Authentication


T = TypeVar("T", bound="ListCourseEnvironmentsRequestBody")


@attr.s(auto_attribs=True)
class ListCourseEnvironmentsRequestBody:
    """
    Attributes:
        status (Union[Unset, str]):
        subject (Union[Unset, str]):
        term (Union[Unset, str]):
        authentication (Union[Unset, Authentication]):
    """

    status: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    term: Union[Unset, str] = UNSET
    authentication: Union[Unset, "Authentication"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        subject = self.subject
        term = self.term
        authentication: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if subject is not UNSET:
            field_dict["subject"] = subject
        if term is not UNSET:
            field_dict["term"] = term
        if authentication is not UNSET:
            field_dict["authentication"] = authentication

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authentication import Authentication

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        subject = d.pop("subject", UNSET)

        term = d.pop("term", UNSET)

        _authentication = d.pop("authentication", UNSET)
        authentication: Union[Unset, Authentication]
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = Authentication.from_dict(_authentication)

        list_course_environments_request_body = cls(
            status=status,
            subject=subject,
            term=term,
            authentication=authentication,
        )

        list_course_environments_request_body.additional_properties = d
        return list_course_environments_request_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
