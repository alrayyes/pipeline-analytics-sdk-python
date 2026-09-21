from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.pipeline_summary import PipelineSummary





T = TypeVar("T", bound="PipelineList")



@_attrs_define
class PipelineList:
    """ 
        Attributes:
            pipelines (list[PipelineSummary]):
            has_more (bool): True when pipelines beyond this page match the filter. Always false when limit was omitted.
     """

    pipelines: list[PipelineSummary]
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pipeline_summary import PipelineSummary # noqa: PLC0415
        pipelines = []
        for pipelines_item_data in self.pipelines:
            pipelines_item = pipelines_item_data.to_dict()
            pipelines.append(pipelines_item)



        has_more = self.has_more


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "pipelines": pipelines,
            "hasMore": has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_summary import PipelineSummary # noqa: PLC0415
        d = dict(src_dict)
        pipelines = []
        _pipelines = d.pop("pipelines")
        for pipelines_item_data in (_pipelines):
            pipelines_item = PipelineSummary.from_dict(pipelines_item_data)



            pipelines.append(pipelines_item)


        has_more = d.pop("hasMore")

        pipeline_list = cls(
            pipelines=pipelines,
            has_more=has_more,
        )


        pipeline_list.additional_properties = d
        return pipeline_list

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
