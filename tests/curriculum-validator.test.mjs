import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';

import {
  parseFrontmatter,
  validateCurriculumMetadata,
  validateEvaluationDataset,
  validateLessonMetadata,
  validateLessonSections,
  validateMarkdownLinks,
} from '../scripts/lib/curriculum-validator.mjs';

function metadata(day, overrides = {}) {
  return {
    schema_version: 1,
    id: `day-${String(day).padStart(2, '0')}`,
    day,
    phase: Math.ceil(day / 15),
    locale: 'en',
    slug: `lesson-${String(day).padStart(2, '0')}`,
    title: `Lesson ${day}`,
    description: `Learn a useful skill for day ${day}.`,
    publication_status: 'preview',
    content_type: 'concept-lesson',
    difficulty: 'foundational',
    duration: { min: 60, max: 90 },
    prerequisites: day === 1 ? [] : [`day-${String(day - 1).padStart(2, '0')}`],
    objectives: ['Identify the problem.', 'Compare useful options.', 'Explain the trade-off.'],
    tags: ['phase-foundations'],
    skills: ['problem-framing'],
    review_status: 'unreviewed',
    test_coverage: 'phase-lab',
    learner_validation_status: 'not-validated',
    ...overrides,
  };
}

function completeCurriculum(overrides = new Map()) {
  return Array.from({ length: 90 }, (_, index) => {
    const day = index + 1;
    return {
      file: `day-${String(day).padStart(2, '0')}.md`,
      metadata: { ...metadata(day), ...(overrides.get(day) ?? {}) },
    };
  });
}

