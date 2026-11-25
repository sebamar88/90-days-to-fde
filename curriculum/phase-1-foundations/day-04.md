---
schema_version: 1
id: day-04
day: 4
phase: 1
locale: en
slug: prepare-a-discovery-interview
title: Prepare a discovery interview
description: Leading questions collect agreement, not evidence.
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
  - day-03
objectives:
  - Ask open questions about specific past behavior.
  - Probe for frequency, impact, exceptions, and workarounds.
  - Set expectations and take notes responsibly.
tags:
  - phase-1
  - interview-design
skills:
  - interview-design
---

# Day 4 — Prepare a discovery interview

## Why this matters

Leading questions collect agreement, not evidence. A good interview reconstructs a recent event and lets the participant describe their own work.

## Scenario

You have 30 minutes with a service-desk coordinator. You need to learn what happens from message arrival to work-order creation without selling a solution.

## Outcomes

- Ask open questions about specific past behavior.
- Probe for frequency, impact, exceptions, and workarounds.
- Set expectations and take notes responsibly.

## Exercise

Write a 30-minute guide: 3-minute intro/consent, 20-minute recent-case walkthrough, 5-minute impact and exception probes, 2-minute close. Include eight non-leading questions. Replace “Would an AI assistant help?” with questions about the last difficult request, what the participant did, what happened next, and how often it occurs.

## Deliverable

`interview-guide.md` with objective, script, questions, and a note-taking template separating quote, observation, and interpretation.

## Assessment

Pass if at least six questions ask about actual behavior, no question assumes AI is desired, and the intro says how notes will be used and that no sensitive data should be recorded.

## Reflection

Which of your questions is most likely to bias the answer, and how can you rephrase it?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
