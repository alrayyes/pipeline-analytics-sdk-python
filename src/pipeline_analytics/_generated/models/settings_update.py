from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.settings_update_forge_filter_type_1 import SettingsUpdateForgeFilterType1
from ..models.settings_update_forge_filter_type_2_type_1 import SettingsUpdateForgeFilterType2Type1
from ..models.settings_update_forge_filter_type_3_type_1 import SettingsUpdateForgeFilterType3Type1
from ..models.settings_update_pipelines_health_filter_type_1 import SettingsUpdatePipelinesHealthFilterType1
from ..models.settings_update_pipelines_health_filter_type_2_type_1 import SettingsUpdatePipelinesHealthFilterType2Type1
from ..models.settings_update_pipelines_health_filter_type_3_type_1 import SettingsUpdatePipelinesHealthFilterType3Type1
from ..models.settings_update_pipelines_sort_order_type_1 import SettingsUpdatePipelinesSortOrderType1
from ..models.settings_update_pipelines_sort_order_type_2_type_1 import SettingsUpdatePipelinesSortOrderType2Type1
from ..models.settings_update_pipelines_sort_order_type_3_type_1 import SettingsUpdatePipelinesSortOrderType3Type1
from ..models.settings_update_theme_type_1 import SettingsUpdateThemeType1
from ..models.settings_update_theme_type_2_type_1 import SettingsUpdateThemeType2Type1
from ..models.settings_update_theme_type_3_type_1 import SettingsUpdateThemeType3Type1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SettingsUpdate")



