from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_json import ApplicationJson
    from ..models.player_json import PlayerJson


T = TypeVar("T", bound="LaunchProfileJson")


@attr.s(auto_attribs=True)
class LaunchProfileJson:
    """
    Attributes:
        name (Union[Unset, str]):
        application (Union[Unset, ApplicationJson]):
        player (Union[Unset, PlayerJson]):
    """

    name: Union[Unset, str] = UNSET
    application: Union[Unset, "ApplicationJson"] = UNSET
    player: Union[Unset, "PlayerJson"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        application: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        player: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.player, Unset):
            player = self.player.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if application is not UNSET:
            field_dict["application"] = application
        if player is not UNSET:
            field_dict["player"] = player

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.application_json import ApplicationJson
        from ..models.player_json import PlayerJson

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _application = d.pop("application", UNSET)
        application: Union[Unset, ApplicationJson]
        if isinstance(_application, Unset):
            application = UNSET
        else:
            application = ApplicationJson.from_dict(_application)

        _player = d.pop("player", UNSET)
        player: Union[Unset, PlayerJson]
        if isinstance(_player, Unset):
            player = UNSET
        else:
            player = PlayerJson.from_dict(_player)

        launch_profile_json = cls(
            name=name,
            application=application,
            player=player,
        )

        launch_profile_json.additional_properties = d
        return launch_profile_json

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
