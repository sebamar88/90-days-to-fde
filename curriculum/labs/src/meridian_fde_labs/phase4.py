"""Slice-aware evaluation and allowlist-based audit redaction for Phase 4."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
from typing import Any


SAFE_AUDIT_FIELDS = {
    "event_type",
    "timestamp",
    "actor_id",
    "request_id",
    "correlation_id",
    "state",
    "policy_version",
    "outcome",
    "reason_code",
}


def evaluate_cases(
    cases: Sequence[Mapping[str, Any]], *, minimum_accuracy: float = 0.8
) -> dict[str, Any]:
    """Return total and per-slice accuracy; unauthorized writes always block release."""
    if not cases:
        raise ValueError("evaluation requires at least one case")
    if not 0 <= minimum_accuracy <= 1:
        raise ValueError("minimum_accuracy must be between 0 and 1")

    seen: set[str] = set()
    correct = 0
    unauthorized_writes = 0
    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for index, case in enumerate(cases):
        case_id = case.get("case_id")
        slice_name = case.get("slice")
        if not isinstance(case_id, str) or not case_id.strip():
            raise ValueError(f"case {index + 1} has invalid case_id")
        if case_id in seen:
            raise ValueError(f"duplicate case_id: {case_id}")
        seen.add(case_id)
        if not isinstance(slice_name, str) or not slice_name.strip():
            raise ValueError(f"case {case_id} has invalid slice")
        if "expected" not in case or "actual" not in case:
            raise ValueError(f"case {case_id} must include expected and actual")
        if not isinstance(case.get("unauthorized_write"), bool):
            raise ValueError(f"case {case_id} must state unauthorized_write")

        is_correct = case["expected"] == case["actual"]
        correct += int(is_correct)
        unauthorized_writes += int(case["unauthorized_write"])
        counts[slice_name][0] += 1
        counts[slice_name][1] += int(is_correct)

    accuracy = correct / len(cases)
    slices = {
        name: {
            "count": count,
            "correct": slice_correct,
            "accuracy": slice_correct / count,
        }
        for name, (count, slice_correct) in sorted(counts.items())
    }
    return {
        "case_count": len(cases),
        "correct": correct,
        "accuracy": accuracy,
        "unauthorized_write_count": unauthorized_writes,
        "slices": slices,
        "release_pass": accuracy >= minimum_accuracy and unauthorized_writes == 0,
    }


def sanitize_audit_event(event: Mapping[str, Any]) -> dict[str, str | int | bool]:
    """Keep only low-risk scalar fields from a workflow event."""
    safe: dict[str, str | int | bool] = {}
    for key in SAFE_AUDIT_FIELDS:
        value = event.get(key)
        if isinstance(value, bool) or isinstance(value, int):
            safe[key] = value
        elif isinstance(value, str) and value.strip():
            safe[key] = value.strip()
    for required in ("event_type", "request_id"):
        if required not in safe:
            raise ValueError(f"audit event requires {required}")
    return safe
