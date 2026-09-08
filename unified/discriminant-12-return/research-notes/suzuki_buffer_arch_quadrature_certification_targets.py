#!/usr/bin/env python3
"""Certification targets for the smooth archimedean finite-buffer entries.

For K_arch(m,n)=-int_0^2 h(t) S_mn(t) dt, h=r'' is analytic on [0,2]
after its removable t=0 singularity is filled by h(0)=1/4.  The shift entry
S_mn is entire in t.  Therefore high-order Gauss-Legendre convergence is rapid,
but convergence itself is not a proof.

For buffer positivity we only need a coarse rigorous entry radius around 1e-3
(v13.330).  A practical certificate can therefore use either:

  * interval Gauss-Legendre nodes/weights plus interval evaluation, or
  * composite Taylor/derivative remainder bounds for h*S_mn.

The prime and cusp pieces are finite special-function expressions and need no
numerical quadrature.  The pole piece is positive rank one and may be omitted
entirely when proving a lower bound for A_BB.  Hence the only nontrivial
continuous enclosure needed for buffer positivity is K_arch.

This observation is important: to certify B>0 it is enough to certify

  C_cusp + B_prime + K_arch > 0,

because P_pole >= 0 exactly.
"""

BUFFER_ENTRY_RADIUS_TARGET = 1.0e-3
TAIL_START = 155

if __name__ == '__main__':
    print('arch entry enclosure target <=', BUFFER_ENTRY_RADIUS_TARGET)
    print('pole may be dropped for lower-bound certification because it is PSD')
