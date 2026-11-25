#!/usr/bin/env python3
"""v15.1453: simultaneous nonlinear 3+1 ADM Hamiltonian and momentum
constraints for curved H2 sigma Cauchy data in a periodic 3-torus.
Conformal spatial gamma=e^(2psi) delta; Kij=-H gammaij+e^(2psi)LW_ij.
Background mean H determined by integrated Hamiltonian constraint.
No Einstein time evolution or full Weyl-Maxwell interaction.
"""
import numpy as np
def trial(N=32,kappa=.003):
 x=2*np.pi*np.arange(N)/N
 X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 k=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=1/N)]*3),indexing="ij"))
 k2=np.sum(k*k,axis=0);nz=k2>0
 def grad(f):
  F=np.fft.fftn(f)
  return np.array([np.fft.ifftn(1j*k[i]*F).real for i in range(3)])
 u=.16*np.sin(X);v=.13*np.sin(2*Y+.3)
 ut=.10*np.sin(2*X);vt=.09*np.sin(4*Y+.6)
 vel=np.array([ut,vt]);sp=np.array([grad(u),grad(v)])
 D=1+u*u+v*v
 G=np.zeros((2,2,N,N,N))
 G[0,0]=1-u*u/D;G[1,1]=1-v*v/D;G[0,1]=G[1,0]=-u*v/D
 kin=np.einsum("ab...,a...,b...->...",G,vel,vel)
 spatial=np.einsum("ab...,ai...,bi...->...",G,sp,sp)
 rho=(kin+spatial)/2
 j=-np.einsum("ab...,a...,bi...->i...",G,vel,sp)
 assert np.max(abs(j.mean(axis=(1,2,3))))<1e-12
 def L(W):
  divergence=np.sum(1j*k*W,axis=0)
  F=np.zeros((3,3,N,N,N),complex)
  for i in range(3):
   for l in range(3):
    F[i,l]=1j*k[i]*W[l]+1j*k[l]*W[i]
    if i==l:F[i,l]-=2*divergence/3
  return np.fft.ifftn(F,axes=(-3,-2,-1)).real
 def invert(source):
  J=np.array([np.fft.fftn(source[i]) for i in range(3)])
  dot=np.sum(k*J,axis=0)
  longitudinal=np.zeros_like(J)
  longitudinal[:,nz]=k[:,nz]*dot[nz]/k2[nz]
  W=np.zeros_like(J)
  W[:,nz]=-(J[:,nz]-.25*longitudinal[:,nz])/k2[nz]
  return W
 W=invert(kappa*j)
 rhok=np.fft.fftn(rho-rho.mean())
 F=np.zeros_like(rhok)
 F[nz]=kappa*rhok[nz]/(2*k2[nz])
 psi=np.fft.ifftn(F).real
 for step in range(20):
  A=L(W);gp=grad(psi)
  gp2=np.sum(gp*gp,axis=0);q=np.exp(2*psi)
  A2=np.einsum("ij...,ij...->...",A,A)
  H2=np.mean(2*gp2+q*(A2+kappa*kin)+kappa*spatial)/(6*q.mean())
  rhs=(-2*gp2+q*(6*H2-A2-kappa*kin)-kappa*spatial)/4
  F=np.fft.fftn(rhs)
  P=np.zeros_like(F);P[nz]=-F[nz]/k2[nz]
  newpsi=np.fft.ifftn(P).real
  rhsW=kappa*j-3*np.einsum("j...,ij...->i...",grad(newpsi),A)
  newW=invert(rhsW)
  delta=max(np.max(abs(newpsi-psi)),np.max(abs(newW-W)))
  psi,W=newpsi,newW
  if delta<2e-16:break
 A=L(W);gp=grad(psi);gp2=np.sum(gp*gp,axis=0);q=np.exp(2*psi)
 A2=np.einsum("ij...,ij...->...",A,A)
 H2=np.mean(2*gp2+q*(A2+kappa*kin)+kappa*spatial)/(6*q.mean())
 lap=np.fft.ifftn(-k2*np.fft.fftn(psi)).real
 scalar3R=np.exp(-2*psi)*(-4*lap-2*gp2)
 rho_actual=(kin+np.exp(-2*psi)*spatial)/2
 ham=scalar3R+6*H2-A2-2*kappa*rho_actual
 Ah=np.fft.fftn(A,axes=(-3,-2,-1))
 divergence=np.fft.ifftn(np.sum(1j*k[:,None]*Ah,axis=0),
                          axes=(-3,-2,-1)).real
 mom=divergence+3*np.einsum("j...,ij...->i...",gp,A)-kappa*j
 errH=float(np.max(abs(ham)));errM=float(np.max(abs(mom)))
 result=dict(N=N,kappa=kappa,iterations=step+1,H=float(np.sqrt(H2)),
   mean_density=float(rho.mean()),max_conformal_psi=float(np.max(abs(psi))),
   nonlinear_Hamiltonian_max_error=errH,nonlinear_momentum_max_error=errM,
   weighted_mean_momentum=np.mean(np.exp(3*psi)*j,axis=(1,2,3)).tolist())
 print(result,flush=True)
 assert errH<2e-12
 assert errM<(1e-10 if N==24 else 1e-12)
 return (result,psi,A,q)

