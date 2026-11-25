---
schema_version: 1
id: day-22
day: 22
phase: 2
locale: en
slug: decide-whether-retrieval-is-justified
title: Decide whether retrieval is justified
description: Retrieval adds ingestion, permissions, freshness, relevance, and evaluation work.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: architecture-challenge
difficulty: intermediate
duration:
  min: 75
  max: 100
prerequisites:
  - day-21
objectives:
  - Identify which fields require external knowledge and which do not.
  - Compare a small approved lookup table with a retrieval system.
  - Define evidence needed before adding a vector database.
tags:
  - phase-2
  - retrieval-selection
skills:
  - retrieval-selection
---

# Day 22 — Decide whether retrieval is justified

## Why this matters

Retrieval adds ingestion, permissions, freshness, relevance, and evaluation work. Add it only when the task needs external knowledge that is not present in the request or a small deterministic reference.

## Scenario

Meridian requests may need a site code lookup or approved category mapping. The current system has no verified manual, corpus, or knowledge owner.

## Outcomes

- Identify which fields require external knowledge and which do not.
- Compare a small approved lookup table with a retrieval system.
- Define evidence needed before adding a vector database.

## Exercise

List the source required for each output field. Compare: no retrieval, a versioned local mapping table, and retrieval over an approved synthetic handbook. Score freshness, access control, explainability, operational cost, and failure behavior. Choose one option for the current slice and write a “do not build yet” condition for vector search.

## Deliverable

An ADR that either adds a minimal knowledge source or explicitly defers retrieval with a revisit trigger.

## Assessment

Pass when retrieval is justified by a named knowledge gap, permissions/freshness are considered, and the chosen approach includes a no-result behavior.

## Reflection

Which evidence would show that retrieval improves the coordinator's outcome rather than just increasing technical complexity?
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
