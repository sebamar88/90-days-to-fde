---
schema_version: 1
id: day-33
day: 33
phase: 3
locale: en
slug: add-one-read-only-tool
title: Add one read-only tool
description: Read-only tools let a workflow use enterprise context while keeping early integration risk small.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: intermediate
duration:
  min: 90
  max: 120
prerequisites:
  - day-32
objectives:
  - Implement the catalog contract against an in-memory fixture.
  - Return only fields needed by downstream routing suggestions.
  - Demonstrate that lookup does not change fixture state.
tags:
  - phase-3
  - data-access
skills:
  - data-access
---

# Day 33 — Add one read-only tool

## Why this matters

Read-only tools let a workflow use enterprise context while keeping early integration risk small. They still need bounded queries and a clear source of truth.

## Scenario

Coordinators need to resolve a synthetic site code into a service region before reviewing a draft. The local fixture is the only approved source for this exercise.

## Outcomes

- Implement the catalog contract against an in-memory fixture.
- Return only fields needed by downstream routing suggestions.
- Demonstrate that lookup does not change fixture state.

## Exercise

Add a fixture with at least four synthetic sites across two regions. Implement exact normalized-code lookup and distinguish not-found from malformed input. Return site ID and region only. Call the tool twice with the same input and prove the fixture remains unchanged. Do not add fuzzy search; record what evidence would be needed before doing so.

## Deliverable

`site-directory.json`, tool implementation, and tests for valid, unknown, malformed, and repeated lookups.

## Assessment

Pass when every fixture lookup is deterministic, invalid values fail closed, unrelated site fields are not returned, and no write path exists.

## Reflection

Which customer-side owner would need to confirm that this directory is authoritative before a real integration?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
