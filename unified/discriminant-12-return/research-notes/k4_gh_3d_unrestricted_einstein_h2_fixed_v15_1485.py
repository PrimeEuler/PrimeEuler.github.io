#!/usr/bin/env python3
"""v15.1485 repaired standalone reproduction of v15.1481.\n\nOriginal initial-data base: v15.1453: simultaneous nonlinear 3+1 ADM Hamiltonian and momentum
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
 assert errM<(1e-8 if N<=16 else 1e-10 if N==24 else 1e-12)
 return (result,psi,A,q)

# v15.1481 — Unrestricted nonlinear 3D generalized-harmonic Einstein-H2
# evolution; independent four GH and four ADM constraint monitors.
# This is an independent implementation companion to the locally executed
# /mnt/data/cone_gh/gh3d.py (SHA-256 087310cf...); Audit replay required.
def initial(N=24,kappa=.003):
 result,psi,A,q=trial(N,kappa)
 x=np.arange(N)*2*np.pi/N;X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 kk=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=1/N)]*3),indexing="ij"))
 gp=np.fft.ifftn(1j*kk*np.fft.fftn(psi),axes=(-3,-2,-1)).real
 phi=np.array([.16*np.sin(X),.13*np.sin(2*Y+.3)])
 pi=np.array([.10*np.sin(2*X),.09*np.sin(4*Y+.6)])
 K=q[None,None]*(A-result["H"]*np.eye(3)[:,:,None,None,None])
 tr=sum(K[i,i]/q for i in range(3))
 p=np.zeros((4,4,N,N,N));g=np.zeros_like(p);g[0,0]=-1;p[0,0]=2*tr
 for i in range(3):
  g[i+1,i+1]=q
  p[0,i+1]=p[i+1,0]=-gp[i]
  for j in range(3):p[i+1,j+1]=-2*K[i,j]
 return (g,p,phi,pi)
class GHGrid:
 def __init__(self,N,kappa=.003):
  self.N=N;self.kappa=kappa
  self.k=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=1/N)]*3),indexing="ij"))
 def grad(self,a):
  h=np.fft.fftn(a,axes=(-3,-2,-1))
  k=self.k.reshape((3,)+(1,)*(a.ndim-3)+(self.N,)*3)
  return np.fft.ifftn(1j*k*h,axes=(-3,-2,-1)).real
 def second(self,a):
  h=np.fft.fftn(a,axes=(-3,-2,-1))
  return np.array([[np.fft.ifftn(-self.k[i]*self.k[j]*h,axes=(-3,-2,-1)).real
                    for j in range(3)] for i in range(3)])
 def rhs(self,y,monitor=False):
  g,p,phi,pi=y;shape=(self.N,)*3
  inv=np.moveaxis(np.linalg.inv(np.moveaxis(g,(0,1),(-2,-1))),(-2,-1),(0,1))
  d=np.zeros((4,4,4)+shape);d[0]=p;d[1:]=self.grad(g)
  dd=np.zeros((4,4,4,4)+shape)
  dd[0,1:]=self.grad(p);dd[1:,0]=dd[0,1:]
  dd[1:,1:]=self.second(g)
  dinv=-np.einsum("ip...,apq...,qj...->aij...",inv,d,inv,optimize=True)
  gam=np.zeros((4,4,4)+shape);dgam0=np.zeros((4,4,4,4)+shape)
  for r in range(4):
   for i in range(4):
    for j in range(4):
     for l in range(4):
      b=d[i,l,j]+d[j,l,i]-d[l,i,j]
      gam[r,i,j]+=.5*inv[r,l]*b
      for h in range(4):dgam0[h,r,i,j]+=.5*dinv[h,r,l]*b
  C=np.einsum("ij...,rij...->r...",inv,gam,optimize=True)
  cl=np.einsum("ij...,j...->i...",g,C,optimize=True)
  R0=np.zeros((4,4)+shape)
  for i in range(4):
   for j in range(4):
    for r in range(4):
     R0[i,j]+=dgam0[r,r,i,j]-dgam0[j,r,i,r]
     for l in range(4):R0[i,j]+=gam[r,i,j]*gam[l,r,l]-gam[r,i,l]*gam[l,j,r]
  dcl=np.einsum("hij...,j...->hi...",d,C,optimize=True)
  for h in range(4):
   for n in range(4):
    for r in range(4):
     dcl[h,n]+=g[n,r]*(np.einsum("ij...,ij...->...",dinv[h],gam[r])+
                    np.einsum("ij...,ij...->...",inv,dgam0[h,r]))
  cov=dcl-np.einsum("rij...,r...->ij...",gam,cl,optimize=True)
  Q=R0-.5*(cov+cov.swapaxes(0,1))
  u,v=phi;D=1+u*u+v*v
  target=np.array([[1-u*u/D,-u*v/D],[-u*v/D,1-v*v/D]])
  dp=np.zeros((2,4)+shape);dp[:,0]=pi;dp[:,1:]=self.grad(phi).swapaxes(0,1)
  hp=np.zeros((2,4,4)+shape)
  hp[:,0,1:]=self.grad(pi).swapaxes(0,1);hp[:,1:,0]=hp[:,0,1:]
  hp[:,1:,1:]=self.second(phi).transpose(2,0,1,3,4,5)
  source=np.einsum("AB...,Ai...,Bj...->ij...",target,dp,dp,optimize=True)
  cross=2*np.einsum("k...,kij...->ij...",inv[0,1:],dd[0,1:],optimize=True)
  space=np.einsum("kl...,klij...->ij...",inv[1:,1:],dd[1:,1:],optimize=True)
  pt=(2*(Q-self.kappa*source)-cross-space)/inv[0,0]
  dot=np.einsum("AB...,Ai...,Bj...,ij...->...",target,dp,dp,inv,optimize=True)
  crossp=2*np.einsum("k...,Ak...->A...",inv[0,1:],hp[:,0,1:],optimize=True)
  spacep=np.einsum("ij...,Aij...->A...",inv[1:,1:],hp[:,1:,1:],optimize=True)
  pit=(phi*dot+np.einsum("i...,Ai...->A...",C,dp,optimize=True)-crossp-spacep)/inv[0,0]
  if monitor:return max(abs(C).ravel()),float(np.min(inv[0,0]))
  return p,pt,pi,pit
 def adm(self,y):
  g,p,phi,vel=y;shape=(self.N,)*3
  gamma=g[1:,1:]
  inv=np.moveaxis(np.linalg.inv(np.moveaxis(gamma,(0,1),(-2,-1))),(-2,-1),(0,1))
  inv4=np.moveaxis(np.linalg.inv(np.moveaxis(g,(0,1),(-2,-1))),(-2,-1),(0,1))
  alpha=1/np.sqrt(-inv4[0,0]);beta=np.einsum("ij...,j...->i...",inv,g[0,1:])
  dg=self.grad(gamma);christ=np.zeros((3,3,3)+shape)
  for a in range(3):
   for i in range(3):
    for j in range(3):
     for l in range(3):
      christ[a,i,j]+=.5*inv[a,l]*(dg[i,l,j]+dg[j,l,i]-dg[l,i,j])
  dc=self.grad(christ);ric=np.zeros((3,3)+shape)
  for i in range(3):
   for j in range(3):
    for l in range(3):
     ric[i,j]+=dc[l,l,i,j]-dc[j,l,i,l]
     for m in range(3):
      ric[i,j]+=christ[l,i,j]*christ[m,l,m]-christ[l,i,m]*christ[m,j,l]
  betacov=g[0,1:];db=self.grad(betacov);K=np.zeros((3,3)+shape)
  for i in range(3):
   for j in range(3):
    K[i,j]=(-p[i+1,j+1]+db[i,j]+db[j,i]-
      2*np.einsum("l...,l...->...",christ[:,i,j],betacov))/(2*alpha)
  mixed=np.einsum("ik...,kj...->ij...",inv,K)
  tr=np.einsum("ij...,ij...->...",inv,K)
  fp=self.grad(phi).swapaxes(0,1)
  Pi=(vel-np.einsum("i...,Ai...->A...",beta,fp))/alpha
  u,v=phi;D=1+u*u+v*v
  target=np.array([[1-u*u/D,-u*v/D],[-u*v/D,1-v*v/D]])
  rho=.5*(np.einsum("ab...,a...,b...->...",target,Pi,Pi)+
       np.einsum("ab...,ai...,bj...,ij...->...",target,fp,fp,inv))
  j=-np.einsum("ab...,a...,bi...->i...",target,Pi,fp)
  ham=(np.einsum("ij...,ij...->...",inv,ric)+tr**2
       -np.einsum("ij...,ji...->...",mixed,mixed)-2*self.kappa*rho)
  dkm=self.grad(mixed);dtr=self.grad(tr);mom=np.zeros((3,)+shape)
  for i in range(3):
   for q in range(3):
    mom[i]+=dkm[q,q,i]
    for l in range(3):
     mom[i]+=christ[q,q,l]*mixed[l,i]-christ[l,q,i]*mixed[q,l]
   mom[i]-=dtr[i]+self.kappa*j[i]
  return float(np.max(abs(ham))),float(np.max(abs(mom)))
def rk4(y,dt,rhs):
 add=lambda a,b,c:tuple(x+c*z for x,z in zip(a,b))
 k1=rhs(y);k2=rhs(add(y,k1,dt/2));k3=rhs(add(y,k2,dt/2));k4=rhs(add(y,k3,dt))
 return tuple(x+dt*(a+2*b+2*c+d)/6 for x,a,b,c,d in zip(y,k1,k2,k3,k4))
if __name__=="__main__":
 for N in (16,24,32):
  solver=GHGrid(N);y=initial(N)
  print("initial",N,solver.rhs(y,True),solver.adm(y),flush=True)
  for _ in range(4):y=rk4(y,.004,solver.rhs)
  C,gtt=solver.rhs(y,True);H,M=solver.adm(y)
  print("final",N,dict(time=.016,gh=C,ham=H,mom=M,gtt=gtt),flush=True)
  assert gtt<0 and np.isfinite(C+H+M)
 print("OPEN longer-time convergence, independent validation and Weyl–Maxwell EFT")
