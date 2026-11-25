---
schema_version: 1
id: day-10
day: 10
phase: 1
locale: en
slug: compare-solution-options-and-scope-the-first-release
title: Compare solution options and scope the first release
description: An enterprise pilot must fit the problem, risk tolerance, and integration reality.
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
  - day-09
objectives:
  - Compare options against explicit criteria.
  - Select a reversible first release with a clear user boundary.
  - State exclusions and decision gates.
tags:
  - phase-1
  - project-scoping
skills:
  - project-scoping
---

# Day 10 — Compare solution options and scope the first release

## Why this matters

An enterprise pilot must fit the problem, risk tolerance, and integration reality. A broad autonomous workflow is hard to evaluate and hard to reverse.

## Scenario

The sponsor is interested in automatic creation. The service desk still needs to verify the extracted details, and system access has not been confirmed.

## Outcomes

- Compare options against explicit criteria.
- Select a reversible first release with a clear user boundary.
- State exclusions and decision gates.

## Exercise

Score the Day 9 options against outcome potential, error impact, time to evidence, integration dependency, and reversibility. Choose a first slice. A reasonable candidate is suggested extraction into a draft that a coordinator reviews, with no automatic write; justify or reject it using evidence. Define what is out of scope and what must be learned before expanding.

## Deliverable

`scope.md` with chosen option, rejected alternatives, first-release boundary, exclusions, risks, and go/no-go evidence.

## Assessment

Pass if scope can be tested without production write access, preserves human confirmation of consequential fields, and names at least two reasons to stop or change direction.

## Reflection

What evidence would justify moving from recommendation to automatic action?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
