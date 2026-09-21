from enum import StrEnum

class SettingsUpdatePipelinesSortOrderType3Type1(StrEnum):
    LASTRUN = "lastRun"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
