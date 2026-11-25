# Repository audit

**Audit date:** 2026-11-25  
**Scope:** Repository contents at `976783e` (`Expand labs across all curriculum phases`), including all 90 lesson files, the Phase 2 Python starter, CI, governance, licenses, project manifests, brand, landing page, and existing validation.  
**Method:** File inventory and Git inspection; full read of Phase 1 lessons; structured review of scenario, outcomes, exercise, deliverable, and assessment sections in Days 16–90; execution of available validation and test commands; primary-source checks linked below.  
**Status:** Findings are verified against this checkout unless explicitly marked as an educational judgment or a setting that could not be inspected.

## Executive assessment

The repository has a coherent six-phase, 90-day sequence, an internally consistent fictional Meridian Facilities scenario, useful safety boundaries, practical learner artifacts, small reference labs for all phases, and separate code/content licenses. The current material is a **public curriculum preview**, not a fully developed or learner-validated course. All lesson files exist and have common scaffolding, but most teach through short prompts rather than explanations, worked examples, or references. “Ready” in front matter currently has no defined editorial meaning.

The strongest qualities are the business-first sequence, explicit simulated-versus-observed distinctions, bounded tool authorization, mandatory human review, and repeated evaluation/security/recovery exercises. The main blockers are the absence of a machine-readable content contract, brittle frontmatter parsing, low teaching depth across the lessons, stale root documentation, and a Python lockfile that CI does not enforce.

No P0 blocker was found for the current static repository. The content contract and validation gaps become a P1 before an external content consumer is built. This audit does not assert real customer validation, learner outcomes, production suitability, or active GitHub security settings.

## Findings

### AUD-001 — Lesson pages are mostly exercise briefs, not standalone teaching units

- **Severity:** P1
- **Classification:** Verified file metrics plus educational judgment.
- **Affected files:** `curriculum/phase-1-foundations/day-01.md` through `day-15.md`; corresponding `day-16.md` through `day-90.md` under Phases 2–6; `templates/lesson.md`; `ROADMAP.md`; `curriculum/README.md`.
- **Evidence:** All 90 pages have the same short sequence of rationale, scenario, outcomes, instructions, artifact, and pass/revise criteria. A whitespace-token count of the lesson bodies ranges from 202 to 283 (mean 230). Only 7/90 lesson files contain external reference URLs. The read-through confirms that many pages ask learners to compare, implement, or explain concepts without first teaching enough of those concepts or showing a worked example. Day 1, for example, is 265 tokens and contains no worked discovery example, role comparison, structured explanation of evidence categories, AI-fit decision method, or reference.
- **Impact:** Learners may need to do substantial unscaffolded research to complete core work; the repository advertises a more complete learning experience than it currently delivers.
- **Recommended remediation:** Use Day 1 as a well-taught reference lesson. Keep the six-phase plan and do not mechanically expand all other pages; review each lesson type and improve content in prioritized batches after the reference is accepted.
- **Acceptance criteria:** Day 1 teaches concepts before assessment, includes a worked example and reusable artifact, has observable scoring, links authoritative sources, and does not overstate Meridian evidence. The remaining 89 lessons have a prioritized, learner-tested improvement backlog rather than a false “complete” label.
- **Dependencies:** Lesson type definitions and revised quality standard (AUD-002).
- **Estimated complexity:** L.

### AUD-002 — No stable, typed content contract exists for the 90 lessons

- **Severity:** P1
- **Classification:** Verified.
- **Affected files:** All `curriculum/phase-*/day-*.md`; `docs/architecture/repository-architecture.md`; `scripts/validate-curriculum.mjs`.
- **Evidence:** Current front matter contains five fields (`day`, `phase`, `status`, `title`, `estimated_effort`). There is no version, stable ID, slug, description, objectives, prerequisites, difficulty, tags, or skill taxonomy. `estimated_effort` is a free-form string. The status values are capitalized editorial labels (`Ready`, `Draft`, `In Progress`) without documented publication semantics. The implementation is Markdown-only and there is no consumer schema.
- **Impact:** Search, navigation, filtering, localization, prerequisites, and future Astro content ingestion must infer metadata from filenames or prose; editorial readiness can be confused with publication or validation.
- **Recommended remediation:** Introduce a versioned JSON Schema and explicit contract documentation; migrate metadata without rewriting lesson bodies. Separate public visibility from editorial review, automated checks, and learner validation.
- **Acceptance criteria:** All 90 records conform; IDs and slugs are unique and stable; enums and prerequisite rules are documented; invalid references and cycles fail validation; status semantics distinguish public publication from quality evidence.
- **Dependencies:** AUD-003 validator.
- **Estimated complexity:** L.

