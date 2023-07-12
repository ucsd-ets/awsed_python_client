from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Modification")


@attr.s(auto_attribs=True)
class Modification:
    """
    Attributes:
        type (Union[Unset, str]):
        username (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        class_name (Union[Unset, str]):
        uid (Union[Unset, int]):
        role (Union[Unset, str]):
        add (Union[Unset, bool]):
        delete (Union[Unset, bool]):
        modify (Union[Unset, bool]):
        gen_api (Union[Unset, bool]):
    """

    type: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    class_name: Union[Unset, str] = UNSET
    uid: Union[Unset, int] = UNSET
    role: Union[Unset, str] = UNSET
    add: Union[Unset, bool] = UNSET
    delete: Union[Unset, bool] = UNSET
    modify: Union[Unset, bool] = UNSET
    gen_api: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        class_name = self.class_name
        uid = self.uid
        role = self.role
        add = self.add
        delete = self.delete
        modify = self.modify
        gen_api = self.gen_api

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if uid is not UNSET:
            field_dict["uid"] = uid
        if role is not UNSET:
            field_dict["role"] = role
        if add is not UNSET:
            field_dict["add"] = add
        if delete is not UNSET:
            field_dict["delete"] = delete
        if modify is not UNSET:
            field_dict["modify"] = modify
        if gen_api is not UNSET:
            field_dict["genApi"] = gen_api

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        username = d.pop("username", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        class_name = d.pop("className", UNSET)

        uid = d.pop("uid", UNSET)

        role = d.pop("role", UNSET)

        add = d.pop("add", UNSET)

        delete = d.pop("delete", UNSET)

        modify = d.pop("modify", UNSET)

        gen_api = d.pop("genApi", UNSET)

        modification = cls(
            type=type,
            username=username,
            first_name=first_name,
            last_name=last_name,
            class_name=class_name,
            uid=uid,
            role=role,
            add=add,
            delete=delete,
            modify=modify,
            gen_api=gen_api,
        )

        modification.additional_properties = d
        return modification

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
