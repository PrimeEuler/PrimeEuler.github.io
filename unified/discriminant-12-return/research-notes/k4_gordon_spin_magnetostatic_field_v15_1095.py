#!/usr/bin/env python3
"""Gravity v15.1095: Gaussian Gordon spin current -> magnetostatic Maxwell field.

This is a sourced, low-energy magnetostatic comparator, not a
self-consistent stationary Dirac-Maxwell or curved Einstein-K4 solution.
Unit conventions hbar,c,mu0 are absorbed into K and Maxwell equations.
"""
import sympy as s
kx,ky,kz,L,K=s.symbols("kx ky kz L K",positive=True,real=True)
k=s.Matrix([kx,ky,kz]); k2=k.dot(k)
zhat=s.Matrix([0,0,1])
rh=s.exp(-L**2*k2/4)
j=s.I*K*k.cross(zhat)*rh
B=s.simplify(s.I*k.cross(j)/k2)
Bexpected=K*rh*(zhat-k*kz/k2)
assert (B-Bexpected).applyfunc(s.simplify)==s.zeros(3,1)
assert s.simplify(k.dot(j))==0
assert s.simplify(k.dot(B))==0
assert (s.I*k.cross(B)-j).applyfunc(s.simplify)==s.zeros(3,1)
r=s.symbols("r",positive=True)
radial=s.integrate(r**2*s.exp(-L**2*r**2/2),(r,0,s.oo))
# angular integral sin^2 theta = 8*pi/3
energy=s.simplify(s.Rational(1,2)*K**2*s.Rational(8,3)*s.pi*
                  radial/(2*s.pi)**3)
assert s.simplify(energy-K**2/(3*(2*s.pi)**s.Rational(3,2)*L**3))==0
assert s.simplify(energy.subs(L,L/2)/energy-8)==0
assert s.simplify(energy.subs(L,2*L)/energy-s.Rational(1,8))==0
print("PASS: spin curl transverse, sourced Maxwell magnetostatics and exact finite field energy")
print("Bhat=",Bexpected)
print("energy=",energy)
