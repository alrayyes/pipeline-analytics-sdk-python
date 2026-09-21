from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.pipeline_steps_group import PipelineStepsGroup





T = TypeVar("T", bound="UnhealthyStepsList")



@_attrs_define
class UnhealthyStepsList:
    """ 
        Attributes:
            groups (list[PipelineStepsGroup]):
            has_more (bool): True when pipeline groups beyond this page have an unhealthy step. Always false when limit was
                omitted.
     """

    groups: list[PipelineStepsGroup]
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pipeline_steps_group import PipelineStepsGroup # noqa: PLC0415
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)



        has_more = self.has_more


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "groups": groups,
            "hasMore": has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_steps_group import PipelineStepsGroup # noqa: PLC0415
        d = dict(src_dict)
        groups = []
        _groups = d.pop("groups")
        for groups_item_data in (_groups):
            groups_item = PipelineStepsGroup.from_dict(groups_item_data)



            groups.append(groups_item)


        has_more = d.pop("hasMore")

        unhealthy_steps_list = cls(
            groups=groups,
            has_more=has_more,
        )


        unhealthy_steps_list.additional_properties = d
        return unhealthy_steps_list

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
