#!/usr/bin/env python3
"""Robust certification target for the N=155 tail gap.

This checkpoint replaces the old non-interval decimal

    ||B_prime|| <= 2.044764260347282...

by the deliberately weaker target

    ||B_prime|| < 2.05.

The k=16 power-Schur midpoint data are

    sup_x (A^16 1)(x) = 93388.18411213082,
    2.05^16             = 97288.5603556106,

leaving absolute slack > 3900.

The finite breakpoint sweep has 3345 intervals at depth 16.  The minimum
midpoint spacing between consecutive breakpoints is about 9.51946e-5.  Every
breakpoint is +/-1 plus at most sixteen signed shifts log(q), q in {2,3,4,5,7}.
Thus log enclosures of radius 1e-10 make breakpoint-order certification trivial
relative to the observed spacing.  A final proof should instantiate this with
outward rational intervals and verify the finite maximum is below 2.05^16.

Using PRIME_BOUND=2.05 in the analytic v13.312 cusp/arch tail formulas gives

    alpha_155 >= 0.02494969... .

For the v13.345 six-dimensional protected full-tail bridge, beta_total about
8.871e-3 then costs only about 3.16e-3 in the Schur complement, leaving a
positive margin near 0.1843 against the finite protected minimum 0.1874456.

This file records the robust target and margins.  The finite interval sweep is
still to be instantiated; no RH/GRH or exact-zero claim follows.
"""
from __future__ import annotations
import math
import mpmath as mp

PRIME_TARGET=2.05
POWER=16
POWER_MIDPOINT_SUP=93388.18411213082
MIN_BREAKPOINT_GAP=9.519462370954912e-5
FINITE_PROTECTED_MIN=0.187445591522
BETA_TOTAL=8.871e-3


def r4_majorant():
    q=2.0/math.pi
    return float(mp.zeta(3))*q**3/(4.0*(1.0-q)**3)


def s2(N): return N**-2+1.0/(2.0*N)
def s4(N): return N**-4+1.0/(6.0*N**3)
def s6(N): return N**-6+1.0/(10.0*N**5)


def arch_tail(N):
    Cr=19.0/12.0+4.0*r4_majorant()
    return Cr*(4.0/math.pi**2)*s2(N)


def cusp_tail(N):
    rank=(2.0/math.pi**2)*s2(N)
    c=2.0/math.pi**3+6.0/math.pi**4
    a=2.0*c/math.pi
    off=2.0*a*math.sqrt((math.pi**2/12.0)*s6(N))
    Cd=2.0/math.pi**2+2.0/math.pi**3+2.0/math.pi**4+6.0/math.pi**5
    return rank+off+Cd*math.sqrt(s4(N))


def alpha(N=155):
    return math.log(N/4.0)-math.pi/2.0-PRIME_TARGET-cusp_tail(N)-arch_tail(N)


def report():
    a=alpha(155)
    penalty=BETA_TOTAL**2/a
    print('2.05^16 =',PRIME_TARGET**POWER)
    print('power-Schur midpoint sup =',POWER_MIDPOINT_SUP)
    print('absolute slack =',PRIME_TARGET**POWER-POWER_MIDPOINT_SUP)
    print('minimum breakpoint midpoint gap =',MIN_BREAKPOINT_GAP)
    print('robust alpha_155 =',a)
    print('bridge Schur penalty =',penalty)
    print('remaining protected margin =',FINITE_PROTECTED_MIN-penalty)
    print('guardrail: interval sweep still pending')


if __name__=='__main__': report()
