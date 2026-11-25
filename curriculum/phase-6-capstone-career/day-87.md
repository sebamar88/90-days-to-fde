---
schema_version: 1
id: day-87
day: 87
phase: 6
locale: en
slug: publish-a-privacy-safe-portfolio-case-study
title: Publish a privacy-safe portfolio case study
description: A portfolio should make engineering judgment visible without disclosing customer information or implying outcomes that were never measured.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: capstone-milestone
difficulty: advanced
duration:
  min: 75
  max: 100
prerequisites:
  - day-86
objectives:
  - Explain the problem, constraints, decisions, and evidence.
  - Remove secrets, personal data, and unapproved stakeholder content.
  - State what the project does not prove.
tags:
  - phase-6
  - portfolio-evidence
skills:
  - portfolio-evidence
---

# Day 87 — Publish a privacy-safe portfolio case study

## Why this matters

A portfolio should make engineering judgment visible without disclosing customer information or implying outcomes that were never measured.

## Scenario

The learner wants to publish the Meridian capstone as evidence of FDE and applied AI skills. Meridian is fictional and all results are synthetic or local.

## Outcomes

- Explain the problem, constraints, decisions, and evidence.
- Remove secrets, personal data, and unapproved stakeholder content.
- State what the project does not prove.

## Exercise

Draft a case study with context, user workflow, architecture, trade-offs, evaluation method, failures fixed, and next steps. Label the customer as fictional, the feedback as simulated, and the metrics as synthetic/local. Search the repository for secrets and examine images/logs manually. Remove any claim that suggests production deployment or measured customer ROI.

## Deliverable

Portfolio case study and privacy/claim review checklist.

## Assessment

Pass when a reader can distinguish implementation from validation, all claims link to evidence, and no secret or real customer data is disclosed.

## Reflection

What limitation, if stated plainly, makes the case study more credible?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
