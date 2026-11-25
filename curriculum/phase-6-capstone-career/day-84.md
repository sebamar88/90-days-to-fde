---
schema_version: 1
id: day-84
day: 84
phase: 6
locale: en
slug: improve-based-on-observed-friction
title: Improve based on observed friction
description: Iteration should address observed user friction without weakening controls or overfitting to one role-play.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: capstone-milestone
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-83
objectives:
  - Select a friction issue using impact and evidence.
  - Change explanation or workflow behavior without altering the safety contract.
  - Re-run relevant usability and regression checks.
tags:
  - phase-6
  - iterative-improvement
skills:
  - iterative-improvement
---

# Day 84 — Improve based on observed friction

## Why this matters

Iteration should address observed user friction without weakening controls or overfitting to one role-play. Small changes with before/after evidence are easier to review.

## Scenario

The panel log shows that one participant could not tell which fields were inferred and another did not know why a request was sent to review.

## Outcomes

- Select a friction issue using impact and evidence.
- Change explanation or workflow behavior without altering the safety contract.
- Re-run relevant usability and regression checks.

## Exercise

Choose one issue from Day 83. Write a before-state observation, hypothesis, and measurable acceptance check. Make the smallest change. Replay the same synthetic task with a new role-play participant or a documented walkthrough, then run affected regression cases. Record whether the issue improved and any new ambiguity.

## Deliverable

One small revision, linked issue, before/after evidence, and regression results.

## Assessment

Pass when the change addresses an observed issue, relevant safety tests remain green, and the evidence is still labeled as simulated.

## Reflection

What did you choose not to change because the evidence was too weak?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
