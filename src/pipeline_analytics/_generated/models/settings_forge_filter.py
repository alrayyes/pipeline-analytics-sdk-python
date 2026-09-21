from enum import StrEnum

class SettingsForgeFilter(StrEnum):
    ALL = "all"
    FORGEJO = "forgejo"
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
