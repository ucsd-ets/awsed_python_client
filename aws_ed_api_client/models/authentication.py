from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Authentication")


@attr.s(auto_attribs=True)
class Authentication:
    """
    Attributes:
        admin (Union[Unset, bool]):
        username (Union[Unset, str]):
        student (Union[Unset, bool]):
        ta (Union[Unset, bool]):
    """

    admin: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    student: Union[Unset, bool] = UNSET
    ta: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin = self.admin
        username = self.username
        student = self.student
        ta = self.ta

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if username is not UNSET:
            field_dict["username"] = username
        if student is not UNSET:
            field_dict["student"] = student
        if ta is not UNSET:
            field_dict["ta"] = ta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        admin = d.pop("admin", UNSET)

        username = d.pop("username", UNSET)

        student = d.pop("student", UNSET)

        ta = d.pop("ta", UNSET)

        authentication = cls(
            admin=admin,
            username=username,
            student=student,
            ta=ta,
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
