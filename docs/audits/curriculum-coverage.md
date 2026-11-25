# Curriculum competency coverage

**Audit date:** 2026-11-25  
**Scope:** Days 1–90 as currently authored, including the Phase 2 starter and the shared lab references.  
**Purpose:** Identify what the current sequence asks learners to do, how much instruction/evidence it actually provides, and which topics merit core or optional treatment. This is a mapping of authored material, not evidence of learner mastery.

## Depth scale

- **Working reference:** The repository includes runnable code or tests for the competency.
- **Practice prompt:** A scenario, deliverable, and assessment ask learners to apply it, but instruction and examples are limited.
- **Mention:** The concept appears as a question or comparison without a substantial lesson or implementation.
- **Absent:** No dedicated learning activity was found in the 90-day sequence.

“Practice prompt” can still be useful, but it does not mean the topic is taught or learner-validated. Core means the transferable capability belongs in the free 90-day path; optional means an advanced lab should be added only when evidence of learner need justifies the extra technology or depth. Day 1 has since been expanded as an instructional reference; its editorial review and learner validation are still pending.

## Business and customer engineering

| Competency | Existing coverage | Depth | Gap / improvement | Placement |
|---|---|---|---|---|
| Customer discovery | Days 1–6, 14–15 | Reference draft + practice prompts | Day 1 now teaches problem framing, evidence classification, neutral questions, a worked example, option analysis, and a measurable rubric; later lessons still need independent review and learner feedback. | Core |
| Stakeholder interviews | Days 2, 4–6 | Practice prompt | Good non-leading interview activities; add a worked question/probe example and safe note-taking guidance. | Core |
| Process mapping | Days 3, 7, 11 | Practice prompt | Teach how to map actors, handoffs, exceptions, and evidence with one annotated example. | Core |
| Requirements engineering | Days 1, 6–7, 10, 13 | Practice prompt | Define functional/non-functional requirements, acceptance examples, traceability, and change handling. | Core |
| Business metrics | Days 7, 27–28, 47–48, 71 | Practice prompt | Formula and denominator exercises exist; teach baseline, counterfactuals, confounders, and guardrails. | Core |
| ROI | Days 27, 66, 71 | Mention | Cost model and hypothetical impact are requested; no worked ROI method or actual data. Add transparent sensitivity example, never an impact claim. | Core (basic); advanced finance optional |
| Technical feasibility | Days 8–11, 22, 61 | Practice prompt | Add a feasibility checklist across data, access, integration, latency, policy, and operating ownership. | Core |
| Scope negotiation | Days 9–10, 13–15, 42 | Practice prompt | Add a worked scope conversation and explicit scope-change / decision log pattern. | Core |
| Change management | Days 68–72 | Practice prompt | Training and ownership artifacts exist; explain adoption risks, accessibility, and feedback loops. | Core |
| Customer adoption | Days 69–74 | Practice prompt | No validated user research; maintain simulation labels and design a real consent-based follow-up study. | Core |
| Technical communication | Days 14, 30, 42, 45, 60, 74–75, 85–88 | Practice prompt | Repeated playbacks, demos, handoffs, and interview exercises; add a worked concise playback and review feedback. | Core |

## Software engineering

