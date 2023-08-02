from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesVolumeMount")


@attr.s(auto_attribs=True)
class KubernetesVolumeMount:
    """
    Attributes:
        name (Union[Unset, str]):
        mount_path (Union[Unset, str]):
        mount_propagation (Union[Unset, str]):
        sub_path (Union[Unset, str]):
        sub_path_expr (Union[Unset, str]):
        read_only (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    mount_path: Union[Unset, str] = UNSET
    mount_propagation: Union[Unset, str] = UNSET
    sub_path: Union[Unset, str] = UNSET
    sub_path_expr: Union[Unset, str] = UNSET
    read_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        mount_path = self.mount_path
        mount_propagation = self.mount_propagation
        sub_path = self.sub_path
        sub_path_expr = self.sub_path_expr
        read_only = self.read_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mount_path is not UNSET:
            field_dict["mountPath"] = mount_path
        if mount_propagation is not UNSET:
            field_dict["mountPropagation"] = mount_propagation
        if sub_path is not UNSET:
            field_dict["subPath"] = sub_path
        if sub_path_expr is not UNSET:
            field_dict["subPathExpr"] = sub_path_expr
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        mount_path = d.pop("mountPath", UNSET)

        mount_propagation = d.pop("mountPropagation", UNSET)

        sub_path = d.pop("subPath", UNSET)

        sub_path_expr = d.pop("subPathExpr", UNSET)

        read_only = d.pop("readOnly", UNSET)

        kubernetes_volume_mount = cls(
            name=name,
            mount_path=mount_path,
            mount_propagation=mount_propagation,
            sub_path=sub_path,
            sub_path_expr=sub_path_expr,
            read_only=read_only,
        )

        kubernetes_volume_mount.additional_properties = d
        return kubernetes_volume_mount

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
