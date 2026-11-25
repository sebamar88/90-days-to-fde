---
day: 40
phase: 3
status: Ready
title: Design audit events
estimated_effort: 75–100 minutes
---

# Day 40 — Design audit events

## Why this matters

Operators need to reconstruct who requested, approved, and executed an action. Audit records should explain the decision without becoming a second copy of sensitive customer data.

## Scenario

Meridian's reviewer asks for a timeline of draft creation and approval. The simulated security reviewer prohibits storing raw request text in general logs.

## Outcomes

- Define events for state transitions and external actions.
- Capture correlation, actor, policy result, and version references.
- Exclude secrets and unnecessary payloads.

## Exercise

Specify a versioned event schema for `draft_created`, `approval_granted`, `submission_attempted`, and `submission_confirmed`. Use synthetic IDs, timestamp, actor subject, prior/new state, decision reason code, policy version, and preview hash. Add a redaction rule for raw text, tokens, and provider output; test the event encoder with a sentinel secret.

## Deliverable

Audit-event schema, four sample JSON events, and a redaction test.

## Assessment

Pass when event order is reconstructable, each write links to approval and policy versions, and the sentinel secret does not appear in serialized output.

## Reflection

Which audit detail belongs in a restricted record rather than ordinary operational logs?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
