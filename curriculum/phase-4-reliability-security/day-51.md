---
day: 51
phase: 4
status: Ready
title: Set service-level indicators and objectives
estimated_effort: 75–100 minutes
---

# Day 51 — Set service-level indicators and objectives

## Why this matters

Availability alone does not show whether the intake workflow is useful or safe. Operational indicators should describe user-visible service behavior and keep quality and safety gates visible.

## Scenario

Operations wants the endpoint “always up.” The workflow may still be unusable when the directory is unavailable or every request requires manual correction.

## Outcomes

- Define service-level indicators with explicit event populations.
- Propose objectives and windows as hypotheses, not customer commitments.
- Separate availability, latency, task outcome, and safety indicators.

## Exercise

Define indicators for successful draft response, p95 response time, dependency failure, abstention, and approval bypass. Specify numerator, denominator, exclusion rules, measurement window, and owner. Draft provisional objectives and a warning policy; explain how volume and customer workflow affect whether those targets make sense.

## Deliverable

`service-objectives.md` with indicator definitions and a review agenda for real service owners.

## Assessment

Pass when each SLI is computable from defined events, customer-facing and safety measures are distinct, and no target is represented as agreed with Meridian.

## Reflection

Which objective would create an incentive to accept risky drafts if used alone?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
