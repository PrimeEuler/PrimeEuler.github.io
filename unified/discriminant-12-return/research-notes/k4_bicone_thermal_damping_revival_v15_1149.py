#!/usr/bin/env python3
"""Gravity v15.1149: finite thermal occupation and mechanical damping at
the first bicone spin-torsion Ramsey revival. Standard Gaussian pure
dephasing comparator, NOT an exact arbitrary-damping Brownian system.

Assume stationary symmetrized correlator C_q(u)=
hbar*(2*nbar+1)/(2*I*w) * exp(-lambda*abs(u))*cos(w*u).
The relative spin frequency is k*q and lambda=w/(2*Q).
"""
import numpy as np
import sympy as s
from scipy.integrate import quad
u,t,lam,w=s.symbols("u t lam w",positive=True,real=True)
J0=s.integrate((t-u)*s.cos(w*u),(u,0,t))
assert s.trigsimp(J0-(1-s.cos(w*t))/w**2)==0
Jprime0=-s.integrate((t-u)*u*s.cos(w*u),(u,0,t))
assert s.simplify(Jprime0.subs(t,2*s.pi/w)-4*s.pi/w**3)==0
def J_numeric(time,l,omega):
    return quad(lambda u:(time-u)*np.exp(-l*u)*np.cos(omega*u),0,time,
                epsabs=1e-12,epsrel=1e-12)[0]
def J_exact(time,l,omega):
    a=l-1j*omega
    return (time/a+np.expm1(-a*time)/a**2).real
for l in (0,.002,.01,.05,.2):
    for time in (.6,1.3,2*np.pi,4*np.pi):
        val=J_exact(time,l,1.)
        assert abs(val-J_numeric(time,l,1.))<1e-9
        assert val>=-1e-10
# r=hbar*k**2/(I*w**3), Q=w/(2lambda)
def V(time,w,Q,r,nbar):
    return np.exp(-r*(2*nbar+1)*w*w*
                  J_exact(time,w/(2*Q),w)/2)
for Q in (30.,100.,1000.):
    for nbar in (0.,1.,10.):
        actual=V(2*np.pi,1.,Q,.1,nbar)
        weak=np.exp(-np.pi*.1*(2*nbar+1)/Q)
        assert 0<actual<1 and abs(actual-weak)<.015
for nbar in (0.,1.,10.):
    assert abs(np.exp(-.1*(2*nbar+1)*
           (1-np.cos(2*np.pi))/2)-1)<1e-14
# Under damping and constant force, the net integrated Ramsey phase
# remains nonzero after one damped mechanical oscillation.
for l in (.001,.05,.2):
    wd=1.;w0=np.hypot(wd,l);T=2*np.pi/wd
    q=lambda tt:(1-np.exp(-l*tt)*
       (np.cos(wd*tt)+l/wd*np.sin(wd*tt)))/w0**2
    assert quad(q,0,T,epsabs=1e-12)[0]>0
print("PASS exact stationary-Gaussian covariance integral vs quadrature")
print("PASS lossless thermal full revival; damped thermal incomplete revival")
print("PASS weak-loss exponent pi*r*(2*nbar+1)/Q and nonzero damped tidal phase")
for Q in (30,100,1000):
    print("Q",Q,"visibility nbar 0,1,10:",
          *[round(V(2*np.pi,1.,Q,.1,n),9) for n in (0,1,10)])
print("CAUTION: stationary weak-damping Gaussian model; no apparatus noise or G")
