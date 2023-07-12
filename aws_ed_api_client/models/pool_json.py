from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolJson")


@attr.s(auto_attribs=True)
class PoolJson:
    """
    Attributes:
        name (Union[Unset, str]):
        root (Union[Unset, str]):
        predicate (Union[Unset, str]):
        ou (Union[Unset, str]):
        course_name (Union[Unset, str]):
        mode (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    root: Union[Unset, str] = UNSET
    predicate: Union[Unset, str] = UNSET
    ou: Union[Unset, str] = UNSET
    course_name: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        root = self.root
        predicate = self.predicate
        ou = self.ou
        course_name = self.course_name
        mode = self.mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if root is not UNSET:
            field_dict["root"] = root
        if predicate is not UNSET:
            field_dict["predicate"] = predicate
        if ou is not UNSET:
            field_dict["ou"] = ou
        if course_name is not UNSET:
            field_dict["courseName"] = course_name
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        root = d.pop("root", UNSET)

        predicate = d.pop("predicate", UNSET)

        ou = d.pop("ou", UNSET)

        course_name = d.pop("courseName", UNSET)

        mode = d.pop("mode", UNSET)

        pool_json = cls(
            name=name,
            root=root,
            predicate=predicate,
            ou=ou,
            course_name=course_name,
            mode=mode,
        )

        pool_json.additional_properties = d
        return pool_json

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
