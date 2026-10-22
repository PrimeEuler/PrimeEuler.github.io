#!/usr/bin/env python3
"""Independent higher-sample Rutherford escape cutoff convergence probe.
Reproduces the self-run 4 x 2^16 Sobol results; no BPS matching implied."""
import numpy as np
from scipy.stats import qmc
from scipy.special import ndtri

def rate(e,theta_min,sigma=1.0,n_pow=16,seed=11):
 n=2**n_pow
 u=qmc.Sobol(d=5,scramble=True,seed=seed).random_base2(n_pow)
 M=2*np.pi*u[:,0];E=M.copy()
 for _ in range(14):
  E-=(E-e*np.sin(E)-M)/(1-e*np.cos(E))
 r=1-e*np.cos(E)
 v=np.stack((e*np.sin(E)/r,np.sqrt(1-e*e)/r,np.zeros(n)),axis=1)
 w=sigma*ndtri(np.clip(u[:,1:4],1e-12,1-1e-12))
 gv=v-w; g=np.linalg.norm(gv,axis=1); kh=gv/g[:,None]
 V=(v+w)/2;Vp=np.sum(V*kh,axis=1)
 Vperp=np.sqrt(np.maximum(0,np.sum(V*V,axis=1)-Vp*Vp))
 lo=np.sin(theta_min/2)**2
 t=1/(1/lo-(1/lo-1)*u[:,4])
 a=np.sum(V*V,axis=1)+g*g/4+g*Vp*(1-2*t)
 b=2*g*Vperp*np.sqrt(t*(1-t))
 c=np.divide(2/r-a,b,out=np.where(2/r<=a,-np.inf,np.inf),where=b>1e-13)
 p=np.arccos(np.clip(c,-1,1))/np.pi
 vals=4*np.pi*(1/lo-1)*p/g**3
 return float(np.mean(vals)),float(np.max(vals)),float(np.mean(vals>0))

if __name__=="__main__":
 for e in (0.,.55,.82):
  gap=np.sqrt(2/(1-e))-np.sqrt((1+e)/(1-e))
  print('e',e,'minimum escape speed gap',gap,flush=True)
  for th in (.4,.2,.1,.05):
   res=np.array([rate(e,th,seed=s) for s in (11,12,13,14)])
   print('cutoff',th,'mean',res[:,0].mean(),'replicate SE',res[:,0].std(ddof=1)/2,'max sample',res[:,1].max(),'positive rate',res[:,2].mean(),flush=True)
