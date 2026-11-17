#!/usr/bin/env python3
"""Gravity v15.1111 — time-dependent cone-shaped Maxwell ellipse, sech timing
and tidal-work parity. Time-dependent shapes are PRESCRIBED, not a force law.

A=(Psi,0,0), Psi=f(x)*psi0*(1-q_e)^4 on q_e<1 with the cone
ellipse's A,B,d prescribed by e(t); compact in x as v15.1110.
E=-partial_t A, B=curl A, rho=div E, J=curl B-partial_t E
in c=epsilon0=mu0=1. The prescribed conserved current is NOT yet
a self-consistent actuator/cavity constitutive model.
"""
import sympy as s
from scipy.integrate import quad
import numpy as np
x,y,z,t=s.symbols('x y z t',real=True)
Psi=s.Function('Psi')(x,y,z,t)
E=s.Matrix([-s.diff(Psi,t),0,0])
B=s.Matrix([0,s.diff(Psi,z),-s.diff(Psi,y)])
rho=s.diff(E[0],x)
J=s.Matrix([-s.diff(Psi,y,2)-s.diff(Psi,z,2)+s.diff(Psi,t,2),
            s.diff(Psi,x,y),s.diff(Psi,x,z)])
curl=lambda v:s.Matrix([s.diff(v[2],y)-s.diff(v[1],z),
                        s.diff(v[0],z)-s.diff(v[2],x),
                        s.diff(v[1],x)-s.diff(v[0],y)])
div=lambda v:s.diff(v[0],x)+s.diff(v[1],y)+s.diff(v[2],z)
assert s.simplify(div(B))==0
assert (curl(E)+B.diff(t)).applyfunc(s.simplify)==s.zeros(3,1)
assert (curl(B)-E.diff(t)-J).applyfunc(s.simplify)==s.zeros(3,1)
assert s.simplify(rho.diff(t)+div(J))==0
# Flat-space integrated Poynting energy of compact fields obeys
# d/dt int[(E^2+B^2)/2] = -int J.E (no boundary flux).
# This follows from pointwise vector identity div(E cross B)
# =B.curl E-E.curl B, and the above Maxwell equations.
S=E.cross(B)
udot=s.diff((E.dot(E)+B.dot(B))/2,t)
assert s.simplify(udot+div(S)+J.dot(E))==0
# At each static e, integrated Maxwell TT stress Iplus=-K e²/sqrt(1-e²).
# Weak tidal metric pumping: P_g=-h_dot Iplus(e(t))/2.
u=s.symbols('u',real=True)
h0,e0,de,sigma,shift=s.symbols('h0 e0 de sigma shift',real=True)
h=h0*(1-u*u)**4
hprime=s.diff(h,u)
eshape=e0+de/s.cosh((u-shift)/sigma)
anis=lambda e: -e*e/s.sqrt(1-e*e)  # normalized Iplus/K
assert s.simplify(hprime.subs(u,-u)+hprime)==0
assert s.simplify(eshape.subs(shift,0).subs(u,-u)-eshape.subs(shift,0))==0
assert s.simplify(eshape.subs(shift,-shift).subs(u,-u)-eshape)==0
power=-hprime*anis(eshape)/2
power_numeric=s.lambdify((u,e0,de,sigma,shift,h0),power,'numpy')
def tidal_work(delay):
    return quad(lambda v:power_numeric(v,.30,.07,.55,delay,1.e-4),
                -1,1,epsabs=1.e-14)[0]
v0=tidal_work(0)
vp=tidal_work(.35)
vm=tidal_work(-.35)
assert abs(v0)<1.e-15
assert abs(vp+vm)<1.e-15
assert vp<0 and vm>0
# The same sech curve can be traversed with arbitrarily rescaled clock
# sigma, hence supplies no physical rate without an equation of motion.
assert s.simplify(s.diff(eshape,u).subs(shift,0).subs(u,0))==0
print('PASS Maxwell constraints, local Poynting identity, sech tidal timing parity')
print('Normalized W_g/K at delay=0, +0.35, -0.35:',v0,vp,vm)
print('Note: numerical work uses prescribed h/e, no backreaction or source dynamics')
