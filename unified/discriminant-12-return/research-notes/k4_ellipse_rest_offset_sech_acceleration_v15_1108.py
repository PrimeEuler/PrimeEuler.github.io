#!/usr/bin/env python3
"""Gravity v15.1108: projected cone ellipse, rest offset, sech trace,
and CONDITIONAL areal-law acceleration/deceleration dynamics.

Source: PaperA Conic Theorem normalized plane T+e X=C on cone T²=X²+Y².
The 2D projected ellipse differs from intrinsic ellipse metric in its
3D cutting plane. Maxwell magnetic current is not derived by this geometry.
"""
import sympy as s
C,e,phi,u,J=s.symbols('C e phi u J', positive=True, real=True)
X,Y,T=s.symbols('X Y T', real=True)
center=-C*e/(1-e**2)
A=C/(1-e**2)
B=C/s.sqrt(1-e**2)
identity=s.expand((C-e*X)**2-X**2-Y**2)
assert s.simplify(identity+(1-e**2)*(X-center)**2+Y**2-C**2/(1-e**2))==0
assert s.simplify(A**2-B**2-center**2)==0
assert s.simplify(-center/A-e)==0
# Projected ellipse is focus-at-origin; intrinsic 3D section has a
# different eccentricity, per the archived PaperA theorem.
e3=s.sqrt(2)*e/s.sqrt(1+e**2)
assert s.simplify(e3**2-2*e**2/(1+e**2))==0
r=C/(1+e*s.cos(phi))
assert s.simplify(r+e*r*s.cos(phi)-C)==0
series=s.series(r,e,0,3).removeO().expand()
assert s.trigsimp(series-C*(1-e*s.cos(phi)+e**2*(1+s.cos(2*phi))/2))==0
# Secant label is k=T+X, and the hyperbola shell height Y changes.
k=s.simplify(r*(1+s.cos(phi)))
yval=r*s.sin(phi)
assert s.trigsimp((k*k+yval*yval)/(2*k)-r)==0
assert s.trigsimp((k*k-yval*yval)/(2*k)-r*s.cos(phi))==0
assert s.simplify(s.tanh(u)**2+s.sech(u)**2-1)==0
ru=C/(1+e*s.tanh(u))
Yu=ru*s.sech(u)
assert s.simplify(ru*(1+e*s.tanh(u))-C)==0
assert s.trigsimp(s.diff(s.atanh(s.cos(phi)),phi)+1/s.sin(phi))==0
# A clock/physical force needs another law. With imposed specific angular
# momentum J=r² phi_dot, the inverse-square radial force follows.
phidot=J/r**2
rdot=s.trigsimp(s.diff(r,phi)*phidot)
rddot=s.trigsimp(s.diff(rdot,phi)*phidot)
ar=s.trigsimp(rddot-r*phidot**2)
assert s.trigsimp(rdot-e*J*s.sin(phi)/C)==0
assert s.trigsimp(rddot-e*J**2*s.cos(phi)/(C*r**2))==0
assert s.trigsimp(ar+J**2/(C*r**2))==0
assert s.trigsimp(r*s.diff(phidot,phi)*phidot+2*rdot*phidot)==0
assert s.simplify(rdot.subs(phi,0))==0
assert s.simplify(rdot.subs(phi,s.pi))==0
assert s.simplify(rddot.subs(phi,s.pi/2))==0
print('PASS: focus-offset, projected and intrinsic eccentricity, exact sech')
print('PASS: Kepler acceleration/deceleration ONLY after imposed areal clock J')
print('focus center:',center,'radial velocity:',rdot)
