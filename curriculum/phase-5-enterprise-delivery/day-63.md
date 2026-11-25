---
schema_version: 1
id: day-63
day: 63
phase: 5
locale: en
slug: prepare-environments-and-repeatable-setup
title: Prepare environments and repeatable setup
description: “Works on my machine” is not an environment strategy.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-62
objectives:
  - Rebuild the service from a clean checkout.
  - Identify environment-specific dependencies and data.
  - Document setup and verification without hidden credentials.
tags:
  - phase-5
  - reproducible-deployment
skills:
  - reproducible-deployment
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
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
