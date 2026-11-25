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
    const phaseMatch = /[/\\]phase-(\d+)-/.exec(file);
    if (!phaseMatch || fields.get('phase') !== phaseMatch[1]) errors.push(`${relative(file)}: front matter phase does not match its directory`);
    if (!['Ready', 'Draft', 'In Progress'].includes(fields.get('status'))) errors.push(`${relative(file)}: invalid status`);

    const headings = new Set([...text.matchAll(/^##\s+(.+?)\s*$/gm)].map((heading) => heading[1].trim().toLowerCase()));
    for (const heading of requiredHeadings) {
      if (!headings.has(heading) && !(heading === 'assessment' && headings.has('assessment rubric'))) {
        errors.push(`${relative(file)}: missing section ${heading}`);
      }
    }
  }
  for (let day = 1; day <= 90; day++) if (!days.has(day)) errors.push(`expected exactly one lesson for days 1–90; missing day ${day}`);
  for (const day of days.keys()) if (day < 1 || day > 90) errors.push(`unexpected lesson day outside 1–90: ${day}`);
  for (const [day, file] of days) {
    const expectedPhase = Math.ceil(day / 15);
    if (Number(/[/\\]phase-(\d+)-/.exec(file)?.[1]) !== expectedPhase) {
      errors.push(`${relative(file)}: day ${day} must belong to phase ${expectedPhase}`);
    }
  }
}

function checkPhaseOverviews() {
  for (let phase = 1; phase <= 6; phase++) {
    const directory = fs.readdirSync(curriculum, { withFileTypes: true })
      .find((entry) => entry.isDirectory() && entry.name.startsWith(`phase-${phase}-`));
    if (!directory) {
      errors.push(`missing curriculum directory for phase ${phase}`);
      continue;
    }
    const overview = path.join(curriculum, directory.name, 'README.md');
    if (!fs.existsSync(overview)) errors.push(`${relative(overview)}: missing phase overview`);
  }
}

function checkRoadmap() {
  const file = path.join(curriculum, 'README.md');
  const text = fs.readFileSync(file, 'utf8');
  const days = new Set([...text.matchAll(/(?:^|[·\s])([1-9]\d?)\./gm)].map((match) => Number(match[1])));
  for (let day = 1; day <= 90; day++) if (!days.has(day)) errors.push(`curriculum/README.md: missing roadmap entry for day ${day}`);
  for (const day of days) if (day < 1 || day > 90) errors.push(`curriculum/README.md: unexpected roadmap day ${day}`);
}

function checkSyntheticDataset() {
  const file = path.join(root, 'curriculum', 'phase-2-production-ai', 'starter', 'data', 'evaluation.jsonl');
  const seen = new Set();
  const allowedCategories = new Set(['electrical', 'hvac', 'plumbing', 'other', 'unknown']);
  const allowedUrgencies = new Set(['routine', 'urgent', 'emergency', 'unknown']);
  const allowedMissing = new Set(['location', 'category', 'urgency']);
  const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/).filter((line) => line.trim());
  if (lines.length < 8) errors.push('Phase 2 synthetic evaluation set must contain at least 8 cases');
  lines.forEach((line, index) => {
    let row;
    try {
      row = JSON.parse(line);
    } catch {
      errors.push(`${relative(file)}:${index + 1}: invalid JSON`);
      return;
    }
    for (const field of ['case_id', 'text', 'expected_category', 'expected_location', 'expected_urgency', 'expected_missing_fields']) {
      if (!(field in row)) errors.push(`${relative(file)}:${index + 1}: missing ${field}`);
    }
    if (!row.case_id || seen.has(row.case_id)) errors.push(`${relative(file)}:${index + 1}: missing or duplicate case_id`);
    seen.add(row.case_id);
    if (!row.text?.trim()) errors.push(`${relative(file)}:${index + 1}: empty text`);
    if (!allowedCategories.has(row.expected_category)) errors.push(`${relative(file)}:${index + 1}: invalid expected_category`);
    if (!allowedUrgencies.has(row.expected_urgency)) errors.push(`${relative(file)}:${index + 1}: invalid expected_urgency`);
    if (!Array.isArray(row.expected_missing_fields) || row.expected_missing_fields.some((field) => !allowedMissing.has(field))) {
      errors.push(`${relative(file)}:${index + 1}: invalid expected_missing_fields`);
    }
  });
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
checkPhaseOverviews();
checkRoadmap();
checkSyntheticDataset();
checkMarkdownLinks();
if (errors.length) {
  for (const item of errors) console.error(`ERROR: ${item}`);
  console.error(`Curriculum validation failed with ${errors.length} issue(s).`);
  process.exitCode = 1;
} else {
  console.log('Curriculum validation passed: 90 lessons, six phase overviews, roadmap coverage, and local Markdown links.');
}
