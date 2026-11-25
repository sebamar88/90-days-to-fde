---
schema_version: 1
id: day-39
day: 39
phase: 3
locale: en
slug: handle-rate-limits-and-partial-failure
title: Handle rate limits and partial failure
description: Enterprise dependencies fail independently.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: intermediate
duration:
  min: 90
  max: 120
prerequisites:
  - day-38
objectives:
  - Distinguish retryable, terminal, and ambiguous outcomes.
  - Respect server retry guidance and bound attempts and total time.
  - Route ambiguous writes to reconciliation rather than blind retry.
tags:
  - phase-3
  - partial-failure-recovery
skills:
  - partial-failure-recovery
---

# Day 39 — Handle rate limits and partial failure

## Why this matters

Enterprise dependencies fail independently. Retrying everything can amplify overload or repeat actions that already succeeded.

## Scenario

The site directory returns a rate-limit response, while the sandbox may accept a draft but time out before the client receives confirmation.

## Outcomes

- Distinguish retryable, terminal, and ambiguous outcomes.
- Respect server retry guidance and bound attempts and total time.
- Route ambiguous writes to reconciliation rather than blind retry.

## Exercise

Create an error table for validation, permission denial, rate limit, timeout-before-send, timeout-after-send, and service-unavailable responses. Specify retry budget, backoff with jitter, deadline, and user-facing state. Simulate a 429 followed by success and a timeout after sandbox acceptance. Keep writes behind the idempotency contract from Day 41.

## Deliverable

`dependency-failure-policy.md` and deterministic retry tests using a fake clock and fake adapter.

## Assessment

Pass when total retries and elapsed time are bounded, non-retryable errors are not retried, and ambiguous writes enter reconciliation.

## Reflection

When is “unknown whether it succeeded” safer than reporting failure or retrying immediately?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
