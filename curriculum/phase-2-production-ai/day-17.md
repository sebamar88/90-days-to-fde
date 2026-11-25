---
day: 17
phase: 2
status: Ready
title: Build a deterministic baseline
estimated_effort: 75–100 minutes
---

# Day 17 — Build a deterministic baseline

## Why this matters

A model's output has no useful comparison point until the team measures a simpler approach. Rules can handle known patterns cheaply and predictably, even if they do not cover every phrasing.

## Scenario

Messages mention categories such as HVAC or plumbing and may include a building code. Coordinators still need to review every draft; urgent language must be surfaced without making an autonomous dispatch decision.

## Outcomes

- Implement a small rules-based extractor with explicit limitations.
- Keep unknown values unknown rather than guessing.
- Test representative positives, negatives, and boundary cases.

## Exercise

Complete `baseline.py`. Extract only recognized building codes, map a small documented set of keywords to categories, and mark urgency as `unknown` unless a clear phrase matches. Always set `review_required=True`. Add tests for capitalization, punctuation, missing location, conflicting keywords, and benign uses of words such as “smoke” in unrelated contexts.

## Deliverable

The rules provider, unit tests, and a short list of patterns it cannot safely classify.

## Assessment

Pass when the baseline is deterministic, never invents a location, preserves unsupported cases for review, and passes tests for both matches and non-matches.

## Reflection

Which rule is likely to become brittle as Meridian's vocabulary changes?
