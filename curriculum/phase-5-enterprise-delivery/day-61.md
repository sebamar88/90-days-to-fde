---
schema_version: 1
id: day-61
day: 61
phase: 5
locale: en
slug: choose-a-deployment-shape-from-constraints
title: Choose a deployment shape from constraints
description: Deployment architecture should follow customer constraints and operating capacity.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: architecture-challenge
difficulty: advanced
duration:
  min: 75
  max: 100
prerequisites:
  - day-60
objectives:
  - Compare local, managed-service, and customer-hosted options.
  - Identify constraints that determine the choice.
  - Document assumptions, operational burden, and a revisit trigger.
tags:
  - phase-5
  - deployment-architecture
skills:
  - deployment-architecture
---

# Day 61 — Choose a deployment shape from constraints

## Why this matters

Deployment architecture should follow customer constraints and operating capacity. Choosing a platform first can add cost and failure modes without improving the workflow.

## Scenario

Meridian has not confirmed data residency, network access, identity integration, request volume, or platform ownership. All current details are scenario assumptions.

## Outcomes

- Compare local, managed-service, and customer-hosted options.
- Identify constraints that determine the choice.
- Document assumptions, operational burden, and a revisit trigger.

## Exercise

Compare three deployment shapes against data location, egress, identity, uptime needs, model hosting, support ownership, cost, and reversibility. Mark each input as known, assumed, or requiring customer confirmation. Select a provisional path for a learning demo, then list the evidence needed before recommending it for a pilot. Do not choose Kubernetes by default.

## Deliverable

Deployment ADR with options, constraints, provisional decision, and open customer questions.

## Assessment

Pass when the chosen shape follows explicit constraints, operational ownership is named, and unknowns are not disguised as requirements.

## Reflection

Which single answer from Meridian's platform team could reverse your deployment recommendation?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
