from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSystemResult")


@attr.s(auto_attribs=True)
class FileSystemResult:
    """
    Attributes:
        identifier (Union[Unset, str]):
        server (Union[Unset, str]):
        path (Union[Unset, str]):
    """

    identifier: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        server = self.server
        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if server is not UNSET:
            field_dict["server"] = server
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        server = d.pop("server", UNSET)

        path = d.pop("path", UNSET)

        file_system_result = cls(
            identifier=identifier,
            server=server,
            path=path,
        )

        file_system_result.additional_properties = d
        return file_system_result

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
