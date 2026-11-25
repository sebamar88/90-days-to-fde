---
day: 52
phase: 4
status: Ready
title: Design timeouts, fallback, and degradation
estimated_effort: 90–120 minutes
---

# Day 52 — Design timeouts, fallback, and degradation

## Why this matters

Fallbacks preserve service only when they do not quietly weaken safety or misrepresent confidence. A deterministic path can be safer than repeating an unreliable model call.

## Scenario

The model provider times out and the site directory is intermittently unavailable. Coordinators still need to view the original request and continue manual handling.

## Outcomes

- Set end-to-end deadlines and per-dependency budgets.
- Define a degraded mode with explicit user messaging.
- Preserve approval and authorization controls in fallback paths.

## Exercise

Draw the request deadline budget across provider, directory, and sandbox calls. Define behavior for provider timeout, directory outage, and sandbox ambiguity. Implement or describe a safe fallback to draft-only/manual review; prove it cannot create a write or imply a complete classification. Add a test for recovery without duplicate submission.

## Deliverable

Timeout budget table, degraded-mode state chart, and failure tests.

## Assessment

Pass when every call has a timeout, total request time is bounded, fallback is visible to the user, and no dependency failure removes a safety gate.

## Reflection

Which dependency can fail open, and which must always fail closed for this workflow?
