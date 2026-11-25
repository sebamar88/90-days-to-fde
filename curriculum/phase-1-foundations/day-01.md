---
schema_version: 1
id: day-01
day: 1
phase: 1
locale: en
slug: from-request-to-business-outcome
title: From request to business outcome
description: An FDE is often handed a proposed solution before anyone has agreed on the problem.
publication_status: preview
review_status: unreviewed
test_coverage: phase-lab
learner_validation_status: not-validated
content_type: business-discovery-exercise
difficulty: foundational
duration:
  min: 60
  max: 90
prerequisites: []
objectives:
  - Separate the requested feature from the outcome it might serve.
  - Name what is known, assumed, and still unknown.
  - Write a neutral problem statement that does not commit to AI.
tags:
  - phase-1
  - problem-framing
skills:
  - problem-framing
---

# Day 1 — From request to business outcome

## Why this matters

An FDE works across software engineering and customer delivery. The role name varies by employer: some teams emphasize building with a customer, while others emphasize integrating software into a customer's operational environment. Across those versions, the shared responsibility is to understand the real work, make a useful technical change, and learn whether that change produced the intended outcome. This is different from treating a feature request as a complete specification.

For example, “build an AI agent that creates work orders” is a proposed solution. It does not tell us whether work orders are delayed, whether staff already enter them elsewhere, whether the source messages contain enough information, or what errors would cost. Discovery makes those unknowns visible before architecture makes them expensive.

Do not confuse discovery with delaying delivery. A focused discovery pass produces testable requirements, a safe first slice, and evidence that can change the plan. It should end with a decision: proceed, gather a specific missing fact, choose a simpler approach, or stop.

## Role comparison

| Role (common emphasis) | Typical center of gravity | Evidence of success |
|---|---|---|
| Forward Deployed Engineer | Builds and adapts software in close contact with a customer, often across discovery, integration, and delivery. | A working change fits the customer context and has evidence of operational value. |
| Product Software Engineer | Builds and operates a product capability for a broader, evolving user base. | Maintainable product behavior, reliability, and user or business outcomes at product scale. |
| Applied AI Engineer | Applies machine learning or generative AI to a defined product or workflow problem. | Measured task performance, safe integration, and operating behavior against a baseline. |
| Solutions Architect | Shapes a solution across system boundaries, requirements, and platform constraints; scope varies by organization. | A feasible design that meets stated requirements and operational constraints. |
| Technical Consultant | Advises or implements around a customer's technology and process context; delivery authority varies. | A useful recommendation or implementation adopted within the agreed engagement. |

These roles overlap. OpenAI and Palantir describe their own FDE roles in their hiring materials; neither source defines every employer's title. An FDE may do product engineering or applied AI, but customer discovery and delivery context are often more central.

## Scenario

Meridian Facilities' VP of Operations says: “We need an AI agent to read maintenance emails and create work orders automatically.” You have not yet met the service desk or seen the current process. This is a fictional scenario; the quote is a prompt for analysis, not customer evidence.

## Prerequisites and preparation

No AI or discovery framework is assumed. Bring a Markdown editor and allow 60–90 minutes as an estimate: 20 minutes to learn the concepts, 15 minutes for the guided pass, 25–40 minutes for the independent brief, and time for reflection. The reference lab is optional support, not a prerequisite. You can complete the lesson with a plain-text editor; screen-reader users can navigate by headings and tables, and may rewrite tables as labeled lists without changing the assessment criteria.

At the start, the only fact is that the VP made this request. Everything else below is a hypothesis until someone supplies evidence:

| Statement | Classification | Why |
|---|---|---|
| The VP requested an AI agent that reads maintenance email. | Observed statement | It is the exact request provided in the scenario. |
| Work orders are delayed. | Unknown | No timing or process evidence has been shared. |
| The service desk manually copies every email. | Unknown | We have not observed the work or interviewed staff. |
| Automatic creation will reduce operating cost. | Hypothesis | No baseline, volume, or cost data supports this yet. |
| A model is required. | Proposed solution | Rules, form changes, routing, or process changes could address the need. |

Use these terms consistently:

- **Observation:** a direct account, event, or record, with source and context. The VP's exact request is an observed statement in this fictional scenario, not evidence of the underlying operational problem.
- **Evidence:** observations or reliable records relevant to a claim; include provenance, sample, and limitations.
- **Assumption:** an unverified belief temporarily used to plan; name how it could be checked.
- **Hypothesis:** a specific, falsifiable expectation, such as “requests missing a location take longer to route.” It remains unproven until tested.
- **Constraint:** a boundary the design must respect, such as an existing identity system, policy, budget, or response-time limit. Confirm it with an accountable source.
- **Requirement:** an agreed, testable condition for success, including who accepted it and how it will be measured.
- **Outcome:** a change in the user's or organization's work that matters; distinguish it from system output volume.
- **Solution:** one possible way to meet requirements, not a fact about the problem.

