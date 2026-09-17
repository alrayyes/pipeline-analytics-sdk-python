from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.health_status import HealthStatus
from ..models.pipeline_summary_triggered_signals_item import PipelineSummaryTriggeredSignalsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trend import Trend


T = TypeVar("T", bound="PipelineDetail")


@_attrs_define
class PipelineDetail:
    """
    Attributes:
        id (str):
        repo_id (str):
        name (str):
        health_status (HealthStatus):
        triggered_signals (list[PipelineSummaryTriggeredSignalsItem] | Unset): Which signal(s) triggered an unhealthy
            status (pipeline-metrics/spec.md).
        last_run_at (datetime.datetime | Unset): The most recent run's start time. Absent if the pipeline has no runs.
        duration_trend (Trend | Unset):
        failure_rate_trend (Trend | Unset):
    """

    id: str
    repo_id: str
    name: str
    health_status: HealthStatus
    triggered_signals: list[PipelineSummaryTriggeredSignalsItem] | Unset = UNSET
    last_run_at: datetime.datetime | Unset = UNSET
    duration_trend: Trend | Unset = UNSET
    failure_rate_trend: Trend | Unset = UNSET
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

        duration_trend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duration_trend, Unset):
            duration_trend = self.duration_trend.to_dict()

        failure_rate_trend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure_rate_trend, Unset):
            failure_rate_trend = self.failure_rate_trend.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "repoId": repo_id,
                "name": name,
                "healthStatus": health_status,
            }
        )
        if triggered_signals is not UNSET:
            field_dict["triggeredSignals"] = triggered_signals
        if last_run_at is not UNSET:
            field_dict["lastRunAt"] = last_run_at
        if duration_trend is not UNSET:
            field_dict["durationTrend"] = duration_trend
        if failure_rate_trend is not UNSET:
            field_dict["failureRateTrend"] = failure_rate_trend

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trend import Trend

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
        if isinstance(_last_run_at, Unset):
            last_run_at = UNSET
        else:
            last_run_at = datetime.datetime.fromisoformat(_last_run_at)

        _duration_trend = d.pop("durationTrend", UNSET)
        duration_trend: Trend | Unset
        if isinstance(_duration_trend, Unset):
            duration_trend = UNSET
        else:
            duration_trend = Trend.from_dict(_duration_trend)

        _failure_rate_trend = d.pop("failureRateTrend", UNSET)
        failure_rate_trend: Trend | Unset
        if isinstance(_failure_rate_trend, Unset):
            failure_rate_trend = UNSET
        else:
            failure_rate_trend = Trend.from_dict(_failure_rate_trend)

        pipeline_detail = cls(
            id=id,
            repo_id=repo_id,
            name=name,
            health_status=health_status,
            triggered_signals=triggered_signals,
            last_run_at=last_run_at,
            duration_trend=duration_trend,
            failure_rate_trend=failure_rate_trend,
        )

        pipeline_detail.additional_properties = d
        return pipeline_detail

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
