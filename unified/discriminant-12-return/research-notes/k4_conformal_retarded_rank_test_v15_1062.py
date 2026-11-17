#!/usr/bin/env python3
"""Gravity v15.1062: K4 conformal retarded tensor modes versus original Euler Green.

Source transfer is conditional on the already-reduced tensor equation.
The diagonal harmonic resolvent alone cannot source the rank-two q2 map.
"""
import sympy as s
k,zeta,dt,sigma,tau=s.symbols("k zeta dt sigma tau",positive=True)
mu2=(8*zeta-3)/s.Integer(9)
w=s.sqrt(k*k+mu2)
nu=s.sqrt(3*k*k+s.Rational(8,3)*zeta-1)
assert s.simplify(nu**2-3*w**2)==0
G=s.sin(w*dt)/w
assert s.simplify(s.diff(G,dt,2)+w**2*G)==0
assert G.subs(dt,0)==0
assert s.simplify(s.diff(G,dt).subs(dt,0)-1)==0
assert s.simplify(s.limit(G.subs(zeta,s.Rational(3,8)),k,0)-dt)==0
assert s.simplify(G.subs(zeta,s.Rational(3,8))-s.sin(k*dt)/k)==0
p=s.symbols("p",positive=True)
for Z in [s.Rational(3,8),s.Rational(3,4),s.Rational(3,2)]:
    resolvent=s.diag(1/(p*p+4+mu2.subs(zeta,Z)),1/(p*p+16+mu2.subs(zeta,Z)))
    assert s.simplify(resolvent.det())!=0
    assert resolvent[0,1]==0 and resolvent[1,0]==0
Gt=sigma**2/tau*s.sin(nu*s.log(tau/sigma))/nu
beta=3*k*k+s.Rational(8,3)*zeta
assert s.simplify(s.diff(Gt,tau,2)+3*s.diff(Gt,tau)/tau+beta*Gt/tau**2)==0
assert s.simplify(Gt.subs(tau,sigma))==0
assert s.simplify(s.diff(Gt,tau).subs(tau,sigma)-1)==0
print("PASS exact: Fourier retarded kernel, edge limit, Euler Green, diagonal full-rank resolvents")
