---
day: 36
phase: 3
status: Ready
title: Model workflow state and resumability
estimated_effort: 90–120 minutes
---

# Day 36 — Model workflow state and resumability

## Why this matters

Enterprise workflows outlive one process, request, or model call. Explicit state makes retries, review, cancellation, and recovery understandable.

## Scenario

A coordinator may pause after lookup, return later to approve a draft, or resume after a temporary sandbox outage.

## Outcomes

- Define legal states and transitions for the intake workflow.
- Persist enough versioned state to resume safely.
- Reject stale or illegal transitions.

## Exercise

Draw a state machine from `received` through `validated`, `needs_review`, `approved`, `submitted`, `failed`, and `cancelled`. Mark the actor and preconditions for each transition. Define a version field and optimistic concurrency check. Simulate process restart after approval and prove that resume uses the same preview hash rather than rebuilding an unreviewed action.

## Deliverable

`workflow-state.md`, transition table, and a serialized synthetic resume fixture.

## Assessment

Pass when every transition has a guard, stale state is rejected, resume cannot bypass approval, and cancellation prevents later submission.

## Reflection

What state must be durable for audit, and what transient data should be recomputed instead?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
