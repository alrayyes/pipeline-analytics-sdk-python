from enum import StrEnum

class Outcome(StrEnum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    PASSED = "passed"
    QUEUED = "queued"
    RUNNING = "running"
    SKIPPED = "skipped"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
