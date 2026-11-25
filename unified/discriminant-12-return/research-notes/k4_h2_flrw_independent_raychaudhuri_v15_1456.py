#!/usr/bin/env python3
"""v15.1456 independent Einstein Raychaudhuri evolution for homogeneous
curved-H2 sigma FLRW. Evolves Hdot=-kappa*rho independently of the
Friedmann constraint and monitors constraint propagation.
Not a 3D inhomogeneous or full Weyl-Maxwell Einstein solution.
"""
import numpy as np
from scipy.integrate import solve_ivp
def trial(kappa=.003,T=120):
 phi0=np.array([.15,-.08]);p0=np.array([.12,.07]);f=1.
 C0=p0@p0+(phi0@p0)**2
 H0=np.sqrt(kappa*C0/6)
 def rhs(t,z):
  a,H=z[:2];phi=z[2:4];p=z[4:6]
  dot=phi@p;C=p@p+dot*dot;rho=C/(2*a**6*f*f)
  return np.r_[a*H,-kappa*rho,(p+phi*dot)/(a**3*f*f),-dot*p/(a**3*f*f)]
 sol=solve_ivp(rhs,(0,T),np.r_[1,H0,phi0,p0],method="DOP853",
               rtol=1e-12,atol=2e-14,dense_output=True)
 assert sol.success
 t=np.linspace(0,T,241);z=sol.sol(t);a,H=z[:2];phi=z[2:4];p=z[4:6]
 C=np.sum(p*p,axis=0)+np.sum(phi*p,axis=0)**2
 rho=C/(2*a**6*f*f)
 constraint=float(np.max(abs(3*H*H-kappa*rho))/(kappa*C0/2))
 exact=1+np.sqrt(3*kappa*C0/2)*t
 scale_error=float(np.max(abs(a**3-exact))/exact[-1])
 C_error=float(np.max(abs(C-C0))/C0)
 assert max(constraint,scale_error,C_error)<2e-9
 print(dict(kappa=kappa,final_a=float(a[-1]),
       Friedmann_relative_violation=constraint,a3_relative_error=scale_error,
       sigma_invariant_relative_drift=C_error))
if __name__=="__main__":
 trial();trial(kappa=.0015)
 print("PASS independent Einstein acceleration and H2 sigma evolution preserves Friedmann")
 print("OPEN inhomogeneous metric evolution, full Weyl-Maxwell and physical quarter selector")
