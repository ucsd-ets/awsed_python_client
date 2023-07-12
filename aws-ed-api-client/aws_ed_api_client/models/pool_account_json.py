from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PoolAccountJson")


@attr.s(auto_attribs=True)
class PoolAccountJson:
    """
    Attributes:
        account_id (Union[Unset, str]):
        account_name (Union[Unset, str]):
        username (Union[Unset, str]):
        team_name (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    account_name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    team_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        account_name = self.account_name
        username = self.username
        team_name = self.team_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if username is not UNSET:
            field_dict["username"] = username
        if team_name is not UNSET:
            field_dict["teamName"] = team_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId", UNSET)

        account_name = d.pop("accountName", UNSET)

        username = d.pop("username", UNSET)

        team_name = d.pop("teamName", UNSET)

        pool_account_json = cls(
            account_id=account_id,
            account_name=account_name,
            username=username,
            team_name=team_name,
        )

        pool_account_json.additional_properties = d
        return pool_account_json

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
