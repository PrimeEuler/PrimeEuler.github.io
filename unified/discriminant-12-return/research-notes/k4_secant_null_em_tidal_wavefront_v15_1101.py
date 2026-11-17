#!/usr/bin/env python3
"""Gravity v15.1101: confocal acceleration secant and retarded null-front circles.
Source-free leading EM radiation has B azimuthal on a spherical wavefront;
its locally collinear TT stress is zero, NOT a full gravitational-wave calculation.
"""
import sympy as s
u,R,k,c,t,x=s.symbols("u R k c t x",positive=True,real=True)
te_c=R*s.sinh(u)
xe=R*(s.cosh(u)-1)
radius2=s.expand((c*t-te_c)**2-(x-xe)**2)
at0=s.factor(radius2.subs({t:0,x:0}))
assert s.simplify(at0-4*R**2*s.sinh(u/2)**2)==0
kcircle=s.simplify(s.expand(at0.rewrite(s.exp).subs(u,s.log(k/R))))
assert s.simplify(kcircle-R*(R-k)**2/k)==0
# Physical retarded emission to (t,x)=(0,0) requires u<0, k<R.
th,ph,C=s.symbols("th ph C",real=True)
n=s.Matrix([s.cos(th),s.sin(th)*s.cos(ph),s.sin(th)*s.sin(ph)])
e_th=s.Matrix([-s.sin(th),s.cos(th)*s.cos(ph),s.cos(th)*s.sin(ph)])
e_ph=s.Matrix([0,-s.sin(ph),s.cos(ph)])
assert (n.cross(e_th)-e_ph).applyfunc(s.trigsimp)==s.zeros(3,1)
E=C*s.sin(th)*e_th
B=n.cross(E)  # radiation units c_light=1
rho=s.simplify((E.dot(E)+B.dot(B))/2)
stress=s.eye(3)*rho-E*E.T-B*B.T
assert s.simplify(rho-C**2*s.sin(th)**2)==0
assert (stress-rho*n*n.T).applyfunc(s.trigsimp)==s.zeros(3)
proj=s.eye(3)-n*n.T
TT=proj*stress*proj-proj*s.trace(proj*stress)/2
assert TT.applyfunc(s.trigsimp)==s.zeros(3)
print("PASS retarded circular wavefront from confocal secant k, 0<k<R")
print("r_perp^2=",kcircle)
print("PASS polar E / azimuthal B, null stress rho*n*n and locally collinear TT=0")
