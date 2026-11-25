"""End-to-end synthetic capstone orchestration for Phase 6."""

from __future__ import annotations

import math
import re
from collections.abc import Mapping
from typing import Protocol

from meridian_fde_labs.phase3 import AccessDenied, Actor, InvalidTransition, ToolWorkflow
from meridian_intake.models import IntakeRequest, IntakeSuggestion


class IntakeProvider(Protocol):
    def extract(self, request: IntakeRequest) -> IntakeSuggestion: ...


class CapstoneService:
    def __init__(self, provider: IntakeProvider, workflow: ToolWorkflow) -> None:
        self.provider = provider
        self.workflow = workflow

    def prepare(self, request: IntakeRequest, actor: Actor, site_code: str) -> dict[str, object]:
        suggestion = self.provider.extract(request)
        serialized = suggestion.model_dump(mode="json")
        if suggestion.missing_fields:
            return {
                "state": "needs_review",
                "missing_fields": list(suggestion.missing_fields),
                "suggestion": serialized,
            }

        preview = self.workflow.prepare(
            request.request_id,
            actor,
            site_code,
            {
                "category": suggestion.category.value,
                "urgency": suggestion.urgency.value,
                "summary": suggestion.summary,
            },
        )
        return {
            "state": self.workflow.states[request.request_id],
            "environment": preview.environment,
            "preview_hash": preview.preview_hash,
            "site_id": preview.site_id,
            "suggestion": serialized,
        }

    def approve_and_submit(
        self,
        request_id: str,
        actor: Actor,
        preview_hash: str,
        *,
        idempotency_key: str,
    ) -> dict[str, str]:
        prior = self.workflow.idempotency.get(idempotency_key)
        if prior:
            preview = self.workflow.previews.get(request_id)
            if preview is None or preview.preview_hash != preview_hash:
                raise InvalidTransition("preview changed; approval rejected")
            return self.workflow.submit(request_id, actor, idempotency_key)

        self.workflow.approve(request_id, actor, preview_hash)
        return self.workflow.submit(request_id, actor, idempotency_key)


def final_release_decision(
    evaluation: Mapping[str, object], operations: Mapping[str, object]
) -> dict[str, object]:
    blockers: list[str] = []

    if not isinstance(evaluation, Mapping):
        blockers.append("evaluation_evidence_invalid")
    else:
        case_count = evaluation.get("case_count")
        accuracy = evaluation.get("accuracy")
        unauthorized_writes = evaluation.get("unauthorized_write_count")
        if (
            not isinstance(case_count, int)
            or isinstance(case_count, bool)
            or case_count < 1
            or not isinstance(accuracy, (int, float))
            or isinstance(accuracy, bool)
            or not 0 <= accuracy <= 1
            or not math.isfinite(accuracy)
            or not isinstance(unauthorized_writes, int)
            or isinstance(unauthorized_writes, bool)
            or unauthorized_writes < 0
        ):
            blockers.append("evaluation_evidence_invalid")
        if evaluation.get("release_pass") is not True:
            blockers.append("evaluation_failed")
        if isinstance(unauthorized_writes, int) and not isinstance(unauthorized_writes, bool) and unauthorized_writes > 0:
            blockers.append("unauthorized_write")

    if not isinstance(operations, Mapping) or set(operations) != {"decision", "blockers"}:
        blockers.append("operational_evidence_invalid")
    else:
        decision = operations.get("decision")
        raw_blockers = operations.get("blockers")
        valid_blockers = (
            isinstance(raw_blockers, list)
            and all(isinstance(item, str) and re.fullmatch(r"[a-z][a-z0-9_]{0,63}", item) for item in raw_blockers)
            and len(set(raw_blockers)) == len(raw_blockers)
        )
        if not valid_blockers:
            blockers.append("operational_evidence_invalid")
        elif decision == "proceed_to_review" and not raw_blockers:
            pass
        elif decision == "block":
            blockers.extend(raw_blockers or ["operations_blocked"])
        elif decision == "proceed_to_review":
            blockers.append("operational_evidence_contradictory")
            blockers.extend(raw_blockers)
        else:
            blockers.append("operational_decision_invalid")

    if not blockers:
        return {"decision": "proceed_to_review", "blockers": []}

    return {
        "decision": "block",
        "blockers": sorted(set(blockers)),
    }
