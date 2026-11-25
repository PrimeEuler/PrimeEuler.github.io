#!/usr/bin/env python3
"""v15.1470: nonlinear Einstein-H2 FLRW in harmonic time (alpha=a^3).
Evolves lapse and H independently, tests Friedmann/gauge constraints.
Homogeneous exact benchmark, not inhomogeneous 3+1 GH evolution.
"""
import numpy as np
from scipy.integrate import solve_ivp
def trial(kappa=.003,S=65):
 phi0=np.array([.15,-.08]);p0=np.array([.12,.07]);f2=1.
 C0=p0@p0+(phi0@p0)**2;B=np.sqrt(3*kappa*C0/(2*f2))
 H0=B/3
 def rhs(s,y):
  a,alpha,H=y[:3];phi=y[3:5];p=y[5:7]
  dot=phi@p;C=p@p+dot*dot;rho=C/(2*a**6*f2)
  return np.r_[alpha*a*H,3*alpha**2*H,-alpha*kappa*rho,
   alpha/(a**3*f2)*(p+phi*dot),-alpha/(a**3*f2)*dot*p]
 sol=solve_ivp(rhs,(0,S),np.r_[1,1,H0,phi0,p0],method='DOP853',
               rtol=1e-12,atol=2e-14,dense_output=True)
 assert sol.success
 s=np.linspace(0,S,201);y=sol.sol(s)
 a,alpha,H=y[:3];phi=y[3:5];p=y[5:7]
 C=np.sum(p*p,axis=0)+np.sum(phi*p,axis=0)**2
 rho=C/(2*a**6*f2)
 gauge=float(np.max(abs(alpha/a**3-1)))
 friedmann=float(np.max(abs(3*H*H-kappa*rho))/(kappa*C0/2))
 exact=float(np.max(abs(a**3-np.exp(B*s))/np.exp(B*s)))
 invariant=float(np.max(abs(C-C0))/C0)
 assert max(gauge,friedmann,exact,invariant)<1e-9
 print(dict(kappa=kappa,B=float(B),final_a=float(a[-1]),
  max_lapse_gauge_ratio_error=gauge,
  Friedmann_relative_constraint_error=friedmann,
  exact_harmonic_a3_relative_error=exact,
  H2_sigma_invariant_relative_error=invariant),flush=True)
if __name__=='__main__':
 trial();trial(kappa=.0015)
 print('PASS nonlinear harmonic-lapse Einstein-H2 time evolution and independent constraints')
 print('OPEN full spatially inhomogeneous GH Einstein-H2 initial value evolution')
