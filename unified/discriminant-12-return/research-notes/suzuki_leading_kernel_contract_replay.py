#!/usr/bin/env python3
"""Exact algebra checks for the isolated parity-arch and pole rank-one channels."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path

def analyze():
    cases=0
    # b represents pi^2/4, and weights represent positive exp(-2a).
    # Rational proxies test algebra, not transcendental source enclosures.
    for b in (F(9,4),F(49,20),F(5,2)):
        for a in (F(1,2),F(5,2),F(9,2)):
            for n in (1,3,7,31):
                for m in (2,4,8,32):
                    z=lambda x:F(x)/(a*a+b*x*x)
                    lhs=(z(n)*m-n*z(m))/(n*n-m*m)
                    rhs=-b*n*m/((a*a+b*n*n)*(a*a+b*m*m))
                    assert lhs==rhs
                    factor=1/((1+a*a/(b*n*n))*(1+a*a/(b*m*m)))
                    assert 0<=1-factor<=a*a/b*(F(1,n*n)+F(1,m*m))
                    cases+=1
    # All signs and coefficient identities independent of pi and h values.
    for e in (F(2),F(3),F(8,3)):
        ch=(e+1/e)/2
        # Formal h=cosh(1/2), s=sinh(1/2), parameter t=e^(1/2).
        t=e;h=(t+1/t)/2;s=(t-1/t)/2
        assert h*h+s*s==(t*t+1/(t*t))/2
        assert -2*(4*s)**2-2*(4*h)**2==-32*(t*t+1/(t*t))/2
    return {'schema':'cone.leading-coefficient-algebra-contract-check.v1',
            'rational_displacement_cases':cases,
            'arch_resolvent_kernel_identity_exact':True,
            'rank_one_remainder_factor_inequality_exact':True,
            'pole_hyperbolic_coefficient_identity_exact':True,
            'checks_are_algebra_not_transcendental_enclosures':True,
            'infinite_capacity_tail_closed':False}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();o=analyze();a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
    print(json.dumps(o,indent=2))
if __name__=='__main__':main()
