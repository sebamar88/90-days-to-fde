# Lesson quality standard

This standard defines what “ready” means for an educational lesson. Passing the curriculum validator proves structure and metadata only; it does not make a lesson reviewed, pedagogically sound, or learner-validated.

## Required for every lesson

- A specific learner and observable outcome, expressed with an action verb.
- A realistic scenario with facts, assumptions, and fictional details clearly distinguished.
- Enough explanation to teach the core idea; the exercise prompt must not substitute for teaching.
- A worked example or annotated reference artifact when the skill is new.
- A guided exercise with setup, steps, checkpoints, expected evidence, and a recovery path.
- A deliverable that can be inspected by a peer or assessed automatically.
- Assessment criteria with a pass/revise threshold and safety gate where relevant.
- A debrief asking what evidence would change the learner's decision.
- Prerequisites, estimated effort, necessary tools, accessibility considerations, and primary sources.
- Accurate metadata: `preview` until editorial review is complete; learner validation requires documented learner evidence.

## Type-specific expectations

Use the `content_type` contract to select required sections. The section list is a minimum, not a word-count target.

- **Concept:** define terms, explain why they matter, show a worked example, then ask the learner to transfer the idea.
- **Technical lab:** list setup/runtime assumptions; provide runnable checkpoints, expected outputs, negative cases, cleanup, and troubleshooting.
- **Discovery:** distinguish evidence, assumptions, and requirements; model neutral questions and consent; use a transparent rubric.
- **Architecture:** compare credible options against stated constraints; capture reversibility, operations, security, cost, and revisit triggers in an ADR.
- **Simulation:** label roles and statements as fictional; provide role cards, timebox, observer notes, decisions, and debrief.
- **Assessment:** use cumulative artifacts and explicit scoring; state proceed/revise/stop criteria and safety gates.
- **Capstone:** define audience, data boundary, acceptance criteria, operational ownership, and a demonstration backed by evidence.

Do not force every content type to use identical headings. Technical labs need runnable setup and recovery; discovery lessons need evidence provenance and neutral prompts; architecture challenges need comparable options and an ADR; simulations need role boundaries and debriefs; assessments need explicit scoring and a decision gate; capstone milestones need traceable evidence and an operational boundary. Knowledge checks, common mistakes, optional extensions, and reference solutions are useful where they help a learner act independently, but are not mandatory in every lesson.

## Editorial review checklist

1. Does this teach something useful to an experienced engineer rather than merely name a task?
2. Can the learner distinguish known evidence, assumptions, and unknowns?
3. Is the exercise bounded enough for its estimated time? Estimates remain estimates until learners report actual time.
4. Do technical steps match the referenced starter and supported runtime?
5. Are model outputs treated as uncertain, with validation, safe failure, and human authority designed in?
6. Are non-obvious external claims cited to primary documentation, standards, research, or clearly labeled employer examples?
7. Does assessment reward evidence and reasoning instead of one preferred architecture?
8. Are licensing, privacy, accessibility, and third-party materials handled correctly?
9. Did a maintainer other than the author approve it before review/publication status changed?
10. Is learner validation documented separately, with cohort/context, method, feedback, revisions, and limitations?

## Status definitions

- **Authored:** content exists.
- **Structurally validated:** metadata, inventory, links, and dataset contract pass automated checks.
- **Reviewed:** a qualified second person completed and recorded this checklist.
- **Tested:** a specified automated test exercises relevant code or content contract; this does not prove every learning outcome.
- **Learner-validated:** real learners tried the material and their feedback was reviewed. Simulations and author walkthroughs do not qualify.
- **Published:** explicit maintainer decision after review. Publication does not imply learner validation or production readiness.

The current 90 lessons remain `preview`, `unreviewed`, and `not-validated`. Day 1 is a reference-quality draft for review, not a claim of external learner validation.
