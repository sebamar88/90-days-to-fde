---
schema_version: 1
id: day-35
day: 35
phase: 3
locale: en
slug: add-human-approval-before-writes
title: Add human approval before writes
description: Human review is meaningful only when the person sees the exact action, understands its impact, and approves the exact version that will execute.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: intermediate
duration:
  min: 90
  max: 120
prerequisites:
  - day-34
objectives:
  - Bind an approval to an immutable preview and actor.
  - Invalidate approval when reviewed fields change or the request expires.
  - Keep the model unable to approve on a person's behalf.
tags:
  - phase-3
  - human-approval
skills:
  - human-approval
---

# Day 35 — Add human approval before writes

## Why this matters

Human review is meaningful only when the person sees the exact action, understands its impact, and approves the exact version that will execute.

## Scenario

Meridian's coordinator may approve a sandbox work-order draft after checking summary, site, category, and urgency. A model suggestion alone is never approval.

## Outcomes

- Bind an approval to an immutable preview and actor.
- Invalidate approval when reviewed fields change or the request expires.
- Keep the model unable to approve on a person's behalf.

## Exercise

Define a preview containing request ID, normalized fields, target environment, and a content hash. Implement `pending → approved → submitted` transitions. Test approve-then-edit, wrong actor, expired preview, and replayed approval. Show the user a meaningful confirmation summary before the approval action.

## Deliverable

Approval sequence diagram, transition tests, and a sample synthetic approval record.

## Assessment

Pass when only an authorized human can approve, the approval references the exact preview hash and sandbox, and any material edit requires new approval.

## Reflection

Which field change should invalidate approval even if the screen still looks almost the same?
## Automated lab

Run the [Phase 3 test suite](../labs/tests/test_phase3_workflow.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