| Competency | Existing coverage | Depth | Gap / improvement | Placement |
|---|---|---|---|---|
| Advanced Python | Phase 2 typed models, deterministic baseline | Working reference (narrow) | No advanced language, packaging, profiling, or maintainability lesson. Add only the subset needed by the core service. | Core (targeted); rest optional |
| TypeScript | None | Absent | No current project need. Do not add a second language only to signal breadth; offer an optional port after demand. | Optional |
| Type safety | Phase 2 Pydantic models; Phase 3 tool/workflow contracts | Working reference (narrow) | Explain validation at trust boundaries and static versus runtime checks. | Core |
| Async programming | No async app or explicit lesson | Absent | Teach concurrency only if the service use case needs it; include cancellation/deadline behavior if added. | Optional/need-driven |
| Dependency injection | Day 19; `create_app(provider)` | Working reference | Add explanation of why injection improves deterministic tests and provider substitution. | Core |
| API design | Days 16, 19–21, 24; FastAPI starter | Working reference (narrow) | Teach error contracts, versioning, auth boundary, input limits, and backwards compatibility. | Core |
| Error handling | Days 19, 24–25, 34, 39, 52; 503/504 baseline | Working reference (partial) | Add unavailable/invalid-output contract tests and explain retry/terminal/ambiguous categories. | Core |
| Testing strategies | Days 17–29, 34–44, 46–60, 78–84; labs | Working reference (phase-specific) | Good test prompts, but thin examples; teach unit, contract, integration, regression, property, and failure injection as concepts. | Core |
| Clean architecture | Provider and work-order ports in Days 19, 24; narrow modules | Mention | No explicit dependency direction or boundary diagram lesson. Introduce only the small architecture visible in the reference app. | Core (basic) |
| Design patterns | Adapter/provider boundary; state machine; idempotency | Practice prompt | Teach patterns from concrete constraints, not pattern catalogues; no need for a separate survey. | Core (embedded) |
| System design | Days 11, 31–41, 53, 61–65, 85 | Practice prompt | Add one worked system-context and sequence design with explicit alternatives and failure paths. | Core |
| Distributed systems fundamentals | Days 25, 36, 39, 41, 52 | Practice prompt | Idempotency, ambiguous outcomes, concurrency, retry, and resume appear; add a coherent lesson on delivery guarantees and state ownership. | Core |

## Production LLM engineering

| Competency | Existing coverage | Depth | Gap / improvement | Placement |
|---|---|---|---|---|
| LLM fundamentals | Days 9, 20–21, 26–28 | Mention | No model behavior, probabilistic output, or baseline explanation. Add task-specific grounding, not a generic AI survey. | Core |
| Tokenization and inference | None | Absent | Not needed for current short-input service; add as optional performance/cost background if a workload requires it. | Optional |
| Structured outputs | Day 20 and Pydantic response model | Working reference (partial) | API contract exists; tests do not yet show malformed provider output/refusal/incomplete result handling. | Core |
| Tool calling | Days 31–35, 37, 43; deterministic registry | Practice prompt | There is no model-driven tool call. Teach proposal/validation/authorization separation; optional provider-specific tool-calling lab later. | Core (safe contract); provider execution optional |
| Context engineering | Days 21–23, 26 | Mention | No explicit instruction on context selection, trust, or source provenance. Add one short worked example if retrieval enters core. | Core (basic) |
| Context budgets | None | Absent | No long-context use case or measured token budget. | Optional |
| Memory and compaction | None | Absent | Current bounded workflow has explicit stored state, not conversation memory. Do not conflate the two; advanced agent lab only if needed. | Optional |
| Provider abstraction | Day 19; `IntakeProvider` protocol | Working reference | Clear narrow interface; document what semantics should not be hidden by a lowest-common-denominator abstraction. | Core |
| Model routing | None | Absent | No measured multi-model workload or router requirement. | Optional |
| Fallback strategies | Days 27, 29, 52; deterministic path and manual mode | Practice prompt / working baseline | Explain when fallback preserves task correctness versus creates misleading output. | Core |
| Caching | None | Absent | No demonstrated repeated computation or freshness policy; avoid adding cache without a workload. | Optional |
| Cost optimization | Days 27, 66; cost estimate lab | Working reference (arithmetic only) | No token counts or provider rate card in core; keep prices dated and estimates separated from measurements. | Core (method); provider pricing optional |
| Local model inference | Day 29 mentions optional Ollama; no local adapter | Mention | Provide a verified, optional path only after checking current local runtime docs and hardware assumptions. | Optional |

## Retrieval-augmented generation

