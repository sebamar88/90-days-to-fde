"""Structural checks for the Phase 1 discovery packet.

These checks validate completeness and evidence labeling. They do not score
the quality of an interview, business judgment, or customer relationship.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


REQUIRED_ARTIFACTS: dict[int, str] = {
    1: "problem-brief",
    2: "stakeholder-map",
    3: "workflow-map",
    4: "interview-guide",
    5: "discovery-notes",
    6: "evidence-assumption-register",
    7: "outcome-and-guardrails",
    8: "data-access-constraints",
    9: "ai-fit-assessment",
    10: "solution-options",
    11: "system-context",
    12: "decision-record",
    13: "thin-slice-plan",
    14: "customer-playback",
    15: "phase-review",
}

ALLOWED_EVIDENCE_STATUSES = {"assumption", "simulated", "synthetic", "observed", "unknown"}


def validate_discovery_packet(packet: Mapping[str, Any]) -> list[str]:
    """Return structural errors for a Phase 1 learner packet, in stable order."""
    errors: list[str] = []
    if packet.get("scenario") != "synthetic_meridian":
        errors.append("scenario must be labeled synthetic_meridian")

    artifacts = packet.get("artifacts")
    if not isinstance(artifacts, list):
        return [*errors, "artifacts must be a list"]

    seen: set[int] = set()
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, Mapping):
            errors.append(f"artifact {index + 1} must be an object")
            continue
        day = artifact.get("day")
        if not isinstance(day, int) or isinstance(day, bool) or day not in REQUIRED_ARTIFACTS:
            errors.append(f"artifact {index + 1} has invalid day")
            continue
        if day in seen:
            errors.append(f"duplicate artifact for day {day}")
        seen.add(day)

        expected_name = REQUIRED_ARTIFACTS[day]
        if artifact.get("name") != expected_name:
            errors.append(f"day {day} artifact name must be {expected_name}")
        if not isinstance(artifact.get("content"), str) or not artifact["content"].strip():
            errors.append(f"day {day} has empty content")

        evidence_status = artifact.get("evidence_status")
        if not isinstance(evidence_status, str) or evidence_status not in ALLOWED_EVIDENCE_STATUSES:
            errors.append(f"day {day} has invalid evidence_status")
        elif evidence_status == "observed":
            if not artifact.get("source") or artifact.get("consent") is not True:
                errors.append(f"day {day} observed evidence requires source and consent")

    for day in REQUIRED_ARTIFACTS:
        if day not in seen:
            errors.append(f"missing artifact for day {day}")

    return errors
