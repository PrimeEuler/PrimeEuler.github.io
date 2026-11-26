#!/usr/bin/env python3
"""Nyquist derivative defect and quarter ratio: initial Einstein-H2 torus.
Run with OPENBLAS_NUM_THREADS=1. Compares conformal Hamiltonian using
direct Hessian versus composed real first derivatives, and analytic
time derivative of contracted GH vector from unrestricted metric RHS."""
import numpy as np
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial

def run(N):
 gr=GHGrid(N); y=initial(N);g,p,phi,vel=y;q=g[1,1];psi=np.log(q)/2
 grad=gr.grad(psi);lap=np.trace(gr.second(psi),axis1=0,axis2=1)
 lap1=sum(gr.grad(grad[i])[i] for i in range(3))
 K=-p[1:,1:]/2/q;tr=np.trace(K,axis1=0,axis2=1)
 u,v=phi;D=1+u*u+v*v
 G=np.array([[1-u*u/D,-u*v/D],[-u*v/D,1-v*v/D]])
 fp=gr.grad(phi)
 rho2=np.einsum('ab...,a...,b...->...',G,vel,vel)+np.einsum('ab...,ia...,ib...->...',G,fp,fp)/q
 extra=tr**2-np.sum(K*K,axis=(0,1))-.003*rho2
 H=(-4*lap-2*np.sum(grad*grad,axis=0))/q+extra
 H1=(-4*lap1-2*np.sum(grad*grad,axis=0))/q+extra
 inv=np.moveaxis(np.linalg.inv(np.moveaxis(g,(0,1),(-2,-1))),(-2,-1),(0,1))
 d=np.concatenate((p[None],gr.grad(g)),axis=0)
 dt=np.concatenate((gr.rhs(y)[1][None],gr.grad(p)),axis=0)
 it=-np.einsum('ia...,ab...,bj...->ij...',inv,p,inv,optimize=True)
 def b(a,b,d):
  return np.einsum('ma...,nb...,nab...->m...',a,b,d,optimize=True)-.5*np.einsum('mn...,ab...,nab...->m...',a,b,d,optimize=True)
 C=b(inv,inv,d);Ct=b(it,inv,d)+b(inv,it,d)+b(inv,inv,dt)
 T=(np.einsum('ij...,j...->i...',g,Ct)+np.einsum('ij...,j...->i...',p,C))[0]
 def norm(a):return np.max(abs(a))
 def modes(a):
  F=np.fft.fftn(a)/N**3;ix=np.unravel_index(np.argmax(abs(F)),F.shape)
  return tuple(int(gr.k[i][ix]) for i in range(3)),F[ix]
 mh,mt=modes(H1),modes(T)
 print(N,'H direct',norm(H),'H composed',norm(H1),'T',norm(T),
       'T-H1/4',norm(T-H1/4),'T-H',norm(T-H),
       'lap defect',norm(lap-lap1),'modes',mh,mt,flush=True)
 assert norm(H)<1e-12
 if N%2==0:
  assert mh[0]==mt[0]==(0,-N//2,0)
  assert abs(mt[1]/mh[1]-.25)<1e-3
  assert norm(T-H1/4)<.01*norm(T)
 else:
  assert norm(lap-lap1)<1e-15

if __name__=='__main__':
 for N in (16,24,32,17):run(N)
