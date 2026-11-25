---
schema_version: 1
id: day-66
day: 66
phase: 5
locale: en
slug: estimate-operating-cost-and-capacity
title: Estimate operating cost and capacity
description: Cost estimates should expose assumptions and uncertainty.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: advanced
duration:
  min: 75
  max: 100
prerequisites:
  - day-65
objectives:
  - Build a transparent per-request and monthly cost model.
  - Estimate throughput and dependency capacity from stated assumptions.
  - Compare model-assisted and deterministic operating paths.
tags:
  - phase-5
  - cost-capacity
skills:
  - cost-capacity
---

# Day 66 — Estimate operating cost and capacity

## Why this matters

Cost estimates should expose assumptions and uncertainty. A model API price is only one part of the cost of operating an enterprise workflow.

## Scenario

Meridian has not provided volume, concurrency, retention, or support-hour data. The learner may use clearly labeled hypothetical values for a sensitivity exercise.

## Outcomes

- Build a transparent per-request and monthly cost model.
- Estimate throughput and dependency capacity from stated assumptions.
- Compare model-assisted and deterministic operating paths.

## Exercise

List compute, storage, telemetry, model usage, network, support, and failure-retry cost categories. Enter low/base/high request volumes in a spreadsheet and show formulas and source date for any public price. Mark every numeric input hypothetical until confirmed. Estimate peak concurrency and identify which dependency limit should be load-tested; do not claim forecast precision.

## Deliverable

Cost/capacity worksheet with assumptions, sensitivity range, and customer questions.

## Assessment

Pass when formulas are inspectable, one-time and recurring costs are separated, uncertainty is visible, and a non-model baseline is included.

## Reflection

Which missing customer input contributes the most uncertainty to your estimate?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
