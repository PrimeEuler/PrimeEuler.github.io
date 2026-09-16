#!/usr/bin/env python3
"""Fail-closed outward budget for the shifted M=16001 seven-plane replay.

This file combines only already recorded/certified bounds.  It intentionally
separates source provenance from arithmetic certification.  The source branches
(prime/cusp/arch) are certified through M=16001, and the shifted midpoint target
is positive.  However, the repository does not yet contain a gamma_n-style
outward certificate for the 7991-dimensional structured solve and the explicit
remote Gram accumulation 16003..2,000,000.  Consequently this helper refuses to
promote index<=3 until those arithmetic radii are supplied.
"""
from decimal import Decimal, getcontext
getcontext().prec=50

# Certified / audited source-side inputs
EPS_SOURCE=Decimal('2e-13')
ARCH_OPERATOR=Decimal('1.22e-13')
PRIME_OPERATOR=Decimal('2.3e-36')
CUSP_OPERATOR=Decimal('4e-18')

# Shifted midpoint targets from v13.477/488
Q_MID_LOWER=Decimal('0.6777')
CROSS_MID_UPPER=Decimal('2.68e-7')
N_MID_LOWER=Decimal('9.22e-13')
PENALTY_MID_UPPER=Decimal('1.06e-13')
FINAL_MID_LOWER=Decimal('8.16e-13')

# Existing arithmetic cross-check (not an outward proof)
RAYLEIGH_DOUBLE_LONG_DIFF=Decimal('1.36e-16')
FINITE_COEFF_DIFF_UPPER=Decimal('4e-15')

# Analytic remote floor, shifted consistently
EPS=Decimal('2e-13')
REMOTE_FLOOR=(Decimal('4.6732')-EPS)-Decimal('0.994')**2/(Decimal('0.22')-EPS)
FAR_N_MID_UPPER=Decimal('1.3e-15')

# Missing theorem-level radii.  None means fail closed.
FINITE_SCHUR_ARITH_RADIUS=None
CROSS_ARITH_RADIUS=None
REMOTE_GRAM_ARITH_RADIUS=None
FAR_MOMENT_ARITH_RADIUS=None


def report():
    print('source operator shift =',EPS_SOURCE)
    print('prime source operator <=',PRIME_OPERATOR)
    print('cusp source operator <=',CUSP_OPERATOR)
    print('arch source operator <=',ARCH_OPERATOR)
    print('shifted remote floor >',REMOTE_FLOOR)
    print('midpoint Q lower >',Q_MID_LOWER)
    print('midpoint Q/N cross <',CROSS_MID_UPPER)
    print('midpoint unresolved scalar >',N_MID_LOWER)
    print('midpoint Schur penalty <',PENALTY_MID_UPPER)
    print('midpoint final seven-plane margin >',FINAL_MID_LOWER)
    print('observed longdouble Rayleigh difference =',RAYLEIGH_DOUBLE_LONG_DIFF)
    print('far unresolved midpoint Gram bound <',FAR_N_MID_UPPER)
    missing=[name for name,val in [
        ('finite Schur arithmetic radius',FINITE_SCHUR_ARITH_RADIUS),
        ('Q/N cross arithmetic radius',CROSS_ARITH_RADIUS),
        ('remote Gram arithmetic radius',REMOTE_GRAM_ARITH_RADIUS),
        ('far-moment arithmetic radius',FAR_MOMENT_ARITH_RADIUS)] if val is None]
    if missing:
        print('FAIL-CLOSED: missing outward radii:',', '.join(missing))
        print('NO THEOREM PROMOTION: ind_{<=0}(A_even(1)) remains <=4')
        return 1
    raise RuntimeError('Populate certified radii before enabling theorem branch')

if __name__=='__main__': report()
