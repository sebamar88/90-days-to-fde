---
day: 55
phase: 4
status: Ready
title: Minimize and protect sensitive data
estimated_effort: 75–100 minutes
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
