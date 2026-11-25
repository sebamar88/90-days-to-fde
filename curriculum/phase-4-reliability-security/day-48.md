---
schema_version: 1
id: day-48
day: 48
phase: 4
locale: en
slug: analyze-errors-by-slice
title: Analyze errors by slice
description: Aggregate scores can hide a systematic failure on a particular request type or workflow state.
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
  - day-47
objectives:
  - Report metric results by meaningful slice and sample count.
  - Inspect false accepts and false abstentions separately.
  - Turn an observed error into a bounded follow-up test.
tags:
  - phase-4
  - error-analysis
skills:
  - error-analysis
---

# Day 48 — Analyze errors by slice

## Why this matters

Aggregate scores can hide a systematic failure on a particular request type or workflow state. Slice analysis makes the next engineering decision concrete.

## Scenario

The synthetic evaluation includes urgent requests, missing locations, conflicting categories, and unseen phrasing. The sponsor asks for one overall success percentage.

## Outcomes

- Report metric results by meaningful slice and sample count.
- Inspect false accepts and false abstentions separately.
- Turn an observed error into a bounded follow-up test.

## Exercise

Run the frozen protocol on the deterministic baseline and one candidate. Tabulate each slice with numerator, denominator, and error examples. Inspect all safety-gate failures individually. Select the highest-impact error, write a hypothesis about its cause, and add a held-out case that would falsify your hypothesis before changing implementation.

## Deliverable

Slice report, anonymized error examples, and a prioritized issue with a falsifiable acceptance test.

## Assessment

Pass when small denominators remain visible, errors are not hidden by averages, and the proposed fix has a test that could fail.

## Reflection

Which slice deserves more data before you recommend a model or threshold change?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
