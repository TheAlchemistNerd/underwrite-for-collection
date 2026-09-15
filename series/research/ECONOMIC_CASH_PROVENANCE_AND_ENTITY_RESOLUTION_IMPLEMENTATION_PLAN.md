# Economic Cash Provenance and Entity Resolution: Implementation Plan

## 1. Intended outcome

This implementation extends *Underwrite for Collection* with a specific upstream control layer for multi-account cash-flow analysis. The existing manuscript already establishes the correct order of work: reconstruct evidence, define eligible cash, calculate explicit lifecycle features, estimate risk, apply policy and observe realised outcomes. The extension will make the first two stages operational when an MSME supplies heterogeneous statements or when authorised transaction feeds cover several accounts, wallets, entities and financial institutions.

The new layer will be called the **Economic Cash Provenance and Entity Resolution Layer**. It will establish which economic unit a transaction belongs to, whether two account references concern the same controlled entity, how funds moved through the observed network, what economic class the movement represents, what was knowable at the decision cutoff, and how much classification uncertainty remains. Ratios and behavioural features will consume this governed output rather than raw statement credits.

The work has two deliverables:

1. A standalone LinkedIn article of approximately 3,500 editorial words, provisionally titled *Before the Ratio: Entity-Resolved Cash Flow for Credit Underwriting*. It will build on the original *Underwrite for Collection* article without replacing or revising that article.
2. Targeted additions to Parts 1, 2a, 2b, 3, 4 and 5 of the white paper. These additions will close the identified specification gap while preserving the existing narrative, equations, HLR, causal programme, intervention architecture, sandbox design, Treasury treatment and references.

## 2. Preservation and scope controls

The implementation will not rewrite the white paper wholesale. The pre-existing Parts 1 through 5 will remain the narrative and technical foundation. Part 6 is not currently part of the canonical manuscript set and will not be invented for this correction.

Before editing, exact copies of all six manuscript files will be stored in the standalone and working-project revision-snapshot directories under:

```text
series/governance/revision_snapshots/
2026-09-15_pre_cash_provenance_extension/
```

Each snapshot will include SHA-256 hashes. Existing historical snapshots and published PDFs will remain unchanged. The original LinkedIn article will remain byte-for-byte unchanged.

The authoring rules are:

- Add content through anchored, localised patches.
- Preserve the established human, economic and institutional narration.
- Avoid defensive language and avoid presenting the extension as a correction of a failed model.
- Describe related-party or circularity signals as evidence requiring attribution, not as automatic proof of fraud or bad faith.
- Distinguish operating cash, financing cash, capital support, transfers and reversals without denying that each can be economically real for a different purpose.
- Keep the HLR and survival models downstream of evidence construction.
- Keep the Credit Policy and Compliance Gate downstream of inference.
- Keep Treasury settlement and availability tests distinct from borrower operating-cash classification.
- Preserve lawful-purpose, data-minimisation, customer-explanation and human-review requirements.

## 3. Canonical architecture

The white paper will adopt the following sequence:

```text
Raw authorised statements and payment events
                    ↓
Source verification and transaction normalisation
                    ↓
Temporal entity and control graph
                    ↓
Transfer pairing, path reconstruction and cycle review
                    ↓
Economic cash attribution with confidence and lineage
                    ↓
Operating, financing, capital, transfer and unresolved views
                    ↓
Explicit lifecycle features and residual AI evidence
                    ↓
Hierarchical Bayesian inference and lifecycle challengers
                    ↓
Credit Policy and Compliance Gate
                    ↓
Accountable action and realised cash outcomes
```

This architecture carries four separations through the manuscripts.

First, **settlement status** answers whether value moved and became available through the relevant rail. **Economic classification** answers why it moved and whether it measures recurring operating capacity. A settled loan drawdown is cash, but it is financing cash rather than sales. A settled self-transfer is cash in the receiving account, but it does not increase the consolidated enterprise's resources.

Second, **entity resolution** answers whether records refer to the same person, enterprise, controlled account or related counterparty. **Transaction classification** answers what a particular movement represents. The two processes inform each other but remain separately reviewable.

