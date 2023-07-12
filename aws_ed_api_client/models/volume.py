from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Volume")


@attr.s(auto_attribs=True)
class Volume:
    """
    Attributes:
        type (Union[Unset, str]):
        name (Union[Unset, str]):
        server (Union[Unset, str]):
        path (Union[Unset, str]):
        access_mode (Union[Unset, str]):
        pvc_name (Union[Unset, str]):
    """

    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    access_mode: Union[Unset, str] = UNSET
    pvc_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        name = self.name
        server = self.server
        path = self.path
        access_mode = self.access_mode
        pvc_name = self.pvc_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if server is not UNSET:
            field_dict["server"] = server
        if path is not UNSET:
            field_dict["path"] = path
        if access_mode is not UNSET:
            field_dict["accessMode"] = access_mode
        if pvc_name is not UNSET:
            field_dict["pvcName"] = pvc_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        server = d.pop("server", UNSET)

        path = d.pop("path", UNSET)

        access_mode = d.pop("accessMode", UNSET)

        pvc_name = d.pop("pvcName", UNSET)

        volume = cls(
            type=type,
            name=name,
            server=server,
            path=path,
            access_mode=access_mode,
            pvc_name=pvc_name,
        )

        volume.additional_properties = d
        return volume

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
