---
schema_version: 1
id: day-28
day: 28
phase: 2
locale: en
slug: compare-model-and-rules-baselines
title: Compare model and rules baselines
description: Overall accuracy can hide a critical failure slice.
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
  - day-27
objectives:
  - Evaluate both systems on identical labeled cases.
  - Report per-field and per-slice results, including abstentions.
  - Use an error review to decide whether a model adds enough value.
tags:
  - phase-2
  - model-evaluation
skills:
  - model-evaluation
---

# Day 28 — Compare model and rules baselines

## Why this matters

Overall accuracy can hide a critical failure slice. Compare systems on the same cases, score the task fields that matter, and inspect harmful false positives separately.

## Scenario

The evaluation set is intentionally small and synthetic. It can expose functional differences but cannot establish real-world prevalence or guarantee customer performance.

## Outcomes

- Evaluate both systems on identical labeled cases.
- Report per-field and per-slice results, including abstentions.
- Use an error review to decide whether a model adds enough value.

## Exercise

Build a comparison table for category, location, urgency, missing-field detection, and safe abstention. Report counts and denominator for each slice; include the exact evaluation set version and prompt/schema versions. Inspect every high-impact error. Do not collapse correctness and safety into one score.

## Deliverable

An evaluation report with a proceed, revise, or retain-rules recommendation and limitations.

## Assessment

Pass when the comparison uses identical cases, exposes high-impact errors and abstentions, includes denominators, and avoids unsupported generalization from synthetic data.

## Reflection

Would you keep the model if it improves average extraction but worsens the unsafe-routing slice?
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
