#!/usr/bin/env python3
"""v15.1422 prescribed tidal parameter is an external time-dependent
source; canonical EM+sigma mode energy changes by supplied work.
A test of Noether bookkeeping, NOT full Weyl/Einstein backreaction.
"""
import numpy as np
from scipy.integrate import solve_ivp,simpson
def test(g=.08,depth=.4,w=.85,T=11.):
 def coeff(t):return depth*np.cos(w*t),-depth*w*np.sin(w*t)
 def rhs(t,Y):
  A,u,pA,pu=Y
  c,dc=coeff(t);z=g*c
  return [(pA-z*pu)/(1-z*z),(pu-z*pA)/(1-z*z),-A,-u]
 def energy(t,Y):
  A,u,pA,pu=Y;c,dc=coeff(t);z=g*c
  return ((pA*pA+pu*pu-2*z*pA*pu)/(1-z*z)+A*A+u*u)/2
 def external(t,Y):
  c,dc=coeff(t);z=g*c
  At=(Y[2]-z*Y[3])/(1-z*z)
  ut=(Y[3]-z*Y[2])/(1-z*z)
  return -g*dc*At*ut
 sol=solve_ivp(rhs,(0,T),[.14,0,0,.09],method="DOP853",
               rtol=2e-12,atol=1e-14,dense_output=True)
 assert sol.success
 time=np.linspace(0,T,3001);Y=sol.sol(time)
 E=[energy(t,y) for t,y in zip(time,Y.T)]
 W=simpson([external(t,y) for t,y in zip(time,Y.T)],x=time)
 delta=E[-1]-E[0];error=abs(delta-W)
 assert error<5e-10,(delta,W,error)
 result=dict(g=g,initial_energy=float(E[0]),final_energy=float(E[-1]),
             energy_change=float(delta),external_work=float(W),work_error=float(error))
 print(result,flush=True)
 return result
if __name__=="__main__":
 a=test();control=test(g=0)
 assert abs(control["energy_change"])<1e-11
 print("PASS prescribed time-varying tidal background exchanges energy")
 print("OPEN evolving EH metric, Bianchi total stress and physical quarter coupling")
