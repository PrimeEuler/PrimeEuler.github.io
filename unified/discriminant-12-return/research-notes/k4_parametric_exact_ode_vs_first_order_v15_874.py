#!/usr/bin/env python3
"""Gravity v15.874: physical oscillator ODE vs v15.873 first-order pump work.
m=w=A=1; k(t)=1+eps sin(2t+phase).
Start x(0)=1,x'(0)=0 and solve full equation x''+k(t)x=0,
measure actual time-dependent mechanical energy at exactly one
unperturbed cycle T=2pi. Work comes from the stiffness controller.
Delta E = pi eps cos(phase)/2 + O(eps^2).
A pi/2 quadrature has zero leading work, not exactly zero work.
No EM/G coupling or source mechanism derived.
"""
import numpy as np
from scipy.integrate import solve_ivp
def simulate(eps,phase):
    end=2*np.pi
    def ode(t,y):
        return (y[1],-(1+eps*np.sin(2*t+phase))*y[0])
    result=solve_ivp(ode,(0,end),(1.,0.),method="DOP853",
                     rtol=2e-12,atol=2e-13)
    assert result.success
    x,v=result.y[:,-1]
    initial=.5*(1+eps*np.sin(phase))
    final=.5*v*v+.5*(1+eps*np.sin(2*end+phase))*x*x
    return final-initial
for eps in (.02,.01,.005):
    for phase in (0.,np.pi/2,np.pi):
        observed=simulate(eps,phase)
        predicted=np.pi*eps*np.cos(phase)/2
        assert abs(observed-predicted)<3*eps*eps
        print(f'eps={eps:.3f}, phase={phase:.6f}, exact={observed:+.12g}, first_order={predicted:+.12g}')
assert simulate(.005,0)>0
assert simulate(.005,np.pi)<0
assert 0<simulate(.005,np.pi/2)<2e-4
e1=abs(simulate(.01,np.pi/2));e2=abs(simulate(.005,np.pi/2))
assert 3.5<e1/e2<4.5
print('PASS first-order phase gain/loss and O(eps²) quadrature remainder')
print('NO Cone selector, quantum Casimir derivation or autonomous pump')
