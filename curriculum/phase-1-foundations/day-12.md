---
day: 12
phase: 1
status: Ready
title: Record a consequential decision
estimated_effort: 60–90 minutes
---

# Day 12 — Record a consequential decision

## Why this matters

Architecture decisions are easier to review when the context and alternatives are preserved. A short ADR also exposes where a choice rests on an assumption.

## Scenario

You need to decide whether the first slice writes to the work-order system or produces a reviewable draft. The API and approval policy are not yet verified.

## Outcomes

- Record context, decision, alternatives, and consequences.
- Separate reversible implementation choices from policy decisions.
- Name evidence that would trigger reconsideration.

## Exercise

Use the ADR template to decide the first-slice write boundary. Include options: production write, sandbox-only write, or draft-only. State the chosen option and why, consequences, unresolved questions, and a revisit trigger.

## Deliverable

`adr/0001-first-slice-write-boundary.md`.

## Assessment

Pass if at least two credible alternatives are compared, the decision follows stated evidence and constraints, and a clear condition for revisiting it is recorded.

## Reflection

Which part of this decision belongs to the customer or security owner rather than the engineering team?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
