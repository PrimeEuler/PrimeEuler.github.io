#!/usr/bin/env python3
"""Operator-level certification gate for chi_-4 Friedrichs Galerkin assembly.

Audits the independently assembled parity operators under quadrature refinement.
For each A,N,q it reports:
- augmented-system condition number and smallest singular value;
- relative Frobenius change of parity Galerkin operator blocks vs the finest q;
- inverse/resolvent change of the augmented systems vs the finest q;
- eigenvalue change of the symmetrized parity operator blocks vs finest q.

This is a discretization-stability audit of the frozen kernel, not a proof of
continuous operator convergence and not a beta-zero test.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("ig",HERE/"suzuki_chi4_friedrichs_independent_galerkin.py")
ig=importlib.util.module_from_spec(s); s.loader.exec_module(ig)
pb=ig.pb


def matrices(A,lam,N,q):
    gx,gw=leggauss(q); x=.5*A*(gx+1); w=.5*A*gw
    E=ig.basis(A,N,x,"e"); O=ig.basis(A,N,x,"o")
    Ke=np.empty((q,q)); Ko=np.empty((q,q))
    for i,xx in enumerate(x):
        for k,yy in enumerate(x):
            kp=pb.ck.g_chi4(float(xx-yy))-lam*pb.Nker(A,xx,yy)
            km=pb.ck.g_chi4(float(xx+yy))-lam*pb.Nker(A,xx,-yy)
            Ke[i,k]=kp+km; Ko[i,k]=kp-km
    WE=w[:,None]*E; WO=w[:,None]*O
    Ae=-(E.T@(w[:,None]*(Ke@WE)))
    Ao=-(O.T@(w[:,None]*(Ko@WO)))
    be1=E.T@w; bx=O.T@(w*x)
    Me=np.zeros((N+1,N+1)); Mo=np.zeros((N+1,N+1))
    Me[:N,:N]=Ae; Me[:N,N]=-be1
    Me[N,:N]=-(w@Ke)@WE; Me[N,N]=-w.sum()
    Mo[:N,:N]=Ao; Mo[:N,N]=-bx
    Mo[N,:N]=-((w*x)@Ko)@WO; Mo[N,N]=-np.sum(w*x*x)
    return Ae,Ao,Me,Mo


def relfro(X,Y): return np.linalg.norm(X-Y,"fro")/max(np.linalg.norm(Y,"fro"),1e-300)
def invrel(X,Y):
    IX=np.linalg.inv(X); IY=np.linalg.inv(Y)
    return np.linalg.norm(IX-IY,2)/max(np.linalg.norm(IY,2),1e-300)
def eigerr(X,Y):
    ex=np.linalg.eigvalsh((X+X.T)/2); ey=np.linalg.eigvalsh((Y+Y.T)/2)
    return np.max(np.abs(ex-ey))/max(np.max(np.abs(ey)),1e-300)


def run(A,N=12,qs=(40,60,80,120,160)):
    zd=pb.fc.deficiency_data(20,A); lam=zd["lam"]
    mats={q:matrices(A,lam,N,q) for q in qs}; ref=mats[qs[-1]]
    print(f"A={A} N={N} lambda={lam:.12g} qref={qs[-1]}")
    for q in qs:
        Ae,Ao,Me,Mo=mats[q]
        se=np.linalg.svd(Me,compute_uv=False); so=np.linalg.svd(Mo,compute_uv=False)
        print("q=%3d cond=(%.3e,%.3e) smin=(%.3e,%.3e) oprel=(%.3e,%.3e) invrel=(%.3e,%.3e) eigrel=(%.3e,%.3e)"%(
            q,se[0]/se[-1],so[0]/so[-1],se[-1],so[-1],
            relfro(Ae,ref[0]),relfro(Ao,ref[1]),
            invrel(Me,ref[2]),invrel(Mo,ref[3]),
            eigerr(Ae,ref[0]),eigerr(Ao,ref[1])))


if __name__=="__main__":
    for A in (1.5,2.,2.5):
        for N in (8,12,16): run(A,N)
