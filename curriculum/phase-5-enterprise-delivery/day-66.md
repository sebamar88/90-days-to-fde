---
day: 66
phase: 5
status: Ready
title: Estimate operating cost and capacity
estimated_effort: 75–100 minutes
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
