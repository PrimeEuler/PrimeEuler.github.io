#!/usr/bin/env python3
"""Direct zero-branch sweep for the independent chi_-4 Friedrichs Galerkin characteristic.

Refines both Galerkin dimension N and assembly quadrature q for A=1.5,2,2.5.
Roots are zeros of the real scalar -i W(pi;z), bracketed on a dense real grid.
Reports ordered positive roots and compares cross-A drift.  This tests whether
the 1/A-like box spectrum seen in the discarded bare-Jz nodal construction
survives the domain-faithful Galerkin repair.

Guardrail: this tests the frozen chi_-4 screw kernel and finite lambda only.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("ig",HERE/"suzuki_chi4_friedrichs_independent_galerkin.py")
ig=importlib.util.module_from_spec(s); s.loader.exec_module(ig)
pb=ig.pb

def roots(g,theta=np.pi,zmax=35.0,step=.02,nroots=10):
    def f(z): return float(np.real(-1j*ig.characteristic(g,z,theta)))
    zs=np.arange(1e-5,zmax+step,step); vals=np.array([f(z) for z in zs])
    rr=[]
    for a,b,fa,fb in zip(zs[:-1],zs[1:],vals[:-1],vals[1:]):
        if not np.isfinite(fa+fb): continue
        if fa==0 or fa*fb<0:
            r=a if fa==0 else brentq(f,a,b,xtol=1e-12,rtol=1e-12)
            if not rr or abs(r-rr[-1])>1e-7: rr.append(r)
            if len(rr)>=nroots: break
    return np.array(rr)

def run():
    Ns=(8,12,16); qs=(80,120,160)
    allr={}
    for A in (1.5,2.,2.5):
        zd=pb.fc.deficiency_data(20,A); theta,_,_=pb.derived_theta(zd)
        print(f"A={A} lambda={zd['lam']:.12g}")
        for N in Ns:
            for q in qs:
                g=ig.assemble(A,zd["lam"],N,q)
                r=roots(g,theta)
                allr[A,N,q]=r
                print(f"N={N:2d} q={q:3d} roots "+" ".join(f"{x:.9f}" for x in r))
    print("\nCross-A finest-grid roots (N=16,q=160):")
    for A in (1.5,2.,2.5): print(A,allr[A,16,160])
    for k in range(10):
        vals=np.array([allr[A,16,160][k] for A in (1.5,2.,2.5)])
        print(f"k={k+1:2d} range={np.ptp(vals):.6e} relrange={np.ptp(vals)/np.mean(vals):.6e}")
    print("\nRefinement max root shifts q120->160 at N=16:")
    for A in (1.5,2.,2.5):
        a=allr[A,16,120];b=allr[A,16,160]
        print(A,np.max(abs(a-b)))
    print("Refinement max root shifts N12->16 at q160:")
    for A in (1.5,2.,2.5):
        a=allr[A,12,160];b=allr[A,16,160]
        print(A,np.max(abs(a-b)))

if __name__=="__main__": run()
