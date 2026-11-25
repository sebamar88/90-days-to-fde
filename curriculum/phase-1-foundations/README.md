# Phase 1 — Foundations & Business Discovery

**Days:** 1–15
**Status:** Lesson drafts are public preview, unreviewed, and not validated with learners. Meridian is a fictional scenario.

**Scenario:** Meridian Facilities is fictional and wants to explore delay and rework in maintenance request intake. The described email and work-order process is a synthetic exercise prompt, not customer evidence. Leadership has asked about AI, but the actual problem and acceptable automation boundary are not yet established.

## Phase objective

Practice turning an ambiguous request into a measurable, technically bounded opportunity. No production implementation or real customer validation is provided in this phase. Your job is to understand the work, expose uncertainty, and propose the smallest safe next step.

## Cumulative packet

Keep these artifacts together in a `meridian-discovery/` folder in your own learning repo:

1. Problem brief and stakeholder map.
2. Current-state workflow and interview evidence log.
3. Outcome metric and guardrails.
4. Data, policy, and integration constraints.
5. Options comparison, system context, and ADR.
6. Thin-slice acceptance plan and customer playback.

## Days

1. [From request to business outcome](day-01.md) · 2. [Map the people around the problem](day-02.md) · 3. [See the work as it happens](day-03.md) · 4. [Prepare a discovery interview](day-04.md) · 5. [Run the discovery conversation](day-05.md) · 6. [Separate evidence from assumptions](day-06.md) · 7. [Define outcomes and guardrails](day-07.md) · 8. [Find data, access, and policy constraints](day-08.md) · 9. [Test whether AI belongs in the solution](day-09.md) · 10. [Compare solution options and scope the first release](day-10.md) · 11. [Draw the system context](day-11.md) · 12. [Record a consequential decision](day-12.md) · 13. [Design the smallest useful slice](day-13.md) · 14. [Play the plan back to the customer](day-14.md) · 15. [Phase review](day-15.md)

## Phase gate

Proceed when a skeptical stakeholder can recognize the problem statement, proposed measure, constraints, and first-slice boundary, and when your evidence log distinguishes observed facts from assumptions. If the evidence does not support AI, recommend a simpler path and record why.

## Lab and automated tests

Use the [Phase 1 artifact lab](../labs/README.md) and its [discovery-packet tests](../labs/tests/test_phase1_discovery_packet.py). They check packet completeness and evidence labels; they do not automate judgments about interview quality or the strength of a business recommendation.