| Competency | Existing coverage | Depth | Gap / improvement | Placement |
|---|---|---|---|---|
| Embeddings | None | Absent | No retrieval corpus or embedding need established. | Optional |
| Chunking strategies | None | Absent | No document corpus or chunk-size evaluation. | Optional |
| Retrieval metadata | Day 23 stable source IDs/version date in a fixture | Practice prompt | Teach source metadata, freshness, and provenance before considering an index. | Core (provenance); advanced indexing optional |
| Vector search | Days 22–23 compare/defer a vector database | Mention | Correctly discourages premature vector search; do not add until retrieval is justified by an approved source. | Optional |
| Hybrid retrieval | None | Absent | No benchmark or retrieval use case. | Optional |
| Reranking | None | Absent | No retrieval quality evidence to justify it. | Optional |
| Permission-aware retrieval | Day 22 raises access control as an option criterion | Mention | No actual tenant/user-scoped retrieval design or negative test. | Core only if retrieval is introduced; otherwise optional |
| Grounding | Day 23 source IDs/snippets, no-result path | Practice prompt | Good provenance requirement; add a worked citation and invalid/fabricated source example. | Core (basic) |
| Retrieval evaluation | Day 22 compares options; no retrieval metrics | Absent | No corpus or retrieval benchmark; add only with a retrieval exercise. | Optional |
| Knowledge freshness | Day 23 versions fixture entries and tests stale/missing | Practice prompt | Add a source owner, refresh trigger, and behavior when source version expires. | Core if retrieval exists; otherwise optional |

## Agentic systems

| Competency | Existing coverage | Depth | Gap / improvement | Placement |
|---|---|---|---|---|
| Deterministic workflow versus agent | Day 31 compares three designs | Practice prompt | Add a worked decision framework tied to uncertainty, reversibility, and error impact. | Core |
| Agent architecture | Days 31–45 | Practice prompt | Current implementation is deterministic and does not implement an LLM agent; state this clearly in phase marketing. | Core (boundaries); framework-specific agent optional |
| State machines | Days 35–36; Phase 3 workflow lab | Working reference | Explain persisted state versioning, concurrency, and transitions alongside the code. | Core |
| Tool contracts | Days 32–34; Phase 3 workflow | Working reference (narrow) | Add contract details for trusted identity, versioning, deadlines, and output minimization. | Core |
| LangGraph | None | Absent | No durable graph execution dependency/use case; add optional comparison only if the core state-machine lab is complete. | Optional |
| Multi-agent patterns | None | Absent | No business need, evaluation evidence, or reliability argument for multiple agents. | Optional / defer by default |
| Durable execution | Day 36 sketches resume; no durable orchestration engine | Mention | Teach durability requirements independent of vendor/framework; optional implementation later. | Core (concept); implementation optional |
| Checkpointing | Day 36 serialized synthetic resume fixture | Practice prompt | Add checkpoint versioning/compatibility and replay safety. | Core (basic) |
| Human-in-the-loop | Days 10, 24–25, 35, 41–45; review_required is enforced in Phase 2 | Working reference (boundary) | Explain approval semantics, expiration, actor identity, and explicit non-approval. | Core |
| MCP servers and clients | None | Absent | No MCP integration or tool server exists. Teach protocol only if it serves an interoperability scenario; otherwise optional. | Optional |
| MCP authorization | None | Absent | Authorization is taught for local tools, not MCP. Add only with MCP; verify protocol version/security docs at that time. | Optional |
| Agent-to-Agent communication | None | Absent | No multi-agent or cross-agent customer need. | Optional |
| Enterprise integration | Days 8, 11, 24–25, 32–41, 61–68; in-memory sandbox | Practice prompt / partial reference | No actual customer connector; integration remains intentionally synthetic. Teach contract, identity, and failure ownership. | Core |
| Idempotency | Days 25, 39, 41; Phase 3 workflow tests | Working reference | Add a worked key scope/payload mismatch case and clarify persistence/retention boundary. | Core |
| Partial failure recovery | Days 39, 44, 52, 58, 65, 73, 81; retry and state tests | Practice prompt / partial reference | Strong topic coverage; teach ambiguous outcomes and reconciliation as one end-to-end worked sequence. | Core |

## Evaluation and security

