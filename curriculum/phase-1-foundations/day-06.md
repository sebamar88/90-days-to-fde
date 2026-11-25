---
schema_version: 1
id: day-06
day: 6
phase: 1
locale: en
slug: separate-evidence-from-assumptions
title: Separate evidence from assumptions
description: Early discovery mixes observations, stakeholder beliefs, and engineering guesses.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: business-discovery-exercise
difficulty: foundational
duration:
  min: 60
  max: 90
prerequisites:
  - day-05
objectives:
  - Classify claims as observed, reported, inferred, or unknown.
  - Identify assumptions that could change scope or safety.
  - Choose the next cheapest evidence-gathering action.
tags:
  - phase-1
  - evidence-analysis
skills:
  - evidence-analysis
---

# Day 6 — Separate evidence from assumptions

## Why this matters

Early discovery mixes observations, stakeholder beliefs, and engineering guesses. Making their status visible prevents an untested assumption from becoming a requirement.

## Scenario

Your notes include a missing-location example, the phrase “sometimes,” a handoff to a technician, and no verified measurement of delays or rework.

## Outcomes

- Classify claims as observed, reported, inferred, or unknown.
- Identify assumptions that could change scope or safety.
- Choose the next cheapest evidence-gathering action.

## Exercise

Create an evidence table with columns: claim, source, type, confidence, impact if wrong, and next check. Add at least eight claims from Days 1–5. Rank assumptions by impact and uncertainty. For the top two, propose a low-cost way to check them (observation, record sample, or follow-up interview).

## Deliverable

`evidence-log.md` and two prioritized validation actions.

## Assessment

Pass if every claim has a source/type, unsupported quantitative claims are labeled unknown, and high-impact uncertain assumptions have a concrete check.

## Reflection

Which assumption would most change the solution if it were false?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
