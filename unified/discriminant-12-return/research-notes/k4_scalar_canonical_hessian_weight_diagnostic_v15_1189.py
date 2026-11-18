#!/usr/bin/env python3
"""Gravity v15.1189. A precise kinetic-Hessian audit gate for archived K4 scalar.
PROVED: for homogeneous quadratic constrained blocks, lapse/shift
Schur elimination preserves a³ in the reduced kinetic Hessian.
NOT PROVED HERE: full ADM scalar blocks satisfy those weights and
the independent scalar algebraic metric constraint causes no dressing.
Tests fixed oscillator mass with a general q qdot mixed term.
"""
import sympy as s
a=s.symbols('a',positive=True)
k0,c0,c1,h0,h1,h2=s.symbols('k0 c0 c1 h0 h1 h2',real=True)
v,z1,z2=s.symbols('v z1 z2',real=True)
H=s.Matrix([[h0,h1],[h1,h2]])
C=s.Matrix([c0,c1])
Z=s.Matrix([z1,z2])
L=a**3*k0*v*v/2+a**2*v*(C.T*Z)[0]+a*(Z.T*H*Z)[0]/2
star=-a*H.inv()*C*v
red=s.factor(L.subs({z1:star[0],z2:star[1]},simultaneous=True))
K=s.factor(s.diff(red,v,2))
assert s.simplify(K-a**3*(k0-(C.T*H.inv()*C)[0]))==0
assert s.simplify(s.diff(K,a)/K-3/a)==0
t=s.symbols('t',positive=True)
q=s.Function('q')(t)
Kt=s.Function('K')(t);Mt=s.Function('M')(t);Vt=s.Function('V')(t)
qd=s.diff(q,t)
Lq=Kt*qd**2/2+Mt*q*qd-Vt*q*q/2
EL=s.factor(s.diff(s.diff(Lq,qd),t)-s.diff(Lq,q))
assert s.simplify(EL-(Kt*s.diff(q,t,2)+s.diff(Kt,t)*qd+(Vt+s.diff(Mt,t))*q))==0
# Most general kinetic power a^(3+r) yields friction (3+r)H;
# on coasting a~tau^1, canonical Omega²=omega²-(r+3)(r+1)/(4 tau²).
r,tau,omega=s.symbols('r tau omega',real=True,positive=True)
Hubble=1/tau
f=(3+r)*Hubble
Omega2=s.simplify(omega**2-s.diff(f,tau)/2-f*f/4)
assert s.simplify(Omega2-omega**2+(r+3)*(r+1)/(4*tau**2))==0
print('PASS conditional Schur weight, mixed-term EL, arbitrary-power canonical frequency')
print('OPEN actual archived scalar reduced coefficient extraction')
