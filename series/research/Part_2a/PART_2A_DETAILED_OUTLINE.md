# Part 2a Detailed Outline

## Title and thesis

**Temporal Evidence, Behavioural Signals and Point-in-Time Feature Engineering**

Thesis: Behavioural credit evidence becomes decision-grade only when the lender can explain its economic meaning, lawful purpose, provenance, availability and historical state at the decision cutoff.

## Planned structure and incremental drafting gates

### Abstract

- Continue the MSME cash-clock story from Part 1.
- Define the temporal evidence problem and Part 2a contribution.
- State the dual-path design: explicit lifecycle features plus residual AI representations.
- Reserve inference, policy action and causal claims for later parts.

### 1. A payment is not one timestamp

- Re-enter the wholesaler narrative at the moment a receipt is expected, initiated, settled, posted and used in a decision.
- Explain why the latest database state is not the historical state.
- Introduce supervisory monitoring and the evidence-value proposition.
- Distinguish event, effective, commit, ingestion, publication, decision, correction, outcome-maturity and cash-realisation clocks.
- Figure 1: nine clocks surrounding one MSME repayment decision.
- Gate: every clock has a distinct operational example and no future evidence crosses `T_decision`.

### 2. The MSME event and state ledger

- Define the canonical event envelope and stable pseudonymous entity keys.
- Separate customer, enterprise, facility, invoice, payment, collateral, guarantee, intervention and outcome entities.
- Show events versus derived states.
- Establish append-only received evidence plus versioned correction records, without calling upstream data immutable.
- Integrate lawful-purpose, minimisation, accuracy and automated-decision safeguards.
- Table 1: source, lawful access, latency, quality, correction and authority matrix.
- Gate: every field is attributable to source, purpose and clock.

### 3. From operational systems to a bank-controlled evidence plane

- Describe source-ledger CDC, file/API ingestion and message-native sources separately.
- Use Debezium only for supported database changes.
- Describe Kafka partition ordering and idempotent consumers.
- Describe Flink event-time state, watermarks and late-record routing.
- Separate online feature state from the versioned historical lakehouse.
- Introduce Delta change records, lineage and authoritative systems of record.
- Figure 2: point-in-time data architecture from bank systems and authorised partners to online and offline views.
- Gate: no global-ordering, universal-latency or automatic-truth claims.

### 4. Reconstruct the state the decision could actually see

- Formalise decision eligibility using event, availability, effective and validity conditions.
- Explain slowly changing dimensions, bitemporal records and source corrections.
- Give a point-in-time join pattern and a counterexample showing leakage.
- Distinguish snapshot version from feature event time and label maturity.
- Specify late-arrival, reversal, backfill and correction rules.
- Gate: training rows reproduce the feature state available at their decision time.

### 5. Explicit lifecycle features with economic meaning

- Organise features by inflow, outflow, liquidity, debt service, utilisation, repayment, arrears, servicing, seasonality and context.
- Define examples mathematically with units and denominator safeguards.
- Treat cash-flow asymmetry, repayment velocity, buffer days and debt-to-liquidity as hypotheses whose direction and stability are tested.
- Separate stocks, flows, ratios and state transitions.
- Define windows, cutoffs, winsorisation and missingness.
- Table 2: governed feature contract and ownership.
- Gate: no named engineered metric is duplicated in the AI branch.

### 6. What AI adds after behavioural scoring is established

- Introduce AI in plain language as a controlled method for learning order, duration and interaction patterns in event sequences.
- Use a GRU as the candidate short-horizon recurrent encoder and a Transformer as a candidate longer-context encoder.
- Avoid making architecture choice a foregone conclusion.
- Define entity and time split, frozen artefact and out-of-fold representation.
- Residualise each representation against the explicit design matrix and optionally whiten the residual block.
- Explain what this does and does not establish.
- Figure 3: explicit-feature and residual-AI dual path into Part 2b.
- Gate: every AI contribution is a challenger against simpler models and is generated out of fold.

### 7. Macroeconomic context moves on another clock

- Ingest Kenyan context from CBK and relevant public authorities, with World Bank and IMF series as complementary sources.
- Distinguish observation period, release date, revision vintage and decision availability.
- Use KESONIA publication timing as a concrete example without moving Part 5 pricing into Part 2a.
- Discuss sector, inflation, rates, exchange-rate, fuel, rainfall or trade context only where a mechanism and validation plan exist.
- Describe lagged values, release masks and low-frequency state summaries.
- Gate: revised macro data cannot overwrite the historical information set used for a prior decision.

### 8. Missingness, quality and lineage are model inputs

- Separate true zero, inactivity, outage, non-participation, denied permission, delayed posting and unavailable history.
- Define fallback levels and uncertainty escalation.
- Quantify exclusions by account count and value.
- Use lineage objects for source dataset, transformation job, run and output artefact.
- Define reconciliation, schema, freshness, duplication, ordering, drift and correction tests.
- Gate: missingness cannot silently become an adverse behavioural conclusion.

### 9. The serving contract passed to Part 2b

- Define the versioned feature vector, residual AI vector, masks, timestamps and lineage token.
- Distinguish training, shadow, production and backfill modes.
- Establish online-offline parity testing and fail-safe behaviour.
- State the Part 2b boundary: inference consumes approved evidence but does not redefine it.
- Figure 4: feature contract, posterior interface and downstream policy boundary.

### Conclusion

- Return to the opening payment.
- State that the value of behavioural evidence lies in temporal and economic discipline, not volume alone.
- Lead into Part 2b's hierarchical inference problem.

### References

- Independent IEEE sequence in first-appearance order.
- Each reference begins as a separate paragraph on a new page in rendered output.

## Word budget

| Component | Editorial target |
|---|---:|
| Abstract | 240 |
| Section 1 | 720 |
| Section 2 | 760 |
| Section 3 | 900 |
| Section 4 | 760 |
| Section 5 | 1,050 |
| Section 6 | 880 |
| Section 7 | 560 |
| Section 8 | 600 |
| Section 9 | 520 |
| Conclusion | 180 |
| **Target editorial prose** | **7,170 before final compression** |

The first complete pass intentionally runs above the 6,348-word editorial benchmark. Final validation will remove repetition while preserving equations, tables, diagrams and technical explanations. The full-source target remains approximately 7,191 words.
