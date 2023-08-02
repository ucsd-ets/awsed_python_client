from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaunchProfileRequestJson")


@attr.s(auto_attribs=True)
class LaunchProfileRequestJson:
    """
    Attributes:
        launch_profile_name (Union[Unset, str]):
        course_name (Union[Unset, str]):
        application_name (Union[Unset, str]):
        player_name (Union[Unset, str]):
    """

    launch_profile_name: Union[Unset, str] = UNSET
    course_name: Union[Unset, str] = UNSET
    application_name: Union[Unset, str] = UNSET
    player_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        launch_profile_name = self.launch_profile_name
        course_name = self.course_name
        application_name = self.application_name
        player_name = self.player_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if launch_profile_name is not UNSET:
            field_dict["launchProfileName"] = launch_profile_name
        if course_name is not UNSET:
            field_dict["courseName"] = course_name
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if player_name is not UNSET:
            field_dict["playerName"] = player_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        launch_profile_name = d.pop("launchProfileName", UNSET)

        course_name = d.pop("courseName", UNSET)

        application_name = d.pop("applicationName", UNSET)

        player_name = d.pop("playerName", UNSET)

        launch_profile_request_json = cls(
            launch_profile_name=launch_profile_name,
            course_name=course_name,
            application_name=application_name,
            player_name=player_name,
        )

        launch_profile_request_json.additional_properties = d
        return launch_profile_request_json

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
