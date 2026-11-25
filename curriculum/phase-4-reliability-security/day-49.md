---
schema_version: 1
id: day-49
day: 49
phase: 4
locale: en
slug: test-prompt-and-model-changes-for-regressions
title: Test prompt and model changes for regressions
description: Prompt, schema, model, and orchestration changes can shift behavior in ways ordinary unit tests miss.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-48
objectives:
  - Record the exact candidate configuration and evaluation-set revision.
  - Compare outputs case by case against the baseline.
  - Block changes that regress a safety-critical slice.
tags:
  - phase-4
  - regression-testing
skills:
  - regression-testing
---

# Day 49 — Test prompt and model changes for regressions

## Why this matters

Prompt, schema, model, and orchestration changes can shift behavior in ways ordinary unit tests miss. Versioned comparisons make changes reviewable and reversible.

## Scenario

A prompt edit improves summaries in three examples but changes urgency labels on another fixture. No production traffic is available for testing.

## Outcomes

- Record the exact candidate configuration and evaluation-set revision.
- Compare outputs case by case against the baseline.
- Block changes that regress a safety-critical slice.

## Exercise

Create a run manifest with code commit, prompt/schema versions, model identifier when applicable, temperature/settings, dataset revision, and timestamp. Compare baseline and candidate outputs using the frozen protocol. Add one regression fixture before accepting any behavior correction. Keep secrets and raw customer data out of the manifest.

## Deliverable

Evaluation run manifest, comparison report, and a change/revert recommendation.

## Assessment

Pass when another learner can reproduce the run, all differences are inspectable, and no aggregate gain overrides a safety-gate regression.

## Reflection

What evidence would distinguish a robust improvement from a lucky change on a tiny fixture?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
