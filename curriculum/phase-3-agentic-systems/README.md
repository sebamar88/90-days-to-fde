# Phase 3 — Agentic Systems & Enterprise Integration

**Days:** 31–45

**Status:** Lessons ready; use the Phase 2 service and synthetic fixtures.

## Phase outcome

Turn the draft-only intake service into a bounded, resumable workflow that can consult approved data and request a sandbox action. The learner must be able to explain why a workflow needs model-directed tool selection, constrain each tool, and demonstrate that authorization and approval—not model intent—control writes.

## Scenario and design boundary

Continue the simulated Meridian Facilities engagement. A coordinator may ask for a request summary, consult a read-only site directory, and prepare a work-order draft. The first implementation uses an explicit state machine and deterministic tool-selection fixtures. A model-backed planner is an optional comparison, not a prerequisite. No lesson connects to a real tenant or performs a production write.

Keep the model outside the trust boundary: tool schemas validate inputs, application code checks actor permissions, approval binds to a specific preview, and the adapter receives only the minimum capability it needs. A workflow that is simpler and safer without an agent is a valid outcome.

## Cumulative deliverables

1. Agent-versus-workflow decision and scoped tool catalog.
2. Read-only site lookup with input/output validation.
3. Approval-gated sandbox action, state-transition table, and resume behavior.
4. Identity/authorization matrix, integration map, retry policy, and audit event schema.
5. Tool-policy evaluation set, failure-injection report, and stakeholder escalation record.

## Lessons

31. [Distinguish an agent from a workflow](day-31.md) · 32. [Define tool permissions and contracts](day-32.md) · 33. [Add one read-only tool](day-33.md) · 34. [Validate tool inputs and outputs](day-34.md) · 35. [Add human approval before writes](day-35.md) · 36. [Model workflow state and resumability](day-36.md) · 37. [Integrate identity and authorization](day-37.md) · 38. [Map enterprise system boundaries](day-38.md) · 39. [Handle rate limits and partial failure](day-39.md) · 40. [Design audit events](day-40.md) · 41. [Prevent duplicate actions](day-41.md) · 42. [Simulate a stakeholder escalation](day-42.md) · 43. [Evaluate tool selection and policy adherence](day-43.md) · 44. [Run a failure-injection exercise](day-44.md) · 45. [Phase review: bounded integrated workflow](day-45.md)

## Phase gate

Score each review criterion 0 (missing), 1 (partial), or 2 (evidenced). Pass at 14/18 with no zero for least privilege, approval binding, or duplicate-action safety. Demonstrate a read-only lookup, an approved sandbox draft, a denied unauthorized action, a resumed workflow, and a recoverable downstream failure. Revise before Phase 4 if a model or user can bypass application authorization.

## Lab and automated tests

Use the [Phase 3 reference lab](../labs/README.md) and [workflow tests](../labs/tests/test_phase3_workflow.py). Tests cover tool scope, authorization, approval binding, resumability, duplicate prevention, and retry bounds.

## References

- [OWASP Agentic AI — Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) — checked 2026-11-25.
- [NIST AI Risk Management Framework: Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) — use as a risk-management reference, not a substitute for organizational policy.