A customer request can be evidence of a stakeholder's preference, but it does not automatically establish a business requirement.

## Explanation

### Start with the work and its impact

Ask who experiences the problem, what they are trying to do, when the difficulty occurs, what they do now, and what happens if nothing changes. Ask for a recent concrete example before asking someone to estimate a general pattern. “Walk me through the last maintenance request” usually reveals more than “Would an AI agent help?”

Avoid leading questions (“Would automation save time?”) and questions that ask the stakeholder to design (“What should the agent do?”). Prefer neutral prompts:

1. “What happened the last time a request was delayed?”
2. “Who touched the request from the first message to the work order?”
3. “Where did the handoff wait, and how do you know?”
4. “What information did the technician need that was missing?”
5. “What should happen when the message is unclear or urgent?”
6. “What evidence would convince you that the process improved?”

Ask permission before recording or collecting sensitive operational data. Record the role and context, not unnecessary personal details. Separate direct quotes from your interpretation, and confirm important interpretations with the people doing the work. A manager can describe goals; frontline staff can expose exceptions and workarounds. Neither view replaces the other.

### Write a useful problem statement

**Weak:** “Meridian needs an AI agent to create work orders from email.” This repeats the preferred implementation and invents a need.

**Stronger, still a hypothesis:** “When maintenance requests arrive, the service desk needs to route complete and urgent requests to the right team with the required information, because delayed or misrouted work may affect facility operations. The current delay, error rate, and missing-field pattern are unknown.” This identifies a user, job, and possible impact without treating them as proven facts. Validate each clause with frontline staff and records before turning it into a requirement.

### Turn discovery into a decision

Write a solution-neutral problem statement:

> When **[situation]**, **[user]** needs to **[job]**, because **[impact]**. Today, **[evidence or explicit unknown]**.

Then write measurable success conditions, a baseline plan, the constraints, and the riskiest assumptions. For Meridian, a useful first metric might be the share of requests with a complete work order within a defined time window. That is only a candidate metric: the team must agree on the window, source of truth, and baseline before claiming improvement. Track safety and quality too, such as incorrect emergency routing or missing required fields. A faster workflow that silently misroutes urgent requests is not successful.

Discovery also tests whether AI belongs in the first slice. Compare at least three options: improve the intake form or process, use deterministic rules for clear cases, and use a model to propose structured fields for ambiguous language. Compare them on expected benefit, error cost, data availability, integration effort, auditability, and fallback. Start with the simplest option that can test the key assumption. A model is justified only if representative examples show that it handles language variation better than a simpler baseline and the remaining errors can be safely reviewed.

| Option | Useful when | Main trade-off | Evidence to collect first |
|---|---|---|---|
| Process or form change | Missing information or handoffs cause most rework. | Requires workflow adoption and ownership. | Observe where information is lost; test whether a required field or clearer handoff changes it. |
| Deterministic rules | Inputs are structured and categories are stable. | Rules can become brittle as formats and exceptions grow. | Compare a rules baseline on representative, held-out examples; inspect error slices. |
| Model-assisted draft | Free text varies and structured fields can be suggested for human review. | Uncertain outputs, data handling, latency, and cost need controls. | Compare against rules and human labels; test ambiguity, safety, and abstention. |
| Human-led workflow | Volume is low, consequence is high, or evidence is insufficient. | Manual effort remains; consistency needs support. | Measure current workload and identify whether a bounded assist is worthwhile. |

### Worked example: keep facts separate from hypotheses

Suppose a service-desk worker later shows five recent messages. Four already contain a building and issue type; one lacks a location. The worker reports that they retype the building and category into the work-order system. These are observations from a tiny sample, not proof about the whole operation. A careful brief would say:

- **Evidence:** In five observed messages, four included a building and issue type; the worker re-entered those fields. Sample: five messages, one worker, one shift.
- **Interpretation:** Re-entry may create avoidable effort. We have not measured time or error rate.
- **Unknown:** Daily volume, variation by building, existing automation, urgency handling, and permission to use email content.
- **Next check:** Observe more shifts, time the current steps, inspect the existing work-order fields, and ask staff what happens for urgent or incomplete requests.
- **Candidate experiment:** On a representative and approved sample, compare a manual rule baseline with a model that drafts fields only. A reviewer corrects every result; nothing writes to the work-order system.

The small sample can motivate a next step. It cannot support a production estimate, a claim of savings, or a decision to automate writes.

## Outcomes

- Separate the requested feature from the outcome it might serve.
- Name what is known, assumed, and still unknown.
- Write a neutral problem statement that does not commit to AI.

## Exercise

### Guided exercise

Use only the explicitly hypothetical five-message example below to practice separating observation from interpretation. Treat its data as invented for teaching; do not describe it as a Meridian customer finding. Fill the [problem brief template](../../templates/problem-brief.md). Compare your result with the [reference example](solutions/day-01-reference.md) only after making your own first pass.

