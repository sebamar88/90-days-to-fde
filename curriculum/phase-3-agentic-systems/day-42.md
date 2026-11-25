---
day: 42
phase: 3
status: Ready
title: Simulate a stakeholder escalation
estimated_effort: 60–90 minutes
---

# Day 42 — Simulate a stakeholder escalation

## Why this matters

FDE work includes surfacing trade-offs when stakeholder goals conflict. A clear escalation preserves trust and avoids silently changing the safety boundary.

## Scenario

In a role-play, operations wants automatic routing this week, while security has not approved identity scopes and a site manager reports that location codes are inconsistent. All participants and statements are fictional prompts, not customer evidence.

## Outcomes

- Separate observed facts, assumptions, and requested decisions.
- Present options with impact, owner, and evidence gap.
- Recommend a reversible next step without implying approval.

## Exercise

Role-play a 15-minute review with an operations sponsor and security reviewer. Use the discovery note template to capture exact claims. Present three options: keep draft-only, enable sandbox submissions, or defer integration. Ask for one explicit decision and owner for each unresolved dependency. Write a short playback and invite correction.

## Deliverable

`escalation-record.md` with simulated transcript notes, options, decisions requested, and follow-up owners.

## Assessment

Pass when simulated statements are labeled as such, no unapproved production behavior is promised, and the playback identifies a reversible next action and accountable owner.

## Reflection

How would you respond if the sponsor interpreted a prototype demo as a production commitment?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
