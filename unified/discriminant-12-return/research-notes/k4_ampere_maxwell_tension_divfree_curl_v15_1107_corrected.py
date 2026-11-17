#!/usr/bin/env python3
"""Gravity v15.1107 canonical physical correction: divergence-free anisotropic curl.

This is a local transverse disk field. For an extended physical source one
must provide bounded radial profile, currents and support. SI mu0=1 here.
Axes: magnetic ring around x; transverse y=r cos phi,z=r sin phi; GW along x.
"""
import sympy as s
p,e,r,b=s.symbols('p e r b',real=True)
# Solenoidal through a stream function Psi=-b r²(1+e cos2p)/2:
# Br=(1/r) partial_phi Psi; Bphi=-partial_r Psi.
Br=e*b*r*s.sin(2*p)
Bphi=b*r*(1+e*s.cos(2*p))
assert s.trigsimp(s.diff(r*Br,r)/r+s.diff(Bphi,p)/r)==0
By=s.trigsimp(Br*s.cos(p)-Bphi*s.sin(p))
Bz=s.trigsimp(Br*s.sin(p)+Bphi*s.cos(p))
assert s.trigsimp(By-b*r*(e-1)*s.sin(p))==0
assert s.trigsimp(Bz-b*r*(e+1)*s.cos(p))==0
# T^ij = u delta_ij - B_i B_j (x-axis propagation).
Tplus=s.expand(Bz**2-By**2)   # Tyy-Tzz
Tcross=s.expand(-By*Bz)       # Tyz
plusint=s.simplify(s.integrate(s.trigsimp(Tplus),(p,0,2*s.pi)))
crossint=s.simplify(s.integrate(s.trigsimp(Tcross),(p,0,2*s.pi)))
assert s.simplify(plusint-4*s.pi*e*b**2*r**2)==0
assert crossint==0
assert plusint.subs(e,0)==0
# Radius-weighted disk integral through radius L; local unbounded profile
# is restricted to a patch and requires a smooth external completion.
L=s.symbols('L',positive=True)
plusdisk=s.simplify(s.integrate(plusint*r,(r,0,L)))
assert s.simplify(plusdisk-s.pi*e*b**2*L**4)==0
print('PASS: divergence-free elliptical magnetic circulation, standard TT m=2 selection')
print('angular plus stress=',plusint,'cross stress=',crossint)
print('disk plus stress=',plusdisk)
