---
day: 26
phase: 2
status: Ready
title: Version prompts and schemas
estimated_effort: 75–100 minutes
---

# Day 26 — Version prompts and schemas

## Why this matters

Prompt or schema edits change system behavior. If they are invisible, a quality regression becomes difficult to reproduce and compare.

## Scenario

Two prompt variants produce different category suggestions for the same request. The service needs to know which prompt and output schema generated each evaluation result.

## Outcomes

- Store prompt text and schema versions as reviewable artifacts.
- Attach stable version identifiers to evaluation outputs.
- Prevent secrets and customer data from entering prompts or logs.

## Exercise

Move the model instruction into a versioned text file and assign a schema version. Create a prompt fixture test for the four risk cases in the evaluation set. Record prompt version, schema version, provider/model identifier when available, and case ID in results. Do not log raw requests by default.

## Deliverable

Versioned prompt/schema artifacts and a reproducibility record format.

## Assessment

Pass when changing a prompt changes a visible version or commit, evaluation outputs identify both versions, and no secret or personal data appears in fixtures.

## Reflection

How would you diagnose a regression if the system recorded only the model name?
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
