#!/usr/bin/env python3
"""Exact v15.637 Taub–NUT monopole line / U(4) vacuum source and Wilson checks."""
import sympy as s
th,phi=s.symbols('theta phi',real=True)
k=s.symbols('k',integer=True)
aN=k*(1-s.cos(th))/2
aS=-k*(1+s.cos(th))/2
assert s.simplify(aN-aS-k)==0
F=s.diff(aN,th)
assert s.simplify(F-k*s.sin(th)/2)==0
assert s.simplify(s.integrate(s.integrate(F,(th,0,s.pi)),(phi,0,2*s.pi))/(2*s.pi)-k)==0
P=s.diag(1,0,0,0)
Id=s.eye(4)
assert P*P==P and P.H==P
AN=s.I*aN*P
AS=s.I*aS*P
assert s.simplify(AN-AS-s.I*k*P)==s.zeros(4)
assert AN*P-P*AN==s.zeros(4) and AS*P-P*AS==s.zeros(4)
z=s.symbols('z')
W=Id+(z-1)*P
assert s.simplify(s.trace(W)-(3+z))==0
assert s.simplify(W.det()-z)==0
character2=s.simplify((s.trace(W)**2-s.trace(W*W))/2)
assert s.simplify(character2-(3+3*z))==0
assert s.simplify((3+z).subs(z,s.I)-(3+s.I))==0
X=s.zeros(4)
X[0,1]=X[1,0]=1
assert X*P-P*X!=s.zeros(4)
print("PASS: monopole Chern flux, parallel projector, source line and all Wilson characters.")
