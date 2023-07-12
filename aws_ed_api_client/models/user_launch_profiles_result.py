from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_launch_profile_json import UserLaunchProfileJson


T = TypeVar("T", bound="UserLaunchProfilesResult")


@attr.s(auto_attribs=True)
class UserLaunchProfilesResult:
    """
    Attributes:
        launch_profiles (Union[Unset, List['UserLaunchProfileJson']]):
    """

    launch_profiles: Union[Unset, List["UserLaunchProfileJson"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        launch_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.launch_profiles, Unset):
            launch_profiles = []
            for launch_profiles_item_data in self.launch_profiles:
                launch_profiles_item = launch_profiles_item_data.to_dict()

                launch_profiles.append(launch_profiles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if launch_profiles is not UNSET:
            field_dict["launchProfiles"] = launch_profiles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_launch_profile_json import UserLaunchProfileJson

        d = src_dict.copy()
        launch_profiles = []
        _launch_profiles = d.pop("launchProfiles", UNSET)
        for launch_profiles_item_data in _launch_profiles or []:
            launch_profiles_item = UserLaunchProfileJson.from_dict(launch_profiles_item_data)

            launch_profiles.append(launch_profiles_item)

        user_launch_profiles_result = cls(
            launch_profiles=launch_profiles,
        )

        user_launch_profiles_result.additional_properties = d
        return user_launch_profiles_result

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
