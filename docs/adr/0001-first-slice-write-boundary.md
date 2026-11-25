# ADR-0001: Keep the first slice draft-only

- **Status:** Accepted for the learning scenario
- **Date:** 2026-11-25
- **Decision owners:** Curriculum maintainers (fictional customer decision pending)

## Context

The Meridian scenario proposes model-assisted extraction of maintenance requests. Neither production API access nor customer approval policy has been verified. Work-order creation is consequential and may route operational work.

## Decision

The curriculum's first slice produces a reviewable draft from synthetic requests. It does not write to a production work-order system. This is a curriculum safety boundary, not a claim that Meridian approved the design.

## Options considered

- **Production write:** closest to the requested automation, but unjustified without access, policy, authorization, and error-impact evidence.
- **Sandbox write:** potentially useful later, but no sandbox contract is established yet.
- **Draft-only:** test extraction and workflow value with synthetic input and human review; provides less evidence about integration behavior.

## Consequences

The first learning slice stays reversible and testable. It cannot claim end-to-end automation value; a later phase must establish integration contracts and explicit approval before demonstrating writes.

## Revisit when

Customer and system owners confirm the sandbox, data handling, authorization, audit requirements, and approval boundary.
