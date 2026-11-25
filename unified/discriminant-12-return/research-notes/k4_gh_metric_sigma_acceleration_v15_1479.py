#!/usr/bin/env python3
"""v15.1479: actual nonlinear 3+1 GH time-acceleration RHS on exact,
inhomogeneous Einstein-H2 + Weyl pp-wave at Cartesian sample points.
Recomputes lower-order GH terms by an independent ZERO-HESSIAN jet,
then solves for g_tt and scalar_tt and compares to exact derivatives.
NOT a freely time-stepped 3D PDE solver.
"""
import numpy as np
import sympy as s
T,Z,X,Y=s.symbols("T Z X Y",real=True);coords=(T,Z,X,Y)
kap=s.Rational(3,1000);a=s.Rational(3,25);eps=s.Rational(1,50)
w=T-Z;f=a*s.sin(w);fp=s.diff(f,w) if False else a*s.cos(w)
HH=-kap*fp**2*(X**2+Y**2)/2+eps*s.cos(w)*(X**2-Y**2)
ell=s.Matrix([1,-1,0,0]);eta=s.diag(-1,1,1,1)
g=eta+HH*ell*ell.T;inv=eta-HH*(eta*ell)*(eta*ell).T
assert s.simplify(g*inv-s.eye(4))==s.zeros(4)
phi=s.Matrix([s.sinh(f),0])
arrays=[g,inv,
 [s.diff(g[i,j],coords[h]) for h in range(4) for i in range(4) for j in range(4)],
 [s.diff(g[i,j],coords[h],coords[q]) for h in range(4) for q in range(4) for i in range(4) for j in range(4)],
 phi,
 [s.diff(phi[i],coords[h]) for i in range(2) for h in range(4)],
 [s.diff(phi[i],coords[h],coords[q]) for i in range(2) for h in range(4) for q in range(4)]]
fn=[s.lambdify(coords,array,"numpy") for array in arrays]
def point(p):
 m,mi,d,dd,ph,dp,ddp=[np.asarray(fun(*p),float) for fun in fn]
 d=d.reshape(4,4,4);dd=dd.reshape(4,4,4,4)
 ph=ph.reshape(2);dp=dp.reshape(2,4);ddp=ddp.reshape(2,4,4)
 di=-np.einsum("ip,apq,qj->aij",mi,d,mi)
 Gamma=np.zeros((4,4,4));D=np.zeros((4,4,4,4))
 D0=np.zeros_like(D)
 for r in range(4):
  for i in range(4):
   for j in range(4):
    for l in range(4):
     base=d[i,l,j]+d[j,l,i]-d[l,i,j]
     Gamma[r,i,j]+=.5*mi[r,l]*base
     for h in range(4):
      D0[h,r,i,j]+=.5*di[h,r,l]*base
      D[h,r,i,j]+=.5*(di[h,r,l]*base+mi[r,l]*(dd[h,i,l,j]+dd[h,j,l,i]-dd[h,l,i,j]))
 C=np.einsum("ij,rij->r",mi,Gamma);Cl=m@C
 def ricci(dG):
  R=np.zeros((4,4))
  for i in range(4):
   for j in range(4):
    for r in range(4):
     R[i,j]+=dG[r,r,i,j]-dG[j,r,i,r]
     for l in range(4):
      R[i,j]+=Gamma[r,i,j]*Gamma[l,r,l]-Gamma[r,i,l]*Gamma[l,j,r]
  return R
 R=ricci(D)
 dCl=np.zeros((4,4))
 for h in range(4):
  for n in range(4):
   for r in range(4):
    dCl[h,n]+=d[h,n,r]*C[r]
    for i in range(4):
     for j in range(4):
      dCl[h,n]+=m[n,r]*(di[h,i,j]*Gamma[r,i,j]+mi[i,j]*D0[h,r,i,j])
 cov=np.array([[dCl[i,j]-np.dot(Gamma[:,i,j],Cl) for j in range(4)] for i in range(4)])
 Q=ricci(D0)-.5*(cov+cov.T)
 metric_target=np.array([[1/(1+ph[0]**2),0],[0,1.]])
 stress=np.einsum("AB,Ai,Bj->ij",metric_target,dp,dp)
 # reduced Ricci is -g^{mn}g_ij,mn/2 + Q, so solve g_ij,tt
 P=np.zeros((4,4))
 for i in range(4):
  for j in range(4):
   cross=sum(2*mi[0,k]*dd[0,k,i,j] for k in (1,2,3))
   spatial=sum(mi[k,l]*dd[k,l,i,j] for k in (1,2,3) for l in (1,2,3))
   P[i,j]=(2*(Q[i,j]-float(kap)*stress[i,j])-cross-spatial)/mi[0,0]
 target_gradient=float(np.einsum("AB,Ai,Bj,ij->",metric_target,dp,dp,mi))
 Pphi=np.zeros(2)
 for A in range(2):
  cross=sum(2*mi[0,k]*ddp[A,0,k] for k in (1,2,3))
  spatial=sum(mi[k,l]*ddp[A,k,l] for k in (1,2,3) for l in (1,2,3))
  Pphi[A]=(ph[A]*target_gradient+np.dot(C,dp[A])-cross-spatial)/mi[0,0]
 result=(float(np.max(abs(P-dd[0,0]))),
   float(np.max(abs(Pphi-ddp[:,0,0]))),
   float(np.max(abs(R-float(kap)*stress))),
   float(np.max(abs(C))),
   float(np.max(abs(dd[0,0]))))
 print("point",p,"error metric_tt,sigma_tt,Ricci,GH,accel",result,flush=True)
 assert max(result[:4])<2e-12 and result[4]>1e-4
 return result
if __name__=="__main__":
 for p in [(0,.15,.2,-.4),(.4,-.2,-.7,.3),(1.1,.4,.5,.6),(2.2,.1,-.2,.8)]:point(p)
 print("PASS full nonlinear GH+H2 wave RHS accelerations versus exact 4D spacetime")
 print("OPEN unrestricted 3D generalized-harmonic time evolution")