### Independent challenge

Start again using only the VP's original request; remove the five-message example from the brief. Create `problem-brief.md` with the following sections:

1. **Request:** quote the VP exactly and label it as a proposed solution.
2. **Users and workflow:** list at least two affected roles and the steps you would observe; mark unknown steps explicitly.
3. **Evidence, assumptions, and requirements:** create separate tables. Do not promote a hypothesis into a requirement.
4. **Problem statement:** use the solution-neutral format above. Include “unknown” where evidence is missing.
5. **Questions:** write at least five neutral interview or observation prompts, including one about exceptions and one about safety.
6. **Success and guardrails:** propose one outcome metric, one quality/safety metric, how to establish a baseline, and who must approve the definition.
7. **Alternatives:** compare process/form change, deterministic rules, and model-assisted drafting. State what evidence would make you choose each.
8. **Next step:** recommend proceed, investigate, use a simpler approach, or stop, with the evidence needed to revisit the decision.

In both cases, label the scenario fictional and do not invent customer facts. Do not propose autonomous work-order creation as the first experiment.

### Optional advanced challenge

Design a small, privacy-safe sampling plan that could distinguish whether delay comes from missing information, queue ownership, or system integration. Specify what data is necessary, what should be excluded, who can authorize access, and what result would stop the AI investigation.

## Knowledge check

1. **The VP asks for an AI agent. Is that a requirement?** No. It is evidence of the VP's preferred solution. A requirement needs an agreed, testable success condition.
2. **A worker reports that requests are often delayed. What is that?** A stakeholder report and a hypothesis to investigate. Record who said it and context; seek records or observation before generalizing.
3. **When is a model a reasonable first slice?** When representative evidence shows simpler options miss an important need, model suggestions improve a defined task, and errors can be reviewed safely.
4. **What does a faster completion time prove?** Only a change in that metric under the measurement conditions. Check quality, routing safety, baseline comparability, and unintended effects too.

## Common mistakes

- Rewriting the requested feature as though it were the business problem.
- Treating a manager's opinion or a tiny sample as a population-wide fact.
- Confusing an output metric (messages processed) with an outcome (work reaches the correct team sooner).
- Choosing AI before comparing process and deterministic alternatives.
- Collecting more customer data than the question requires or skipping consent and policy checks.
- Automating consequential writes before measuring error cost and providing review and recovery.

## Deliverable

Submit the brief plus a short decision note (maximum 150 words). The problem statement must not prescribe a technology. Each evidence statement must have a source or be labeled unknown. Each recommendation must identify what would change your mind. For an actual customer engagement, obtain consent before observing or collecting operational content and follow the customer's data-handling requirements.

## Assessment

Score each criterion 0 (missing/unsafe), 1 (partial or unsupported), or 2 (clear and evidence-based):

| Criterion | 2-point evidence |
|---|---|
| Request versus problem | The quote is preserved and labeled as a solution proposal. |
| Evidence discipline | Facts have a source; assumptions and unknowns are explicit. |
| User and workflow | At least two roles and a concrete observation plan are included. |
| Outcome and measurement | A candidate metric, baseline method, and quality/safety guardrail are defined without fabricated numbers. |
| Option quality | Process, rules, and model-assisted options have trade-offs and decision evidence. |
| Safe discovery | Questions are neutral; privacy/consent and human review are addressed. |

**Pass:** at least 9/12, with no zero for evidence discipline or safe discovery. Revise otherwise. This rubric assesses the artifact, not the learner's readiness for customer deployment. A reviewer should leave one evidence-based comment and one next question.

## Reflection

What would you need to observe before claiming the proposed system could reduce delay? Which finding would lead you to recommend no AI at all?

## References

- OpenAI, [Forward Deployed Engineer role description](https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/) (employer-specific role example; accessed 2026-11-25).
- Palantir, [Software Engineering and Forward Deployed Software Engineering](https://www.palantir.com/careers/students-and-early-talent/) (employer-specific role comparison; accessed 2026-11-25).
- AWS, [Solutions Architect Associate exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) (one employer-independent example of assessed role scope; accessed 2026-11-25).
- UK Government Service Manual, [User research in discovery](https://www.gov.uk/service-manual/user-research/user-research-in-discovery) (accessed 2026-11-25).
- UK Government Service Manual, [Taking notes and recording user research sessions](https://www.gov.uk/service-manual/user-research/taking-notes-and-recording-user-research-sessions) (accessed 2026-11-25).
- NIST, [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) (accessed 2026-11-25).
## Automated lab

Run the [Phase 1 test suite](../labs/tests/test_phase1_discovery_packet.py) alongside the assessment. The tests check the phase reference lab; use the lesson rubric for judgment, communication, and other qualitative evidence.
