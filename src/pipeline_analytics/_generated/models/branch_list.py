from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.branch_list_window import BranchListWindow
from typing import cast

if TYPE_CHECKING:
  from ..models.branch_entry import BranchEntry





T = TypeVar("T", bound="BranchList")



@_attrs_define
class BranchList:
    """ 
        Attributes:
            window (BranchListWindow): The window these counts cover: the requested one, or the server's default.
            branches (list[BranchEntry]):
     """

    window: BranchListWindow
    branches: list[BranchEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.branch_entry import BranchEntry # noqa: PLC0415
        window = self.window.value

        branches = []
        for branches_item_data in self.branches:
            branches_item = branches_item_data.to_dict()
            branches.append(branches_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "window": window,
            "branches": branches,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.branch_entry import BranchEntry # noqa: PLC0415
        d = dict(src_dict)
        window = BranchListWindow(d.pop("window"))




        branches = []
        _branches = d.pop("branches")
        for branches_item_data in (_branches):
            branches_item = BranchEntry.from_dict(branches_item_data)



            branches.append(branches_item)


        branch_list = cls(
            window=window,
            branches=branches,
        )


        branch_list.additional_properties = d
        return branch_list

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
