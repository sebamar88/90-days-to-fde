# Phase 5 — Enterprise Deployment & Delivery

**Days:** 61–75

**Status:** Lesson drafts are public preview, unreviewed, and not validated with learners. Deployment remains local or simulated.

## Phase outcome

Prepare the Meridian workflow for a controlled, supportable pilot by making a deployment choice that fits stated constraints, separating environment configuration, rehearsing release and rollback, and preparing operators and users. The curriculum does not provision a cloud account or assert customer authorization.

## Delivery boundary

Start with the smallest operational shape that meets the evidence-backed use case. A local container or documented managed runtime is enough for the exercise; Kubernetes is an optional comparison, not a default. Do not use real customer data or credentials. A deployment plan must identify ownership, observability, support, and a rollback trigger before a release is considered.

## Cumulative deliverables

1. Deployment decision record and environment/configuration inventory.
2. Repeatable setup and least-privilege CI/release pipeline proposal.
3. Release, rollback, cost/capacity, and operational runbooks.
4. Support/escalation model, user training, feedback loop, and impact-measurement plan.
5. Launch-readiness review, incident simulation, and customer handoff packet.

## Lessons

61. [Choose a deployment shape from constraints](day-61.md) · 62. [Separate configuration and secrets](day-62.md) · 63. [Prepare environments and repeatable setup](day-63.md) · 64. [Add a deployment pipeline](day-64.md) · 65. [Define rollback and release controls](day-65.md) · 66. [Estimate operating cost and capacity](day-66.md) · 67. [Write an operations runbook](day-67.md) · 68. [Set up support ownership and escalation](day-68.md) · 69. [Plan user training and change adoption](day-69.md) · 70. [Design feedback and correction loops](day-70.md) · 71. [Measure workflow impact after launch](day-71.md) · 72. [Conduct a launch readiness review](day-72.md) · 73. [Simulate a production incident](day-73.md) · 74. [Deliver the customer handoff](day-74.md) · 75. [Phase review: deployment and adoption packet](day-75.md)

## Phase gate

Score each criterion 0 (missing), 1 (partial), or 2 (evidenced). Pass at 14/20 with no zero for secret handling, rollback, support ownership, or user-impact measurement. Demonstrate a reproducible environment, a release/rollback rehearsal, an operator runbook, and a user-facing explanation. All launch decisions remain hypothetical until real customer owners approve them.

## Lab and automated tests

Use the [Phase 5 delivery lab](../labs/README.md) and [deployment/release tests](../labs/tests/test_phase5_delivery.py). Tests check secret-source rules, hosted-deployment evidence, safety release blocks, and cost arithmetic.

## References

- [GitHub Actions security](https://docs.github.com/en/actions/how-tos/secure-your-work) — checked 2026-11-25.
- [Kubernetes probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/) and [Deployment updates](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — checked 2026-11-25; Kubernetes is an optional path.
