from __future__ import annotations

from meridian_fde_labs.phase5 import assess_release, estimate_monthly_cost, validate_deployment_plan


def test_local_demo_can_run_without_secret_or_cloud_account() -> None:
    plan = {
        "shape": "local",
        "config_source": "environment",
        "secret_source": "none",
        "setup_documented": True,
        "teardown_documented": True,
    }

    assert validate_deployment_plan(plan) == []


def test_committed_secret_is_rejected_in_every_deployment_shape() -> None:
    plan = {
        "shape": "local",
        "config_source": "environment",
        "secret_source": "repository",
        "setup_documented": True,
        "teardown_documented": True,
    }

    assert any("must not be stored in the repository" in error for error in validate_deployment_plan(plan))


def test_unknown_secret_source_is_rejected() -> None:
    plan = {"shape": "local", "config_source": "environment", "secret_source": "magic"}

    assert any("secret_source is unsupported" in error for error in validate_deployment_plan(plan))


def test_managed_plan_requires_owner_data_residency_rollback_and_support() -> None:
    plan = {"shape": "managed", "config_source": "environment", "secret_source": "secret_manager"}

    errors = validate_deployment_plan(plan)

    for required in ("owner", "data_residency", "rollback", "support_runbook"):
        assert any(required in error for error in errors)


def test_release_gate_cannot_trade_away_safety_failure() -> None:
    evidence = {
        "tests_pass": True,
        "security_review": True,
        "rollback_rehearsed": True,
        "support_owner": True,
        "safety_failures": 1,
    }

    result = assess_release(evidence)

    assert result["decision"] == "block"
    assert "safety_failure" in result["blockers"]


def test_release_passes_only_when_all_required_evidence_exists() -> None:
    evidence = {
        "tests_pass": True,
        "security_review": True,
        "rollback_rehearsed": True,
        "support_owner": True,
        "safety_failures": 0,
    }

    assert assess_release(evidence) == {"decision": "proceed_to_review", "blockers": []}


def test_monthly_cost_estimate_exposes_component_totals() -> None:
    estimate = estimate_monthly_cost(
        requests=1_000,
        cost_per_request=0.002,
        fixed_cost=20.0,
        support_hours=2,
        hourly_rate=50.0,
    )

    assert estimate == {"usage": 2.0, "fixed": 20.0, "support": 100.0, "total": 122.0}


def test_negative_cost_input_is_rejected() -> None:
    import pytest

    with pytest.raises(ValueError, match="finite and non-negative"):
        estimate_monthly_cost(requests=1, cost_per_request=-1.0, fixed_cost=0, support_hours=0, hourly_rate=0)
