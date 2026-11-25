import assert from 'node:assert/strict';
import test from 'node:test';

import { migrateLessonFrontmatter } from '../scripts/lib/lesson-metadata-migration.mjs';

const dayOne = `---
day: 1
phase: 1
status: Ready
title: From request to business outcome
estimated_effort: 60–90 minutes
---

# Day 1 — From request to business outcome

## Why this matters

An FDE is often handed a proposed solution before anyone agrees on the problem.

## Outcomes
- Separate a request from a business outcome.
- Identify evidence and assumptions.

## Exercise
Create a problem brief.
`;

test('migrates one legacy lesson while preserving its body and explicit preview evidence', () => {
  const migrated = migrateLessonFrontmatter(dayOne, 'curriculum/phase-1-foundations/day-01.md');
  const [frontmatter, body] = migrated.split('---\n').slice(1);

  assert.match(frontmatter, /schema_version: 1/);
  assert.match(frontmatter, /id: day-01/);
  assert.match(frontmatter, /publication_status: preview/);
  assert.match(frontmatter, /learner_validation_status: not-validated/);
  assert.deepEqual(body, dayOne.split('---\n').slice(2).join('---\n'));
});

test('metadata migration is idempotent', () => {
  const once = migrateLessonFrontmatter(dayOne, 'curriculum/phase-1-foundations/day-01.md');
  assert.equal(migrateLessonFrontmatter(once, 'curriculum/phase-1-foundations/day-01.md'), once);
});

test('rejects a legacy lesson without a parseable effort range or outcomes', () => {
  const invalid = dayOne.replace('estimated_effort: 60–90 minutes', 'estimated_effort: unknown');
  assert.throws(() => migrateLessonFrontmatter(invalid, 'broken.md'), /effort range/i);
});
