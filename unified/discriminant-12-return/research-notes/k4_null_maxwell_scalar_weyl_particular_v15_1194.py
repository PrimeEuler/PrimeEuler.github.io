#!/usr/bin/env python3
"""Gravity v15.1194 — complete traceful Maxwell source to scalar electric Weyl.

Source equations: archived v15.728 / 15.729 pressure-corrected scalar P,
Bardeen Phi_N/Psi_N, and Weyl STF reconstruction, with a phase-convention
specified single null-Maxwell harmonic from v15.1193.
Source is eternal test-field wave; particular solution (not unique retarded),
not full Riemann, not quarter-grid physical coupling.
"""
import sympy as s
t,k,eta,J0=s.symbols('tau k eta J0',positive=True,real=True)
I=s.I
w=s.sqrt(3)*k
nu2=(8*eta-3)*(1+k*k)/3
J=J0*t**(-1-I*w)
JPhi=Jpsi=J;JB=I*k*J
assert s.simplify(t*s.diff(JPhi,t)+s.sqrt(3)*JB+Jpsi)==0
# The correct full pressure/stress P equation from v15.728/729.
drive=s.factor(3*s.sqrt(3)*Jpsi/(2*k*k*t**3)
               -9*(t*s.diff(JB,t)+JB)/(2*k**4*t**3))
assert s.simplify(drive+3*s.sqrt(3)*J/(k*k*t**3))==0
D=(-1-I*w)**2+nu2
P=-3*s.sqrt(3)*J0*t**(-2-I*w)/(k*k*D)
beta=nu2+1
assert s.simplify(s.diff(P,t,2)+3*s.diff(P,t)/t+beta*P/t**2-drive)==0
# Source-first, spatial-stress-corrected v15.729 Bardeen potentials.
Phi=(t*t*s.diff(P,t,2)+2*t*s.diff(P,t))/(3*(1+k*k)) \
    +s.sqrt(3)*(JPhi+Jpsi)/(2*t*(1+k*k)) \
    -3*s.diff(JB,t)/(2*k*k*(1+k*k))
Psi=(k*k*P-t*s.diff(P,t))/(3*(1+k*k)) \
    +s.sqrt(3)*JPhi/(2*t*(1+k*k)) \
    +3*JB/(2*k*k*t*(1+k*k))
W=s.factor(3*k*k*(Phi+Psi)/(2*t*t))
coefficient=9*(I*(2*eta-3)*k-s.sqrt(3))/(4*eta*(1+k*k)-6*k*k+3*s.sqrt(3)*I*k)
assert s.simplify(W-coefficient*J0*t**(-4-I*w))==0
matchk2=(8*eta-3)/(4*(3-2*eta))
assert s.simplify((nu2-w*w).subs(k**2,matchk2))==0
for ev in (s.Rational(1,2),s.Rational(3,4),s.Integer(1)):
    km=s.sqrt(matchk2.subs(eta,ev))
    assert km>0
    den=s.simplify(D.subs({eta:ev,k:km}))
    assert den!=0
    fact=s.N(coefficient.subs({eta:ev,k:km}),17)
    assert abs(complex(fact))>0
    if ev==s.Rational(3,4):
        assert abs(complex(fact)-complex(-3.7115374447904514,2.727411870290969))<1e-12
        print('eta=3/4, k²=1/2: W/(J0 tau^(-4-i sqrt3 k))=',fact)
# Weyl is STF, with nontrivial scalar rank-2 electric projection.
e=s.diag(-s.Rational(1,3),-s.Rational(1,3),s.Rational(2,3))
assert s.trace(e)==0 and s.trace(e*e)==s.Rational(2,3)
print('PASS full scalar pressure correction, exact P particular, Phi_N/Psi_N, nonzero Weyl')
print('PASS phase-match finite nonsecular transfer, 2/3 STF norm')
print('OPEN causal switching, full Ricci/Riemann, E-shear constraint, quarter carrier')
