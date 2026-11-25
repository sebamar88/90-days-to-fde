---
day: 86
phase: 6
status: Ready
title: Prepare a live demo with failure paths
estimated_effort: 90–120 minutes
---

# Day 86 — Prepare a live demo with failure paths

## Why this matters

A credible demo shows how a system handles uncertainty and failure, not only its best response. Rehearsal also prevents accidental use of real data or credentials.

## Scenario

The audience includes a prospective technical reviewer and operations stakeholder. The demo runs entirely on synthetic fixtures.

## Outcomes

- Tell a clear customer-outcome story in a bounded time.
- Demonstrate success, denial, and recovery paths.
- Prepare a safe fallback if the demo environment fails.

## Exercise

Script a seven-minute demo: problem and limits, normal request, correction, approval-bound action, unauthorized denial, and dependency failure/degraded mode. Rehearse from a clean reset. Prepare screenshots or terminal captures as a fallback and ensure they are synthetic and labeled. Finish with measured evidence and open questions, not a job or impact claim.

## Deliverable

Demo script, reset instructions, failure-path checklist, and privacy-reviewed backup material.

## Assessment

Pass when the demo is reproducible, includes at least one failure path, never exposes a secret, and accurately labels simulated evidence.

## Reflection

If the live model call fails, what can you still demonstrate honestly?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
