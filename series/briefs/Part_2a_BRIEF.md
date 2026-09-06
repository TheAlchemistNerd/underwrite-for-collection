# Part 2a Brief

## Working title

**Temporal Evidence, Behavioural Signals and Point-in-Time Feature Engineering**

## Scale

- Full-source target: 7,191 words.
- Editorial-prose target: 6,348 words.

## Purpose

Part 2a defines the evidence architecture through which fragmented MSME operations become reproducible, explainable and time-correct risk information inside a bank-controlled boundary.

## Governing question

What must be observed, timestamped, governed and transformed before behavioural evidence can responsibly inform MSME credit decisions?

## Core sections

1. MSME events, ledgers, exposures, stocks, flows and outcomes.
2. Event time, posting time, effective time, correction time and model-availability time.
3. Point-in-time joins, slowly changing dimensions and leakage prevention.
4. Explicit lifecycle features and their economic meanings.
5. AI neural sequence representations and their limited, complementary role.
6. Cross-fitting, residualisation against explicit variables and optional whitening.
7. Missingness, revisions, data-quality fallbacks and feature ownership.
8. Low-frequency Kenyan macroeconomic and sector inputs.
9. Secure analytical views, synthetic development data and model-to-data access.
10. Reproducibility, lineage and validation tests.

## Canonical feature families

- cash inflow and outflow velocity;
- cash-flow asymmetry and volatility;
- debt-service coverage and debt-to-liquidity;
- utilisation and limit pressure;
- repayment velocity and allocation behaviour;
- arrears-state transitions;
- time since depletion and buffer days;
- seasonality and sector context;
- servicing contacts, promises and fulfilled arrangements;
- governed interactions specified before modelling.

Features must have one engineered owner. Raw event sequences may feed both branches, but an explicitly defined metric will not be duplicated as an independently learned and explicit input without a stated experiment.

## Required diagrams and tables

- Point-in-time temporal data architecture.
- Explicit-feature and AI-representation dual path.
- Feature ownership and availability table.
- Data source, lawful access, latency and quality matrix.

## Technical appendices

Candidate appendices may retain B-spline–RW1, B-spline–AR(1), low-frequency state-space, sequence-model and hardware optimisation alternatives. The main body will use governed P-splines and the residual representation interface required by Part 2b.

## Acceptance tests

- No future information enters a training or scoring record.
- Every feature has unit, window, clock, missingness rule and owner.
- AI is identified plainly as AI and introduced only after the behavioural-scoring purpose is clear.
- Residualisation is described as redundancy control, not causal adjustment.
- Public aggregate data and institution-level lifecycle data are not conflated.

