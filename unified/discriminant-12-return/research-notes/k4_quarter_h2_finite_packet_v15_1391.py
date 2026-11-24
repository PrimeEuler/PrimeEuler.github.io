#!/usr/bin/env python3
"""v15.1391 finite-energy periodic sigma/TT free packets and Weyl-area
transverse Maxwell current. Physical real fields. Does not evolve backreaction.
"""
import numpy as np
from math import pi,sqrt
def trial(N=16,width=2.,t=.3,step=.0008,misalign=False,physical_real=True,
          sigma_multiplier=1.,gravity_multiplier=1.,quiet=False,output_vector=False):
 L=np.array([4*pi,4*pi,2*pi*sqrt(2)])
 x=[(np.arange(N)-N//2)*l/N for l in L]
 X,Y,Z=np.meshgrid(*x,indexing='ij')
 q=np.array(np.meshgrid(*[np.fft.fftfreq(N,d=l/N)*2*pi for l in L],indexing='ij'))
 norm=np.sqrt(np.sum(q*q,axis=0));good=norm>1e-14
 env=np.exp(-.5*(X*X+Y*Y+Z*Z)/width**2)
 p=np.array([1.,0,0]);vv=np.array([0,1.,0]);gw=np.array([.5,.5,1/sqrt(2)])
 if misalign:gw=np.array([0.,0.,sqrt(2)])
 def seed(k,amp):return np.fft.fftn(amp*env*np.exp(1j*(k[0]*X+k[1]*Y+k[2]*Z)))
 uh=seed(p,.065*sigma_multiplier);vh=seed(vv,.07*sigma_multiplier)
 H0=seed(-gw,.025*gravity_multiplier)
 ez=gw/np.linalg.norm(gw);e1=np.array([1.,-1.,0.])/sqrt(2);e2=np.cross(ez,e1)
 base=np.outer(e1,e1)-np.outer(e2,e2)
 nh=np.divide(q,norm,out=np.zeros_like(q),where=good)
 Q=np.eye(3)[:,:,None,None,None]-np.einsum('i...,j...->ij...',nh,nh)
 Hp=np.einsum('ia...,jb...,ab...->ij...',Q,Q,base[:,:,None,None,None]*H0)
 Hp-=Q*np.einsum('ab...,ab...->...',Q,base[:,:,None,None,None]*H0)/2
 Hp[:,:,~good]=0
 ix=lambda z:np.fft.ifftn(z,axes=(-3,-2,-1))
 def evalK(time):
  Uf=uh*np.exp(-1j*norm*time);Vf=vh*np.exp(-1j*norm*time)
  Hf=Hp*np.exp(1j*norm*time)
  d=np.empty((2,4,N,N,N),complex)
  for fld,F in enumerate([Uf,Vf]):
   for mu in range(4):
    z=ix((-1j*norm if mu==0 else 1j*q[mu-1])*F)
    d[fld,mu]=z.real if physical_real else z
  B=np.einsum('a...,b...->ab...',d[0],d[1])-np.einsum('a...,b...->ab...',d[1],d[0])
  sign=np.array([-1,1,1,1])
  Bup=B*sign[:,None,None,None,None]*sign[None,:,None,None,None]
  dmu=np.empty((4,N,N,N),complex);dmu[0]=1j*norm;dmu[1:]=1j*q
  deriv={}
  for aa in range(4):
   for bb in range(aa,4):
    z=ix(Hf*dmu[aa]*dmu[bb])
    deriv[aa,bb]=z.real if physical_real else z
  def dh(a,b,i,j):
   if i==0 or j==0:return 0
   return deriv[min(a,b),max(a,b)][i-1,j-1]
  K=np.zeros((4,4,N,N,N),complex)
  for mu in range(4):
   for nu in range(mu+1,4):
    vtot=np.zeros((N,N,N),complex)
    for rho in range(4):
     for sig in range(4):
      R=(dh(nu,rho,mu,sig)+dh(mu,sig,nu,rho)-dh(nu,sig,mu,rho)-dh(mu,rho,nu,sig))/2
      vtot+=R*Bup[rho,sig]
    K[mu,nu]=vtot;K[nu,mu]=-vtot
  return K
 K0=evalK(t);Kp=evalK(t+step);Km=evalK(t-step)
 Kf=np.fft.fftn(K0,axes=(-3,-2,-1))/N**3
 Ktf=np.fft.fftn((Kp-Km)/(2*step),axes=(-3,-2,-1))/N**3
 sign=np.array([-1,1,1,1])
 Kup=Kf*sign[:,None,None,None,None]*sign[None,:,None,None,None]
 Ktup=Ktf*sign[:,None,None,None,None]*sign[None,:,None,None,None]
 J=np.zeros((4,N,N,N),complex)
 for nu in range(4):
  J[nu]=-Ktup[0,nu]
  for mu in range(1,4):J[nu]-=1j*q[mu-1]*Kup[mu,nu]
 Jtime0=np.zeros((N,N,N),complex)
 for i in range(1,4):Jtime0-=1j*q[i-1]*Ktup[i,0]
 maxward=float(np.max(abs(Jtime0+np.sum(1j*q*J[1:],axis=0))))
 assert maxward<1e-12
 def energy(when):
  uf=uh*np.exp(-1j*norm*when);vf=vh*np.exp(-1j*norm*when);hf=Hp*np.exp(1j*norm*when)
  def scalar(F,dot):
   R=np.fft.fftn(ix(F).real);D=np.fft.fftn(ix(dot).real)
   return float(np.sum(abs(D)**2+norm**2*abs(R)**2)/(2*N**6))
  Eu=scalar(uf,-1j*norm*uf);Ev=scalar(vf,-1j*norm*vf)
  Hr=np.fft.fftn(ix(hf).real,axes=(-3,-2,-1))
  Hd=np.fft.fftn(ix(1j*norm*hf).real,axes=(-3,-2,-1))
  Eh=float(np.sum(abs(Hd)**2+norm[None,None]**2*abs(Hr)**2)/(2*N**6))
  return (Eu,Ev,Eh)
 E0=energy(0.);E1=energy(.8)
 assert np.allclose(E0,E1,rtol=1e-12,atol=1e-14)
 target=p+vv-gw
 which=np.unravel_index(np.argmin(np.sum((q-target[:,None,None,None])**2,axis=0)),norm.shape)
 assert np.allclose(q[(slice(None),)+which],target)
 qv=q[(slice(None),)+which];current=J[1:][(slice(None),)+which]
 transverse=current-qv*(qv@current)/(qv@qv)
 out=dict(N=N,width=width,time=t,physical_real=physical_real,misalign=misalign,
  sigma_u_energy=E0[0],sigma_v_energy=E0[1],tensor_energy=E0[2],
  free_energy_relative_drift=float(max(abs(np.array(E0)-np.array(E1)))/max(E0)),
  matched_mode_k=qv.tolist(),matched_k2=float(qv@qv),
  matched_J_transverse=float(np.linalg.norm(transverse)),
  matched_J_total=float(np.linalg.norm(current)),ward_max=maxward,
  sigma_multiplier=sigma_multiplier,gravity_multiplier=gravity_multiplier)
 if not quiet:print(out,flush=True)
 if output_vector:return out,transverse
 return out
if __name__=='__main__':
 for n in (12,16,24):trial(n)
 for w in (1.7,2.4):trial(16,width=w)
 base=trial(16);half=trial(16,sigma_multiplier=.5)
 none=trial(16,sigma_multiplier=0);no_gw=trial(16,gravity_multiplier=0)
 assert abs(base['matched_J_transverse']/half['matched_J_transverse']-4)<1e-10
 assert none['matched_J_transverse']<1e-18 and no_gw['matched_J_transverse']<1e-18
 print('PASS finite periodic-energy real free packets, nonzero transverse Weyl-H2 current')
 print('OPEN total interacting energy conservation, finite radiation, quarter selector')
