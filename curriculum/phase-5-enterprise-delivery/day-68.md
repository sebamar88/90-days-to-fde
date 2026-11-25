---
schema_version: 1
id: day-68
day: 68
phase: 5
locale: en
slug: set-up-support-ownership-and-escalation
title: Set up support ownership and escalation
description: Enterprise delivery crosses product, platform, security, and operations teams.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: enterprise-simulation
difficulty: advanced
duration:
  min: 60
  max: 90
prerequisites:
  - day-67
objectives:
  - Assign ownership for service, data, policy, and dependency incidents.
  - Define severity, escalation triggers, and response expectations as proposals.
  - Identify gaps that require customer agreement.
tags:
  - phase-5
  - service-ownership
skills:
  - service-ownership
---

# Day 68 — Set up support ownership and escalation

## Why this matters

Enterprise delivery crosses product, platform, security, and operations teams. Unowned failures become customer problems even when the software behaves as designed.

## Scenario

The simulated Meridian pilot has a business owner, service-desk lead, platform owner, identity owner, and AI application maintainer. Availability and escalation hours are not agreed.

## Outcomes

- Assign ownership for service, data, policy, and dependency incidents.
- Define severity, escalation triggers, and response expectations as proposals.
- Identify gaps that require customer agreement.

## Exercise

Build a RACI-style table for release, policy updates, access reviews, data corrections, incidents, and evaluation changes. Draft escalation routes for safety incident, availability incident, and routine feedback. Mark response-time objectives as proposed until approved. Role-play a handoff where the primary owner is unavailable.

## Deliverable

Support and escalation matrix with named roles, not invented individuals.

## Assessment

Pass when every critical responsibility has one accountable role, backup coverage is explicit, and unagreed service expectations are labeled proposals.

## Reflection

Which ownership gap would make a controlled pilot irresponsible even if the system were technically sound?
## Automated lab

Run the [Phase 5 test suite](../labs/tests/test_phase5_delivery.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
