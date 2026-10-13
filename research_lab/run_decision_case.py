"""Generate the bounded GOV-001 evidence record and appendix from baseline inputs."""
from pathlib import Path
from decimal import Decimal
import argparse, hashlib, io, json, unittest
import decision_case as g
from cases import load_inputs


def money(x):
    return 'Requires separate delinquency path' if x is None else f'{x:,.2f}'


def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+
                     ['| '+' | '.join(str(x).replace('|','/') for x in r)+' |' for r in rows])


def publication_fingerprints(fixture, finance_raw):
    def digest(obj):
        return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    return {'decision_case_inputs.json':digest(fixture),'case_inputs.json':digest(finance_raw)}


def publication_is_current(fixture, finance_raw):
    expected=json.loads(Path(__file__).with_name('decision_case_publication_baseline.json').read_text(encoding='utf-8'))
    return publication_fingerprints(fixture,finance_raw)==expected['input_fingerprints']


def narrative(f, r):
    before,after=r['before'],r['after']
    cash=table(['KES','30 September cutoff','3 October verified classification'],[
        ['Opening enterprise cash',money(before['opening']),money(after['opening'])],
        ['Gross statement credits',money(before['raw_credits']),money(after['raw_credits'])],
        ['Paired internal-transfer credits',money(before['transfer_credits']),money(after['transfer_credits'])],
        ['Credits subsequently reversed',money(before['reversed_credits']),money(after['reversed_credits'])],
        ['Confirmed operating receipts',money(before['operating_receipts']),money(after['operating_receipts'])],
        ['Settled operating costs',money(before['operating_costs']),money(after['operating_costs'])],
        ['Net operating cash',money(before['operating_net']),money(after['operating_net'])],
        ['Prior financing draw less principal repaid',money(before['financing_net']),money(after['financing_net'])],
        ['Owner capital contribution',money(before['capital_net']),money(after['capital_net'])],
        ['Unresolved related-party receipt',money(before['unresolved_net']),money(after['unresolved_net'])],
        ['Closing enterprise cash',money(before['closing']),money(after['closing'])]])
    tx=table(['Record','Account','Cash amount, KES','Settlement / initial knowledge','Initial purpose'],[
        [x['id'],x['account'],money(Decimal(x['amount'])),x['settled_at'],x['reference']] for x in f['transactions']])
    opts=table(['Option','Minimum forecast cash','Funding needed to keep 100,000 floor','Finance cost incl. upfront fee','Terminal cash','Lender margin-budget economic profit'],[
        [k.replace('_',' '),money(v['minimum_cash']),money(v['financing_needed']),money(v['finance_cost']),money(v['terminal_cash']),money(v['margin_budget_economic_profit'])]
        for k,v in r['options'].items()])
    acts=table(['Knowledge cutoff','Recorded state','Effective due day','Expected payment','Settled cash','Outcome evidence'],[
        [v['cutoff'],v['state'],v['effective_due_day'],money(v['expected_contract_payment']),money(v['settled_cash']),v['outcome']]
        for v in r['action_snapshots']])
    prot=table(['Cutoff','Latest evidence','Last successful verification','Verified gross recovery','Nominal LGD','Expected nominal loss'],[
        [v['cutoff'],v['latest_evidence'],v['last_verified_at'],money(v['verified_gross_recovery']),f"{v['nominal_lgd']:.0%}",money(v['expected_nominal_loss'])]
        for v in r['protection']])
    return f'''# Governing evidence and intervention: a reproducible operating case

**Case U4C-GOV-001.** 1 October 2026. Hypothetical transactions, internal policy, authorised roles and later follow-up events. All amounts are KES. This appendix develops Part 3's Credit Policy and Compliance Gate through four connected decision traces. Each trace states the evidence, financial consequences, responsible decision and subsequent observable event.

## 1. The decision the lender is making

An MSME's statement contains KES {money(before['raw_credits'])} of credits. The lender needs to establish how much represents operating cash generation, what evidence supports a change to an existing loan, and who can authorise the resulting customer treatment. The workflow preserves settled cash while changing the interpretation and use of that evidence.

The September account window ends at **KES {money(before['closing'])}**, exactly the opening cash used in operating case U4C-MSME-001. This is a reconciliation of the earlier period into that opening balance. September flows are included once. The prior KES100,000 bridge-loan principal is fully repaid within this window. The new KES500,000 order loan begins on 1 October under the existing case assumptions.

The four traces are: unresolved operating evidence, a verified but permission-dependent amendment, execution and payment follow-up, and protection re-verification with an authorised decision to retain the customer's contract.

## 2. Trace one: reconstruct enterprise cash before using income features

The economic unit owns BANK-A and BANK-B through verified account identifiers known on 1 September. Opening balances are KES180,000 and KES20,000. Counterparty T08 is connected to the owner; classification requires an invoice and cash-purpose review. Entity control and transaction purpose are separate evidence objects.

{tx}

Transactions T03/T04 are the two sides of one KES70,000 movement between controlled accounts. T06/T07 are a KES20,000 credit and its exact reversal. A matched pair has opposite signs, equal amount, distinct controlled accounts and a shared transfer identifier. Reversal records identify the original credit. Duplicate source identifiers or unmatched pairs stop the consolidated view for reconciliation.

{cash}

The two account closing balances are BANK-A KES130,000 and BANK-B KES120,000. At the first cutoff, the source-to-feature bridge is:

```text
Operating receipts = gross credits 390,000 − self-transfer 70,000
                     − reversed credit 20,000 − financing draw 100,000
                     − owner capital 30,000 − unresolved receipt 50,000
                   = 120,000
Closing cash = opening 200,000 + operating 120,000 − costs 150,000
               + financing 100,000 − prior principal 100,000
               + owner capital 30,000 + unresolved 50,000
             = 250,000
```

On 3 October, invoice INV-02 and a matched receipt establish T08 as a related-party operating receipt. The classification is economically effective on 25 September and **known and verified on 3 October**. The September decision replay continues to show KES50,000 unresolved; the updated view shows KES170,000 operating receipts. Bank cash remains KES250,000. A new classification changes recurring-income evidence and the operating/financing bridge without changing money already settled.

One supported commercial receipt establishes its purpose for this fixture. Recurrence and future operating capacity require further observations. The example uses deterministic identifiers and invoice evidence. A probabilistic matching or scoring extension can add calibrated probabilities and validation against reviewed transactions.

### The internal policy route

The illustrative policy compares unresolved positive cash with external positive inflows after transfer/reversal elimination. At 30 September the share is 50,000 / 300,000 = 16.67%. It exceeds the adopted 10% review threshold. The lender uses KES120,000 as the confirmed operating-receipt scenario, requests the specific invoice and receipt evidence, routes the case to a credit-evidence officer and defers a material decision that depends on recurring income. The KES50,000 remains visible in settled liquidity.

After 3 October the governed classification can be accepted for its stated purpose. If an account feed is missing, the branch returns **reduced features**, preserving observed account cash while requesting the missing account coverage. If authority to obtain/use a required source is missing, that source-dependent decision is deferred. These branches are sample internal policy, with named evidence and review actions; transaction purpose is established through the named evidence and review actions.

## 3. Trace two: compare affordable options and obtain the necessary authority

The primary order receives a customer advance of KES200,000 and expects another KES800,000. The contract calls for principal 500,000 plus 60-day simple interest 15,000 on day 60. A verified customer schedule now puts the final receipt on day 90. The same model calculates both borrower cash and lender economics:

{opts}

The day 90 extension raises total financing cost from KES25,000 to KES32,500, including the already specified KES10,000 upfront fee. Minimum borrower cash is KES120,000, giving KES20,000 above the adopted operating floor. Keeping the day 60 contract with a day 90 receipt leaves a KES495,000 funding need to preserve that floor. That uncovered payment forecast requires an actual delinquency/workout path before its lender outcome can be valued.

Holding the supplied PD and recovery assumptions fixed to isolate timing, the amended loan's margin-budget economic profit is KES−3,650. The sample policy allows a delegated officer to consider an analytical concession loss up to KES4,000. The authorised officer verifies the receipt evidence, records the business rationale, approves the revised schedule and obtains the borrower's agreement. That limit is an explicit teaching assumption.

| Decision snapshot | Evidence / permission | Result |
| --- | --- | --- |
| Customer requests extension | New receipt date remains unverified | Request the specific customer schedule; substantive human review; defer amendment |
| Receipt date and affordability verified | Officer authority recorded; borrower agreement outstanding | Await borrower agreement; original contract remains effective |
| Receipt date, affordability and agreement recorded | Delegated authority absent | Await the authorised officer |
| Complete reviewed evidence packet | Authority and borrower agreement recorded | Approve the amendment and issue the controlled servicing instruction |

The customer explanation can be direct: “We have reviewed the expected receipt date. The proposed payment moves to day 90, with total principal and interest of KES522,500. Please review and agree to the revised schedule.” A record identifies the evidence version, responsible officer, consent record, next payment date and follow-up owner.

## 4. Trace three: follow the authorised instruction into actual delivery

The event log separates review, approval, contract booking and receipt. A booking event needs an earlier matching approval and evidence version. Approval requires both authority and borrower agreement. Settlement needs the booked contract and a unique rail reference. Replaying an identical event identifier is idempotent; conflicting identifiers or a duplicate settlement reference require reconciliation.

{acts}

The amended payment is KES522,500: 500,000 principal plus 22,500 simple interest for 90 days. Approval on 18 November records permission to execute. Booking on 19 November makes the revised schedule effective. The fixture's later payment occurs on 30 December and becomes known on 31 December; a replay before the knowledge date retains “awaiting observed payment.”

The last record is a **synthetic follow-up observation** used to exercise the ledger. A partial payment of KES510,000 leaves KES12,500 unpaid, which the test suite preserves. Actual customer performance and durable follow-up populate the corresponding observation fields during application. A defined comparison design and identified assumptions then support estimation of the intervention effect.

## 5. Trace four: re-verify protection and record an authorised decision to retain the contract

The borrower/protection review uses the same KES500,000 exposure, 4% PD and KES20,000 workout-cost assumption as the financial case. The previous verified gross recovery is KES200,000. A source outage, new dispute evidence and specialist interpretation have different meanings:

{prot}

On 8 November, source unavailability preserves the last successful verification date of 1 October. On 10 November, a dispute effective on 5 November becomes known. The current approved recovery assumption stays at KES200,000 while a KES100,000 alternative is sent for specialist review. On 15 November the specialist verifies the changed recovery assumption.

```text
Before: LGD = (500,000 − 200,000 + 20,000) / 500,000 = 64%
        Expected nominal loss = 4% × 320,000 = 12,800
After:  LGD = (500,000 − 100,000 + 20,000) / 500,000 = 84%
        Expected nominal loss = 4% × 420,000 = 16,800
```

The changed loss assumption is reviewed by its financial-model owner. PD stays at 4% in this isolated sensitivity. A separate customer-decision record CD01 contains the delegated officer's authority, rationale, decision knowledge date and next review on 15 December. It records **retention of the existing borrower contract** because the borrower remains performing and the evidence changes the recovery assumption. Closure links P04's specialist evidence with CD01's authorised customer decision. If authority or rationale is missing, the financial sensitivity still updates and the customer decision remains open for review.

The account cash, recovery estimate, accounting stage and customer decision each retain their own approval record. The case calculates nominal management loss; an accounting measurement uses its separate cash-flow, discounting and recognition conventions.

## 6. What governance changes in this case

| Evidence or control | Financial effect | Borrower and operating effect |
| --- | --- | --- |
| Paired transfers and reversals | Statement credits 390,000 reconcile to confirmed operating receipts 120,000 | Review is based on attributable operating cash |
| Verified purpose of T08 | Operating receipts become 170,000; cash remains 250,000 | Reviewer can explain and resolve the uncertainty |
| Verified day 90 receipt and affordable amendment | Minimum forecast cash 120,000; financing cost 32,500; analytical lender concession 3,650 | Supplier/payroll and operating floor remain in the cash path |
| Approval and booking controls | Contract changes only at the booked instruction; cash is recognised on observed receipt | Clear schedule, recorded agreement and execution responsibility |
| Protection specialist review | Nominal expected loss rises 4,000 under a fixed PD sensitivity | Authorised rationale supports retaining the customer contract |

The gate receives evidence versions and financial scenarios, returns a specific reason and permitted next step, and retains the later delivered action and outcome. This connects the temporal-evidence discussion in Part 2a, the decision responsibilities in Part 3, the execution records in Part 4 and the financial measures in Part 5.

## 7. Reproduce the case

The companion software is identified as **U4C-GOV-001, 1 October 2026**. It contains the transaction and evidence records printed in this appendix, the financial calculations shared with U4C-MSME-001, event replay rules and automated tests. The [GitHub research lab](https://github.com/TheAlchemistNerd/underwrite-for-collection/tree/main/research_lab) publishes the code and inputs. Its [reproduction guide](https://github.com/TheAlchemistNerd/underwrite-for-collection/blob/main/research_lab/README.md) contains installation and execution instructions for both cases.

The calculations preserve full decimal precision. Independent checks reconcile account balances to enterprise cash, remove paired transfers and reversals from operating receipts, retain unresolved classifications at the appropriate decision cutoff, and reproduce the extension and recovery sensitivities. Control tests verify authority, borrower agreement, consistent event identifiers and complete, unique settlement references. A verified recovery update can proceed while the separate customer decision still awaits authority and rationale.

The example covers two controlled accounts, exact-value transfer and reversal pairs, and one 90-day amendment. Further account structures, partial transfers and product amendments require additional rules and tests. Version fingerprints bind the published explanation to both the transaction inputs and the primary operating-case inputs. Changed assumptions produce separately labelled numerical results until the accompanying explanation has been reviewed.

## 8. Relationship to the main argument

Two principles connect the four traces. First, all observed cash must reconcile even when its economic purpose remains uncertain: borrowing, owner capital and transfers are different from operating receipts. Second, a borrower's and lender's position must be re-verified as evidence changes. A review ends with a reasoned decision, a responsible owner and a follow-up record. The transaction tables, financial comparisons and event histories above demonstrate these principles directly.

| Manuscript home | Useful exhibit |
| --- | --- |
| Part 1 | September cash reconciles to the existing order's opening 250,000 |
| Part 2a | Versioned entity ownership, source transactions, transfer pairing, reversal and point-in-time classification |
| Part 3 | Four decision traces, substantive review, affordability, authority, borrower agreement and authorised contract retention |
| Part 4 | Evidence/event IDs, idempotent replay, approval-to-booking references and observed settlement |
| Part 5 | Operating-cash classification, liquidity, amendment cost and recovery-assumption change |

The self-contained fixtures provide a reproducible foundation for application. The institution then evaluates entity-match quality, intervention effects and fairness using observed outcomes; connects the approved production interfaces; and documents the applicable legal basis, customer-review routes and decision authority.
'''


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    parser.add_argument('--write-appendix',action='store_true')
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--results-only',action='store_true')
    args=parser.parse_args()
    here=Path(__file__).resolve().parent; root=here.parent
    f=g.load_fixture(); c=load_inputs()
    from cases import __file__ as finance_module
    finance_raw=json.loads(Path(finance_module).with_name('case_inputs.json').read_text(encoding='utf-8'))
    baseline=publication_is_current(f,finance_raw)
    if not baseline and not args.results_only:
        raise ValueError('Inputs changed from publication baseline. Use --results-only --output <separate-directory>, then review the new narrative before updating its publication fingerprint.')
    if args.results_only and (args.write_appendix or args.output is None):
        raise ValueError('--results-only requires a separate --output and cannot write the canonical appendix')
    if args.check and args.write_appendix:
        raise ValueError('--check verifies existing output without writing an appendix')
    result=g.build_results(f,c)
    exact=json.dumps(result,default=g.json_default,ensure_ascii=False,indent=2)+'\n'
    if exact != json.dumps(g.build_results(f,c),default=g.json_default,ensure_ascii=False,indent=2)+'\n':
        raise AssertionError('Deterministic repetition failed')
    log=io.StringIO(); tests=None
    if baseline:
        suite=unittest.defaultTestLoader.discover(str(here),pattern='test_decision_case.py')
        tests=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
        if not tests.wasSuccessful(): raise RuntimeError(log.getvalue())
    else:
        log.write('Custom inputs: engine cash/event invariants and deterministic replay executed. Baseline numerical regression suite is not applicable.\n')
    output=args.output or root/'output/governed_evidence_case_2026-10-01'
    report=narrative(f,result) if not args.results_only else None
    if args.results_only and (output/'00_GOVERNED_EVIDENCE_AND_INTERVENTION_CASE.md').exists():
        raise ValueError('Results-only output must be separate from a published narrative directory')
    files={'results.json':exact,'fixture.json':json.dumps(f,ensure_ascii=False,indent=2)+'\n'}
    if report is not None: files['00_GOVERNED_EVIDENCE_AND_INTERVENTION_CASE.md']=report
    paths=[here/x for x in ['decision_case.py','decision_case_inputs.json','test_decision_case.py','run_decision_case.py','decision_case_publication_baseline.json']]
    paths.extend([Path(finance_module),Path(finance_module).with_name('case_inputs.json')])
    evidence={'case_id':f['case_id'],'tests_run':tests.testsRun if tests else 0,'failures':len(tests.failures) if tests else 0,'errors':len(tests.errors) if tests else 0,
              'publication_baseline':baseline,'verification_scope':'baseline regression suite and engine invariants' if baseline else 'custom engine invariants only',
              'deterministic_repetition':True,'results_sha256':hashlib.sha256(exact.encode()).hexdigest(),
              'sources':[{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]}
    files['validation.json']=json.dumps(evidence,indent=2)+'\n'
    if args.check:
        mismatches=[name for name,body in files.items() if not (output/name).exists() or (output/name).read_bytes()!=body.encode('utf-8')]
        if mismatches: raise AssertionError('Regeneration mismatch: '+', '.join(mismatches))
    else:
        output.mkdir(parents=True,exist_ok=True)
        files['test_results.txt']=log.getvalue()
        for name,body in files.items(): (output/name).write_text(body,encoding='utf-8',newline='\n')
    if args.write_appendix:
        target=root/'series/appendices/GOVERNED_EVIDENCE_AND_INTERVENTION_CASE.md'
        target.parent.mkdir(parents=True,exist_ok=True); target.write_text(report,encoding='utf-8',newline='\n')
    print(json.dumps({'output':str(output),'tests_run':tests.testsRun if tests else 0,'check':args.check,'results_sha256':evidence['results_sha256']}))


if __name__=='__main__': main()
