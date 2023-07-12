from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserResultJson")


@attr.s(auto_attribs=True)
class UserResultJson:
    """
    Attributes:
        username (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        uid (Union[Unset, int]):
        enrollments (Union[Unset, List[str]]):
    """

    username: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    uid: Union[Unset, int] = UNSET
    enrollments: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        uid = self.uid
        enrollments: Union[Unset, List[str]] = UNSET
        if not isinstance(self.enrollments, Unset):
            enrollments = self.enrollments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if uid is not UNSET:
            field_dict["uid"] = uid
        if enrollments is not UNSET:
            field_dict["enrollments"] = enrollments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        uid = d.pop("uid", UNSET)

        enrollments = cast(List[str], d.pop("enrollments", UNSET))

        user_result_json = cls(
            username=username,
            first_name=first_name,
            last_name=last_name,
            uid=uid,
            enrollments=enrollments,
        )

        user_result_json.additional_properties = d
        return user_result_json

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
