---
day: 24
phase: 2
status: Ready
title: Integrate with a work-order sandbox
estimated_effort: 90–120 minutes
---

# Day 24 — Integrate with a work-order sandbox

## Why this matters

Enterprise integration is a contract and authorization problem as much as an HTTP problem. A local sandbox makes request/response behavior testable without implying access to a customer's production system.

## Scenario

Meridian's real API details and permissions remain unverified. The training service may submit a reviewed draft to an in-memory fake only after the learner explicitly invokes the sandbox path.

## Outcomes

- Define a narrow work-order port and fake adapter.
- Keep suggestion creation separate from work-order creation.
- Validate mapping and error behavior at the integration boundary.

## Exercise

Add an in-memory `WorkOrderPort` with a create method and a fake that records calls. Require an explicit human-approved command/object before creating a fake work order. Add tests for missing location, duplicate request IDs, and downstream failure. Do not add production credentials or a real customer endpoint.

## Deliverable

An interface, fake adapter, explicit approval input, and contract tests.

## Assessment

Pass when generating a suggestion cannot trigger a write, the fake rejects invalid drafts, and a write failure is visible and recoverable.

## Reflection

What customer and security-owner decisions would you need before replacing the fake with a real adapter?
