---
day: 78
phase: 6
status: Ready
title: Implement the end-to-end happy path
estimated_effort: 120–150 minutes
---

# Day 78 — Implement the end-to-end happy path

## Why this matters

A narrow vertical slice proves that contracts, orchestration, and user-visible behavior work together. It also gives later safety and failure tests a concrete path to challenge.

## Scenario

A coordinator submits one synthetic maintenance request. The service validates it, produces a suggestion, performs a read-only site lookup, and displays a reviewable draft.

## Outcomes

- Connect the Phase 2 service to the bounded Phase 3 workflow.
- Keep provider choice behind the existing application boundary.
- Demonstrate a complete draft without production writes.

## Exercise

Implement the normal path from request validation through suggestion, site lookup, preview, and sandbox submission only if the approval fixture is already present. Use the deterministic provider first. Add a single end-to-end test with synthetic fixtures and assert the exact states and returned fields. Record any simplification versus the proposed architecture.

## Deliverable

Runnable capstone slice, one end-to-end test, and updated component/sequence diagrams.

## Assessment

Pass when a clean local run reproduces the expected draft, all inputs are synthetic, no real endpoint is called, and each boundary has an owner in the diagram.

## Reflection

Which interface made this integration easier, and which contract still leaks implementation detail?
## Automated lab

Run the [Phase 6 test suite](../labs/tests/test_phase6_capstone.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
