#!/usr/bin/env python3
"""Signed moments of a represented full-vector Galerkin trial.

Exact point vector and sums; source scalar uncertainty is not included here.
This is a diagnostic interface, not the exact finite physical inverse.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from suzuki_exact_outward_certificate import read_snapshot
from suzuki_exact_integer_source_action import frac
from suzuki_trace_congruence_replay import inv,mul,display

if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)


def analyze(snapshot, certificate):
    meta,s,v,p=read_snapshot(snapshot)
    c=json.loads(Path(certificate).read_bytes())
    assert c['sector']==meta['sector'] and c['cutoff']==2*len(s['modes'])
    m=[[F(x) for x in row] for row in c['M_point_decimal']]
    coeff=mul(inv([row[:6] for row in m[:6]]),[[-row[6]] for row in m[:6]])
    bits=512
    q=[x[0].numerator*(1<<bits)//x[0].denominator for x in coeff]
    vb=max(x['bits'] for x in v)
    vv=[[z<<(vb-x['bits']) for z in x['values']] for x in v]
    values=[(vv[6][i]<<bits)+sum(q[j]*vv[j][i] for j in range(6)) for i in range(len(s['modes']))]
    xb=vb+bits
    n=s['modes'];z=s['z'];pole=s['pole']
    zi=0;mi=0;power=[1]*len(n)
    moments=[]
    for j in range(11):
        zi=sum(a*b*t for a,b,t in zip(z['values'],values,power))
        mi=sum(a*b*t for a,b,t in zip(n,values,power))
        moments.append({'j':j,'Z_even_rational':str(frac(zi,z['bits']+xb)),
                        'M_odd_rational':str(frac(mi,xb)),
                        'X_even_abs_rational':str(frac(sum(abs(a)*t for a,t in zip(values,power)),xb))})
        power=[a*b*b for a,b in zip(power,n)]
    pole_moment=frac(sum(a*b for a,b in zip(pole['values'],values)),pole['bits']+xb)
    # power is now n^22; exact absolute moments for the K10 remainder.
    az=frac(sum(abs(a*b)*t for a,b,t in zip(z['values'],values,power)),z['bits']+xb)
    ax=frac(sum(abs(b)*a*t for a,b,t in zip(n,values,power)),xb)
    # Preserve all seven separate leading functionals for later uncertainty transport.
    channels=[]
    for j,x in enumerate(v):
        zz=frac(sum(a*b for a,b in zip(z['values'],x['values'])),z['bits']+x['bits'])
        pp=frac(sum(a*b for a,b in zip(pole['values'],x['values'])),pole['bits']+x['bits'])
        channels.append({'column':j,'Z0_rational':str(zz),'pole_moment_rational':str(pp)})
    return {'schema':'cone.frozen-fullvector-tail-moments.point.v1','sector':meta['sector'],
            'cutoff':c['cutoff'],'remote_start':meta['remote_start'],
            'snapshot_sha256':hashlib.sha256(Path(snapshot).read_bytes()).hexdigest(),
            'certificate_sha256':hashlib.sha256(Path(certificate).read_bytes()).hexdigest(),
            'stationary_coefficients_rounded_down_rational':[str(frac(t,bits)) for t in q],
            'coefficient_rounding_absolute_error_le_rational':str(F(1,1<<bits)),
            'trial_l1_rational':str(frac(sum(abs(x) for x in values),xb)),
            'trial_l2_squared_rational':str(frac(sum(x*x for x in values),2*xb)),
            'pole_moment_rational':str(pole_moment),'moments':moments,
            'S22_z_point_rational':str(az),'S23_point_rational':str(ax),
            'separate_leading_channels':channels,
            'source_scalar_uncertainty_included':False,
            'exact_finite_inverse_uncertainty_included':False,
            'infinite_tail_closed':False,
            'guardrail':'Represented rounded Galerkin trial only. Preserve signed leading channels. Physical finite inverse and source uncertainties require separate transport before infinite capacity use.'}


def main():
    a=argparse.ArgumentParser();a.add_argument('--snapshot',required=True);a.add_argument('--certificate',required=True);a.add_argument('--output',type=Path,required=True)
    k=a.parse_args();out=analyze(k.snapshot,k.certificate)
    k.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'sector':out['sector'],'trial_l1_display':display(F(out['trial_l1_rational'])),
                      'Z0_display':display(F(out['moments'][0]['Z_even_rational'])),
                      'pole_moment_display':display(F(out['pole_moment_rational'])),
                      'infinite_tail_closed':False},indent=2))


if __name__=='__main__':main()
