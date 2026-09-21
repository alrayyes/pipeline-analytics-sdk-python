from enum import StrEnum

class SettingsUpdateForgeFilterType2Type1(StrEnum):
    ALL = "all"
    FORGEJO = "forgejo"
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
