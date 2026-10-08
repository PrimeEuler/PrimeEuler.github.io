#!/usr/bin/env python3
"""Outward C_S(N)=C_D+M_even,11-M_odd,11 from leading-source certificates."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from suzuki_exact_leading_source_certificate import capacity_interval
from suzuki_frozen_trial_far_outward import add,neg,times,recip,constant,enclose,atan_recip,power
from suzuki_trace_congruence_replay import display

def exp_positive(x,terms):
    assert x>=0
    term=F(1);total=term
    for k in range(1,terms):term=term*x/k;total+=term
    first=term*x/terms;ratio=x/(terms+1);assert ratio<1
    return enclose((total,total+first/(1-ratio)))

def analyze(even,odd):
    files=[Path(even),Path(odd)];objects=[json.loads(p.read_bytes()) for p in files]
    e,o=objects
    assert e['sector']=='even-v' and o['sector']=='odd-v' and e['cutoff']==o['cutoff']==32000
    assert all(x['schema']=='cone.exact-leading-source-outward-certificate.v1' and x['remote_start']==0 for x in objects)
    for x in objects:assert x['leading_capacity_interval']==capacity_interval(x)
    pi=enclose(add(times(constant(16),atan_recip(5)),neg(times(constant(4),atan_recip(239)))))
    e1=exp_positive(F(1),160);e4=exp_positive(F(4),256)
    cosh1=times(constant(F(1,2)),add(e1,recip(e1)))
    E0=times(recip(e1),recip(add(constant(1),neg(recip(e4)))))
    CD=times(add(times(constant(-32),cosh1),times(constant(16),E0)),power(recip(pi),2))
    ie=tuple(F(x) for x in e['leading_capacity_interval']['interval_rational'])
    io=tuple(F(x) for x in o['leading_capacity_interval']['interval_rational'])
    CS=add(CD,add(ie,neg(io)));bound=max(abs(x) for x in CS)
    return {'schema':'cone.exact-leading-coefficient-pair.v1','cutoff':32000,
            'input_sha256':[hashlib.sha256(p.read_bytes()).hexdigest() for p in files],
            'source_definition':'w1=-c*z+alpha*(4*h/pi)*pole, full finite A_32000 inverse',
            'C_D_definition':'(-32*cosh(1)+16*exp(-1)/(1-exp(-4)))/pi^2',
            'pi_interval_rational':[str(x) for x in pi],
            'exp1_interval_rational':[str(x) for x in e1],'exp4_interval_rational':[str(x) for x in e4],
            'C_D_interval_rational':[str(x) for x in CD],
            'C_D_interval_display_approximate':[display(x) for x in CD],
            'leading_capacity_intervals':[x['leading_capacity_interval'] for x in objects],
            'C_S_interval_rational':[str(x) for x in CS],
            'C_S_interval_display_approximate':[display(x) for x in CS],
            'C_S_abs_upper_rational':str(bound),'C_S_abs_upper_display':display(bound),
            'C_S_abs_le_640_exact':bound<=640,'C_S_abs_le_1600_exact':bound<=1600,
            'C_S_interval_positive_exact':CS[0]>0,
            'audit_status':'new leading-source certificate bridge requires independent review',
            'infinite_capacity_tail_closed':False,
            'guardrail':'Finite leading coefficient only. No substitution for inverse-weighted correlated infinite remainder; independent source-contract and C_D derivation audit required.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--even',required=True);p.add_argument('--odd',required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--reference',type=Path)
    p.add_argument('--require-640',action='store_true')
    a=p.parse_args();o=analyze(a.even,a.odd);raw=(json.dumps(o,indent=2,sort_keys=True)+'\n').encode()
    a.output.write_bytes(raw)
    if a.reference:assert raw==a.reference.read_bytes()
    if a.require_640:assert o['C_S_abs_le_640_exact'] and o['C_S_interval_positive_exact']
    print(json.dumps({k:v for k,v in o.items() if k.endswith('_display') or k.endswith('_exact')
                      or k=='C_S_interval_display_approximate'},indent=2))
if __name__=='__main__':main()
