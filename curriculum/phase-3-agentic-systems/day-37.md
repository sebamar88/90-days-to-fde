---
day: 37
phase: 3
status: Ready
title: Integrate identity and authorization
estimated_effort: 90–120 minutes
---

# Day 37 — Integrate identity and authorization

## Why this matters

An agent's natural-language claim is not an identity. The application must authorize each action using authenticated actor context and current policy.

## Scenario

The synthetic organization has coordinators, supervisors, and read-only auditors. Only a coordinator assigned to a region can approve its draft; only the sandbox adapter can submit it.

## Outcomes

- Separate authentication, authorization, and model-provided content.
- Apply least privilege to each role and tool.
- Test both allowed and denied access paths.

## Exercise

Create an actor-role-region matrix and a policy function that receives a trusted actor context, action, and resource region. Test coordinator in-region, coordinator out-of-region, auditor approval attempt, missing actor, and forged role in the user message. Ensure the tool never accepts a caller-supplied role field.

## Deliverable

Authorization matrix, policy pseudocode or implementation, and a deny-case test report.

## Assessment

Pass when all five cases match the matrix, denial happens before any external call, and model text cannot alter the trusted actor context.

## Reflection

Where should permission be checked again when a request passes through multiple services?
