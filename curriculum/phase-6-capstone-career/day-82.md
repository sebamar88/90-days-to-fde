---
schema_version: 1
id: day-82
day: 82
phase: 6
locale: en
slug: deploy-or-document-a-reproducible-deployment
title: Deploy or document a reproducible deployment
description: Deployment practice should be proportional to the learning objective and environment access.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: capstone-milestone
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-81
objectives:
  - Reproduce the service from a clean environment.
  - Verify configuration and health behavior without exposing secrets.
  - Document the deployment boundary and missing production prerequisites.
tags:
  - phase-6
  - deployment-reproducibility
skills:
  - deployment-reproducibility
---

# Day 82 — Deploy or document a reproducible deployment

## Why this matters

Deployment practice should be proportional to the learning objective and environment access. A well-documented local deployment can be more honest than an unowned cloud demo.

## Scenario

No real Meridian account, identity provider, or deployment permission is available. The learner may run locally or use an independently authorized personal sandbox.

## Outcomes

- Reproduce the service from a clean environment.
- Verify configuration and health behavior without exposing secrets.
- Document the deployment boundary and missing production prerequisites.

## Exercise

Choose local/container deployment or a permitted sandbox. Record exact setup and teardown steps. Verify startup/readiness behavior, synthetic data path, and absence of public credentials. If a cloud environment is unavailable, use a local run and provide a deployment manifest walkthrough instead of fabricating a live service. Do not publish an endpoint containing personal or customer data.

## Deliverable

Reproducible deployment record, environment assumptions, teardown instructions, and production gap list.

## Assessment

Pass when another learner can reproduce and stop the system, no secret is exposed, and production-only prerequisites are stated plainly.

## Reflection

What would need to change before this deployment could handle real customer traffic?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
