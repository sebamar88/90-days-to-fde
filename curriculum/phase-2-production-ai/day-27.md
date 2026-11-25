---
day: 27
phase: 2
status: Ready
title: Measure latency and cost
estimated_effort: 75–100 minutes
---

# Day 27 — Measure latency and cost

## Why this matters

An accurate result may still be too slow or expensive for the workflow. Measure actual behavior and keep provider-specific token pricing outside the core interface.

## Scenario

Coordinators process a queue and need a response within a locally agreed target. No customer target or production volume has been supplied, so do not fabricate an SLO or cost forecast.

## Outcomes

- Measure end-to-end latency for representative cases.
- Record provider usage metadata when available without requiring it from all providers.
- Separate measured cost from assumptions and rate-card estimates.

## Exercise

Run repeated trials against the deterministic provider and any optional model path. Record p50/p95 latency, error/timeout rate, and provider token/cost metadata when supplied. Label the sample size, machine, model, and date. Do not use synthetic timing as a production SLA.

## Deliverable

A small benchmark report and an instrumentation interface that does not expose raw message content.

## Assessment

Pass when metrics can be reproduced from the recorded setup, provider-missing cost is marked unavailable rather than zero, and the report distinguishes measurements from estimates.

## Reflection

Which measurement would change your architecture decision most: latency tail, failure rate, or cost per reviewed draft?
