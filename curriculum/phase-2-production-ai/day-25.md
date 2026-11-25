---
schema_version: 1
id: day-25
day: 25
phase: 2
locale: en
slug: bound-retries-and-make-writes-idempotent
title: Bound retries and make writes idempotent
description: Retries can duplicate work or amplify an outage.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: intermediate
duration:
  min: 75
  max: 100
prerequisites:
  - day-24
objectives:
  - Define a stable idempotency key and duplicate behavior.
  - Retry only bounded, retryable failures.
  - Preserve ambiguous outcomes for lookup/reconciliation rather than blind replay.
tags:
  - phase-2
  - idempotency-and-retry
skills:
  - idempotency-and-retry
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
