---
schema_version: 1
id: day-81
day: 81
phase: 6
locale: en
slug: complete-telemetry-runbooks-and-fallback
title: Complete telemetry, runbooks, and fallback
description: Software is not operationally complete if a reviewer cannot see what happened, contain a fault, and recover without guessing.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: capstone-milestone
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-80
objectives:
  - Verify trace/log correlation and sensitive-data redaction.
  - Rehearse the documented fallback and stop action.
  - Confirm recovery preserves approval and idempotency state.
tags:
  - phase-6
  - operations-validation
skills:
  - operations-validation
---

# Day 81 — Complete telemetry, runbooks, and fallback

## Why this matters

Software is not operationally complete if a reviewer cannot see what happened, contain a fault, and recover without guessing.

## Scenario

An operator must distinguish an upstream timeout, invalid provider output, authorization denial, and uncertain sandbox submission using synthetic traces and events.

## Outcomes

- Verify trace/log correlation and sensitive-data redaction.
- Rehearse the documented fallback and stop action.
- Confirm recovery preserves approval and idempotency state.

## Exercise

Trigger the four scenarios and follow the runbook without editing it mid-run. Record the signal found, time to diagnosis, containment action, and recovery evidence. Check for raw request text or secrets in every captured event. Update procedures only after the rehearsal and rerun the changed step.

## Deliverable

Operational rehearsal report, final runbook, and redaction results.

## Assessment

Pass when an unfamiliar operator can find each failure, stop unsafe writes, and recover without duplicate action; all captured artifacts remain privacy-safe.

## Reflection

Which operational instruction still depends on knowledge that only the developer has?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
