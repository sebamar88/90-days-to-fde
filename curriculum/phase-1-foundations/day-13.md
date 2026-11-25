---
schema_version: 1
id: day-13
day: 13
phase: 1
locale: en
slug: design-the-smallest-useful-slice
title: Design the smallest useful slice
description: Small slices shorten the path to evidence.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: architecture-challenge
difficulty: foundational
duration:
  min: 75
  max: 100
prerequisites:
  - day-12
objectives:
  - Define one end-to-end user journey and its boundaries.
  - Write acceptance criteria including ambiguous and failure cases.
  - Identify dependencies and test data needed.
tags:
  - phase-1
  - acceptance-criteria
skills:
  - acceptance-criteria
---

# Day 13 — Design the smallest useful slice

## Why this matters

Small slices shorten the path to evidence. The slice still needs a meaningful user task and observable behavior; a toy demo can prove little about operational usefulness.

## Scenario

The candidate slice turns one synthetic request into a suggested work-order draft for a coordinator to review. The customer has not yet agreed to pilot data or access.

## Outcomes

- Define one end-to-end user journey and its boundaries.
- Write acceptance criteria including ambiguous and failure cases.
- Identify dependencies and test data needed.

## Exercise

Specify a slice for synthetic requests only: input, suggested fields, missing-information behavior, confidence/uncertainty presentation, coordinator correction, and output. Add acceptance examples for complete, incomplete, ambiguous, and unsafe-to-route requests. Keep actual work-order creation disabled.

## Deliverable

`thin-slice.md` with a user story, acceptance criteria, exclusions, and test-case table.

## Assessment

Pass if every acceptance criterion is observable, at least two cases cause the system to ask for human input, and no acceptance criterion assumes an unverified customer integration.

## Reflection

What is the smallest test that would show whether the draft saves meaningful effort?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
