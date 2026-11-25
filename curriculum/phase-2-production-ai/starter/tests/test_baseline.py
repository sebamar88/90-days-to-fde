from meridian_intake.baseline import RuleBasedProvider
from meridian_intake.models import Category, IntakeRequest, Urgency


def test_extracts_synthetic_location_and_plumbing_category() -> None:
    result = RuleBasedProvider().extract(
        IntakeRequest(request_id="syn-001", text="Building 12: active leak under the sink.")
    )

    assert result.location == "Building 12"
    assert result.category is Category.PLUMBING
    assert result.urgency is Urgency.URGENT
    assert result.review_required is True


def test_does_not_treat_smoke_detector_mention_as_emergency() -> None:
    result = RuleBasedProvider().extract(
        IntakeRequest(request_id="syn-006", text="The smoke detector needs a battery replacement in Building 3.")
    )

    assert result.urgency is Urgency.UNKNOWN
    assert "urgency" in result.missing_fields


def test_ambiguous_category_remains_unknown() -> None:
    result = RuleBasedProvider().extract(
        IntakeRequest(request_id="syn-007", text="Building 12 has a plumbing leak and an electrical outlet issue.")
    )

    assert result.category is Category.UNKNOWN
    assert "category" in result.missing_fields


def test_never_disables_human_review() -> None:
    result = RuleBasedProvider().extract(
        IntakeRequest(request_id="syn-005", text="There is a problem near the back room again.")
    )

    assert result.review_required is True
