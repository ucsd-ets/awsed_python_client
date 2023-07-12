from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerJson")


@attr.s(auto_attribs=True)
class PlayerJson:
    """
    Attributes:
        name (Union[Unset, str]):
        min_cpu (Union[Unset, int]):
        max_cpu (Union[Unset, int]):
        min_memory (Union[Unset, int]):
        max_memory (Union[Unset, int]):
        gpu (Union[Unset, int]):
    """

    name: Union[Unset, str] = UNSET
    min_cpu: Union[Unset, int] = UNSET
    max_cpu: Union[Unset, int] = UNSET
    min_memory: Union[Unset, int] = UNSET
    max_memory: Union[Unset, int] = UNSET
    gpu: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        min_cpu = self.min_cpu
        max_cpu = self.max_cpu
        min_memory = self.min_memory
        max_memory = self.max_memory
        gpu = self.gpu

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if min_cpu is not UNSET:
            field_dict["minCpu"] = min_cpu
        if max_cpu is not UNSET:
            field_dict["maxCpu"] = max_cpu
        if min_memory is not UNSET:
            field_dict["minMemory"] = min_memory
        if max_memory is not UNSET:
            field_dict["maxMemory"] = max_memory
        if gpu is not UNSET:
            field_dict["gpu"] = gpu

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        min_cpu = d.pop("minCpu", UNSET)

        max_cpu = d.pop("maxCpu", UNSET)

        min_memory = d.pop("minMemory", UNSET)

        max_memory = d.pop("maxMemory", UNSET)

        gpu = d.pop("gpu", UNSET)

        player_json = cls(
            name=name,
            min_cpu=min_cpu,
            max_cpu=max_cpu,
            min_memory=min_memory,
            max_memory=max_memory,
            gpu=gpu,
        )

        player_json.additional_properties = d
        return player_json

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
