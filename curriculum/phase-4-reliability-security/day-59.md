---
schema_version: 1
id: day-59
day: 59
phase: 4
locale: en
slug: run-a-reliability-and-security-review
title: Run a reliability and security review
description: A review is actionable when it connects system behavior to evidence, owners, and release conditions.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: architecture-challenge
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-58
objectives:
  - Trace high risks to controls and tests.
  - Review degraded behavior, telemetry, and recovery ownership.
  - Separate blockers from accepted residual risks.
tags:
  - phase-4
  - risk-review
skills:
  - risk-review
---

# Day 59 — Run a reliability and security review

## Why this matters

A review is actionable when it connects system behavior to evidence, owners, and release conditions. It should make uncertainty visible rather than certify a prototype by checklist.

## Scenario

The simulated platform, security, and operations reviewers examine the workflow before a hypothetical limited pilot.

## Outcomes

- Trace high risks to controls and tests.
- Review degraded behavior, telemetry, and recovery ownership.
- Separate blockers from accepted residual risks.

## Exercise

Walk the Day 53 threat model against the current sequence and code. For each top risk, show its preventive control, detection signal, response owner, and test. Inspect Day 52 fallback and Day 58 incident actions. Record disagreement and missing customer evidence. Do not use “reviewed” as a substitute for a test result.

## Deliverable

Review record with findings, severity rationale, owners, due conditions, and explicit out-of-scope risks.

## Assessment

Pass when every critical risk has evidence or a release block, every finding has an owner, and residual risk is stated without claiming certification.

## Reflection

What would make you recommend stopping the pilot even if all planned tests pass?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
