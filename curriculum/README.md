# 90-day curriculum map

## How to use this map

The days are a recommended sequence, not a daily time promise. Each day adds evidence to one running customer engagement. Work with the fictional **Meridian Facilities**: a multi-region facilities operator whose service desk receives maintenance requests through email and a legacy work-order system. The team is exploring whether AI can help classify and route requests while keeping people in control of consequential actions. All records are synthetic.

Do not assume AI is the answer. The learner must validate the workflow and compare a simple rules-based baseline before proposing a model. The capstone is a bounded, auditable request-intake assistant with human approval before work-order creation or routing changes.

**Status:** Days 1–90 have lesson pages and assessments. Learner feedback and demand validation remain ongoing; simulated exercises are not real customer validation.

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

31. [Distinguish an agent from a workflow](phase-3-agentic-systems/day-31.md) · 32. [Define tool permissions and contracts](phase-3-agentic-systems/day-32.md) · 33. [Add one read-only tool](phase-3-agentic-systems/day-33.md) · 34. [Validate tool inputs and outputs](phase-3-agentic-systems/day-34.md) · 35. [Add human approval before writes](phase-3-agentic-systems/day-35.md) · 36. [Model workflow state and resumability](phase-3-agentic-systems/day-36.md) · 37. [Integrate identity and authorization](phase-3-agentic-systems/day-37.md) · 38. [Map enterprise system boundaries](phase-3-agentic-systems/day-38.md) · 39. [Handle rate limits and partial failure](phase-3-agentic-systems/day-39.md) · 40. [Design audit events](phase-3-agentic-systems/day-40.md) · 41. [Prevent duplicate actions](phase-3-agentic-systems/day-41.md) · 42. [Simulate a stakeholder escalation](phase-3-agentic-systems/day-42.md) · 43. [Evaluate tool selection and policy adherence](phase-3-agentic-systems/day-43.md) · 44. [Run a failure-injection exercise](phase-3-agentic-systems/day-44.md) · 45. [Phase review: bounded integrated workflow](phase-3-agentic-systems/day-45.md)

## Phase 4 — Reliability, Evaluation & Security (Days 46–60)

**Outcome:** a credible evaluation report, operational signals, threat model, incident playbook, and tested failure behavior.

46. [Build a task-specific evaluation set](phase-4-reliability-security/day-46.md) · 47. [Define scoring and acceptance thresholds](phase-4-reliability-security/day-47.md) · 48. [Analyze errors by slice](phase-4-reliability-security/day-48.md) · 49. [Test prompt and model changes for regressions](phase-4-reliability-security/day-49.md) · 50. [Add structured logs and traces](phase-4-reliability-security/day-50.md) · 51. [Set service-level indicators and objectives](phase-4-reliability-security/day-51.md) · 52. [Design timeouts, fallback, and degradation](phase-4-reliability-security/day-52.md) · 53. [Threat-model the workflow](phase-4-reliability-security/day-53.md) · 54. [Defend against prompt injection and unsafe inputs](phase-4-reliability-security/day-54.md) · 55. [Minimize and protect sensitive data](phase-4-reliability-security/day-55.md) · 56. [Review supply chain and dependency risk](phase-4-reliability-security/day-56.md) · 57. [Test authorization boundaries](phase-4-reliability-security/day-57.md) · 58. [Practice incident response](phase-4-reliability-security/day-58.md) · 59. [Run a reliability and security review](phase-4-reliability-security/day-59.md) · 60. [Phase review: evidence-backed release gate](phase-4-reliability-security/day-60.md)

## Phase 5 — Enterprise Deployment & Delivery (Days 61–75)

**Outcome:** a staged deployment and support plan, adoption measures, runbooks, training, and a customer-ready handoff.

61. [Choose a deployment shape from constraints](phase-5-enterprise-delivery/day-61.md) · 62. [Separate configuration and secrets](phase-5-enterprise-delivery/day-62.md) · 63. [Prepare environments and repeatable setup](phase-5-enterprise-delivery/day-63.md) · 64. [Add a deployment pipeline](phase-5-enterprise-delivery/day-64.md) · 65. [Define rollback and release controls](phase-5-enterprise-delivery/day-65.md) · 66. [Estimate operating cost and capacity](phase-5-enterprise-delivery/day-66.md) · 67. [Write an operations runbook](phase-5-enterprise-delivery/day-67.md) · 68. [Set up support ownership and escalation](phase-5-enterprise-delivery/day-68.md) · 69. [Plan user training and change adoption](phase-5-enterprise-delivery/day-69.md) · 70. [Design feedback and correction loops](phase-5-enterprise-delivery/day-70.md) · 71. [Measure workflow impact after launch](phase-5-enterprise-delivery/day-71.md) · 72. [Conduct a launch readiness review](phase-5-enterprise-delivery/day-72.md) · 73. [Simulate a production incident](phase-5-enterprise-delivery/day-73.md) · 74. [Deliver the customer handoff](phase-5-enterprise-delivery/day-74.md) · 75. [Phase review: deployment and adoption packet](phase-5-enterprise-delivery/day-75.md)

## Phase 6 — Capstone & Career Readiness (Days 76–90)

**Outcome:** a secure, evaluated, demonstrable capstone and an honest portfolio narrative supported by artifacts.

76. [Confirm capstone scope and evidence gaps](phase-6-capstone-career/day-76.md) · 77. [Close the highest-risk design gaps](phase-6-capstone-career/day-77.md) · 78. [Implement the end-to-end happy path](phase-6-capstone-career/day-78.md) · 79. [Add authorization and approval boundaries](phase-6-capstone-career/day-79.md) · 80. [Complete evaluation and regression evidence](phase-6-capstone-career/day-80.md) · 81. [Complete telemetry, runbooks, and fallback](phase-6-capstone-career/day-81.md) · 82. [Deploy or document a reproducible deployment](phase-6-capstone-career/day-82.md) · 83. [Test with a simulated customer panel](phase-6-capstone-career/day-83.md) · 84. [Improve based on observed friction](phase-6-capstone-career/day-84.md) · 85. [Write a concise architecture and trade-off brief](phase-6-capstone-career/day-85.md) · 86. [Prepare a live demo with failure paths](phase-6-capstone-career/day-86.md) · 87. [Publish a privacy-safe portfolio case study](phase-6-capstone-career/day-87.md) · 88. [Practice customer and technical interviews](phase-6-capstone-career/day-88.md) · 89. [Build a role-specific evidence map](phase-6-capstone-career/day-89.md) · 90. [Retrospective and continued learning plan](phase-6-capstone-career/day-90.md)

## Completion evidence

Completion means producing the artifacts and demonstrating the skills, not simply reaching the last numbered page. Use the assessment rubrics, keep evidence synthetic and shareable, and document gaps honestly. A future maintainer may revise roadmap days as the field changes.
