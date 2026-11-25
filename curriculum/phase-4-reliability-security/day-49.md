---
day: 49
phase: 4
status: Ready
title: Test prompt and model changes for regressions
estimated_effort: 90–120 minutes
---

# Day 49 — Test prompt and model changes for regressions

## Why this matters

Prompt, schema, model, and orchestration changes can shift behavior in ways ordinary unit tests miss. Versioned comparisons make changes reviewable and reversible.

## Scenario

A prompt edit improves summaries in three examples but changes urgency labels on another fixture. No production traffic is available for testing.

## Outcomes

- Record the exact candidate configuration and evaluation-set revision.
- Compare outputs case by case against the baseline.
- Block changes that regress a safety-critical slice.

## Exercise

Create a run manifest with code commit, prompt/schema versions, model identifier when applicable, temperature/settings, dataset revision, and timestamp. Compare baseline and candidate outputs using the frozen protocol. Add one regression fixture before accepting any behavior correction. Keep secrets and raw customer data out of the manifest.

## Deliverable

Evaluation run manifest, comparison report, and a change/revert recommendation.

## Assessment

Pass when another learner can reproduce the run, all differences are inspectable, and no aggregate gain overrides a safety-gate regression.

## Reflection

What evidence would distinguish a robust improvement from a lucky change on a tiny fixture?
