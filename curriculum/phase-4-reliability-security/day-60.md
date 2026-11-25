---
day: 60
phase: 4
status: Ready
title: Phase review — evidence-backed release gate
estimated_effort: 90–120 minutes
---

# Day 60 — Phase review: evidence-backed release gate

## Why this matters

Reliability and security work is a set of bounded claims supported by evidence. A prototype may pass its learning gate and still require customer, legal, or platform approval before any deployment.

## Scenario

Present the synthetic Meridian workflow to a simulated release board. The board asks for quality by slice, a safe fallback, an authorization denial, and an incident response path.

## Outcomes

- Present evaluation and operational evidence with limitations.
- Explain threat coverage, residual risk, and owners.
- Make a proceed, revise, or stop recommendation with conditions.

## Exercise

Assemble Days 46–59. Re-run the frozen evaluation, show one critical failure and its disposition, simulate a provider timeout, demonstrate a denied cross-region action, and walk through the incident timeline. Present sample counts and unresolved real-customer validation. Record the gate decision and conditions; do not convert a simulated review into customer approval.

## Deliverable

Phase 4 release packet: protocol, slice report, run manifest, traces, SLI/SLO proposal, threat model, privacy/dependency reviews, incident playbook, and gate memo.

## Assessment rubric

Score 0 (missing), 1 (partial), or 2 (evidenced): evaluation design; slice analysis; regression control; useful redacted telemetry; service objectives; safe degradation; threat/control traceability; privacy; supply-chain review. Pass at 14/18 with no zero for evaluation validity, write safety, privacy, or incident containment.

## Reflection

What new evidence would change your release recommendation most?
