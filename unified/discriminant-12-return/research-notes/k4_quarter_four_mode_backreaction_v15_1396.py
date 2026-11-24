#!/usr/bin/env python3
"""v15.1396: stipulated four-mode resonant Hamiltonian backreaction surrogate.
NOT derived by projection from full Weyl-H2 action."""
import numpy as np
from scipy.integrate import solve_ivp
def trial(k=.05,T=50.,initial=(0j,1+0j,1+0j,1+0j)):
 def rhs(t,z):
  a,g,u,v=z
  return -1j*k*np.array([np.conj(g)*u*v,np.conj(a)*u*v,a*g*np.conj(v),a*g*np.conj(u)])
 sol=solve_ivp(rhs,(0,T),np.array(initial,complex),method="DOP853",
               rtol=5e-12,atol=1e-13,dense_output=True)
 assert sol.success
 time=np.linspace(0,T,801)
 z=sol.sol(time);n=abs(z)**2
 inv=np.array([n[0]+n[2],n[0]+n[3],n[1]+n[2],n[1]+n[3]])
 hint=k*(np.conj(z[0]*z[1])*z[2]*z[3]+z[0]*z[1]*np.conj(z[2]*z[3]))
 H=np.sum(n,axis=0)+hint.real
 err=max(np.max(abs(inv-inv[:,0,None])),np.max(abs(H-H[0])))
 assert err<1e-8,err
 out=dict(k=k,T=T,photon=float(n[0,-1]),gravity=float(n[1,-1]),
          internal_u=float(n[2,-1]),internal_v=float(n[3,-1]),
          max_conservation_error=float(err))
 print(out,flush=True)
 return out
if __name__=="__main__":
 a=trial()
 b=trial(T=15)
 c=trial(k=.025,T=30)
 assert abs(b["photon"]-c["photon"])<2e-11
 assert trial(k=0)["photon"]==0
 assert trial(initial=(0j,0j,1+0j,1+0j))["photon"]==0
 print("PASS four-wave Hamiltonian Manley-Rowe conservation and pump depletion")
 print("OPEN derive kappa, projections, full EFT stress and physical quarter selector")
