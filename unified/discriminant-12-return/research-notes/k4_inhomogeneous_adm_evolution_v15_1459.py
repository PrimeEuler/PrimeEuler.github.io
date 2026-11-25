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
 return (np.eye(3)[:,:,None,None,None]*np.exp(2*psi),
         np.exp(2*psi)*(A-np.sqrt(H2)*np.eye(3)[:,:,None,None,None]),
         np.array([u,v]),np.array([ut,vt]))

def evolve(N=32,dt=.002,T=.004,method="rk4",kappa=.003):
 gam,ext,phi,vel=trial(N,kappa)
 ks=np.fft.fftfreq(N,d=1/N)
 k=np.array(np.meshgrid(ks,ks,ks,indexing="ij"))
 def d(f,i):return np.fft.ifftn(1j*k[i]*np.fft.fftn(f)).real
 def df(f):return np.array([d(f,i) for i in range(3)])
 size=N**3; n=9*size;nf=2*size
 def unpack(y):
  return (y[:n].reshape(3,3,N,N,N),y[n:2*n].reshape(3,3,N,N,N),
          y[2*n:2*n+nf].reshape(2,N,N,N),y[2*n+nf:].reshape(2,N,N,N))
 def evaleq(y,only_constraints=False):
  gamma,K,field,Pi=unpack(y)
  inv=np.moveaxis(np.linalg.inv(np.moveaxis(gamma,(0,1),(-2,-1))),(-2,-1),(0,1))
  Dg=np.array([df(gamma[i,j]) for i in range(3) for j in range(3)]).reshape(3,3,3,N,N,N)
  C=np.zeros((3,3,3,N,N,N))
  for a in range(3):
   for i in range(3):
    for j in range(3):
     for l in range(3):
      C[a,i,j]+=.5*inv[a,l]*(Dg[l,j,i]+Dg[l,i,j]-Dg[i,j,l])
  dC=np.array([df(C[a,i,j]) for a in range(3) for i in range(3)
             for j in range(3)]).reshape(3,3,3,3,N,N,N)
  Ric=np.zeros_like(gamma)
  for i in range(3):
   for j in range(3):
    for l in range(3):
     Ric[i,j]+=dC[l,i,j,l]-dC[l,i,l,j]
     for m in range(3):
      Ric[i,j]+=C[l,i,j]*C[m,l,m]-C[l,i,m]*C[m,j,l]
  Kmix=np.einsum("ik...,kj...->ij...",inv,K)
  trK=np.einsum("ij...,ij...->...",inv,K)
  scalar=np.einsum("ij...,ij...->...",inv,Ric)
  U,V=field
  D=1+U*U+V*V
  G=np.array([[1-U*U/D,-U*V/D],[-U*V/D,1-V*V/D]])
  gp=np.array([df(field[i]) for i in range(2)])
  time=np.einsum("ab...,a...,b...->...",G,Pi,Pi)
  space=np.einsum("ab...,ai...,bj...,ij...->...",G,gp,gp,inv)
  rho=.5*(time+space)
  J=-np.einsum("ab...,a...,bi...->i...",G,Pi,gp)
  ham=scalar+trK**2-np.einsum("ij...,ji...->...",Kmix,Kmix)-2*kappa*rho
  dKm=np.array([df(Kmix[i,j]) for i in range(3) for j in range(3)]).reshape(3,3,3,N,N,N)
  mom=np.zeros_like(J)
  for i in range(3):
   mom[i]=sum(dKm[j,i,j] for j in range(3))-d(trK,i)-kappa*J[i]
   for j in range(3):
    for l in range(3):
     mom[i]+=C[j,j,l]*Kmix[l,i]-C[l,j,i]*Kmix[j,l]
  if only_constraints:
   return float(np.max(abs(ham))),float(np.max(abs(mom)))
  matter=np.einsum("ab...,ai...,bj...->ij...",G,gp,gp)
  Kdot=Ric+trK*K-2*np.einsum("ik...,kj...->ij...",K,Kmix)-kappa*matter
  pidot=np.zeros_like(Pi)
  for a in range(2):
   lap=np.zeros((N,N,N))
   for i in range(3):
    for j in range(3):
     cov=d(d(field[a],i),j)
     for l in range(3):cov-=C[l,i,j]*gp[a,l]
     lap+=inv[i,j]*cov
   pidot[a]=trK*Pi[a]+lap+field[a]*(time-space)
  return np.r_[(-2*K).ravel(),Kdot.ravel(),Pi.ravel(),pidot.ravel()]
 y=np.r_[gam.ravel(),ext.ravel(),phi.ravel(),vel.ravel()]
 initial=evaleq(y,True)
 for _ in range(round(T/dt)):
  k1=evaleq(y);k2=evaleq(y+dt*k1/2)
  if method=="rk4":
   k3=evaleq(y+dt*k2/2);k4=evaleq(y+dt*k3)
   y+=dt*(k1+2*k2+2*k3+k4)/6
  else:y+=dt*k2
 final=evaleq(y,True)
 result=dict(N=N,method=method,dt=dt,T=T,initial_H=initial[0],
             initial_M=initial[1],final_H=final[0],final_M=final[1])
 print("EVOLUTION",result,flush=True)
 return result
if __name__=="__main__":
 for n in (24,32,40):
  row=evolve(N=n,method="rk4")
  assert row["final_H"]<(2e-8 if n==24 else 3e-10)
  assert row["final_M"]<(2e-9 if n==24 else 5e-11)
 print("PASS short-time RK4 3+1 Einstein-H2 sigma constraint evolution")
 print("NEGATIVE N12 initial momentum alias; T=.04 convergence not closed")
