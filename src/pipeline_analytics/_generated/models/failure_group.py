from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.failure_category import FailureCategory
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.failure_group_pipelines_item import FailureGroupPipelinesItem





T = TypeVar("T", bound="FailureGroup")



@_attrs_define
class FailureGroup:
    """ 
        Attributes:
            step (str):
            category (FailureCategory):
            occurrences (int):
            pipelines (list[FailureGroupPipelinesItem]): Pipelines the step failed in, each reachable via GET .../flaky-
                runs.
            conclusion (str | Unset): The most common step conclusion in the group, shown so a heuristic category can be
                checked.
     """

    step: str
    category: FailureCategory
    occurrences: int
    pipelines: list[FailureGroupPipelinesItem]
    conclusion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.failure_group_pipelines_item import FailureGroupPipelinesItem # noqa: PLC0415
        step = self.step

        category = self.category.value

        occurrences = self.occurrences

        pipelines = []
        for pipelines_item_data in self.pipelines:
            pipelines_item = pipelines_item_data.to_dict()
            pipelines.append(pipelines_item)



        conclusion = self.conclusion


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "step": step,
            "category": category,
            "occurrences": occurrences,
            "pipelines": pipelines,
        })
        if conclusion is not UNSET:
            field_dict["conclusion"] = conclusion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failure_group_pipelines_item import FailureGroupPipelinesItem # noqa: PLC0415
        d = dict(src_dict)
        step = d.pop("step")

        category = FailureCategory(d.pop("category"))




        occurrences = d.pop("occurrences")

        pipelines = []
        _pipelines = d.pop("pipelines")
        for pipelines_item_data in (_pipelines):
            pipelines_item = FailureGroupPipelinesItem.from_dict(pipelines_item_data)



            pipelines.append(pipelines_item)


        conclusion = d.pop("conclusion", UNSET)

        failure_group = cls(
            step=step,
            category=category,
            occurrences=occurrences,
            pipelines=pipelines,
            conclusion=conclusion,
        )


        failure_group.additional_properties = d
        return failure_group

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
