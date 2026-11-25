---
schema_version: 1
id: day-21
day: 21
phase: 2
locale: en
slug: abstain-when-the-request-is-ambiguous
title: Abstain when the request is ambiguous
description: Valid structure does not mean the content is known.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: intermediate
duration:
  min: 75
  max: 100
prerequisites:
  - day-20
objectives:
  - Define task-specific conditions for abstention and human clarification.
  - Preserve source evidence for extracted fields.
  - Avoid treating model-reported confidence as a calibrated probability.
tags:
  - phase-2
  - safe-abstention
skills:
  - safe-abstention
---

# Day 21 — Abstain when the request is ambiguous

## Why this matters

Valid structure does not mean the content is known. When location, issue, or urgency is ambiguous, a safe system exposes uncertainty and asks for clarification instead of fabricating certainty.

## Scenario

“There is water near the unit again” could refer to multiple units, an active leak, or a past issue. The model must not invent an address or decide dispatch priority from vague text.

## Outcomes

- Define task-specific conditions for abstention and human clarification.
- Preserve source evidence for extracted fields.
- Avoid treating model-reported confidence as a calibrated probability.

## Exercise

Add ambiguity cases to the evaluation set. Require the draft to return `unknown`/missing fields and a reason when evidence is insufficient. Add a clarification question that asks only for missing facts. Verify the API never changes an unknown field to a default value such as “routine.”

## Deliverable

An abstention policy, ambiguity cases, and tests proving that unknowns survive validation and serialization.

## Assessment

Pass when ambiguous and conflicting requests produce a review/clarification outcome and do not create a false urgency or location assertion.

## Reflection

Which errors are safer to miss, and which errors require immediate human escalation?
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
