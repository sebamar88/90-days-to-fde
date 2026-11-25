# Phase 1 Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the empty repository into a launch-ready, quality-checked open curriculum with the first 15 complete lessons.

**Architecture:** Markdown-first content with one canonical page per lesson, policy and strategy documents under `docs/`, reusable templates, and dependency-free validation invoked locally and in GitHub Actions. GitHub issue and milestone definitions are prepared as importable files; no hosted platform or paid service is required.

**Tech Stack:** Markdown, YAML front matter, Node.js 20 standard library for validation, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-11-25-phase-1-foundation-design.md`

## Global Constraints

- Audience is experienced software engineers; do not teach introductory programming.
- The canonical curriculum is English-first, free-first, provider-agnostic, and production-first.
- Do not implement premium products or require paid model APIs.
- Original code is MIT; original curriculum prose is CC BY-SA 4.0, subject to attribution and third-party license review.
- Keep setup minimal and validation secret-free.
- Learner artifacts should accumulate toward a realistic capstone.

## Review Focus

- Missing or duplicated day numbers: validator checks exactly one lesson for days 1–15 and a complete 1–90 roadmap.
- Incomplete lesson metadata or assessment: validator checks required fields and rubric presence.
- Broken local links or malformed front matter: validation checks document links and expected metadata shape.
- Unlicensed third-party material: contribution/license guidance requires attribution and source/license records.
- Non-provider-neutral curriculum or unsafe learner practices: lesson review checklist checks local/offline path where applicable and security/privacy guidance.

---

### Task 1: Product and repository foundations

**Files:** `README.md`, `docs/product/vision.md`, `docs/product/audience.md`, `docs/architecture/repository-architecture.md`

- [x] Publish a README that explains audience, outcomes, learning format, phases, contribution entry points, and honest limits.
- [x] Record the vision, target learner, exclusions, and validation hypotheses.
- [x] Document repository conventions and future extension points without implementing them.

### Task 2: Curriculum map and first 15 lessons

**Files:** `curriculum/README.md`, `curriculum/phase-*/README.md`, `curriculum/phase-*/day-*.md`

- [x] Map all 90 days across six phases with cumulative deliverables.
- [x] Write complete days 1–15 using one consistent lesson contract and fictional customer context.
- [x] Review progression, workload assumptions, and objective assessments.

### Task 3: Governance, templates, and quality bar

**Files:** `LICENSE`, `LICENSE-CONTENT.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `templates/*`, `docs/quality/standards.md`, `docs/licensing.md`

- [x] Add separate code/content license notices and third-party attribution policy.
- [x] Add lesson, exercise, assessment, and ADR templates.
- [x] Define accessibility, security, accuracy, and review standards.

### Task 4: Automated validation and GitHub collaboration

**Files:** `scripts/validate_curriculum.py`, `.github/workflows/validate.yml`, `.github/ISSUE_TEMPLATE/*`, `.github/PULL_REQUEST_TEMPLATE.md`, `project-management/*`

- [x] Validate curriculum numbering, front matter, required lesson sections, and local links.
- [x] Add GitHub Actions workflow and issue/PR templates.
- [x] Prepare milestone manifest and draft backlog issues for import/creation.
- [x] Run the validator against the authored curriculum and fix all failures.

### Task 5: Brand, landing page, and launch plan

**Files:** `docs/brand/identity.md`, `assets/brand/*`, `site/index.html`, `docs/launch/strategy.md`

- [x] Specify brand voice, mark, palette, and accessible usage.
- [x] Build a simple responsive static landing page aligned with the README.
- [x] Define a launch sequence and low-cost audience/demand validation measures.

### Task 6: Review and handoff

- [x] Inspect git diff and run all available checks.
- [x] Ensure no credentials, personal data, or uncredited third-party content entered the repo.
- [x] Report completed assets, validation results, and remaining launch actions.

## Implementation ruling

Ruling: Use Node.js 20 instead of Python for the dependency-free validator — the workspace has a usable Node runtime while Python resolves to a blocked Store stub, and GitHub Actions supports Node directly — cost if wrong: contributors without Node need to install it before running checks.
