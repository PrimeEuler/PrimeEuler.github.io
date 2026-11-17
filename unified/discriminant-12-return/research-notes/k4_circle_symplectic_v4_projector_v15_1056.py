#!/usr/bin/env python3
"""Gravity v15.1056: exact symplectic secant-circle lift, V4 projectors, q2 controls."""
import sympy as s
from itertools import combinations
k,n,A,p=s.symbols('k n A p',positive=True)
x=A*(k*k-n)/(k*k+n)
f=s.factor(s.diff(x,k))
Px=p/f
assert s.simplify(s.diff(x,k)*s.diff(Px,p)-s.diff(x,p)*s.diff(Px,k))==1
assert s.simplify(Px*s.diff(x,k)-p)==0
H=s.Matrix([[(-1)**(a*i+b*j) for i in range(2) for j in range(2)] for a in range(2) for b in range(2)])/2
assert H.T*H==s.eye(4)
projs=[]
for inds in combinations(range(4),2):
    C=s.zeros(4)
    for i in inds:
        v=H.row(i).T
        C+=v*v.T
    assert C*C==C and C.T==C and C.rank()==2
    projs.append(C)
assert len(projs)==6
for a in range(2):
    for b in range(2):
        U=s.zeros(4)
        for i in range(2):
            for j in range(2):
                U[2*(i^a)+(j^b),2*i+j]=1
        for C in projs:
            assert U*C==C*U
for L in range(3,16):
    w=s.Rational(L+1,4)
    P=s.zeros(L+1)
    P[1,1]=P[L-1,L-1]=1
    T=s.zeros(L+3,L+1)
    T[0,1]=s.sqrt(w)
    T[L+2,L-1]=s.sqrt(w)
    assert T.T*T==w*P and T.rank()==P.rank()==2
print('PASS: canonical cotangent lift, six V4 rank-two projectors, q2 comparison L=3..15')
