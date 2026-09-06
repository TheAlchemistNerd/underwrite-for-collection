# Part 4 Source and Claim Ledger

Access date for online sources: 6 September 2026.

| Claim family | Authority and source | Planned use | Boundary or qualification |
|---|---|---|---|
| Data-protection principles, DPIA, automated decisions and research | Kenya, *Data Protection Act, 2019*, ss. 25, 31, 35, 41 and 53 | Lawful and purpose-bound research, high-risk assessment, design controls, human reconsideration and non-identifiable publication | Research use is not a blanket exemption. Pseudonymised data remains personal where re-identification remains possible. |
| Detailed processing safeguards | Kenya, *Data Protection (General) Regulations, 2021*, regs. 19, 22, 33-36 and 49 | Retention, minimisation, accuracy, pseudonymisation, automated-decision controls and DPIA triggers | Apply according to the processing and entity in scope. |
| Research-specific implementation | ODPC, *Guidance Notes: Processing for Research Purposes*, 2025 | Lawful-basis record, trusted research environment, secure handling, publication control, participant information and internal compliance checklist | Current official guidance, not a substitute for institution-specific legal assessment. |
| Cybersecurity governance | CBK, *Guidance Note on Cybersecurity for the Banking Sector*, 2017 | Board ownership, cyber-risk framework, access protection, incident record, testing and connected-party risk | Applies to Banking Act institutions. Technology controls support, but do not independently establish, lawful or fair processing. |
| Outsourcing and retained bank responsibility | CBK, *Prudential Guidelines*, CBK/PG/16, Guideline on Outsourcing | Materiality, approval, due diligence, access, continuity and limits on outsourcing lending and compliance decisions | Research or technology partners may provide services and evidence. The licensed bank retains decision authority and accountability. |
| Risk-data architecture and lineage | BCBS, *Principles for effective risk data aggregation and risk reporting* and 2026 implementation note | Canonical identifiers, metadata, authoritative sources, reconciliation, completeness, timeliness and independent validation | International supervisory standard and comparator; proportional use according to the Kenyan institution's scale and risk profile. |
| AI lifecycle governance | E. Tabassi, NIST AI 100-1, *AI Risk Management Framework 1.0*, 2023 | Govern, map, measure and manage model risk; testing, evaluation, verification and validation | Voluntary international comparator, not Kenyan law. |
| Enterprise privacy-risk management | NIST, *Privacy Framework 1.0*, 2020 | Connect processing purpose, data actions, privacy risk and control outcomes | Voluntary comparator used after Kenyan legal requirements. |
| Federated learning | B. McMahan et al., “Communication-Efficient Learning of Deep Networks from Decentralized Data,” AISTATS, 2017 | Define distributed optimisation without centralising raw training records | Local updates can still create privacy, security, heterogeneity and integrity risks. Not required for a single-bank pilot. |
| Secure aggregation | K. Bonawitz et al., “Practical Secure Aggregation for Privacy-Preserving Machine Learning,” ACM CCS, 2017 | Explain aggregation of local updates without revealing each update to the coordinator | Protects an aggregation step, not the complete research or model lifecycle. |
| Differential privacy | J. Near, D. Darais and N. Lefkovitz, NIST SP 800-226, 2025 | Define quantifiable output privacy and implementation hazards | Requires an explicit privacy unit, adjacency relation, mechanism and cumulative budget; may reduce utility. |
| Third-party service risk | FSB, *Enhancing Third-Party Risk Management and Oversight*, 2023 | Service inventory, criticality, concentration, due diligence, monitoring and exit | International toolkit that complements Kenyan outsourcing requirements. |
| Operational resilience | BCBS, *Principles for Operational Resilience*, 2021, consolidated in 2026 | Critical-operation mapping, tolerances, testing, incident management and recovery | International comparator for a bank-operated lifecycle-credit service. |
| Regulatory versus internal sandbox | CMA Kenya, *Regulatory Sandbox Policy Guidance Note*, 2019 | Demonstrate the distinct meaning of a regulator-operated live capital-markets sandbox | It does not establish a CBK banking-sandbox process for this programme. Part 4 uses “bank-controlled research sandbox.” |
| Internal corpus | Parts 1-3; *Underwrite for Collection*; side-by-side semantic analysis; KBA canonical specification and data dictionary; Mwendo Pamoja Part 4 | Narrative continuity, event schema, artefact content, treatment ledger, synthetic-to-shadow progression and enterprise fit-gap | Rough and comparator material supplies design hypotheses. External claims require the authorities above. |

## Planned IEEE first-appearance sequence

1. Kenya Data Protection Act.
2. Kenya Data Protection (General) Regulations.
3. ODPC research-purpose guidance.
4. CBK Guidance Note on Cybersecurity.
5. CBK Prudential Guideline on Outsourcing.
6. BCBS 239 principles and implementation material.
7. NIST AI RMF 1.0.
8. NIST Privacy Framework 1.0.
9. McMahan et al. on federated learning.
10. Bonawitz et al. on secure aggregation.
11. NIST SP 800-226 on differential privacy.
12. FSB third-party risk toolkit.
13. BCBS operational resilience principles.
14. CMA Kenya Regulatory Sandbox Policy Guidance Note.

The final sequence will be frozen after drafting and tested against first appearance, orphaned entries and duplicate canonical URLs.

## Claims deliberately narrowed

- The bank-controlled research sandbox is not described as regulatory approval or a published CBK regulatory-sandbox route.
- Consent is not described as the only lawful basis for research processing.
- Pseudonymisation, encryption, a clean room, federated learning, secure aggregation or a TEE is not described as producing automatic anonymity.
- Differential privacy is not named without a privacy unit, adjacency relation, mechanism and budget.
- Synthetic data demonstrates mechanics and failure handling, not Kenyan borrower performance.
- Shadow scoring observes model behaviour without changing customer treatment.
- A research partner does not own the bank's lending decision, policy gate, customer communication or statutory books.
- An ERP or general ledger receives approved accounting events; it does not become the owner of unsupported model, ECL or pricing calculations.