Third, **point-in-time validity** answers what the institution could know at the decision cutoff. **Economic authenticity and sustainability** answer whether the observed flow represents the operating mechanism relevant to repayment. A pre-review related-party transfer can pass the first test and require further evidence under the second.

Fourth, **classification confidence** is not a disguised credit score. It records the strength of the evidence supporting the cash category. A low-confidence or unresolved share changes feature availability, sensitivity analysis or review routing. It does not automatically assign adverse borrower intent.

## 4. LinkedIn article design

The new article will open with the practical problem raised by the exchange: an account can display apparently strong operating cash shortly before review even when the value came from a connected party or another controlled account. It will then reconnect that observation to the original *Underwrite for Collection* thesis: sustainable collection depends on correctly understanding the cash mechanism before approving, pricing or intervening.

The article will have the following structure:

1. **A settled credit can still answer the wrong question.** Introduce the difference between booked movement, available liquidity, operating income and sustainable repayment capacity.
2. **The ratio is downstream of a data-generating process.** Explain why arithmetic cannot repair entity or transaction misclassification.
3. **An account is not the economic borrower.** Describe enterprises, proprietors, related entities, accounts, wallets, facilities and counterparties as a temporal relationship graph.
4. **Classify cash by economic purpose.** Separate external operating receipts, internal transfers, related-party operating receipts, related-party funding, loan proceeds, owner capital, refunds, reversals, asset sales, protected funds and unresolved flows.
5. **Trace paths, not isolated credits.** Explain transfer pairing, multi-hop paths, short cycles, fan-in, fan-out, temporary balance uplift and repeated counterparty dependence.
6. **Sequence the architecture correctly.** Present the canonical pipeline from raw evidence to policy.
7. **Preserve uncertainty.** Introduce resolved-share, coverage, classification confidence and sensitivity to alternative classifications.
8. **Let models consume governed evidence.** Explain what the HLR, survival challenger and residual AI block can add after attribution, and why upstream quality masks remain visible.
9. **Use human review and customer recourse.** Distinguish a review signal from a finding of manipulation.
10. **Connect provenance to collection, ECL, capital and Treasury.** Show how the same economic classification affects affordability, forecast cash, expected shortfall, concentration and funding while each function retains its recognition rules.
11. **A practical implementation sequence.** Provide a staged route covering statement ingestion, gold-standard labelling, entity graph, classification, shadow ratios, model sensitivity and bounded production.
12. **Conclusion.** State the extension to the original doctrine: underwrite for collection by understanding the economic origin and path of cash before measuring its apparent strength.

The article will use compact IEEE citations. It will draw primarily on the existing white-paper evidence base and add the original entity-resolution literature, BCBS 239 and FATF beneficial-ownership guidance for bounded, accurately described propositions. FATF material will support the need to understand control and ownership, not convert a credit-underwriting article into an AML allegation framework.

## 5. Part 1 additions

### 5.1 Paragraph to add after the initial liquidity identity

After the explanation of available cash, add a narrative qualification that an account credit is not automatically collected operating cash. Describe a customer payment, owner injection, loan draw, refund and self-transfer as different economic events even when each raises the receiving account balance.

This paragraph will establish the human problem early without interrupting the existing wholesaler story. It will introduce the idea that an enterprise may operate through multiple accounts and related entities, making the cash-conversion cycle observable only after controlled consolidation.

### 5.2 Paragraphs to strengthen “One borrower, many institutions”

Add a distinction between the ecosystem view and the economic-entity view. The existing section correctly distributes roles among institutions. The extension will explain that multi-institution participation does not automatically create a consolidated borrower view. Each statement or feed remains source-specific until account ownership, control, observation coverage and permitted purpose are resolved.

### 5.3 New diagram

Add **Figure 4A: From account movement to enterprise cash evidence** after the existing ecosystem figure. It will use the established straight, grid-like Mermaid layout and show:

- bank accounts, wallets and related entities;
- source verification and canonicalisation;
- temporal entity and control graph;
- transaction paths and circularity review;
- cash categories;
- explicit lifecycle features;
- HLR, policy and collection outcomes.

The caption will clarify that the graph supports economic attribution. It will not describe every related-party movement as abusive.

## 6. Part 2a additions

Part 2a is the principal technical home for the new layer.

### 6.1 Expand the entity ledger

