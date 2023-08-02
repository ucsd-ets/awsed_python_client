from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesVolume")


@attr.s(auto_attribs=True)
class KubernetesVolume:
    """
    Attributes:
        name (Union[Unset, str]):
        type (Union[Unset, str]):
        server (Union[Unset, str]):
        path (Union[Unset, str]):
        access_mode (Union[Unset, str]):
        pvc_name (Union[Unset, str]):
        nfs (Union[Unset, bool]):
        host_path (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    access_mode: Union[Unset, str] = UNSET
    pvc_name: Union[Unset, str] = UNSET
    nfs: Union[Unset, bool] = UNSET
    host_path: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type
        server = self.server
        path = self.path
        access_mode = self.access_mode
        pvc_name = self.pvc_name
        nfs = self.nfs
        host_path = self.host_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if server is not UNSET:
            field_dict["server"] = server
        if path is not UNSET:
            field_dict["path"] = path
        if access_mode is not UNSET:
            field_dict["accessMode"] = access_mode
        if pvc_name is not UNSET:
            field_dict["pvcName"] = pvc_name
        if nfs is not UNSET:
            field_dict["nfs"] = nfs
        if host_path is not UNSET:
            field_dict["hostPath"] = host_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        server = d.pop("server", UNSET)

        path = d.pop("path", UNSET)

        access_mode = d.pop("accessMode", UNSET)

        pvc_name = d.pop("pvcName", UNSET)

        nfs = d.pop("nfs", UNSET)

        host_path = d.pop("hostPath", UNSET)

        kubernetes_volume = cls(
            name=name,
            type=type,
            server=server,
            path=path,
            access_mode=access_mode,
            pvc_name=pvc_name,
            nfs=nfs,
            host_path=host_path,
        )

        kubernetes_volume.additional_properties = d
        return kubernetes_volume

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
