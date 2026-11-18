#!/usr/bin/env python3
"""Gravity v15.1131: calibrated tidal torsion-to-Larmor paired-Jxy readout.

A locally Maxwell-consistent source-free gradient is B=(G*z,0,B0+G*x).
At z=0 two spins at x=+/-d*cos(theta)/2 have DeltaOmega=gamma*G*d*cos(theta).
A conventional quadrupole tidal torque yields deltaTheta(omega)=
 DeltaQ*sin(2theta0)*g(omega)/(kappa-Im*omega**2-i*Gamma*omega).
The relative Ramsey phase integrated over a finite interrogation tau
produces a sinc window and paired Cxy=-2*cos(phi) readout. No new
gravity coupling, Casimir, or intrinsic clock is implied.
"""
import sympy as s
x,z,G,B0,d,theta,gamma,tau,phi0=s.symbols('x z G B0 d theta gamma tau phi0',real=True)
kappa,Im,drag,omega,DQ,g=s.symbols('kappa Im drag omega DQ g',real=True)
Bx=G*z; Bz=B0+G*x
assert s.diff(Bx,x)+s.diff(Bz,z)==0
assert s.diff(Bx,z)-s.diff(Bz,x)==0
xp=d*s.cos(theta)/2
Bm=Bz.subs(x,-xp); Bp=Bz.subs(x,xp)
DOmega=s.simplify(gamma*(Bp-Bm))
assert s.simplify(DOmega-gamma*G*d*s.cos(theta))==0
deriv=s.diff(DOmega,theta)
assert s.simplify(deriv+gamma*G*d*s.sin(theta))==0
chi=1/(kappa-Im*omega**2-s.I*drag*omega)
Tdrive=DQ*s.sin(2*theta)
C=-2*s.cos(phi0)
trans=s.trigsimp(s.diff(C,phi0)*tau*deriv*chi*Tdrive)
expected=-2*gamma*G*d*tau*s.sin(phi0)*s.sin(theta)*DQ*s.sin(2*theta)*chi
assert s.simplify(trans-expected)==0
for subs in ({theta:0},{theta:s.pi/2},{G:0},{phi0:0}):
    assert s.simplify(trans.subs(subs))==0
f=s.sin(theta)*s.sin(2*theta)
stat=s.trigsimp(s.diff(f,theta))
assert s.trigsimp(stat-2*s.sin(theta)*(2-3*s.sin(theta)**2))==0
best=s.asin(s.sqrt(s.Rational(2,3)))
assert s.simplify(s.cos(best)-1/s.sqrt(3))==0
assert s.simplify(s.trigsimp(f.subs(theta,best))-4/(3*s.sqrt(3)))==0
assert s.simplify(s.trigsimp(f.subs(theta,s.pi/4))-s.sqrt(2)/2)==0
# Finite Ramsey window: integral from t-tau to t of deltaOmega(t').
# For exp(-i*omega*t) convention, multiply by exp(+i*omega*u).
window_exact=(s.exp(s.I*omega*tau)-1)/(s.I*omega)
window_sinc=tau*s.exp(s.I*omega*tau/2)*s.sin(omega*tau/2)/(omega*tau/2)
assert s.simplify(s.expand_complex(window_exact-window_sinc))==0
assert s.limit(window_exact,omega,0)==tau
assert s.simplify(window_exact.subs(omega,2*s.pi/tau))==0
transfer_exact=s.simplify(trans*window_exact/tau)
assert s.simplify(s.limit(transfer_exact,omega,0)-trans.subs(omega,0))==0
print('PASS Maxwell gradient, bicone torsion, Larmor and Jxy Ramsey transducer')
print('PASS angle and phase bias nulls, optimum theta=',s.N(best*180/s.pi),'deg')
print('PASS finite Ramsey sinc transfer: omega*tau=2*pi has a zero')
print('DeltaOmega=',DOmega)
print('dCxy/dg (quasi-static Ramsey)=',trans)
print('CAVEATS: externally prepared singlet, phase bias, magnetic hardware and springs')
