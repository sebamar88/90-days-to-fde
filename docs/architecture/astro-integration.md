# Astro integration guide

The repository does not implement an Astro application. If a site is justified, it should consume the Markdown curriculum as build-time content while keeping this repository the canonical source.

## Recommended shape

1. Pin this repository to a release tag or immutable commit in the site build. Do not consume the moving default branch in production.
2. Check out or fetch that pin during the site build; avoid maintaining a second hand-edited copy of lessons. A Git submodule is another option, but adds update and recursive-checkout steps for contributors.
3. Read the versioned frontmatter contract and JSON Schema. Reject unknown `schema_version` values and validate metadata at the consumer boundary.
4. Treat `id` as the stable cross-reference key and `day` as sequence order. Generate navigation; do not add a second navigation graph.
5. Filter `publication_status` explicitly. The present catalog is preview content, so the site must visibly label it and must not silently treat it as reviewed or learner-validated.
6. Render the Markdown body with a trusted Markdown pipeline. Sanitize any generated HTML and keep arbitrary HTML/MDX execution disabled unless separately reviewed.
7. Preserve attribution and license per content type. Code and lesson content have different licenses; brand assets are excluded.

## Astro content collections

Astro's content collections provide typed build-time access to content and schemas. They are a suitable adapter, not the canonical contract. Keep the JSON Schema versioned here, and add a parity test if a Zod schema is introduced in the site. A future Zod schema must not loosen status, prerequisites, or license semantics silently.

Keep source-relative asset URLs resolvable from the pinned curriculum checkout, or copy only explicit allowlisted assets into the build output. Reject path traversal and avoid accepting arbitrary remote image URLs from contributed lesson metadata.

## Localization and search

Translations should reuse the stable lesson `id`, keep their locale in BCP-47 form, and use locale-unique slugs. The English entry remains canonical for technical changes; translation status and review must be tracked independently. Search indexes can be generated from title, description, objectives, tags, and body at build time.

## Build and failure behavior

- Run the repository checks before publishing and fail the build for invalid metadata or missing curriculum references.
- Pin the source commit and record it in the build metadata so a deployment can be reproduced.
- Make previews opt-in or visibly labeled until review status changes.
- Ensure no private keys or analytics secrets are required to browse the free lessons.
- Keep progress tracking, accounts, paid access, and AI mentorship out of the initial integration; validate learner needs before adding these systems.

## Decision gate

Before starting Astro, confirm that maintainers can keep a static site current and that a specific discovery/search/accessibility need is unmet by the GitHub repository and current landing page. If not, improve source docs and links instead of introducing another deployment surface.

References: [Astro content collections](https://docs.astro.build/en/guides/content-collections/); [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use).