Add a subsection after the current discussion of stable pseudonymous keys. Define a temporal multi-entity graph:

```text
G_t = (V_t, E_t)
```

where nodes include enterprises, people in authorised roles, accounts, wallets, counterparties, facilities, invoices and payment events. Edges represent ownership, control, authority, payment, settlement, financing, invoice and possible-match relationships. Both nodes and edges will carry valid and knowledge intervals.

The subsection will distinguish deterministic links based on authoritative identifiers from probabilistic or rule-assisted links. Possible matches remain possible matches until approved. Consolidation will therefore retain the match method, confidence, evidence, reviewer and version.

### 6.2 Add a transaction-path and economic-classification subsection

Define the transaction record as containing source institution, source account, resolved sender and recipient where permitted, amount, currency, direction, event time, settlement time, knowledge time, reference, channel, related transaction, economic class, confidence and lineage.

The cash taxonomy will include:

- external operating receipt;
- internal transfer;
- related-party operating receipt;
- related-party funding;
- loan or overdraft proceeds;
- owner capital contribution;
- refund or reversal;
- asset-sale or exceptional proceeds;
- insurance, guarantee or recovery proceeds;
- protected or restricted funds;
- unresolved.

Add a table explaining how each class affects account cash, consolidated enterprise cash, operating-income measures, liquidity measures and review requirements.

### 6.3 Formalise cash eligibility

Extend the existing eligible-inflow definition with a weighted classification expression. The modelling view will preserve raw amounts while calculating eligible operating cash from events that are settled, externally sourced, classified as operating, non-duplicated, non-reversed and known at the cutoff. A confidence or approved haircut may be applied where policy permits. Unresolved amounts will remain separately reported rather than silently treated as zero or revenue.

Add coverage measures for:

- observed-account coverage;
- resolved-entity share;
- classified-value share;
- external-operating share;
- financing-inflow share;
- related-party concentration;
- circular-flow share;
- unresolved-flow share.

### 6.4 New diagram

Add **Figure 2A: Economic cash provenance and entity-resolution path** between the evidence-plane diagram and point-in-time reconstruction. The diagram will show the upstream sequence and the two outputs: an audit-preserving gross-flow view and a governed economic-flow view.

### 6.5 Expand validation

Add explicit tests for:

- source-document authenticity and balance reconciliation;
- deterministic and probabilistic entity-match quality;
- transfer-pair precision and recall;
- cycle-detection false positives;
- stability across institutions and statement formats;
- reviewer disagreement;
- value-weighted and count-weighted unresolved populations;
- sensitivity of CFA, velocity, DLR and affordability ratios to alternative classifications;
- point-in-time replay of later-discovered entity links.

## 7. Part 2b additions

Add a paragraph to the observation contract stating that the connected borrower unit comes from the approved temporal entity graph. The feature packet will include account coverage, resolved-value share, unresolved-value share, classification version and sensitivity bounds.

Extend the metadata block in the HLR description to name provenance and classification quality. The HLR will consume explicit features calculated from governed economic flows. Classification uncertainty may affect masks, review routes or scenario sensitivity. It will not be hidden inside the residual neural representation.

Expand validation so that the champion is re-scored under plausible reclassification scenarios. The model should demonstrate that a small number of ambiguous high-value credits do not create uncontrolled changes in PD, expected collectible cash or action. Connected entities must remain in the same fold after every approved graph version.

## 8. Part 3 additions

Extend the Credit Policy and Compliance Gate with provenance-aware conditions. The gate will receive observation coverage, resolved share, related-party concentration, unresolved cash and classification age. It may:

- accept the governed cash view;
- use a reduced feature set;
- apply an approved conservative scenario;
- request specific supporting evidence;
- route the case for substantive human review;
- defer a material decision until reconciliation is complete.

The text will state positively that related-party flows can have legitimate commercial purposes. The review establishes purpose, recurrence, contract support and cash path. Customer explanations will describe incomplete or unverifiable cash-flow evidence without alleging motive.

## 9. Part 4 additions

Part 4 will operationalise the layer within the bank-controlled environment.

Expand the canonical identifier paragraph to describe an entity-linkage service and versioned relationship graph. The graph service will preserve authoritative identifiers, normalised aliases, match evidence, confidence, effective dates, reviewer decisions and superseded links.

