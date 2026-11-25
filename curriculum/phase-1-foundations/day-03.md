---
day: 3
phase: 1
status: Ready
title: See the work as it happens
estimated_effort: 75–100 minutes
---

# Day 3 — See the work as it happens

## Why this matters

Process descriptions often omit handoffs, workarounds, queues, and exceptions. A system built from an idealized process usually breaks on the first real case.

## Scenario

The service desk receives maintenance requests by email, then staff interpret the text and enter a work order in a legacy system. The actual path and exceptions are not yet verified.

## Outcomes

- Model a current-state workflow with actors, decisions, and handoffs.
- Mark delays, rework, exceptions, and missing evidence.
- Avoid drawing the desired future state as if it were current.

## Exercise

Draw a swimlane with requester, service desk, and technician. Use only scenario facts as solid steps; use dashed or `?` markers for assumptions. Include intake, clarification, urgency/location interpretation, entry, assignment, and completion feedback as questions to verify. Add likely exception paths without presenting them as observed.

## Deliverable

`current-state.md` with workflow, assumptions legend, and five observations to seek in a live walkthrough.

## Assessment

Pass if actors and handoffs are visible, unknown steps are marked, and the workflow contains at least one exception path and one feedback loop to investigate.

## Reflection

What important work might happen outside the official ticketing system?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
