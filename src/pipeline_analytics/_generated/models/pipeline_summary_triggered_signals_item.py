from enum import StrEnum

class PipelineSummaryTriggeredSignalsItem(StrEnum):
    DURATION_REGRESSION = "duration_regression"
    FAILURE_RATE = "failure_rate"
    FLAKY_STEP = "flaky_step"

    def __str__(self) -> str:
        return str(self.value)
