---
day: 82
phase: 6
status: Ready
title: Deploy or document a reproducible deployment
estimated_effort: 90–120 minutes
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
