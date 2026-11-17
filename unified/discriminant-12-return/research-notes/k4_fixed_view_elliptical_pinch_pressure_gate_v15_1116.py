#!/usr/bin/env python3
"""Gravity v15.1116: a fixed oblique camera circularizes just one
nonzero cone ellipse eccentricity; smooth elliptical magnetic pinch
requires anisotropic/nonbarotropic support beyond scalar pressure.

2D x-invariant magnetostatic stream field B=(0,Psi_z,-Psi_y),
Jx=-Laplacian(Psi)/mu0. Lorentz force F=J cross B=-DeltaPsi grad Psi/mu0.
"""
import sympy as s
q,e=s.symbols("q e",real=True)
condition=s.expand((1-q*e)**2-(1-e*e))
assert s.simplify(condition-e*((1+q*q)*e-2*q))==0
# e=0: fixed-T circle; otherwise e=2q/(1+q²) for
# circle image of the tilted cone plane under U=X+qT,V=Y.
assert s.simplify(condition.subs(e,2*q/(1+q*q)))==0
y,z,A,B=s.symbols("y z A B",positive=True)
f=y*y/A**2+z*z/B**2
Psi=(1-f)**4
lap=s.diff(Psi,y,2)+s.diff(Psi,z,2)
Fy=-lap*s.diff(Psi,y)
Fz=-lap*s.diff(Psi,z)
forcecurl=s.factor(s.diff(Fz,y)-s.diff(Fy,z))
assert forcecurl!=0
assert s.simplify(forcecurl.subs(B,A))==0
# A scalar pressure force has identically zero curl.
# In the smooth elliptical patch A!=B,y*z!=0 the curl is nonzero.
# Piecewise linear stream profiles make DeltaPsi constant in the
# interior, but their derivative jumps at the boundary (sheet current).
Psi_linear=1-f
lap_linear=s.simplify(s.diff(Psi_linear,y,2)+s.diff(Psi_linear,z,2))
assert s.simplify(s.diff(lap_linear,y))==0
assert s.simplify(s.diff(lap_linear,z))==0
print("PASS fixed oblique view circularizes a unique nonzero ellipticity")
print("PASS smooth 2D elliptical magnetic pinch scalar-pressure no-go")
print("force curl=",forcecurl)
print("linear-stream interior exception requires surface sheet support")
