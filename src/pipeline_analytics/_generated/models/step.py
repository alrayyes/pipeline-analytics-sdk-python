from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Step")


@_attrs_define
class Step:
    """
    Attributes:
        id (str):
        name (str):
        duration_contribution_seconds (float):
        queue_seconds (float):
        exec_seconds (float):
        failure_rate (float):
        flaky (bool):
        forge_url (str | Unset): Deep link to this step's log on the originating forge.
    """

    id: str
    name: str
    duration_contribution_seconds: float
    queue_seconds: float
    exec_seconds: float
    failure_rate: float
    flaky: bool
    forge_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        duration_contribution_seconds = self.duration_contribution_seconds

        queue_seconds = self.queue_seconds

        exec_seconds = self.exec_seconds

        failure_rate = self.failure_rate

        flaky = self.flaky

        forge_url = self.forge_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "durationContributionSeconds": duration_contribution_seconds,
                "queueSeconds": queue_seconds,
                "execSeconds": exec_seconds,
                "failureRate": failure_rate,
                "flaky": flaky,
            }
        )
        if forge_url is not UNSET:
            field_dict["forgeUrl"] = forge_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        duration_contribution_seconds = d.pop("durationContributionSeconds")

        queue_seconds = d.pop("queueSeconds")

        exec_seconds = d.pop("execSeconds")

        failure_rate = d.pop("failureRate")

        flaky = d.pop("flaky")

        forge_url = d.pop("forgeUrl", UNSET)

        step = cls(
            id=id,
            name=name,
            duration_contribution_seconds=duration_contribution_seconds,
            queue_seconds=queue_seconds,
            exec_seconds=exec_seconds,
            failure_rate=failure_rate,
            flaky=flaky,
            forge_url=forge_url,
        )

        step.additional_properties = d
        return step

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
