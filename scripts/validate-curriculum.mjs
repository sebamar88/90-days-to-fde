#!/usr/bin/env node
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateCurriculum } from './lib/curriculum-validator.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const errors = validateCurriculum(root);

if (errors.length > 0) {
  for (const error of errors) console.error(`ERROR: ${error}`);
  console.error(`Curriculum validation failed with ${errors.length} issue(s).`);
  process.exitCode = 1;
} else {
  console.log('Curriculum validation passed: metadata schema, 90 day/phase assignments, prerequisite graph, lesson sections, Markdown links and anchors, phase overviews, roadmap coverage, and synthetic dataset are valid.');
}
