---
day: 44
phase: 3
status: Ready
title: Run a failure-injection exercise
estimated_effort: 90–120 minutes
---

# Day 44 — Run a failure-injection exercise

## Why this matters

Failure paths should be observed before a customer depends on them. Small, controlled injections reveal missing state transitions and operator guidance.

## Scenario

In a local sandbox, the directory becomes unavailable, approval expires, the process restarts after submission, and the audit sink rejects an event. No production system is involved.

## Outcomes

- Inject failures at declared boundaries and observe system behavior.
- Verify state, duplicate protection, and operator signals.
- Record unexpected behavior without hiding it.

## Exercise

Run one injection at a time using deterministic fakes. For each, record trigger, expected state, observed state, user message, audit event, and recovery action. Include a restart after ambiguous submission and a denied audit write. Stop the exercise if the fake adapter unexpectedly reaches any real endpoint; record the safety incident and reset the environment.

## Deliverable

`phase-3-failure-report.md` with evidence, severity, owner, and a prioritized correction list.

## Assessment

Pass when all four injections are reproducible, no failure bypasses authorization or approval, and each non-recoverable state has a human recovery path.

## Reflection

Which fault was hardest to distinguish from a slow but healthy dependency?
