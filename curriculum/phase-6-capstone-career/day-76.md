---
schema_version: 1
id: day-76
day: 76
phase: 6
locale: en
slug: confirm-capstone-scope-and-evidence-gaps
title: Confirm capstone scope and evidence gaps
description: Capstones become unfinishable when scope grows faster than evidence.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: capstone-milestone
difficulty: advanced
duration:
  min: 75
  max: 100
prerequisites:
  - day-75
objectives:
  - Restate the outcome, non-goals, and measurable success criteria.
  - Separate verified artifacts from simulated assumptions.
  - Reduce scope to a demonstrable, safe end-to-end slice.
tags:
  - phase-6
  - capstone-scoping
skills:
  - capstone-scoping
---

# Day 76 — Confirm capstone scope and evidence gaps

## Why this matters

Capstones become unfinishable when scope grows faster than evidence. Starting with the user outcome, boundaries, and missing approvals keeps the project honest and shippable.

## Scenario

The Meridian sponsor asks for a complete intake assistant. The learner has a discovery packet and prototype evidence, but no real customer validation or production access.

## Outcomes

- Restate the outcome, non-goals, and measurable success criteria.
- Separate verified artifacts from simulated assumptions.
- Reduce scope to a demonstrable, safe end-to-end slice.

## Exercise

Review all prior phase packets. Build an evidence register with claim, source, status (`observed`, `synthetic`, `simulated`, `unknown`), owner, and next validation step. Define a capstone in/out scope and a minimum successful demo. Remove any feature that lacks a user outcome or requires unapproved real data/access.

## Deliverable

`capstone-charter.md`, evidence register, and explicit acceptance criteria.

## Assessment

Pass when every outcome claim has an evidence status, scope fits the remaining days, and the charter preserves the draft-only production boundary.

## Reflection

Which attractive feature would you cut first to protect the evidence quality of the capstone?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
