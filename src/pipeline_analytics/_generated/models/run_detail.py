from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.run_step import RunStep





T = TypeVar("T", bound="RunDetail")



@_attrs_define
class RunDetail:
    """ 
        Attributes:
            run_id (str):
            steps (list[RunStep]):
            started_at (datetime.datetime | Unset):
     """

    run_id: str
    steps: list[RunStep]
    started_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_step import RunStep # noqa: PLC0415
        run_id = self.run_id

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)



        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "runId": run_id,
            "steps": steps,
        })
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_step import RunStep # noqa: PLC0415
        d = dict(src_dict)
        run_id = d.pop("runId")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in (_steps):
            steps_item = RunStep.from_dict(steps_item_data)



            steps.append(steps_item)


        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        run_detail = cls(
            run_id=run_id,
            steps=steps,
            started_at=started_at,
        )


        run_detail.additional_properties = d
        return run_detail

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
