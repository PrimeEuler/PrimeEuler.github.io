#!/usr/bin/env python3
"""Dimension-dependence of quadratic moments and hot-bath cross covariance."""
import sympy as s
x,T,mu,D,q,v,L,d=s.symbols('x T mu D q v L d',positive=True)
segment=s.integrate(1-x*x,(x,-1,1))
assert segment==s.Rational(4,3)
assert segment/2==s.Rational(2,3)
assert s.simplify((d-1)/d).subs(d,3)==s.Rational(2,3)
h=-mu/(2*T)
Th=2*T*T/mu
qh=q/(2*h)
CTq=s.factor(Th*(qh*(2*D*v*v)+(q/L)*(2*D*L)))
assert s.simplify(CTq.subs(v*v,mu/T))==0
print('Parabolic segment area:', segment, 'rectangle fraction:',segment/2)
print('Sphere S^(d-1) quadratic transverse fraction:',(d-1)/d)
print('Unaveraged covariance d[T,q]/dt:',CTq)
print('Kepler orbit average d[T,q]/dt =',s.simplify(CTq.subs(v*v,mu/T)))
print('Kepler orbit average d[T,e^2]/dt = 0 by e^2=1-q^2')
