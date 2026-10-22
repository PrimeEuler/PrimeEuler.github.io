#!/usr/bin/env python3
"""Exact high-speed bath diffusion and phase Gram witness gate."""
import sympy as S
z,e,C=S.symbols("z e C",positive=True)
A=C*(1-2*z); B=2*C*z*(1-z)
q=S.sqrt(1-z)
W=4*S.sqrt(z)/(3*(1+S.sqrt(z)))
def gen(f): return S.simplify(A*S.diff(f,z)+B*S.diff(f,z,2)/2)
qw=S.factor(gen(q).subs(z,e**2))
ww=S.factor(gen(W).subs(z,e**2))
assert S.simplify(qw + C*(3*(1-e**2)-1)/(4*S.sqrt(1-e**2)))==0
assert S.simplify(ww + C*(e**2+2*e-1)/(3*e*(e+1)**2))==0
p=S.Integer(1)
assert S.simplify(A*p-S.diff(B*p,z)/2)==0
assert S.simplify(S.integrate(z,(z,0,1))-S.Rational(1,2))==0
assert S.simplify(S.integrate(q,(z,0,1))-S.Rational(2,3))==0
assert S.simplify(S.integrate(8*e**2/(3*(1+e)),(e,0,1))-(8*S.log(2)-4)/3)==0
print("drift-zero e² =",S.Rational(2,3))
print("Lq =",qw)
print("LW =",ww)
print("L W at e²=2/3 =",S.simplify(ww.subs(e,S.sqrt(S.Rational(2,3)))))
print("zero L W at e =",S.sqrt(2)-1)
print("stationary p(e²)=1, E[e²] =",S.Rational(1,2))
print("stationary E[q] =",S.Rational(2,3))
print("stationary E[W] =",S.simplify((8*S.log(2)-4)/3))
print("W at q-drift-zero =",S.simplify(W.subs(z,S.Rational(2,3))))
