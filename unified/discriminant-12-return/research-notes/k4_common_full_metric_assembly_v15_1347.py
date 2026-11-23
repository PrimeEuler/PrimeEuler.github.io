#!/usr/bin/env python3
"""Gravity v15.1347: one Maxwell source => full linearized k>0 S/V/TT +
k=0 Bianchi metric; source-equation conditional residuals, weak-field gate.
No independent off-shell Einstein tensor nor causal photon clock calculation.
"""
import numpy as np
from math import pi,sqrt
from scipy.interpolate import CubicSpline

def run(N=12,nt=13,tf=1.08,amplitude=0.1):
 L=4*pi;x=(np.arange(N)-N//2)*L/N
 X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
 f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
 fp=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
 E0=amplitude*np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),-fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
 q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing="ij"))
 k2=np.sum(q*q,axis=0);k=np.sqrt(k2);n=np.zeros_like(q)
 np.divide(q,k,out=n,where=k>0)
 mask=(k2>0)&np.all(abs(q)<N/2*2*pi/L,axis=0)
 H=np.fft.fftn(E0,axes=(1,2,3));H-=n*np.einsum("i...,i...->...",n,H)
 H[:,np.any(abs(q)==N/2*2*pi/L,axis=0)]=0
 curl=1j*np.cross(q,H,axis=0);M=2*N
 idx=np.mod(np.rint(np.fft.fftfreq(N)*N).astype(int),M)
 I=np.eye(3)[:,:,None,None,None]
 Q=I-np.einsum("i...,j...->ij...",n,n)
 def inv(v):
  pad=[(0,0)]*(v.ndim-3)+[(N//2,N//2)]*3
  z=np.fft.ifftshift(np.pad(np.fft.fftshift(v,axes=(-3,-2,-1)),pad),axes=(-3,-2,-1))*8
  return np.fft.ifftn(z,axes=(-3,-2,-1)).real
 def fft(v):
  z=np.fft.fftn(v,axes=(-3,-2,-1))/M**3
  return z[...,idx[:,None,None],idx[None,:,None],idx[None,None,:]]
 def source(t):
  xi=sqrt(3)*np.log(t);sn=np.zeros_like(k);np.divide(np.sin(k*xi),k,out=sn,where=k>0)
  E,B,Ed,Bd=map(inv,(H*np.cos(k*xi),-curl*sn,-H*k*np.sin(k*xi)*sqrt(3)/t,-curl*np.cos(k*xi)*sqrt(3)/t))
  rho=np.sum(E*E+B*B,axis=0)/2;rd=np.sum(E*Ed+B*Bd,axis=0)
  F=np.cross(E,B,axis=0);Fd=np.cross(Ed,B,axis=0)+np.cross(E,Bd,axis=0)
  Tij=I*rho-np.einsum("i...,j...->ij...",E,E)-np.einsum("i...,j...->ij...",B,B)
  r,rp,Fh,Fhp,Th=map(fft,(rho,rd,F,Fd,Tij))
  Fn=np.einsum("i...,i...->...",n,Fh);Fnd=np.einsum("i...,i...->...",n,Fhp)
  Fperp=Fh-n*Fn
  Tnn=np.einsum("i...,ij...,j...->...",n,Th,n)
  Tnp=np.einsum("ij...,j...->i...",Th,n)-n*Tnn
  Ttt=np.einsum("ia...,jb...,ab...->ij...",Q,Q,Th)-Q*np.einsum("ab...,ab...->...",Q,Th)/2
  for v in (r,rp,Fn,Fnd,Tnn):v[~mask]=0
  for v in (Fperp,Tnp):v[:,~mask]=0
  Ttt[:,:,~mask]=0
  Tmean=Th[:,:,0,0,0].real;R=float(rho.mean())
  Pi=np.diag(Tmean)-np.trace(Tmean)/3
  return r,rp,Fn,Fnd,Fperp,Tnn,Tnp,Ttt,R,Pi
 ts=np.linspace(1,tf,nt)
 series=[source(t) for t in ts]
 spl=[CubicSpline(ts,np.stack([z[j] for z in series]),axis=0) for j in range(10)]
 p=np.zeros((2,N,N,N),complex);v=np.zeros((2,3,N,N,N),complex)
 h=np.zeros((2,3,3,N,N,N),complex);sh=np.zeros((2,3))
 def rhs(t,p,v,h,sh):
  r,_,_,_,_,Tnn,Tnp,Ttt,R,Pi=(s(t) for s in spl)
  force=np.zeros_like(r);np.divide(9*(3*Tnn-r),2*k2*t**4,out=force,where=mask)
  vf=np.zeros_like(Tnp);np.divide(-18j*Tnp,k*t**4,out=vf,where=mask)
  return (np.stack((p[1],-3*p[1]/t-(2+k2)*p[0]/t**2+force)),
          np.stack((v[1],-3*v[1]/t-(4+3*k2)*v[0]/(2*t**2)+vf)),
          np.stack((h[1],-3*h[1]/t-(3*k2+2)*h[0]/t**2+18*Ttt/t**4)),
          np.stack((sh[1],-3*sh[1]/t-2*sh[0]/t**2+9*Pi/t**4)))
 for j in range(nt-1):
  t=ts[j];dt=ts[j+1]-t;u=(p,v,h,sh)
  a=rhs(t,*u);b=rhs(t+dt/2,*(x+dt*y/2 for x,y in zip(u,a)))
  c=rhs(t+dt/2,*(x+dt*y/2 for x,y in zip(u,b)))
  d=rhs(t+dt,*(x+dt*y for x,y in zip(u,c)))
  for x,aa,bb,cc,dd in zip(u,a,b,c,d):x+=dt*(aa+2*bb+2*cc+dd)/6
 t=tf;r,rd,Fn,Fnd,Fperp,Tnn,Tnp,Ttt,R,Pi=source(t)
 Pdd,Vdd,Hdd,_=(x[1] for x in rhs(t,p,v,h,sh))
 safe=np.where(mask,k2,1);den=1+k2
 jb=-1j*sqrt(3)*k*Fn/t
 jbd=(-3*k2*Tnn+1j*sqrt(3)*k*Fn)/t**2
 phi=((t*t*Pdd+2*t*p[1])/3-3*r/t**2-3*jbd/(2*safe))/den
 psi=((k2*p[0]-t*p[1])/3-3*r/(2*t**2)+3*jb/(2*safe*t))/den
 jbp=-1j*sqrt(3)*k*(Fnd/t-Fn/t**2)
 psid=((k2*p[1]-p[1]-t*Pdd)/3-3*rd/(2*t**2)+3*r/t**3+
       3*(jbp/t-jb/t**2)/(2*safe))/den
 for z in (phi,psi,psid):z[~mask]=0
 D=4+3*k2
 Bv=4*t*v[1]/(sqrt(3)*D)+18*Fperp/(t*t*D)
 Fpd=-1j*sqrt(3)*k*Tnp/t
 Bvd=4*(v[1]+t*Vdd)/(sqrt(3)*D)+18*(Fpd/t**2-2*Fperp/t**3)/D
 Qs=t*psid+phi
 C00=6*(k2*psi+Qs)/t**2+9*r/t**4+6*psi/t**2-2*k2*p[0]/t**2
 C0s=-2j*k*Qs/t-3*sqrt(3)*Fn/t**3+2j*k*p[1]/3
 C0v=sqrt(3)*k2*Bv/(2*t)-3*sqrt(3)*Fperp/t**3-2*(v[1]-sqrt(3)*Bv/t)/3
 Cv=sqrt(3)*1j*k*(t*Bvd+2*Bv)/(2*t**2)-9*Tnp/t**4+1j*k*v[0]/t**2
 Ct=(Hdd+3*h[1]/t+3*k2*h[0]/t**2)/2-9*Ttt/t**4+h[0]/t**2
 # Single numerical four-metric: homogeneous k0 plus all S/V/TT nonzero modes.
 a=t/sqrt(3);hom_u=1.5*R*(t-1)/t**2
 metric_spatial=-2*I*psi+h[0]
 metric_spatial[:,:,0,0,0]=np.diag(2*hom_u+2*sh[0])
 inverse=lambda z:np.fft.ifftn(N**3*z,axes=(-3,-2,-1))
 g00=-1+inverse(-2*phi)
 g0i=inverse(-a*Bv)
 gij=a*a*(I[:,:,:1,:1,:1]+inverse(metric_spatial))
 maxinter=lambda z:float(abs(z[...,mask]).max())
 reality=max(float(abs(g00.imag).max()),float(abs(g0i.imag).max()),float(abs(gij.imag).max()))
 symmetric=float(abs(gij-gij.swapaxes(0,1)).max())
 weak_lapse=float(abs(g00.real+1).max())
 weak_spatial=float(abs(gij.real/(a*a)-I[:,:,:1,:1,:1]).max())
 row=dict(N=N,nt=nt,amplitude=amplitude,tau=t,source_mean=R,
          max_weak_lapse=weak_lapse,max_weak_spatial=weak_spatial,
          max_shift=float(abs(g0i.real).max()),
          max_H00=maxinter(C00),max_Mlong=maxinter(C0s),
          max_Mtrans=maxinter(C0v),max_Svector=maxinter(Cv),
          max_STT=maxinter(Ct),max_metric_imag=reality,
          max_metric_asym=symmetric,
          max_TT_transverse=float(abs(np.einsum("i...,ij...->j...",q,h[0])).max()),
          max_TT_trace=float(abs(np.einsum("ii...->...",h[0])).max()))
 assert max(row[z] for z in ("max_H00","max_Mlong","max_Mtrans","max_Svector","max_STT","max_metric_imag","max_metric_asym","max_TT_transverse","max_TT_trace"))<3e-10
 if amplitude<=0.1:assert weak_lapse<0.01 and weak_spatial<0.01
 print(row,flush=True);return row

if __name__=="__main__":
 for N in (12,16,24,32):run(N)
 run(24,amplitude=1.0) # large weak-field error: negative admissibility control
 for nt in (9,25):run(16,nt=nt)
 print("PASS common-source conditional S/V/TT + homogeneous real four-metric")
 print("OPEN independent off-shell all-component Einstein tensor and optical path")
