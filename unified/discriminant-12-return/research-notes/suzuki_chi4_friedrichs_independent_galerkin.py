#!/usr/bin/env python3
"""Independent Friedrichs Galerkin solve for the chi_-4 Fredholm deficiency problem.

Unlike v13.621, this does NOT project a breakpoint solution.  It assembles
Galerkin matrices directly in endpoint-adapted parity bases by tensor
Gauss-Legendre quadrature, solves the even/odd first-kind equations with the
constant/linear nuisance terms included, and compares the resulting projective
characteristic against the breakpoint-aware control at the same finite lambda.

Basis on [0,A]:
 e_n=sqrt(2/A) cos((n+1/2)pi x/A),  e_n(A)=0
 o_n=sqrt(2/A) sin((n+1)pi x/A),    o_n(0)=o_n(A)=0

The augmented Galerkin equations are
  <e_m,-K_e q_e> - B <e_m,1> = <e_m,cosh>,
  <o_m,-K_o q_o> - C <o_m,x> = <o_m,sinh>.
The nuisance scalars are determined by one extra weighted residual condition:
the residual is orthogonal to 1 in the even sector and x in the odd sector.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("pb",HERE/"suzuki_chi4_phase_and_breakpoint_comparison.py")
pb=importlib.util.module_from_spec(s); s.loader.exec_module(pb)


def basis(A,N,x,p):
    x=np.asarray(x); n=np.arange(N)
    if p=="e": return np.sqrt(2/A)*np.cos(np.pi*np.outer(x,n+.5)/A)
    return np.sqrt(2/A)*np.sin(np.pi*np.outer(x,n+1.)/A)


def assemble(A,lam,N,q=120):
    gx,gw=leggauss(q); x=.5*A*(gx+1); w=.5*A*gw
    E=basis(A,N,x,"e"); O=basis(A,N,x,"o")
    Ke=np.empty((q,q)); Ko=np.empty((q,q))
    for i,xx in enumerate(x):
        for k,yy in enumerate(x):
            kp=pb.ck.g_chi4(float(xx-yy))-lam*pb.Nker(A,xx,yy)
            km=pb.ck.g_chi4(float(xx+yy))-lam*pb.Nker(A,xx,-yy)
            Ke[i,k]=kp+km; Ko[i,k]=kp-km
    W=np.diag(w)
    Ae=-(E.T@W@Ke@W@E); Ao=-(O.T@W@Ko@W@O)
    one=np.ones(q); xx=x
    be1=E.T@(w*one); bx=O.T@(w*xx)
    fe=E.T@(w*np.cosh(x)); fo=O.T@(w*np.sinh(x))

    # N Galerkin rows + one nuisance-test row; unknowns are N coeffs + scalar.
    Me=np.zeros((N+1,N+1)); re=np.zeros(N+1)
    Me[:N,:N]=Ae; Me[:N,N]=-be1; re[:N]=fe
    # residual tested against 1: <1,-Ke q>-B<1,1>=<1,cosh>
    Me[N,:N]=-(one*w)@Ke@W@E; Me[N,N]=-np.sum(w); re[N]=np.sum(w*np.cosh(x))

    Mo=np.zeros((N+1,N+1)); ro=np.zeros(N+1)
    Mo[:N,:N]=Ao; Mo[:N,N]=-bx; ro[:N]=fo
    # residual tested against x.
    Mo[N,:N]=-(xx*w)@Ko@W@O; Mo[N,N]=-np.sum(w*xx*xx); ro[N]=np.sum(w*xx*np.sinh(x))

    ue=np.linalg.solve(Me,re); uo=np.linalg.solve(Mo,ro)
    return dict(A=A,lam=lam,ce=ue[:N],co=uo[:N],B=ue[N],C=uo[N],
                cond_e=np.linalg.cond(Me),cond_o=np.linalg.cond(Mo),
                res_e=np.linalg.norm(Me@ue-re,np.inf),res_o=np.linalg.norm(Mo@uo-ro,np.inf))


def characteristic(s,z,theta=np.pi,q=240):
    gx,gw=leggauss(q); x=.5*s["A"]*(gx+1); w=.5*s["A"]*gw
    qe=basis(s["A"],len(s["ce"]),x,"e")@s["ce"]
    qo=basis(s["A"],len(s["co"]),x,"o")@s["co"]
    Fp=2*np.sum(w*(qe*np.cos(z*x)+1j*qo*np.sin(z*x)))
    Fm=2*np.sum(w*(qe*np.cos(z*x)-1j*qo*np.sin(z*x)))
    return (z-1j)*Fp+np.exp(1j*theta)*(z+1j)*Fm


def run(A,Ns=(4,6,8,10,12,16),q=120):
    zd=pb.fc.deficiency_data(20,A); theta,_,_=pb.derived_theta(zd)
    bp=pb.solve_breakpoint(A,zd["lam"],14,12)
    b0=pb.bp_char(bp,.5,theta)
    print(f"A={A} lambda={zd['lam']:.12g} BPcond=({bp['cond_e']:.3e},{bp['cond_o']:.3e})")
    for N in Ns:
        g=assemble(A,zd["lam"],N,q); g0=characteristic(g,.5,theta)
        diffs=[abs(characteristic(g,z,theta)/g0-pb.bp_char(bp,z,theta)/b0) for z in (1.,3.,6.,10.)]
        print(f"N={N:2d} cond=({g['cond_e']:.3e},{g['cond_o']:.3e}) res=({g['res_e']:.2e},{g['res_o']:.2e}) "
              f"maxdiff={max(diffs):.6e} diffs="+" ".join(f"{d:.6e}" for d in diffs))


if __name__=="__main__":
    for A in (1.5,2.,2.5): run(A)
