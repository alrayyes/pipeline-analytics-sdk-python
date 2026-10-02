from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.failing_pipeline import FailingPipeline
  from ..models.failure_group import FailureGroup
  from ..models.stage_failure_count import StageFailureCount





T = TypeVar("T", bound="FailureInsights")



@_attrs_define
class FailureInsights:
    """ 
        Attributes:
            total_runs (int):
            failed_runs (int):
            pass_rate (float): Fraction in [0, 1] of concluded runs that succeeded.
            flaky_step_ratio (float): Fraction in [0, 1] of distinct steps flagged flaky.
            stage_distribution (list[StageFailureCount]): Failures by failing step name, highest first.
            top_failing_pipelines (list[FailingPipeline]): Pipelines ordered by failed runs, highest first.
            failure_groups (list[FailureGroup]): Failed steps grouped by name, highest occurrence count first.
            pass_rate_delta (float | Unset): Percentage points versus the preceding window of equal length. Absent when that
                window had no runs.
            mttr_seconds (float | Unset): Mean time from a pipeline's first failed run to its next successful run. Absent
                when nothing recovered in the window.
     """

    total_runs: int
    failed_runs: int
    pass_rate: float
    flaky_step_ratio: float
    stage_distribution: list[StageFailureCount]
    top_failing_pipelines: list[FailingPipeline]
    failure_groups: list[FailureGroup]
    pass_rate_delta: float | Unset = UNSET
    mttr_seconds: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.failing_pipeline import FailingPipeline # noqa: PLC0415
        from ..models.failure_group import FailureGroup # noqa: PLC0415
        from ..models.stage_failure_count import StageFailureCount # noqa: PLC0415
        total_runs = self.total_runs

        failed_runs = self.failed_runs

        pass_rate = self.pass_rate

        flaky_step_ratio = self.flaky_step_ratio

        stage_distribution = []
        for stage_distribution_item_data in self.stage_distribution:
            stage_distribution_item = stage_distribution_item_data.to_dict()
            stage_distribution.append(stage_distribution_item)



        top_failing_pipelines = []
        for top_failing_pipelines_item_data in self.top_failing_pipelines:
            top_failing_pipelines_item = top_failing_pipelines_item_data.to_dict()
            top_failing_pipelines.append(top_failing_pipelines_item)



        failure_groups = []
        for failure_groups_item_data in self.failure_groups:
            failure_groups_item = failure_groups_item_data.to_dict()
            failure_groups.append(failure_groups_item)



        pass_rate_delta = self.pass_rate_delta

        mttr_seconds = self.mttr_seconds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "totalRuns": total_runs,
            "failedRuns": failed_runs,
            "passRate": pass_rate,
            "flakyStepRatio": flaky_step_ratio,
            "stageDistribution": stage_distribution,
            "topFailingPipelines": top_failing_pipelines,
            "failureGroups": failure_groups,
        })
        if pass_rate_delta is not UNSET:
            field_dict["passRateDelta"] = pass_rate_delta
        if mttr_seconds is not UNSET:
            field_dict["mttrSeconds"] = mttr_seconds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failing_pipeline import FailingPipeline # noqa: PLC0415
        from ..models.failure_group import FailureGroup # noqa: PLC0415
        from ..models.stage_failure_count import StageFailureCount # noqa: PLC0415
        d = dict(src_dict)
        total_runs = d.pop("totalRuns")

        failed_runs = d.pop("failedRuns")

        pass_rate = d.pop("passRate")

        flaky_step_ratio = d.pop("flakyStepRatio")

        stage_distribution = []
        _stage_distribution = d.pop("stageDistribution")
        for stage_distribution_item_data in (_stage_distribution):
            stage_distribution_item = StageFailureCount.from_dict(stage_distribution_item_data)



            stage_distribution.append(stage_distribution_item)


        top_failing_pipelines = []
        _top_failing_pipelines = d.pop("topFailingPipelines")
        for top_failing_pipelines_item_data in (_top_failing_pipelines):
            top_failing_pipelines_item = FailingPipeline.from_dict(top_failing_pipelines_item_data)



            top_failing_pipelines.append(top_failing_pipelines_item)


        failure_groups = []
        _failure_groups = d.pop("failureGroups")
        for failure_groups_item_data in (_failure_groups):
            failure_groups_item = FailureGroup.from_dict(failure_groups_item_data)



            failure_groups.append(failure_groups_item)


        pass_rate_delta = d.pop("passRateDelta", UNSET)

        mttr_seconds = d.pop("mttrSeconds", UNSET)

        failure_insights = cls(
            total_runs=total_runs,
            failed_runs=failed_runs,
            pass_rate=pass_rate,
            flaky_step_ratio=flaky_step_ratio,
            stage_distribution=stage_distribution,
            top_failing_pipelines=top_failing_pipelines,
            failure_groups=failure_groups,
            pass_rate_delta=pass_rate_delta,
            mttr_seconds=mttr_seconds,
        )


        failure_insights.additional_properties = d
        return failure_insights

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
