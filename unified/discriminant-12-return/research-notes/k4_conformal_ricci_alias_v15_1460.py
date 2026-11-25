#!/usr/bin/env python3
"""v15.1460 independent full 3D Christoffel Ricci versus exact conformal
scalar R=e^-2psi(-4 Delta psi-2 gradpsi^2) on same initial fields.
An aliasing diagnostic, not an Einstein evolution.
"""
import numpy as np
def check(N):
 x=np.arange(N)*2*np.pi/N
 X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 k=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=1/N)]*3),indexing="ij"))
 kk=np.sum(k*k,axis=0);mask=kk>0
 def d(f,i):return np.fft.ifftn(1j*k[i]*np.fft.fftn(f)).real
 def grad(f):return np.array([d(f,i) for i in range(3)])
 u=.16*np.sin(X);v=.13*np.sin(2*Y+.3)
 ut=.10*np.sin(2*X);vt=.09*np.sin(4*Y+.6)
 D=1+u*u+v*v;G=np.array([[1-u*u/D,-u*v/D],[-u*v/D,1-v*v/D]])
 p=np.array([ut,vt]);gp=np.array([grad(u),grad(v)])
 rho=.5*(np.einsum("ab...,a...,b...->...",G,p,p)+
         np.einsum("ab...,ai...,bi...->...",G,gp,gp))
 rh=np.fft.fftn(rho-rho.mean());ph=np.zeros_like(rh);ph[mask]=.003*rh[mask]/(2*kk[mask])
 psi=np.fft.ifftn(ph).real
 q=np.exp(2*psi);metric=q[None,None]*np.eye(3)[:,:,None,None,None]
 inv=np.eye(3)[:,:,None,None,None]/q
 dg=np.array([grad(metric[i,j]) for i in range(3) for j in range(3)]).reshape(3,3,3,N,N,N)
 C=np.zeros((3,3,3,N,N,N))
 for a in range(3):
  for i in range(3):
   for j in range(3):
    for l in range(3):
     C[a,i,j]+=.5*inv[a,l]*(dg[l,j,i]+dg[l,i,j]-dg[i,j,l])
 dc=np.array([grad(C[a,i,j]) for a in range(3) for i in range(3)
   for j in range(3)]).reshape(3,3,3,3,N,N,N)
 R=np.zeros_like(metric)
 for i in range(3):
  for j in range(3):
   for l in range(3):
    R[i,j]+=dc[l,i,j,l]-dc[l,i,l,j]
    for m in range(3):R[i,j]+=C[l,i,j]*C[m,l,m]-C[l,i,m]*C[m,j,l]
 ric=np.einsum("ij...,ij...->...",inv,R)
 lap=np.fft.ifftn(-kk*ph).real
 closed=np.exp(-2*psi)*(-4*lap-2*np.sum(grad(psi)**2,axis=0))
 err=float(np.max(abs(ric-closed)))
 print(dict(N=N,max_conformal_ricci_disagreement=err),flush=True)
 return err
if __name__=="__main__":
 values=[check(n) for n in (12,16,24,32,40)]
 assert values[2]>values[3]>values[4]
 print("PASS resolution-dependent alias floor of full Christoffel Ricci")
 print("NEGATIVE N16 error worse than N12; no monotone coarse-grid guarantee")
