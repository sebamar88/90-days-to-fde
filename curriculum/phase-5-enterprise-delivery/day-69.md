---
schema_version: 1
id: day-69
day: 69
phase: 5
locale: en
slug: plan-user-training-and-change-adoption
title: Plan user training and change adoption
description: An assistant changes how people review and route work.
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
  - day-68
objectives:
  - Identify role-specific tasks and training needs.
  - Teach review, correction, abstention, and escalation behavior.
  - Measure comprehension without implying adoption equals success.
tags:
  - phase-5
  - change-management
skills:
  - change-management
---

# Day 69 — Plan user training and change adoption

## Why this matters

An assistant changes how people review and route work. Training must explain limits and preserve user judgment, not pressure people to accept suggestions.

## Scenario

Two fictional coordinators have different experience: one handles urgent maintenance and one covers multiple sites. Neither has used the prototype.

## Outcomes

- Identify role-specific tasks and training needs.
- Teach review, correction, abstention, and escalation behavior.
- Measure comprehension without implying adoption equals success.

## Exercise

Draft a 20-minute walkthrough using three synthetic requests: clear, incomplete, and adversarial. Ask learners to inspect source fields, correct a suggestion, request human help, and decline an unsafe action. Write five teach-back questions and an accessibility check. Role-play the session and capture friction as simulated feedback.

## Deliverable

Training outline, quick-reference card, and comprehension checklist.

## Assessment

Pass when the material distinguishes suggestion from fact, teaches safe correction and escalation, and does not frame acceptance rate as a success target.

## Reflection

What user behavior would reveal that the interface is shifting risk onto coordinators?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
