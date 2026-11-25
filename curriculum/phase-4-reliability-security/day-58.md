---
day: 58
phase: 4
status: Ready
title: Practice incident response
estimated_effort: 90–120 minutes
---

# Day 58 — Practice incident response

## Why this matters

Teams need a rehearsed way to contain unsafe behavior, communicate clearly, preserve evidence, and recover. An incident exercise should reveal missing ownership, not just test alerting.

## Scenario

In a tabletop, a configuration error causes the prototype to attempt drafts for the wrong region. The environment remains synthetic; no real system is connected.

## Outcomes

- Assign incident roles and containment authority.
- Preserve a minimal, privacy-conscious timeline.
- Define customer communication and recovery criteria.

## Exercise

Run a 20-minute tabletop. Inject discovery, uncertain impact, a second alert, and a request for immediate restart. Decide whether to disable the tool, revoke credentials, or keep read-only service available. Record timestamps, evidence, decisions, owner, and communication. Close only after the scope is understood and replay tests pass.

## Deliverable

Incident timeline, containment checklist, and follow-up actions with owners.

## Assessment

Pass when a named role can stop writes, evidence is preserved without copying sensitive payloads, and recovery has explicit authorization and test criteria.

## Reflection

What decision would be hardest to make when the impact is still uncertain?
