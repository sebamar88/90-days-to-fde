# Phase 6 — Capstone & Career Readiness

**Days:** 76–90

**Status:** Lesson drafts are public preview, unreviewed, and not validated with learners. The capstone remains local and synthetic unless a learner's organization separately authorizes another environment.

## Phase outcome

Assemble a reproducible, bounded Meridian intake assistant and its evidence into a capstone that a technical reviewer and simulated stakeholder can inspect. Demonstrate the normal path, denial paths, and recovery behavior. Then turn the work into an honest portfolio narrative that separates simulated work from customer-validated results.

## Capstone acceptance boundary

The capstone suggests and prepares drafts; it does not create or route real work orders. The learner must show an explicit actor identity, least-privilege tools, preview-bound human approval, idempotent sandbox submission, redacted audit trail, slice-based evaluation, timeout/degraded mode, and rollback/runbook. Provider-backed inference is optional; the deterministic baseline must remain runnable without an API key or network. Do not publish secrets, real customer information, or unapproved stakeholder statements.

## Cumulative deliverables

1. Scope/evidence register, updated ADRs, and end-to-end implementation.
2. Authorization/approval tests, evaluation/regression report, telemetry, and runbook.
3. Reproducible local deployment or a clearly bounded deployment walkthrough.
4. Simulated panel feedback, prioritized revisions, and architecture/trade-off brief.
5. Failure-aware demo, privacy-safe case study, interview stories, evidence map, and learning plan.

## Lessons

76. [Confirm capstone scope and evidence gaps](day-76.md) · 77. [Close the highest-risk design gaps](day-77.md) · 78. [Implement the end-to-end happy path](day-78.md) · 79. [Add authorization and approval boundaries](day-79.md) · 80. [Complete evaluation and regression evidence](day-80.md) · 81. [Complete telemetry, runbooks, and fallback](day-81.md) · 82. [Deploy or document a reproducible deployment](day-82.md) · 83. [Test with a simulated customer panel](day-83.md) · 84. [Improve based on observed friction](day-84.md) · 85. [Write a concise architecture and trade-off brief](day-85.md) · 86. [Prepare a live demo with failure paths](day-86.md) · 87. [Publish a privacy-safe portfolio case study](day-87.md) · 88. [Practice customer and technical interviews](day-88.md) · 89. [Build a role-specific evidence map](day-89.md) · 90. [Retrospective and continued learning plan](day-90.md)

## Final gate

Score each Day 90 criterion 0 (missing), 1 (partial), or 2 (evidenced). Pass at 16/20 with no zero for approval/authorization, evaluation honesty, privacy, or failure-path demonstration. The reviewer may mark “not evidenced” where the work is only simulated. Completion is educational evidence, not a job guarantee, certification, production approval, or proof of customer impact.

## Lab and automated tests

Use the [Phase 6 capstone lab](../labs/README.md) and [end-to-end tests](../labs/tests/test_phase6_capstone.py). They exercise abstention, approval-gated sandbox submission, authorization, idempotent replay, and release blocking when evaluation fails.
