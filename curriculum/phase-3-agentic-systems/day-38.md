---
schema_version: 1
id: day-38
day: 38
phase: 3
locale: en
slug: map-enterprise-system-boundaries
title: Map enterprise system boundaries
description: Integration work crosses ownership, data, identity, and operational boundaries.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: architecture-challenge
difficulty: intermediate
duration:
  min: 75
  max: 100
prerequisites:
  - day-37
objectives:
  - Map trust zones, data flows, and owners.
  - Identify where identity and policy are enforced.
  - Record integration assumptions that need customer confirmation.
tags:
  - phase-3
  - system-integration
skills:
  - system-integration
---

# Day 38 — Map enterprise system boundaries

## Why this matters

Integration work crosses ownership, data, identity, and operational boundaries. A technically reachable API is not automatically an approved dependency.

## Scenario

The proposed workflow touches the intake service, synthetic site directory, identity provider, human approval screen, and work-order sandbox. Their owners and service levels are simulated.

## Outcomes

- Map trust zones, data flows, and owners.
- Identify where identity and policy are enforced.
- Record integration assumptions that need customer confirmation.

## Exercise

Extend the Day 11 system-context diagram with containers and a sequence for one request. Label protocol, data class, direction, credential owner, failure response, and whether the boundary is trusted. Add explicit lines for approval and sandbox writes. List three facts that remain unknown until Meridian's real IT/security owners confirm them.

## Deliverable

Updated context/container diagram, sequence diagram, and integration question log.

## Assessment

Pass when every external call has an owner, data classification, and failure path, and all unverified assumptions are clearly labeled as simulated.

## Reflection

Which boundary would change your design most if its owner prohibited outbound network access?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
