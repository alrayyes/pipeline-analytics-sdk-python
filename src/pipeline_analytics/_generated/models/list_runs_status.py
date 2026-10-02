from enum import StrEnum

class ListRunsStatus(StrEnum):
    ALL = "all"
    FAILED = "failed"
    RUNNING = "running"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
