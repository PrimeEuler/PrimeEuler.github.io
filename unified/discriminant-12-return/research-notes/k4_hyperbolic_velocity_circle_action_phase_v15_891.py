#!/usr/bin/env python3
"""Gravity v15.891: exact velocity-circle/action-angle phase-map numerical control.
Model: H=m*qdot^2/2+V0(cosh(q/ell)-1). No field-derived clock assumed.
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import ellipk, ellipkinc
from scipy.optimize import minimize_scalar

u = sp.symbols("u",real=True)
assert sp.simplify(sp.cosh(u/2)**2-1-sp.sinh(u/2)**2)==0
theta1,theta2=np.arcsin(.25),np.arcsin(.5)

def phase(theta,k):
    return np.pi*ellipkinc(theta,-k*k)/(2*ellipk(-k*k))

def delta(A):
    k=np.sinh(A/2)
    return phase(theta2,k)-phase(theta1,k)

for A in [0.01,0.1,0.5,1.,2.,4.,8.]:
    k=np.sinh(A/2)
    K=ellipk(-k*k)
    num=quad(lambda t:1/np.sqrt(1+k*k*np.sin(t)**2),theta1,theta2,epsabs=1e-12)[0]
    assert abs(delta(A)-np.pi*num/(2*K))<2e-12
    assert abs(quad(lambda t:1/np.sqrt(1+k*k*np.sin(t)**2),0,np.pi/2)[0]-K)<1e-12
    print("A",A,"k",k,"node_phase",delta(A),"cycle_fraction",delta(A)/(2*np.pi))
assert abs(delta(.01)-(theta2-theta1))<2e-6
assert abs(delta(2)-delta(.1))>0.03
opt=minimize_scalar(lambda A:-delta(A),bounds=(2,6),method="bounded")
assert abs(opt.x-3.85336)<.01
assert abs(-opt.fun-.34855265)<1e-6
print("max near",opt.x,"phase", -opt.fun)
print("PASS: complete elliptic phase, quadrature control, amplitude noninvariance")
