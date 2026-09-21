from enum import StrEnum

class SettingsUpdateThemeType3Type1(StrEnum):
    DARK = "dark"
    LIGHT = "light"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
