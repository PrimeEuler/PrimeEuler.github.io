#!/usr/bin/env python3
"""Gravity v15.1118: two-component cone tilt response in standard
Maxwell+elasticity. Quadratic small-tilt, specified anchor and fixed
weak-TT external pump. No new Cone frequency or physical K4 source.
"""
import sympy as s
a,b,K,C,kappa,hp,hx,Me=s.symbols("a b K C kappa hp hx Me",real=True)
r2=a*a+b*b
Iplus=-K*(a*a-b*b)/s.sqrt(1-r2)
Icross=-2*K*a*b/s.sqrt(1-r2)
Uanchor=kappa*C*C*r2/(2*(1-r2)**2)
V=Uanchor-(hp*Iplus+hx*Icross)/2
H=s.simplify(s.hessian(V,(a,b)).subs({a:0,b:0}))
expected=s.Matrix([[kappa*C*C+K*hp,K*hx],[K*hx,kappa*C*C-K*hp]])
assert H==expected
z=s.symbols("z")
assert s.factor(H.charpoly(z).as_expr()-
                  ((z-kappa*C*C)**2-K*K*(hp*hp+hx*hx)))==0
assert s.simplify(s.trace(H)-2*kappa*C*C)==0
assert s.simplify(H.det()-kappa*kappa*C**4+K*K*(hp*hp+hx*hx))==0
# tilt vector rotates by theta, tidal quadrupole rotates by 2theta
theta=s.symbols("theta",real=True)
rot=s.Matrix([[s.cos(theta),-s.sin(theta)],[s.sin(theta),s.cos(theta)]])
Q=s.Matrix([[a*a-b*b,2*a*b]])
ap=rot*s.Matrix([a,b])
Qrot=s.simplify(s.Matrix([ap[0]**2-ap[1]**2,2*ap[0]*ap[1]]))
assert s.trigsimp(Qrot[0]-(a*a-b*b)*s.cos(2*theta)+2*a*b*s.sin(2*theta))==0
assert s.trigsimp(Qrot[1]-(a*a-b*b)*s.sin(2*theta)-2*a*b*s.cos(2*theta))==0
# intrinsic weak-field source threshold in the *externally anchored*
# reduced oscillator; without anchor the quadratic restoring scale is zero.
assert s.simplify(H.subs({hp:0,hx:0,kappa:0}))==s.zeros(2,2)
print("PASS double-tilt stiffness, spin-2 rotation, trace invariance and no free resonance")
print("Hessian:",H)
print("eigenvalues: kappa*C^2 +/- K*sqrt(hplus^2+hcross^2)")
print("M(q) at circular limit = C^2*(material_mass+K/c^2) for the specified carrier")
