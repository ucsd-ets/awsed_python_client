from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImmutablePool")


@attr.s(auto_attribs=True)
class ImmutablePool:
    """
    Attributes:
        name (Union[Unset, str]):
        pool_root_name (Union[Unset, str]):
        rule (Union[Unset, str]):
        ou (Union[Unset, str]):
        course_name (Union[Unset, str]):
        mode (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    pool_root_name: Union[Unset, str] = UNSET
    rule: Union[Unset, str] = UNSET
    ou: Union[Unset, str] = UNSET
    course_name: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        pool_root_name = self.pool_root_name
        rule = self.rule
        ou = self.ou
        course_name = self.course_name
        mode = self.mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if pool_root_name is not UNSET:
            field_dict["poolRootName"] = pool_root_name
        if rule is not UNSET:
            field_dict["rule"] = rule
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

        pool_root_name = d.pop("poolRootName", UNSET)

        rule = d.pop("rule", UNSET)

        ou = d.pop("ou", UNSET)

        course_name = d.pop("courseName", UNSET)

        mode = d.pop("mode", UNSET)

        immutable_pool = cls(
            name=name,
            pool_root_name=pool_root_name,
            rule=rule,
            ou=ou,
            course_name=course_name,
            mode=mode,
        )

        immutable_pool.additional_properties = d
        return immutable_pool

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
