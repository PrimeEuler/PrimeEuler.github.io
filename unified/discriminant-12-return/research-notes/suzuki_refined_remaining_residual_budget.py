#!/usr/bin/env python3
"""Exact remaining residual requirement, reserving global transport once."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from suzuki_exact_integer_source_action import sqrt_upper
PINS={'even-v':'aba4f170458412a47f474d4935511ae45db231ac549f1744f46d81255ddea5ea','odd-v':'7a301d3b9806a1ad44623c971c38c0885c4de1b66e2677151b6403930c8157fc'}
def run(root):
 cases=[];target=F('3e-5');eps=F(1,1<<256)
 for sector,pin in PINS.items():
  raw=(root/f'refined-region1-residual-{sector}.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==pin;d=json.loads(raw);r={k:F(v) for k,v in d['rational'].items()}
  first=r['point_norm_upper']+r['physical_composition_error_upper'];T=r['source_transport_upper']+r['finite_lift_transport_upper'];assert r['complete_transport_upper']==T+r['physical_composition_error_upper']
  threshold=target-T;assert 0<first<threshold;rad=threshold**2-first**2;budget=max(F(0),sqrt_upper(rad,256)-eps);assert first**2+budget**2<=threshold**2
  cases.append({'sector':sector,'region1_certificate_sha256':pin,'rational':{'whole_residual_target':str(target),'physical_region1_residual_upper':str(first),'global_source_and_lift_transport_reserved_once':str(T),'remaining_physical_residual_budget_lower':str(budget),'exact_squared_remaining_budget':str(rad)},'display_approximate':{'physical_region1_upper':float(first),'global_transport':float(T),'remaining_physical_residual_budget':float(budget)},'required_remaining_domain':'all remote rows outside Region1, including Middle and infinite Far','composition_rule':'sqrt(physical_region1_upper^2+physical_remaining_upper^2)+global_transport<=3e-5','global_transport_added_once':True,'remaining_residual_evaluated':False,'whole_residual_acceptance_certified':False,'infinite_capacity_tail_closed':False})
 return {'schema':'cone.refined-remaining-physical-residual-budget.v1','cases':cases,'whole_residual_acceptance_certified':False}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();d=run(a.root);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps([r['display_approximate'] for r in d['cases']]))
