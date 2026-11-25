---
day: 47
phase: 4
status: Ready
title: Define scoring and acceptance thresholds
estimated_effort: 75–100 minutes
---

# Day 47 — Define scoring and acceptance thresholds

## Why this matters

Metrics influence release decisions. Averages, thresholds, and denominators must be agreed before results are seen to reduce metric shopping.

## Scenario

The simulated sponsor values fewer coordinator corrections, while the security reviewer treats unauthorized writes as unacceptable. These are different outcome classes.

## Outcomes

- Choose metrics tied to task outcomes and risk.
- Define denominator, unit, and missing-data handling.
- Separate hard safety gates from aggregate quality thresholds.

## Exercise

For field extraction, abstention, valid tool arguments, unauthorized invocation, and human correction, write each metric's formula and evaluation unit. Propose thresholds before running a candidate. Make unauthorized writes and approval bypass zero-tolerance. State why a small synthetic set cannot establish a production confidence level; identify the customer evidence needed next.

## Deliverable

`evaluation-protocol.md` with frozen metric definitions, provisional thresholds, and release rules.

## Assessment

Pass when every metric has a denominator and interpretation, hard gates are explicit, and thresholds are labeled provisional rather than customer-approved.

## Reflection

Which metric would you refuse to combine into a single quality score, and why?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
