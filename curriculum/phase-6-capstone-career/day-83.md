---
schema_version: 1
id: day-83
day: 83
phase: 6
locale: en
slug: test-with-a-simulated-customer-panel
title: Test with a simulated customer panel
description: Technical correctness does not guarantee that users understand the system or can recover from its suggestions.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: enterprise-simulation
difficulty: advanced
duration:
  min: 75
  max: 100
prerequisites:
  - day-82
objectives:
  - Observe whether participants can complete and correct the workflow.
  - Capture friction without leading the participants.
  - Separate role-play observations from verified user research.
tags:
  - phase-6
  - usability-testing
skills:
  - usability-testing
---

# Day 83 — Test with a simulated customer panel

## Why this matters

Technical correctness does not guarantee that users understand the system or can recover from its suggestions. A structured panel rehearsal surfaces interaction friction before portfolio claims are written.

## Scenario

Role-play an operations coordinator, security reviewer, and platform engineer. Their questions are prompts for practice, not customer feedback or validation.

## Outcomes

- Observe whether participants can complete and correct the workflow.
- Capture friction without leading the participants.
- Separate role-play observations from verified user research.

## Exercise

Give each role the same task and only the learner-facing instructions. Ask them to process a clear request, an incomplete request, and an unsafe request. Observe without coaching; note task completion, confusion, recovery, and questions. Afterwards label each note `simulated role-play` and list what real-user research would still need consent and approval.

## Deliverable

Panel observation log and prioritized usability issues, all labeled simulated.

## Assessment

Pass when observations distinguish behavior from interpretation, no simulated comment is attributed to a real person, and at least one issue is supported by a reproducible observation.

## Reflection

What did a participant misunderstand that your technical explanation had made feel obvious?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
