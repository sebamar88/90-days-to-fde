---
schema_version: 1
id: day-70
day: 70
phase: 5
locale: en
slug: design-feedback-and-correction-loops
title: Design feedback and correction loops
description: Corrections can improve a service, but only if teams know what is collected, who reviews it, and whether it changes a rule, prompt, dataset, or policy.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: advanced
duration:
  min: 75
  max: 100
prerequisites:
  - day-69
objectives:
  - Design a minimal, purpose-bound feedback record.
  - Route corrections to review rather than automatic training.
  - Close the loop with users and version changes.
tags:
  - phase-5
  - feedback-governance
skills:
  - feedback-governance
---

# Day 70 — Design feedback and correction loops

## Why this matters

Corrections can improve a service, but only if teams know what is collected, who reviews it, and whether it changes a rule, prompt, dataset, or policy.

## Scenario

Meridian coordinators may correct a category or report an unsafe suggestion. There is no consent, retention, or data-use agreement for real feedback yet.

## Outcomes

- Design a minimal, purpose-bound feedback record.
- Route corrections to review rather than automatic training.
- Close the loop with users and version changes.

## Exercise

Define separate flows for usability feedback, field correction, and safety incident. For each specify consent/notice, data captured, access, retention, reviewer, severity path, and closure message. Use synthetic examples only. Demonstrate that a correction changes neither the model nor policy until an authorized maintainer reviews and versions it.

## Deliverable

Feedback workflow diagram and data-minimization record.

## Assessment

Pass when safety reports have an escalation path, ordinary feedback avoids unnecessary raw text, and no correction silently becomes training data.

## Reflection

How will a coordinator know their correction was reviewed and what changed as a result?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
