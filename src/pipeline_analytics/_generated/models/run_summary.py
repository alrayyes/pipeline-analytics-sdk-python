from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.outcome import Outcome
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.run_step import RunStep





T = TypeVar("T", bound="RunSummary")



@_attrs_define
class RunSummary:
    """ 
        Attributes:
            id (str):
            pipeline_id (str):
            pipeline_name (str):
            repo_id (str):
            status (str): The forge's run status, as recorded.
            outcome (Outcome): What a run's or step's forge state means, computed by the server so no client interprets
                status strings. `failed` covers a `failure` or `timed_out` conclusion; a conclusion wins over a stale status;
                `running` and `queued` are work still pending (the run list's `running` filter covers both); a state the server
                doesn't recognise is `unknown`, never `passed`.
            steps (list[RunStep]): The run's steps in recorded order.
            conclusion (str | Unset): Absent until the run concludes.
            started_at (datetime.datetime | Unset):
            duration_seconds (float | Unset): Absent while the run is still going or has no recorded end.
            branch (str | Unset): Absent on runs ingested before commit metadata was recorded.
            sha (str | Unset): Head commit SHA. Absent where the forge or an older row lacks it.
            message (str | Unset): First line of the head commit message.
            actor (str | Unset): The triggering user or bot.
            forge_url (str | Unset): Deep link to the run on the originating forge.
     """

    id: str
    pipeline_id: str
    pipeline_name: str
    repo_id: str
    status: str
    outcome: Outcome
    steps: list[RunStep]
    conclusion: str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    duration_seconds: float | Unset = UNSET
    branch: str | Unset = UNSET
    sha: str | Unset = UNSET
    message: str | Unset = UNSET
    actor: str | Unset = UNSET
    forge_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_step import RunStep # noqa: PLC0415
        id = self.id

        pipeline_id = self.pipeline_id

        pipeline_name = self.pipeline_name

        repo_id = self.repo_id

        status = self.status

        outcome = self.outcome.value

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)



        conclusion = self.conclusion

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        duration_seconds = self.duration_seconds

        branch = self.branch

        sha = self.sha

        message = self.message

        actor = self.actor

        forge_url = self.forge_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "pipelineId": pipeline_id,
            "pipelineName": pipeline_name,
            "repoId": repo_id,
            "status": status,
            "outcome": outcome,
            "steps": steps,
        })
        if conclusion is not UNSET:
            field_dict["conclusion"] = conclusion
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if branch is not UNSET:
            field_dict["branch"] = branch
        if sha is not UNSET:
            field_dict["sha"] = sha
        if message is not UNSET:
            field_dict["message"] = message
        if actor is not UNSET:
            field_dict["actor"] = actor
        if forge_url is not UNSET:
            field_dict["forgeUrl"] = forge_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_step import RunStep # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        pipeline_id = d.pop("pipelineId")

        pipeline_name = d.pop("pipelineName")

        repo_id = d.pop("repoId")

        status = d.pop("status")

        outcome = Outcome(d.pop("outcome"))




        steps = []
        _steps = d.pop("steps")
        for steps_item_data in (_steps):
            steps_item = RunStep.from_dict(steps_item_data)



            steps.append(steps_item)


        conclusion = d.pop("conclusion", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        duration_seconds = d.pop("durationSeconds", UNSET)

        branch = d.pop("branch", UNSET)

        sha = d.pop("sha", UNSET)

        message = d.pop("message", UNSET)

        actor = d.pop("actor", UNSET)

        forge_url = d.pop("forgeUrl", UNSET)

        run_summary = cls(
            id=id,
            pipeline_id=pipeline_id,
            pipeline_name=pipeline_name,
            repo_id=repo_id,
            status=status,
            outcome=outcome,
            steps=steps,
            conclusion=conclusion,
            started_at=started_at,
            duration_seconds=duration_seconds,
            branch=branch,
            sha=sha,
            message=message,
            actor=actor,
            forge_url=forge_url,
        )


        run_summary.additional_properties = d
        return run_summary

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
