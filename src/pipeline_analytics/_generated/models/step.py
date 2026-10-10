from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.quarantine import Quarantine





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
            failure_count (int): Times this step failed within the window.
            flaky (bool):
            quarantined (bool): True when a person has marked this step as known. It is still `flaky`; it just stops making
                its pipeline unhealthy.
            quarantine (Quarantine | Unset): A person's mark on a flaky step. Present only while it is in force.
            forge_url (str | Unset): Deep link to one occurrence's log on the originating forge -- not necessarily one where
                the step failed. GET .../flaky-runs is the reliable way to reach a run the step actually failed on.
     """

    id: str
    name: str
    duration_contribution_seconds: float
    queue_seconds: float
    exec_seconds: float
    failure_rate: float
    failure_count: int
    flaky: bool
    quarantined: bool
    quarantine: Quarantine | Unset = UNSET
    forge_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.quarantine import Quarantine # noqa: PLC0415
        id = self.id

        name = self.name

        duration_contribution_seconds = self.duration_contribution_seconds

        queue_seconds = self.queue_seconds

        exec_seconds = self.exec_seconds

        failure_rate = self.failure_rate

        failure_count = self.failure_count

        flaky = self.flaky

        quarantined = self.quarantined

        quarantine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quarantine, Unset):
            quarantine = self.quarantine.to_dict()

        forge_url = self.forge_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "durationContributionSeconds": duration_contribution_seconds,
            "queueSeconds": queue_seconds,
            "execSeconds": exec_seconds,
            "failureRate": failure_rate,
            "failureCount": failure_count,
            "flaky": flaky,
            "quarantined": quarantined,
        })
        if quarantine is not UNSET:
            field_dict["quarantine"] = quarantine
        if forge_url is not UNSET:
            field_dict["forgeUrl"] = forge_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quarantine import Quarantine # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        duration_contribution_seconds = d.pop("durationContributionSeconds")

        queue_seconds = d.pop("queueSeconds")

        exec_seconds = d.pop("execSeconds")

        failure_rate = d.pop("failureRate")

        failure_count = d.pop("failureCount")

        flaky = d.pop("flaky")

        quarantined = d.pop("quarantined")

        _quarantine = d.pop("quarantine", UNSET)
        quarantine: Quarantine | Unset
        if isinstance(_quarantine,  Unset):
            quarantine = UNSET
        else:
            quarantine = Quarantine.from_dict(_quarantine)




        forge_url = d.pop("forgeUrl", UNSET)

        step = cls(
            id=id,
            name=name,
            duration_contribution_seconds=duration_contribution_seconds,
            queue_seconds=queue_seconds,
            exec_seconds=exec_seconds,
            failure_rate=failure_rate,
            failure_count=failure_count,
            flaky=flaky,
            quarantined=quarantined,
            quarantine=quarantine,
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
