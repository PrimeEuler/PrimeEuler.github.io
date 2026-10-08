#!/usr/bin/env python3
"""Outward finite Q and exact conditional remaining-tail budget.

The C_S cap is explicitly a hypothesis, never inferred from a historical
midpoint. Finite capacities use the audited exact endpoint composition.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from suzuki_exact_outward_pair_certificate import endpoint
from suzuki_trace_congruence_replay import display


def analyze(even,odd,cutoff,cs_cap=F(640),tail=F('5e-9'),target=F('1e-8')):
    e=endpoint(even,'even-v',cutoff);o=endpoint(odd,'odd-v',cutoff)
    assert e[1]['remote_start']==o[1]['remote_start']==32000
    assert e[2]>e[3]>=0 and o[2]>o[3]>=0
    assert cs_cap>=0 and 0<=tail<target
    diff=e[2]-o[2];de=e[3]+o[3]
    product_hi=(e[2]+e[3])*(o[2]+o[3])
    lo=diff-de-cs_cap*product_hi;hi=diff+de+cs_cap*product_hi
    finite=max(abs(lo),abs(hi));available=target-finite
    threshold=(target-tail-abs(diff)-de)/product_hi
    return {'schema':'cone.exact-conditional-tail-closure-budget.v1','cutoff':cutoff,
            'remote_start':32000,'endpoints':[e[4],o[4]],
            'C_S_cap_hypothesis_rational':str(cs_cap),'C_S_cap_verified_by_this_consumer':False,
            'tail_remainder_hypothesis_rational':str(tail),'tail_remainder_verified_by_this_consumer':False,
            'oscillatory_scalar_target_rational':str(target),
            'finite_Q_interval_rational':[str(lo),str(hi)],
            'finite_Q_interval_display_approximate':[display(lo),display(hi)],
            'finite_Q_abs_upper_rational':str(finite),'finite_Q_abs_upper_display':display(finite),
            'remaining_tail_budget_rational':str(available),'remaining_tail_budget_display':display(available),
            'maximum_C_S_cap_for_requested_tail_reserve_rational':str(threshold),
            'maximum_C_S_cap_for_requested_tail_reserve_display':display(threshold),
            'conditional_total_abs_upper_rational':str(finite+tail),
            'conditional_total_abs_upper_display':display(finite+tail),
            'conditional_total_strictly_below_target_exact':finite+tail<target,
            'infinite_capacity_tail_closed':False,
            'guardrail':'Finite source capacities outward; C_S cap and infinite remainder remain explicit unverified hypotheses. No historical midpoint coefficient or dyadic extrapolation is promoted.'}


def main():
    p=argparse.ArgumentParser();p.add_argument('--even',required=True);p.add_argument('--odd',required=True);p.add_argument('--cutoff',type=int,required=True)
    p.add_argument('--C-S-cap',default='640');p.add_argument('--tail-reserve',default='5e-9');p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=analyze(a.even,a.odd,a.cutoff,F(a.C_S_cap),F(a.tail_reserve))
    a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in o.items() if k.endswith('_display') or k.endswith('_exact')},indent=2))


if __name__=='__main__':main()
