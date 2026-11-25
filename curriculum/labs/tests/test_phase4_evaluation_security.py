from __future__ import annotations

import pytest

from meridian_fde_labs.phase4 import evaluate_cases, sanitize_audit_event


@pytest.fixture
def cases() -> list[dict]:
    return [
        {"case_id": "c1", "slice": "routine", "expected": "lookup", "actual": "lookup", "unauthorized_write": False},
        {"case_id": "c2", "slice": "ambiguous", "expected": "abstain", "actual": "abstain", "unauthorized_write": False},
        {"case_id": "c3", "slice": "cross_region", "expected": "deny", "actual": "deny", "unauthorized_write": False},
    ]


def test_evaluation_reports_total_and_slice_denominators(cases: list[dict]) -> None:
    report = evaluate_cases(cases, minimum_accuracy=1.0)

    assert report["case_count"] == 3
    assert report["accuracy"] == 1.0
    assert report["slices"]["cross_region"] == {"count": 1, "correct": 1, "accuracy": 1.0}
    assert report["release_pass"] is True


def test_unsafe_action_fails_release_even_when_accuracy_is_high(cases: list[dict]) -> None:
    cases[0]["unauthorized_write"] = True

    report = evaluate_cases(cases, minimum_accuracy=0.5)

    assert report["accuracy"] == 1.0
    assert report["unauthorized_write_count"] == 1
    assert report["release_pass"] is False


def test_wrong_prediction_reduces_accuracy(cases: list[dict]) -> None:
    cases[1]["actual"] = "lookup"

    report = evaluate_cases(cases, minimum_accuracy=0.8)

    assert report["slices"]["ambiguous"]["accuracy"] == 0.0
    assert report["release_pass"] is False


def test_duplicate_case_ids_are_rejected(cases: list[dict]) -> None:
    cases.append(cases[0].copy())

    with pytest.raises(ValueError, match="duplicate case_id"):
        evaluate_cases(cases)


def test_empty_evaluation_is_rejected() -> None:
    with pytest.raises(ValueError, match="at least one case"):
        evaluate_cases([])


def test_audit_event_rejects_raw_content_and_unknown_fields() -> None:
    event = {
        "event_type": "tool_denied",
        "request_id": "req-syn-01",
        "correlation_id": "trace-syn-01",
        "outcome": "denied",
        "raw_text": "patient name and phone",
        "prompt": "ignore policy",
        "api_key": "secret-test-value",
        "unknown_payload": {"private": True},
    }

    with pytest.raises(ValueError, match="unknown audit fields"):
        sanitize_audit_event(event)


def test_audit_event_rejects_empty_required_identifiers() -> None:
    with pytest.raises(ValueError, match="request_id"):
        sanitize_audit_event({"event_type": "approved", "request_id": ""})


def test_audit_event_accepts_only_typed_allowlisted_values() -> None:
    event = {
        "event_type": "approval_granted",
        "timestamp": "2026-11-25T10:30:00Z",
        "actor_id": "actor-17",
        "request_id": "req-syn-01",
        "correlation_id": "trace-syn-01",
        "state": "approved",
        "policy_version": "v1.2",
        "outcome": "success",
        "reason_code": "approval_recorded",
    }

    assert sanitize_audit_event(event) == event


@pytest.mark.parametrize(
    "event",
    [
        {"event_type": "freeform customer email", "request_id": "req-01"},
        {"event_type": "approval_granted", "request_id": "req-01", "outcome": "probably fine"},
        {"event_type": "approval_granted", "request_id": "req-01", "actor_id": "person@example.com"},
        {"event_type": "approval_granted", "request_id": "req-01", "correlation_id": "x" * 200},
        {"event_type": "approval_granted", "request_id": "req-01", "timestamp": "yesterday"},
        {"event_type": "approval_granted", "request_id": "req-01", "state": 4},
        {"event_type": "approval_granted", "request_id": "req-01", "reason_code": "customer said call me"},
        {"event_type": "approval_granted", "request_id": "req-01", "policy_version": "current"},
    ],
)
def test_audit_event_rejects_freeform_invalid_or_oversized_values(event: dict) -> None:
    with pytest.raises(ValueError):
        sanitize_audit_event(event)
