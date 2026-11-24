#!/usr/bin/env python3
"""Gravity v15.1406: action-based auxiliary null-Q two-sector transport.
Tests 3:1 interval vs probabilities, Noether norm, flat connection and
SU2 scalar-intertwiner Casimir obstruction. NOT a physical Cone force.
"""
import sympy as s
import numpy as np
from scipy.linalg import expm
D,k,Q=s.symbols('D k Q',positive=True,real=True)
a=s.Rational(1,16);b=s.Rational(1,4)
sx=s.Matrix([[0,1],[1,0]])
assert s.simplify(sx*sx-s.eye(2))==s.zeros(2)
assert s.simplify(s.exp(-s.I*k*a*sx)[1,0]+s.I*s.sin(k*a))==0
assert s.simplify(s.exp(-s.I*k*(b-a)*sx)[1,0]+s.I*s.sin(k*(b-a)))==0
pin=s.sin(k*a)**2;pout=s.sin(k*(b-a))**2
assert s.simplify((b-a)/a)==3
assert s.limit(pout/pin,k,0)==9
assert s.simplify((pout/pin).subs(k,8*s.pi/3))==4
j=(D-1)/2;J=(2*D-1)/2
assert s.simplify(J*(J+1)-j*(j+1)-3*D**2/4)==0
assert s.diff(k*sx,Q)==s.zeros(2)
for kval in [.1,1,4,8*np.pi/3]:
    e=np.array([1+0j,0j]);S=np.array(sx).astype(float)
    U1=expm(-1j*kval*float(a)*S);U2=expm(-1j*kval*float(b-a)*S)
    assert abs(np.vdot(U2@U1@e,U2@U1@e).real-1)<1e-13
    x=abs((U1@e)[1])**2;y=abs((U2@e)[1])**2
    print(dict(k=kval,inner_probability=x,outer_probability=y,ratio=y/x),flush=True)
print('PASS 3:1 interval, 9:1 weak probability, k-dependent finite probabilities')
print('PASS SU2 scalar mixing barred by physical Casimir gap 3D²/4')
print('NEGATIVE unitary two-state Q-connection pure gauge and k arbitrary')
