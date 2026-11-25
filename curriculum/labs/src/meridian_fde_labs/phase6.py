"""End-to-end synthetic capstone orchestration for Phase 6."""

from __future__ import annotations

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
            prior_hash, result = prior
            if prior_hash != preview_hash:
                raise InvalidTransition("idempotency key reused with changed preview")
            preview = self.workflow.previews.get(request_id)
            if preview is None or self.workflow.approved_by.get(request_id) != actor.subject:
                raise AccessDenied("submission actor must own the approval")
            if actor.role != "coordinator" or actor.region != preview.region:
                raise AccessDenied("coordinator is not authorized for this site")
            if preview.preview_hash != preview_hash:
                raise InvalidTransition("preview changed; approval rejected")
            return dict(result)

        self.workflow.approve(request_id, actor, preview_hash)
        return self.workflow.submit(request_id, actor, idempotency_key)


def final_release_decision(
    evaluation: dict[str, object], operations: dict[str, object]
) -> dict[str, object]:
    blockers: list[str] = []
    if evaluation.get("release_pass") is not True:
        blockers.append("evaluation_failed")
    if operations.get("decision") != "proceed_to_review":
        blockers.extend(operations.get("blockers", ["operational_evidence_incomplete"]))
    return {
        "decision": "block" if blockers else "proceed_to_review",
        "blockers": sorted(set(blockers)),
    }
