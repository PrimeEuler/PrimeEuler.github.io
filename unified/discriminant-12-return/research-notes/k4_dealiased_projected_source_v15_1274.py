#!/usr/bin/env python3
"""v15.1274: test exactly dealiased Maxwell 4-stress in native interior modes."""
import numpy as np
from math import pi,sqrt
def run(N,t=1.08):
 L=4*pi;x=(np.arange(N)-N//2)*L/N
 X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
 f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
 fp=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
 e0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),-fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
 q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing="ij"))
 k=np.sqrt((q*q).sum(0));n=np.zeros_like(q);np.divide(q,k,out=n,where=k>0)
 h=np.fft.fftn(e0,axes=(1,2,3));h-=n*np.einsum("i...,i...->...",n,h)
 h[:,np.any(abs(q)==N/2*2*pi/L,axis=0)]=0
 curl=1j*np.cross(q,h,axis=0);xi=sqrt(3)*np.log(t)
 sinc=np.zeros_like(k);np.divide(np.sin(k*xi),k,out=sinc,where=k>0)
 Ehat=h*np.cos(k*xi);Bhat=-curl*sinc
 Edhat=-h*k*np.sin(k*xi)*sqrt(3)/t;Bdhat=-curl*np.cos(k*xi)*sqrt(3)/t
 M=2*N
 def inv(z):
  pad=[(0,0)]*(z.ndim-3)+[(N//2,N//2)]*3
  v=np.fft.ifftshift(np.pad(np.fft.fftshift(z,axes=(-3,-2,-1)),pad),axes=(-3,-2,-1))
  return np.fft.ifftn(v*8,axes=(-3,-2,-1)).real
 E,B,Ed,Bd=map(inv,(Ehat,Bhat,Edhat,Bdhat))
 rho=(E*E+B*B).sum(0)/2;rhod=(E*Ed+B*Bd).sum(0)
 F=np.cross(E,B,axis=0);Fd=np.cross(Ed,B,axis=0)+np.cross(E,Bd,axis=0)
 T=np.eye(3)[:,:,None,None,None]*rho-np.einsum("i...,j...->ij...",E,E)-np.einsum("i...,j...->ij...",B,B)
 fft=lambda z:np.fft.fftn(z,axes=(-3,-2,-1))/M**3
 R,Rd,Fh,Fdh,Th=map(fft,(rho,rhod,F,Fd,T))
 qm=np.array(np.meshgrid(*([np.fft.fftfreq(M,d=L/M)*2*pi]*3),indexing="ij"))
 re=Rd+sqrt(3)/t*1j*np.einsum("j...,j...->...",qm,Fh)
 rm=Fdh+sqrt(3)/t*1j*np.einsum("j...,ij...->i...",qm,Th)
 m=np.rint(np.fft.fftfreq(N)*N).astype(int);ids=np.mod(m,M)
 valid=abs(m)<N/2;mask=valid[:,None,None]&valid[None,:,None]&valid[None,None,:]
 def pick(z):return z[...,ids[:,None,None],ids[None,:,None],ids[None,None,:]]
 er=float(abs(pick(re)[mask]).max());mr=float(abs(pick(rm)[:,mask]).max())
 out=dict(N=N,tau=t,energy_residual=er,momentum_residual=mr,mean_rho=float(R[0,0,0].real),safe_modes=int(mask.sum()))
 assert er<2e-12 and mr<2e-12
 print(out,flush=True)
 return out
if __name__=="__main__":
 for N in (16,24,32,40,48):run(N)
 print("PASS dealiased Maxwell stress projected onto native non-Nyquist modes")
 print("OPEN coupled Einstein-K4 ADM constraints and full metric")
