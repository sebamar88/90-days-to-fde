---
day: 16
phase: 2
status: Ready
title: Set up the service and contract
estimated_effort: 75–100 minutes
---

# Day 16 — Set up the service and contract

## Why this matters

AI experiments become hard to compare when they have no stable interface or repeatable environment. Start with a small service contract and a clean local setup before adding model dependencies.

## Scenario

The Phase 1 packet chose a draft-only intake helper. A coordinator submits one synthetic maintenance message and receives suggested fields plus explicit review flags. The service must not write to Meridian systems.

## Outcomes

- Create an isolated Python environment and reproducible project layout.
- Define request/response contracts independently of the model provider.
- Expose one local endpoint and test it without network access.

## Exercise

Start from `starter/`. Create a virtual environment, install the project and test extras, then run the FastAPI app locally. Inspect `IntakeRequest` and `IntakeSuggestion`; document field meanings, size limits, and what is a suggestion versus a verified fact. Send one synthetic request to `POST /v1/intake/suggestions` and confirm the response has no write capability.

## Deliverable

A runnable local app, a short interface contract, and one request/response example using synthetic data.

## Assessment

Pass when the app starts from a fresh environment, rejects an empty or oversized request, returns a typed draft, and has no outbound model or work-order call on the default path.

## Reflection

Which contract decision will let you swap providers later without changing the coordinator-facing API?

## References

- [Python `venv`](https://docs.python.org/3/library/venv.html)
- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [Starlette TestClient](https://www.starlette.io/testclient/)
## Automated lab

Run the [Phase 2 test suite](../phase-2-production-ai/starter/tests/) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
