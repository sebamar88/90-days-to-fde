---
day: 85
phase: 6
status: Ready
title: Write a concise architecture and trade-off brief
estimated_effort: 75–100 minutes
---

# Day 85 — Write a concise architecture and trade-off brief

## Why this matters

FDEs must explain system behavior to both builders and decision-makers. A short architecture brief should connect choices to constraints, alternatives, and measurable consequences.

## Scenario

The simulated sponsor has five minutes; the platform reviewer wants enough detail to challenge the integration and trust boundaries.

## Outcomes

- Explain the system context and primary sequence concisely.
- Defend two consequential decisions and rejected alternatives.
- Distinguish evidence from assumptions and future work.

## Exercise

Write a two-page maximum brief with context/sequence diagrams, component ownership, data/identity boundaries, provider option, approval flow, failure behavior, evaluation evidence, and operational risks. Explain two ADRs using constraint → options → choice → consequence. Add a “not validated” section listing customer-owned unknowns.

## Deliverable

Architecture/trade-off brief with links to ADRs, tests, and evaluation artifacts.

## Assessment

Pass when a reviewer can identify the trust boundary, action path, rejected option, and evidence limit without inferring them from code.

## Reflection

Which architectural choice would you revisit first if request volume or data residency changed?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
