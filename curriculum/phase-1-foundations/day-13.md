---
day: 13
phase: 1
status: Ready
title: Design the smallest useful slice
estimated_effort: 75–100 minutes
---

# Day 13 — Design the smallest useful slice

## Why this matters

Small slices shorten the path to evidence. The slice still needs a meaningful user task and observable behavior; a toy demo can prove little about operational usefulness.

## Scenario

The candidate slice turns one synthetic request into a suggested work-order draft for a coordinator to review. The customer has not yet agreed to pilot data or access.

## Outcomes

- Define one end-to-end user journey and its boundaries.
- Write acceptance criteria including ambiguous and failure cases.
- Identify dependencies and test data needed.

## Exercise

Specify a slice for synthetic requests only: input, suggested fields, missing-information behavior, confidence/uncertainty presentation, coordinator correction, and output. Add acceptance examples for complete, incomplete, ambiguous, and unsafe-to-route requests. Keep actual work-order creation disabled.

## Deliverable

`thin-slice.md` with a user story, acceptance criteria, exclusions, and test-case table.

## Assessment

Pass if every acceptance criterion is observable, at least two cases cause the system to ask for human input, and no acceptance criterion assumes an unverified customer integration.

## Reflection

What is the smallest test that would show whether the draft saves meaningful effort?
