from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FailureGroupPipelinesItem")



@_attrs_define
class FailureGroupPipelinesItem:
    """ 
        Attributes:
            pipeline_id (str):
            pipeline_name (str):
     """

    pipeline_id: str
    pipeline_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        pipeline_id = self.pipeline_id

        pipeline_name = self.pipeline_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "pipelineId": pipeline_id,
            "pipelineName": pipeline_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pipeline_id = d.pop("pipelineId")

        pipeline_name = d.pop("pipelineName")

        failure_group_pipelines_item = cls(
            pipeline_id=pipeline_id,
            pipeline_name=pipeline_name,
        )


        failure_group_pipelines_item.additional_properties = d
        return failure_group_pipelines_item

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
