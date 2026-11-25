import fs from 'node:fs';
import path from 'node:path';
import Ajv from 'ajv';
import { LineCounter, parseDocument } from 'yaml';

const schemaPath = new URL('../../schemas/lesson.schema.json', import.meta.url);
const lessonSchema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
const validateSchema = new Ajv({ allErrors: true, strict: true }).compile(lessonSchema);

const requiredSections = {
  'concept-lesson': ['why this matters', 'outcomes', 'explanation', 'exercise', 'assessment'],
  'guided-technical-lab': ['scenario', 'outcomes', 'exercise', 'deliverable', 'assessment', 'automated lab'],
  'business-discovery-exercise': ['scenario', 'outcomes', 'exercise', 'deliverable', 'assessment'],
  'architecture-challenge': ['scenario', 'outcomes', 'exercise', 'deliverable', 'assessment'],
  'enterprise-simulation': ['scenario', 'outcomes', 'exercise', 'deliverable', 'assessment'],
  'phase-assessment': ['scenario', 'outcomes', 'deliverable', 'assessment rubric'],
  'capstone-milestone': ['scenario', 'outcomes', 'exercise', 'deliverable', 'assessment'],
};

function displayPath(file) {
  return typeof file === 'string' ? file : String(file);
}

function lineNumber(lineCounter, error) {
  const offset = Array.isArray(error.pos) ? error.pos[0] : 0;
  return lineCounter.linePos(offset).line + 1;
}

export function parseFrontmatter(markdown, file = '<memory>') {
  const content = markdown.replace(/^\uFEFF/, '');
  const match = /^(?:---)\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/.exec(content);
  if (!match) {
    return { metadata: null, body: '', errors: [`${displayPath(file)}: missing YAML front matter delimited by ---`] };
  }

  const lineCounter = new LineCounter();
  const document = parseDocument(match[1], {
    lineCounter,
    prettyErrors: true,
    strict: true,
    uniqueKeys: true,
  });
  const errors = [...document.errors].map((error) =>
    `${displayPath(file)}:${lineNumber(lineCounter, error)}: invalid YAML front matter: ${error.message}`,
  );

  let metadata = null;
  if (errors.length === 0) {
    try {
      metadata = document.toJS({ maxAliasCount: 20 });
      if (metadata === null || Array.isArray(metadata) || typeof metadata !== 'object') {
        errors.push(`${displayPath(file)}: front matter must be a YAML mapping`);
        metadata = null;
      }
    } catch (error) {
      errors.push(`${displayPath(file)}: could not convert YAML front matter: ${error.message}`);
    }
  }

  return { metadata, body: content.slice(match[0].length), errors };
}

export function validateLessonMetadata(metadata, file = '<memory>') {
  const errors = [];
  if (!validateSchema(metadata)) {
    for (const error of validateSchema.errors ?? []) {
      const field = error.instancePath || '/';
      errors.push(`${displayPath(file)}: metadata ${field} ${error.message}`);
    }
  }

  if (metadata === null || typeof metadata !== 'object' || Array.isArray(metadata)) return errors;

  if (Number.isInteger(metadata.day) && Number.isInteger(metadata.phase)
    && metadata.phase !== Math.ceil(metadata.day / 15)) {
    errors.push(`${displayPath(file)}: day ${metadata.day} must belong to phase ${Math.ceil(metadata.day / 15)}`);
  }
  if (Number.isInteger(metadata.duration?.min) && Number.isInteger(metadata.duration?.max)
    && metadata.duration.min > metadata.duration.max) {
    errors.push(`${displayPath(file)}: duration.min must be less than or equal to duration.max`);
  }
  if (metadata.publication_status === 'published' && metadata.review_status !== 'reviewed') {
    errors.push(`${displayPath(file)}: published lessons must have review_status: reviewed`);
  }
  return errors;
}

