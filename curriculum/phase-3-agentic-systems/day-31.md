---
day: 31
phase: 3
status: Ready
title: Distinguish an agent from a workflow
estimated_effort: 75–100 minutes
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
