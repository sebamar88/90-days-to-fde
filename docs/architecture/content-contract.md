# Curriculum content contract

**Contract version:** 1  
**Canonical content:** Markdown files in `curriculum/`  
**Machine-readable metadata schema:** [`schemas/lesson.schema.json`](../../schemas/lesson.schema.json)

This contract makes lessons discoverable and validates metadata without duplicating lesson bodies. It is designed for the current repository validator and future independent consumers, including a static Astro site. A consumer must read the contract version and must not infer quality from a filename or a public GitHub URL.

## Required fields

| Field | Type and rules | Meaning |
|---|---|---|
| `schema_version` | Integer; currently `1` | Frontmatter contract version. |
| `id` | Stable string `day-01` through `day-90` | Permanent cross-link identifier. Do not change when a title or URL slug changes. Future translations reuse this ID. |
| `day` | Integer 1–90 | Position in the learning path. |
| `phase` | Integer 1–6; must equal `ceil(day / 15)` and match the directory | Phase assignment. |
| `locale` | BCP-47-like lower-case language tag with optional upper-case region; current canonical content uses `en` | Language of this entry. The repository remains English-first. |
| `slug` | Lowercase ASCII words separated by single hyphens; unique within a locale | Human-readable URL segment. Slugs are stable once externally linked. |
| `title` | Non-empty string, max 120 characters | Display title. |
| `description` | One-line string, 20–200 characters | Search and metadata summary; must describe the actual lesson. |
| `publication_status` | `draft`, `preview`, `published`, `archived` | Controls site visibility; never means learner mastery. |
| `review_status` | `unreviewed`, `reviewed` | Whether an independent maintainer/editor reviewed the content. |
| `test_coverage` | `none`, `curriculum-structure`, `phase-lab`, `lesson-specific` | Level of automated evidence linked to the lesson; it is coverage metadata, not a live test result. |
| `learner_validation_status` | `not-validated`, `validated` | Whether a real learner review has been conducted and documented. Simulated role-play does not count. |
| `content_type` | One of the lesson types below | Determines which teaching/assessment sections are required. |
| `difficulty` | `foundational`, `intermediate`, `advanced` | Expected task complexity for the target engineer; not a job level or certification. |
| `duration` | Object with integer `min` and `max` minutes; 15–240; `min <= max` | Estimated active learning time. These are planning estimates until learner timing exists. |
| `prerequisites` | Array of unique lesson IDs; no self, future, dangling, or circular references | Direct dependencies needed to complete this lesson. Previous/next navigation is derived from `day`, not duplicated here. |
| `objectives` | 2–5 plain-language strings | Observable capabilities learners should demonstrate. |
| `tags` | 1–4 lower-kebab-case strings | Broad subject filters. |
| `skills` | 1–4 lower-kebab-case strings | Specific capability filters; names should be reused consistently. |

The schema disallows unknown frontmatter properties so a misspelled field fails visibly. Human assessment remains responsible for quality and learner evidence that automation cannot judge.

## Publication and quality semantics

- **Authored:** a file exists with learning content. All current entries are authored.
- **Reviewed:** a human maintainer or qualified peer applied the editorial standard; automated validation is not review.
- **Tested:** the `test_coverage` field names which automated contract is linked. `phase-lab` means the phase suite exercises the reference implementation or phase-level behavior; it does not claim each daily outcome is automated.
- **Published:** only `publication_status: published` is eligible for normal site navigation. It must also have `review_status: reviewed`. Publication does not imply learner validation.
- **Learner-validated:** only `learner_validation_status: validated` means real learners completed a documented feedback/evaluation round. Role-play, author self-review, stars, and page views do not qualify.

Current day pages are marked `preview`: they are visible in the public repository and may be surfaced only as an explicitly unfinished preview. They remain `unreviewed` and `not-validated` until evidence changes. Their `phase-lab` value points to the suite that exists, not a claim of independent educational validation.

## Lesson types and section contracts

These types describe the dominant learning activity. Extra sections are welcome where they improve teaching, but a validator should only enforce the minimum for that type.

| `content_type` | Minimum required sections | Acceptance emphasis |
|---|---|---|
| `concept-lesson` | Why this matters, Outcomes, Explanation, Exercise, Assessment | Teach concepts before checking transfer; include a worked example when the idea is new. |
| `guided-technical-lab` | Scenario, Outcomes, Exercise, Deliverable, Assessment, Automated lab | State prerequisites, setup, checkpoints, expected observable behavior, and failure path. |
| `business-discovery-exercise` | Scenario, Outcomes, Exercise, Deliverable, Assessment | Separate evidence from assumption; protect consent/privacy; score reasoning with a rubric. |
| `architecture-challenge` | Scenario, Outcomes, Exercise, Deliverable, Assessment | Compare credible options, constraints, trade-offs, operational risks, and revisit triggers. |
| `enterprise-simulation` | Scenario, Simulation/roles, Outcomes, Exercise, Deliverable, Assessment | Label all fictional roles/statements; provide role cards, decision prompts, and debrief criteria. |
| `phase-assessment` | Scenario, Outcomes, Deliverable, Assessment rubric | Review cumulative artifacts; state scoring, safety gates, and proceed/revise/stop rule. |
| `capstone-milestone` | Scenario, Outcomes, Exercise, Deliverable, Assessment | Build on prior evidence; define a small acceptance gate and link to needed artifacts. |

The shared minimum headings in the current short pages are retained where useful. The quality standard defines additional required depth for a full reviewed/published lesson and permits type-specific structure.

## Stable IDs, slugs, navigation, and prerequisites

- IDs are allocated by day and do not change with titles, phase wording, or translated slugs.
- A slug is unique within a locale. Before changing a published slug, a consumer must preserve the prior URL through a redirect or alias.
- `day` determines previous/next navigation. Consumers must not create a duplicate navigation graph.
- Prerequisites are direct pedagogical dependencies, not a copy of every earlier day. They must reference an earlier `id`; cycles and dangling references are errors.
- The current migration encodes the 90-day sequence as a linear prerequisite chain where each exercise consumes the prior artifact. Maintainers may shorten a chain only when an exercise is genuinely completable without that artifact and the phase overview still explains the cumulative path.
- Future translations keep `id` and day/phase stable, use their own `locale` and unique `slug`, and may adapt examples without changing technical facts or safety boundaries.

## Validation and schema evolution

Run `npm ci` and `npm run check:curriculum` from the repository root. The validator parses YAML into typed JavaScript values, applies this JSON Schema, then checks relationships that JSON Schema cannot express (phase/day path agreement, uniqueness, earlier prerequisites, cycles, local paths/anchors, and dataset relationships). External URL availability is deliberately not part of routine pull-request validation.

Schema changes follow these rules:

1. Add compatible optional fields or loosen a constraint within version 1 only when old content remains valid and consumers can ignore the addition.
2. For a breaking required-field, type, enum, identifier, or semantic change, increment `schema_version` and update the schema, migration, validator tests, and consumer guide together.
3. Keep the previous reader/migration path available for at least one release cycle if external consumers may pin it.
4. Never silently infer a new publication or validation status from file presence.
5. Keep Markdown bodies canonical; generated indexes or site bundles are disposable build outputs.

## Consumer behavior

Consumers should load a pinned repository commit/tag, validate `schema_version`, build navigation from `day`, filter `publication_status` deliberately, show preview/review/learner status honestly, and display the applicable content license and attribution. The source tree remains the canonical material; do not copy Markdown into a maintained second content repository.
