#!/usr/bin/env python3
"""Exact constants for the uniform finite/infinite full-Q bridge.

The Hilbert norm proof is analytic (weighted Schur + midpoint convexity);
this script checks its coefficient signs, public floor rounding and shear
inequality on independent finite Fraction systems. No infinite extrapolation.
"""
from fractions import Fraction as F
import argparse
import json
from pathlib import Path
import random
from suzuki_trace_congruence_replay import inv, mul, psd, tr, display


def replay():
    # f_a(t)=t^(-1/2)/(a+t), a,t>0:
    # f''=(3a^2+10at+15t^2)/(4t^(5/2)(a+t)^3)>0.
    second_derivative_numerator = [3,10,15]
    assert all(c>0 for c in second_derivative_numerator)
    # cosh(1/2): term_2=1/384, subsequent ratios <=1/120.
    cosh_upper = F(1)+F(1,8)+F(1,384)/(1-F(1,120))
    assert cosh_upper < F(8,7)
    displacement = F(10)  # (10/pi)*||Hilbert|| <= 10.
    pole = F(256,49)
    cross = displacement+pole
    assert cross < 16
    cases=[]
    for sector,delta,public in (('even-v',F('7.79e-6'),F('1.84e-18')),
                                ('odd-v',F('3.26e-5'),F('1.35e-16'))):
        exact = delta/(1+F(16)/delta)**2
        assert exact > public
        cases.append({'sector':sector,'base_Q8_floor_rational':str(delta),
                      'uniform_cross_bound_rational':'16',
                      'derived_fullQ_floor_rational':str(exact),
                      'derived_fullQ_floor_display':display(exact),
                      'public_fullQ_floor_rational':str(public),
                      'rounding_down_verified_exact':True,
                      'scope':'all nominal cutoffs R>=8000 and the infinite closed quadratic form'})
    synthetic=[]
    for seed in (31,107,211):
        rng=random.Random(seed)
        delta=F(1,17)
        # Positive diagonal front; exact finite Schur is H>=I.
        a=[[delta*(i+2) if i==j else F(0) for j in range(2)] for i in range(2)]
        b=[[F(rng.randrange(-20,21),7) for j in range(3)] for i in range(2)]
        b2=sum(x*x for row in b for x in row);assert b2<=16**2
        d=mul(tr(b),mul(inv(a),b))
        for i in range(3):d[i][i]+=1+F(i,5)
        c=[a[i]+b[i] for i in range(2)]+[tr(b)[i]+d[i] for i in range(3)]
        lower=delta/(1+F(16)/delta)**2
        shifted=[[x-lower*F(i==j) for j,x in enumerate(row)] for i,row in enumerate(c)]
        assert psd(shifted)
        synthetic.append({'seed':seed,'exact_schur_ge_I':True,'full_block_floor_verified_exact':True})
    return {'schema':'cone.uniform-infinite-fullQ-bridge.v1',
            'hilbert_weight':'w_j=(j+1/2)^(-1/2)',
            'positive_second_derivative_numerator_coefficients':second_derivative_numerator,
            'hilbert_norm_bound':'pi; analytic midpoint-convexity/weighted-Schur proof',
            'displacement_cross_cap_rational':str(displacement),
            'pole_cross_cap_strict_rational':str(pole),
            'total_cross_cap_strict_rational':str(cross),
            'public_total_cross_cap_rational':'16','cases':cases,'synthetic':synthetic,
            'parent_inputs':['v14.025 global z','v14.044/v14.071 remote Schur >=I',
                             'v14.155/v14.158/v14.161 frozen-P Q8 base and protected positivity'],
            'source_scalar_caps_beyond_256k_claimed':False,
            'infinite_capacity_tail_closed':False,
            'guardrail':'Uniform full-Q coercivity only. No remote unit-floor transfer, sampled infinite norm, geometric extrapolation, or tail-capacity conclusion.'}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--reference',type=Path)
    a=p.parse_args();out=replay();raw=(json.dumps(out,indent=2,sort_keys=True)+'\n').encode()
    if a.reference:assert raw==a.reference.read_bytes()
    a.output.write_bytes(raw)
    print(json.dumps({'uniform_cross_cap':16,'public_floors':{r['sector']:r['public_fullQ_floor_rational'] for r in out['cases']},'all_exact_checks_pass':True,'infinite_capacity_tail_closed':False},indent=2))


if __name__=='__main__':main()
