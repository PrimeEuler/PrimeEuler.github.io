#!/usr/bin/env python3
"""Gravity v15.1148 — exact driven torsion and paired-spin Ramsey revival.

Constant gravitational tidal torque Fg=DeltaQ*sin(2theta0)*g on [0,t]
gives q_g(t)=Fg/(I*w²)*(1-cos wt), and induced relative Zeeman phase
phi_g(t)=k*Fg/(I*w²)*(t-sin wt/w).
For an initial mechanical oscillator ground state under a linear Dz
spin-mechanical interaction the spin contrast is
V=exp[-hbar*k²/(I*w³)*sin²(wt/2)].
At a full period 2pi*n/w, V=1 but phi_g is nonzero unless kFg=0.
No gravitational source law or natural frequency is derived here.
"""
import sympy as s
t,u,Im,w,k,Fg,hbar=s.symbols('t u Im omega k Fg hbar',positive=True,real=True)
q=Fg/(Im*w*w)*(1-s.cos(w*t))
phi=s.simplify(s.integrate(k*q,(t,0,t)))
assert s.simplify(phi-k*Fg/(Im*w*w)*(t-s.sin(w*t)/w))==0
visibility=s.exp(-hbar*k*k/(Im*w**3)*s.sin(w*t/2)**2)
for n in (1,2,3,4):
    end=2*s.pi*n/w
    assert s.simplify(visibility.subs(t,end)-1)==0
    assert s.simplify(phi.subs(t,end)-2*s.pi*n*k*Fg/(Im*w**3))==0
assert s.simplify(
    s.integrate(s.sin(w*(t-u)),(u,0,t))-(1-s.cos(w*t))/w
)==0
g,DQ,theta=s.symbols('g DQ theta',real=True)
phig=phi.subs(Fg,g*DQ*s.sin(2*theta))
magic=s.atan(s.sqrt(2))
assert s.simplify(
    s.trigsimp(s.diff(phig,g).subs({theta:magic,t:2*s.pi/w}))-
    4*s.pi*s.sqrt(2)*k*DQ/(3*Im*w**3)
)==0
print('PASS driven torsion and exact spin-relative Ramsey phase')
print('PASS full-revival visibility=1, tidal phase=',phi.subs(t,2*s.pi/w))
print('LIMIT: finite classical torque, ideal closed oscillator, no source selector')
