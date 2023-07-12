from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pool_json import PoolJson


T = TypeVar("T", bound="PoolsResult")


@attr.s(auto_attribs=True)
class PoolsResult:
    """
    Attributes:
        pools (Union[Unset, List['PoolJson']]):
    """

    pools: Union[Unset, List["PoolJson"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pools: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pools, Unset):
            pools = []
            for pools_item_data in self.pools:
                pools_item = pools_item_data.to_dict()

                pools.append(pools_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pools is not UNSET:
            field_dict["pools"] = pools

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pool_json import PoolJson

        d = src_dict.copy()
        pools = []
        _pools = d.pop("pools", UNSET)
        for pools_item_data in _pools or []:
            pools_item = PoolJson.from_dict(pools_item_data)

            pools.append(pools_item)

        pools_result = cls(
            pools=pools,
        )

        pools_result.additional_properties = d
        return pools_result

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
