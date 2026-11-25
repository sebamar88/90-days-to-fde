---
day: 72
phase: 5
status: Ready
title: Conduct a launch readiness review
estimated_effort: 90–120 minutes
---

# Day 72 — Conduct a launch readiness review

## Why this matters

Readiness is a cross-functional decision. A green test suite does not substitute for data approval, support ownership, training, security review, or a rollback path.

## Scenario

A fictional review board must decide whether a narrowly scoped, human-reviewed pilot can be proposed. No real Meridian representative has approved one.

## Outcomes

- Review evidence and open conditions across technical and customer workstreams.
- Assign go/no-go authority and owners.
- Distinguish a learning recommendation from customer authorization.

## Exercise

Build a readiness checklist for security, privacy, identity, evaluation, operations, user training, support, cost, and rollback. Attach evidence from prior phases or mark the item blocked. Role-play objections from one operations, one security, and one platform reviewer. Record the proposed decision, conditions, and person who must approve in a real engagement.

## Deliverable

Launch-readiness packet and decision log with every blocked item assigned.

## Assessment

Pass when no critical blocker is waived silently, decision authority is explicit, and the packet states that customer authorization is still required.

## Reflection

Which unresolved blocker should prevent even a limited pilot?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
