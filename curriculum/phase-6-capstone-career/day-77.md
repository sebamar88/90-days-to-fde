---
day: 77
phase: 6
status: Ready
title: Close the highest-risk design gaps
estimated_effort: 90–120 minutes
---

# Day 77 — Close the highest-risk design gaps

## Why this matters

The final implementation should resolve risks that could invalidate the demo or violate its safety boundary before adding polish.

## Scenario

The capstone review finds three open items: stale approval handling, cross-region authorization, and evaluation cases for ambiguous urgent requests.

## Outcomes

- Prioritize gaps by impact, likelihood, and detectability.
- Update the relevant ADR or threat-model record when assumptions change.
- Define a testable closure condition for each selected risk.

## Exercise

Rank the open issues from prior phases. Select the top two that fit the timebox. For each, write an issue with evidence, owner, acceptance test, and rollback path. Implement one risk reduction or update the design with a justified stop condition. Do not mark unknown customer approvals as closed by code changes.

## Deliverable

Prioritized risk register and updated ADRs/issues with closure evidence.

## Assessment

Pass when the highest-severity risks have testable acceptance conditions, design changes are recorded, and organizational approvals remain assigned to their owners.

## Reflection

Which risk is not yours to “fix” as an engineer because it requires a customer decision?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
