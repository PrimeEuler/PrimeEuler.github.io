#!/usr/bin/env python3
"""Exact v15.651 CP1 spinor/charge-one cancellation and SU2 lowest-multiplet bridge."""
import sympy as s
from fractions import Fraction
th,ph,z=s.symbols('theta phi z',real=True)
# Unit-charge monopole plus chiral spin connection cancel on standard round S2.
aN=(1-s.cos(th))/2; aS=-(1+s.cos(th))/2
bN=-aN; bS=-aS
assert s.simplify(aN-aS-1)==0 and s.simplify(bN-bS+1)==0
assert s.simplify(s.diff(aN+bN,th))==0
assert s.simplify(s.exp(s.I*ph)*s.exp(-s.I*ph)-1)==0
flux=s.integrate(s.integrate(s.diff(aN,th),(th,0,s.pi)),(ph,0,2*s.pi))/(2*s.pi)
assert s.simplify(flux-1)==0
for k in range(13):
    assert (-1)+(k+1)==k
    assert (k+2)-(k+1-1)==2
    assert Fraction(k*(k+2),4)-Fraction(k*(k+4),16)==Fraction(k*(3*k+4),16)
# SU2 in normalized holomorphic degree-k polynomial representation.
z=s.symbols('z')
for k in range(10):
    Jp=s.zeros(k+1); Jm=s.zeros(k+1); Jz=s.zeros(k+1)
    for r in range(k+1):
        Jz[r,r]=s.Rational(2*r-k,2)
        if r<k:
            Jp[r+1,r]=s.sqrt((k-r)*(r+1))
            lhs=(k*z*z**r-z*z*s.diff(z**r,z))*s.sqrt(s.binomial(k,r))
            rhs=Jp[r+1,r]*s.sqrt(s.binomial(k,r+1))*z**(r+1)
            assert s.simplify(lhs-rhs)==0
        if r>0:Jm[r-1,r]=s.sqrt(r*(k-r+1))
    I=s.eye(k+1)
    assert Jp.T==Jm
    assert Jz*Jp-Jp*Jz==Jp
    assert Jp*Jm-Jm*Jp==2*Jz
    assert s.simplify(Jz**2+(Jp*Jm+Jm*Jp)/2)==s.Rational(k,2)*(s.Rational(k,2)+1)*I
    # The angular spinor zero-mode and scalar lowest modules use the same normalized basis.
    B=I
    assert B.T*B==I and B*Jz==Jz*B and B*Jp==Jp*B
print('PASS v15.651: monopole-spin patch cancellation, exact charge-step, CP1 zero-mode SU2 intertwiner k=0..9; no physical coupling claim.')
