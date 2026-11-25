# Phase 2 — Production AI Engineering

**Days:** 16–30
**Status:** Lesson drafts are public preview, unreviewed, and not validated with learners. A local reference starter is provided; provider-backed model calls are optional.

## Phase outcome

Build and evaluate a small request-intake service that turns synthetic maintenance messages into reviewable drafts. The service must have a deterministic baseline, a provider boundary, schema validation, explicit abstention, and measured failure behavior. No model is allowed to create or route a real work order in this phase.

## Scenario

Continue with Meridian Facilities. The first phase proposed a draft-only intake helper because customer workflow, data controls, and system access are not yet validated. Phase 2 tests whether model-assisted extraction improves the coordinator's task over a rules baseline, using synthetic messages only.

## Stack and local path

The reference implementation follows the stack named in the project README: Python 3.12+, FastAPI, and Pydantic 2. The starter's default provider is deterministic and needs no API key. An optional local-model adapter can be added behind the same interface. Provider-specific examples are never required to complete the assessments.

## Cumulative deliverables

1. Runnable service with a stable input/output contract.
2. Deterministic rules baseline and synthetic evaluation set.
3. Provider adapter and validated typed output.
4. Ambiguity, missing-data, refusal, timeout, and malformed-output behavior.
5. A sandbox-only work-order boundary, prompt/schema versions, and cost/latency measurements.
6. A comparison report and reproducible local demo.

## Lessons

16. [Set up the service and contract](day-16.md) · 17. [Build a deterministic baseline](day-17.md) · 18. [Create a synthetic evaluation set](day-18.md) · 19. [Define a provider adapter](day-19.md) · 20. [Return schema-validated suggestions](day-20.md) · 21. [Abstain when the request is ambiguous](day-21.md) · 22. [Decide whether retrieval is justified](day-22.md) · 23. [Ground suggestions in approved knowledge](day-23.md) · 24. [Integrate with a work-order sandbox](day-24.md) · 25. [Bound retries and make writes idempotent](day-25.md) · 26. [Version prompts and schemas](day-26.md) · 27. [Measure latency and cost](day-27.md) · 28. [Compare model and rules baselines](day-28.md) · 29. [Package a repeatable local demo](day-29.md) · 30. [Phase review: production AI service](day-30.md)

## Phase gate

Pass when the learner can replay the same synthetic cases against the rules and optional model path, explain quality and operational trade-offs with measured evidence, validate all output before use, and demonstrate that ambiguous or unsafe requests stay in human review. A model that does not beat the baseline on the agreed task should not be retained just because it is more sophisticated.

## Lab and automated tests

Run the [Phase 2 starter tests](starter/tests/) from the [shared lab workspace](../labs/README.md). The all-phase CI workflow runs these tests together with Phases 1 and 3–6.
