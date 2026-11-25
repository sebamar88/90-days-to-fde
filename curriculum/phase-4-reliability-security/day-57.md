---
day: 57
phase: 4
status: Ready
title: Test authorization boundaries
estimated_effort: 90–120 minutes
---

# Day 57 — Test authorization boundaries

## Why this matters

Happy-path tests prove a permitted user can act. Security depends just as much on proving that neighboring tenants, roles, and workflow states cannot.

## Scenario

The fake organization has two regions, three roles, and drafts in pending, approved, submitted, and cancelled states.

## Outcomes

- Build a role/resource/state access matrix.
- Test deny paths at every read and write boundary.
- Detect authorization gaps caused by stale or changed resource state.

## Exercise

Generate cases for each role × region × state combination and mark expected read, approve, and submit permissions. Add cross-region identifier substitution and approval-after-cancellation. Run tests at the service and tool adapter boundaries. Record any expected denial that still reached an external adapter call.

## Deliverable

Authorization matrix and automated negative-test report.

## Assessment

Pass when every matrix cell is exercised, denied requests cause no adapter call, and authorization is rechecked on resume and immediately before submission.

## Reflection

Which resource attribute should be reloaded at action time to avoid trusting stale authorization state?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
