#!/usr/bin/env python3
"""Homotopy continuation of chi_-4 Friedrichs characteristic zeros.

Tracks real zero branches while k_tau=tau*g_chi4-lambda*N_A, 0<=tau<=1.
At each tau, roots are found near the previous branch locations and matched
by minimum-distance assignment. Reports branch displacement, minimum
neighbor gaps, and any order exchanges/crossing warnings.

This resolves the ordered-root ambiguity in v13.629. It is numerical branch
continuation for the frozen finite-A kernel, not an arithmetic identification.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.optimize import linear_sum_assignment

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("fk",HERE/"suzuki_chi4_friedrichs_free_kernel_zero_shifts.py")
fk=importlib.util.module_from_spec(s); s.loader.exec_module(fk)
pb=fk.pb

def assemble_tau(A,lam,N,q,tau):
    # Same assembly as v13.629, but scale only the arithmetic screw term.
    gx,gw=leggauss(q);x=.5*A*(gx+1);w=.5*A*gw
    E=fk.ig.basis(A,N,x,"e");O=fk.ig.basis(A,N,x,"o")
    Ke=np.empty((q,q));Ko=np.empty((q,q))
    for i,xx in enumerate(x):
      for k,yy in enumerate(x):
        kp=tau*pb.ck.g_chi4(float(xx-yy))-lam*pb.Nker(A,xx,yy)
        km=tau*pb.ck.g_chi4(float(xx+yy))-lam*pb.Nker(A,xx,-yy)
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

def continue_A(A,N=16,q=160,taus=np.linspace(0,1,21),nr=10):
    zd=pb.fc.deficiency_data(20,A);theta,_,_=pb.derived_theta(zd)
    history=[]
    for tau in taus:
      g=assemble_tau(A,zd["lam"],N,q,tau)
      r=fk.roots(g,theta,nroots=nr)
      if len(r)!=nr: raise RuntimeError((A,tau,len(r)))
      if not history: tracked=r.copy()
      else:
        prev=history[-1][1]
        I,J=linear_sum_assignment(abs(prev[:,None]-r[None,:]))
        tracked=np.empty_like(prev);tracked[I]=r[J]
      history.append((tau,tracked))
    H=np.array([r for _,r in history])
    print(f"A={A} N={N} q={q}")
    for k in range(nr):
      print(f"{k+1:2d} r0={H[0,k]:.9f} r1={H[-1,k]:.9f} delta={H[-1,k]-H[0,k]:+.9e} "
            f"maxstep={np.max(abs(np.diff(H[:,k]))):.3e}")
    gaps=np.diff(np.sort(H,axis=1),axis=1)
    print("minimum adjacent gap over homotopy",np.min(gaps))
    print("order exchanges",sum(not np.all(np.diff(row)>0) for row in H))
    return H

if __name__=="__main__":
  for A in (1.5,2.,2.5): continue_A(A)
