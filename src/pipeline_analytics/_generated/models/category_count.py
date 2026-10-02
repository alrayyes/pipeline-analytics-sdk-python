from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.failure_category import FailureCategory






T = TypeVar("T", bound="CategoryCount")



@_attrs_define
class CategoryCount:
    """ 
        Attributes:
            category (FailureCategory):
            occurrences (int): Failed-step occurrences whose step falls in this category.
            share (float): Fraction in (0, 1] of all failed-step occurrences in the window; the categories' shares sum to 1.
     """

    category: FailureCategory
    occurrences: int
    share: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        occurrences = self.occurrences

        share = self.share


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "category": category,
            "occurrences": occurrences,
            "share": share,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = FailureCategory(d.pop("category"))




        occurrences = d.pop("occurrences")

        share = d.pop("share")

        category_count = cls(
            category=category,
            occurrences=occurrences,
            share=share,
        )


        category_count.additional_properties = d
        return category_count

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
