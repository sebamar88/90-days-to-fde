"""Slice-aware evaluation and allowlist-based audit redaction for Phase 4."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
from datetime import datetime
import re
from typing import Any, Literal, NotRequired, TypedDict, get_type_hints


class AuditEvent(TypedDict):
    """Structured audit fields; IDs must be opaque references, never user content."""

    event_type: Literal[
        "tool_denied", "preview_prepared", "approval_granted", "submission_completed",
        "submission_replayed", "workflow_cancelled", "release_blocked", "release_proposed",
    ]
    request_id: str
    timestamp: NotRequired[str]
    actor_id: NotRequired[str]
    correlation_id: NotRequired[str]
    state: NotRequired[Literal["needs_review", "pending_approval", "approved", "cancelled", "submitted", "blocked"]]
    policy_version: NotRequired[str]
    outcome: NotRequired[Literal["allowed", "denied", "success", "failure", "blocked"]]
    reason_code: NotRequired[
        Literal[
            "approval_recorded", "policy_denied", "preview_changed", "provider_timeout",
            "provider_unavailable", "invalid_provider_output", "evaluation_failed",
            "operations_blocked", "operational_evidence_incomplete", "safety_failure",
            "unauthorized_actor", "invalid_transition",
        ]
    ]


AUDIT_SCHEMA = get_type_hints(AuditEvent)
AUDIT_FIELDS = frozenset(AUDIT_SCHEMA)
AUDIT_EVENT_TYPES = frozenset(AUDIT_SCHEMA["event_type"].__args__)
AUDIT_STATES = frozenset(AUDIT_SCHEMA["state"].__args__)
AUDIT_OUTCOMES = frozenset(AUDIT_SCHEMA["outcome"].__args__)
AUDIT_REASON_CODES = frozenset(AUDIT_SCHEMA["reason_code"].__args__)
OPAQUE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,79}$")
POLICY_VERSION = re.compile(r"^v\d+(?:\.\d+){0,2}$")


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


def sanitize_audit_event(event: Mapping[str, Any]) -> dict[str, str]:
    """Validate an allowlisted event schema; never accept freeform log values."""
    if not isinstance(event, Mapping):
        raise ValueError("audit event must be a mapping")
    unknown = set(event) - AUDIT_FIELDS
    if unknown:
        raise ValueError(f"unknown audit fields: {', '.join(sorted(map(str, unknown)))}")
    for required in ("event_type", "request_id"):
        if required not in event:
            raise ValueError(f"audit event requires {required}")
    request_id = event["request_id"]
    if not isinstance(request_id, str) or not request_id or len(request_id) > 80 or not OPAQUE_ID.fullmatch(request_id):
        raise ValueError("audit request_id must be a bounded opaque identifier")
    if not isinstance(event["event_type"], str) or event["event_type"] not in AUDIT_EVENT_TYPES:
        raise ValueError("audit event_type is unsupported")

    safe: dict[str, str] = {}
    for key, value in event.items():
        if not isinstance(key, str) or not isinstance(value, str) or not value or value.strip() != value:
            raise ValueError(f"audit field {key!r} must be a non-empty string without surrounding whitespace")
        if key in {"request_id", "actor_id", "correlation_id"}:
            if len(value) > 80 or not OPAQUE_ID.fullmatch(value):
                raise ValueError(f"audit field {key} must be a bounded opaque identifier")
        elif key == "event_type" and value not in AUDIT_EVENT_TYPES:
            raise ValueError("audit event_type is unsupported")
        elif key == "state" and value not in AUDIT_STATES:
            raise ValueError("audit state is unsupported")
        elif key == "outcome" and value not in AUDIT_OUTCOMES:
            raise ValueError("audit outcome is unsupported")
        elif key == "reason_code" and value not in AUDIT_REASON_CODES:
            raise ValueError("audit reason_code is unsupported")
        elif key == "policy_version" and not POLICY_VERSION.fullmatch(value):
            raise ValueError("audit policy_version must use vN or vN.N[.N] format")
        elif key == "timestamp":
            try:
                parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError as exc:
                raise ValueError("audit timestamp must be ISO 8601") from exc
            if parsed.tzinfo is None or parsed.utcoffset() is None:
                raise ValueError("audit timestamp must include a timezone")
        safe[key] = value
    return safe
