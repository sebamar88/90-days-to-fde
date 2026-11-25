# Tested curriculum labs

These labs provide a runnable reference implementation and automated checks for every curriculum phase. The Phase 2 FastAPI starter remains in its existing directory; the other phase modules live in this workspace and compose into the Phase 6 capstone.

## Run the complete suite

Requires Python 3.12 or newer. From this directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e "../phase-2-production-ai/starter[test]"
python -m pip install -e ".[test]"
python -m pytest tests "../phase-2-production-ai/starter/tests"
```

On macOS/Linux, activate with `source .venv/bin/activate`; the install and pytest commands are otherwise the same. The suite uses synthetic fixtures and local fakes. It does not require a cloud account, model API key, or external service.

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

Tests verify contracts, state transitions, safety properties, calculations, and reproducibility. Phase 1 tests can confirm that artifacts distinguish observed, simulated, assumed, synthetic, and unknown evidence; they cannot decide whether discovery was insightful. Human rubrics still assess judgment, communication, trade-offs, and the quality of learner-authored artifacts. Never label a simulated role-play as real customer validation.

The included modules are reference solutions for study and local execution. Learners should make changes in a branch or copy, add their own cases, and rerun the relevant phase suite. Every phase overview and daily lesson links back to its test instructions.
