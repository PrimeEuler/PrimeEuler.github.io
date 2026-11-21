#!/usr/bin/env python3
"""Gravity v15.1275: independent homogeneous Bianchi-I Einstein 00 and
three spatial equations; original Nyquist-clean Maxwell stress.
Not an inhomogeneous ADM constraint or optical detection test."""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp
from math import sqrt,pi

def run(N=24,end=1.08,nt=33):
 L=4*pi;x=(np.arange(N)-N//2)*L/N
 X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
 f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
 fp=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
 E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),-fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
 q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing='ij'))
 k=np.sqrt(np.sum(q*q,axis=0));unit=np.zeros_like(q)
 np.divide(q,k,out=unit,where=k>0)
 h=np.fft.fftn(E0,axes=(1,2,3));h-=unit*np.einsum('i...,i...->...',unit,h)
 h[:,np.any(abs(q)==N/2*2*pi/L,axis=0)]=0
 curl=1j*np.cross(q,h,axis=0)
 def stress(t):
  xi=sqrt(3)*np.log(t)
  sinc=np.zeros_like(k);np.divide(np.sin(k*xi),k,out=sinc,where=k>0)
  e=(h*np.cos(k*xi)).reshape(3,-1)
  b=(-curl*sinc).reshape(3,-1)
  M=(e@e.conj().T+b@b.conj().T).real/N**6
  rho=float(np.trace(M)/2)
  Pi=np.diag(2*rho*np.eye(3)/3-M)
  return rho,Pi
 ts=np.linspace(1,end,nt)
 means=np.array([stress(t)[0] for t in ts]);pis=np.array([stress(t)[1] for t in ts])
 R=float(means[0]);drift=float(np.max(abs(means-R)))
 ps=CubicSpline(ts,pis,axis=0)
 mass=2.0
 def rhs(t,y):
  be=y[:3];vel=y[3:]
  return np.r_[vel,-3*vel/t-mass*be/t**2+9*ps(t)/t**4]
 sol=solve_ivp(rhs,(1,end),np.zeros(6),rtol=1e-12,atol=1e-15,dense_output=True)
 assert sol.success
 def u(t):return 1.5*R*(t-1)/t**2
 def ud(t):return 1.5*R*(2-t)/t**3
 def udd(t):return 1.5*R*(2*t-6)/t**4
 checks=[]
 for t in ts:
  beta,bd=np.split(sol.sol(t),2);bdd=rhs(t,sol.sol(t))[3:]
  # Geometric Bianchi-I: G00=sum(i<j)H_i H_j, H_i=1/t+u'+beta_i'
  G00_pert=6*ud(t)/t
  T00_pert=-6*u(t)/t**2+9*R/t**4
  ham=G00_pert-T00_pert
  # G^i_i=-(H_j'+H_k'+H_j^2+H_k^2+H_j H_k)
  Gii_pert=-2*udd(t)-6*ud(t)/t+bdd+3*bd/t
  # solid isotropic p perturbation + Maxwell isotropic/STF + solid shear
  Tii_pert=2*u(t)/t**2+3*R/t**4+9*ps(t)/t**4-mass*beta/t**2
  spatial=Gii_pert-Tii_pert
  iso=-2*udd(t)-6*ud(t)/t-2*u(t)/t**2-3*R/t**4
  checks.append((abs(ham),max(abs(spatial)),abs(iso),abs(beta.sum())))
 checks=np.array(checks)
 out={'N':N,'times':nt,'tau_final':end,'rho_mean':R,'rho_drift':drift,
      'max_Hamiltonian':float(checks[:,0].max()),
      'max_spatial':float(checks[:,1].max()),
      'max_iso':float(checks[:,2].max()),
      'max_beta_trace':float(checks[:,3].max()),
      'beta_final':sol.sol(end)[:3].tolist(),'u_final':u(end)}
 print(out,flush=True)
 assert out['max_Hamiltonian']<1e-12
 assert out['max_spatial']<1e-11
 assert out['max_iso']<1e-12
 assert out['max_beta_trace']<1e-10
 return out

if __name__=='__main__':
 for N in (16,24,32,40,48):run(N)
 print('PASS homogeneous 00 and all spatial Bianchi-I Einstein equations')
 print('OPEN nonzero-mode ADM Hamiltonian/momentum and spatial field equations')
