---
day: 63
phase: 5
status: Ready
title: Prepare environments and repeatable setup
estimated_effort: 90–120 minutes
---

# Day 63 — Prepare environments and repeatable setup

## Why this matters

“Works on my machine” is not an environment strategy. Repeatable setup lets a customer engineer reproduce a result and makes differences between test and pilot visible.

## Scenario

The Meridian platform engineer receives the repository but cannot access the original learner's environment or model cache.

## Outcomes

- Rebuild the service from a clean checkout.
- Identify environment-specific dependencies and data.
- Document setup and verification without hidden credentials.

## Exercise

Follow the starter README from a clean environment or isolated container. Install from the lockfile, load only synthetic fixtures, and run the assessments. Record runtime, required ports, external calls, and optional model assets. Compare local and hypothetical pilot settings; explicitly call out migrations or identity integration that are not implemented.

## Deliverable

Reproducibility record and environment matrix with verified commands.

## Assessment

Pass when another learner can reproduce the local demo from documented steps, no real secret or customer data is needed, and pilot-only gaps are listed.

## Reflection

What setup step is most likely to fail for a customer engineer behind a restricted network?