export function validateCurriculumMetadata(records) {
  const errors = [];
  const days = new Map();
  const ids = new Map();
  const slugs = new Map();

  for (const record of records) {
    if (!record?.metadata || typeof record.metadata !== 'object') {
      errors.push(`${displayPath(record?.file ?? '<unknown>')}: lesson metadata is unavailable`);
      continue;
    }

    const { metadata, file } = record;
    errors.push(...validateLessonMetadata(metadata, file));

    if (Number.isInteger(metadata.day) && typeof metadata.id === 'string') {
      const expectedId = `day-${String(metadata.day).padStart(2, '0')}`;
      if (metadata.id !== expectedId) errors.push(`${displayPath(file)}: id must be ${expectedId} for this day`);
    }

    if (Number.isInteger(metadata.day)) {
      if (days.has(metadata.day)) {
        errors.push(`${displayPath(file)}: duplicate day ${metadata.day}; also found in ${displayPath(days.get(metadata.day))}`);
      } else {
        days.set(metadata.day, file);
      }
    }
    if (typeof metadata.id === 'string') {
      if (ids.has(metadata.id)) {
        errors.push(`${displayPath(file)}: duplicate id "${metadata.id}"; also found in ${displayPath(ids.get(metadata.id))}`);
      } else {
        ids.set(metadata.id, file);
      }
    }
    for (const [field, index] of [['slug', slugs]]) {
      if (typeof metadata[field] !== 'string') continue;
      const key = `${metadata.locale}:${metadata[field]}`;
      if (index.has(key)) {
        errors.push(`${displayPath(file)}: duplicate ${field} "${metadata[field]}"; also found in ${displayPath(index.get(metadata[field]))}`);
      } else {
        index.set(key, file);
      }
    }
  }

  for (let day = 1; day <= 90; day += 1) {
    if (!days.has(day)) errors.push(`curriculum: expected one lesson for day ${day}; missing day ${day}`);
  }

  const byId = new Map(records
    .filter((record) => typeof record?.metadata?.id === 'string')
    .map((record) => [record.metadata.id, record]));
  const graph = new Map();
  for (const { file, metadata } of records) {
    if (!metadata || !Array.isArray(metadata.prerequisites)) continue;
    const dependencies = [];
    for (const prerequisite of metadata.prerequisites) {
      const referenced = byId.get(prerequisite);
      if (!referenced) {
        errors.push(`${displayPath(file)}: prerequisite "${prerequisite}" does not exist`);
      } else {
        dependencies.push(prerequisite);
        if (Number.isInteger(metadata.day) && Number.isInteger(referenced.metadata.day)
          && referenced.metadata.day >= metadata.day) {
          errors.push(`${displayPath(file)}: prerequisite "${prerequisite}" must refer to an earlier lesson`);
        }
      }
    }
    graph.set(metadata.id, dependencies);
  }

  const visited = new Set();
  const active = new Set();
  const cycleSignatures = new Set();
  function visit(id, trail = []) {
    if (active.has(id)) {
      const cycle = trail.slice(trail.indexOf(id)).concat(id);
      const signature = [...new Set(cycle)].sort().join('|');
      if (!cycleSignatures.has(signature)) {
        cycleSignatures.add(signature);
        errors.push(`curriculum: prerequisite cycle detected: ${cycle.join(' -> ')}`);
      }
      return;
    }
    if (visited.has(id)) return;
    active.add(id);
    for (const dependency of graph.get(id) ?? []) visit(dependency, trail.concat(id));
    active.delete(id);
    visited.add(id);
  }
  for (const id of graph.keys()) visit(id);

  return errors;
}

