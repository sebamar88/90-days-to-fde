---
day: 30
phase: 2
status: Ready
title: Phase review — production AI service
estimated_effort: 90–120 minutes
---

# Day 30 — Phase review: production AI service

## Why this matters

This phase succeeds when you can justify the system's boundary and measured behavior, including when not to use a model. A polished demo without evaluation or failure handling is not a production engineering result.

## Scenario

Present the Meridian draft-only service to an operations sponsor and a skeptical platform/security reviewer. Every record and metric is synthetic or locally measured.

## Outcomes

- Demonstrate the workflow, error paths, and human review boundary.
- Compare rules and model behavior with honest limitations.
- Recommend whether to proceed, revise, or keep the deterministic baseline.

## Exercise

Assemble Days 16–29. Demonstrate a routine request, missing location, ambiguous urgency, malformed provider output, timeout, and duplicate sandbox action. Present evaluation slices, latency/cost methodology, and the decision record. Identify the evidence still needed from a real customer before deployment.

## Deliverable

A reproducible service, evaluation report, ADRs, and a five-minute technical/customer playback.

## Assessment rubric

Score 0 (missing), 1 (partial), or 2 (evidenced) for: stable contract; deterministic baseline; synthetic data provenance; adapter/schema boundary; abstention and human review; integration/retry safety; evaluation quality; latency/cost measurement; reproducibility and communication. Pass at 14/18 with no zero for safety boundary or evaluation. Revise before Phase 3 if either is absent.

## Reflection

What result would convince you to remove the model from the design?
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
