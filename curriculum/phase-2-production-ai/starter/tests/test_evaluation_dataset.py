import json
from pathlib import Path

from meridian_intake.baseline import RuleBasedProvider
from meridian_intake.models import IntakeRequest


DATASET = Path(__file__).parents[1] / "data" / "evaluation.jsonl"


def test_development_cases_match_the_current_rules_baseline() -> None:
    provider = RuleBasedProvider()
    cases = [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]
    cases = [case for case in cases if case["split"] == "development"]

    assert len(cases) >= 4
    for case in cases:
        result = provider.extract(IntakeRequest(request_id=case["case_id"], text=case["text"]))
        assert result.category.value == case["expected_category"], case["case_id"]
        assert result.location == case["expected_location"], case["case_id"]
        assert result.urgency.value == case["expected_urgency"], case["case_id"]
        assert result.missing_fields == case["expected_missing_fields"], case["case_id"]


def test_dataset_documents_development_and_holdout_splits() -> None:
    cases = [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]

    assert {case["split"] for case in cases} == {"development", "holdout"}
    assert all(case["rationale"].strip() for case in cases)
