---
day: 80
phase: 6
status: Ready
title: Complete evaluation and regression evidence
estimated_effort: 90–120 minutes
---

# Day 80 — Complete evaluation and regression evidence

## Why this matters

A final demo can be curated to hide known failure cases. A versioned evaluation run and regression gate make claims inspectable beyond the demo script.

## Outcomes

- Re-run the frozen evaluation against the capstone commit.
- Report quality by slice and safety gate.
- Preserve enough run metadata to reproduce the result.

## Scenario

The simulated release reviewer asks whether the latest tool, prompt, or schema change altered behavior on prior cases.

## Exercise

Run every evaluation case against the deterministic baseline and selected capstone path. Capture commit, configuration, dataset revision, environment, and result. Compare with the prior phase report. Inspect all unsafe-action and abstention failures individually; add a regression fixture for each fixed defect. If an optional provider is unavailable, report the deterministic run and leave provider metrics unclaimed.

## Deliverable

Capstone evaluation report, run manifest, regression cases, and limitations section.

## Assessment

Pass when all scores have denominators, safety failures are individually dispositioned, and provider results are claimed only if actually run.

## Reflection

What evidence would make the deterministic baseline the better final recommendation?
