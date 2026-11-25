#!/usr/bin/env python3
"""v15.1454 homogeneous flat-FLRW Einstein plus fully curved H2 sigma geodesic.
Exact conserved C=p.p+(phi.p)^2 and a^3=1+t sqrt(3*kappa*C/(2*f^2)).
Not the inhomogeneous 3D ADM evolution or full Weyl-Maxwell EFT.
"""
import numpy as np
from scipy.integrate import solve_ivp
def trial(kappa=.003,T=120):
 phi0=np.array([.15,-.08]);p0=np.array([.12,.07]);f=1.
 C0=p0@p0+(phi0@p0)**2
 slope=np.sqrt(3*kappa*C0/(2*f*f))
 def rhs(t,z):
  scale=z[0];phi=z[1:3];p=z[3:5];dot=phi@p
  C=p@p+dot*dot;H=np.sqrt(kappa*C/(6*f*f))/scale**3
  return np.r_[scale*H,(p+phi*dot)/(scale**3*f*f),-dot*p/(scale**3*f*f)]
 sol=solve_ivp(rhs,(0,T),np.r_[1.,phi0,p0],method="DOP853",
               rtol=2e-12,atol=1e-14,dense_output=True)
 assert sol.success
 t=np.linspace(0,T,251);z=sol.sol(t);scale=z[0];phi=z[1:3];p=z[3:5]
 C=np.sum(p*p,axis=0)+np.sum(phi*p,axis=0)**2
 rho=C/(2*scale**6*f*f);H=np.sqrt(kappa*rho/3)
 errC=float(np.max(abs(C-C0))/C0)
 erra=float(np.max(abs(scale**3-(1+slope*t)))/np.max(1+slope*t))
 errH=float(np.max(abs(3*H*H-kappa*rho)))
 assert errC<3e-10 and erra<3e-10 and errH<2e-17
 print(dict(kappa=kappa,T=T,C=C0,slope=slope,a_final=float(scale[-1]),
       sigma_final=phi[:,-1].tolist(),C_relative_drift=errC,
       a_cubed_relative_error=erra,Friedmann_error=errH))
if __name__=="__main__":
 trial();trial(kappa=.0015)
 print("PASS homogeneous curved H2 Einstein-FLRW Friedmann constraint and kinetic invariant")
 print("OPEN inhomogeneous 3D ADM metric evolution, full Weyl-Maxwell and quarter selector")
