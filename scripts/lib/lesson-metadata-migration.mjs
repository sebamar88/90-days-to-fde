import { parseFrontmatter } from './curriculum-validator.mjs';
import { stringify } from 'yaml';

const skills = [
  'problem-framing', 'stakeholder-mapping', 'process-mapping', 'interview-design', 'customer-interview',
  'evidence-analysis', 'metric-design', 'data-governance', 'ai-fit-assessment', 'project-scoping',
  'system-context', 'architecture-decision', 'acceptance-criteria', 'customer-playback', 'discovery-synthesis',
  'api-contracts', 'deterministic-classification', 'evaluation-data', 'provider-abstraction', 'structured-output',
  'safe-abstention', 'retrieval-selection', 'grounding', 'integration-boundaries', 'idempotency-and-retry',
  'reproducible-evaluation', 'cost-latency', 'model-evaluation', 'reproducible-development', 'solution-communication',
  'autonomy-design', 'tool-contracts', 'data-access', 'contract-validation', 'human-approval',
  'durable-state', 'authorization', 'system-integration', 'partial-failure-recovery', 'auditability',
  'idempotent-operations', 'stakeholder-communication', 'tool-evaluation', 'failure-injection', 'architecture-defense',
  'evaluation-datasets', 'metric-design', 'error-analysis', 'regression-testing', 'observability',
  'service-level-objectives', 'degraded-mode', 'threat-modeling', 'prompt-injection-defense', 'privacy-engineering',
  'supply-chain-security', 'access-control', 'incident-response', 'risk-review', 'release-readiness',
  'deployment-architecture', 'secret-management', 'reproducible-deployment', 'ci-cd-security', 'release-rollback',
  'cost-capacity', 'incident-runbooks', 'service-ownership', 'change-management', 'feedback-governance',
  'impact-measurement', 'readiness-gates', 'incident-response', 'customer-handoff', 'delivery-review',
  'capstone-scoping', 'risk-prioritization', 'integration-engineering', 'secure-authorization', 'final-evaluation',
  'operations-validation', 'deployment-reproducibility', 'usability-testing', 'iterative-improvement', 'architecture-communication',
  'technical-demonstration', 'portfolio-evidence', 'interview-communication', 'career-readiness', 'professional-retrospective',
];

function contentType(day) {
  if ([15, 30, 45, 60, 75, 90].includes(day)) return 'phase-assessment';
  if (day <= 10 || day === 14) return 'business-discovery-exercise';
  if (day >= 11 && day <= 13) return 'architecture-challenge';
  if (day === 22 || [31, 38, 53, 59, 61, 85].includes(day)) return 'architecture-challenge';
  if ([42, 44, 58, 68, 69, 72, 73, 74, 83, 86, 88].includes(day)) return 'enterprise-simulation';
  if (day >= 76) return 'capstone-milestone';
  return 'guided-technical-lab';
}

function firstSection(markdown, title) {
  const lines = markdown.split(/\r?\n/);
  const start = lines.findIndex((line) => new RegExp(`^##\\s+${title}\\s*$`, 'i').test(line));
  if (start < 0) return '';
  let end = start + 1;
  while (end < lines.length && !/^##\s+/.test(lines[end])) end += 1;
  return lines.slice(start + 1, end).join('\n').trim();
}

function descriptionFrom(markdown, title) {
  const why = firstSection(markdown, 'Why this matters');
  const paragraph = why.split(/\r?\n\s*\r?\n/)[0]?.replace(/\s+/g, ' ').trim() ?? '';
  const sentence = paragraph.match(/^.*?[.!?](?=\s|$)/)?.[0] ?? paragraph;
  if (sentence.length >= 20 && sentence.length <= 200) return sentence;
  const fallback = `Practice ${title} in the fictional Meridian Facilities scenario.`;
  return fallback.length <= 200 ? fallback : `${fallback.slice(0, 197).trimEnd()}...`;
}

export function migrateLessonFrontmatter(markdown, file = '<memory>') {
  const parsed = parseFrontmatter(markdown, file);
  if (parsed.errors.length) throw new Error(parsed.errors.join('\n'));
  const legacy = parsed.metadata;
  if (legacy.schema_version === 1) return markdown;

  const day = legacy.day;
  if (!Number.isInteger(day) || day < 1 || day > 90) throw new Error(`${file}: legacy lesson day must be an integer from 1 to 90`);
  if (legacy.phase !== Math.ceil(day / 15)) throw new Error(`${file}: legacy phase does not match day ${day}`);
  const skill = skills[day - 1];
  if (!skill) throw new Error(`${file}: no skill mapping exists for day ${day}`);

  const effortValues = [...String(legacy.estimated_effort ?? '').matchAll(/\d+/g)].map((match) => Number(match[0]));
  if (effortValues.length !== 2 || effortValues[0] < 15 || effortValues[1] > 240 || effortValues[0] > effortValues[1]) {
    throw new Error(`${file}: estimated_effort must contain a valid effort range in minutes`);
  }
  const objectives = firstSection(parsed.body, 'Outcomes')
    .split(/\r?\n/)
    .map((line) => line.trim().replace(/^[-*]\s+/, ''))
    .filter(Boolean);
  if (objectives.length < 2 || objectives.length > 5) throw new Error(`${file}: expected 2–5 objective bullets in the Outcomes section`);

  const title = legacy.title;
  const slug = title
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[—–]/g, ' ')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
  const phase = legacy.phase;
  const metadata = {
    schema_version: 1,
    id: `day-${String(day).padStart(2, '0')}`,
    day,
    phase,
    locale: 'en',
    slug,
    title,
    description: descriptionFrom(parsed.body, title),
    publication_status: 'preview',
    review_status: 'unreviewed',
    test_coverage: 'phase-lab',
    learner_validation_status: 'not-validated',
    content_type: contentType(day),
    difficulty: phase === 1 ? 'foundational' : phase <= 3 ? 'intermediate' : 'advanced',
    duration: { min: effortValues[0], max: effortValues[1] },
    prerequisites: day === 1 ? [] : [`day-${String(day - 1).padStart(2, '0')}`],
    objectives,
    tags: [`phase-${phase}`, skill],
    skills: [skill],
  };

  return `---\n${stringify(metadata, { lineWidth: 0 })}---\n${parsed.body}`;
}
