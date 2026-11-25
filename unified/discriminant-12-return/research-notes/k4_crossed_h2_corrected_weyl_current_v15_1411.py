#!/usr/bin/env python3
"""Gravity v15.1411: actual linear TT Weyl tensor contracted with
leading and fifth-order corrected nonlinear H2 crossed-wave area map.
Current J=-partial_mu(C^{mu nu rho sigma} B_rho sigma);
controlled finite-difference derivatives in prescribed flat background.
"""
import numpy as np
import sympy as sp
A,B,a,b=sp.symbols('A B a b',real=True)
u=a*sp.sin(A);v=b*sp.sin(B)
du=-a**3*b**2*sp.sin(A)**3*sp.sin(B)**2/6
dv=-a**2*b**3*sp.sin(A)**2*sp.sin(B)**3/6
areas=[sp.diff(u,A)*sp.diff(v,B),
       sp.diff(u,A)*sp.diff(v,B)/sp.sqrt(1+u*u+v*v),
       (sp.diff(u+du,A)*sp.diff(v+dv,B)-sp.diff(u+du,B)*sp.diff(v+dv,A))/sp.sqrt(1+(u+du)**2+(v+dv)**2)]
functions=[sp.lambdify((A,B,a,b),f,'numpy') for f in areas]
eta=np.diag([-1.,1.,1.,1.])
pull=np.zeros((4,4))
pull[0,1]=pull[1,2]=1
pull[0,2]=-1
pull-=pull.T
def riemann(t,z):
 h=np.zeros((4,4));co=np.cos(t-z)
 h[0,0]=h[3,3]=-co;h[0,3]=h[3,0]=co
 def dd(i,j,m,n):
  if m==n==1:return h[i,j]
  if m==n==2:return -h[i,j]
  return 0.
 R=np.zeros((4,4,4,4))
 for i in range(4):
  for j in range(4):
   for k in range(4):
    for l in range(4):
     R[i,j,k,l]=(dd(k,j,i,l)+dd(l,i,j,k)-dd(l,j,i,k)-dd(k,i,j,l))/2
 return R
def K(t,x,y,z,amp,mode):
 scalar=float(functions[mode](t-x,t-y,amp,amp))
 B=eta@(pull*scalar)@eta
 return np.einsum('ijrs,rs->ij',riemann(t,z),B)
def current(t,x,y,z,amp,mode,dt=1e-5):
 pos=np.array([t,x,y,z],float)
 J=np.zeros(4)
 for i in range(4):
  pp=pos.copy();pm=pos.copy()
  pp[i]+=dt;pm[i]-=dt
  derivative=(eta@K(*pp,amp,mode)@eta-eta@K(*pm,amp,mode)@eta)/(2*dt)
  J-=derivative[i,:]
 return J
if __name__=='__main__':
 last=None
 for amp in (.3,.15,.075):
  J=[current(.53,.1,-.2,.26,amp,m) for m in range(3)]
  assert np.linalg.norm(J[2])>0
  diff=np.linalg.norm(J[2]-J[1])/np.linalg.norm(J[1])
  print(dict(amplitude=amp,leading=J[0].tolist(),area_normalized=J[1].tolist(),
    sigma_corrected=J[2].tolist(),relative_dynamic_delta=diff),flush=True)
  if last: assert .04<diff/last<.09
  last=diff
 print('PASS true tensor-source survives sigma correction; relative correction scales as amplitude fourth power')
 print('OPEN retarded corrected sigma data, Einstein stress, physical quarter-grid selector')