| Competency | Existing coverage | Depth | Gap / improvement | Placement |
|---|---|---|---|---|
| Evaluation-driven development | Days 18, 28, 43, 46–49, 80 | Practice prompt / deterministic baseline | Add a worked loop from requirement to fixture, metric, failure, and regression. | Core |
| Golden datasets | Days 18, 28, 46–49 | Practice prompt | Existing eight cases have no holdout split. Add a documented development/holdout policy with synthetic fixtures. | Core |
| Deterministic evaluation | Days 28, 43, 46–49; tests | Working reference (small) | Tests are useful but set is tiny and reused. Report denominators and limitations. | Core |
| LLM-as-a-Judge | None | Absent | No requirement for judge-based scoring. Do not add by default; if added, compare with human labels. | Optional |
| Judge calibration and bias | None | Absent | Depends on a judge use case; requires separate calibration and disagreement study. | Optional |
| RAG evaluation | None | Absent | No retrieval implementation to evaluate. | Optional |
| Agent trajectory evaluation | Day 43 scores tool choice/arguments/policy; no generated trajectory | Mention | Add trajectory metrics only if a model-directed workflow is actually implemented. | Optional |
| Regression testing | Days 28, 49, 80; tests | Working reference (small) | Separate fixed holdout from cases added during development to avoid tuning on all tests. | Core |
| Adversarial testing | Days 43, 53–57; injection fixtures | Practice prompt / security tests | Add a simple deterministic threat-to-test trace; no claim of exhaustive attack coverage. | Core |
| Prompt injection | Day 54; input is treated as untrusted text | Practice prompt | The lesson says app controls must enforce boundaries, but add a worked example and test harness. | Core |
| Excessive agency | Days 9–10, 31–35, 37, 43–45 | Practice prompt | Good control concepts; no model-driven agent, so distinguish risk analysis from demonstrated mitigation. | Core |
| Least privilege | Days 32, 37, 53, 57; Phase 3 actor scopes | Working reference (synthetic) | Add least-privilege examples and ensure identity context cannot be supplied by model text. | Core |
| RBAC | Days 37, 57, 79; Phase 3 tests | Working reference (small) | State test matrix and maintain human-owned authorization decisions. | Core |
| Data isolation | Days 22, 37, 53, 55, 57 | Practice prompt | Tenant/region isolation is discussed; no persistent multi-tenant datastore exists. | Core (concept); implementation optional |
| Secrets management | Days 55–56, 62; release gate lab | Practice prompt / checklist | No real cloud secret store is implemented. Keep environment secrets out of fixtures and teach rotation/ownership conceptually. | Core |
| Privacy | Days 4, 8, 40, 50, 55, 70, 87; redaction test | Practice prompt / partial reference | Add purpose, consent, retention, deletion, and evidence boundaries; jurisdiction-specific legal advice is out of scope. | Core |
| Auditability | Days 40, 53, 59; allowlisted audit-event test | Working reference (schema only) | Tie traceability to action, actor, policy version, and preview hash; document retention/immutability limits. | Core |

## Infrastructure and operations

