---
schema_version: 1
id: day-71
day: 71
phase: 5
locale: en
slug: measure-workflow-impact-after-launch
title: Measure workflow impact after launch
description: Technical quality does not prove business impact.
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
  - day-70
objectives:
  - Define an outcome measure tied to the original discovery brief.
  - Specify baseline, observation window, exclusions, and comparison risks.
  - Include correction burden and safety outcomes, not just throughput.
tags:
  - phase-5
  - impact-measurement
skills:
  - impact-measurement
---

# Day 71 — Measure workflow impact after launch

## Why this matters

Technical quality does not prove business impact. A credible measurement plan compares the actual workflow before and after introduction while accounting for workload and user choice.

## Scenario

The sponsor wants to claim time saved. No baseline, production sample, or customer approval has been provided; numbers in this exercise must stay hypothetical.

## Outcomes

- Define an outcome measure tied to the original discovery brief.
- Specify baseline, observation window, exclusions, and comparison risks.
- Include correction burden and safety outcomes, not just throughput.

## Exercise

Choose one primary outcome and two guardrails. Write an analysis plan with unit of analysis, data source, sampling, missingness, comparison period, and confounders. Include manual-review time, correction rate, and unsafe-action incidents. Use a toy synthetic table to demonstrate the calculation; label it simulated and make no impact claim.

## Deliverable

Post-launch measurement plan and worked synthetic example.

## Assessment

Pass when the primary measure matches a customer outcome, guardrails can veto a positive result, and no simulated number is represented as actual impact.

## Reflection

What result would show that the assistant increases work even if average response time falls?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
