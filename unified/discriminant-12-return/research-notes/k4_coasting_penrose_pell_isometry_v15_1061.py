#!/usr/bin/env python3
"""Gravity v15.1061: coasting K4 null metric and discriminant-12 boost-isometry test."""
import sympy as s
eta,z,tau,tau0=s.symbols("eta z tau tau0",positive=True,real=True)
lam=2+s.sqrt(3)
a=tau/s.sqrt(3)
conf=s.sqrt(3)*s.log(tau/tau0)
assert s.simplify(s.diff(conf,tau)-1/a)==0
U,V=eta+z,eta-z
Up,Vp=lam*U,V/lam
eta_p=s.simplify((Up+Vp)/2)
assert s.simplify(eta_p-(2*eta+s.sqrt(3)*z))==0
assert s.simplify(Up*Vp-U*V)==0
def scale(e): return tau0*s.exp(e/s.sqrt(3))/s.sqrt(3)
ratio=s.simplify(scale(eta_p)**2/scale(eta)**2)
assert s.simplify(ratio-s.exp(2*(eta+s.sqrt(3)*z)/s.sqrt(3)))==0
assert s.simplify(s.diff(ratio,z))!=0
print("PASS: coasting conformal null metric; Pell boost preserves flat -dU dV but not physical K4 conformal metric")
print("eta_p=",eta_p,"pullback conformal ratio=",ratio)
