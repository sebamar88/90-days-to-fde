import json
from pathlib import Path

from meridian_intake.baseline import RuleBasedProvider
from meridian_intake.models import IntakeRequest


DATASET = Path(__file__).parents[1] / "data" / "evaluation.jsonl"


def test_rules_baseline_matches_all_labeled_synthetic_cases() -> None:
    provider = RuleBasedProvider()
    cases = [json.loads(line) for line in DATASET.read_text(encoding="utf-8").splitlines() if line.strip()]

    assert len(cases) >= 8
    for case in cases:
        result = provider.extract(IntakeRequest(request_id=case["case_id"], text=case["text"]))
        assert result.category.value == case["expected_category"], case["case_id"]
        assert result.location == case["expected_location"], case["case_id"]
        assert result.urgency.value == case["expected_urgency"], case["case_id"]
        assert result.missing_fields == case["expected_missing_fields"], case["case_id"]
