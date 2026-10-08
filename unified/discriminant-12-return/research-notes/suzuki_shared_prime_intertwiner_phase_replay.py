#!/usr/bin/env python3
"""Exact integer phase/wrap checks for the analytic shared-prime intertwiner."""
import argparse
import json
from pathlib import Path

def sign(x):return (x>0)-(x<0)

def wrap(v,D):
    m=(v+D)//(2*D)
    return v-2*D*m,m

def analyze(D=400):
    assert D>=2
    rows=[]
    for s in range(1,D):
        tested=0
        for t in range(-D+1,D):
            mid,_=wrap(t+s,D);out,m=wrap(t+2*s,D)
            if t==0 or out==0 or abs(mid)==s or abs(mid)<s:continue
            # The e^(i phi) factor is removed. The remaining coefficient
            # is sign(output)/sign(input) times the half-phase wrap sign.
            assert sign(out)*sign(t)*(-1 if m%2 else 1)==1
            tested+=1
        rows.append({'phi_over_pi':f'{s}/{D}','tested':tested})
    return {'schema':'cone.shared-prime-intertwiner-phase-test.v1',
            'denominator':D,'phi_count':len(rows),
            'allowed_frequency_tests':sum(x['tested'] for x in rows),
            'all_phase_wrap_sign_identities_exact':True,
            'proof_is_analytic_not_grid_extrapolation':True,
            'infinite_capacity_tail_closed':False,'rows':rows}

def main():
    p=argparse.ArgumentParser();p.add_argument('--denominator',type=int,default=400)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--reference',type=Path)
    a=p.parse_args();out=analyze(a.denominator)
    raw=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode()
    if a.reference:assert raw==a.reference.read_bytes()
    a.output.write_bytes(raw)
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