def harmonic_initial(N=24,kappa=.003):
 out,psi,A,q=trial(N,kappa)
 ks=np.fft.fftfreq(N,d=1/N)
 k=np.array(np.meshgrid(*([ks]*3),indexing="ij"))
 grad=lambda f:np.array([np.fft.ifftn(1j*k[i]*np.fft.fftn(f)).real for i in range(3)])
 gp=grad(psi);H=out["H"]
 K=q[None,None]*(A-H*np.eye(3)[:,:,None,None,None])
 trace=sum(K[i,i]/q for i in range(3))
 adot=-trace;bdot=-gp/q
 ginv=np.zeros((4,4,N,N,N));ginv[0,0]=-1
 for i in range(3):ginv[i+1,i+1]=1/q
 dg=np.zeros((4,4,4,N,N,N))
 dg[0,0,0]=-2*adot
 for i in range(3):
  dg[0,0,i+1]=q*bdot[i];dg[0,i+1,0]=q*bdot[i]
  for j in range(3):dg[0,i+1,j+1]=-2*K[i,j]
 for axis in range(3):
  for i in range(3):dg[axis+1,i+1,i+1]=2*q*gp[axis]
 Gamma=np.zeros((4,4,4,N,N,N))
 for a in range(4):
  for m in range(4):
   for n in range(4):
    for ell in range(4):
     Gamma[a,m,n]+=.5*ginv[a,ell]*(dg[m,ell,n]+dg[n,ell,m]-dg[ell,m,n])
 contracted=np.einsum("mn...,amn...->a...",ginv,Gamma)
 err=float(np.max(abs(contracted)))
 wrong=dg.copy()
 wrong[0,0,0]=0;wrong[0,0,1:]=0;wrong[0,1:,0]=0
 bad=np.zeros_like(contracted)
 for a in range(4):
  for m in range(4):
   for n in range(4):
    for ell in range(4):
     bad[a]+=.5*ginv[m,n]*ginv[a,ell]*(wrong[m,ell,n]+wrong[n,ell,m]-wrong[ell,m,n])
 result=dict(N=N,ADM_Hamiltonian=out["nonlinear_Hamiltonian_max_error"],
  ADM_momentum=out["nonlinear_momentum_max_error"],
  GH_initial_residual=err,
  naive_GH_residual=float(np.max(abs(bad))),
  lapse_derivative_mean=float(np.mean(adot)),
  shift_derivative_max=float(np.max(abs(bdot))))
 assert err<1e-14 and result["ADM_Hamiltonian"]<2e-12
 assert result["ADM_momentum"]<1e-10
 assert result["naive_GH_residual"]>1e-3
 print("GAUGE",result,flush=True)
 return result
if __name__=="__main__":
 for N in (24,32):harmonic_initial(N)
 print("PASS simultaneous nonlinear Einstein-H2 ADM and initial GH constraints")
 print("OPEN strongly hyperbolic nonlinear evolution, gauge propagation and Weyl EFT")
