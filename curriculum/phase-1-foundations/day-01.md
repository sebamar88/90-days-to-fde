---
day: 1
phase: 1
status: Ready
title: From request to business outcome
estimated_effort: 60–90 minutes
---

# Day 1 — From request to business outcome

## Why this matters

An FDE is often handed a proposed solution before anyone has agreed on the problem. Treating the request as the problem leads to polished software that does not change the work.

## Scenario

Meridian Facilities' VP of Operations says: “We need an AI agent to read maintenance emails and create work orders automatically.” You have not yet met the service desk or seen the current process.

## Outcomes

- Separate the requested feature from the outcome it might serve.
- Name what is known, assumed, and still unknown.
- Write a neutral problem statement that does not commit to AI.

## Exercise

Create `problem-brief.md` with four sections: exact request, plausible underlying need, evidence available, and questions to resolve. Draft a problem statement in this form: “When [situation], [user] needs to [job], because [impact]. Today [evidence or unknown].” Then list three alternative explanations for why requests are delayed.

## Deliverable

A one-page problem brief with at least five open questions and no solution prescribed in the problem statement.

## Assessment

Pass when the brief clearly distinguishes quote from interpretation, does not present guesses as facts, and identifies at least one affected user beyond the VP. Revise if “AI agent” appears as a requirement rather than a hypothesis.

## Reflection

What would you need to observe before claiming the proposed system could reduce delay?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
