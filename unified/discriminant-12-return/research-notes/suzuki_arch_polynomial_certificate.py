#!/usr/bin/env python3
"""Quadrature-free polynomial certificate for h(t)=r''(t) on [0,2].

Use

  h(t)=1/4 [csch(t/2)+sech(t/2)-2/t].

The singular 2/t term cancels the first csch term exactly.  The remaining
Taylor coefficients are rational combinations of Bernoulli and Euler numbers.

For sech,

  sech z = sum_{r>=0} E_{2r} z^(2r)/(2r)!,

and the exact Euler-number formula gives

  |E_{2r}|/(2r)! = 4^(r+1) beta(2r+1)/pi^(2r+1).

Since beta(2r+1)<=1 for r>=1, on t in [0,2]

  (1/4)*|sech-tail after r=N|
  <= (1/pi) q^(2N+2)/(1-q^2),  q=2/pi.

For csch,

  csch z = 1/z + 2 sum_{r>=1}(1-2^(2r-1)) B_{2r} z^(2r-1)/(2r)!,

and |B_{2r}|=2(2r)! zeta(2r)/(2pi)^(2r), zeta(2r)<2, gives

  (1/4)*|csch-tail after r=N|
  <= (1/pi) s^(2N+1)/(1-s^2),  s=1/pi.

At N=32 the total uniform remainder is <6.1e-14.

Because |S_nn(t)|<=2 and |sin(n*pi*t/2)|<=1,

  |delta D_n| <= 4 ||h-h_N||_infty < 2.44e-13,
  |delta H_n| <= 2 ||h-h_N||_infty < 1.22e-13.

Thus the whole 77x77 finite arch matrix can be generated without numerical
quadrature, with a crude operator contribution below about 2e-11 before
rounding of the polynomial/trigonometric antiderivatives.

A proof-grade implementation must still outward-round pi and the exact finite
polynomial antiderivatives, but the analytic truncation error is explicit.
"""
import math

N=32
q=2/math.pi
s=1/math.pi
SECH_TAIL=(1/math.pi)*q**(2*N+2)/(1-q*q)
CSCH_TAIL=(1/math.pi)*s**(2*N+1)/(1-s*s)
H_UNIFORM=SECH_TAIL+CSCH_TAIL
H_SEQUENCE_ERROR=2*H_UNIFORM
D_SEQUENCE_ERROR=4*H_UNIFORM
ARCH_OPERATOR_TRUNCATION=77*D_SEQUENCE_ERROR

if __name__=='__main__':
    print('uniform h remainder <=',H_UNIFORM)
    print('H_n truncation error <=',H_SEQUENCE_ERROR)
    print('D_n truncation error <=',D_SEQUENCE_ERROR)
    print('77x77 crude arch operator truncation <=',ARCH_OPERATOR_TRUNCATION)
