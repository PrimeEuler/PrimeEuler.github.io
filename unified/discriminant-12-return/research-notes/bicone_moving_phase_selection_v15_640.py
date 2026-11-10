#!/usr/bin/env python3
"""Exact classical Fourier and finite quantum angular selection test for Lane A v15.640."""
import sympy as s
from itertools import product
t1,t2,alpha=s.symbols('theta1 theta2 alpha',real=True)
u=s.cos(t1-t2)-3*s.cos(t1-alpha)*s.cos(t2-alpha)
reduced=-s.cos(t1-t2)/2-s.Rational(3,2)*s.cos(t1+t2-2*alpha)
assert s.trigsimp(u-reduced)==0
assert s.trigsimp(u.subs({t1:t1+s.pi,t2:t2+s.pi})-u)==0
assert s.trigsimp(u.subs(t1,t1+s.pi)+u)==0
# Fourier components shift both body angular momenta by one, preserving total parity.
steps=[(1,-1,0),(-1,1,0),(1,1,-2),(-1,-1,2)]
assert all((a+b)%2==0 and a+b+c==0 for a,b,c in steps)
levels=range(-2,3)
basis=list(product(levels,repeat=2))
lookup={x:i for i,x in enumerate(basis)}
H=s.zeros(len(basis))
for col,(a,b) in enumerate(basis):
    for da,db,amplitude in [(1,-1,-s.Rational(1,4)),
                            (-1,1,-s.Rational(1,4)),
                            (1,1,-s.Rational(3,4)),
                            (-1,-1,-s.Rational(3,4))]:
        if (a+da,b+db) in lookup:
            H[lookup[(a+da,b+db)],col]+=amplitude
P=s.diag(*[s.Integer(-1)**(a+b) for a,b in basis])
S=s.zeros(len(basis))
for col,(a,b) in enumerate(basis):
    S[lookup[(b,a)],col]=1
assert H==H.T and P*H==H*P and S*H==H*S and P*S==S*P
assert s.trace(P)==1 # 13 even, 12 odd on this chosen 5x5 cutoff
print("PASS: exact dipole Fourier decomposition, combined Pi rotation, 25x25 rotor parity and exchange symmetries")
print("Quantum rotor quantization is a diagnostic, not part of the original classical simulation.")
