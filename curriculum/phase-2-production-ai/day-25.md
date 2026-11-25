---
day: 25
phase: 2
status: Ready
title: Bound retries and make writes idempotent
estimated_effort: 75–100 minutes
---

# Day 25 — Bound retries and make writes idempotent

## Why this matters

Retries can duplicate work or amplify an outage. A safe integration distinguishes transient transport failure from invalid data and makes repeated submissions produce a predictable result.

## Scenario

The in-memory sandbox sometimes simulates a timeout after accepting a work order. The client cannot tell whether the first attempt succeeded.

## Outcomes

- Define a stable idempotency key and duplicate behavior.
- Retry only bounded, retryable failures.
- Preserve ambiguous outcomes for lookup/reconciliation rather than blind replay.

## Exercise

Derive an idempotency key from the reviewed request ID and action version. Make the fake sandbox return the original work order for a repeat key. Add a maximum-attempt policy for transient errors and ensure validation errors are not retried. Simulate a timeout-after-commit and verify reconciliation prevents a duplicate.

## Deliverable

Retry policy, idempotency behavior, and tests for timeout, duplicate, and non-retryable errors.

## Assessment

Pass when retries are bounded, the same approved action does not create duplicate work orders, and an ambiguous timeout is not treated as a definite failure.

## Reflection

Which failure state must be represented separately from “failed” and “succeeded”?
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
