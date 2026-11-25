---
day: 67
phase: 5
status: Ready
title: Write an operations runbook
estimated_effort: 75–100 minutes
---

# Day 67 — Write an operations runbook

## Why this matters

Operators need concise actions for expected failures, safe containment, and escalation. A runbook is useful only if its commands and owners match the deployed shape.

## Scenario

An on-call engineer sees rising provider timeouts and stale approvals in the hypothetical pilot.

## Outcomes

- Turn alerts and states into safe operator steps.
- Include impact checks, containment, and recovery verification.
- Separate prototype commands from unimplemented production actions.

## Exercise

Write procedures for provider degradation, directory outage, growing approval backlog, suspected unauthorized action, and failed release. Each procedure names trigger, user impact, read-only diagnosis, containment authority, communication, recovery check, and escalation. Mark commands as verified, illustrative, or unavailable; do not invent access to Meridian systems.

## Deliverable

Runbook with an operator quick path and detailed procedures.

## Assessment

Pass when an unfamiliar reader can identify impact and stop unsafe writes without guessing, and unverified production steps are clearly marked.

## Reflection

Which step should be automated only after an operator has rehearsed it manually?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
