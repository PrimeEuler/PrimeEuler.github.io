#!/usr/bin/env python3
"""v15.1478: exact numerical 4D metric-jet test of nonlinear
GH reduced Ricci principal Hessian: R_mn - nabla_(m Gamma_n)
= -1/2 g^ab g_mn,ab + lower-order metric first derivatives.
"""
import numpy as np
def one(seed,hseed):
 rng=np.random.default_rng(seed)
 metric=np.diag([-1.,1.,1.,1.])
 a=rng.normal(size=(4,4));metric+=.04*(a+a.T)/2
 inv=np.linalg.inv(metric)
 d=rng.normal(size=(4,4,4))*.025
 d=(d+d.transpose(0,2,1))/2
 dd=np.random.default_rng(hseed).normal(size=(4,4,4,4))*.015
 dd=(dd+dd.transpose(1,0,2,3))/2
 dd=(dd+dd.transpose(0,1,3,2))/2
 dinv=-np.einsum('ip,apq,qj->aij',inv,d,inv)
 Gamma=np.zeros((4,4,4));dGamma=np.zeros((4,4,4,4))
 for r in range(4):
  for m in range(4):
   for n in range(4):
    for l in range(4):
     br=d[m,l,n]+d[n,l,m]-d[l,m,n]
     Gamma[r,m,n]+=.5*inv[r,l]*br
     for h in range(4):
      dGamma[h,r,m,n]+=.5*(dinv[h,r,l]*br+
          inv[r,l]*(dd[h,m,l,n]+dd[h,n,l,m]-dd[h,l,m,n]))
 Ric=np.zeros((4,4))
 for m in range(4):
  for n in range(4):
   for r in range(4):
    Ric[m,n]+=dGamma[r,r,m,n]-dGamma[n,r,m,r]
    for l in range(4):
     Ric[m,n]+=Gamma[r,m,n]*Gamma[l,r,l]-Gamma[r,m,l]*Gamma[l,n,r]
 C=np.einsum('mn,rmn->r',inv,Gamma);Cl=metric@C
 dCl=np.zeros((4,4))
 for h in range(4):
  for n in range(4):
   for r in range(4):
    dCl[h,n]+=d[h,n,r]*C[r]
    for m in range(4):
     for q in range(4):
      dCl[h,n]+=metric[n,r]*(dinv[h,m,q]*Gamma[r,m,q]+inv[m,q]*dGamma[h,r,m,q])
 covC=np.zeros((4,4))
 for m in range(4):
  for n in range(4):
   covC[m,n]=dCl[m,n]-np.dot(Gamma[:,m,n],Cl)
 reduced=Ric-.5*(covC+covC.T)
 hessian=np.einsum('ab,abij->ij',inv,dd)
 return reduced+.5*hessian,Ric,hessian
if __name__=='__main__':
 for seed in (1,7,55):
  vals=[one(seed,j) for j in (2,4,9,17)]
  err=max(float(np.max(abs(t[0]-vals[0][0]))) for t in vals)
  changed=max(float(np.max(abs(t[1]-vals[0][1]))) for t in vals)
  print('metric seed',seed,'GH Hessian cancellation',err,
        'Ricci Hessian sensitivity',changed)
  assert err<2e-15 and changed>1e-3
 print('PASS full nonlinear GH reduced Ricci has wave principal Hessian')
 print('OPEN numerical 3D GH evolution, subsidiary constraint and full Weyl-Maxwell EFT')
