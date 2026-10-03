from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.flaky_step_list_window import FlakyStepListWindow
from typing import cast

if TYPE_CHECKING:
  from ..models.flaky_step_entry import FlakyStepEntry





T = TypeVar("T", bound="FlakyStepList")



@_attrs_define
class FlakyStepList:
    """ 
        Attributes:
            window (FlakyStepListWindow): The window these figures cover: the requested one, or the server's default.
                Clients show this rather than assuming a default.
            steps (list[FlakyStepEntry]):
            has_more (bool): True when flaky steps beyond this page exist. Always false when limit was omitted.
     """

    window: FlakyStepListWindow
    steps: list[FlakyStepEntry]
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.flaky_step_entry import FlakyStepEntry # noqa: PLC0415
        window = self.window.value

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)



        has_more = self.has_more


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "window": window,
            "steps": steps,
            "hasMore": has_more,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.flaky_step_entry import FlakyStepEntry # noqa: PLC0415
        d = dict(src_dict)
        window = FlakyStepListWindow(d.pop("window"))




        steps = []
        _steps = d.pop("steps")
        for steps_item_data in (_steps):
            steps_item = FlakyStepEntry.from_dict(steps_item_data)



            steps.append(steps_item)


        has_more = d.pop("hasMore")

        flaky_step_list = cls(
            window=window,
            steps=steps,
            has_more=has_more,
        )


        flaky_step_list.additional_properties = d
        return flaky_step_list

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
