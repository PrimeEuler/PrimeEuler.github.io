#!/usr/bin/env python3
"""Exact scalar budget for the analytic infinite polynomial constructor."""
from fractions import Fraction as F
import json, argparse, hashlib
from pathlib import Path

def build(source_directory):
    C=575
    # log(256001/4)>11; use the weaker rational floor for both lattices.
    L=F(11); a=F(1,C+1); b=1+F(C,11)
    x=(a+b)/(b-a); u,v=x.numerator,x.denominator
    J=6000
    # T_j(u/v)=P_j/v**j, exact integer recurrence.
    p0,p1=1,u
    for j in range(2,J+1): p0,p1=p1,2*u*p1-v*v*p0
    qbar=F(v**J,p1)
    factor=1+F(2*C*J*J,1)/(L*(b-a))
    source=F(500000000000)
    inputs={}
    for sector,expected in [('even','40fcbd9ba5745598fa0e8d98a5da43b7c088411c8fdcb4c6d0dcae10a0b9dc80'),('odd','41fdeb3af0ab1d00bc154cc7111b62d28d5e75365de795ce4a970f779e25138f')]:
        raw=(Path(source_directory)/('full-stationary-source-'+sector+'-v.json')).read_bytes()
        digest=hashlib.sha256(raw).hexdigest(); assert digest==expected
        d=json.loads(raw); norm2=F(d['rational']['represented_full_stationary_vector_norm2'])
        eta=F(d['rational']['whole_remote_source_transport_upper'])
        assert norm2<((source-2)/23)**2 and eta<1
        inputs[sector]=digest
    residual=qbar*factor*source
    assert x>1 and a<1<b
    assert qbar<F('1e-29')
    assert residual<F('1e-9')<F('3e-5')
    return {'schema':'cone.logarithmic-infinite-constructor-budget.v1',
      'operator_remainder_upper':C,'log_diagonal_lower_rational':str(L),
      'spectral_lower_rational':str(a),'spectral_upper_rational':str(b),
      'degree':J,'source_norm_sufficient_upper':str(source),
      'chebyshev_denominator_reciprocal_strict_upper':'1e-29',
      'exact_residual_strict_upper':'1e-9','residual_target':'3e-5',
      'exact_integer_recurrence_comparison_passed':True,
      'source_certificate_sha256':inputs,
      'physical_source_norm_bound_assembled':True,
      'numerical_whole_source_assembly_certified':False,
      'evaluated_infinite_trial':False,'trial_norm_certified':False,
      'stationary_scalar_certified':False,'infinite_capacity_tail_closed':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--source-directory',required=True)
    args=ap.parse_args()
    print(json.dumps(build(args.source_directory),indent=2,sort_keys=True))
