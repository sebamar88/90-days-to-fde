from __future__ import annotations

import pytest
import json

from meridian_fde_labs.phase3 import (
    AccessDenied,
    Actor,
    InvalidTransition,
    ToolWorkflow,
    TransientDependencyError,
    retry_transient,
)


@pytest.fixture
def workflow() -> ToolWorkflow:
    return ToolWorkflow({"B12": {"site_id": "site-12", "region": "north"}})


@pytest.fixture
def coordinator() -> Actor:
    return Actor(subject="coord-1", role="coordinator", region="north")


def test_site_lookup_is_bounded_and_read_only(workflow: ToolWorkflow) -> None:
    before = workflow.snapshot()

    result = workflow.lookup_site("B12")

    assert result == {"site_id": "site-12", "region": "north"}
    assert workflow.snapshot() == before
    with pytest.raises(ValueError, match="invalid site code"):
        workflow.lookup_site("https://example.invalid")


def test_wrong_region_actor_cannot_prepare_preview(workflow: ToolWorkflow) -> None:
    actor = Actor(subject="coord-2", role="coordinator", region="south")

    with pytest.raises(AccessDenied):
        workflow.prepare("req-1", actor, "B12", {"category": "plumbing"})


def test_model_or_auditor_cannot_prepare_a_write(workflow: ToolWorkflow) -> None:
    actor = Actor(subject="agent", role="agent", region="north")

    with pytest.raises(AccessDenied):
        workflow.prepare("req-1", actor, "B12", {"category": "plumbing"})


def test_tool_rejects_unadvertised_fields(workflow: ToolWorkflow, coordinator: Actor) -> None:
    with pytest.raises(ValueError, match="unsupported draft field"):
        workflow.prepare("req-1", coordinator, "B12", {"category": "plumbing", "target_url": "https://bad.invalid"})


def test_approval_is_bound_to_exact_preview_and_actor(workflow: ToolWorkflow, coordinator: Actor) -> None:
    preview = workflow.prepare("req-1", coordinator, "B12", {"category": "plumbing"})

    with pytest.raises(InvalidTransition, match="preview changed"):
        workflow.approve("req-1", coordinator, "wrong-hash")
    workflow.approve("req-1", coordinator, preview.preview_hash)
    with pytest.raises(AccessDenied):
        workflow.submit("req-1", Actor("other", "coordinator", "north"), "op-1")


def test_submission_requires_approval(workflow: ToolWorkflow, coordinator: Actor) -> None:
    workflow.prepare("req-1", coordinator, "B12", {"category": "plumbing"})

    with pytest.raises(InvalidTransition, match="approval required"):
        workflow.submit("req-1", coordinator, "op-1")


def test_same_idempotency_key_replays_one_draft(workflow: ToolWorkflow, coordinator: Actor) -> None:
    preview = workflow.prepare("req-1", coordinator, "B12", {"category": "plumbing"})
    workflow.approve("req-1", coordinator, preview.preview_hash)

    first = workflow.submit("req-1", coordinator, "op-1")
    replay = workflow.submit("req-1", coordinator, "op-1")

    assert first == replay
    assert len(workflow.drafts) == 1


def test_idempotency_key_cannot_be_reused_for_another_payload(workflow: ToolWorkflow, coordinator: Actor) -> None:
    first = workflow.prepare("req-1", coordinator, "B12", {"category": "plumbing"})
    workflow.approve("req-1", coordinator, first.preview_hash)
    workflow.submit("req-1", coordinator, "op-1")
    second = workflow.prepare("req-2", coordinator, "B12", {"category": "electrical"})
    workflow.approve("req-2", coordinator, second.preview_hash)

    with pytest.raises(InvalidTransition, match="changed payload"):
        workflow.submit("req-2", coordinator, "op-1")


def test_cancelled_workflow_cannot_be_submitted(workflow: ToolWorkflow, coordinator: Actor) -> None:
    preview = workflow.prepare("req-1", coordinator, "B12", {"category": "plumbing"})
    workflow.approve("req-1", coordinator, preview.preview_hash)
    workflow.cancel("req-1", coordinator)

    with pytest.raises(InvalidTransition):
        workflow.submit("req-1", coordinator, "op-1")


