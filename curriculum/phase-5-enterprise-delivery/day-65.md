---
day: 65
phase: 5
status: Ready
title: Define rollback and release controls
estimated_effort: 75–100 minutes
---

# Day 65 — Define rollback and release controls

## Why this matters

A release without an observable stop condition is not controlled. Rollback must restore a known application/configuration state and account for any data or external actions already performed.

## Scenario

The candidate release changes a prompt, schema, and tool policy. A bad result could produce incorrect draft suggestions but still must not submit unapproved actions.

## Outcomes

- Define staged promotion and release owners.
- Select rollback triggers based on safety and service indicators.
- Separate code rollback from irreversible external side effects.

## Exercise

Write a staged release plan: local, synthetic evaluation, restricted pilot, and wider use (the latter two remain hypothetical). Define stop/rollback triggers, approver, last-known-good artifact, configuration compatibility, and communication path. Simulate a failing safety case and show how rollout halts. Record how submitted sandbox actions are reconciled rather than “rolled back.”

## Deliverable

Release/rollback playbook and one completed rehearsal record.

## Assessment

Pass when a named owner can halt promotion, triggers are measurable, last-known-good versions are identifiable, and irreversible writes have a reconciliation path.

## Reflection

Which change cannot be undone by redeploying the previous application version?
