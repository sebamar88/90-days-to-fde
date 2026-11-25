---
schema_version: 1
id: day-15
day: 15
phase: 1
locale: en
slug: phase-review-discovery-packet-and-next-step-gate
title: Phase review — discovery packet and next-step gate
description: The first two weeks are successful when the team has better evidence and a safer decision, not when it has committed to an AI build.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: phase-assessment
difficulty: foundational
duration:
  min: 90
  max: 120
prerequisites:
  - day-14
objectives:
  - Present the problem, evidence, metric, constraints, options, decision, and thin slice as one coherent story.
  - Identify unresolved risks and accountable owners.
  - Make a justified proceed, revise, or stop recommendation.
tags:
  - phase-1
  - discovery-synthesis
skills:
  - discovery-synthesis
---

# Day 15 — Phase review: discovery packet and next-step gate

## Why this matters

The first two weeks are successful when the team has better evidence and a safer decision, not when it has committed to an AI build.

## Scenario

You will review the cumulative Meridian packet as if you were a skeptical operations sponsor and an integration/security reviewer.

## Outcomes

- Present the problem, evidence, metric, constraints, options, decision, and thin slice as one coherent story.
- Identify unresolved risks and accountable owners.
- Make a justified proceed, revise, or stop recommendation.

## Exercise

Assemble the Days 1–14 artifacts. Conduct two reviews: (1) operations asks whether the outcome and workflow are represented accurately; (2) IT/security asks about data, access, writes, and failure boundaries. Record each objection, response, and evidence gap. Make a gate recommendation with explicit conditions.

## Deliverable

`phase-1-review.md` linking the complete discovery packet and listing decisions, risks, owners, and next evidence.

## Assessment rubric

Score each 0 (missing), 1 (partial), or 2 (clear and evidence-backed): problem framing; stakeholder/workflow evidence; measurable outcome and guardrails; data/access constraints; alternatives and AI justification; safe thin-slice boundary; clear customer communication. Pass at 11/14 with no zero for constraints or safety boundary. A lower score means revise the packet, not rush to Phase 2.

## Reflection

Which decision in your packet is strongest, and which depends on the weakest evidence?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
