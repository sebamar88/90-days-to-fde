---
schema_version: 1
id: day-50
day: 50
phase: 4
locale: en
slug: add-structured-logs-and-traces
title: Add structured logs and traces
description: When a multi-step request fails, operators need to connect the API request, model call, tool call, approval, and sandbox result without collecting unnecessary content.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-49
objectives:
  - Define correlation and trace boundaries for one workflow.
  - Record useful status and duration fields with bounded cardinality.
  - Redact request content, secrets, and sensitive model output.
tags:
  - phase-4
  - observability
skills:
  - observability
---

# Day 50 — Add structured logs and traces

## Why this matters

When a multi-step request fails, operators need to connect the API request, model call, tool call, approval, and sandbox result without collecting unnecessary content.

## Scenario

The simulated on-call engineer can see a generic 500 error but cannot tell whether lookup, generation, policy evaluation, or submission failed.

## Outcomes

- Define correlation and trace boundaries for one workflow.
- Record useful status and duration fields with bounded cardinality.
- Redact request content, secrets, and sensitive model output.

## Exercise

Instrument a synthetic request with spans for intake, provider call, tool invocation, approval, and sandbox submission. Add request ID, operation name, outcome, retry count, and duration; do not attach prompt or raw maintenance text. Trigger one timeout and trace the parent/child relationship. Validate redaction with a sentinel secret.

## Deliverable

Trace example, structured log schema, and privacy/redaction test.

## Assessment

Pass when the failure can be located from the trace, event names use bounded values, and neither input text nor sentinel secret appears in telemetry.

## Reflection

What diagnostic detail is useful to a restricted audit record but unsafe in a broadly accessible trace?

## References

- [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/)
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
