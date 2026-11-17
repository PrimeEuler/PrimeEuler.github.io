#!/usr/bin/env python3
"""Gravity v15.1107: Ampere/Maxwell magnetic tension and plus/cross
tidal quadrupole selection of an azimuthal curl ring.

SI mu0=1 for the angular demonstration. The tensor T_ij here is the
spatial momentum flux u delta_ij - E_i E_j - B_i B_j. For a GW
propagating along ring axis x, plus stretches y against z.
An axisymmetric magnetic ring has zero integrated TT transverse stress;
a cos(2phi) anisotropy supplies a plus-channel overlap.
This is a local weak-field stress-work comparison, not independent G.
"""
import sympy as s
phi, b0, eps, dh = s.symbols('phi b0 eps dh', real=True)
By=-b0*s.sin(phi)
Bz=b0*s.cos(phi)
Tdiff=s.simplify(-By**2+Bz**2)    # Tyy-Tzz
Tcross=s.simplify(-By*Bz)         # Tyz
assert s.simplify(Tdiff-b0**2*s.cos(2*phi))==0
assert s.integrate(Tdiff,(phi,0,2*s.pi))==0
assert s.integrate(Tcross,(phi,0,2*s.pi))==0
# B_phi(phi)^2=b0^2[1+eps cos(2phi)], |eps|<1 for positivity.
Tplus=b0**2*(1+eps*s.cos(2*phi))*s.cos(2*phi)
assert s.simplify(s.integrate(Tplus,(phi,0,2*s.pi))-s.pi*b0**2*eps)==0
# Weak TT stress/strain-rate power density -h_dot/2(Tyy-Tzz).
work=-dh*Tplus/s.Integer(2)
assert s.simplify(s.integrate(work,(phi,0,2*s.pi))+s.pi*b0**2*eps*dh/2)==0
# A sin(2phi) envelope instead selects the cross component.
Tcross_aniso=b0**2*(1+eps*s.sin(2*phi))*s.sin(2*phi)/2
assert s.simplify(s.integrate(Tcross_aniso,(phi,0,2*s.pi))-s.pi*b0**2*eps/2)==0
print('PASS: axisymmetric Ampere/Maxwell curl tension TT null; m=2 quadrupole opens pump')
print('plus TT stress angular overlap=',s.integrate(Tplus,(phi,0,2*s.pi)))
