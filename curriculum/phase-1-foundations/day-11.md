---
schema_version: 1
id: day-11
day: 11
phase: 1
locale: en
slug: draw-the-system-context
title: Draw the system context
description: A context diagram reveals actors, trust boundaries, systems, and data movement before implementation choices become expensive.
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
  - day-10
objectives:
  - Draw a system context that distinguishes current systems from proposed components.
  - Show data flows and trust boundaries.
  - Mark unverified integration assumptions.
tags:
  - phase-1
  - system-context
skills:
  - system-context
---

# Day 11 — Draw the system context

## Why this matters

A context diagram reveals actors, trust boundaries, systems, and data movement before implementation choices become expensive.

## Scenario

The proposed slice receives a request, extracts fields, shows a draft to a coordinator, and may later create a work order after approval. The mail and work-order interfaces remain unverified.

## Outcomes

- Draw a system context that distinguishes current systems from proposed components.
- Show data flows and trust boundaries.
- Mark unverified integration assumptions.

## Exercise

Create a Mermaid or hand-drawn context diagram with requester, email intake, proposed assistant, coordinator, identity provider, work-order system, and operations owner. Show read/write directions and label sensitive data flows. Use dashed lines for unconfirmed interfaces; do not imply the assistant has permissions that have not been agreed.

## Deliverable

`system-context.md` with diagram, boundary notes, and five questions for system owners.

## Assessment

Pass if people and systems are distinct, data and authority flows are visible, and unknown interfaces are marked rather than asserted.

## Reflection

Where does data cross an organizational or trust boundary in your diagram?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
