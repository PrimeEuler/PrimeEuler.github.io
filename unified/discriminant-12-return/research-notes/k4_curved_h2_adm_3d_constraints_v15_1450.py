#!/usr/bin/env python3
"""v15.1450: leading 3+1 ADM constraints for genuine curved H2 sigma
Cauchy data on spatial 3-torus. Nonzero k modes solved spectrally;
positive mean energy forces nonzero homogeneous expansion H.
No full non-linear Einstein evolution or Weyl interaction included.
Units kappa=8*pi*G, effective sigma kinetic factor f*r=1.
"""
import numpy as np
def trial(N=16,kappa=.003):
 x=2*np.pi*np.arange(N)/N
 X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 u=.16*np.sin(X);v=.13*np.sin(2*Y+.3)
 ut=.10*np.sin(2*X);vt=.09*np.sin(4*Y+.6)
 k=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=1/N)]*3),indexing="ij"))
 k2=np.sum(k*k,axis=0);nonzero=k2>0
 grad=lambda f:np.array([np.fft.ifftn(1j*k[i]*np.fft.fftn(f)).real for i in range(3)])
 ph=np.array([u,v]);speed=np.array([ut,vt])
 D=1+u*u+v*v
 G=np.zeros((2,2,N,N,N))
 G[0,0]=1-u*u/D;G[1,1]=1-v*v/D;G[0,1]=G[1,0]=-u*v/D
 gp=np.array([grad(u),grad(v)])
 rho=.5*(np.einsum("ab...,a...,b...->...",G,speed,speed)+
         np.einsum("ab...,ai...,bi...->...",G,gp,gp))
 j=-np.einsum("ab...,a...,bi...->i...",G,speed,gp)
 rho0=rho.mean();j0=np.mean(j,axis=(1,2,3))
 assert rho0>0 and np.max(abs(j0))<1e-13
 # 3R=-4 Delta psi; Hamiltonian 3R+6H²=2kappa rho
 rhok=np.fft.fftn(rho-rho0)
 psik=np.zeros_like(rhok,complex)
 psik[nonzero]=kappa*rhok[nonzero]/(2*k2[nonzero])
 hamerr=np.max(abs(-4*np.fft.ifftn(-k2*psik).real-2*kappa*(rho-rho0)))
 # A_ij=partial_i W_j+partial_j W_i-(2/3)delta_ij div W
 # div A_i=Delta W_i+(1/3)partial_i div W=kappa(j_i-j0_i)
 jk=np.array([np.fft.fftn(j[i]-j0[i]) for i in range(3)])
 along=np.sum(k*jk,axis=0)
 longitudinal=np.zeros_like(jk)
 longitudinal[:,nonzero]=k[:,nonzero]*along[nonzero]/k2[nonzero]
 transverse=jk-longitudinal
 W=np.zeros_like(jk)
 W[:,nonzero]=-kappa*(transverse[:,nonzero]+.75*longitudinal[:,nonzero])/k2[nonzero]
 divW=np.sum(1j*k*W,axis=0)
 Ah=np.zeros((3,3,N,N,N),complex)
 for i in range(3):
  for l in range(3):
   Ah[i,l]=1j*k[i]*W[l]+1j*k[l]*W[i]
   if i==l:Ah[i,l]-=(2/3)*divW
 divA=np.sum(1j*k[:,None]*Ah,axis=0)
 momerr=float(np.max(abs(divA-kappa*jk)))
 assert hamerr<2e-14 and momerr<2e-12
 H=np.sqrt(kappa*rho0/3)
 result=dict(N=N,kappa=kappa,mean_density=float(rho0),
  mean_momentum=j0.tolist(),required_H=float(H),
  max_conformal_psi=float(np.max(abs(np.fft.ifftn(psik).real))),
  nonzero_hamiltonian_error=float(hamerr),nonzero_momentum_error=momerr,
  flat_periodic_zero_mode_defect=float(2*kappa*rho0))
 print(result,flush=True)
 return result
if __name__=="__main__":
 for N in (12,16,24):trial(N)
 print("PASS 3+1 leading linear ADM nonzero-mode H/M constraints")
 print("NEGATIVE strictly static flat torus cannot host positive homogeneous H2 energy")
 print("OPEN nonlinear constraints, FLRW time evolution, full Weyl metric variation and quarter selector")
