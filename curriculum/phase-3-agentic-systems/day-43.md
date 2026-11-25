---
day: 43
phase: 3
status: Ready
title: Evaluate tool selection and policy adherence
estimated_effort: 90–120 minutes
---

# Day 43 — Evaluate tool selection and policy adherence

## Why this matters

Task success alone hides unsafe tool choices. A workflow can return the right answer while querying an unauthorized source or attempting an unnecessary write.

## Outcomes

- Create cases that measure tool choice, argument quality, and policy adherence.
- Separate task completion from safety-critical errors.
- Compare the deterministic planner with an optional model planner.

## Scenario

The evaluation set includes a clear site lookup, an unknown site, a request to create a production work order, and prompt text that asks the system to ignore its tool rules.

## Exercise

Add at least 12 synthetic cases with expected action, allowed tools, expected arguments, approval requirement, and prohibited actions. Include benign requests, missing data, injection-like text, wrong-region actors, and ambiguous requests. Score valid tool choice, argument validity, unauthorized invocation, and unnecessary invocation. Keep unauthorized invocation as a zero-tolerance slice regardless of aggregate score.

## Deliverable

Tool-policy evaluation JSONL, scoring script or worksheet, and baseline results.

## Assessment

Pass when every case has a rationale, unsafe invocation is reported separately, and aggregate success cannot mask any unauthorized write attempt.

## Reflection

Would you ship a planner with better task completion but one attempted unauthorized action? State your release rule.
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
