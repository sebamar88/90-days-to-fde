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


def test_audit_event_drops_raw_content_and_unknown_fields() -> None:
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

    safe = sanitize_audit_event(event)

    assert safe == {
        "event_type": "tool_denied",
        "request_id": "req-syn-01",
        "correlation_id": "trace-syn-01",
        "outcome": "denied",
    }
    assert "secret-test-value" not in repr(safe)


def test_audit_event_rejects_empty_required_identifiers() -> None:
    with pytest.raises(ValueError, match="request_id"):
        sanitize_audit_event({"event_type": "approved", "request_id": ""})