def test_snapshot_can_resume_without_losing_approval(workflow: ToolWorkflow, coordinator: Actor) -> None:
    preview = workflow.prepare("req-1", coordinator, "B12", {"category": "plumbing"})
    workflow.approve("req-1", coordinator, preview.preview_hash)
    snapshot = json.loads(json.dumps(workflow.snapshot()))
    resumed = ToolWorkflow.restore(workflow.sites, snapshot)

    assert resumed.submit("req-1", coordinator, "op-1")["request_id"] == "req-1"


def test_preview_fields_cannot_be_mutated_after_creation(workflow: ToolWorkflow, coordinator: Actor) -> None:
    preview = workflow.prepare("req-immutable", coordinator, "B12", {"category": "plumbing"})

    with pytest.raises(TypeError):
        preview.fields["category"] = "electrical"

    workflow.approve("req-immutable", coordinator, preview.preview_hash)
    with pytest.raises(TypeError):
        preview.fields["category"] = "electrical"


def test_tampered_preview_snapshot_is_rejected(workflow: ToolWorkflow, coordinator: Actor) -> None:
    preview = workflow.prepare("req-tampered", coordinator, "B12", {"category": "plumbing"})
    snapshot = workflow.snapshot()
    snapshot["previews"]["req-tampered"]["fields"]["category"] = "electrical"

    with pytest.raises(ValueError, match="preview integrity"):
        ToolWorkflow.restore(workflow.sites, snapshot)


def test_cancelled_approval_cannot_be_reused_after_request_recreation(
    workflow: ToolWorkflow, coordinator: Actor
) -> None:
    first = workflow.prepare("req-recreate", coordinator, "B12", {"category": "plumbing"})
    workflow.approve("req-recreate", coordinator, first.preview_hash)
    workflow.cancel("req-recreate", coordinator)
    second = workflow.prepare("req-recreate", coordinator, "B12", {"category": "electrical"})

    with pytest.raises(InvalidTransition, match="approval required"):
        workflow.submit("req-recreate", coordinator, "op-recreated")

    workflow.approve("req-recreate", coordinator, second.preview_hash)
    assert workflow.submit("req-recreate", coordinator, "op-recreated")["request_id"] == "req-recreate"


def test_snapshot_rejects_malformed_workflow_state(workflow: ToolWorkflow, coordinator: Actor) -> None:
    workflow.prepare("req-invalid-state", coordinator, "B12", {"category": "plumbing"})
    snapshot = workflow.snapshot()
    snapshot["states"]["req-invalid-state"] = "approved_without_actor"

    with pytest.raises(ValueError, match="snapshot state"):
        ToolWorkflow.restore(workflow.sites, snapshot)


def test_replay_requires_the_same_authorized_actor(workflow: ToolWorkflow, coordinator: Actor) -> None:
    preview = workflow.prepare("req-replay-auth", coordinator, "B12", {"category": "plumbing"})
    workflow.approve("req-replay-auth", coordinator, preview.preview_hash)
    workflow.submit("req-replay-auth", coordinator, "op-replay-auth")

    with pytest.raises(AccessDenied):
        workflow.submit("req-replay-auth", Actor("coord-other", "coordinator", "north"), "op-replay-auth")


def test_snapshot_cannot_relabel_a_submitted_request_as_cancelled(
    workflow: ToolWorkflow, coordinator: Actor
) -> None:
    preview = workflow.prepare("req-tampered-state", coordinator, "B12", {"category": "plumbing"})
    workflow.approve("req-tampered-state", coordinator, preview.preview_hash)
    workflow.submit("req-tampered-state", coordinator, "op-tampered-state")
    snapshot = workflow.snapshot()
    snapshot["states"]["req-tampered-state"] = "cancelled"

    with pytest.raises(ValueError, match="approval state|submission state"):
        ToolWorkflow.restore(workflow.sites, snapshot)


def test_retry_stops_after_the_declared_attempt_budget() -> None:
    attempts = 0

    def unavailable() -> str:
        nonlocal attempts
        attempts += 1
        raise TransientDependencyError("temporary outage")

    with pytest.raises(TransientDependencyError):
        retry_transient(unavailable, max_attempts=3)

    assert attempts == 3


def test_retry_does_not_repeat_terminal_errors() -> None:
    attempts = 0

    def denied() -> str:
        nonlocal attempts
        attempts += 1
        raise PermissionError("denied")

    with pytest.raises(PermissionError):
        retry_transient(denied, max_attempts=3)

    assert attempts == 1
