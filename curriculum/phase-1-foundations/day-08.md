---
schema_version: 1
id: day-08
day: 8
phase: 1
locale: en
slug: find-data-access-and-policy-constraints
title: Find data, access, and policy constraints
description: Data access, privacy rules, identity boundaries, and legacy integration constraints shape what can safely be built.
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
  - day-07
objectives:
  - Inventory data categories, systems, owners, and access paths.
  - Identify sensitive fields and retention questions.
  - Turn unknown policies and integration details into discovery actions.
tags:
  - phase-1
  - data-governance
skills:
  - data-governance
---

# Day 8 — Find data, access, and policy constraints

## Why this matters

Data access, privacy rules, identity boundaries, and legacy integration constraints shape what can safely be built. These are design inputs, not last-minute reviews.

## Scenario

Requests may contain names, phone numbers, access instructions, and building details. The work-order system is described as legacy; its API, ownership, and test environment are unknown.

## Outcomes

- Inventory data categories, systems, owners, and access paths.
- Identify sensitive fields and retention questions.
- Turn unknown policies and integration details into discovery actions.

## Exercise

Create a data/system inventory. For each item record purpose, sensitivity hypothesis, owner to ask, permitted environment, retention question, and access status. Include email, work-order records, location data, identity/roles, and audit logs. Use synthetic examples only; do not paste real records into your notes.

## Deliverable

`constraints.md` with a data-flow sketch and a blocking-question list for IT, privacy, and operations.

## Assessment

Pass if sensitive data is identified as a hypothesis pending policy confirmation, no real personal data is included, and each integration unknown has a named owner or next step.

## Reflection

What should the system do when it cannot access the work-order system or verify a user's authority?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
