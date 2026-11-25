# Phase 4 — Reliability, Evaluation & Security

**Days:** 46–60

**Status:** Lesson drafts are public preview, unreviewed, and not validated with learners. Exercises use synthetic or locally generated evidence.

## Phase outcome

Produce evidence that the bounded Meridian workflow behaves acceptably across defined cases, degrades safely under dependency failures, emits useful privacy-conscious signals, and resists the threat scenarios in its scope. This phase does not claim a security certification or production readiness.

## Working rules

Keep task quality, operational reliability, and safety as separate dimensions. Define denominators before reporting rates; show small sample sizes; inspect slices; and block release on a safety-critical failure even when an aggregate score looks good. Use a threat model to choose controls, not as proof that unknown threats are absent. Optional model tests must be repeatable, versioned, and free of real personal data.

## Cumulative deliverables

1. Versioned evaluation set, metric definitions, thresholds, and slice-based error report.
2. Regression results for prompt/schema/planner changes and trace examples with redacted data.
3. SLI/SLO proposal, bounded timeout/fallback policy, and a degraded-mode test.
4. Threat model, prompt-injection cases, privacy/retention rules, and dependency review.
5. Authorization test report, incident playbook, and evidence-backed release gate.

## Lessons

46. [Build a task-specific evaluation set](day-46.md) · 47. [Define scoring and acceptance thresholds](day-47.md) · 48. [Analyze errors by slice](day-48.md) · 49. [Test prompt and model changes for regressions](day-49.md) · 50. [Add structured logs and traces](day-50.md) · 51. [Set service-level indicators and objectives](day-51.md) · 52. [Design timeouts, fallback, and degradation](day-52.md) · 53. [Threat-model the workflow](day-53.md) · 54. [Defend against prompt injection and unsafe inputs](day-54.md) · 55. [Minimize and protect sensitive data](day-55.md) · 56. [Review supply chain and dependency risk](day-56.md) · 57. [Test authorization boundaries](day-57.md) · 58. [Practice incident response](day-58.md) · 59. [Run a reliability and security review](day-59.md) · 60. [Phase review: evidence-backed release gate](day-60.md)

## Phase gate

Pass at 14/18 on the Day 60 rubric, with no zero for evaluation validity, unsafe-action controls, privacy, or incident containment. Demonstrate at least one failing evaluation slice, one safe degraded mode, one denied authorization case, and one incident timeline. “No known issues” is not acceptable evidence; list limits and owners.

## Lab and automated tests

Use the [Phase 4 reference lab](../labs/README.md) and [evaluation/security tests](../labs/tests/test_phase4_evaluation_security.py). Tests verify denominators and slices, safety-critical release blocking, and allowlist-based audit redaction.

## References

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) — checked 2026-11-25.
- [OWASP Agentic AI — Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) — checked 2026-11-25.
- [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) — checked 2026-11-25.