@_attrs_define
class SettingsUpdate:
    """ Every property is optional; an absent one is left untouched. A property set to null clears it back to its documented
    default instead of setting it.

        Attributes:
            theme (None | SettingsUpdateThemeType1 | SettingsUpdateThemeType2Type1 | SettingsUpdateThemeType3Type1 | Unset):
            forge_filter (None | SettingsUpdateForgeFilterType1 | SettingsUpdateForgeFilterType2Type1 |
                SettingsUpdateForgeFilterType3Type1 | Unset):
            pipelines_health_filter (None | SettingsUpdatePipelinesHealthFilterType1 |
                SettingsUpdatePipelinesHealthFilterType2Type1 | SettingsUpdatePipelinesHealthFilterType3Type1 | Unset):
            pipelines_repo_selector (None | str | Unset):
            pipelines_sort_order (None | SettingsUpdatePipelinesSortOrderType1 | SettingsUpdatePipelinesSortOrderType2Type1
                | SettingsUpdatePipelinesSortOrderType3Type1 | Unset):
     """

    theme: None | SettingsUpdateThemeType1 | SettingsUpdateThemeType2Type1 | SettingsUpdateThemeType3Type1 | Unset = UNSET
    forge_filter: None | SettingsUpdateForgeFilterType1 | SettingsUpdateForgeFilterType2Type1 | SettingsUpdateForgeFilterType3Type1 | Unset = UNSET
    pipelines_health_filter: None | SettingsUpdatePipelinesHealthFilterType1 | SettingsUpdatePipelinesHealthFilterType2Type1 | SettingsUpdatePipelinesHealthFilterType3Type1 | Unset = UNSET
    pipelines_repo_selector: None | str | Unset = UNSET
    pipelines_sort_order: None | SettingsUpdatePipelinesSortOrderType1 | SettingsUpdatePipelinesSortOrderType2Type1 | SettingsUpdatePipelinesSortOrderType3Type1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        theme: None | str | Unset
        if isinstance(self.theme, Unset):
            theme = UNSET
        elif isinstance(self.theme, SettingsUpdateThemeType1):
            theme = self.theme.value
        elif isinstance(self.theme, SettingsUpdateThemeType2Type1):
            theme = self.theme.value
        elif isinstance(self.theme, SettingsUpdateThemeType3Type1):
            theme = self.theme.value
        else:
            theme = self.theme

        forge_filter: None | str | Unset
        if isinstance(self.forge_filter, Unset):
            forge_filter = UNSET
        elif isinstance(self.forge_filter, SettingsUpdateForgeFilterType1):
            forge_filter = self.forge_filter.value
        elif isinstance(self.forge_filter, SettingsUpdateForgeFilterType2Type1):
            forge_filter = self.forge_filter.value
        elif isinstance(self.forge_filter, SettingsUpdateForgeFilterType3Type1):
            forge_filter = self.forge_filter.value
        else:
            forge_filter = self.forge_filter

        pipelines_health_filter: None | str | Unset
        if isinstance(self.pipelines_health_filter, Unset):
            pipelines_health_filter = UNSET
        elif isinstance(self.pipelines_health_filter, SettingsUpdatePipelinesHealthFilterType1):
            pipelines_health_filter = self.pipelines_health_filter.value
        elif isinstance(self.pipelines_health_filter, SettingsUpdatePipelinesHealthFilterType2Type1):
            pipelines_health_filter = self.pipelines_health_filter.value
        elif isinstance(self.pipelines_health_filter, SettingsUpdatePipelinesHealthFilterType3Type1):
            pipelines_health_filter = self.pipelines_health_filter.value
        else:
            pipelines_health_filter = self.pipelines_health_filter

        pipelines_repo_selector: None | str | Unset
        if isinstance(self.pipelines_repo_selector, Unset):
            pipelines_repo_selector = UNSET
        else:
            pipelines_repo_selector = self.pipelines_repo_selector

        pipelines_sort_order: None | str | Unset
        if isinstance(self.pipelines_sort_order, Unset):
            pipelines_sort_order = UNSET
        elif isinstance(self.pipelines_sort_order, SettingsUpdatePipelinesSortOrderType1):
            pipelines_sort_order = self.pipelines_sort_order.value
        elif isinstance(self.pipelines_sort_order, SettingsUpdatePipelinesSortOrderType2Type1):
            pipelines_sort_order = self.pipelines_sort_order.value
        elif isinstance(self.pipelines_sort_order, SettingsUpdatePipelinesSortOrderType3Type1):
            pipelines_sort_order = self.pipelines_sort_order.value
        else:
            pipelines_sort_order = self.pipelines_sort_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if theme is not UNSET:
            field_dict["theme"] = theme
        if forge_filter is not UNSET:
            field_dict["forgeFilter"] = forge_filter
        if pipelines_health_filter is not UNSET:
            field_dict["pipelinesHealthFilter"] = pipelines_health_filter
        if pipelines_repo_selector is not UNSET:
            field_dict["pipelinesRepoSelector"] = pipelines_repo_selector
        if pipelines_sort_order is not UNSET:
            field_dict["pipelinesSortOrder"] = pipelines_sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_theme(data: object) -> None | SettingsUpdateThemeType1 | SettingsUpdateThemeType2Type1 | SettingsUpdateThemeType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                theme_type_1 = SettingsUpdateThemeType1(data)



                return theme_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                theme_type_2_type_1 = SettingsUpdateThemeType2Type1(data)



                return theme_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                theme_type_3_type_1 = SettingsUpdateThemeType3Type1(data)



                return theme_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SettingsUpdateThemeType1 | SettingsUpdateThemeType2Type1 | SettingsUpdateThemeType3Type1 | Unset, data)

        theme = _parse_theme(d.pop("theme", UNSET))


        def _parse_forge_filter(data: object) -> None | SettingsUpdateForgeFilterType1 | SettingsUpdateForgeFilterType2Type1 | SettingsUpdateForgeFilterType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                forge_filter_type_1 = SettingsUpdateForgeFilterType1(data)



                return forge_filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                forge_filter_type_2_type_1 = SettingsUpdateForgeFilterType2Type1(data)



                return forge_filter_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                forge_filter_type_3_type_1 = SettingsUpdateForgeFilterType3Type1(data)



                return forge_filter_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SettingsUpdateForgeFilterType1 | SettingsUpdateForgeFilterType2Type1 | SettingsUpdateForgeFilterType3Type1 | Unset, data)

        forge_filter = _parse_forge_filter(d.pop("forgeFilter", UNSET))


        def _parse_pipelines_health_filter(data: object) -> None | SettingsUpdatePipelinesHealthFilterType1 | SettingsUpdatePipelinesHealthFilterType2Type1 | SettingsUpdatePipelinesHealthFilterType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pipelines_health_filter_type_1 = SettingsUpdatePipelinesHealthFilterType1(data)



                return pipelines_health_filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pipelines_health_filter_type_2_type_1 = SettingsUpdatePipelinesHealthFilterType2Type1(data)



                return pipelines_health_filter_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pipelines_health_filter_type_3_type_1 = SettingsUpdatePipelinesHealthFilterType3Type1(data)



                return pipelines_health_filter_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SettingsUpdatePipelinesHealthFilterType1 | SettingsUpdatePipelinesHealthFilterType2Type1 | SettingsUpdatePipelinesHealthFilterType3Type1 | Unset, data)

        pipelines_health_filter = _parse_pipelines_health_filter(d.pop("pipelinesHealthFilter", UNSET))


        def _parse_pipelines_repo_selector(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pipelines_repo_selector = _parse_pipelines_repo_selector(d.pop("pipelinesRepoSelector", UNSET))


        def _parse_pipelines_sort_order(data: object) -> None | SettingsUpdatePipelinesSortOrderType1 | SettingsUpdatePipelinesSortOrderType2Type1 | SettingsUpdatePipelinesSortOrderType3Type1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pipelines_sort_order_type_1 = SettingsUpdatePipelinesSortOrderType1(data)



                return pipelines_sort_order_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pipelines_sort_order_type_2_type_1 = SettingsUpdatePipelinesSortOrderType2Type1(data)



                return pipelines_sort_order_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pipelines_sort_order_type_3_type_1 = SettingsUpdatePipelinesSortOrderType3Type1(data)



                return pipelines_sort_order_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SettingsUpdatePipelinesSortOrderType1 | SettingsUpdatePipelinesSortOrderType2Type1 | SettingsUpdatePipelinesSortOrderType3Type1 | Unset, data)

        pipelines_sort_order = _parse_pipelines_sort_order(d.pop("pipelinesSortOrder", UNSET))


        settings_update = cls(
            theme=theme,
            forge_filter=forge_filter,
            pipelines_health_filter=pipelines_health_filter,
            pipelines_repo_selector=pipelines_repo_selector,
            pipelines_sort_order=pipelines_sort_order,
        )


        settings_update.additional_properties = d
        return settings_update

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
