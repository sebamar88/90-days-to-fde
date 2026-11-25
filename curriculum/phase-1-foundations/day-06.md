---
day: 6
phase: 1
status: Ready
title: Separate evidence from assumptions
estimated_effort: 60–90 minutes
---

# Day 6 — Separate evidence from assumptions

## Why this matters

Early discovery mixes observations, stakeholder beliefs, and engineering guesses. Making their status visible prevents an untested assumption from becoming a requirement.

## Scenario

Your notes include a missing-location example, the phrase “sometimes,” a handoff to a technician, and no verified measurement of delays or rework.

## Outcomes

- Classify claims as observed, reported, inferred, or unknown.
- Identify assumptions that could change scope or safety.
- Choose the next cheapest evidence-gathering action.

## Exercise

Create an evidence table with columns: claim, source, type, confidence, impact if wrong, and next check. Add at least eight claims from Days 1–5. Rank assumptions by impact and uncertainty. For the top two, propose a low-cost way to check them (observation, record sample, or follow-up interview).

## Deliverable

`evidence-log.md` and two prioritized validation actions.

## Assessment

Pass if every claim has a source/type, unsupported quantitative claims are labeled unknown, and high-impact uncertain assumptions have a concrete check.

## Reflection

Which assumption would most change the solution if it were false?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
