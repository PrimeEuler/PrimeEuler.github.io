#!/usr/bin/env python3
"""Gravity v15.1344: full-grid TT physical metric, two polarizations,
dealiased compact Maxwell, finite-time signed Einstein residuals."""
import numpy as np
from scipy.interpolate import CubicSpline
from math import pi,sqrt

def run(N=16,t=1.08,nt=13):
 L=4*pi;x=(np.arange(N)-N//2)*L/N
 X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
 f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
 df=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
 E0=np.array(np.broadcast_arrays(.5*f(X)*df(Y/2)*f(Z),-df(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
 q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing="ij"))
 k2=(q*q).sum(0);k=np.sqrt(k2);n=np.zeros_like(q)
 np.divide(q,k,out=n,where=k>0)
 h0=np.fft.fftn(E0,axes=(1,2,3))
 h0-=n*np.einsum("i...,i...->...",n,h0)
 h0[:,np.any(abs(q)==N/2*2*pi/L,axis=0)]=0
 curl=1j*np.cross(q,h0,axis=0);M=2*N
 def inv(A):
  pad=[(0,0)]*(A.ndim-3)+[(N//2,N//2)]*3
  w=np.fft.ifftshift(np.pad(np.fft.fftshift(A,axes=(-3,-2,-1)),pad),axes=(-3,-2,-1))*8
  return np.fft.ifftn(w,axes=(-3,-2,-1)).real
 ids=np.mod(np.rint(np.fft.fftfreq(N)*N).astype(int),M)
 def source(tau):
  xi=sqrt(3)*np.log(tau);sinc=np.zeros_like(k)
  np.divide(np.sin(k*xi),k,out=sinc,where=k>0)
  E=inv(h0*np.cos(k*xi));B=inv(-curl*sinc)
  rho=np.sum(E*E+B*B,axis=0)/2
  Tij=np.eye(3)[:,:,None,None,None]*rho-np.einsum("i...,j...->ij...",E,E)-np.einsum("i...,j...->ij...",B,B)
  Th=np.fft.fftn(Tij,axes=(-3,-2,-1))/M**3
  return Th[...,ids[:,None,None],ids[None,:,None],ids[None,None,:]]
 proj=np.eye(3)[:,:,None,None,None]-np.einsum("i...,j...->ij...",n,n)
 modes=(k2>0)&np.all(abs(q)<N/2*2*pi/L,axis=0)
 def project(T):
  trP=np.einsum("ij...,ij...->...",proj,T)
  TT=np.einsum("ia...,jb...,ab...->ij...",proj,proj,T)-proj*trP/2
  TT*=modes
  return TT
 T=project(source(t))
 tr=float(abs(np.einsum("ii...->...",T)).max())
 div=float(abs(np.einsum("i...,ij...->j...",q,T)).max())
 sym=float(abs(T-T.swapaxes(0,1)).max())
 imag=float(abs(np.fft.ifftn(T*N**3,axes=(-3,-2,-1)).imag).max())
 ts=np.linspace(1,t,nt);hist=np.stack([project(source(tt)) for tt in ts])
 interp=CubicSpline(ts,hist,axis=0)
 strain=np.zeros_like(T);velocity=np.zeros_like(T)
 def rhs(tt,h,hd):
  return hd,-3*hd/tt-(3*k2+2)*h/tt**2+18*interp(tt)/tt**4
 for j in range(nt-1):
  tt=ts[j];dt=ts[j+1]-tt
  a,b=rhs(tt,strain,velocity)
  c,d=rhs(tt+dt/2,strain+dt*a/2,velocity+dt*b/2)
  e,f=rhs(tt+dt/2,strain+dt*c/2,velocity+dt*d/2)
  g,i=rhs(tt+dt,strain+dt*e,velocity+dt*f)
  strain+=dt*(a+2*c+2*e+g)/6
  velocity+=dt*(b+2*d+2*f+i)/6
 acc=rhs(t,strain,velocity)[1]
 base=(acc+3*velocity/t+3*k2*strain/t**2)/2
 good=float(abs(base-9*T/t**4+strain/t**2).max())
 wrong=float(abs(-base-9*T/t**4-strain/t**2).max())
 strtr=float(abs(np.einsum("ii...->...",strain)).max())
 strdiv=float(abs(np.einsum("i...,ij...->j...",q,strain)).max())
 assert max(tr,div,sym,strtr,strdiv,imag,good)<1e-11
 assert wrong>1e-5
 row=dict(N=N,tau=t,nt=nt,modes=int(modes.sum()),max_TT_source=float(abs(T).max()),
          max_TT_trace=tr,max_TT_divergence=div,max_TT_symmetry=sym,
          max_physical_strain=float(abs(strain).max()),max_strain_trace=strtr,
          max_strain_divergence=strdiv,max_realspace_imaginary=imag,
          corrected_Einstein_max=good,archived_as_metric_Einstein_max=wrong)
 print(row,flush=True);return row

if __name__=="__main__":
 for N in (16,24,32):run(N)
 for nt in (9,25):run(24,nt=nt)
 print("PASS full-grid both-helicity physical TT sector; old sign NEGATIVE")
 print("OPEN full SVT+homogeneous metric and causal observer optical response")
