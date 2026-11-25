---
schema_version: 1
id: day-18
day: 18
phase: 2
locale: en
slug: create-a-synthetic-evaluation-set
title: Create a synthetic evaluation set
description: Evaluating only a few hand-picked happy paths rewards a system for the cases it already handles.
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
  - day-17
objectives:
  - Define a JSONL record format with expected fields and provenance.
  - Cover key categories and failure conditions without personal data.
  - Keep evaluation examples separate from prompt demonstrations.
tags:
  - phase-2
  - evaluation-data
skills:
  - evaluation-data
---

# Day 18 — Create a synthetic evaluation set

## Why this matters

Evaluating only a few hand-picked happy paths rewards a system for the cases it already handles. A small, labeled, representative fixture lets you compare changes and inspect important slices.

## Scenario

Meridian has no approved data-sharing agreement for this exercise. The evaluation set must be wholly synthetic and include ordinary, incomplete, ambiguous, and high-impact wording.

## Outcomes

- Define a JSONL record format with expected fields and provenance.
- Cover key categories and failure conditions without personal data.
- Keep evaluation examples separate from prompt demonstrations.

## Exercise

Review `data/evaluation.jsonl`. Add at least four synthetic cases: a missing location, two plausible categories, an urgent phrase that must be escalated for human review, and an unrelated message. Each record needs an opaque case ID, input text, expected category/urgency, expected missing fields, and rationale. Check the file for actual names, phone numbers, addresses, or copied customer text.

## Deliverable

A versioned JSONL fixture and a data card describing its synthetic construction, coverage, and known gaps.

## Assessment

Pass when every record parses, every expected label has a rationale, there is at least one example per critical slice, and no record is claimed to represent real customer prevalence.

## Reflection

What real-world distribution claim can this synthetic set not support?
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
