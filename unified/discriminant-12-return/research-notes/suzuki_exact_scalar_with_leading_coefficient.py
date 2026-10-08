#!/usr/bin/env python3
"""Finite paired scalar using the outward leading coefficient, not a midpoint."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from suzuki_exact_outward_pair_certificate import endpoint
from suzuki_exact_leading_coefficient_pair import analyze
from suzuki_trace_congruence_replay import display

def main():
    p=argparse.ArgumentParser();p.add_argument('--even',required=True);p.add_argument('--odd',required=True)
    p.add_argument('--cutoff',type=int,required=True);p.add_argument('--leading-even',required=True)
    p.add_argument('--leading-odd',required=True);p.add_argument('--coefficient',required=True)
    p.add_argument('--tail-reserve',default='5e-9');p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();cs=analyze(a.leading_even,a.leading_odd)
    assert (json.dumps(cs,indent=2,sort_keys=True)+'\n').encode()==Path(a.coefficient).read_bytes()
    e=endpoint(a.even,'even-v',a.cutoff);o=endpoint(a.odd,'odd-v',a.cutoff)
    assert e[1]['remote_start']==o[1]['remote_start']==cs['cutoff']==32000
    ce=json.loads(Path(a.leading_even).read_bytes());co=json.loads(Path(a.leading_odd).read_bytes())
    assert ce['frozen_base_P_sha256']==e[4]['frozen_base_P_sha256']
    assert co['frozen_base_P_sha256']==o[4]['frozen_base_P_sha256']
    elo,ehi=e[2]-e[3],e[2]+e[3];olo,ohi=o[2]-o[3],o[2]+o[3]
    clo,chi=(F(x) for x in cs['C_S_interval_rational'])
    assert clo>0 and elo>0 and olo>0 and 1-chi*ohi>0
    lower=elo-ohi-chi*elo*ohi;upper=ehi-olo-clo*ehi*olo
    bound=max(abs(lower),abs(upper));tail=F(a.tail_reserve);assert tail>=0
    out={'schema':'cone.exact-finite-scalar-outward-leading-coefficient.v1','cutoff':a.cutoff,
         'source_frontier':32000,'paired_capacity_endpoints':[e[4],o[4]],
         'leading_coefficient_input_sha256':cs['input_sha256'],'C_S_interval_rational':cs['C_S_interval_rational'],
         'finite_Q_interval_rational':[str(lower),str(upper)],
         'finite_Q_interval_display_approximate':[display(lower),display(upper)],
         'finite_Q_abs_upper_rational':str(bound),'finite_Q_abs_upper_display':display(bound),
         'finite_Q_interval_strictly_negative_exact':upper<0,
         'tail_remainder_hypothesis_rational':str(tail),'tail_remainder_verified':False,
         'conditional_total_abs_upper_rational':str(bound+tail),
         'conditional_total_abs_upper_display':display(bound+tail),
         'conditional_total_abs_le_1e_minus8_exact':bound+tail<=F('1e-8'),
         'leading_coefficient_audit_pending':True,'infinite_capacity_tail_closed':False,
         'guardrail':'Outward finite leading-source bridge and finite scalar composed exactly; new coefficient bridge awaits independent audit. Correlated infinite remainder alone remains a tail hypothesis.'}
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k.endswith('_display') or k.endswith('_exact')
                      or k=='finite_Q_interval_display_approximate'},indent=2))
if __name__=='__main__':main()