Expand Figure 2's controlled-linkage node so that it visibly includes the temporal entity graph and economic cash-provenance service. The production identity systems remain authoritative. The research zone receives only purpose-limited pseudonymous relationships and classified events.

Add a source-to-feature reconciliation sequence covering raw statement hash or feed identifier, source totals, normalised totals, paired transfers, classified cash, exclusions, unresolved value and final feature aggregates. This makes the output reproducible without exporting unnecessary direct identity.

## 10. Part 5 additions

Part 5 will preserve its settlement-finality and Treasury-recognition treatment. Add a distinction between:

- cash that is settled and available to the legal entity;
- cash classified as external operating generation;
- cash arising from financing or capital support;
- cash moved within the controlled group;
- cash still unresolved.

All may matter to liquidity, but only the appropriate categories support operating-cash persistence or customer cash-generation assumptions. Treasury will receive separate views rather than one netted label. The recognition gate will monitor changes in classification coverage and related-party concentration alongside settlement, reversal and forecast error.

The monthly reconciliation section will add economic-classification movement to the bridge. A reclassification from operating receipt to financing inflow changes behavioural assumptions and affordability evidence without pretending that the settled bank cash vanished.

## 11. Citation and terminology policy

The implementation will use these canonical terms consistently:

- Economic Cash Provenance and Entity Resolution Layer.
- Temporal entity and control graph.
- Economic cash attribution.
- External operating receipt.
- Related-party operating receipt.
- Related-party funding.
- Financing inflow.
- Internal transfer.
- Circular-flow indicator.
- Unresolved flow.
- Resolved-value share.
- Classification confidence.

“Suspicious,” “manipulative” and “fraudulent” will not be used as automatic consequences of graph patterns. Where financial-crime or fraud indicators arise, the credit process may refer them to the authorised control function under its own rules. Credit underwriting will retain the narrower question of sustainable, attributable cash generation.

References in the article will appear in first-use IEEE order. New manuscript sources, if required, will be appended to the affected part's existing reference sequence rather than renumbering unrelated citations.

## 12. Verification and acceptance criteria

The implementation will be complete when:

- The original LinkedIn article remains unchanged.
- A new article exists and contains at least 3,500 editorial words before references.
- The article reads as a successor to *Underwrite for Collection*, not as a technical audit report.
- All substantive external claims have an IEEE reference.
- Parts 1, 2a, 2b, 3, 4 and 5 contain only targeted additions or local diagram updates.
- Part 2a defines the temporal entity graph, cash taxonomy, classification uncertainty and ratio eligibility.
- Part 2a contains a dense straight-line Mermaid diagram for the new layer.
- Part 1 contains a reader-facing diagram that connects observed account movement to economic cash evidence.
- Part 2b carries graph and provenance quality into the feature packet and validation.
- Part 3 routes unresolved evidence without inferring intent.
- Part 4 provides the controlled linkage and reconciliation implementation.
- Part 5 separates operating cash provenance from settlement and legal availability.
- No mathematical or Mermaid block is malformed.
- All headings and figure labels remain unique.
- The standalone and working manuscript copies are byte-identical after implementation.
- A diff review confirms that the HLR, survival challenger, P-splines, Pólya-Gamma inference, causal design, Treasury framework and prior diagrams remain intact.

## 13. Implementation order

1. Preserve source snapshots and hashes.
2. Create the implementation plan.
3. Draft and word-count the LinkedIn article.
4. Extend Part 1's narrative and add Figure 4A.
5. Build the complete Part 2a provenance layer and Figure 2A.
6. Carry provenance metadata into Part 2b.
7. Add the Part 3 review routes.
8. Add the Part 4 linkage service and reconciliation bridge.
9. Clarify the Part 5 Treasury boundary.
10. Validate Markdown, Mermaid, headings, references and word counts.
11. Mirror the canonical standalone changes into the ignored working copy and verify hashes.
12. Review diffs before any later PDF compilation or publication decision.

The extension is successful when it makes cash-flow evidence harder to misinterpret while preserving the white paper's central economic language: underwrite toward sustainable collection, carry uncertainty honestly and measure success in realised, risk-adjusted cash and fair customer outcomes.
