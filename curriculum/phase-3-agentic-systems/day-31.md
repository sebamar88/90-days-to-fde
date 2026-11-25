---
schema_version: 1
id: day-31
day: 31
phase: 3
locale: en
slug: distinguish-an-agent-from-a-workflow
title: Distinguish an agent from a workflow
description: “Agentic” is not a reason to delegate control.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: architecture-challenge
difficulty: intermediate
duration:
  min: 75
  max: 100
prerequisites:
  - day-30
objectives:
  - Compare a fixed workflow, a model-assisted workflow, and a model-directed tool loop.
  - Identify which decisions require flexible language understanding and which should stay deterministic.
  - Recommend a bounded design with a measurable reason.
tags:
  - phase-3
  - autonomy-design
skills:
  - autonomy-design
---

# Day 31 — Distinguish an agent from a workflow

## Why this matters

“Agentic” is not a reason to delegate control. FDEs must choose the least complex system that meets the customer outcome and explain where nondeterminism is useful.

## Scenario

Meridian asks for an intake assistant that may look up a site and prepare a draft. The operations lead expects predictable steps; the product lead expects natural-language flexibility. Both expectations are simulated.

## Outcomes

- Compare a fixed workflow, a model-assisted workflow, and a model-directed tool loop.
- Identify which decisions require flexible language understanding and which should stay deterministic.
- Recommend a bounded design with a measurable reason.

## Exercise

Write three sequence diagrams for the same request: fixed rules, model extraction plus fixed orchestration, and model-selected tools. For each, mark every nondeterministic decision, external call, write, and recovery path. Score them against the Day 7 outcome and Day 12 write-boundary ADR. Choose a design and state what evidence would justify moving to a more autonomous option.

## Deliverable

`agent-boundary.md` with diagrams, decision comparison, chosen autonomy level, and a revisit trigger.

## Assessment

Pass when every consequential action has a deterministic application-controlled gate, the chosen design addresses a stated outcome, and a simpler alternative is fairly considered.

## Reflection

Which uncertainty actually requires model-directed planning, and which only makes the diagram look more advanced?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