function markdownAnchor(heading) {
  return heading
    .replace(/<[^>]*>/g, '')
    .replace(/`/g, '')
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^\p{L}\p{N}_ -]/gu, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');
}

function markdownAnchors(markdown) {
  const anchors = new Set();
  const counts = new Map();
  const cleanMarkdown = markdown.replace(/```[\s\S]*?```/g, '').replace(/~~~[\s\S]*?~~~/g, '');
  for (const match of cleanMarkdown.matchAll(/^#{1,6}\s+(.+?)\s*#*\s*$/gm)) {
    const base = markdownAnchor(match[1]);
    if (!base) continue;
    const count = counts.get(base) ?? 0;
    counts.set(base, count + 1);
    anchors.add(count === 0 ? base : `${base}-${count}`);
  }
  for (const match of cleanMarkdown.matchAll(/\bid\s*=\s*["']([^"']+)["']/gi)) anchors.add(match[1]);
  for (const match of cleanMarkdown.matchAll(/\bname\s*=\s*["']([^"']+)["']/gi)) anchors.add(match[1]);
  return anchors;
}

function resolveMarkdownTarget(sourceFile, decodedPath) {
  if (decodedPath === '') return path.resolve(sourceFile);
  const candidate = path.resolve(path.dirname(sourceFile), decodedPath);
  if (!fs.existsSync(candidate) || !fs.statSync(candidate).isDirectory()) return candidate;
  for (const name of ['index.md', 'README.md']) {
    const indexFile = path.join(candidate, name);
    if (fs.existsSync(indexFile)) return indexFile;
  }
  return candidate;
}

export function validateMarkdownLinks(markdown, sourceFile, repositoryRoot) {
  const errors = [];
  const source = path.resolve(sourceFile);
  const root = path.resolve(repositoryRoot);
  const readable = markdown.replace(/```[\s\S]*?```/g, '').replace(/~~~[\s\S]*?~~~/g, '');
  const markdownLink = /!?\[[^\]]*\]\(([^)]+)\)/g;

  for (const match of readable.matchAll(markdownLink)) {
    const target = match[1].trim().split(/\s+/)[0].replace(/^<|>$/g, '');
    if (!target || /^[a-z][a-z0-9+.-]*:/i.test(target) || target.startsWith('//')) continue;

    let decodedPath;
    let anchor;
    try {
      const hashIndex = target.indexOf('#');
      const rawPath = hashIndex < 0 ? target : target.slice(0, hashIndex);
      const rawAnchor = hashIndex < 0 ? '' : target.slice(hashIndex + 1);
      decodedPath = decodeURIComponent(rawPath);
      anchor = decodeURIComponent(rawAnchor);
    } catch {
      errors.push(`${displayPath(sourceFile)}: malformed percent encoding in local link "${target}"`);
      continue;
    }

    let destination;
    try {
      destination = resolveMarkdownTarget(source, decodedPath);
    } catch {
      errors.push(`${displayPath(sourceFile)}: invalid local link path "${target}"`);
      continue;
    }

    const relative = path.relative(root, destination);
    if (relative === '..' || relative.startsWith(`..${path.sep}`) || path.isAbsolute(relative)) {
      errors.push(`${displayPath(sourceFile)}: link escapes repository: ${target}`);
      continue;
    }
    if (!fs.existsSync(destination)) {
      errors.push(`${displayPath(sourceFile)}: broken local path: ${target}`);
      continue;
    }
    if (fs.statSync(destination).isDirectory()) {
      if (anchor) errors.push(`${displayPath(sourceFile)}: cannot resolve anchor on directory link "${target}"`);
      continue;
    }
    if (anchor) {
      const targetText = fs.readFileSync(destination, 'utf8');
      if (!markdownAnchors(targetText).has(anchor)) {
        errors.push(`${displayPath(sourceFile)}: missing anchor "${anchor}" in ${path.relative(root, destination).split(path.sep).join('/')}`);
      }
    }
  }
  return errors;
}

export function validateEvaluationDataset(contents, file = '<dataset>') {
  const errors = [];
  const caseIds = new Set();
  const allowedCategories = new Set(['electrical', 'hvac', 'plumbing', 'other', 'unknown']);
  const allowedUrgencies = new Set(['routine', 'urgent', 'emergency', 'unknown']);
  const allowedMissingFields = new Set(['location', 'category', 'urgency']);
  const splitCounts = new Map([['development', 0], ['holdout', 0]]);
  const lines = contents.split(/\r?\n/).filter((line) => line.trim());

  if (lines.length < 8) errors.push(`${displayPath(file)}: evaluation dataset must contain at least 8 records`);
  lines.forEach((line, index) => {
    const prefix = `${displayPath(file)}:${index + 1}`;
    let row;
    try {
      row = JSON.parse(line);
    } catch {
      errors.push(`${prefix}: invalid JSON`);
      return;
    }
    if (row === null || Array.isArray(row) || typeof row !== 'object') {
      errors.push(`${prefix}: each record must be a JSON object`);
      return;
    }

    for (const field of ['case_id', 'split', 'text', 'expected_category', 'expected_location', 'expected_urgency', 'expected_missing_fields', 'rationale']) {
      if (!(field in row)) errors.push(`${prefix}: missing ${field}`);
    }
    if (typeof row.case_id !== 'string' || !row.case_id.trim()) {
      errors.push(`${prefix}: case_id must be a non-empty string`);
    } else if (caseIds.has(row.case_id)) {
      errors.push(`${prefix}: duplicate case_id "${row.case_id}"`);
    } else {
      caseIds.add(row.case_id);
    }
    if (row.split !== 'development' && row.split !== 'holdout') {
      errors.push(`${prefix}: split must be development or holdout`);
    } else {
      splitCounts.set(row.split, splitCounts.get(row.split) + 1);
    }
    if (typeof row.text !== 'string' || !row.text.trim()) errors.push(`${prefix}: text must be a non-empty string`);
    if (!allowedCategories.has(row.expected_category)) errors.push(`${prefix}: invalid expected_category`);
    if (row.expected_location !== null && (typeof row.expected_location !== 'string' || !row.expected_location.trim())) {
      errors.push(`${prefix}: expected_location must be null or a non-empty string`);
    }
    if (!allowedUrgencies.has(row.expected_urgency)) errors.push(`${prefix}: invalid expected_urgency`);
    if (!Array.isArray(row.expected_missing_fields)
      || row.expected_missing_fields.some((field) => !allowedMissingFields.has(field))
      || new Set(row.expected_missing_fields).size !== row.expected_missing_fields.length) {
      errors.push(`${prefix}: invalid expected_missing_fields`);
    }
    if (typeof row.rationale !== 'string' || !row.rationale.trim()) errors.push(`${prefix}: rationale must be a non-empty string`);
  });

  for (const split of ['development', 'holdout']) {
    if (splitCounts.get(split) === 0) errors.push(`${displayPath(file)}: evaluation dataset must include ${split} cases`);
  }
  return errors;
}

export function validateLessonSections(markdown, metadata, file = '<memory>') {
  const required = requiredSections[metadata.content_type] ?? [];
  const errors = [];
  const readable = markdown.replace(/```[\s\S]*?```/g, '').replace(/~~~[\s\S]*?~~~/g, '');
  const matches = [...readable.matchAll(/^##\s+(.+?)\s*$/gm)];
  const sections = new Map();
  matches.forEach((match, index) => {
    const name = match[1].trim().toLowerCase();
    const end = matches[index + 1]?.index ?? readable.length;
    const body = readable.slice(match.index + match[0].length, end).trim();
    const entries = sections.get(name) ?? [];
    entries.push(body);
    sections.set(name, entries);
  });

  for (const requiredHeading of required) {
    const heading = requiredHeading === 'assessment rubric' && !sections.has('assessment rubric')
      ? 'assessment'
      : requiredHeading;
    const bodies = sections.get(heading);
    if (!bodies) {
      errors.push(`${displayPath(file)}: missing section "${requiredHeading}" required for ${metadata.content_type}`);
      continue;
    }
    if (bodies.length > 1) errors.push(`${displayPath(file)}: duplicate section "${heading}"`);
    if (bodies.some((body) => body.length === 0)) errors.push(`${displayPath(file)}: section "${heading}" must not be empty`);
  }
  return errors;
}

function lessonFiles(root) {
  const curriculumRoot = path.join(root, 'curriculum');
  const files = [];
  for (const directory of fs.readdirSync(curriculumRoot, { withFileTypes: true })) {
    if (!directory.isDirectory() || !/^phase-[1-6]-/.test(directory.name)) continue;
    const directoryPath = path.join(curriculumRoot, directory.name);
    for (const entry of fs.readdirSync(directoryPath, { withFileTypes: true })) {
      if (entry.isFile() && /^day-\d+\.md$/.test(entry.name)) files.push(path.join(directoryPath, entry.name));
    }
  }
  return files.sort((left, right) => left.localeCompare(right, 'en', { numeric: true }));
}

function allMarkdownFiles(root) {
  const files = [];
  const skippedDirectories = new Set(['.git', '.venv', 'node_modules', '.superpowers', 'dist']);
  const stack = [root];
  while (stack.length) {
    const current = stack.pop();
    for (const entry of fs.readdirSync(current, { withFileTypes: true })) {
      if (entry.isDirectory()) {
        if (!skippedDirectories.has(entry.name)) stack.push(path.join(current, entry.name));
      } else if (entry.isFile() && entry.name.endsWith('.md')) {
        files.push(path.join(current, entry.name));
      }
    }
  }
  return files;
}

function relativeToRoot(root, file) {
  return path.relative(root, file).split(path.sep).join('/');
}

export function validateCurriculum(root) {
  const errors = [];
  const records = [];
  for (const file of lessonFiles(root)) {
    const relative = relativeToRoot(root, file);
    const markdown = fs.readFileSync(file, 'utf8');
    const parsed = parseFrontmatter(markdown, relative);
    errors.push(...parsed.errors);
    if (parsed.metadata) {
      records.push({ file: relative, metadata: parsed.metadata });
      errors.push(...validateLessonSections(markdown, parsed.metadata, relative));
      const expectedName = `day-${String(parsed.metadata.day).padStart(2, '0')}.md`;
      if (path.basename(file) !== expectedName) errors.push(`${relative}: filename must match metadata day (${expectedName})`);
      const phaseDirectory = /^phase-(\d+)-/.exec(path.basename(path.dirname(file)));
      if (phaseDirectory && parsed.metadata.phase !== Number(phaseDirectory[1])) {
        errors.push(`${relative}: metadata phase does not match its phase directory`);
      }
    }
  }
  errors.push(...validateCurriculumMetadata(records));

  const markdownFiles = allMarkdownFiles(root);
  for (const file of markdownFiles) {
    const markdown = fs.readFileSync(file, 'utf8');
    errors.push(...validateMarkdownLinks(markdown, file, root));
  }

  for (let phase = 1; phase <= 6; phase += 1) {
    const phaseDirectory = fs.readdirSync(path.join(root, 'curriculum'), { withFileTypes: true })
      .find((entry) => entry.isDirectory() && entry.name.startsWith(`phase-${phase}-`));
    if (!phaseDirectory) {
      errors.push(`curriculum: missing directory for phase ${phase}`);
      continue;
    }
    const overview = path.join(root, 'curriculum', phaseDirectory.name, 'README.md');
    if (!fs.existsSync(overview)) errors.push(`${relativeToRoot(root, overview)}: phase overview is missing`);
  }

  const curriculumMap = path.join(root, 'curriculum', 'README.md');
  if (!fs.existsSync(curriculumMap)) {
    errors.push('curriculum/README.md: curriculum map is missing');
  } else {
    const mapText = fs.readFileSync(curriculumMap, 'utf8');
    const mappedDays = new Set([...mapText.matchAll(/(?:^|[·\s])([1-9]\d?)\./gm)].map((match) => Number(match[1])));
    for (let day = 1; day <= 90; day += 1) {
      if (!mappedDays.has(day)) errors.push(`curriculum/README.md: missing roadmap entry for day ${day}`);
    }
  }

  const dataset = path.join(root, 'curriculum', 'phase-2-production-ai', 'starter', 'data', 'evaluation.jsonl');
  if (fs.existsSync(dataset)) {
    errors.push(...validateEvaluationDataset(fs.readFileSync(dataset, 'utf8'), relativeToRoot(root, dataset)));
  } else {
    errors.push('curriculum/phase-2-production-ai/starter/data/evaluation.jsonl: dataset is missing');
  }
  return errors;
}
