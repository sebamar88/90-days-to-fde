---
day: 88
phase: 6
status: Ready
title: Practice customer and technical interviews
estimated_effort: 75–100 minutes
---

# Day 88 — Practice customer and technical interviews

## Why this matters

FDE interviews test listening, trade-off reasoning, delivery judgment, and communication under ambiguity as well as implementation skill.

## Scenario

Practice with one interviewer playing an operations sponsor and another a skeptical staff engineer. Their prompts are fictional and are not hiring advice from a specific employer.

## Outcomes

- Ask clarifying questions before proposing architecture.
- Explain one technical trade-off and one failure decision clearly.
- Reflect on feedback without overstating contribution or outcome.

## Exercise

Run two 15-minute rounds. In the customer round, discover the workflow, outcome, and constraints before recommending a thin slice. In the technical round, whiteboard the trust boundary, idempotency approach, and degraded mode. Use the capstone as an example with “situation, action, evidence, limitation.” Record questions you missed and one concise revision to each answer.

## Deliverable

Interview practice notes and two evidence-based story outlines.

## Assessment

Pass when the customer round includes clarifying questions and a playback, the technical round includes a failure path, and claims match the evidence register.

## Reflection

Which question helped you discover a constraint before designing a solution?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
