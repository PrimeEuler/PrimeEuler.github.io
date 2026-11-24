#!/usr/bin/env python3
"""v15.1405: exact divergence-free null-coordinate currents do not fix
a uniform affine transport weight. Integration of J^V along V is a
candidate weight, NOT automatically the flux across a physical detector.
"""
import sympy as s
U,V,c,d,h=s.symbols("U V c d h",positive=True,real=True)
Ju=-d*U;Jv=c+d*V
assert s.simplify(s.diff(Ju,U)+s.diff(Jv,V))==0
Winner=s.integrate(Jv,(V,0,h))
Wouter=s.integrate(Jv,(V,h,4*h))
ratio=s.factor(Wouter/Winner)
assert s.simplify(ratio-(3*c+s.Rational(15,2)*d*h)/(c+d*h/2))==0
assert s.simplify(ratio.subs(d,0))==3
assert s.simplify(ratio.subs(d,c/h))==7
assert s.limit(ratio,d,s.oo)==15
print("PASS current divergence exactly zero")
print("null-line candidate weighted intervals:",Winner,Wouter)
print("uniform d=0 ratio",ratio.subs(d,0))
print("redistributed d*h=c ratio",ratio.subs(d,c/h))
print("general ratio",ratio)
print("NEGATIVE conservation does not force uniform null-line transport density")
