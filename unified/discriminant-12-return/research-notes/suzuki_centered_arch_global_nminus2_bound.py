#!/usr/bin/env python3
"""Global n^-2 bound for the centered corrected arch generator.

Let

  H_n = int_0^2 h(t) sin(n*pi*t/2) dt,
  Y_n = n H_n,
  c_inf = (2/pi)(h(0)+h(2))
        = (2/pi) exp(-1)/(1-exp(-4)),
  Ytilde_n = Y_n-c_inf,

for odd positive n.  Two integrations by parts give the exact identity

  Ytilde_n = -(8/(pi^3 n^2)) [
      h''(0)+h''(2)+int_0^2 h'''(t) cos(n*pi*t/2) dt
  ].

Hence

  |Ytilde_n| <= (8/(pi^3 n^2)) C_h,

where

  C_h = |h''(0)|+|h''(2)|+int_0^2 |h'''(t)|dt.

For the certified degree-65 rational polynomial h_32 from the project, a
termwise absolute bound on [0,2] gives

  sup |h_32''| <= 0.687343597681,
  int |h_32'''| <= 3.541154722978,

and therefore the deliberately coarse polynomial contribution

  C_h,poly <= 2*0.687343597681 + 3.541154722978
           < 4.915841919.

(The endpoint sum is bounded by twice the uniform h_32'' bound.)

The differentiated omitted Taylor tails are bounded directly from the same
coefficient majorants used in the h_32 certificate.  For the sech part, with
q=2/pi and omitted even powers r>=33, the term magnitude at t=2 obeys

  |term_r(2)| <= (1/pi) q^(2r).

For the regular csch part, omitted odd powers r>=34 obey the cruder bound

  |term_r(2)| <= pi^(-2r).

Multiplying each term by p(p-1)/4 for the second derivative and by
p(p-1)(p-2)/8 for the third derivative at t<=2, then summing the geometric
series, gives

  2 sup |R''| + 2 sup |R'''| < 4.60e-9.

Thus

  C_h < 4.915841924,

and

  (8/pi^3) C_h < 1.268348.

We therefore record the rounded global bound

  |Ytilde_n| < 1.27/n^2

for every odd positive n.

This bound is independent of the earlier incorrect arch off-diagonal formula;
it is derived directly from the defining sine transform H_n.  It is intended
for the corrected rank-four cross/tail analysis.
"""

import math

POLY_H2_SUP = 0.687343597681
POLY_H3_L1 = 3.541154722978
TAIL_DERIVATIVE_BUDGET = 4.60e-9
CH = 2*POLY_H2_SUP + POLY_H3_L1 + TAIL_DERIVATIVE_BUDGET
COEFFICIENT = 8*CH/math.pi**3
ROUNDED_COEFFICIENT = 1.27

if __name__ == '__main__':
    print('C_h bound =', CH)
    print('(8/pi^3) C_h =', COEFFICIENT)
    assert COEFFICIENT < ROUNDED_COEFFICIENT
    print('PASS: |Ytilde_n| < 1.27/n^2 for odd positive n')
