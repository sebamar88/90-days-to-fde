---
schema_version: 1
id: day-29
day: 29
phase: 2
locale: en
slug: package-a-repeatable-local-demo
title: Package a repeatable local demo
description: A demo should work for a reviewer from a clean checkout and make its environment, data, and limitations clear.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: intermediate
duration:
  min: 75
  max: 100
prerequisites:
  - day-28
objectives:
  - Document a fresh setup and one-command test/demo path.
  - Make provider and model selection explicit.
  - Include a failure and abstention demonstration, not just the happy path.
tags:
  - phase-2
  - reproducible-development
skills:
  - reproducible-development
---

# Day 29 — Package a repeatable local demo

## Why this matters

A demo should work for a reviewer from a clean checkout and make its environment, data, and limitations clear. A paid endpoint or a developer's local secrets should not be hidden prerequisites.

## Scenario

You need to show a coordinator the draft-only workflow using synthetic messages. The deterministic path must work offline; a local model path is optional.

## Outcomes

- Document a fresh setup and one-command test/demo path.
- Make provider and model selection explicit.
- Include a failure and abstention demonstration, not just the happy path.

## Exercise

Follow your own setup from a clean environment. Run the automated assessment suite, start the local API, submit one complete and one ambiguous request, and show a downstream sandbox failure. If you add Ollama, document model download size and hardware assumptions separately and keep it optional.

## Deliverable

Quickstart, demo script or command sequence, synthetic sample inputs, and known-limitations section.

## Assessment

Pass when a peer can reproduce the offline path without secrets, observe a review-required result, and understand that no production system is connected.

## Reflection

What did the demo make look easier or more certain than it actually is?

## References

- [Ollama structured outputs](https://ollama.com/blog/structured-outputs)
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
