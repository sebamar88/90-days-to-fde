---
schema_version: 1
id: day-45
day: 45
phase: 3
locale: en
slug: phase-review-bounded-integrated-workflow
title: Phase review — bounded integrated workflow
description: An integrated workflow is ready for deeper reliability work only when its actions, identities, state, and failure behavior can be explained and replayed.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: phase-assessment
difficulty: intermediate
duration:
  min: 90
  max: 120
prerequisites:
  - day-44
objectives:
  - Demonstrate the full path and its control boundaries.
  - Defend the autonomy and integration choices with evidence.
  - Identify remaining risks before evaluating and hardening the system.
tags:
  - phase-3
  - architecture-defense
skills:
  - architecture-defense
---

# Day 45 — Phase review: bounded integrated workflow

## Why this matters

An integrated workflow is ready for deeper reliability work only when its actions, identities, state, and failure behavior can be explained and replayed.

## Scenario

Present the synthetic Meridian workflow to a simulated operations sponsor and security reviewer. They ask for one successful sandbox draft, one denial, and one recovery from partial failure.

## Outcomes

- Demonstrate the full path and its control boundaries.
- Defend the autonomy and integration choices with evidence.
- Identify remaining risks before evaluating and hardening the system.

## Exercise

Assemble Days 31–44. Replay a read-only lookup, a human-approved sandbox draft, an out-of-region denial, a stale approval, and an ambiguous write recovery. Show the tool-policy results and audit trail. Ask each simulated reviewer to challenge one assumption; label all responses as role-play. Recommend proceed, revise, or stop.

## Deliverable

Phase 3 review packet: diagrams, tool catalog, policy matrix, state machine, evaluation results, failure report, and a five-minute playback.

## Assessment rubric

Score 0 (missing), 1 (partial), or 2 (evidenced): least-privilege tools; validated contracts; approval bound to preview; state/resume safety; actor authorization; integration/failure mapping; idempotency; audit/redaction; policy evaluation. Pass at 14/18 with no zero for least privilege, approval, or duplicate-action safety.

## Reflection

Which single unresolved assumption blocks a responsible move into Phase 4?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
