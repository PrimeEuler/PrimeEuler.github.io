#!/usr/bin/env python3
"""Exact uniform nonprime scalar reduction budget beyond the frozen front."""
from fractions import Fraction as F
import json
R=256000
# e>2 => exp(-4)<1/16, exp(-1)<1/2.
S2=F(1,2)*(F(1,4)*F(16,15)+2*F(1,16)*F(16,15)**2
              +4*F(1,16)*F(17,16)*F(16,15)**3)
assert S2<1
digamma=F(4,9*R*R)
arch=F(16,27*R**3)
elementary=F(7,81*R**3)
error=digamma+arch+elementary
assert error<F('1e-11')
source_charge=F('4e-5')*error
assert source_charge<F('4e-16')
o={'schema':'cone.remote-nonprime-scalar-reduction.v1',
   'cutoff':R,'parity_sign_retained':True,
   'digamma_error_upper_rational':str(digamma),
   'exponential_moment_upper_rational':str(S2),
   'arch_error_upper_rational':str(arch),
   'elementary_error_upper_rational':str(elementary),
   'uniform_z_surrogate_error_upper_rational':str(error),
   'whole_affine_source_error_upper_rational':str(source_charge),
   'uniform_z_error_lt_1e_minus11':True,
   'prime_sine_functions_retained_exact':True,
   'numerical_prime_evaluation_certified':False,
   'evaluated_infinite_trial':False,'infinite_capacity_tail_closed':False}
print(json.dumps(o,indent=2,sort_keys=True))
