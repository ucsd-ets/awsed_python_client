from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_environment_variable import KubernetesEnvironmentVariable
    from ..models.kubernetes_volume import KubernetesVolume
    from ..models.kubernetes_volume_mount import KubernetesVolumeMount


T = TypeVar("T", bound="ApplicationJson")


@attr.s(auto_attribs=True)
class ApplicationJson:
    """
    Attributes:
        name (Union[Unset, str]):
        image (Union[Unset, str]):
        description (Union[Unset, str]):
        pull_policy (Union[Unset, str]):
        volume_mounts (Union[Unset, List['KubernetesVolumeMount']]):
        volumes (Union[Unset, List['KubernetesVolume']]):
        command (Union[Unset, str]):
        args (Union[Unset, List[str]]):
        environment (Union[Unset, List['KubernetesEnvironmentVariable']]):
        extra_yaml (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    pull_policy: Union[Unset, str] = UNSET
    volume_mounts: Union[Unset, List["KubernetesVolumeMount"]] = UNSET
    volumes: Union[Unset, List["KubernetesVolume"]] = UNSET
    command: Union[Unset, str] = UNSET
    args: Union[Unset, List[str]] = UNSET
    environment: Union[Unset, List["KubernetesEnvironmentVariable"]] = UNSET
    extra_yaml: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        image = self.image
        description = self.description
        pull_policy = self.pull_policy
        volume_mounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.volume_mounts, Unset):
            volume_mounts = []
            for volume_mounts_item_data in self.volume_mounts:
                volume_mounts_item = volume_mounts_item_data.to_dict()

                volume_mounts.append(volume_mounts_item)

        volumes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = []
            for volumes_item_data in self.volumes:
                volumes_item = volumes_item_data.to_dict()

                volumes.append(volumes_item)

        command = self.command
        args: Union[Unset, List[str]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args

        environment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = []
            for environment_item_data in self.environment:
                environment_item = environment_item_data.to_dict()

                environment.append(environment_item)

        extra_yaml = self.extra_yaml

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if image is not UNSET:
            field_dict["image"] = image
        if description is not UNSET:
            field_dict["description"] = description
        if pull_policy is not UNSET:
            field_dict["pullPolicy"] = pull_policy
        if volume_mounts is not UNSET:
            field_dict["volumeMounts"] = volume_mounts
        if volumes is not UNSET:
            field_dict["volumes"] = volumes
        if command is not UNSET:
            field_dict["command"] = command
        if args is not UNSET:
            field_dict["args"] = args
        if environment is not UNSET:
            field_dict["environment"] = environment
        if extra_yaml is not UNSET:
            field_dict["extraYaml"] = extra_yaml

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.kubernetes_environment_variable import KubernetesEnvironmentVariable
        from ..models.kubernetes_volume import KubernetesVolume
        from ..models.kubernetes_volume_mount import KubernetesVolumeMount

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        image = d.pop("image", UNSET)

        description = d.pop("description", UNSET)

        pull_policy = d.pop("pullPolicy", UNSET)

        volume_mounts = []
        _volume_mounts = d.pop("volumeMounts", UNSET)
        for volume_mounts_item_data in _volume_mounts or []:
            volume_mounts_item = KubernetesVolumeMount.from_dict(volume_mounts_item_data)

            volume_mounts.append(volume_mounts_item)

        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = KubernetesVolume.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        command = d.pop("command", UNSET)

        args = cast(List[str], d.pop("args", UNSET))

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = KubernetesEnvironmentVariable.from_dict(environment_item_data)

            environment.append(environment_item)

        extra_yaml = d.pop("extraYaml", UNSET)

        application_json = cls(
            name=name,
            image=image,
            description=description,
            pull_policy=pull_policy,
            volume_mounts=volume_mounts,
            volumes=volumes,
            command=command,
            args=args,
            environment=environment,
            extra_yaml=extra_yaml,
        )

        application_json.additional_properties = d
        return application_json

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
