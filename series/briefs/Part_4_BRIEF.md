# Part 4 Brief

## Working title

**Bank-Controlled Research Sandboxes and Enterprise Credit Architecture**

## Scale

- Full-source target: 4,500 words.
- Editorial-prose target: 3,745 words.

## Purpose

Part 4 explains how banks and research partners can build, test, govern and reproduce the lifecycle-credit architecture without assuming unrestricted access to identifiable customer data.

## Core architecture

```text
Core banking, payments, bureau, servicing and approved external data
                              ↓
                 Bank-controlled data boundary
                              ↓
 Point-in-time features → model training → validation → approved artifact
                              ↓
 Shadow scoring → policy gate → case management → experiment logging
                              ↓
 Accounting, ECL, capital, treasury and governed research outputs
```

## Core sections

1. Systems of record and canonical credit events.
2. Model-to-data access and role-based analytical views.
3. Synthetic development and reproducible public-data baselines.
4. Secure enclave, private cloud and clean-room options.
5. Federated learning, secure aggregation, differential privacy and TEE tradeoffs.
6. Model registry, approval, versioning and rollback.
7. Experiment assignment, propensity and outcome logging.
8. Integration with core banking, collections, finance and risk systems.
9. Independent validation, disclosure control and audit evidence.
10. Ecosystem RACI and service-level obligations.

## Fit-gap doctrine

For each bank platform, the team will determine what can be calculated natively, what belongs in a governed analytical service, and what should be posted or surfaced as an approved result. Unsupported calculations will not be hidden inside manual interfaces.

## Acceptance tests

- No architecture depends on exporting an unrestricted customer dataset to the research team.
- Every decision can be reproduced from versioned data, feature, model and policy artifacts.
- Privacy technologies are tied to a threat model and do not create unsupported anonymity claims.
- Experiment logs support intention-to-treat and per-protocol analysis.
- The document does not imply that an internal research environment is regulatory approval.
