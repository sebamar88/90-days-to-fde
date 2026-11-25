#!/usr/bin/env node
// Dependency-free structural checks for the 90 Days to FDE curriculum.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const curriculum = path.join(root, 'curriculum');
const requiredFields = ['day', 'phase', 'status', 'title', 'estimated_effort'];
const requiredHeadings = ['why this matters', 'scenario', 'outcomes', 'exercise', 'deliverable', 'assessment', 'reflection'];
const errors = [];

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const full = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(full) : [full];
  });
}

function relative(file) {
  return path.relative(root, file).split(path.sep).join('/');
}

function checkLessons() {
  const lessonFiles = walk(curriculum).filter((file) => /[/\\]phase-[^/\\]+[/\\]day-\d+\.md$/.test(file));
  const days = new Map();
  for (const file of lessonFiles) {
    const name = path.basename(file);
    const match = /^day-(\d{2})\.md$/.exec(name);
    if (!match) {
      errors.push(`${relative(file)}: expected day-NN.md filename`);
      continue;
    }
    const day = Number(match[1]);
    if (days.has(day)) errors.push(`duplicate lesson for day ${day}: ${relative(days.get(day))} and ${relative(file)}`);
    days.set(day, file);

    const text = fs.readFileSync(file, 'utf8');
    const front = /^---\s*\n([\s\S]*?)\n---\s*\n/.exec(text);
    if (!front) {
      errors.push(`${relative(file)}: missing YAML front matter`);
      continue;
    }
    const fields = new Map();
    for (const line of front[1].split(/\r?\n/)) {
      const field = /^([a-z_]+):\s*(.*?)\s*$/.exec(line);
      if (field) fields.set(field[1], field[2].replace(/^['"]|['"]$/g, ''));
    }
    for (const field of requiredFields) if (!fields.has(field)) errors.push(`${relative(file)}: missing front matter field ${field}`);
    if (fields.get('day') !== String(day)) errors.push(`${relative(file)}: front matter day does not match filename`);
    if (fields.get('phase') !== '1') errors.push(`${relative(file)}: expected phase 1`);
    if (!['Ready', 'Draft', 'In Progress'].includes(fields.get('status'))) errors.push(`${relative(file)}: invalid status`);

    const headings = new Set([...text.matchAll(/^##\s+(.+?)\s*$/gm)].map((heading) => heading[1].trim().toLowerCase()));
    for (const heading of requiredHeadings) {
      if (!headings.has(heading) && !(heading === 'assessment' && headings.has('assessment rubric'))) {
        errors.push(`${relative(file)}: missing section ${heading}`);
      }
    }
  }
  for (let day = 1; day <= 15; day++) if (!days.has(day)) errors.push(`expected exactly one lesson for days 1–15; missing day ${day}`);
  for (const day of days.keys()) if (day < 1 || day > 15) errors.push(`unexpected lesson day outside 1–15: ${day}`);
}

function checkRoadmap() {
  const file = path.join(curriculum, 'README.md');
  const text = fs.readFileSync(file, 'utf8');
  const days = new Set([...text.matchAll(/(?:^|[·\s])([1-9]\d?)\./gm)].map((match) => Number(match[1])));
  for (let day = 1; day <= 90; day++) if (!days.has(day)) errors.push(`curriculum/README.md: missing roadmap entry for day ${day}`);
  for (const day of days) if (day < 1 || day > 90) errors.push(`curriculum/README.md: unexpected roadmap day ${day}`);
}

function checkMarkdownLinks() {
  const files = [path.join(root, 'README.md'), ...walk(curriculum), ...walk(path.join(root, 'docs'))]
    .filter((file) => file.endsWith('.md'));
  const links = /!?\[[^\]]*\]\(([^)]+)\)/g;
  for (const source of files) {
    const text = fs.readFileSync(source, 'utf8');
    for (const match of text.matchAll(links)) {
      const target = match[1].trim().split(/\s+/)[0].replace(/^<|>$/g, '');
      if (/^[a-z][a-z0-9+.-]*:/i.test(target) || target.startsWith('#')) continue;
      const pathname = decodeURIComponent(target.split('#')[0]);
      if (!pathname) continue;
      const destination = path.resolve(path.dirname(source), pathname);
      const insideRepo = destination === root || destination.startsWith(`${root}${path.sep}`);
      if (!insideRepo) {
        errors.push(`${relative(source)}: link escapes repository: ${target}`);
      } else if (!fs.existsSync(destination)) {
        errors.push(`${relative(source)}: broken local link: ${target}`);
      }
    }
  }
}

checkLessons();
checkRoadmap();
checkMarkdownLinks();
if (errors.length) {
  for (const item of errors) console.error(`ERROR: ${item}`);
  console.error(`Curriculum validation failed with ${errors.length} issue(s).`);
  process.exitCode = 1;
} else {
  console.log('Curriculum validation passed: 15 lessons, 90 roadmap days, local Markdown links.');
}
