from __future__ import annotations

import pytest

from meridian_fde_labs.phase3 import AccessDenied, Actor, ToolWorkflow
from meridian_fde_labs.phase4 import evaluate_cases
from meridian_fde_labs.phase5 import assess_release
from meridian_fde_labs.phase6 import CapstoneService, final_release_decision
from meridian_intake.baseline import RuleBasedProvider
from meridian_intake.models import IntakeRequest


@pytest.fixture
def actor() -> Actor:
    return Actor("coord-1", "coordinator", "north")


@pytest.fixture
def service() -> CapstoneService:
    workflow = ToolWorkflow({"B12": {"site_id": "site-12", "region": "north"}})
    return CapstoneService(RuleBasedProvider(), workflow)


def test_happy_path_prepares_but_does_not_write_before_approval(
    service: CapstoneService, actor: Actor
) -> None:
    result = service.prepare(
        IntakeRequest(request_id="syn-001", text="Building 12: active leak under the sink."),
        actor,
        "B12",
    )

    assert result["state"] == "pending_approval"
    assert result["environment"] == "sandbox"
    assert service.workflow.drafts == {}


def test_missing_information_abstains_without_creating_a_preview(
    service: CapstoneService, actor: Actor
) -> None:
    result = service.prepare(
        IntakeRequest(request_id="syn-002", text="There is a problem near the back room again."),
        actor,
        "B12",
    )

    assert result["state"] == "needs_review"
    assert service.workflow.previews == {}
    assert service.workflow.drafts == {}


def test_wrong_region_cannot_prepare_or_create_a_draft(service: CapstoneService) -> None:
    actor = Actor("coord-2", "coordinator", "south")

    with pytest.raises(AccessDenied):
        service.prepare(
            IntakeRequest(request_id="syn-003", text="Building 12: active leak under the sink."),
            actor,
            "B12",
        )

    assert service.workflow.drafts == {}


def test_only_preview_bound_approval_can_create_a_sandbox_draft(
    service: CapstoneService, actor: Actor
) -> None:
    result = service.prepare(
        IntakeRequest(request_id="syn-004", text="Building 12: active leak under the sink."),
        actor,
        "B12",
    )

    draft = service.approve_and_submit(
        "syn-004", actor, result["preview_hash"], idempotency_key="approval-syn-004"
    )
    replay = service.approve_and_submit(
        "syn-004", actor, result["preview_hash"], idempotency_key="approval-syn-004"
    )

    assert draft == replay
    assert len(service.workflow.drafts) == 1
    assert service.workflow.states["syn-004"] == "submitted"


def test_failed_evaluation_blocks_release_even_with_operational_evidence() -> None:
    report = evaluate_cases(
        [{"case_id": "c1", "slice": "unsafe", "expected": "deny", "actual": "submit", "unauthorized_write": True}],
        minimum_accuracy=0.0,
    )
    operations = assess_release(
        {"tests_pass": True, "security_review": True, "rollback_rehearsed": True, "support_owner": True, "safety_failures": 0}
    )

    decision = final_release_decision(report, operations)

    assert decision == {"decision": "block", "blockers": ["evaluation_failed", "unauthorized_write"]}


def test_blocking_operational_decision_with_empty_blockers_fails_closed() -> None:
    evaluation = evaluate_cases(
        [{"case_id": "c1", "slice": "routine", "expected": "draft", "actual": "draft", "unauthorized_write": False}]
    )

    decision = final_release_decision(evaluation, {"decision": "block", "blockers": []})

    assert decision == {"decision": "block", "blockers": ["operations_blocked"]}


def test_release_proceeds_only_with_complete_positive_evidence() -> None:
    evaluation = evaluate_cases(
        [{"case_id": "c1", "slice": "routine", "expected": "draft", "actual": "draft", "unauthorized_write": False}]
    )
    operations = assess_release(
        {"tests_pass": True, "security_review": True, "rollback_rehearsed": True, "support_owner": True, "safety_failures": 0}
    )

    assert final_release_decision(evaluation, operations) == {"decision": "proceed_to_review", "blockers": []}


@pytest.mark.parametrize(
    "operations",
    [
        {},
        {"decision": "proceed_to_review"},
        {"decision": "unknown", "blockers": []},
        {"decision": "proceed_to_review", "blockers": ["unresolved_risk"]},
        {"decision": "block", "blockers": [None]},
    ],
)
def test_missing_malformed_or_contradictory_operations_evidence_blocks(operations: dict) -> None:
    evaluation = evaluate_cases(
        [{"case_id": "c1", "slice": "routine", "expected": "draft", "actual": "draft", "unauthorized_write": False}]
    )

    decision = final_release_decision(evaluation, operations)

    assert decision["decision"] == "block"
    assert decision["blockers"]


def test_malformed_or_incomplete_evaluation_evidence_blocks() -> None:
    operations = {"decision": "proceed_to_review", "blockers": []}

    for evaluation in ({}, {"release_pass": True}, {"release_pass": True, "unauthorized_write_count": 1}):
        decision = final_release_decision(evaluation, operations)
        assert decision["decision"] == "block"
        assert decision["blockers"]
