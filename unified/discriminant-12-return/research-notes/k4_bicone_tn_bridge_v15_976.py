#!/usr/bin/env python3
"""Gravity v15.976: exact bicone quadratic/selection and Taub-NUT
fiber-charge comparison. No physical G or sourced coupling.
"""
import sympy as s
from fractions import Fraction
I=s.I
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-I],[I,0]])
sz=s.diag(1,-1);e2=s.eye(2);e4=s.eye(4)
J1=[s.kronecker_product(a,e2)/2 for a in (sx,sy,sz)]
J2=[s.kronecker_product(e2,a)/2 for a in (sx,sy,sz)]
L=[a+b for a,b in zip(J1,J2)]
A=[a-b for a,b in zip(J1,J2)]
L2=sum((x*x for x in L),s.zeros(4))
A2=sum((x*x for x in A),s.zeros(4))
assert L2+A2==3*e4
assert L2.eigenvals()=={s.Integer(0):1,s.Integer(2):3}
assert A2.eigenvals()=={s.Integer(3):1,s.Integer(1):3}
Ps=(2*e4-L2)/2;Pt=L2/2
assert Ps*Ps==Ps and Pt*Pt==Pt and Ps*Pt==s.zeros(4)
assert all(Ps*L[i]==s.zeros(4) for i in range(3))
assert all(Ps*A[i]*Ps==s.zeros(4) for i in range(3))
assert all(Pt*A[i]*Pt==s.zeros(4) for i in range(3))
assert any(Pt*A[i]*Ps!=s.zeros(4) for i in range(3))
Q=A[0]**2-A[1]**2
assert L2*Q-Q*L2==s.zeros(4)
assert Ps*Q==s.zeros(4) and Q*Ps==s.zeros(4)
assert Q.rank()==2
for D in range(2,101):
    je=Fraction(D-1,2);jq=Fraction(2*D-1,2)
    gap=jq-je
    assert gap==Fraction(D,2)
    assert jq not in (0,1) # bicone 0+1 never contains target q2 irrep
    for p in range(1,11):
        allowed=(gap.denominator==1 and gap<=p)
        if D%2: assert not allowed
        elif p>=D//2: assert allowed
        else: assert not allowed
q,k=s.symbols('q k',integer=True);psi=s.symbols('psi',real=True)
f=s.exp(s.I*k*psi)
charge=lambda v:-s.I*s.diff(v,psi)
raise_op=s.exp(s.I*q*psi)
assert s.simplify(charge(raise_op*f)-raise_op*charge(f)-q*raise_op*f)==0
assert s.simplify(charge(f)-k*f)==0
print('PASS: bicone L2+A2=3, singlet/triplet, rank2 triplet-only,')
print('shared-D spin rank/parity for D=2..100, Fourier charge raising')
