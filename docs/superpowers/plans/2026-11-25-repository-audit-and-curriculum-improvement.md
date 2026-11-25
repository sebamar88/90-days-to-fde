# Repository Audit and Curriculum Improvement Implementation Plan

> **Execution:** Native inline execution in the current task, as directed by the supplied brief. Do not delegate or push/merge without new explicit authorization.

**Goal:** Verify and improve the public curriculum’s engineering quality, teachability, content contract, reproducibility, and integration readiness without introducing the commercial platform.

**Architecture:** Keep Markdown in `curriculum/` canonical. Add a versioned JSON Schema and a small Node validation tool that parses YAML structurally, reports deterministic failures, and has fixture-backed tests. Improve one gold-standard lesson and preserve the six-phase structure; document the remaining 89-lesson quality backlog instead of rewriting it mechanically.

**Tech Stack:** Markdown, Node.js 20, YAML parser, JSON Schema validator, Python 3.12, uv, pytest, GitHub Actions.

**Spec:** User-provided “90 Days to FDE — Repository Audit & Curriculum Improvement” brief in this conversation.

## Global Constraints

- Preserve the six phases and 90-day sequence.
- Keep provider and paid services optional in the core path.
- Keep all learner scenarios synthetic and all action examples draft-only until approved.
- Keep educational content in English and preserve existing lesson paths.
- Do not rewrite all 90 lesson bodies before the Day 1 reference is reviewed.
- Do not implement website, auth, billing, Polar, or paid products.
- Do not create remote issues or push/merge without new explicit authorization.
- Distinguish authored, reviewed, tested, published, and learner-validated claims.

## Review Focus

- Malformed or malicious YAML/frontmatter — validation fails with file and line details, without executing content.
- Duplicate, missing, cross-phase, circular, and dangling prerequisites — validation reports all affected stable IDs.
- Draft or in-progress content — website integration filters it out of published navigation by explicit status semantics.
- Invalid Markdown links/anchors and encoded paths — validator catches in-repository failures without network dependence.
- Provider errors and invalid model output — adapter boundary rejects safely and keeps human review mandatory.

---

## Tasks

## Progress

- [x] Task 1 — audit baseline and competency coverage documented.
- [x] Task 2 — content contract, schema, ADR, and 90 metadata migrations.
- [x] Task 3 — parser/schema validator, fixtures, and 12 tests.
- [x] Task 4 — lesson types, quality standards, and templates.
- [x] Task 5 — Day 1 reference lesson.
- [x] Task 6 — Phase 2 starter contracts, synthetic splits, and locked CI.
- [x] Task 7 — README, roadmap, phase status, and governance guidance synchronized.
- [x] Task 8 — independent Astro integration contract.
- [x] Task 9 — existing local project backlog retained; no remote issues created.
- [x] Task 10 — local Node validation, 42 shared lab tests, 11 Phase 2 starter unit tests, locked uv consistency check, issue-manifest YAML parse, and diff review. `uv sync --locked` could not download the build dependency because sandbox DNS/network access is blocked; the GitHub workflow now performs the locked sync. Tests used the existing local venv, not a fresh lockfile install.

### Task 1: Establish the audit baseline

Inspect all 90 lessons, repository docs, code, tests, CI, licenses, governance, and project manifests. Create the verified audit and competency coverage reports; label hypotheses and subjective judgments. Run the existing tests and validator, then save concise baseline metrics.

### Task 2: Define versioned curriculum metadata

Add `docs/architecture/content-contract.md`, `schemas/lesson.schema.json`, and an ADR. Migrate all 90 frontmatter records with deterministic stable IDs, slugs, objective lists, tags, skills, difficulty, duration bounds, and prerequisites. Preserve existing paths and lesson bodies.

### Task 3: Replace brittle curriculum validation

Add the YAML parser and JSON Schema validator as explicit dev dependencies. Split validation into testable modules; validate metadata, IDs/slugs, day-phase assignments, prerequisite references/cycles, headings, local links/anchors, and dataset records. Add malformed and edge-case fixtures and tests. Keep external URL checks out of required PR validation.

### Task 4: Set teaching quality criteria

Define lesson types and acceptance criteria in `docs/quality/lesson-quality-standard.md`; improve lesson, exercise, and assessment templates with required teaching/context/evidence elements while allowing type-specific variation.

### Task 5: Publish the Day 1 reference lesson

Rewrite `curriculum/phase-1-foundations/day-01.md` as an independently useful lesson with role distinctions, business problem framing, evidence categories, AI-fit decision, worked example, guided/independent exercises, artifact, measurable rubric, common mistakes, reflection, and verified primary references. Do not disclose a full solution in the learner-facing exercise.

### Task 6: Harden the Phase 2 Python starter

Verify lockfile/CI mismatch. Add uv-based locked setup and CI, explicit provider spies/contracts, failure and malformed-output tests, safe parsing boundaries, and better-separated development/holdout synthetic fixtures. Document the small synthetic baseline’s limits.

### Task 7: Synchronize product and governance documentation

Update `README.md`, `ROADMAP.md`, phase/curriculum overviews, contribution/local validation guidance, and repository status language. Confirm separate code/content/brand terms and document any GitHub settings requiring manual maintainer action. Do not create issues.

### Task 8: Specify independent website consumption

Create `docs/architecture/astro-integration.md` covering schema/version discovery, publication filtering, IDs/URLs/assets/links/licenses, synchronization options, and a reproducible recommendation for an independent Astro repository. Do not initialize Astro.

### Task 9: Prioritize remaining delivery and learner validation

Update existing `project-management/issues.yml` and milestone manifest with audit-driven review work, prerequisite links, acceptance criteria, and phased improvements. Do not create remote issues.

### Task 10: Full verification and review

Run validator tests, all curriculum tests, Python starter tests, and the curriculum validator. Review the complete diff, report all unresolved issues, and state technical, educational, website, and commercial readiness separately. Do not push or merge.
