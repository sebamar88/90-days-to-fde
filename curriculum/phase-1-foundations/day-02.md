---
schema_version: 1
id: day-02
day: 2
phase: 1
locale: en
slug: map-the-people-around-the-problem
title: Map the people around the problem
description: The person funding a project, the person doing the work, and the person accountable for risk may value different outcomes.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: business-discovery-exercise
difficulty: foundational
duration:
  min: 60
  max: 90
prerequisites:
  - day-01
objectives:
  - Identify users, decision makers, operators, and affected parties.
  - Record each role's goals, constraints, and influence without assuming agreement.
  - Plan who to involve in discovery.
tags:
  - phase-1
  - stakeholder-mapping
skills:
  - stakeholder-mapping
---

# Day 2 — Map the people around the problem

## Why this matters

The person funding a project, the person doing the work, and the person accountable for risk may value different outcomes. Missing one can invalidate the design.

## Scenario

Meridian has a VP sponsor, service-desk coordinators, regional technicians, an IT integration owner, and a privacy officer. You have only heard the VP's request.

## Outcomes

- Identify users, decision makers, operators, and affected parties.
- Record each role's goals, constraints, and influence without assuming agreement.
- Plan who to involve in discovery.

## Exercise

Create a stakeholder map with at least five roles. For each, note their decisions, daily work, likely success measure, and one question to validate. Add a simple influence/impact grid. Mark unknowns rather than inventing names or opinions.

## Deliverable

`stakeholders.md` plus a prioritized interview list that includes frontline operators and risk/IT roles.

## Assessment

Pass if the map includes the people who do the intake work and the people who own data/integration risk, and distinguishes role-based hypotheses from confirmed evidence.

## Reflection

Which stakeholder could quietly block adoption even if the sponsor approves the project?
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
