---
schema_version: 1
id: day-55
day: 55
phase: 4
locale: en
slug: minimize-and-protect-sensitive-data
title: Minimize and protect sensitive data
description: Data minimization reduces exposure across prompts, logs, evaluation fixtures, and support workflows.
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
  - day-54
objectives:
  - Map collection, processing, storage, and deletion for each data field.
  - Define a minimal retention and access policy for the prototype.
  - Detect accidental secrets or personal data in fixtures and telemetry.
tags:
  - phase-4
  - privacy-engineering
skills:
  - privacy-engineering
---

# Day 55 — Minimize and protect sensitive data

## Why this matters

Data minimization reduces exposure across prompts, logs, evaluation fixtures, and support workflows. “Synthetic” should be verifiable, not merely asserted.

## Scenario

The simulated reviewer asks whether request text is stored, sent to a provider, retained in traces, or reused in evaluation. The project has no approved real-data agreement.

## Outcomes

- Map collection, processing, storage, and deletion for each data field.
- Define a minimal retention and access policy for the prototype.
- Detect accidental secrets or personal data in fixtures and telemetry.

## Exercise

Create a field-level data inventory for request text, normalized fields, actor ID, preview hash, logs, and evaluation cases. For each, state purpose, location, access, retention, and deletion. Add a repository scan/check for obvious secret patterns, and manually review fixtures for identifying details. Keep real customer data out of this exercise.

## Deliverable

Data-flow inventory, retention table, and privacy review checklist.

## Assessment

Pass when every stored or transmitted field has a purpose and owner, raw text is excluded from ordinary telemetry, and the deletion path is testable or clearly marked as a prototype gap.

## Reflection

What information can the service discard immediately after producing a reviewable suggestion?
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
