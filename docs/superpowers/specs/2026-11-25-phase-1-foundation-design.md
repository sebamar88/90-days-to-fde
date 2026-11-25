# Phase 1 Foundation Design

## Intent

Build a credible, useful, international open-source learning path for experienced software engineers moving into Forward Deployed Engineering (FDE) and Applied AI Engineering. The repo should help learners demonstrate production judgment by building realistic systems, while giving contributors a clear way to improve the curriculum.

## Goals

- Publish the complete 90-day sequence across six phases and make the first 15 days usable end to end.
- Make lessons build on one another through artifacts, customer context, exercises, and objective assessments.
- Establish repository conventions, templates, licensing, contribution rules, quality checks, launch positioning, and a coherent visual identity.
- Keep the initial learner experience free, provider-agnostic, and usable with local models where practical.
- Make course assumptions and technical claims traceable to primary sources.

## Non-goals

- A hosted course platform, paid labs, certification, simulator, or AI mentor.
- Prescribing one cloud, model provider, framework, or programming language for all learners.
- Promising job placement or claiming that 90 days guarantees a role.
- Building a complex site or custom curriculum application before demand is validated.

## Constraints and product calls

- Audience: experienced engineers with production software experience; this is not an introductory programming course.
- English is the canonical language. Translations can follow without blocking English revisions.
- A day is a guided learning unit, not a guarantee of a fixed number of hours. Learners should be able to adapt pacing.
- Every day should create evidence: a decision, artifact, implementation, test, or reflection that feeds a cumulative capstone.
- Use neutral fictional customers and synthetic data. Do not embed real customer data, secrets, or unlicensed material.
- Keep the repo Markdown-first; add code only when a lesson needs a runnable artifact. Avoid a runtime or framework until learner workflows demonstrate the need.
- Licensing: MIT for original code and CC BY-SA 4.0 for original curriculum prose, with third-party content explicitly attributed and separately licensed. Review before accepting contributions that conflict with these terms.
- Brand direction: pragmatic field engineering; a route/compass motif combined with a terminal cursor; deep navy, warm white, and electric teal; clear typography and high contrast. Use a text-first mark until a distinctive, reusable vector is ready.

## Approaches considered

1. **Documentation-first curriculum repo (selected):** Markdown lessons, local scripts for validation, GitHub-native collaboration. Fast to read, fork, translate, and contribute; limited interactivity is acceptable while demand is unknown.
2. **Custom web learning platform:** richer progress and assessments, but creates product and maintenance work before the curriculum is validated.
3. **Framework-backed course site:** improves navigation/search, but binds content and workflow to a platform prematurely.

The documentation-first approach best fits the free-first and community-driven goals, supports early release, and preserves a later path to interactive products without making the free curriculum dependent on them.

## Curriculum architecture

The six phases move from business discovery to a deployed capstone and career evidence. Each day states a purpose, scenario, learning outcomes, build/exercise, deliverable, assessment rubric, and sources where claims need support. Phase artifacts accumulate in a fictional customer engagement dossier and implementation repository. Assessments evaluate observable behavior; they do not require a paid model API. An optional provider adapter may be used in later lessons, with a local/offline path where feasible.

## Repository structure

`curriculum/` holds phase overviews and day-by-day lessons; `templates/` holds reusable lesson, exercise, assessment, and ADR formats; `docs/` holds product, architecture, quality, launch, and curriculum policy; `scripts/` holds dependency-free validation; `.github/` holds contribution workflows and issue forms; `assets/` holds brand files. Keep one source of truth for each policy and link to it elsewhere.

## Quality and release bar

- Curriculum sequence covers all 90 days, with explicit outcomes and a cumulative capstone.
- Published lessons have complete metadata, clear learner instructions, deliverables, and assessable rubrics.
- Links and external claims are reviewed; source licenses and attribution are recorded.
- Repository checks run locally and in GitHub Actions without secrets or paid services.
- Contributions use reviewable changes and preserve accessibility, provider neutrality, and security.
- Initial release is a public curriculum preview, not a claim of proven employment outcomes. Validate demand through learner interviews, repository engagement, and completion feedback.

## Open decisions for maintainers

- Which capstone customer domain best attracts the intended first cohort.
- Whether one primary implementation language should be recommended while keeping the concepts language-neutral.
- Launch date and any distribution channels beyond GitHub and a static landing page.

## Sources

- CC BY-SA 4.0 terms: https://creativecommons.org/licenses/by-sa/4.0/
- GitHub issue forms: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository
- GitHub contribution guidelines: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors
