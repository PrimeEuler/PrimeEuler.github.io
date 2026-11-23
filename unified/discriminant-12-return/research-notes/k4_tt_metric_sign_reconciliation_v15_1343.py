#!/usr/bin/env python3
"""Gravity v15.1343: dealiased Maxwell TT physical-metric sign reconciliation.
Historical gamma_old evolves with negative Maxwell source; physical spatial
strain h=-gamma_old obeys the positive-source Einstein TT equation. The
source and metric conventions are explicit; no parent files modified.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from math import pi,sqrt

def run(N,nt=31,tfinal=1.12):
 L=4*pi;x=(np.arange(N)-N//2)*L/N
 X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
 f=lambda q:np.where(abs(q)<1,(1-q*q)**3,0.)
 fp=lambda q:np.where(abs(q)<1,-6*q*(1-q*q)**2,0.)
 E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),-fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
 q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing='ij'))
 k=np.sqrt(np.sum(q*q,axis=0));n=np.zeros_like(q);np.divide(q,k,out=n,where=k>0)
 h=np.fft.fftn(E0,axes=(1,2,3))
 h-=n*np.einsum('i...,i...->...',n,h)
 h[:,np.any(abs(q)==N/2*2*pi/L,axis=0)]=0
 curl=1j*np.cross(q,h,axis=0)
 M=2*N;pads=[(0,0)]+[(N//2,N//2)]*3
 e=np.array([1.,0.,-1.])/sqrt(2);b=np.array([0.,1.,0.])
 def inv(A):
  v=np.fft.ifftshift(np.pad(np.fft.fftshift(A,axes=(1,2,3)),pads),axes=(1,2,3))*8
  return np.fft.ifftn(v,axes=(1,2,3)).real
 def source(t):
  xi=sqrt(3)*np.log(t);sinc=np.zeros_like(k)
  np.divide(np.sin(k*xi),k,out=sinc,where=k>0)
  E=inv(h*np.cos(k*xi));B=inv(-curl*sinc)
  rho=np.sum(E*E+B*B,axis=0)/2
  T=np.eye(3)[:,:,None,None,None]*rho-np.einsum('i...,j...->ij...',E,E)-np.einsum('i...,j...->ij...',B,B)
  pol=(np.einsum('i,ij...,j->...',e,T,e)-np.einsum('i,ij...,j->...',b,T,b))/2
  return np.fft.fftn(pol)[2,0,2]/M**3
 ts=np.linspace(1,tfinal,nt);sourcehist=np.array([source(t) for t in ts])
 spl=CubicSpline(ts,sourcehist)
 mass=8.0 # k²=2, eta_s=3/4 -> 3k²+2
 def evolve(sign):
  def rhs(t,y):return [y[1],-3*y[1]/t-mass*y[0]/t**2+sign*18*spl(t)/t**4]
  sol=solve_ivp(rhs,(1,tfinal),np.zeros(2,dtype=complex),t_eval=ts,
                rtol=2e-11,atol=1e-14)
  assert sol.success
  H,Hd=sol.y
  Hdd=np.array([rhs(t,[H[i],Hd[i]])[1] for i,t in enumerate(ts)])
  # from g_ij=a²(delta_ij+h_ij): Gplus=(h''+3h'/tau+3k²h/tau²)/2;
  # physical Maxwell pressure=9Pi/tau⁴, K4 solid TT pressure=-h/tau².
  residual=(Hdd+3*Hd/ts+6*H/ts**2)/2-9*sourcehist/ts**4+H/ts**2
  return H,residual
 physical=evolve(1);archived=evolve(-1)
 corrected=float(np.max(abs(physical[1])))
 incorrect=float(np.max(abs(archived[1])))
 identity=float(np.max(abs(physical[0]+archived[0])))
 assert corrected<2e-13 and incorrect>1e-4 and identity<2e-13
 out=dict(N=N,nt=nt,tfinal=tfinal,Pi0=float(sourcehist[0].real),
          h_physical_final=float(physical[0][-1].real),
          gamma_archived_final=float(archived[0][-1].real),
          max_corrected_Einstein_residual=corrected,
          max_archived_as_metric_Einstein_residual=incorrect,
          max_gamma_archived_plus_h_physical=identity)
 print(out,flush=True)
 return out

if __name__=='__main__':
 for N in (24,32,48):run(N)
 print('PASS physical TT metric and +Maxwell source Einstein equation')
 print('PASS historical gamma=-physical h source-convention reconciliation')
 print('NEGATIVE archived gamma used directly as physical metric TT strain')
 print('OPEN full 3D physical metric, all Einstein residuals, optical apparatus')
