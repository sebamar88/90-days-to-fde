#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { migrateLessonFrontmatter } from './lib/lesson-metadata-migration.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const write = process.argv.includes('--write');
const lessonFiles = [];
for (const entry of fs.readdirSync(path.join(root, 'curriculum'), { withFileTypes: true })) {
  if (!entry.isDirectory() || !/^phase-[1-6]-/.test(entry.name)) continue;
  const directory = path.join(root, 'curriculum', entry.name);
  for (const file of fs.readdirSync(directory)) {
    if (/^day-\d+\.md$/.test(file)) lessonFiles.push(path.join(directory, file));
  }
}

let changed = 0;
for (const file of lessonFiles) {
  const original = fs.readFileSync(file, 'utf8');
  const migrated = migrateLessonFrontmatter(original, path.relative(root, file).split(path.sep).join('/'));
  if (migrated === original) continue;
  changed += 1;
  if (write) fs.writeFileSync(file, migrated, 'utf8');
}

if (write) console.log(`Migrated ${changed} lesson metadata records to contract v1.`);
else console.log(`Dry run: ${changed} lesson metadata records would be migrated. Re-run with --write to apply.`);
