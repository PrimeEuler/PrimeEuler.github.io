#!/usr/bin/env python3
"""Gravity v15.920: independent 2p/3p hydrogen lifetime ratio benchmark.
Ordinary Coulomb QM/SO(4,2), not Cone-specific. Experimental lifetimes from
Chupp, Dotchin & Pegg, Phys. Rev. 175, 44 (1968), 2p 1.60(1) ns and
3p 5.5(2) ns. No theoretical Einstein A values used as experimental data.
"""
import math
import sympy as s
from sympy.physics.hydrogen import R_nl
r=s.symbols('r',positive=True)
def radial(n,l,m,j):
    return s.simplify(s.integrate(R_nl(n,l,r)*R_nl(m,j,r)*r**3,(r,0,s.oo)))
d21=radial(2,1,1,0)
d31=radial(3,1,1,0)
d32=radial(3,1,2,0)
assert s.simplify(d21-128*s.sqrt(6)/243)==0
assert s.simplify(d31-27*s.sqrt(6)/128)==0
assert s.simplify(d32-27648*s.sqrt(3)/15625)==0
# All p->s branches have the same nonrelativistic angular E1 factor.
# A_if scales omega_if^3 * |radial|^2; omega ratios from E_n=-Ry/n^2.
A31=s.simplify(s.Rational(32,27)**3*(d31/d21)**2)
A32=s.simplify(s.Rational(5,27)**3*(d32/d21)**2)
assert A31==s.Rational(2187,8192)
assert A32==s.Rational(69984,1953125)
ratio=s.simplify(A31+A32)
assert ratio==s.Rational(4844793303,16000000000)
tau2,sigma2=1.60,.01
tau3,sigma3=5.5,.2
prediction=tau2/float(ratio)
sigma_prediction=sigma2/float(ratio)
pull=(tau3-prediction)/math.hypot(sigma3,sigma_prediction)
assert abs(pull)<2
print("radial Bohr-unit matrix elements",d21,d31,d32)
print("3p branches relative to 2p:",A31,A32,"total",ratio)
print("3p branching",float(A31/ratio),float(A32/ratio))
print("3p predicted lifetime ns",prediction,"±",sigma_prediction)
print("3p measured lifetime ns",tau3,"±",sigma3,"pull",pull)
print("PASS exact E1 radial/angular/frequency ratios and independent 3p lifetime")
