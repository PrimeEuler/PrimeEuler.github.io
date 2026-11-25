#!/usr/bin/env python3
"""Gravity v15.1417: frozen-tidal 1+1D H2/EM surrogate kinetic positivity
and a conditional superluminal characteristic. Not full Weyl EFT.
"""
import sympy as s
u,v,ux,vx,g,z,k=s.symbols("u v ux vx g z k",real=True)
D=1+u*u+v*v
G=s.Matrix([[1-u*u/D,-u*v/D],[-u*v/D,1-v*v/D]])
O=1/s.sqrt(D)
M=s.Matrix([[1,g*O*vx,-g*O*ux],
 [g*O*vx,G[0,0],G[0,1]],[-g*O*ux,G[1,0],G[1,1]]])
speednorm=(s.Matrix([ux,vx]).T*G*s.Matrix([ux,vx]))[0]
assert s.simplify(M.det()-(1-g*g*speednorm)/D)==0
K=s.Matrix([[1,-g*z],[-g*z,1]])
assert s.simplify(K.det()-(1-g*g*z*z))==0
w2=s.symbols("w2",real=True)
disp=s.factor((w2*K-k*k*s.eye(2)).det())
assert s.simplify(disp-(w2*(1-g*z)-k*k)*(w2*(1+g*z)-k*k))==0
for val in [s.Rational(1,10),s.Rational(1,4)]:
 print("g*s",val,"speeds",float(1/s.sqrt(1+val)),float(1/s.sqrt(1-val)))
assert float(1/s.sqrt(1-s.Rational(1,10)))>1
print("PASS positive kinetic condition g^2 |grad phi|_H^2 < 1")
print("NEGATIVE frozen tidal truncation can give superluminal characteristic")
print("OPEN complete covariant Weyl operator principal symbol and causality")
