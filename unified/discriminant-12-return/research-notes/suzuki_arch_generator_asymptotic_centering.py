#!/usr/bin/env python3
"""Exact gauge-centering of the corrected Suzuki archimedean generator.

The corrected off-diagonal archimedean term is

    K_mn = pi*m*n*(Y_n-Y_m)/(m^2-n^2),
    Y_n  = n H_n,
    H_n  = int_0^2 h(t) sin(n*pi*t/2) dt,

for odd m,n, with

    h(t)=exp(-t/2)/(1-exp(-2t))-1/(2t),  h(0)=1/4.

The displacement generator pair can be taken as

    p_n=n,   q_n=n Y_n.

Gauge freedom
-------------
For any constant c,

    q_n -> q_n-c p_n = n(Y_n-c)

leaves

    p_m q_n-q_m p_n

exactly unchanged.  Hence the represented matrix is identical.

Natural asymptotic center
-------------------------
Let b=n*pi/2.  Integration by parts gives, for odd n,

    H_n = (h(0)+h(2))/b + O(b^-3),

because cos(2b)=cos(n*pi)=-1 and the sine endpoint terms vanish in the next
integration by parts.  Therefore

    Y_n=nH_n
       = (2/pi)(h(0)+h(2)) + O(n^-2).

Since

    h(0)=1/4,
    h(2)=exp(-1)/(1-exp(-4))-1/4,

the exact natural center is

    c_inf = (2/pi) exp(-1)/(1-exp(-4)).

Thus the centered second generator

    qtilde_n = n(Y_n-c_inf)

is O(n^-1), whereas the raw q_n=nY_n is O(n).

This gauge is algebraically exact and dramatically improves numerical
conditioning of the rank-four LDL and far-tail Cauchy representation.
"""
from math import exp, pi

C_INF = (2.0/pi)*exp(-1.0)/(1.0-exp(-4.0))

# Midpoint diagnostics from the corrected degree-65 scalar reconstruction.
RAW_Y_AT_16001 = 0.23856886737245636
MAX_ABS_CENTERED_Q_21_16001 = 6.2489484e-4

# Diagnostic local-replay comparison using a float64 point factor and
# longdouble checker.  These are conditioning diagnostics, not certificates.
RAW_GAUGE_LOCAL_DEFECT_SUM_DIAGNOSTIC = 1.3031136959914852e-4
CENTERED_GAUGE_LOCAL_DEFECT_SUM_DIAGNOSTIC = 1.7932298188050986e-8

if __name__ == '__main__':
    print('c_inf =', C_INF)
    print('Y_16001 midpoint =', RAW_Y_AT_16001)
    print('Y_16001-c_inf =', RAW_Y_AT_16001-C_INF)
    print('max |n(Y_n-c_inf)| midpoint ~', MAX_ABS_CENTERED_Q_21_16001)
    print('raw/centered diagnostic local-defect ratio =',
          RAW_GAUGE_LOCAL_DEFECT_SUM_DIAGNOSTIC/CENTERED_GAUGE_LOCAL_DEFECT_SUM_DIAGNOSTIC)
    print('guardrail: replay values are conditioning diagnostics only')