| Competency | Existing coverage | Depth | Gap / improvement | Placement |
|---|---|---|---|---|
| Docker | Day 63 asks for a clean environment/container option | Mention | No Dockerfile or hands-on container lab. Add only when a container simplifies reproducibility. | Optional |
| CI/CD | Days 56, 64; three current GitHub Actions workflows | Working reference (CI only) | CI does not enforce the Phase 2 lock; no deployment job (correctly). Teach pipeline permissions and immutable artifacts. | Core |
| Infrastructure as code | None | Absent | No real infrastructure is deployed. | Optional |
| Terraform | None | Absent | No customer/cloud requirements support a Terraform module yet. | Optional |
| Cloud deployment | Days 61–65, 82 compare/document deployment, no live deployment | Practice prompt | The deployment is explicitly hypothetical/local; no cloud endpoint is implemented. | Core (decision process); live cloud optional |
| AWS | None | Absent | No provider-specific need; no paid account should be required. | Optional |
| OpenTelemetry | Day 50 asks for trace spans, but no SDK/exporter | Mention | Teach trace context and privacy first; add an optional SDK lab with exact current docs when needed. | Core (concept); vendor/API lab optional |
| Distributed tracing | Days 50, 81 | Practice prompt | No runnable trace implementation or end-to-end example. | Core |
| LLM observability | Days 26–28, 40, 50 | Practice prompt | No provider observability implementation; define minimum privacy-safe signal set and cost metadata. | Core (concept) |
| SLOs and SLIs | Day 51; Phase 5 release gate | Practice prompt / calculation | Teach good event populations, windows, and error budgets before hypothetical target values. | Core |
| Reliability | Days 25, 34–41, 44, 49, 52, 57–60 | Practice prompt / partial tests | Strongly represented across failure handling; pair prompts with worked examples and code. | Core |
| Incident response | Days 58, 67, 73, 81 | Practice prompt | Tabletop scenarios; no real production incident. Clarify containment roles and evidence handling. | Core |
| Capacity planning | Days 27, 66 | Practice prompt / arithmetic lab | No traffic observations; teach sensitivity and queueing assumptions without pretending to forecast. | Core (method) |
| Multi-tenancy | Days 37, 53, 57 discuss roles/regions | Mention | No tenant storage or isolation code. Teach as risk boundary; implementation depends on product architecture. | Core (concept); implementation optional |
| Rollback strategies | Days 65, 73, 75 | Practice prompt | Explain immutable release identity and why irreversible external writes require reconciliation rather than rollback. | Core |

## Career readiness

| Competency | Existing coverage | Depth | Gap / improvement | Placement |
|---|---|---|---|---|
| System design interviews | Days 85, 88 | Practice prompt | No timed worked interview or evaluation rubric for system-design reasoning. | Core |
| Architecture defense | Days 12, 30, 45, 60, 75, 85 | Practice prompt | ADR, review packet, and trade-off brief; add a worked claim → constraint → option → evidence defense. | Core |
| Technical demonstrations | Days 14, 30, 45, 60, 75, 86 | Practice prompt | Demo scripts are requested; add success, denial, failure, and reset example without implying production deployment. | Core |
| Portfolio development | Days 76–90, especially 87–89 | Practice prompt | Portfolio artifacts are outlined, but learner claims need explicit evidence links and limitations. | Core |
| Customer-facing communication | Days 4–5, 14–15, 42, 69, 74–75, 83, 86–89 | Practice prompt | Simulation-heavy; no real customer feedback. Preserve clear evidence labels. | Core |
| Technical proposals | Days 10, 14, 30, 61, 72, 75, 85 | Practice prompt | Teach a concise proposal structure with options, evidence, constraints, and decision request. | Core |
| Production incident scenarios | Days 44, 58, 67, 73, 81 | Practice prompt | Rehearsal is fictional; use as judgment practice, never as a production credential. | Core |

## Coverage conclusions

1. The sequence covers discovery, safety, evaluation, integration, operations, and customer communication as **activities**, but it currently teaches many topics through brief assignments rather than reusable instruction.
2. The Phase 2 app and phase-specific labs make a useful small synthetic spine; they do not implement the entire curriculum's listed technologies. The core path should stay focused on transferable contracts, state, evaluation, and safe delivery.
3. Defer LangGraph, multi-agent orchestration, MCP/A2A, vector databases, rerankers, Terraform, AWS, and TypeScript until a learner outcome or partner/user feedback justifies an optional lab.
4. Prioritize next: Day 1 reference lesson; a prerequisite/content contract; a Phase 2 provider-contract and evaluation holdout improvement; then one taught-and-coded end-to-end exercise per phase based on learner feedback.
5. Public job descriptions can illustrate employer-specific FDE expectations, not define a universal role. For example, OpenAI describes discovery, scoping, design, build, and rollout; Palantir describes a customer technical/operational outcome mandate. The lesson should state that titles and boundaries vary by company.

## Sources checked

- [OpenAI Forward Deployed Engineer role](https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/), checked 2026-11-25.
- [Palantir explanation of software engineer and forward-deployed software engineer roles](https://www.palantir.com/careers/students-and-early-talent/), checked 2026-11-25.
- [GOV.UK user research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery), checked 2026-11-25.
- [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), checked 2026-11-25.
