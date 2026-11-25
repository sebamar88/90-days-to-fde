---
day: 62
phase: 5
status: Ready
title: Separate configuration and secrets
estimated_effort: 75–100 minutes
---

# Day 62 — Separate configuration and secrets

## Why this matters

Environment-specific settings and credentials have different lifecycles and access needs. Mixing them into source or logs creates avoidable exposure and makes safe rotation harder.

## Scenario

The service has local, test, and hypothetical pilot settings. A provider key, sandbox URL, and timeout currently appear as developer assumptions.

## Outcomes

- Classify configuration versus secret material.
- Load settings without committing credentials.
- Define rotation, missing-value, and redaction behavior.

## Exercise

Create a configuration inventory with name, purpose, default, environment, secret classification, owner, and rotation trigger. Move settings into typed environment configuration; use placeholders in `.env.example` only. Verify startup fails clearly when a required pilot secret is missing and that logs never echo it. Keep the local deterministic path usable without any key.

## Deliverable

Configuration schema, `.env.example`, and secret-handling checklist.

## Assessment

Pass when no usable secret is committed, required settings are validated at startup, local learning requires no key, and the sentinel value is absent from logs.

## Reflection

Which secret could be removed entirely by choosing a different integration boundary?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
