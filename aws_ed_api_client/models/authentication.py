from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Authentication")


@attr.s(auto_attribs=True)
class Authentication:
    """
    Attributes:
        ta (Union[Unset, bool]):
        username (Union[Unset, str]):
        admin (Union[Unset, bool]):
        student (Union[Unset, bool]):
    """

    ta: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    admin: Union[Unset, bool] = UNSET
    student: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ta = self.ta
        username = self.username
        admin = self.admin
        student = self.student

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ta is not UNSET:
            field_dict["ta"] = ta
        if username is not UNSET:
            field_dict["username"] = username
        if admin is not UNSET:
            field_dict["admin"] = admin
        if student is not UNSET:
            field_dict["student"] = student

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ta = d.pop("ta", UNSET)

        username = d.pop("username", UNSET)

        admin = d.pop("admin", UNSET)

        student = d.pop("student", UNSET)

        authentication = cls(
            ta=ta,
            username=username,
            admin=admin,
            student=student,
        )

        authentication.additional_properties = d
        return authentication

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
