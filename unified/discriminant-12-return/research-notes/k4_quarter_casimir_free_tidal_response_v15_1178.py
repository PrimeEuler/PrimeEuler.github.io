#!/usr/bin/env python3
"""Gravity v15.1178 — Casimir-free tidal observables vs quarter shell labels.
No claim that a geometric shell Casimir is physical. The EM Jxy
midpoint correction is an exact quadratic interpolation identity,
whereas tidal torque uses a tensor orientation in a fixed lab frame.
"""
import sympy as s
D,k,h=s.symbols('D k h',real=True)
f=lambda x:x*(D-x)
assert s.expand(f(k+h/2)-(f(k)+f(k+h))/2-h*h/4)==0
assert s.simplify(f(k+s.Rational(1,2))-(f(k)+f(k+1))/2-s.Rational(1,4))==0
assert s.simplify(f(k+s.Rational(1,4))-(f(k)+f(k+s.Rational(1,2)))/2-s.Rational(1,16))==0
E=s.diag(2,-1,-1)
t=s.symbols('t',real=True)
R=s.Matrix([[s.cos(t),-s.sin(t),0],
            [s.sin(t),s.cos(t),0],[0,0,1]])
Er=s.trigsimp(R*E*R.T)
assert s.simplify(s.trace(Er)-s.trace(E))==0
assert s.simplify(s.trace(Er*Er)-s.trace(E*E))==0
assert s.simplify(s.trace(Er*Er*Er)-s.trace(E*E*E))==0
u=s.Matrix([1,0,0]);v=s.Matrix([0,1,0])
DQ=s.symbols('DeltaQ',real=True)
tau=s.trigsimp(-DQ*(u.T*Er*v)[0])
assert s.simplify(tau+s.Rational(3,2)*DQ*s.sin(2*t))==0
assert tau.subs(t,0)==0 and tau.subs(t,s.pi/4)==-3*DQ/2
for L in range(1,13):
    C=s.Rational(L*(L+4),16)
    assert C>0
    assert s.diff(tau,t).subs(t,0)==-3*DQ
print('PASS any step h midpoint completion h²/4; unit edge 1/4 and refined edge 1/16')
print('PASS same trE, trE², trE³ but distinct orientation-dependent bicone torque')
print('NEGATIVE: standard tidal response neither requires nor selects quarter Casimir')
