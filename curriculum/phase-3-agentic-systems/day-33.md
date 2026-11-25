---
day: 33
phase: 3
status: Ready
title: Add one read-only tool
estimated_effort: 90–120 minutes
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
