#!/usr/bin/env python3
"""Finite full-front M11 contract, without changing the original C_S."""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
local=Path(__file__).resolve().parents[1]/'producers'
if local.is_dir():sys.path.insert(0,str(local))
from suzuki_exact_leading_source_certificate import capacity_interval
from suzuki_exact_outward_certificate import P_HASHES
from suzuki_trace_congruence_replay import display

def enclose(lo,hi,bits=192):
    s=1<<bits;return F(lo.numerator*s//lo.denominator,s),F(-((-hi.numerator*s)//hi.denominator),s)

def build(even,odd,cutoff):
    rows=[]
    for sector,path in [('even-v',even),('odd-v',odd)]:
        raw=path.read_bytes();d=json.loads(raw)
        assert d['sector']==sector and d['cutoff']==cutoff
        assert d['remote_start']==0 and d['frozen_base_P_sha256']==P_HASHES[sector]
        assert d['all_six_numerical_targets_met'] and all(d['checks_exact'].values())
        replay=capacity_interval(d)
        assert replay==d['leading_capacity_interval']
        lo,hi=map(F,replay['interval_rational']);out=enclose(lo,hi)
        assert 0<out[0]<=lo<=hi<=out[1]
        rows.append({'sector':sector,'cutoff':cutoff,'certificate_sha256':hashlib.sha256(raw).hexdigest(),
          'M11_full_front_interval_rational':[str(x) for x in out],
          'M11_full_front_interval_display_approximate':[display(x) for x in out],
          'exact_capacity_recomposition_matches_certificate':True})
    return {'schema':'cone.remote-leading-full-front-selfenergy.v1','cutoff':cutoff,
      'cases':rows,'source_definition':'w1_R(m)=-c z_m+alpha_p L_p p_p(m), every finite m<=R; full A_p,R inverse',
      'role':'Leading coefficient of B_>R,<=R A_R^-1 B_>R,<=R*; higher channels and geometric remainder still required.',
      'original_C_S_32000_replaced':False,'infinite_operator_action_certified':False,
      'infinite_capacity_tail_closed':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--even',type=Path,required=True);p.add_argument('--odd',type=Path,required=True);p.add_argument('--cutoff',type=int,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=build(a.even,a.odd,a.cutoff);a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps(o,indent=2,sort_keys=True))
