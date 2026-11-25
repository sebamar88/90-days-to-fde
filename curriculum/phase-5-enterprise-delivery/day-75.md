---
day: 75
phase: 5
status: Ready
title: Phase review — deployment and adoption packet
estimated_effort: 90–120 minutes
---

# Day 75 — Phase review: deployment and adoption packet

## Why this matters

Successful delivery is measured by reproducibility, safe operation, and user value—not by whether a service was pushed to a cloud account.

## Scenario

Present the Meridian deployment recommendation to a simulated sponsor and receiving engineering team. They must decide whether the evidence is enough to request a real customer pilot review.

## Outcomes

- Demonstrate environment setup, release controls, and rollback.
- Explain operating cost, ownership, training, and measurement limits.
- Hand off risks and open customer approvals accurately.

## Exercise

Assemble Days 61–74. Reproduce the local service from a clean setup, walk through a release stop/rollback rehearsal, runbook response, user training sample, and impact-measurement plan. Have the receiving engineer locate an owner for one simulated incident. End with a proceed-to-customer-review, revise, or stop recommendation.

## Deliverable

Deployment and adoption packet with ADR, config inventory, pipeline, rollback, cost/capacity, runbook, support map, training, measurement plan, incident rehearsal, and handoff.

## Assessment rubric

Score 0 (missing), 1 (partial), or 2 (evidenced): deployment fit; secret/config handling; reproducible setup; CI/release controls; rollback; cost/capacity assumptions; runbook; support ownership; user adoption; impact measurement. Pass at 14/20 with no zero for secrets, rollback, support ownership, or impact guardrails.

## Reflection

What customer-owned decision must happen before your provisional deployment plan becomes a real plan?
