#!/usr/bin/env python3
"""Gravity v15.986: an existing physical transverse tidal source
produces BOTH radial force and angular torque on a planar rotor.
This is ordinary Fermi-normal tidal mechanics, NOT new Cone coupling.
"""
import sympy as s
r,phi,M,B=s.symbols('r phi M B',real=True)
x=r*s.cos(phi);y=r*s.sin(phi)
V=M*B*x*y
expected=M*B*r*r*s.sin(2*phi)/2
assert s.trigsimp(V-expected)==0
Fr=-s.diff(V,r);torque=-s.diff(V,phi)
assert s.trigsimp(Fr+M*B*r*s.sin(2*phi))==0
assert s.trigsimp(torque+M*B*r*r*s.cos(2*phi))==0
assert s.trigsimp(torque.subs(phi,0)+M*B*r*r)==0
assert s.trigsimp(Fr.subs(phi,0))==0
assert s.trigsimp(torque.subs(phi,s.pi/4))==0
assert s.trigsimp(Fr.subs(phi,s.pi/4)+M*B*r)==0
print("PASS sourced tidal potential: radial force and angular torque independently nonzero")