### AUD-003 — Curriculum validation is regex-based and has no test suite

- **Severity:** P1
- **Classification:** Verified.
- **Affected files:** `scripts/validate-curriculum.mjs`; `.github/workflows/validate.yml`; future validator tests.
- **Evidence:** The script extracts YAML with a regular expression and reads only simple one-line `key: value` fields into a `Map`. It does not parse YAML types, lists, quoted multiline values, or schema constraints. It checks day and phase relationships, a set of headings, roadmap entries, JSONL records, and local Markdown destinations, but not prerequisite graphs or internal anchors. No validator-specific tests or malformed-content fixtures exist.
- **Impact:** Valid YAML features can be misread, duplicate keys can be silently overwritten, malformed content can escape the intended contract, and regressions in the validator are not pinned by tests.
- **Recommended remediation:** Use a real YAML parser and JSON Schema validation, retain repository-specific graph and link checks, and test both valid and malformed fixtures. Keep routine CI network-independent.
- **Acceptance criteria:** Tests cover malformed YAML, wrong types/enums, duplicate IDs/slugs/days, phase mismatch, missing/dangling/circular prerequisites, duration bounds, required sections, broken paths/anchors, and invalid JSONL records. CI uses the same deterministic validation command as local contributors.
- **Dependencies:** AUD-002.
- **Estimated complexity:** M.

### AUD-004 — Root README and roadmap contradict current repository state

- **Severity:** P1
- **Classification:** Verified.
- **Affected files:** `README.md`; `ROADMAP.md`; `curriculum/README.md`; `CONTRIBUTING.md`.
- **Evidence:** Root `README.md` describes Phase 2 as “Planned,” lists an old directory structure (`02-production-ai`), retains unchecked boxes for the detailed 90-day roadmap and Phase 2, and estimates 3 hours per day / 270 total hours. Current lessons estimate mostly 60–90 or 75–100 minutes, with longer phase reviews; the exact workload is variable and cannot be summarized as a verified 270 hours. `ROADMAP.md` calls Phase 1 complete and Phases 2–6 ready, while all six phase overviews and 90 daily pages exist but have not undergone a documented peer or learner validation. The current root README is 1,000+ lines and contains substantial historical planning detail.
- **Impact:** New visitors receive stale status, path, and effort information and may mistake authored files for reviewed or validated instruction.
- **Recommended remediation:** Replace the root README with a concise entry page; preserve relevant product detail in existing docs. Align roadmap and curriculum status using explicit authored/reviewed/tested/published/learner-validated distinctions.
- **Acceptance criteria:** README links resolve; phase status and technology reflect current files; effort is described as a range/estimate, not a commitment; no phase or lesson is called validated without evidence; detailed day links remain discoverable.
- **Dependencies:** AUD-002 and AUD-001.
- **Estimated complexity:** M.

### AUD-005 — The Phase 2 CI path does not use its checked-in lockfile

- **Severity:** P1
- **Classification:** Verified.
- **Affected files:** `curriculum/phase-2-production-ai/starter/pyproject.toml`; `curriculum/phase-2-production-ai/starter/uv.lock`; `.github/workflows/phase-2-reference.yml`; `curriculum/phase-2-production-ai/starter/README.md`.
- **Evidence:** `uv.lock` is committed, but both the CI workflow and Quickstart install with `python -m pip install -e ".[test]"`. That command resolves current compatible releases and does not enforce `uv.lock`. The Phase 2 dependency graph therefore is not reproduced by CI or the documented setup.
- **Impact:** Different learners or CI runs may resolve different dependency versions; the lockfile gives a false impression of reproducibility.
- **Recommended remediation:** Use uv and the lockfile consistently in CI and local setup, with a locked-mode check that fails if project metadata and lock diverge.
- **Acceptance criteria:** The same lock-enforced command installs dependencies and runs tests in CI and documented local setup; `uv lock --check` passes; an intentionally stale lock is rejected.
- **Dependencies:** None.
- **Estimated complexity:** S.

