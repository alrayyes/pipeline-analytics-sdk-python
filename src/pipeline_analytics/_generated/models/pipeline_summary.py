from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.health_status import HealthStatus
from ..models.pipeline_summary_triggered_signals_item import PipelineSummaryTriggeredSignalsItem
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="PipelineSummary")



@_attrs_define
class PipelineSummary:
    """ 
        Attributes:
            id (str):
            repo_id (str):
            name (str):
            health_status (HealthStatus):
            triggered_signals (list[PipelineSummaryTriggeredSignalsItem] | Unset): Which signal(s) triggered an unhealthy
                status (pipeline-metrics/spec.md).
            last_run_at (datetime.datetime | Unset): The most recent run's start time. Absent if the pipeline has no runs.
     """

    id: str
    repo_id: str
    name: str
    health_status: HealthStatus
    triggered_signals: list[PipelineSummaryTriggeredSignalsItem] | Unset = UNSET
    last_run_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        repo_id = self.repo_id

        name = self.name

        health_status = self.health_status.value

        triggered_signals: list[str] | Unset = UNSET
        if not isinstance(self.triggered_signals, Unset):
            triggered_signals = []
            for triggered_signals_item_data in self.triggered_signals:
                triggered_signals_item = triggered_signals_item_data.value
                triggered_signals.append(triggered_signals_item)



        last_run_at: str | Unset = UNSET
        if not isinstance(self.last_run_at, Unset):
            last_run_at = self.last_run_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "repoId": repo_id,
            "name": name,
            "healthStatus": health_status,
        })
        if triggered_signals is not UNSET:
            field_dict["triggeredSignals"] = triggered_signals
        if last_run_at is not UNSET:
            field_dict["lastRunAt"] = last_run_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        repo_id = d.pop("repoId")

        name = d.pop("name")

        health_status = HealthStatus(d.pop("healthStatus"))




        _triggered_signals = d.pop("triggeredSignals", UNSET)
        triggered_signals: list[PipelineSummaryTriggeredSignalsItem] | Unset = UNSET
        if _triggered_signals is not UNSET:
            triggered_signals = []
            for triggered_signals_item_data in _triggered_signals:
                triggered_signals_item = PipelineSummaryTriggeredSignalsItem(triggered_signals_item_data)



                triggered_signals.append(triggered_signals_item)


        _last_run_at = d.pop("lastRunAt", UNSET)
        last_run_at: datetime.datetime | Unset
        if isinstance(_last_run_at,  Unset):
            last_run_at = UNSET
        else:
            last_run_at = datetime.datetime.fromisoformat(_last_run_at)




        pipeline_summary = cls(
            id=id,
            repo_id=repo_id,
            name=name,
            health_status=health_status,
            triggered_signals=triggered_signals,
            last_run_at=last_run_at,
        )


        pipeline_summary.additional_properties = d
        return pipeline_summary

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
