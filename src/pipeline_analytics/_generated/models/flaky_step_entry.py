from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.outcome import Outcome
from typing import cast






T = TypeVar("T", bound="FlakyStepEntry")



@_attrs_define
class FlakyStepEntry:
    """ 
        Attributes:
            pipeline_id (str):
            pipeline_name (str):
            repo_id (str):
            name (str):
            flake_rate (float): Fraction in (0, 1] of the step's runs in the window that failed.
            run_count (int): Runs of this step in the window.
            recent_outcomes (list[Outcome]): The step's result in its most recent runs, oldest first.
     """

    pipeline_id: str
    pipeline_name: str
    repo_id: str
    name: str
    flake_rate: float
    run_count: int
    recent_outcomes: list[Outcome]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        pipeline_id = self.pipeline_id

        pipeline_name = self.pipeline_name

        repo_id = self.repo_id

        name = self.name

        flake_rate = self.flake_rate

        run_count = self.run_count

        recent_outcomes = []
        for recent_outcomes_item_data in self.recent_outcomes:
            recent_outcomes_item = recent_outcomes_item_data.value
            recent_outcomes.append(recent_outcomes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "pipelineId": pipeline_id,
            "pipelineName": pipeline_name,
            "repoId": repo_id,
            "name": name,
            "flakeRate": flake_rate,
            "runCount": run_count,
            "recentOutcomes": recent_outcomes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pipeline_id = d.pop("pipelineId")

        pipeline_name = d.pop("pipelineName")

        repo_id = d.pop("repoId")

        name = d.pop("name")

        flake_rate = d.pop("flakeRate")

        run_count = d.pop("runCount")

        recent_outcomes = []
        _recent_outcomes = d.pop("recentOutcomes")
        for recent_outcomes_item_data in (_recent_outcomes):
            recent_outcomes_item = Outcome(recent_outcomes_item_data)



            recent_outcomes.append(recent_outcomes_item)


        flaky_step_entry = cls(
            pipeline_id=pipeline_id,
            pipeline_name=pipeline_name,
            repo_id=repo_id,
            name=name,
            flake_rate=flake_rate,
            run_count=run_count,
            recent_outcomes=recent_outcomes,
        )


        flaky_step_entry.additional_properties = d
        return flaky_step_entry

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