### AUD-006 — One API test title overstates what it verifies

- **Severity:** P2
- **Classification:** Verified.
- **Affected files:** `curriculum/phase-2-production-ai/starter/tests/test_api.py`.
- **Evidence:** `test_invalid_request_is_rejected_before_provider_call` uses `FixedProvider`, but does not inspect whether the provider was called. It asserts only that FastAPI returns HTTP 422.
- **Impact:** The test does not prove the ordering implied by its name, so a future refactor could invoke a provider before request validation without detection.
- **Recommended remediation:** Use a spy provider that records calls and assert zero calls for an invalid request.
- **Acceptance criteria:** The test fails if the provider is invoked for an invalid request and passes when validation rejects it first.
- **Dependencies:** None.
- **Estimated complexity:** S.

### AUD-007 — Phase 2 provider failures and dataset independence are under-tested

- **Severity:** P1
- **Classification:** Verified.
- **Affected files:** `curriculum/phase-2-production-ai/starter/tests/`; `curriculum/phase-2-production-ai/starter/src/meridian_intake/`; `curriculum/phase-2-production-ai/starter/data/evaluation.jsonl`; `curriculum/phase-2-production-ai/starter/data/README.md`.
- **Evidence:** The starter contains an eight-record synthetic dataset and the baseline test evaluates every record in that same dataset. There is no separate development and holdout split. API tests cover a successful response, timeout mapping, and invalid request status, but not `ProviderUnavailable`, a provider returning an invalid response object, or the no-provider-call guarantee. The dataset is small and intentionally synthetic; its perfect rule-match result does not establish representativeness or generalization.
- **Impact:** Regression performance is measured on a tiny set that doubles as the development set; some provider/service failure contracts remain unpinned.
- **Recommended remediation:** Add explicit provider contract tests and separate a small development set from an independent synthetic holdout. Document that neither estimates real request prevalence or production performance.
- **Acceptance criteria:** Timeout, unavailable, invalid output, malformed JSON where applicable, and invalid-request call ordering have tests; evaluation reports set identity and denominators; holdout cases are not used to tune rules/prompts.
- **Dependencies:** AUD-005 for repeatable test execution.
- **Estimated complexity:** M.

### AUD-008 — Advanced implementation coverage is advertised more broadly than the reference code provides

- **Severity:** P2
- **Classification:** Verified plus curriculum-design judgment.
- **Affected files:** `curriculum/phase-2-production-ai/README.md`; `curriculum/phase-3-agentic-systems/README.md`; `curriculum/phase-4-reliability-security/README.md`; `curriculum/phase-5-enterprise-delivery/README.md`; `curriculum/phase-6-capstone-career/README.md`; `curriculum/labs/README.md`.
- **Evidence:** Phase 2 has the only HTTP service implementation; Phases 1, 3–6 have small reference modules for artifact validation, workflow state, evaluation/redaction, deployment checks, and capstone composition. There is no Docker/Terraform/AWS deployment, OpenTelemetry exporter, MCP server/client, LangGraph implementation, multi-agent code, vector database, reranker, local model adapter, or TypeScript project. The lesson prompts sometimes ask learners to implement or research those patterns but do not provide a runnable reference for them.
- **Impact:** A reader may mistake one narrow synthetic reference path for implementation coverage of the entire technical curriculum.
- **Recommended remediation:** Document implemented versus conceptual/optional topics explicitly; keep frameworks as optional examples only when they teach a transferable concept. Prioritize hands-on examples from demonstrated learner need.
- **Acceptance criteria:** Phase overviews and landing material distinguish runnable reference labs from design exercises and optional advanced implementations; missing topics have an explicit core/optional decision in the coverage map.
- **Dependencies:** AUD-009 coverage report.
- **Estimated complexity:** M.

### AUD-009 — References and technical source freshness are sparse

