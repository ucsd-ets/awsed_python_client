from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_json import ApplicationJson
    from ..models.course_2_json import Course2Json
    from ..models.player_json import PlayerJson
    from ..models.team_2_json import Team2Json


T = TypeVar("T", bound="UserLaunchProfileJson")


@attr.s(auto_attribs=True)
class UserLaunchProfileJson:
    """
    Attributes:
        name (Union[Unset, str]):
        application (Union[Unset, ApplicationJson]):
        player (Union[Unset, PlayerJson]):
        course (Union[Unset, Course2Json]):
        teams (Union[Unset, List['Team2Json']]):
    """

    name: Union[Unset, str] = UNSET
    application: Union[Unset, "ApplicationJson"] = UNSET
    player: Union[Unset, "PlayerJson"] = UNSET
    course: Union[Unset, "Course2Json"] = UNSET
    teams: Union[Unset, List["Team2Json"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        application: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        player: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.player, Unset):
            player = self.player.to_dict()

        course: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.course, Unset):
            course = self.course.to_dict()

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()

                teams.append(teams_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if application is not UNSET:
            field_dict["application"] = application
        if player is not UNSET:
            field_dict["player"] = player
        if course is not UNSET:
            field_dict["course"] = course
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.application_json import ApplicationJson
        from ..models.course_2_json import Course2Json
        from ..models.player_json import PlayerJson
        from ..models.team_2_json import Team2Json

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

        _course = d.pop("course", UNSET)
        course: Union[Unset, Course2Json]
        if isinstance(_course, Unset):
            course = UNSET
        else:
            course = Course2Json.from_dict(_course)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = Team2Json.from_dict(teams_item_data)

            teams.append(teams_item)

        user_launch_profile_json = cls(
            name=name,
            application=application,
            player=player,
            course=course,
            teams=teams,
        )

        user_launch_profile_json.additional_properties = d
        return user_launch_profile_json

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
