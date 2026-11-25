# Tested curriculum labs

These labs provide a runnable reference implementation and automated checks for every curriculum phase. The Phase 2 FastAPI starter remains in its existing directory; the other phase modules live in this workspace and compose into the Phase 6 capstone.

## Run the complete suite

Requires Python 3.12 or newer and [uv](https://docs.astral.sh/uv/). From this directory:

```powershell
uv sync --locked --extra test
uv run --locked pytest tests
```

The shared lab lockfile includes the Phase 2 starter as a local path dependency so imports are consistent without running its tests twice. Run the Phase 2 starter suite separately from `curriculum/phase-2-production-ai/starter/` with `uv sync --locked --extra test && uv run --locked pytest`. Both suites use synthetic fixtures and local fakes; neither needs a cloud account, model API key, or external service.

## Phase-to-test map

| Phase | Days | Reference lab | Automated checks |
|---|---:|---|---|
| 1 — Discovery | 1–15 | `src/meridian_fde_labs/phase1.py` validates the discovery packet's structure and evidence labels. | `tests/test_phase1_discovery_packet.py` |
| 2 — Production AI | 16–30 | `../phase-2-production-ai/starter/src/meridian_intake/` provides the API, typed contract, deterministic baseline, and synthetic evaluation data. | `../phase-2-production-ai/starter/tests/` |
| 3 — Agentic workflow | 31–45 | `src/meridian_fde_labs/phase3.py` implements scoped lookup, approval, workflow state, replay, and bounded retry behavior. | `tests/test_phase3_workflow.py` |
| 4 — Reliability and security | 46–60 | `src/meridian_fde_labs/phase4.py` scores slices and emits allowlisted audit events. | `tests/test_phase4_evaluation_security.py` |
| 5 — Delivery | 61–75 | `src/meridian_fde_labs/phase5.py` checks deployment evidence, release blockers, and cost arithmetic. | `tests/test_phase5_delivery.py` |
| 6 — Capstone | 76–90 | `src/meridian_fde_labs/phase6.py` composes the Phase 2 baseline with the Phase 3 workflow and Phase 4–5 gates. | `tests/test_phase6_capstone.py` |

## Assessment boundary

Tests verify contracts, state transitions, safety properties, calculations, and reproducibility. Snapshot restoration checks internal consistency and preview hashes; it is not authenticated durable storage and does not protect against an attacker who can rewrite the entire snapshot and recompute hashes. Phase 1 tests can confirm that artifacts distinguish observed, simulated, assumed, synthetic, and unknown evidence; they cannot decide whether discovery was insightful. Human rubrics still assess judgment, communication, trade-offs, and the quality of learner-authored artifacts. Never label a simulated role-play as real customer validation.

The included modules are reference solutions for study and local execution. Learners should make changes in a branch or copy, add their own cases, and rerun the relevant phase suite. Every phase overview and daily lesson links back to its test instructions.
