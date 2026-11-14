#!/usr/bin/env python3
"""Gravity v15.986: sourced electromagnetic/tidal Schwinger terms
versus the existing fixed-angular-momentum rotor (v15.900).
Ordinary 2D isotropic Cartesian oscillator identity Lz=2*hbar*Jy.
Radial r is an independently stipulated classical parameter, NOT
a quantized fixed-N rotor coordinate. No K4-specific source.
"""
import sympy as s
I=s.I
for D in range(2,13):
    j=s.Rational(D-1,2)
    x=s.zeros(D);y=s.zeros(D)
    z=s.diag(*[j-a for a in range(D)])
    for a in range(D-1):
        v=s.sqrt((a+1)*(D-a-1))/2
        x[a,a+1]=v;x[a+1,a]=v
        y[a,a+1]=-I*v;y[a+1,a]=I*v
    assert x*y-y*x==I*z
    assert y*z-z*y==I*x
    assert z*x-x*z==I*y
    y2=y*y
    assert all(y2[a,b]==0 for a in range(D) for b in range(D) if abs(a-b) not in (0,2))
    assert all(y2[a,a+1]==0 for a in range(D-1))
    assert all(x[a,a+1]!=0 for a in range(D-1))
    assert all(s.simplify(y2[a,a]-(j*(j+1)-(j-a)**2)/2)==0 for a in range(D))
    if D>=3:assert any(y2[a,a+2]!=0 for a in range(D-2))
    assert x*y2-y2*x==I*(z*y+y*z)
    assert y*x-x*y==-I*z
    assert y*z-z*y==I*x
    if D==5:
        assert y2==s.Matrix([[1,0,-s.sqrt(6)/2,0,0],[0,s.Rational(5,2),0,-s.Rational(3,2),0],[-s.sqrt(6)/2,0,3,0,-s.sqrt(6)/2],[0,-s.Rational(3,2),0,s.Rational(5,2),0],[0,0,-s.sqrt(6)/2,0,1]])
print("PASS D=2..12: centrifugal Jy² connects Δk=0,±2; Jx/Jy Δk=±1; tidal Jx torque, magnetic Jy conservation.")
