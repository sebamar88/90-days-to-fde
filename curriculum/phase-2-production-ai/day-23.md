---
day: 23
phase: 2
status: Ready
title: Ground suggestions in approved knowledge
estimated_effort: 75–100 minutes
---

# Day 23 — Ground suggestions in approved knowledge

## Why this matters

When a response depends on a policy or reference source, the user needs to see what source supported it. A generated citation is not proof; the application must attach provenance from retrieved material.

## Scenario

If Day 22 selected a synthetic category guide, a suggested category may cite that guide. If you deferred retrieval, keep the field marked as not knowledge-backed rather than inventing a citation.

## Outcomes

- Attach source IDs and snippets from retrieved records, not model-authored URLs.
- Separate direct extraction from reference-backed inference.
- Return a clear no-evidence result.

## Exercise

Create two or three synthetic policy entries with stable IDs and version dates. Implement a trivial exact lookup or small keyword matcher only if justified. The adapter may use selected snippets as context, but the response must include source IDs supplied by the application. Test stale, missing, and conflicting entries.

## Deliverable

A small approved knowledge fixture or a documented deferral, plus provenance and no-result tests.

## Assessment

Pass when citations resolve to stored fixture IDs, unsupported suggestions are labeled, and a model cannot fabricate a valid-looking source ID.

## Reflection

What does provenance let a coordinator verify that a plausible paragraph alone cannot?
