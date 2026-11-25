---
day: 41
phase: 3
status: Ready
title: Prevent duplicate actions
estimated_effort: 90–120 minutes
---

# Day 41 — Prevent duplicate actions

## Why this matters

Network timeouts make the caller uncertain whether a write succeeded. Exactly-once behavior is rarely a property of a network call; safe replay needs a durable idempotency contract.

## Scenario

The sandbox may accept a draft and lose the response. A coordinator can also double-click approval or reopen a browser tab.

## Outcomes

- Create a stable idempotency key from the approved operation identity.
- Return the prior result for an identical replay.
- Reject a replay whose payload differs under the same key.

## Exercise

Define a key scoped by tenant, request, action, and approval version. Store the canonical payload hash and result in a fake adapter ledger. Test same key/same payload, same key/changed payload, concurrent duplicate submission, and retry after a simulated lost response. Document retention and reconciliation ownership.

## Deliverable

Idempotency contract, replay ledger fixture, and four deterministic tests.

## Assessment

Pass when the same approved operation creates at most one sandbox record, changed payload is rejected, and a lost response can be reconciled without a second write.

## Reflection

Which key fields would accidentally cause two identical approved actions to be treated as different operations?
