---
schema_version: 1
id: day-80
day: 80
phase: 6
locale: en
slug: complete-evaluation-and-regression-evidence
title: Complete evaluation and regression evidence
description: A final demo can be curated to hide known failure cases.
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
  - day-79
objectives:
  - Re-run the frozen evaluation against the capstone commit.
  - Report quality by slice and safety gate.
  - Preserve enough run metadata to reproduce the result.
tags:
  - phase-6
  - final-evaluation
skills:
  - final-evaluation
---

# Day 80 — Complete evaluation and regression evidence

## Why this matters

A final demo can be curated to hide known failure cases. A versioned evaluation run and regression gate make claims inspectable beyond the demo script.

## Outcomes

- Re-run the frozen evaluation against the capstone commit.
- Report quality by slice and safety gate.
- Preserve enough run metadata to reproduce the result.

## Scenario

The simulated release reviewer asks whether the latest tool, prompt, or schema change altered behavior on prior cases.

## Exercise

Run every evaluation case against the deterministic baseline and selected capstone path. Capture commit, configuration, dataset revision, environment, and result. Compare with the prior phase report. Inspect all unsafe-action and abstention failures individually; add a regression fixture for each fixed defect. If an optional provider is unavailable, report the deterministic run and leave provider metrics unclaimed.

## Deliverable

Capstone evaluation report, run manifest, regression cases, and limitations section.

## Assessment

Pass when all scores have denominators, safety failures are individually dispositioned, and provider results are claimed only if actually run.

## Reflection

What evidence would make the deterministic baseline the better final recommendation?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
