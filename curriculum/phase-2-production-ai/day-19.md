---
schema_version: 1
id: day-19
day: 19
phase: 2
locale: en
slug: define-a-provider-adapter
title: Define a provider adapter
description: Provider independence comes from a narrow application-owned contract, not from a universal SDK that hides every difference.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: guided-technical-lab
difficulty: intermediate
duration:
  min: 75
  max: 100
prerequisites:
  - day-18
objectives:
  - Define a typed provider protocol around the task, not a vendor API.
  - Inject the provider into the service.
  - Normalize provider errors without erasing useful failure categories.
tags:
  - phase-2
  - provider-abstraction
skills:
  - provider-abstraction
---

# Day 19 — Define a provider adapter

## Why this matters

Provider independence comes from a narrow application-owned contract, not from a universal SDK that hides every difference. Keep provider details at the edge and make the offline stub useful.

## Scenario

The service needs one operation: propose an intake draft from a request. It must run in CI and learner machines without API credentials.

## Outcomes

- Define a typed provider protocol around the task, not a vendor API.
- Inject the provider into the service.
- Normalize provider errors without erasing useful failure categories.

## Exercise

Implement `IntakeProvider.extract(request) -> IntakeSuggestion`. Keep `RuleBasedProvider` as the default. Add a `FakeProvider` in tests that returns a fixed suggestion and another that raises a timeout. Confirm the FastAPI route uses dependency injection and that provider names/configuration never leak into the response contract.

## Deliverable

An adapter protocol, deterministic implementation, test fake, and a one-page note on which provider capabilities cannot be normalized away.

## Assessment

Pass when app/service tests run with the fake, default behavior needs no credentials, and adapter errors map to explicit service outcomes rather than silent empty drafts.

## Reflection

What provider-specific feature would create enough value to justify adding it to the interface?
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
