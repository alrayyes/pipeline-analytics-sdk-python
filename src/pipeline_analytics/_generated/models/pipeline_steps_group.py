from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.step import Step


T = TypeVar("T", bound="PipelineStepsGroup")


@_attrs_define
class PipelineStepsGroup:
    """
    Attributes:
        pipeline_id (str):
        pipeline_name (str):
        repo_id (str):
        steps (list[Step]):
    """

    pipeline_id: str
    pipeline_name: str
    repo_id: str
    steps: list[Step]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pipeline_id = self.pipeline_id

        pipeline_name = self.pipeline_name

        repo_id = self.repo_id

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pipelineId": pipeline_id,
                "pipelineName": pipeline_name,
                "repoId": repo_id,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step import Step

        d = dict(src_dict)
        pipeline_id = d.pop("pipelineId")

        pipeline_name = d.pop("pipelineName")

        repo_id = d.pop("repoId")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = Step.from_dict(steps_item_data)

            steps.append(steps_item)

        pipeline_steps_group = cls(
            pipeline_id=pipeline_id,
            pipeline_name=pipeline_name,
            repo_id=repo_id,
            steps=steps,
        )

        pipeline_steps_group.additional_properties = d
        return pipeline_steps_group

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
