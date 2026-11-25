# Contributing

Thanks for helping build a practical, open learning path. Start with a focused issue or pull request; curriculum corrections, clearer examples, accessibility improvements, and tested exercises are especially useful.

## Before you contribute

- Read the [product vision](docs/product/vision.md), [lesson quality standard](docs/quality/lesson-quality-standard.md), and [licensing policy](docs/licensing.md).
- Search existing issues and lessons so work complements rather than duplicates them.
- For a substantial curriculum change, open an issue describing the learner problem and evidence before drafting a large rewrite.

## Contribution expectations

- Address experienced engineers; avoid introductory filler and unexplained jargon.
- Tie advice to a user, workflow, constraint, observable outcome, or technical trade-off.
- Label assumptions and simulation details. Never fabricate customer validation or performance results.
- Keep model/cloud vendors optional. Label provider-specific examples and include a provider-neutral concept.
- Use synthetic data and safe examples. Never add secrets or real personal/customer data.
- Attribute third-party material and confirm its license; links are preferred to copied content.
- Follow the relevant file in `templates/` and keep changes focused.

## Local checks

Run `npm ci` and `npm run check:curriculum` from the repository root. For Phase 2 changes, run `uv sync --locked --extra test` and `uv run --locked pytest` from `curriculum/phase-2-production-ai/starter/`. For shared labs, run `uv sync --locked --extra test` and `uv run --locked pytest tests` from `curriculum/labs/`. These commands use the committed lockfiles; neither suite needs paid services. For lesson changes, use `docs/quality/lesson-quality-standard.md` and the matching file in `templates/`.

## Pull requests

Explain the learner problem, the change, and how you checked it. Link the related issue when available. Curriculum PRs should state whether outcomes, prerequisites, assessment, accessibility, or licensing changed. Maintainers may request revisions or decline work that conflicts with the product principles.

Contributions are offered under the terms in [Licensing](docs/licensing.md). Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
