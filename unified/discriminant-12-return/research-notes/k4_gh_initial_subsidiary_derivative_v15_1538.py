#!/usr/bin/env python3
"""Gravity v15.1538: initial GH subsidiary normal derivative.
Continuum identity C=0 on a unit-lapse zero-shift slice implies
partial_t C_0=H, partial_t C_i=-2 M_i. Discrete negative on
constrained torus, positive pointwise smooth nonconstraint control.
"""
import numpy as np
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial

def derivative(gr,y):
 g,p,phi,vel=y
 inv=np.moveaxis(np.linalg.inv(np.moveaxis(g,(0,1),(-2,-1))),(-2,-1),(0,1))
 d=np.concatenate((p[None],gr.grad(g)),axis=0)
 pt=gr.rhs(y)[1];dt=np.concatenate((pt[None],gr.grad(p)),axis=0)
 invt=-np.einsum('ia...,ab...,bj...->ij...',inv,p,inv,optimize=True)
 def b(a,b,d):
  return np.einsum('ma...,nb...,nab...->m...',a,b,d,optimize=True)-.5*np.einsum('mn...,ab...,nab...->m...',a,b,d,optimize=True)
 C=b(inv,inv,d);Ct=b(invt,inv,d)+b(inv,invt,d)+b(inv,inv,dt)
 Clt=np.einsum('ij...,j...->i...',g,Ct)+np.einsum('ij...,j...->i...',p,C)
 return C,Clt

def evaluate(N):
 gr=GHGrid(N);y=initial(N);C,Clt=derivative(gr,y);H,M=gr.adm(y)
 out=dict(C=float(np.max(abs(C))),H=H,M=M,
  Ct_lower0=float(np.max(abs(Clt[0]))),Ct_loweri=float(np.max(abs(Clt[1:]))),
  H_norm_gap=float(abs(np.max(abs(Clt[0]))-H)),
  M_norm_gap=float(abs(np.max(abs(Clt[1:]))-2*M)))
 print(N,out,flush=True)
 return out

def control():
 N=17;gr=GHGrid(N);x=2*np.pi*np.arange(N)/N
 X,Y,Z=np.meshgrid(x,x,x,indexing='ij');psi=.005*np.cos(X)*np.cos(Y)
 q=np.exp(2*psi);g=np.zeros((4,4,N,N,N));p=np.zeros_like(g);g[0,0]=-1
 for i in range(3):
  g[i+1,i+1]=q;p[0,i+1]=p[i+1,0]=-gr.grad(psi)[i]
 y=(g,p,np.zeros((2,N,N,N)),np.zeros((2,N,N,N)))
 C,Clt=derivative(gr,y)
 H=(-4*gr.second(psi).trace(axis1=0,axis2=1)-2*np.sum(gr.grad(psi)**2,axis=0))/q
 gap=float(np.max(abs(H-Clt[0])))
 print('smooth control',dict(C=float(np.max(abs(C))),H=float(np.max(abs(H))),
  Ct0=float(np.max(abs(Clt[0]))),pointwise_gap=gap,
  Ct_spatial=float(np.max(abs(Clt[1:]))),ADM=gr.adm(y)),flush=True)
 assert gap<2e-12 and np.max(abs(H))>.03 and np.max(abs(Clt[1:]))<1e-12

if __name__=='__main__':
 rows=[evaluate(N) for N in (16,24,32)]
 assert all(.20<r['Ct_lower0']/r['H']<.30 for r in rows)
 control()
 print('PASS smooth continuum identity control; NEGATIVE constrained native-grid equality not resolved')
