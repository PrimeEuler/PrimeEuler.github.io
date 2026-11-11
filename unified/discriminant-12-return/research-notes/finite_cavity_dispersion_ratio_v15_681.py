#!/usr/bin/env python3
"""v15.681: finite-cavity two-length dispersion-ratio and translation audit.

Two aligned fixed-wall cavities are tuned to the same EM angular frequency omega:
cavity 1 uses its n=1 mode with L1=pi/omega; cavity 2 uses its n=2 mode
with L2=2pi/omega.  Their seeded resonant responses share the same GW strain,
K/omega=r, and after division by calibrated Q and static B bias their complex
ratio is the ratio of exact spatial overlaps.

The apparent O(1-r) phase shift in left-end coordinates is tested against a
common-center translation.  Only the magnitude is translation invariant.
"""
import sympy as s

r,mu=s.symbols("r mu", positive=True)
pi=s.pi

def J(n):
    # Dimensionless overlap at common resonant frequency, using z in [0,L_n].
    # L_n=n*pi/omega and r=K/omega.
    return s.Rational(2,1)/(n*pi) * (
        1-(-1)**n*s.exp(-s.I*n*pi*r)
    )/(1-r**2)

J1=s.simplify(J(1))
J2=s.simplify(J(2))
X=s.simplify(J2/J1)
Xclosed=s.I*s.exp(-s.I*pi*r/2)*s.sin(pi*r/2)
assert s.simplify(s.expand_complex(X-Xclosed)) == 0

# The cavities defined from the same left end have centers separated by
# (L2-L1)/2=pi/(2 omega).  Remove that ordinary plane-wave propagation phase.
X_common_center=s.simplify(s.exp(s.I*pi*r/2)*X)
assert s.simplify(s.expand_complex(
    X_common_center-s.I*s.sin(pi*r/2)
)) == 0

# For a timelike pump, r=sqrt(1-mu^2), mu=m_T/omega.
rmu=s.sqrt(1-mu**2)
Amp=s.sin(pi*rmu/2)
assert s.limit((1-Amp)/mu**4,mu,0) == pi**2/32

# The tempting left-end phase is exactly propagation over the center offset:
# Delta phi = pi(1-r)/2 = pi mu^2/4 + O(mu^4), but it is not an
# internal translation-invariant cavity observable.
phase_left=pi*(1-rmu)/2
assert s.limit(phase_left/mu**2,mu,0) == pi/4

print("left-end complex ratio: i exp(-i*pi*r/2) sin(pi*r/2)")
print("common-center ratio:     i sin(pi*r/2)")
print("|ratio| timelike:         1 - pi^2 mu^4/32 + O(mu^6)")
print("PASS: leading O(mu^2) phase is propagation/placement, not internal cavity physics")
