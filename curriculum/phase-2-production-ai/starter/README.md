# Meridian intake starter

This starter backs Phase 2. It runs locally with a deterministic provider and synthetic data; no API key, hosted model, or customer system is required. The included code is a teaching baseline, not a production deployment.

## Quickstart

Requires Python 3.12 or newer and [uv](https://docs.astral.sh/uv/).

```bash
uv sync --locked --extra test
uv run --locked pytest
uv run --locked uvicorn meridian_intake.app:app --reload
```

Send a synthetic request to `POST http://127.0.0.1:8000/v1/intake/suggestions`:

```json
{"request_id":"demo-001","text":"Building 12: active leak under the sink in the break room."}
```

Every returned suggestion requires human review. The local fake work-order interface is not connected to an external system. Model providers and local inference are optional exercises implemented behind `IntakeProvider`.

## Contents

- `src/meridian_intake/` — typed request/response models, rule provider, provider boundary, and HTTP app
- `data/evaluation.jsonl` — synthetic labeled examples
- `tests/` — automated checks for the starter contract and baseline

The fixture labels are assessment examples, not claims about real maintenance requests or expected customer prevalence.

The `uv.lock` file pins the resolved Python environment. Keep it synchronized with `pyproject.toml` and run `uv lock --check` before submitting. The evaluation set separates four development cases from four holdout cases. Holdout examples are public teaching data, not secret benchmark data; do not iteratively tune against them and claim independent generalization. The set is too small and synthetic to support real-world performance claims.

API tests include invalid input rejected before provider invocation, provider timeout/unavailability, and malformed provider output. The endpoint translates provider contract failures into bounded HTTP errors without exposing raw provider error payloads.
