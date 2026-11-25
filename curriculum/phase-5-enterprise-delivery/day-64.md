---
schema_version: 1
id: day-64
day: 64
phase: 5
locale: en
slug: add-a-deployment-pipeline
title: Add a deployment pipeline
description: CI can reduce release risk but also executes code with permissions.
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
  - day-63
objectives:
  - Define build, test, artifact, and release stages.
  - Limit workflow permissions and credential exposure.
  - Keep deployment approval separate from pull-request validation.
tags:
  - phase-5
  - ci-cd-security
skills:
  - ci-cd-security
---

# Day 64 — Add a deployment pipeline

## Why this matters

CI can reduce release risk but also executes code with permissions. A useful pipeline verifies the artifact and limits what untrusted changes can access.

## Scenario

The repository already runs curriculum and Phase 2 checks. A future container build should not receive production credentials from pull requests.

## Outcomes

- Define build, test, artifact, and release stages.
- Limit workflow permissions and credential exposure.
- Keep deployment approval separate from pull-request validation.

## Exercise

Draw the pipeline from pull request through release. Identify each job's token permissions, artifacts, and trust source. Specify tests and dependency checks before build, immutable artifact identity, environment approval, and who can promote. Review the current Actions workflow for broad permissions and mutable external actions; propose the smallest safe change without creating a cloud deployment.

## Deliverable

Pipeline diagram, permission matrix, and release checklist.

## Assessment

Pass when pull requests receive no production secrets, job permissions are minimal, release artifacts are traceable to a commit, and deployment requires an accountable approval.

## Reflection

What can a malicious contribution change if a workflow runs with a write token?

## References

- [GitHub Actions security](https://docs.github.com/en/actions/how-tos/secure-your-work)
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
