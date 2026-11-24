#!/usr/bin/env python3
"""Gravity v15.1407: intrinsic H2 Levi-Civita holonomy.
Loop at chi=ln2 yields 90-degree rotation, but no action selects that loop.
"""
import sympy as sp
import numpy as np
from scipy.linalg import expm
chi,r=sp.symbols('chi r',positive=True,real=True)
omega=-sp.cosh(chi)
assert sp.simplify(sp.diff(omega,chi)+sp.sinh(chi))==0
area=2*sp.pi*sp.integrate(r*r*sp.sinh(chi),(chi,0,sp.log(2)))
assert sp.simplify(area-sp.pi*r*r/2)==0
angle=-2*sp.pi*(sp.cosh(sp.log(2))-1)
assert sp.simplify(angle+sp.pi/2)==0
J=np.array([[0.,-1.],[1.,0.]])
computed=expm(-2*np.pi*np.cosh(np.log(2))*J)
expected=expm(-np.pi/2*J)
assert np.linalg.norm(computed-expected)<2e-12
for radius in [sp.Rational(1,4),sp.Rational(1,2)]:
 print('r',radius,'area',sp.simplify(area.subs(r,radius)),
       'rotation',sp.simplify(angle))
print('PASS canonical H2 connection curvature and conditional chi=ln2 quarter-turn')
print('NEGATIVE no physical action/EM-quarter bridge selects a closed disk of chi=ln2')
