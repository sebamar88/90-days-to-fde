---
day: 14
phase: 1
status: Ready
title: Play the plan back to the customer
estimated_effort: 60–90 minutes
---

# Day 14 — Play the plan back to the customer

## Why this matters

A playback catches mismatched definitions of the problem, success, and acceptable risk before a team invests in implementation.

## Scenario

You have a discovery packet, but the coordinator, sponsor, and IT owner may have different views. Prepare a short playback that invites correction rather than approval theater.

## Outcomes

- Summarize evidence, uncertainties, and proposed next step plainly.
- Separate stakeholder-confirmed statements from your recommendation.
- Ask for concrete corrections and decisions.

## Exercise

Write a five-minute playback: what we heard, what we observed or simulated, what remains unknown, the outcome measure, the bounded slice, and the decision needed next. Include three correction prompts. If no real customer is available, label the playback as a rehearsal, not customer validation.

## Deliverable

`customer-playback.md` plus a decision log with who must confirm the next gate.

## Assessment

Pass if the summary does not overstate simulated evidence, asks the customer to correct the problem and metric definitions, and makes a specific low-risk next-step request.

## Reflection

What feedback would cause you to stop building the proposed slice?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
