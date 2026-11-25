---
schema_version: 1
id: day-20
day: 20
phase: 2
locale: en
slug: return-schema-validated-suggestions
title: Return schema-validated suggestions
description: JSON that parses can still contain missing keys, unsupported labels, or invalid business values.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: intermediate
duration:
  min: 90
  max: 120
prerequisites:
  - day-19
objectives:
  - Generate a schema from an application-owned model.
  - Validate decoded output and distinguish schema errors from transport/refusal/incomplete outcomes.
  - Keep business rules outside the generation schema where appropriate.
tags:
  - phase-2
  - structured-output
skills:
  - structured-output
---

# Day 20 — Return schema-validated suggestions

## Why this matters

JSON that parses can still contain missing keys, unsupported labels, or invalid business values. Validate untrusted model output at the boundary and handle refusals or incomplete responses explicitly.

## Scenario

An optional model provider may suggest category, location, urgency, summary, and missing fields. The service owns final validation and always presents suggestions for human review.

## Outcomes

- Generate a schema from an application-owned model.
- Validate decoded output and distinguish schema errors from transport/refusal/incomplete outcomes.
- Keep business rules outside the generation schema where appropriate.

## Exercise

Use Pydantic to define the output schema, reject extra properties, and validate an adapter response. Add test fixtures for valid output, invalid enum, missing required value, malformed JSON, refusal, and truncated output. If you add a provider, use a supported structured-output mode or local Ollama JSON Schema path, but retain the same application validation.

## Deliverable

Schema, parser, provider-specific capability note if applicable, and edge-case tests.

## Assessment

Pass when malformed, refused, or incomplete output cannot become an accepted draft; schema validation is tested separately from business-rule checks.

## Reflection

Which failures should the API return to a coordinator, and which should remain internal provider diagnostics?

## References

- [Pydantic models and validation](https://docs.pydantic.dev/latest/concepts/models/)
- [OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [Ollama structured outputs](https://ollama.com/blog/structured-outputs)
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
