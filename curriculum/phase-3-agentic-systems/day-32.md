---
day: 32
phase: 3
status: Ready
title: Define tool permissions and contracts
estimated_effort: 75–100 minutes
---

# Day 32 — Define tool permissions and contracts

## Why this matters

A tool description is part of the system's control surface. Vague names, broad inputs, and hidden side effects make a model difficult to constrain or evaluate.

## Scenario

The intake helper needs a site lookup and a sandbox draft action. Meridian's fictional service catalog includes unrelated destructive operations that must not be exposed.

## Outcomes

- Define a narrow contract for each permitted operation.
- Separate read-only lookup from draft creation and production writes.
- Document authorization, data scope, limits, and failure behavior per tool.

## Exercise

Create a tool registry with exactly two entries: `lookup_site(site_code)` and `create_work_order_draft(request_id, approved_fields)`. Specify types, required fields, max lengths, allowed effects, actor scope, timeout, and error codes. Mark the draft tool as sandbox-only and approval-required. Remove any field that is not needed to complete the workflow; record one rejected broad alternative.

## Deliverable

`tool-catalog.md` and machine-readable JSON Schemas for the two tool inputs and outputs.

## Assessment

Pass when schemas reject extra or oversized values, the read tool cannot mutate state, and the draft contract cannot target a production system.

## Reflection

What harmful action becomes possible if a tool receives a generic URL or arbitrary query instead of a narrow identifier?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
