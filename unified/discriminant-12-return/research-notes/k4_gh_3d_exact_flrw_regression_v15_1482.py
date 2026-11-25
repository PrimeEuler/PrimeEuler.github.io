#!/usr/bin/env python3
"""v15.1482: Fourth-order independent exact FLRW-in-harmonic-time
test of the unrestricted 3D GH Einstein-H2 solver v15.1481.
Does not replace genuinely inhomogeneous constraint convergence.
"""
import numpy as np
from k4_gh_3d_unrestricted_einstein_h2_v15_1481 import GHGrid,rk4
def run(dt=.1,T=.4,N=6):
 kappa=.003;f0=.2;fs=.12;B=np.sqrt(3*kappa*fs**2/2)
 shape=(N,)*3;g=np.zeros((4,4)+shape);p=np.zeros_like(g)
 g[0,0]=-1;p[0,0]=-2*B
 for i in range(3):g[i+1,i+1]=1;p[i+1,i+1]=2*B/3
 phi=np.zeros((2,)+shape);Pi=np.zeros_like(phi)
 phi[0]=np.sinh(f0);Pi[0]=fs*np.cosh(f0)
 state=(g,p,phi,Pi);solver=GHGrid(N,kappa)
 for _ in range(round(T/dt)):state=rk4(state,dt,solver.rhs)
 g,p,phi,Pi=state
 error=max(float(np.max(abs(g[0,0]+np.exp(2*B*T)))),
           float(np.max(abs(g[1,1]-np.exp(2*B*T/3)))),
           float(np.max(abs(phi[0]-np.sinh(f0+fs*T)))))
 gauge,gtt=solver.rhs(state,True);ham,mom=solver.adm(state)
 assert gtt<0 and max(gauge,ham,mom)<1e-10
 print(dict(dt=dt,T=T,error=error,gauge=gauge,Hamiltonian=ham,momentum=mom),flush=True)
 return error
if __name__=="__main__":
 errs=[run(dt=v) for v in (.1,.05,.025)]
 factors=[errs[i]/errs[i+1] for i in (0,1)]
 print("RK4 convergence factors",factors)
 assert all(15<r<17 for r in factors)
 print("PASS fully unrestricted 3D GH code reproduces homogeneous nonlinear exact Einstein-H2 harmonic solution")
 print("OPEN longer-time inhomogeneous constraint monitoring and spectral alias reduction")
