---
schema_version: 1
id: day-54
day: 54
phase: 4
locale: en
slug: defend-against-prompt-injection-and-unsafe-inputs
title: Defend against prompt injection and unsafe inputs
description: Instructions can arrive inside user text or retrieved content.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: advanced
duration:
  min: 90
  max: 120
prerequisites:
  - day-53
objectives:
  - Treat user and retrieved content as data, not trusted policy.
  - Prevent untrusted text from changing identity, scope, or approval state.
  - Test safe handling of injection-like content and refusal paths.
tags:
  - phase-4
  - prompt-injection-defense
skills:
  - prompt-injection-defense
---

# Day 54 — Defend against prompt injection and unsafe inputs

## Why this matters

Instructions can arrive inside user text or retrieved content. Prompt wording alone cannot enforce a security boundary; trusted application policy and tool permissions must do that.

## Scenario

A synthetic maintenance request says to ignore prior rules, reveal another site's records, and submit a work order immediately. A retrieved note contains similar adversarial text.

## Outcomes

- Treat user and retrieved content as data, not trusted policy.
- Prevent untrusted text from changing identity, scope, or approval state.
- Test safe handling of injection-like content and refusal paths.

## Exercise

Add at least six adversarial fixtures: direct override, quoted instruction, retrieved instruction, cross-site request, secret request, and urgent-language pressure. Run them through the same authorization and approval checks as ordinary input. Assert that none can broaden the tool catalog, change the actor, or create a draft without approval. Record false positives and safe user-facing responses.

## Deliverable

Injection test set, results, and an application-control diagram.

## Assessment

Pass when every attack is blocked at a deterministic boundary, legitimate request content remains reviewable, and no mitigation relies only on prompt text.

## Reflection

Which control still holds if the model completely ignores its system instructions?

## References

- [OWASP Agentic AI — Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
## Automated lab

Run the [Phase 4 test suite](../labs/tests/test_phase4_evaluation_security.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
