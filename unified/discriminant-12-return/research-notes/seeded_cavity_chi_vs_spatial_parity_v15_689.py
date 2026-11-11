#!/usr/bin/env python3
"""v15.689: seeded-cavity spatial parity versus Cone chi sector parity.

Two independent facts are tested:

1) Ordinary reflection parity in a centered 1D PEC cavity gives exact seeded
   overlap zeros for standing-wave metric drives.  A traveling drive contains
   both reflection parities and generically excites both classes.

2) The q=2 Cone grading chi=(-1)^L is a sector grading.  If ordinary EM states
   are chi=+ and a minimal quarter-rung interaction is chi-odd, then every
   EM->EM matrix element of that interaction vanishes identically.  A nonzero
   seeded EM response therefore needs a chi-even effective interaction, an
   additional chi-odd compensator, or a different physical identification.

This does not identify chi with spatial reflection parity.
"""
import sympy as s

# ----------------------------------------------------------------------
# Abstract Cone-sector theorem.
# ----------------------------------------------------------------------
a,b,c,d,e,f,g,h=s.symbols("a b c d e f g h", complex=True)
chi=s.diag(1,1,-1,-1)
Pp=(s.eye(4)+chi)/2
Pm=(s.eye(4)-chi)/2

# Most general displayed block-off-diagonal example: chi-odd.
Wodd=s.Matrix([
    [0,0,a,b],
    [0,0,c,d],
    [e,f,0,0],
    [g,h,0,0],
])
assert s.simplify(chi*Wodd*chi + Wodd) == s.zeros(4)
assert s.simplify(Pp*Wodd*Pp) == s.zeros(4)
assert s.simplify(Pm*Wodd*Pm) == s.zeros(4)

# A chi-even operator is block diagonal and can act within the EM sector.
u1,u2,u3,u4=s.symbols("u1 u2 u3 u4", complex=True)
Weven=s.diag(u1,u2,u3,u4)
assert s.simplify(chi*Weven*chi-Weven)==s.zeros(4)
assert Pp*Weven*Pp != s.zeros(4)

# Product of two chi-odd factors is chi-even.
Vodd=s.Matrix([
    [0,0,1,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,1,0,0],
])
assert s.simplify(chi*(Wodd*Vodd)*chi-(Wodd*Vodd))==s.zeros(4)

# ----------------------------------------------------------------------
# Ordinary centered-cavity reflection parity control.
# Domain z in [-pi/2,pi/2], Dirichlet tangential field at endcaps.
# f_even=cos z, f_odd=sin 2z are normalized cavity modes of opposite parity.
# Seeded source is proportional to d_z b.
# ----------------------------------------------------------------------
z,K=s.symbols("z K", real=True)
pi=s.pi
fe=s.sqrt(s.Rational(2,1)/pi)*s.cos(z)      # reflection even
fo=s.sqrt(s.Rational(2,1)/pi)*s.sin(2*z)    # reflection odd
assert s.integrate(fe**2,(z,-pi/2,pi/2))==1
assert s.integrate(fo**2,(z,-pi/2,pi/2))==1

b_even=s.cos(K*z)
b_odd=s.sin(K*z)
S_from_even=s.diff(b_even,z)   # odd
S_from_odd=s.diff(b_odd,z)     # even

# Exact parity zeros.
assert s.simplify(s.integrate(fe*S_from_even,(z,-pi/2,pi/2)))==0
assert s.simplify(s.integrate(fo*S_from_odd,(z,-pi/2,pi/2)))==0

# The allowed opposite-parity overlaps are generically nonzero.
I_odd=s.integrate(fo*S_from_even,(z,-pi/2,pi/2))
I_even=s.integrate(fe*S_from_odd,(z,-pi/2,pi/2))
K0=s.Rational(3,2)
assert s.simplify(I_odd.subs(K,K0)) != 0
assert s.simplify(I_even.subs(K,K0)) != 0

# Traveling wave b=exp(iKz) contains both standing-wave parities, so its
# derivative couples to both reflection classes at a generic K.
S_trav=s.diff(s.exp(s.I*K*z),z)
T_even=s.simplify(s.integrate(fe*S_trav,(z,-pi/2,pi/2)).subs(K,K0))
T_odd=s.simplify(s.integrate(fo*S_trav,(z,-pi/2,pi/2)).subs(K,K0))
assert T_even != 0 and T_odd != 0

print("Cone chi theorem: P_EM W_odd P_EM = 0")
print("two chi-odd factors compose to a chi-even effective operator")
print("centered cavity: even standing metric drive -> odd source -> even-mode overlap 0")
print("centered cavity: odd standing metric drive -> even source -> odd-mode overlap 0")
print("generic traveling drive couples to both reflection parities")
print("PASS: ordinary spatial parity is physical here; Cone chi needs a separate intertwiner")
