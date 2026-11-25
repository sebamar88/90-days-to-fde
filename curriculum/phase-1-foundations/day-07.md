---
schema_version: 1
id: day-07
day: 7
phase: 1
locale: en
slug: define-outcomes-and-guardrails
title: Define outcomes and guardrails
description: “Use AI” is not a success measure.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: business-discovery-exercise
difficulty: foundational
duration:
  min: 75
  max: 100
prerequisites:
  - day-06
objectives:
  - Define an outcome metric with a clear numerator, denominator, and observation window.
  - Pair it with quality and safety guardrails.
  - State what baseline data is needed before setting a target.
tags:
  - phase-1
  - metric-design
skills:
  - metric-design
---

# Day 7 — Define outcomes and guardrails

## Why this matters

“Use AI” is not a success measure. Teams need an outcome that reflects the workflow and guardrails that keep a local efficiency gain from creating downstream harm.

## Scenario

Meridian wants faster request intake. Missing locations can cause delay; incorrect urgency or assignment could create operational risk. No baseline has been measured.

## Outcomes

- Define an outcome metric with a clear numerator, denominator, and observation window.
- Pair it with quality and safety guardrails.
- State what baseline data is needed before setting a target.

## Exercise

Propose one primary metric (for example, median time from complete request receipt to accepted work order), define its event boundaries and exclusions, and propose three guardrails (such as missing-field rate, correction rate, and unsafe urgency escalation). Specify where each event might be recorded and what baseline period is needed. Do not invent target values.

## Deliverable

`success-measures.md` with metric definitions, guardrails, data gaps, and a measurement plan.

## Assessment

Pass if the metric can be measured from named events, guardrails include correctness and operational risk, and targets are explicitly deferred until baseline evidence exists.

## Reflection

How could improving the primary metric make the requester or technician experience worse?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
