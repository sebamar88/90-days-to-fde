---
day: 46
phase: 4
status: Ready
title: Build a task-specific evaluation set
estimated_effort: 90–120 minutes
---

# Day 46 — Build a task-specific evaluation set

## Why this matters

An evaluation set is a measurement instrument. If it omits realistic ambiguity, high-impact language, or common failure cases, a score can be precise and still misleading.

## Scenario

Meridian reviewers want to know whether the service proposes useful intake fields without turning unsafe requests into actions. The only available material is synthetic.

## Outcomes

- Define evaluation units from the task and decision boundary.
- Cover ordinary, ambiguous, adversarial, and failure cases.
- Record provenance and limitations for every case.

## Exercise

Extend Phase 2 and 3 fixtures to at least 30 synthetic cases. Include category, location, urgency, missing fields, expected tool action, actor scope, and whether abstention is required. Tag cases by risk and scenario. Add a data card with authorship, intended use, excluded populations, and the explicit limitation that the set estimates no real-world prevalence.

## Deliverable

Versioned evaluation JSONL and dataset card with case-to-requirement coverage.

## Assessment

Pass when every label has a rationale, each critical control has at least one positive and negative case, and no record contains real personal data.

## Reflection

What behavior could score highly on your set while still frustrating a real coordinator?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
