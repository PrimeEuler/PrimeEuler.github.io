#!/usr/bin/env python3
"""v15.1491: Solve projected nonlinear Einstein-H2 ADM H/M constraints
with every nonlinear source evaluated on a 2x padded Fourier grid.
Compare the projected residual to independent *full* 2x-grid residual.
Dealiased RHS is NOT a proof of pointwise constraints at fixed N.
"""
import numpy as np
from scipy.signal import resample
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid

def resize(a,M):
 for ax in (-3,-2,-1):a=resample(a,M,axis=ax)
 return a.real

def solve(N,kappa=.003):
 M=2*N;coarse=GHGrid(N);fine=GHGrid(M)
 x=np.arange(N)*2*np.pi/N;X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 phi=np.array([.16*np.sin(X),.13*np.sin(2*Y+.3)])
 Pi=np.array([.10*np.sin(2*X),.09*np.sin(4*Y+.6)])
 ph=resize(phi,M);pn=resize(Pi,M)
 u,v=ph;D=1+u*u+v*v
 G=np.array([[1-u*u/D,-u*v/D],[-u*v/D,1-v*v/D]])
 gp=fine.grad(ph).swapaxes(0,1)
 kin=np.einsum("ab...,a...,b...->...",G,pn,pn)
 spatial=np.einsum("ab...,ai...,bi...->...",G,gp,gp)
 j=-np.einsum("ab...,a...,bi...->i...",G,pn,gp)
 rho=.5*(kin+spatial)
 ks=coarse.k;k2=np.sum(ks*ks,axis=0);nz=k2>0
 def invlap(src):
  F=np.fft.fftn(src,axes=(-3,-2,-1));out=np.zeros_like(F)
  out[...,nz]=-F[...,nz]/k2[nz]
  return np.fft.ifftn(out,axes=(-3,-2,-1)).real
 def invL(src):
  F=np.fft.fftn(src,axes=(-3,-2,-1))
  dot=np.einsum("i...,i...->...",ks,F)
  longitudinal=np.zeros_like(F)
  longitudinal[:,nz]=ks[:,nz]*dot[nz]/k2[nz]
  W=np.zeros_like(F)
  W[:,nz]=-(F[:,nz]-.25*longitudinal[:,nz])/k2[nz]
  return np.fft.ifftn(W,axes=(-3,-2,-1)).real
 def L(W):
  derivative=fine.grad(resize(W,M))
  A=derivative+derivative.swapaxes(0,1)
  divergence=sum(derivative[i,i] for i in range(3))
  for i in range(3):A[i,i]-=2*divergence/3
  return A
 psi=invlap(-kappa*resize(rho,N)/2)
 W=invL(kappa*resize(j,N))
 for iteration in range(24):
  psi_f=resize(psi,M);A=L(W)
  gradpsi=fine.grad(psi_f)
  grad2=np.sum(gradpsi*gradpsi,axis=0)
  q=np.exp(2*psi_f);A2=np.sum(A*A,axis=(0,1))
  H2=np.mean(2*grad2+q*(A2+kappa*kin)+kappa*spatial)/(6*q.mean())
  rhs=(-2*grad2+q*(6*H2-A2-kappa*kin)-kappa*spatial)/4
  next_psi=invlap(resize(rhs,N))
  next_W=invL(resize(kappa*j-3*np.einsum("j...,ij...->i...",
                                      fine.grad(resize(next_psi,M)),A),N))
  change=max(np.max(abs(next_psi-psi)),np.max(abs(next_W-W)))
  psi,W=next_psi,next_W
  if change<1e-15:break
 psi_f=resize(psi,M);A=L(W)
 gradpsi=fine.grad(psi_f);grad2=np.sum(gradpsi*gradpsi,axis=0)
 q=np.exp(2*psi_f);A2=np.sum(A*A,axis=(0,1))
 H2=np.mean(2*grad2+q*(A2+kappa*kin)+kappa*spatial)/(6*q.mean())
 lap=np.fft.ifftn(-np.sum(fine.k**2,axis=0)*np.fft.fftn(psi_f)).real
 ham=(-4*lap-2*grad2)+q*(6*H2-A2-kappa*kin)-kappa*spatial
 Ah=np.fft.fftn(A,axes=(-3,-2,-1))
 flatdiv=np.fft.ifftn(np.sum(1j*fine.k[:,None]*Ah,axis=0),axes=(-3,-2,-1)).real
 mom=flatdiv+3*np.einsum("j...,ij...->i...",gradpsi,A)-kappa*j
 projH=float(np.max(abs(resize(ham,N))))
 projM=float(np.max(abs(resize(mom,N))))
 offH=float(np.max(abs(ham)));offM=float(np.max(abs(mom)))
 out=dict(N=N,iterations=iteration+1,projected_H=projH,
          projected_M=projM,offgrid_H=offH,offgrid_M=offM)
 print(out,flush=True)
 assert projH<1e-14 and projM<(2e-11 if N==16 else 1e-12)
 assert offH>100*projH and offM>100*projM
 return out

if __name__=="__main__":
 results=[solve(N) for N in (16,24,32)]
 assert all(results[i]["offgrid_H"]>results[i+1]["offgrid_H"] for i in (0,1))
 assert all(results[i]["offgrid_M"]>results[i+1]["offgrid_M"] for i in (0,1))
 print("PASS projected dealiased elliptic equations; off-grid residuals converge with N")
 print("NEGATIVE at fixed N, projected constraints are NOT pointwise constraints")
 print("OPEN high-grid constraint-certified 3D GH evolution and Maxwell/Weyl EFT")