- **Severity:** P2
- **Classification:** Verified.
- **Affected files:** All 90 lesson files; `templates/lesson.md`; `docs/quality/standards.md`.
- **Evidence:** Only 7/90 lessons contain an external URL (12 occurrences). Topics with provider, security, evaluation, deployment, protocol, or framework details may change; most pages do not provide source attribution or a checked date.
- **Impact:** Learners cannot consistently verify technical claims or trace vendor-specific details to current primary documentation.
- **Recommended remediation:** Require authoritative references when claims need current verification; keep stable concepts provider-neutral; identify provider/version and date where guidance is provider-specific.
- **Acceptance criteria:** Revised Day 1 citations work and are primary sources; templates distinguish stable concepts from time-sensitive implementation advice; references are not copied prose.
- **Dependencies:** AUD-001.
- **Estimated complexity:** M.

### AUD-010 — GitHub security and dependency automation settings are not fully verifiable here

- **Severity:** P2
- **Classification:** Partly verified; repository settings remain unverified.
- **Affected files:** `.github/workflows/*.yml`; `CODEOWNERS`; `SECURITY.md`; repository settings.
- **Evidence:** Current workflows declare `contents: read`, which is a good least-privilege baseline. They reference actions by major version tags (`@v4`/`@v5`) rather than immutable commit SHAs. `CODEOWNERS` assigns the repository to `@sebamar88`. No `dependabot.yml` or `FUNDING.yml` exists. The authenticated repository metadata does not expose whether private vulnerability reporting is enabled or whether branch protection/required checks are configured. `SECURITY.md` correctly phrases private reporting as conditional, but its fallback private contact route has not been verified in this audit.
- **Impact:** Action tags can move; dependency update automation is absent; contributors cannot infer repository-side protections from checked-in files alone.
- **Recommended remediation:** Decide whether Dependabot and SHA pinning are justified for this low-dependency repository; document branch protection and private reporting settings as maintainer checks. Do not claim sponsorship or private reporting is active without direct evidence.
- **Acceptance criteria:** Maintainer checklist records actual setting state; security instructions link to a working private route or clearly explain its unavailability; workflow permissions remain read-only unless a job needs more.
- **Dependencies:** None.
- **Estimated complexity:** S.

### AUD-011 — Project-management manifests are proposals, not synchronized GitHub state

- **Severity:** P2
- **Classification:** Verified.
- **Affected files:** `project-management/issues.yml`; `project-management/milestones.yml`.
- **Evidence:** Both files state that milestones are drafts and that the GitHub connector cannot create them; issues are a proposed manifest. There is no schema or automated validator for these records, and no evidence that entries have been created remotely.
- **Impact:** Maintainers may confuse the backlog with active GitHub issues/milestones; YAML mistakes may go unnoticed.
- **Recommended remediation:** Keep these as canonical local proposals or explicitly mark/synchronize each entry; validate their shape in CI. Do not create remote issues without authorization.
- **Acceptance criteria:** The manifest has documented status and schema, parses in validation, and does not claim remote synchronization unless verified.
- **Dependencies:** AUD-003.
- **Estimated complexity:** S.

### AUD-012 — The landing page and brand are a useful static preview, not a curriculum website

- **Severity:** P3
- **Classification:** Verified.
- **Affected files:** `site/index.html`; `assets/brand/mark.svg`; `docs/brand/identity.md`; `docs/launch/strategy.md`.
- **Evidence:** The repository includes one static HTML landing page and a simple SVG mark. It links to GitHub curriculum files and has no lesson rendering, search, progress tracking, analytics, or deployed site configuration. Product docs frame an interactive simulator and hosted offerings as future hypotheses.
- **Impact:** No major issue for an open-source, free-first preview; avoid marketing it as an interactive platform or learner-validated product.
- **Recommended remediation:** Preserve the static preview; document the future consumer contract without initializing Astro until discovery justifies it.
- **Acceptance criteria:** Public launch copy describes what exists and links directly to the open curriculum; future platform features remain explicitly future work.
- **Dependencies:** AUD-002.
- **Estimated complexity:** S.

## Verified repository facts

