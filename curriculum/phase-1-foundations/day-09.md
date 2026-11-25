---
schema_version: 1
id: day-09
day: 9
phase: 1
locale: en
slug: test-whether-ai-belongs-in-the-solution
title: Test whether AI belongs in the solution
description: AI can help interpret variable language, but adds uncertainty, evaluation burden, cost, and new failure modes.
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
  - day-08
objectives:
  - Match problem characteristics to deterministic, human, and model-based approaches.
  - Define where model uncertainty must be visible.
  - Identify a baseline that can test whether AI adds value.
tags:
  - phase-1
  - ai-fit-assessment
skills:
  - ai-fit-assessment
---

# Day 9 — Test whether AI belongs in the solution

## Why this matters

AI can help interpret variable language, but adds uncertainty, evaluation burden, cost, and new failure modes. A sound proposal compares it with simpler alternatives.

## Scenario

Some requests omit location or describe the same maintenance issue in different words. The current workflow already involves a person checking details before work-order entry.

## Outcomes

- Match problem characteristics to deterministic, human, and model-based approaches.
- Define where model uncertainty must be visible.
- Identify a baseline that can test whether AI adds value.

## Exercise

Compare three options: improve the form/template, rules plus required-field checks, and model-assisted extraction with human confirmation. For each, assess fit, failure impact, data needs, evaluation difficulty, operational burden, and reversibility. Identify which fields could be safely suggested versus which must be confirmed.

## Deliverable

`solution-hypotheses.md` with an options table and a falsifiable hypothesis for an AI-assisted slice.

## Assessment

Pass if a non-AI option is seriously evaluated, uncertainty and human review are explicit, and the AI hypothesis has a measurable test rather than a claim of general intelligence.

## Reflection

Which part of the workflow is genuinely language-variable, and which part is ordinary validation or integration?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
