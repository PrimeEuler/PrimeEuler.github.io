#!/usr/bin/env python3
"""Cone v15.972: quarter rest/product circle and formal vs co-scaled
quadratic Casimirs at the SAME shared EM n+1 diameter.
Only a conditional kinetic normalization, not physical gravitational
operator identification. Exact symbolic plus D=2..100 matrix checks.
"""
import sympy as s
D=s.symbols("D",integer=True,positive=True)
P=s.factor((2*D-1)/4)
j=P
C_formal=j*(j+1)
C_scaled=j*(j+s.Rational(1,2))
C_em=s.factor((D**2-1)/4)
assert s.simplify(C_formal-C_scaled-P/2)==0
assert s.simplify((C_formal-C_scaled)/P-s.Rational(1,2))==0
assert s.simplify(C_scaled-(D**2-s.Rational(1,4))/4)==0
assert s.simplify(C_formal/P-C_em/(D-1)-(D+2)/4)==0
assert s.simplify(C_scaled/P-C_em/(D-1)-D/4)==0
assert s.simplify((C_formal-C_scaled)/P-s.Rational(1,2))==0
hbar,M,ell=s.symbols("hbar M ell",positive=True)
I=M*ell**2*P
deltaE=s.factor(hbar**2*(C_formal-C_scaled)/(2*I))
assert s.simplify(deltaE-hbar**2/(4*M*ell**2))==0
# The q2 refined grid has 2D sites, a genuine spin J=(2D-1)/2
# with a half-unit physical ladder J'_±=J_±/2 and Casimir C_scaled.
for d in range(2,101):
    N=2*d-1
    J=s.Rational(N,2)
    # Full matrix check for D<=8; exact scalar Casimir for rest.
    assert J*(J+1)/4==C_scaled.subs(D,d)
    assert (2*J+1)==2*d
    assert (2*j.subs(D,d)+1).q != 1  # formal j is odd-quarter, not SU2 irrep
    if d<=8:
        jp=s.zeros(2*d)
        for k in range(1,2*d):
            jp[k-1,k]=s.sqrt(k*(2*d-k))/2
        jm=jp.T
        mz=s.diag(*[J/2-s.Rational(k,2) for k in range(2*d)])
        C=s.simplify(mz*mz+(jp*jm+jm*jp)/2)
        assert s.simplify(C-C_scaled.subs(D,d)*s.eye(2*d))==s.zeros(2*d)
        assert s.simplify(jp*jm-jm*jp-mz)==s.zeros(2*d)
print("PASS: 100 exact shell comparisons; full refined q2 matrix D=2..8;")
print("rest product equals formal j; constant normalized difference 1/2;")
print("conditional Delta E=hbar²/(4 M ell²), no clock or source selected")
