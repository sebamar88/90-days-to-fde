# Day 1 reference example: Meridian intake discovery

> **Teaching example only.** Every detail below, including the five messages and worker interview, is fictional and synthetic. No Meridian customer research occurred. This is one defensible answer, not a prescribed product decision.

## Request

The fictional VP says: “We need an AI agent to read maintenance emails and create work orders automatically.” This is a proposed solution, not an agreed requirement.

## Users and workflow

- Service-desk coordinator: likely receives and routes requests; exact steps are unknown outside the invented example.
- Maintenance dispatcher/technician: may need a location, category, urgency, and access context; confirm which fields are actually required.
- Operations leader: wants a reliable service outcome; define the outcome with the people doing and receiving the work.

## Evidence versus interpretation

For the exercise only, imagine one worker shows five synthetic messages: four contain a building and issue type; one has no location. The worker says they re-enter the building and category into a work-order system.

- **Evidence within the fictional example:** 4/5 examples contain those fields; one interviewed fictional worker reports re-entry. Sample size is five messages, one worker, and an unspecified shift.
- **Interpretation:** re-entry might be avoidable effort. No duration or error data exists.
- **Unknown:** actual request volume, shift/building variation, urgency behavior, current integrations, policy, data permission, delay/error baseline, and the cost of misrouting.
- **Hypothesis to test:** requests lacking required fields take longer to route. Compare timestamps and missing-field patterns on an approved, representative sample.

## Problem statement

When maintenance requests arrive, the service desk needs to get complete and urgent requests to the correct team with required information, because delay or misrouting may affect facility operations. The current delay, error rate, and missing-field pattern are unknown.

## Options

1. Map the workflow and add a clearer intake form if missing fields dominate.
2. Compare deterministic field extraction/routing rules if fields and categories are stable.
3. Compare a model that drafts structured fields for human review if varied language defeats simpler approaches.
4. Keep the process human-led if volume is low, errors are costly, or evidence is insufficient.

Before selecting, agree on an outcome metric and source of truth, establish the baseline, measure quality and unsafe routing, and confirm data-use authorization. A safe experiment would compare rules and model drafts on approved representative examples with a human checking every result. No system writes to the work-order platform.

## Decision

**Investigate first.** Observe several roles and shifts, inspect field definitions and policy, and measure current completion time and correction rate. Stop considering AI if the workflow is already timely or a form/process change addresses the verified problem. Revisit after the evidence is reviewed with frontline staff and the metric owner.
