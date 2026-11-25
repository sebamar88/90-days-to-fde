---
day: 73
phase: 5
status: Ready
title: Simulate a production incident
estimated_effort: 90–120 minutes
---

# Day 73 — Simulate a production incident

## Why this matters

Production readiness includes coordinated response under pressure. A tabletop connects the technical runbook to customer communication and decision rights.

## Scenario

In a hypothetical limited pilot, a prompt update increases unsafe urgency suggestions and the provider is also intermittently unavailable. This is a fictional exercise, not a report of a real event.

## Outcomes

- Detect and contain degraded or unsafe behavior.
- Coordinate technical and customer-facing roles.
- Define recovery evidence and a transparent incident update.

## Exercise

Run a tabletop with injects at detection, uncertain scope, sponsor inquiry, and recovery. Use the Day 58 playbook and Day 65 rollback plan. Decide whether to disable model suggestions, keep deterministic draft mode, or stop intake assistance entirely. Preserve synthetic evidence, assign communications, and state what must pass before re-enabling.

## Deliverable

Incident rehearsal timeline, decision record, and a sample customer update labeled hypothetical.

## Assessment

Pass when unsafe behavior is contained before optimization, users receive an accurate status, and re-enable criteria include evaluation and owner approval.

## Reflection

How would you communicate uncertainty without minimizing risk or speculating about cause?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
