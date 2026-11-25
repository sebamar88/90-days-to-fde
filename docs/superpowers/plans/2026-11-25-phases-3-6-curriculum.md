# Phases 3–6 Curriculum Completion Plan

> **Execution:** Native implementation in the current session.

**Goal:** Complete the 90-day curriculum with usable, assessed lessons for Days 31–90.

**Architecture:** Keep one canonical Markdown page per day and one overview per phase. Continue the synthetic Meridian Facilities engagement across tool use, security, operations, deployment, capstone, and career evidence. Extend dependency-free validation to enforce exactly 90 lessons and the existing quality contract.

**Tech Stack:** Markdown, Node.js validation, existing Python 3.12/FastAPI/Pydantic reference starter in Phase 2.

## Global Constraints

- English-first, provider-agnostic, free-first, and runnable without paid APIs.
- All customer data and stakeholder feedback remain explicitly simulated and synthetic.
- No model may perform consequential writes without a validated human approval boundary.
- Keep Phase 2's service as the capstone foundation; avoid introducing a second framework or cloud-specific path.
- Every lesson includes the repository's required metadata and sections, a named artifact, observable assessment criteria, and a transfer reflection.

## Review Focus

- Agent/tool access can cross a boundary or produce unauthorized writes; lessons require least privilege and approval evidence.
- Retry and resume behavior can duplicate work; lessons require stable operation IDs and replay tests.
- Security/evaluation scores can hide severe subgroup failures; lessons require slices and safety-critical gates.
- Deployment health checks can amplify outages; lessons distinguish startup, readiness, and liveness intent.
- Portfolio claims can disclose sensitive data or overstate results; capstone artifacts use synthetic data and bounded claims.

## Tasks

### Task 1: Phase 3 — Agentic Systems & Enterprise Integration

- [x] Add phase overview and Days 31–45 with scoped tools, stateful workflow, approvals, integration failure behavior, and a phase gate.

### Task 2: Phase 4 — Reliability, Evaluation & Security

- [x] Add phase overview and Days 46–60 with evaluation protocol, observability, reliability controls, threat model, and release gate.

### Task 3: Phase 5 — Enterprise Deployment & Delivery

- [x] Add phase overview and Days 61–75 with deployment decision, release controls, operations, adoption, and customer handoff.

### Task 4: Phase 6 — Capstone & Career Readiness

- [x] Add phase overview and Days 76–90 with capstone build/evidence, simulated customer review, portfolio, and career readiness.

### Task 5: Curriculum quality gate

- [x] Update the map with links and accurate status for all 90 lessons.
- [x] Extend the validator to require exactly one lesson per day 1–90 and a phase overview for each phase.
- [x] Verify local links, front matter, lesson sections, roadmap coverage, and the existing Phase 2 assessments.

## Verification record

- `node scripts/validate-curriculum.mjs` → passed: 90 lessons, six phase overviews, roadmap coverage, and local Markdown links.
- `node --check scripts/validate-curriculum.mjs` → passed.
- `git diff --check` → passed.
