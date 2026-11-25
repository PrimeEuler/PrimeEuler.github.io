#!/usr/bin/env python3
"""v15.1452: nonlinear Hamiltonian constraint residual of the controlled
3+1 linearized ADM data from v15.1450. Spatial metric exp(2 psi) delta,
Kij=-H gammaij+exp(2psi)Aij, lapse 1. Checks residual O(kappa^2).
Not exact initial data and NOT a full C-F-B curvature-EFT solution.
"""
import numpy as np
def trial(N=24,kappa=.003):
 x=2*np.pi*np.arange(N)/N;X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 ks=np.fft.fftfreq(N,d=1/N)
 k=np.array(np.meshgrid(ks,ks,ks,indexing="ij"))
 k2=np.sum(k*k,axis=0);mask=k2>0
 grad=lambda f:np.array([np.fft.ifftn(1j*k[i]*np.fft.fftn(f)).real for i in range(3)])
 u=.16*np.sin(X);v=.13*np.sin(2*Y+.3)
 ut=.10*np.sin(2*X);vt=.09*np.sin(4*Y+.6)
 speed=np.array([ut,vt]);space=np.array([grad(u),grad(v)])
 D=1+u*u+v*v
 G=np.zeros((2,2,N,N,N))
 G[0,0]=1-u*u/D;G[1,1]=1-v*v/D;G[0,1]=G[1,0]=-u*v/D
 kin=np.einsum("ab...,a...,b...->...",G,speed,speed)
 spatial=np.einsum("ab...,ai...,bi...->...",G,space,space)
 rho=(kin+spatial)/2
 mom=-np.einsum("ab...,a...,bi...->i...",G,speed,space)
 assert np.max(abs(mom.mean(axis=(1,2,3))))<1e-12
 rho0=rho.mean();H=np.sqrt(kappa*rho0/3)
 rhok=np.fft.fftn(rho-rho0)
 psik=np.zeros_like(rhok)
 psik[mask]=kappa*rhok[mask]/(2*k2[mask])
 psi=np.fft.ifftn(psik).real
 lap=np.fft.ifftn(-k2*psik).real;gradpsi=grad(psi)
 jk=np.array([np.fft.fftn(mom[i]) for i in range(3)])
 along=np.sum(k*jk,axis=0)
 jl=np.zeros_like(jk);jl[:,mask]=k[:,mask]*along[mask]/k2[mask]
 W=np.zeros_like(jk);W[:,mask]=-kappa*(jk[:,mask]-.25*jl[:,mask])/k2[mask]
 divW=np.sum(1j*k*W,axis=0)
 A=np.zeros((3,3,N,N,N))
 for i in range(3):
  for j in range(3):
   ak=1j*k[i]*W[j]+1j*k[j]*W[i]
   if i==j:ak-=2*divW/3
   A[i,j]=np.fft.ifftn(ak).real
 A2=np.einsum("ij...,ij...->...",A,A)
 R3=np.exp(-2*psi)*(-4*lap-2*np.sum(gradpsi**2,axis=0))
 rho_curved=(kin+np.exp(-2*psi)*spatial)/2
 residual=R3+6*H*H-A2-2*kappa*rho_curved
 value=float(np.max(abs(residual)))
 out=dict(N=N,kappa=kappa,mean_rho=float(rho0),H=float(H),
  nonlinear_constraint_error=value,relative_to_max_source=float(value/(2*kappa*np.max(rho))),
  max_psi=float(np.max(abs(psi))),mean_constraint_error=float(residual.mean()))
 print(out,flush=True)
 return out
if __name__=="__main__":
 rows=[trial(kappa=g) for g in (.003,.0015,.00075)]
 for i in range(2):
  ratio=rows[i]["nonlinear_constraint_error"]/rows[i+1]["nonlinear_constraint_error"]
  print("halved coupling constraint-error ratio",ratio)
  assert 3.9<ratio<4.1
 print("PASS full nonlinear Hamiltonian residual O(kappa^2) on leading reconstructed 3+1 ADM data")
 print("OPEN exact nonlinear ADM constraints and dynamical full Weyl-Einstein-Maxwell-H2 solution")
