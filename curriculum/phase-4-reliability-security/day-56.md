---
schema_version: 1
id: day-56
day: 56
phase: 4
locale: en
slug: review-supply-chain-and-dependency-risk
title: Review supply chain and dependency risk
description: An application inherits risk from libraries, build actions, base images, and model artifacts.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: advanced
duration:
  min: 75
  max: 100
prerequisites:
  - day-55
objectives:
  - Inventory direct and transitive dependencies and workflow actions.
  - Identify update, vulnerability, and provenance signals.
  - Set a practical review and response policy without claiming zero risk.
tags:
  - phase-4
  - supply-chain-security
skills:
  - supply-chain-security
---

# Day 56 — Review supply chain and dependency risk

## Why this matters

An application inherits risk from libraries, build actions, base images, and model artifacts. A lockfile improves repeatability but is not proof that a dependency is safe.

## Scenario

The prototype uses Python packages, a GitHub Actions workflow, and optionally a local model artifact. The simulated platform team asks what is pinned and what can execute during CI.

## Outcomes

- Inventory direct and transitive dependencies and workflow actions.
- Identify update, vulnerability, and provenance signals.
- Set a practical review and response policy without claiming zero risk.

## Exercise

Inspect the lockfile and CI workflow. Record package names, versions, source, update owner, and whether code executes in CI. Review action permissions and pinning choices. For an optional model artifact, record publisher, checksum/version mechanism, license, storage needs, and removal steps. Prioritize one improvement and state its maintenance cost.

## Deliverable

Dependency inventory, workflow review, and a short supply-chain risk decision.

## Assessment

Pass when direct dependencies, CI actions, and optional model artifacts are covered; update responsibility is named; and remaining unknown provenance is explicit.

## Reflection

Which pinning or verification choice would create the most maintenance burden for this small open-source project?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
