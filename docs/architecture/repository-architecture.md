# Repository architecture

## Content model

The canonical source is plain Markdown in `curriculum/`, one page per day and a short overview per phase. A day is an independently linkable learning unit with outcomes, scenario, exercise, deliverable, rubric, and references. Phase roadmaps list the cumulative artifacts and dependencies. Templates live separately so improvements can be applied without duplicating policy text.

## Directories

| Path | Responsibility |
|---|---|
| `curriculum/phase-N-*/` | Phase overview and lesson pages linked to phase tests |
| `curriculum/labs/` | Cumulative reference labs, synthetic fixtures, and cross-phase tests |
| `templates/` | Lesson, exercise, assessment, ADR authoring formats |
| `docs/product/` | Vision and audience |
| `docs/architecture/` | Repository and system design conventions |
| `docs/quality/` | Editorial and technical acceptance standards |
| `docs/brand/`, `docs/launch/` | Identity and audience validation plan |
| `scripts/` | YAML parsing, JSON Schema curriculum checks, and metadata migration |
| `.github/` | Issue/PR forms and CI |
| `project-management/` | Human-readable milestone and issue manifests |
| `site/` | Static public landing page |
| `assets/brand/` | Source artwork and logo exports |

## Extension rules

- Add code examples only when they teach a concept better than pseudocode; keep concepts language-neutral where practical.
- Keep provider-specific material optional and label provider, date checked, and equivalent concept.
- Avoid committing generated course copies or duplicated lesson sources.
- Introduce a site generator or application only when search, localization, accessibility, or learner feedback shows a concrete need.
- Store no learner analytics or personal data in the repository.
