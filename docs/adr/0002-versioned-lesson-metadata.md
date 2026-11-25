# ADR-0002: Version lesson metadata as JSON Schema

- **Status:** Accepted
- **Date:** 2026-11-25
- **Decision owners:** Curriculum maintainers

## Context

The repository currently stores lesson metadata in Markdown front matter, but does not define a stable ID, slug, typed duration, objectives, skills, prerequisites, or publication semantics. A future site needs reliable navigation and filtering without becoming a second source of curriculum content. The current validator reads YAML with regular expressions and cannot safely enforce nested values.

## Decision

Keep Markdown files in `curriculum/` as the canonical content. Define `schemas/lesson.schema.json` as the versioned metadata contract and validate YAML front matter with a real YAML parser followed by JSON Schema validation. Use stable IDs `day-01` through `day-90`; keep lesson paths and headings intact. Add repository-level checks for phase/day alignment, unique IDs/slugs, prerequisite references/cycles, headings, links, and dataset shape.

`publication_status` describes site visibility, not proof of quality:

- `draft`: exclude from public lesson navigation.
- `preview`: show only when the consumer opts into previews and visibly label it unfinished.
- `published`: eligible for normal navigation after maintainer review.
- `archived`: hide from current navigation while preserving links/history.

`review_status`, `test_coverage`, and `learner_validation_status` are separate evidence fields. A linked or passing phase lab does not mean the lesson itself has been peer-reviewed or validated with learners. `published` requires `review_status: reviewed`, but learner validation remains separately reported and is not implied.

Schema version 1 requires metadata compatible with the existing 90 lessons; adding properties or constraints requires a schema version change when it breaks existing producers. Consumers must reject unknown schema versions and can continue to consume old versions through an explicit migration adapter. Do not rewrite lesson bodies as part of metadata migrations.

## Options considered

1. **Continue parsing YAML with regexes or infer from filenames.** No dependency, but nested fields and types are unsafe to consume, and validation becomes progressively more brittle.
2. **Use an Astro-specific schema as canonical.** Convenient for a future site, but couples the public source repository to an application that does not exist and duplicates validation for non-Astro consumers.
3. **Versioned JSON Schema plus YAML parser.** Adds two small development dependencies but provides a machine-readable contract usable by independent tools and a complete YAML parser for source files.

## Consequences

- Markdown remains readable and is not duplicated into generated content files.
- CI/local validation becomes dependent on npm dev dependencies; `package-lock.json` pins them.
- The schema is language-neutral. An Astro consumer may use a generated or equivalent Zod schema at its boundary, but the JSON Schema remains canonical and must be checked for semantic parity.
- Metadata review labels must be maintained honestly; an automated phase test is not a substitute for educational review.
- Stable IDs and slugs should be treated as public identifiers and should not be changed casually.

## Revisit when

An independent consumer demonstrates a concrete need that cannot be served by the current schema, a breaking schema change is proposed, or learner and maintainer feedback shows the metadata burdens authoring without improving navigation or quality.
