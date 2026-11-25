---
day: 79
phase: 6
status: Ready
title: Add authorization and approval boundaries
estimated_effort: 90–120 minutes
---

# Day 79 — Add authorization and approval boundaries

## Why this matters

The happy path is incomplete until it proves that an unauthorized actor, changed preview, or untrusted instruction cannot cause an action.

## Scenario

The same synthetic workflow is exercised by an in-region coordinator, a cross-region coordinator, an auditor, and an unauthenticated caller.

## Outcomes

- Enforce trusted actor context at every action boundary.
- Bind approval to immutable preview content and target environment.
- Demonstrate that denied paths make no downstream call.

## Exercise

Implement or assemble the authorization checks and preview-bound approval flow. Add tests for correct approval, preview edit after approval, wrong-region actor, auditor write attempt, missing actor, cancelled request, and forged role text. Assert that the adapter call count remains zero for every denied case.

## Deliverable

Authorization/approval implementation evidence and negative-test report.

## Assessment

Pass when only an authorized actor can approve the exact preview, every denial occurs before the write adapter, and the model cannot supply identity or approval.

## Reflection

What is the strongest evidence that a human approval is about the action the system actually performed?
