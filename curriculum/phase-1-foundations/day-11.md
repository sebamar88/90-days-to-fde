---
day: 11
phase: 1
status: Ready
title: Draw the system context
estimated_effort: 75–100 minutes
---

# Day 11 — Draw the system context

## Why this matters

A context diagram reveals actors, trust boundaries, systems, and data movement before implementation choices become expensive.

## Scenario

The proposed slice receives a request, extracts fields, shows a draft to a coordinator, and may later create a work order after approval. The mail and work-order interfaces remain unverified.

## Outcomes

- Draw a system context that distinguishes current systems from proposed components.
- Show data flows and trust boundaries.
- Mark unverified integration assumptions.

## Exercise

Create a Mermaid or hand-drawn context diagram with requester, email intake, proposed assistant, coordinator, identity provider, work-order system, and operations owner. Show read/write directions and label sensitive data flows. Use dashed lines for unconfirmed interfaces; do not imply the assistant has permissions that have not been agreed.

## Deliverable

`system-context.md` with diagram, boundary notes, and five questions for system owners.

## Assessment

Pass if people and systems are distinct, data and authority flows are visible, and unknown interfaces are marked rather than asserted.

## Reflection

Where does data cross an organizational or trust boundary in your diagram?
