#!/usr/bin/env python3
"""v15.988: v15.900 radial rotor + ordinary sourced v15.986 Fermi
cross-tidal potential. Exact work budget and first-order torque check.
Dimensionless sample M=ri=L0=1, ro=5/4, F0=18/25.
NO unsourced quarter-Casimir Hamiltonian term.
"""
import numpy as np
from scipy.integrate import solve_ivp, trapezoid

M,F0,ro,L0,T=1.,18/25,1.25,1.,2.2
y0=[ro,0.,0.,L0,0.]

def field(t,eps,mode):
    if mode=='static': return eps,0.
    if mode=='periodic': return eps*np.cos(1.7*t),-1.7*eps*np.sin(1.7*t)
    return 0.,0.

def energy(t,y,eps,mode):
    r,pr,phi,L,W=y
    B,_=field(t,eps,mode)
    return pr**2/(2*M)+L**2/(2*M*r*r)+F0*r+M*B*r*r*np.sin(2*phi)/2

def dynamics(t,y,eps,mode):
    r,pr,phi,L,W=y
    B,dB=field(t,eps,mode)
    return [pr/M,L**2/(M*r**3)-F0-M*B*r*np.sin(2*phi),
            L/(M*r*r),-M*B*r*r*np.cos(2*phi),
            M*dB*r*r*np.sin(2*phi)/2]

runs=[('baseline',0.,'none'),('static',.02,'static'),
      ('periodic',.02,'periodic'),('static_half',.01,'static'),
      ('static_double',.04,'static')]
sols={}
for tag,eps,mode in runs:
    sol=solve_ivp(lambda t,y:dynamics(t,y,eps,mode),(0,T),y0,
                  rtol=1e-12,atol=1e-13,max_step=.005,dense_output=True)
    assert sol.success
    ts=np.linspace(0,T,601)
    yy=sol.sol(ts)
    error=max(abs(energy(t,yy[:,i],eps,mode)-energy(0,y0,eps,mode)-yy[4,i])
              for i,t in enumerate(ts))
    assert error<2e-10,(tag,error)
    sols[tag]=sol
    print(tag,'r=',format(sol.y[0,-1],'.12f'),
          'L=',format(sol.y[3,-1],'.12f'),
          'W=',format(sol.y[4,-1],'.12f'),'E-W_error=',error)
assert abs(sols['baseline'].y[3,-1]-1)<1e-12
assert abs(sols['static'].y[3,-1]-1)>1e-3
assert abs(sols['static'].y[4,-1])<1e-15
assert abs(sols['periodic'].y[4,-1])>1e-5
assert sols['static'].y[0,-1]<1
# Linear response of angular momentum to weak static curvature.
ts=np.linspace(0,T,10001)
yb=sols['baseline'].sol(ts)
linear=-trapezoid(yb[0]**2*np.cos(2*yb[2]),ts)
slopes=[]
for tag,eps in [('static_half',.01),('static',.02),('static_double',.04)]:
    slope=(sols[tag].y[3,-1]-L0)/eps
    slopes.append(slope)
    print('torque_slope',tag,slope,'linear_control',linear)
assert abs(slopes[0]-linear)<abs(slopes[2]-linear)
print('PASS: driven rotor, torque, work conservation, first-order response.')