- Public GitHub repository; default branch is `main` (repository metadata checked through the connected GitHub app).
- Six phase directories contain exactly 90 numbered lesson files and six overview files.
- All 90 lessons currently use the status label `Ready`; that label has no documented acceptance meaning.
- The root README exceeds 1,000 lines; it describes older planned structure and effort estimates.
- Existing current checks: `node scripts/validate-curriculum.mjs` passes; shared phase labs and Phase 2 baseline/dataset tests pass as run below.
- No `AGENTS.md`, `dependabot.yml`, `package.json`, or `FUNDING.yml` exists in the inspected repository inventory.
- `LICENSE` is MIT; `LICENSE-CONTENT.md` applies CC BY-SA 4.0 to original educational content; `docs/licensing.md` explains contribution and third-party material policy. Branding is excluded from those open licenses per the policy.
- `CODEOWNERS` lists `@sebamar88`. `SECURITY.md` asks reporters to use private vulnerability reporting if enabled and otherwise request a secure channel; current repository settings were not observable via the available repository metadata.
- Current Actions workflows set contents to read-only. They use version tags for GitHub-maintained actions rather than full commit hashes.
- Project manifests explicitly call proposed milestones drafts; no remote issue or milestone state is asserted.

## Baseline validation

Commands and observed results at the audited revision:

- `node scripts/validate-curriculum.mjs` — passed; 90 day pages, six overviews, roadmap entries, dataset records, and local Markdown destinations accepted by the current validator.
- `& ..\phase-2-production-ai\starter\.venv\Scripts\python.exe -m pytest tests ../phase-2-production-ai/starter/tests/test_baseline.py ../phase-2-production-ai/starter/tests/test_evaluation_dataset.py -q` from `curriculum/labs` — **47 passed**.
- `curriculum/phase-2-production-ai/starter/tests/test_api.py` — not counted in the baseline total here. Its `TestClient` attempts a Windows loopback socket and hangs in this sandbox; earlier direct diagnosis showed the hang in Windows `socket.accept` while creating the AnyIO event-loop self-pipe. The Linux GitHub Actions run is the intended full-platform check.
- `git diff --check` — passed after the audit documents and plan were added.
- From `curriculum/phase-2-production-ai/starter`: `uv lock --check --offline` — passed; the committed lockfile matches the current project metadata. CI and the Quickstart still use pip, so they do not consume that lockfile.

## Primary references checked

Checked 2026-11-25. These inform the audit and Day 1 revision; they are linked rather than copied.

