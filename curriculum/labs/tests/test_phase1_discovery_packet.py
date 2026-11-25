from __future__ import annotations

import json
from pathlib import Path

import pytest

from meridian_fde_labs.phase1 import REQUIRED_ARTIFACTS, validate_discovery_packet


@pytest.fixture
def complete_packet() -> dict:
    return {
        "scenario": "synthetic_meridian",
        "artifacts": [
            {
                "day": day,
                "name": name,
                "evidence_status": "simulated",
                "content": f"Synthetic practice artifact for day {day}.",
            }
            for day, name in REQUIRED_ARTIFACTS.items()
        ],
    }


def test_published_reference_packet_passes() -> None:
    fixture = Path(__file__).parents[1] / "fixtures" / "phase1_packet.json"

    packet = json.loads(fixture.read_text(encoding="utf-8"))

    assert validate_discovery_packet(packet) == []


def test_complete_synthetic_packet_passes_structural_assessment(complete_packet: dict) -> None:
    assert validate_discovery_packet(complete_packet) == []


def test_missing_daily_artifact_is_reported(complete_packet: dict) -> None:
    complete_packet["artifacts"].pop(4)

    errors = validate_discovery_packet(complete_packet)

    assert any("day 5" in error and "missing" in error for error in errors)


def test_duplicate_daily_artifact_is_rejected(complete_packet: dict) -> None:
    complete_packet["artifacts"].append(complete_packet["artifacts"][0].copy())

    errors = validate_discovery_packet(complete_packet)

    assert any("duplicate artifact for day 1" in error for error in errors)


def test_observed_evidence_requires_a_source_and_consent(complete_packet: dict) -> None:
    complete_packet["artifacts"][0]["evidence_status"] = "observed"

    errors = validate_discovery_packet(complete_packet)

    assert any("day 1" in error and "source and consent" in error for error in errors)


def test_packet_cannot_label_synthetic_work_as_customer_validated(complete_packet: dict) -> None:
    complete_packet["artifacts"][0]["evidence_status"] = "customer_validated"

    errors = validate_discovery_packet(complete_packet)

    assert any("day 1" in error and "invalid evidence_status" in error for error in errors)


def test_empty_artifact_content_is_rejected(complete_packet: dict) -> None:
    complete_packet["artifacts"][2]["content"] = "  "

    errors = validate_discovery_packet(complete_packet)

    assert any("day 3" in error and "empty content" in error for error in errors)


def test_malformed_evidence_status_returns_an_error_instead_of_crashing(complete_packet: dict) -> None:
    complete_packet["artifacts"][0]["evidence_status"] = ["simulated"]

    errors = validate_discovery_packet(complete_packet)

    assert any("day 1" in error and "invalid evidence_status" in error for error in errors)
