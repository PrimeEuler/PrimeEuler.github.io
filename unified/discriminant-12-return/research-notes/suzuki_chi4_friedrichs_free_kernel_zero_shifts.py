#!/usr/bin/env python3
"""Free/endpoint versus chi_-4 kernel zero-shift dissection.

The full finite equation uses k=g_chi4-lambda*N.  Define the endpoint/free
control by deleting the arithmetic screw term g_chi4 while retaining exactly
the same interval, Friedrichs bases, nuisance rows, Neumann inverse term,
finite lambda, and characteristic construction:
    k_free = -lambda*N.
Then the kernel-dependent effect is quantified by ordered zero shifts
    delta r_k = r_k(full)-r_k(free).
This is an operational finite-A decomposition, not an additive decomposition
of zeros or of inverse operators.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("ig",HERE/"suzuki_chi4_friedrichs_independent_galerkin.py")
ig=importlib.util.module_from_spec(s); s.loader.exec_module(ig)
pb=ig.pb

def assemble(A,lam,N,q,include_kernel):
    gx,gw=leggauss(q);x=.5*A*(gx+1);w=.5*A*gw
    E=ig.basis(A,N,x,"e");O=ig.basis(A,N,x,"o")
    Ke=np.empty((q,q));Ko=np.empty((q,q))
    for i,xx in enumerate(x):
      for k,yy in enumerate(x):
        gp=pb.ck.g_chi4(float(xx-yy)) if include_kernel else 0.
        gm=pb.ck.g_chi4(float(xx+yy)) if include_kernel else 0.
        kp=gp-lam*pb.Nker(A,xx,yy); km=gm-lam*pb.Nker(A,xx,-yy)
        Ke[i,k]=kp+km;Ko[i,k]=kp-km
    WE=w[:,None]*E;WO=w[:,None]*O
    Ae=-(E.T@(w[:,None]*(Ke@WE)));Ao=-(O.T@(w[:,None]*(Ko@WO)))
    be=E.T@w;bx=O.T@(w*x);fe=E.T@(w*np.cosh(x));fo=O.T@(w*np.sinh(x))
    Me=np.zeros((N+1,N+1));re=np.zeros(N+1);Me[:N,:N]=Ae;Me[:N,N]=-be;re[:N]=fe
    Me[N,:N]=-(w@Ke)@WE;Me[N,N]=-w.sum();re[N]=np.sum(w*np.cosh(x))
    Mo=np.zeros((N+1,N+1));ro=np.zeros(N+1);Mo[:N,:N]=Ao;Mo[:N,N]=-bx;ro[:N]=fo
    Mo[N,:N]=-((w*x)@Ko)@WO;Mo[N,N]=-np.sum(w*x*x);ro[N]=np.sum(w*x*np.sinh(x))
    ue=np.linalg.solve(Me,re);uo=np.linalg.solve(Mo,ro)
    return dict(A=A,ce=ue[:N],co=uo[:N])

def roots(g,theta=np.pi,zmax=35,step=.02,nroots=10,qf=240):
    gx,gw=leggauss(qf);A=g["A"];x=.5*A*(gx+1);w=.5*A*gw
    qe=ig.basis(A,len(g["ce"]),x,"e")@g["ce"];qo=ig.basis(A,len(g["co"]),x,"o")@g["co"]
    def f(z):
      c=np.cos(z*x);s=np.sin(z*x)
      Fp=2*np.sum(w*(qe*c+1j*qo*s));Fm=2*np.sum(w*(qe*c-1j*qo*s))
      return float(np.real(-1j*((z-1j)*Fp+np.exp(1j*theta)*(z+1j)*Fm)))
    zs=np.arange(1e-6,zmax+step,step);vs=np.array([f(z) for z in zs]);rr=[]
    for i in range(len(zs)-1):
      if vs[i]*vs[i+1]<0:
        r=brentq(f,zs[i],zs[i+1],xtol=1e-12)
        if not rr or abs(r-rr[-1])>1e-7:rr.append(r)
        if len(rr)>=nroots:break
    return np.array(rr)

if __name__=="__main__":
  for A in (1.5,2.,2.5):
    zd=pb.fc.deficiency_data(20,A);theta,_,_=pb.derived_theta(zd)
    full=assemble(A,zd["lam"],16,160,True);free=assemble(A,zd["lam"],16,160,False)
    rf=roots(full,theta);r0=roots(free,theta);d=rf-r0
    print(f"A={A} lambda={zd['lam']:.12g}")
    for k,(a,b,c) in enumerate(zip(r0,rf,d),1):
      print(f"{k:2d} free={a:.9f} full={b:.9f} shift={c:+.9e} Ashift={A*c:+.9e}")