- OpenAI’s current FDE role description describes one employer’s role expectations (not a universal definition): [Forward Deployed Engineer (FDE)](https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/).
- Palantir distinguishes its forward-deployed software engineering role from its product-development software engineering role in its own career material: [Students and early talent](https://www.palantir.com/careers/students-and-early-talent/).
- GOV.UK recommends observing current work, interviewing users, and involving people who deliver/support the service in discovery: [User research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery).
- GOV.UK’s research guidance calls for informed consent before notes/recording and for observation notes to remain distinct from interpretation: [Taking notes and recording sessions](https://www.gov.uk/service-manual/user-research/taking-notes-and-recording-user-research-sessions).
- NIST provides a Generative AI Profile as a risk-management companion, not a universal proof that an AI solution is suitable: [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).
- Astro content collections accept typed schemas and expose IDs/data/body to build-time consumers: [Astro content collections](https://docs.astro.build/en/guides/content-collections/).
- uv documents that `uv.lock` pins exact resolved versions and that `--locked` fails when metadata would change the lock: [uv locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/).
- GitHub Actions security guidance recommends granting `GITHUB_TOKEN` the minimum required permissions: [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use).

## Unresolved risks and maintainer actions

1. No real learner has been shown to complete or assess these materials consistently. Run a consent-based, synthetic-or-no-sensitive-data review after the Day 1 reference is available.
2. The 90-day time commitment cannot be established from current per-lesson estimates. Collect actual learner time-to-complete before promising a schedule.
3. GitHub repository security settings (private vulnerability reporting, branch protection, required checks) need an account-level maintainer check; do not infer them from file contents.
4. The core curriculum is published as files in a public repository, but no site publication workflow or separate educational peer-review evidence exists yet.
5. A sample of eight synthetic requests is useful for deterministic examples only. It is not a representative benchmark or a customer performance claim.

## Remediation update — 2026-11-25

The baseline above describes the repository before this audit's implementation changes. The current working tree addresses several findings:

- Replaced regex frontmatter parsing with typed YAML parsing, a versioned JSON Schema contract, and validator tests for malformed YAML, duplicate keys, invalid metadata, prerequisite graph errors, local paths/anchors, and JSONL shape.
- Migrated all 90 lessons to stable IDs, typed time ranges, objectives, prerequisites, skill tags, content type, and explicit preview/review/learner-validation statuses. Migration is repeatable and preserves lesson bodies.
- Expanded Day 1 into a teaching reference with evidence discipline, worked example, interview prompts, options comparison, rubric, and primary references.
- Rewrote the root README to show actual paths and honest preview status; aligned the roadmap and Phase 1/2 overviews with synthetic scenarios and learner validation boundaries.
- Updated Phase 2 CI/setup to use the pinned `uv.lock`; added tests for provider unavailability, malformed outputs, and invalid requests not invoking providers; separated public development/holdout examples and documented their limits.
- Added lesson quality, content contract, Astro consumer guidance, and brand usage standards.

Still open: second-person editorial review across the 90 lessons; real learner validation; verifying repository-level security settings; running the full HTTP TestClient suite on Linux CI; and implementing the website only after a concrete discovery need. No changes have been pushed.

## Recommended order

1. Introduce the content contract and real parser/validator tests.
2. Set lesson type and quality criteria; produce the Day 1 reference lesson.
3. Improve reproducibility and tests in the Phase 2 starter.
4. Correct README, roadmap, and public status claims.
5. Document independent Astro consumption and project-manifest validation.
6. Gather consent-based external learner feedback before labeling broader lesson sets reviewed or learner-validated.

## Pre-web quality gate confirmation — 2026-11-25

This update tests the six audit concerns in the supplied pre-web quality gate against the working tree. The findings below were reproduced in tests before implementation, then fixed and retested. Local passing tests do not establish that GitHub Actions has run; no changes were pushed.

| Finding | Reproduced behavior | Fix and regression evidence |
|---|---|---|
| Mutable approved preview | Preview fields could be changed through a nested dict; restored snapshots could contain inconsistent preview/state data. | Preview fields are immutable defensive copies, canonical payload hashes are checked at approval/submission/restoration boundaries, malformed states are rejected, and re-creation/cancellation clears approval. See `test_phase3_workflow.py`. |
| Workflow replay/state consistency | A replay could return a previous result without confirming the current request state and approved action. | Replay is bound to request, actor, idempotency key, payload hash, and submitted state; tests cover valid replay and altered state. Snapshots are documented as unsigned in-memory consistency checks, not durable or attacker-authenticated persistence. |
| Release gate fail-open | A blocking operations decision with an empty blocker list could pass the gate. | Evaluation and operations schemas are validated; missing, contradictory, malformed, failed, or blocking evidence fails closed. See `test_phase6_capstone.py`. |
| Free-form audit values | Accepted keys still allowed arbitrary scalar content. | `AuditEvent` uses finite event/state/outcome/reason values and bounded identifier/version/timestamp formats; unknown keys and free-form content raise `ValueError`. See `test_phase4_evaluation_security.py`. This is data minimization, not a detector for every possible secret or identifier. |
| Dependency/CI drift | The shared suite lacked its own committed lock and CI could resolve dependencies independently. | Shared labs now use `uv.lock`, the local Phase 2 starter path dependency, and `uv sync --locked`; workflows use the locked command. Offline lock consistency is checked locally. Fresh installation depends on package-index availability and remote CI has not been observed. |
| Assessment scope ambiguity | Phase-to-suite links could be read as per-exercise automated grading. | README, lab docs, curriculum map, and lesson pages distinguish suite linkage, reference behavior tests, learner-authored assessment, code coverage, and educational validation. |

The content contract validator was also hardened against null metadata and empty/duplicate required sections; the curriculum suite exercises those cases. Day 1 now has an explicit role comparison, glossary, weak/strong problem statements, decision trade-offs, a guided and separate independent exercise, reusable brief, reference solution, knowledge check with explanations, common mistakes, optional challenge, and transparent qualitative/automated assessment boundary. All scenario observations and the five-message example are explicitly synthetic. It remains unreviewed by an independent educator and not learner-validated.

Outstanding external evidence: successful hosted GitHub Actions execution; human editorial/technical review; real learner feedback; repository-level GitHub protections; and a clean locked dependency install where package-index access is available.