test('parses typed YAML metadata and preserves the Markdown body', () => {
  const parsed = parseFrontmatter(
    '---\nday: 1\nobjectives:\n  - Explain the result\n---\n\n# Lesson\n',
    'fixture.md',
  );

  assert.equal(parsed.metadata.day, 1);
  assert.deepEqual(parsed.metadata.objectives, ['Explain the result']);
  assert.match(parsed.body, /^\n# Lesson/);
  assert.deepEqual(parsed.errors, []);
});

test('reports malformed YAML with fixture path and line context', () => {
  const fixture = fs.readFileSync(new URL('./fixtures/malformed-frontmatter.md', import.meta.url), 'utf8');
  const parsed = parseFrontmatter(fixture, 'malformed-frontmatter.md');

  assert.equal(parsed.metadata, null);
  assert.ok(parsed.errors.some((error) => error.includes('malformed-frontmatter.md') && /:3:/.test(error)));
});

test('rejects duplicate YAML keys', () => {
  const fixture = fs.readFileSync(new URL('./fixtures/duplicate-frontmatter-key.md', import.meta.url), 'utf8');
  const parsed = parseFrontmatter(fixture, 'duplicate-frontmatter-key.md');

  assert.equal(parsed.metadata, null);
  assert.ok(parsed.errors.some((error) => /duplicate-frontmatter-key.md.*unique|duplicate.*key/i.test(error)));
});

test('accepts contract metadata and rejects incorrect types or status values', () => {
  assert.deepEqual(validateLessonMetadata(metadata(1), 'day-01.md'), []);

  const errors = validateLessonMetadata(
    metadata(1, { day: '1', publication_status: 'Ready', duration: { min: 90, max: 60 } }),
    'day-01.md',
  );
  assert.ok(errors.some((error) => /day/i.test(error)));
  assert.ok(errors.some((error) => /publication_status/i.test(error)));
  assert.ok(errors.some((error) => /duration/i.test(error)));
});

test('rejects non-object metadata without crashing', () => {
  assert.ok(validateLessonMetadata(null, 'null-frontmatter.md').some((error) => /metadata/i.test(error)));
});

test('rejects empty and duplicate required lesson sections', () => {
  const content = [
    '## Why this matters', 'A teaching explanation.',
    '## Outcomes', '- Demonstrate the first outcome.',
    '## Explanation', '## Exercise', 'Complete one task.',
    '## Assessment', 'Pass when evidence is present.',
  ].join('\n\n');
  const errors = validateLessonSections(content, metadata(1), 'empty-section.md');

  assert.ok(errors.some((error) => /section "explanation" must not be empty/i.test(error)));

  const duplicate = `${content}\n\n## Explanation\n\nSecond explanation.`;
  assert.ok(validateLessonSections(duplicate, metadata(1), 'duplicate-section.md').some((error) => /duplicate section "explanation"/i.test(error)));
});

test('checks exactly one lesson per day and unique IDs and slugs', () => {
  const records = completeCurriculum();
  records[1].metadata.id = records[0].metadata.id;
  records[2].metadata.slug = records[1].metadata.slug;

  const errors = validateCurriculumMetadata(records);
  assert.ok(errors.some((error) => /duplicate.*id/i.test(error)));
  assert.ok(errors.some((error) => /duplicate.*slug/i.test(error)));
  assert.deepEqual(validateCurriculumMetadata(records.slice(1)).filter((error) => /missing day 1/i.test(error)).length, 1);
});

test('rejects wrong phase, missing prerequisite IDs, and prerequisite cycles', () => {
  const wrongPhase = new Map([[16, { phase: 1 }]]);
  const errors = validateCurriculumMetadata(completeCurriculum(wrongPhase));
  assert.ok(errors.some((error) => /day-16.*phase/i.test(error)));

  const missing = new Map([[3, { prerequisites: ['day-99'] }]]);
  assert.ok(validateCurriculumMetadata(completeCurriculum(missing)).some((error) => /prerequisite.*day-99/i.test(error)));

  const cycle = new Map([
    [1, { prerequisites: ['day-02'] }],
    [2, { prerequisites: ['day-01'] }],
  ]);
  assert.ok(validateCurriculumMetadata(completeCurriculum(cycle)).some((error) => /cycle/i.test(error)));

  const self = new Map([[7, { prerequisites: ['day-07'] }]]);
  const selfErrors = validateCurriculumMetadata(completeCurriculum(self));
  assert.ok(selfErrors.some((error) => /day-07.*earlier lesson/i.test(error)));
  assert.ok(selfErrors.some((error) => /cycle.*day-07/i.test(error)));
});

test('checks local Markdown paths and anchors but ignores external URLs', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'fde-links-'));
  const source = path.join(root, 'source.md');
  fs.writeFileSync(path.join(root, 'target.md'), '# Target\n\n## A useful section\n');
  const errors = validateMarkdownLinks(
    '[good](target.md#a-useful-section) [bad anchor](target.md#missing) [missing](absent.md) [web](https://example.com)',
    source,
    root,
  );

  assert.ok(errors.some((error) => /missing anchor/i.test(error)));
  assert.ok(errors.some((error) => /broken.*path/i.test(error)));
  assert.equal(errors.some((error) => /example.com/.test(error)), false);
});

test('rejects links that escape the repository root', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'fde-links-'));
  const errors = validateMarkdownLinks('[escape](../../outside.md)', path.join(root, 'lesson.md'), root);
  assert.ok(errors.some((error) => /escapes repository/i.test(error)));
});

test('validates synthetic JSONL types, required fields, enums, and duplicate case IDs', () => {
  const rows = [
    JSON.stringify({ case_id: 'x', split: 'development', text: 'Building 1 leak', expected_category: 'plumbing', expected_location: 'Building 1', expected_urgency: 'urgent', expected_missing_fields: [], rationale: 'The text explicitly identifies a leak.' }),
    JSON.stringify({ case_id: 'x', split: 'holdout', text: '   ', expected_category: 'unknown-value', expected_location: null, expected_urgency: 'urgent', expected_missing_fields: 'location' }),
  ].join('\n');

  const errors = validateEvaluationDataset(rows, 'dataset.jsonl');
  assert.ok(errors.some((error) => /duplicate.*case_id/i.test(error)));
  assert.ok(errors.some((error) => /text/i.test(error)));
  assert.ok(errors.some((error) => /expected_category/i.test(error)));
  assert.ok(errors.some((error) => /expected_missing_fields/i.test(error)));
  assert.ok(errors.some((error) => /rationale/i.test(error)));
});
