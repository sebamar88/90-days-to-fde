---
day: 53
phase: 4
status: Ready
title: Threat-model the workflow
estimated_effort: 90–120 minutes
---

# Day 53 — Threat-model the workflow

## Why this matters

Security review is most useful when tied to assets, actors, trust boundaries, and credible abuse paths. A list of generic AI risks is not a threat model for this system.

## Scenario

The workflow processes user text, consults a site directory, stores approval state, emits traces, and can create sandbox drafts. Each boundary has a distinct owner.

## Outcomes

- Identify assets, trust boundaries, and attacker-controlled inputs.
- Prioritize threats by impact and plausible path.
- Link each chosen mitigation to a verification artifact.

## Exercise

Use the Day 38 data-flow diagram. For each boundary, write a threat statement in actor/action/asset/impact form. Cover prompt injection, tool misuse, identity confusion, replay, sensitive logging, and dependency compromise. Rank the top five with rationale; assign a control, owner, residual risk, and test to each. Do not claim completeness.

## Deliverable

Threat model and mitigation-to-test traceability table.

## Assessment

Pass when each high-priority threat has a concrete attack path, owner, test, and residual risk, and all trust boundaries match the current diagram.

## Reflection

Which threat is primarily a workflow or identity problem rather than a model problem?

## References

- [OWASP Agentic AI — Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
