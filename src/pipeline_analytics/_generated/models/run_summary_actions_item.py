from enum import StrEnum

class RunSummaryActionsItem(StrEnum):
    CANCEL = "cancel"
    RERUN = "rerun"

    def __str__(self) -> str:
        return str(self.value)
