#!/usr/bin/env python3
"""Sharper exact full-Q floor retaining the unit shell Schur bound."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from suzuki_trace_congruence_replay import inv,mul,psd,tr,display


def replay():
    cases=[]
    for sector,delta,public in [('even-v',F('7.79e-6'),F('2.37e-13')),
                                ('odd-v',F('3.26e-5'),F('4.15e-12'))]:
        exact=delta**2/(delta+delta**2+16**2)
        old=delta/(1+16/delta)**2
        assert exact>public>old
        cases.append({'sector':sector,'delta_rational':str(delta),'cross_cap_rational':'16',
                      'shell_partial_Schur_floor_rational':'1',
                      'derived_floor_rational':str(exact),'derived_floor_display':display(exact),
                      'public_floor_rational':str(public),
                      'old_public_floor_rational':str(F('1.84e-18') if sector=='even-v' else F('1.35e-16')),
                      'public_rounding_down_verified_exact':True})
    synthetic=[]
    # Includes scalar systems approaching saturation and a coupled 2+2 case.
    for delta,B in [(F(1,10),F(16)),(F('7.79e-6'),F(16)),(F('3.26e-5'),F(16))]:
        a=[[delta]];b=[[B]];d=[[1+B*B/delta]]
        C=[a[0]+b[0],[b[0][0]]+d[0]]
        gamma=delta**2/(delta+delta**2+B**2)
        assert psd([[x-gamma*F(i==j) for j,x in enumerate(row)] for i,row in enumerate(C)])
        synthetic.append({'delta':str(delta),'cross':str(B),'exact_PSD_floor_check':True})
    delta=F(1,23);a=[[2*delta,F(0)],[F(0),delta]]
    b=[[F(3),F(-2)],[F(5),F(7)]]
    d=mul(tr(b),mul(inv(a),b))
    for i in range(2):d[i][i]+=1
    C=[a[i]+b[i] for i in range(2)]+[tr(b)[i]+d[i] for i in range(2)]
    B2=sum(x*x for row in b for x in row);gamma=delta**2/(delta+delta**2+B2)
    assert psd([[x-gamma*F(i==j) for j,x in enumerate(row)] for i,row in enumerate(C)])
    synthetic.append({'delta':str(delta),'cross_squared_fro_upper':str(B2),'exact_PSD_floor_check':True})
    return {'schema':'cone.weighted-uniform-infinite-fullQ-bridge.v1','cases':cases,
            'synthetic':synthetic,'parent_uniform_cross_and_form_inputs':'v14.171 independently audited in v14.172',
            'scope':'all cutoffs R>=8000 and infinite closed form, identical frozen P',
            'infinite_capacity_tail_closed':False,
            'guardrail':'Sharper coercivity only. Unit floor is retained for the partial shell Schur, not transferred to the full Q operator.'}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--reference',type=Path)
    a=p.parse_args();o=replay();raw=(json.dumps(o,indent=2,sort_keys=True)+'\n').encode()
    if a.reference:assert raw==a.reference.read_bytes()
    a.output.write_bytes(raw)
    print(json.dumps({'public_floors':{x['sector']:x['public_floor_rational'] for x in o['cases']},'all_exact_checks_pass':True},indent=2))


if __name__=='__main__':main()
