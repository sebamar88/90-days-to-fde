# Pre-web quality gates

**Goal:** Complete the repository content contract, accurate public docs, a reference-quality Day 1 lesson, and secure/reproducible synthetic labs before Astro integration.

**Constraints:** Keep the six-phase/90-day curriculum, Markdown as canonical source, English content, synthetic data, provider-neutral free path. Do not start Astro or commercial platform work. Do not push or merge. Keep human review and learner validation claims evidence-based.

## Sequence and evidence

- [x] Gate 1 — versioned JSON Schema, YAML parser, 90 metadata migrations, dependency graph and link checks, regression suite. Evidence: `npm run check:curriculum`; 14 tests passed; all 90 lessons validated.
- [x] Gate 2 — synchronize README, roadmap, curriculum map, phase overviews, landing, readiness, contributor setup, and assessment-scope statements. Evidence: curriculum validation accepted all local links; claims distinguish authored, reviewed, tested, and learner-validated states.
- [x] Gate 3 — expand Day 1 with role comparison, discovery glossary, weak/strong statements, options and trade-offs, guided and independent work, reusable template/reference, knowledge check, common mistakes, and assessment boundaries. Evidence: lesson validator and link check pass. Independent review and learner validation remain outstanding.
- [x] Gate 4 — reproduce regressions, fix preview mutability/state/replay, fail-open capstone release gate, and free-form audit values; lock shared and Phase 2 dependencies in CI. Evidence: 65 shared lab tests and 11 starter tests pass; both lockfiles pass offline consistency checks.
- [x] Review diff and local validation. `git diff --check` passes. Fresh `uv sync --locked --extra test --offline` could not complete because required wheels are absent from cache and this environment has no network; hosted CI has not run because changes have not been pushed.

## Release decision

**Astro content integration: GO for a separate consumer prototype**, using the versioned contract and explicit publication statuses. **Public curriculum maturity: preview only** until independent technical/editorial review and learner feedback are recorded. **Hosted CI and fresh dependency installation remain unverified** in this environment. Do not claim production readiness or learning outcome validation.
