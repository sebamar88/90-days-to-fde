# 90-day curriculum map

## How to use this map

The days are a recommended sequence, not a daily time promise. Each day adds evidence to one running customer engagement. Work with the fictional **Meridian Facilities**: a multi-region facilities operator whose service desk receives maintenance requests through email and a legacy work-order system. The team is exploring whether AI can help classify and route requests while keeping people in control of consequential actions. All records are synthetic.

Do not assume AI is the answer. The learner must validate the workflow and compare a simple rules-based baseline before proposing a model. The capstone is a bounded, auditable request-intake assistant with human approval before work-order creation or routing changes.

**Status:** Days 1–30 are Ready. Days 31–90 are roadmap entries; their details are scope targets, not finished lessons.

## Phase 1 — Foundations & Business Discovery (Days 1–15)

**Outcome:** a customer-backed problem brief, workflow map, success measures, constraints, solution options, architecture context, ADR, thin-slice plan, and playback.

1. From request to business outcome
2. Map the people around the problem
3. See the work as it happens
4. Prepare a discovery interview
5. Run the discovery conversation
6. Separate evidence from assumptions
7. Define outcomes and guardrails
8. Find data, access, and policy constraints
9. Test whether AI belongs in the solution
10. Compare solution options and scope the first release
11. Draw the system context
12. Record a consequential decision
13. Design the smallest useful slice
14. Play the plan back to the customer
15. Phase review: discovery packet and next-step gate

## Phase 2 — Production AI Engineering (Days 16–30)

**Outcome:** a tested request-intake service with a deterministic baseline, provider-neutral model boundary, structured outputs, representative evaluation set, and explicit cost/latency limits.

16. [Set up the service and contract](phase-2-production-ai/day-16.md) · 17. [Build a deterministic baseline](phase-2-production-ai/day-17.md) · 18. [Create a synthetic evaluation set](phase-2-production-ai/day-18.md) · 19. [Define a provider adapter](phase-2-production-ai/day-19.md) · 20. [Return schema-validated suggestions](phase-2-production-ai/day-20.md) · 21. [Abstain when the request is ambiguous](phase-2-production-ai/day-21.md) · 22. [Decide whether retrieval is justified](phase-2-production-ai/day-22.md) · 23. [Ground suggestions in approved knowledge](phase-2-production-ai/day-23.md) · 24. [Integrate with a work-order sandbox](phase-2-production-ai/day-24.md) · 25. [Bound retries and make writes idempotent](phase-2-production-ai/day-25.md) · 26. [Version prompts and schemas](phase-2-production-ai/day-26.md) · 27. [Measure latency and cost](phase-2-production-ai/day-27.md) · 28. [Compare model and rules baselines](phase-2-production-ai/day-28.md) · 29. [Package a repeatable local demo](phase-2-production-ai/day-29.md) · 30. [Phase review: production AI service](phase-2-production-ai/day-30.md)

## Phase 3 — Agentic Systems & Enterprise Integration (Days 31–45)

**Outcome:** a bounded workflow that uses approved tools safely, integrates through explicit contracts, and pauses for people at the right points.

31. Distinguish an agent from a workflow · 32. Define tool permissions and contracts · 33. Add one read-only tool · 34. Validate tool inputs and outputs · 35. Add human approval before writes · 36. Model workflow state and resumability · 37. Integrate identity and authorization · 38. Map enterprise system boundaries · 39. Handle rate limits and partial failure · 40. Design audit events · 41. Prevent duplicate actions · 42. Simulate a stakeholder escalation · 43. Evaluate tool selection and policy adherence · 44. Run a failure-injection exercise · 45. Phase review: bounded integrated workflow

## Phase 4 — Reliability, Evaluation & Security (Days 46–60)

**Outcome:** a credible evaluation report, operational signals, threat model, incident playbook, and tested failure behavior.

46. Build a task-specific evaluation set · 47. Define scoring and acceptance thresholds · 48. Analyze errors by slice · 49. Test prompt and model changes for regressions · 50. Add structured logs and traces · 51. Set service-level indicators and objectives · 52. Design timeouts, fallback, and degradation · 53. Threat-model the workflow · 54. Defend against prompt injection and unsafe inputs · 55. Minimize and protect sensitive data · 56. Review supply chain and dependency risk · 57. Test authorization boundaries · 58. Practice incident response · 59. Run a reliability and security review · 60. Phase review: evidence-backed release gate

## Phase 5 — Enterprise Deployment & Delivery (Days 61–75)

**Outcome:** a staged deployment and support plan, adoption measures, runbooks, training, and a customer-ready handoff.

61. Choose a deployment shape from constraints · 62. Separate configuration and secrets · 63. Prepare environments and repeatable setup · 64. Add a deployment pipeline · 65. Define rollback and release controls · 66. Estimate operating cost and capacity · 67. Write an operations runbook · 68. Set up support ownership and escalation · 69. Plan user training and change adoption · 70. Design feedback and correction loops · 71. Measure workflow impact after launch · 72. Conduct a launch readiness review · 73. Simulate a production incident · 74. Deliver the customer handoff · 75. Phase review: deployment and adoption packet

## Phase 6 — Capstone & Career Readiness (Days 76–90)

**Outcome:** a secure, evaluated, demonstrable capstone and an honest portfolio narrative supported by artifacts.

76. Confirm capstone scope and evidence gaps · 77. Close the highest-risk design gaps · 78. Implement the end-to-end happy path · 79. Add authorization and approval boundaries · 80. Complete evaluation and regression evidence · 81. Complete telemetry, runbooks, and fallback · 82. Deploy or document a reproducible deployment · 83. Test with a simulated customer panel · 84. Improve based on observed friction · 85. Write a concise architecture and trade-off brief · 86. Prepare a live demo with failure paths · 87. Publish a privacy-safe portfolio case study · 88. Practice customer and technical interviews · 89. Build a role-specific evidence map · 90. Retrospective and continued learning plan

## Completion evidence

Completion means producing the artifacts and demonstrating the skills, not simply reaching the last numbered page. Use the assessment rubrics, keep evidence synthetic and shareable, and document gaps honestly. A future maintainer may revise roadmap days as the field changes.
