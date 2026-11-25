# 90 Days to FDE

**90 days. Real challenges. Real engineering.**
**Learn. Build. Deploy. Deliver.**

A free-first, open-source learning path for experienced software engineers moving into Forward Deployed Engineering (FDE) and Applied AI Engineering.

> **Curriculum preview:** all 90 lesson files are authored and publicly available. They have not yet completed independent technical/editorial review or real learner validation. Meridian Facilities is a fictional scenario, and the 90-day sequence is not a promise of fixed daily effort, mastery, or employment.

## What an FDE does

A Forward Deployed Engineer works close to customer teams to understand an operational problem, build and integrate software in its real context, and learn whether the delivery improves the intended outcome. The role may include discovery, hands-on engineering, deployment, and adoption. Employers define the role differently; FDE is not a standardized job description.

This curriculum is for experienced engineers comfortable with programming, APIs, Git, and basic testing. It assumes no prior LLM experience and teaches customer discovery, business framing, and delivery practices that software engineers may not have used in their existing roles.

## What you will build

Practice a cumulative fictional engagement with **Meridian Facilities**, a facilities operator exploring maintenance request intake. You will investigate the scenario, compare process/rules/model options, build a draft-only intake service, develop a bounded human-approved workflow, evaluate failures and safety, and prepare an auditable capstone and delivery handoff. All exercise data and stakeholder statements are synthetic; they are not customer research or proof of real-world outcomes.

## Start learning

Begin with [Day 01 — From request to business outcome](curriculum/phase-1-foundations/day-01.md). The [curriculum map](curriculum/README.md) links every day and cumulative phase artifact.

| Phase | Days | Focus | Phase guide |
|---|---:|---|---|
| 1 | 1–15 | Foundations & Business Discovery | [Phase 1](curriculum/phase-1-foundations/README.md) |
| 2 | 16–30 | Production AI Engineering | [Phase 2](curriculum/phase-2-production-ai/README.md) |
| 3 | 31–45 | Agentic Systems & Enterprise Integration | [Phase 3](curriculum/phase-3-agentic-systems/README.md) |
| 4 | 46–60 | Reliability, Evaluation & Security | [Phase 4](curriculum/phase-4-reliability-security/README.md) |
| 5 | 61–75 | Enterprise Deployment & Delivery | [Phase 5](curriculum/phase-5-enterprise-delivery/README.md) |
| 6 | 76–90 | Capstone & Career Readiness | [Phase 6](curriculum/phase-6-capstone-career/README.md) |

The duration metadata currently totals **120.5–162.2 estimated hours** across all 90 lessons (80–108 minutes per lesson on average). These are author estimates, not observed learner time. Phase assessments may require more time than a typical daily lesson.

## How you learn

Each phase builds on prior artifacts through realistic scenarios, architecture trade-offs, technical labs, stakeholder simulations, and assessments. The free core path stays provider-agnostic; local fakes and synthetic fixtures are available without a paid model or cloud account. Human rubrics assess reasoning, communication, and judgment that code tests cannot determine.

## What is implemented and what remains to validate

| Evidence | Current status |
|---|---|
| Lesson files authored | 90/90 |
| Independent technical/editorial review | Not completed across the lesson set |
| Approved for normal published navigation | None; lessons are marked `preview` |
| Real learner validation | None documented |
| Reference implementations | Available for all six phases in `curriculum/labs/` and the Phase 2 starter |
| Automated tests | Validate curriculum structure and reference-lab behavior |
| Individual learner submissions assessed by tests | Not consistently; each lesson links to its phase suite, which is structural linkage, not proof that the individual exercise is automatically graded |
| Code coverage | Not measured or claimed |

Passing a test suite does not mean a lesson has been peer-reviewed, that an individual learner exercise is automatically scored, or that the project is production-ready for customer use. See the [lesson quality standard](docs/quality/lesson-quality-standard.md) and [audit report](docs/audits/repository-audit.md).

## Prerequisites and practical labs

Bring production software engineering experience and a development environment. Labs target Python 3.12; curriculum checks require Node.js 20+. No paid API is required.

For the shared phase labs, run from `curriculum/labs/`:

```sh
uv sync --locked --extra test
uv run --locked pytest tests
```

For the Phase 2 starter, run from `curriculum/phase-2-production-ai/starter/`:

```sh
uv sync --locked --extra test
uv run --locked pytest
```

For content and link validation from the repository root:

```sh
npm ci
npm run check:curriculum
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for review standards, governance, and templates. The [roadmap](ROADMAP.md) and [local backlog](project-management/issues.yml) distinguish authored work from review and learner research still to do.

## Community, licensing, and project status

Contributions are welcome. Read the [Code of Conduct](CODE_OF_CONDUCT.md), [contribution guide](CONTRIBUTING.md), and [security policy](SECURITY.md). Curriculum content is English-first; translations and international contributions are welcome.

Code is licensed under [MIT](LICENSE). Original curriculum and learning materials are licensed under [CC BY-SA 4.0](LICENSE-CONTENT.md). Brand assets and marks are excluded from those licenses; review the licensing documents before reuse.

The present product is the open-source curriculum and reference labs. An interactive learning site, FDE simulator, paid enterprise labs, mentorship, certification, and corporate training remain unbuilt ideas to validate with the community. The static page in [`site/`](site/) is a landing page, not the Astro learning platform.
