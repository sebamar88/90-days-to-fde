"""Deployment-plan and release checks for the Phase 5 delivery lab."""

from __future__ import annotations

import math
from collections.abc import Mapping
from typing import Any


def validate_deployment_plan(plan: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    shape = plan.get("shape")
    if shape not in {"local", "customer_hosted", "managed"}:
        errors.append("shape must be local, customer_hosted, or managed")
    if not plan.get("config_source"):
        errors.append("config_source is required")
    secret_source = plan.get("secret_source")
    if secret_source == "repository":
        errors.append("secrets must not be stored in the repository")
    elif secret_source not in {"none", "environment", "secret_manager", "platform_secret_store"}:
        errors.append("secret_source is unsupported")
    if not secret_source:
        errors.append("secret_source must be explicit, including none for local labs")
    if shape == "local":
        if plan.get("setup_documented") is not True:
            errors.append("local setup must be documented")
        if plan.get("teardown_documented") is not True:
            errors.append("local teardown must be documented")
    if shape in {"customer_hosted", "managed"}:
        for field in ("owner", "data_residency", "rollback", "support_runbook", "monitoring"):
            if not plan.get(field):
                errors.append(f"{field} is required for a hosted deployment")
    return errors


def assess_release(evidence: Mapping[str, Any]) -> dict[str, Any]:
    """Block on missing operational evidence or any safety-critical regression."""
    blockers = [
        name
        for name in ("tests_pass", "security_review", "rollback_rehearsed", "support_owner")
        if evidence.get(name) is not True
    ]
    failures = evidence.get("safety_failures")
    if not isinstance(failures, int) or isinstance(failures, bool) or failures < 0:
        blockers.append("safety_failure_count_invalid")
    elif failures:
        blockers.append("safety_failure")
    return {
        "decision": "block" if blockers else "proceed_to_review",
        "blockers": blockers,
    }


def estimate_monthly_cost(
    *, requests: int, cost_per_request: float, fixed_cost: float, support_hours: float, hourly_rate: float
) -> dict[str, float]:
    values = (cost_per_request, fixed_cost, support_hours, hourly_rate)
    if requests < 0 or any(not math.isfinite(value) or value < 0 for value in values):
        raise ValueError("cost inputs must be finite and non-negative")
    usage = requests * cost_per_request
    support = support_hours * hourly_rate
    return {
        "usage": round(usage, 2),
        "fixed": round(fixed_cost, 2),
        "support": round(support, 2),
        "total": round(usage + fixed_cost + support, 2),
    }
