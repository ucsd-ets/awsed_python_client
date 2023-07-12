from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pool_account_json import PoolAccountJson


T = TypeVar("T", bound="PoolAccountResult")


@attr.s(auto_attribs=True)
class PoolAccountResult:
    """
    Attributes:
        accounts (Union[Unset, List['PoolAccountJson']]):
    """

    accounts: Union[Unset, List["PoolAccountJson"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()

                accounts.append(accounts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accounts is not UNSET:
            field_dict["accounts"] = accounts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pool_account_json import PoolAccountJson

        d = src_dict.copy()
        accounts = []
        _accounts = d.pop("accounts", UNSET)
        for accounts_item_data in _accounts or []:
            accounts_item = PoolAccountJson.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        pool_account_result = cls(
            accounts=accounts,
        )

        pool_account_result.additional_properties = d
        return pool_account_result

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
