---
schema_version: 1
id: day-53
day: 53
phase: 4
locale: en
slug: threat-model-the-workflow
title: Threat-model the workflow
description: Security review is most useful when tied to assets, actors, trust boundaries, and credible abuse paths.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: architecture-challenge
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-52
objectives:
  - Identify assets, trust boundaries, and attacker-controlled inputs.
  - Prioritize threats by impact and plausible path.
  - Link each chosen mitigation to a verification artifact.
tags:
  - phase-4
  - threat-modeling
skills:
  - threat-modeling
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
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
