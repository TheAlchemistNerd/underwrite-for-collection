"""Run the case and export auditable input, event, decision and outcome records."""
from pathlib import Path
import argparse, csv, hashlib, json
from model import SCENARIOS, DEFAULTS, run_scenario


def write_csv(path, rows):
    if not rows: return
    with path.open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader()
        for row in rows:
            writer.writerow({k:json.dumps(v,sort_keys=True) if isinstance(v,(dict,list)) else v for k,v in row.items()})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);parser.add_argument('--inputs',type=Path);args=parser.parse_args()
    root=Path(__file__).resolve().parents[2]
    out=args.output or root/'output/moniepoint_cashflow_case_2026-10-18';out.mkdir(parents=True,exist_ok=True)
    params=json.loads(args.inputs.read_text(encoding='utf-8-sig')) if args.inputs else DEFAULTS
    summaries=[]; snapshots={};checks=[]
    for scenario in SCENARIOS:
        result=run_scenario(scenario,params);target=out/scenario;target.mkdir(exist_ok=True)
        summaries.append(result['summary']);snapshots[scenario]=result['snapshot']
        for key,value in result.items():
            if isinstance(value,list): write_csv(target/(key+'.csv'),value)
        (target/'decision_snapshot.json').write_text(json.dumps(result['snapshot'],indent=2),encoding='utf-8')
        checks.append(dict(scenario=scenario,cash_error=result['summary']['max_cash_reconciliation_error'],contribution_error=result['summary']['lender_contribution_reconciliation_error']))
    write_csv(out/'scenario_summary.csv',summaries)
    (out/'summary.json').write_text(json.dumps(summaries,indent=2),encoding='utf-8')
    (out/'decision_snapshots.json').write_text(json.dumps(snapshots,indent=2),encoding='utf-8')
    (out/'inputs.json').write_text(json.dumps(params,indent=2),encoding='utf-8')
    files=list(Path(__file__).parent.glob('*.py'))+[out/'inputs.json']
    manifest=dict(model='Synthetic Moniepoint application of Underwrite for Collection',currency='KES',checks=checks,
        checks_pass=all(abs(x['cash_error'])<1e-6 and abs(x['contribution_error'])<1e-6 for x in checks),
        sha256={str(f.relative_to(root)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in files})
    (out/'verification.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(json.dumps(dict(output=str(out),scenarios=len(summaries),reconciliation_pass=manifest['checks_pass']),indent=2))

if __name__=='__main__': main()
