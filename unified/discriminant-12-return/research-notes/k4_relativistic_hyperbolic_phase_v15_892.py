#!/usr/bin/env python3
"""Gravity v15.892 exact SR cosh-well turning-point and action-angle control."""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import ellipk, ellipkinc

u,eps,k,theta=sp.symbols("u eps k theta",positive=True,real=True)
assert sp.simplify(sp.cosh(u)-1-2*sp.sinh(u/2)**2)==0
z=2*eps*k*k*sp.cos(theta)**2
v_by_c=sp.sqrt(z*(2+z))/(1+z)
dq_dtheta=2*k*sp.cos(theta)/sp.sqrt(1+k*k*sp.sin(theta)**2)
dt_dtheta=sp.simplify(dq_dtheta/v_by_c)
closed=(1+2*eps*k*k*sp.cos(theta)**2)/(sp.sqrt(eps)*sp.sqrt(1+k*k*sp.sin(theta)**2)*sp.sqrt(1+eps*k*k*sp.cos(theta)**2))
# Squared equality; on the outgoing quarter-orbit cos(theta)>=0 all factors are positive.
assert sp.simplify(dt_dtheta**2-closed**2)==0
m,c,L,V=sp.symbols("m c L V",positive=True)
F=-V/L*sp.sinh(u)
Fp=-V/L**2*sp.cosh(u)
q4=sp.simplify(Fp*F/m**2-3*F**3/(m**3*c**2))
assert sp.simplify(q4-(V**2*sp.sinh(u)*sp.cosh(u)/(m*m*L**3)+3*V**3*sp.sinh(u)**3/(m**3*L**3*c**2)))==0

theta1,theta2=np.arcsin(.25),np.arcsin(.5)
def f(th,A,alpha):
    kk=np.sinh(A/2.)
    x=alpha*kk*kk*np.cos(th)**2
    return (1+2*x)/(np.sqrt(1+kk*kk*np.sin(th)**2)*np.sqrt(1+x))
def quarter(A,alpha):
    return quad(lambda t:f(t,A,alpha),0,np.pi/2,epsabs=1e-12,epsrel=1e-12)[0]
def node_phase(A,alpha):
    num=quad(lambda t:f(t,A,alpha),theta1,theta2,epsabs=1e-12,epsrel=1e-12)[0]
    return (np.pi/2)*num/quarter(A,alpha)

for A in (.1,.5,1.,2.,4.):
    kk=np.sinh(A/2)
    newt=(np.pi/2)*(ellipkinc(theta2,-kk*kk)-ellipkinc(theta1,-kk*kk))/ellipk(-kk*kk)
    assert abs(node_phase(A,0)-newt)<5e-14
    print(f"A={A:g}: Newton={newt:.12f}; epsilon=.01,.1,1:",
          *(f"{node_phase(A,alpha):.12f}" for alpha in (.01,.1,1)))
assert abs(node_phase(2.,1)-node_phase(2.,0))>0.05
print("PASS: SR speed bound, Newtonian limit, exact phase normalization, turning-point quartic")
