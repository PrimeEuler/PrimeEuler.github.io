#!/usr/bin/env python3
"""Friedrichs-adapted parity Galerkin carrier and unitary SU(2) transport test.

This gate deliberately separates two questions.

(1) Can the source-faithful breakpoint Fredholm deficiency solution be represented
in a basis that exactly satisfies the finite endpoint/domain conditions?
(2) After such a finite coefficient space is obtained, does unitary transport to
a spin-j carrier alter the characteristic?

On [0,A] use the orthonormal Friedrichs-adapted basis
  even: sqrt(2/A) cos((n+1/2) pi x/A), n=0,...,N-1,
  odd : sqrt(2/A) sin((n+1) pi x/A),   n=0,...,N-1.
Every basis function vanishes at x=A; the odd basis also vanishes at x=0.
Thus q_e(A)=0 and q_o(0)=q_o(A)=0 hold identically, not by a sampled penalty.

The breakpoint-aware solution from v13.614 is projected in L2 onto these spaces.
Its projective characteristic is compared with the original breakpoint object.
Then the 2N coefficient vector is transported by an explicit unitary matrix to
the standard spin j=(2N-1)/2 Zeeman space. Sources/observables are transported
covariantly. Characteristic invariance under that transport is an algebraic
identity and is checked numerically.

This does NOT claim that bare Jz nodes are valid quadrature nodes; indeed the
purpose is to retain SU(2) only as a unitarily equivalent finite carrier.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("pb",HERE/"suzuki_chi4_phase_and_breakpoint_comparison.py")
pb=importlib.util.module_from_spec(s); s.loader.exec_module(pb)


def basis(A,N,x,parity):
    x=np.asarray(x,float)
    n=np.arange(N)
    if parity=="even":
        return np.sqrt(2/A)*np.cos(np.pi*np.outer(x,n+.5)/A)
    if parity=="odd":
        return np.sqrt(2/A)*np.sin(np.pi*np.outer(x,n+1.)/A)
    raise ValueError


def project_breakpoint(sol,N,qorder=240):
    gx,gw=leggauss(qorder); x=.5*sol["A"]*(gx+1); w=.5*sol["A"]*gw
    L=pb.Lvals(sol["nodes"],sol["bary"],x)
    qe=L@sol["qe"]; qo=L@sol["qo"]
    Ee=basis(sol["A"],N,x,"even"); Eo=basis(sol["A"],N,x,"odd")
    ce=Ee.T@(w*qe); co=Eo.T@(w*qo)
    return ce,co


def gal_char(A,ce,co,z,theta=np.pi,qorder=240):
    gx,gw=leggauss(qorder); x=.5*A*(gx+1); w=.5*A*gw
    qe=basis(A,len(ce),x,"even")@ce; qo=basis(A,len(co),x,"odd")@co
    Fp=2*np.sum(w*(qe*np.cos(z*x)+1j*qo*np.sin(z*x)))
    Fm=2*np.sum(w*(qe*np.cos(z*x)-1j*qo*np.sin(z*x)))
    return (z-1j)*Fp+np.exp(1j*theta)*(z+1j)*Fm


def zeeman_unitary(N):
    # Columns define a deterministic orthonormal carrier basis in C^(2N).
    # DFT is chosen only to make the transport nontrivial; any unitary gives
    # the same covariantly transported characteristic.
    d=2*N
    r=np.arange(d)[:,None]; c=np.arange(d)[None,:]
    U=np.exp(2j*np.pi*r*c/d)/np.sqrt(d)
    j=(d-1)/2
    m=np.arange(d)-j
    Jz=np.diag(m)
    Jx=np.zeros((d,d),complex)
    for k,mm in enumerate(m[:-1]):
        Jx[k,k+1]=Jx[k+1,k]=.5*np.sqrt((j-mm)*(j+mm+1))
    return U,Jz,Jx


def transport_check(A,ce,co,zgrid=(.5,1.,3.,6.,10.)):
    c=np.r_[ce,co].astype(complex); U,Jz,Jx=zeeman_unitary(len(ce)); psi=U@c
    # Build the characteristic as a linear functional l(z)^* c by evaluating
    # each coefficient basis vector once. Transport l covariantly: l_Z=U l.
    errs=[]
    for z in zgrid:
        vals=[]
        for k in range(len(c)):
            e=np.zeros_like(c);e[k]=1
            vals.append(gal_char(A,e[:len(ce)].real,e[len(ce):].real,z))
        # gal_char = sum vals[k] c[k]; use bilinear row form.
        row=np.asarray(vals,complex)
        direct=row@c
        transported=(row@U.conj().T)@psi
        errs.append(abs(direct-transported))
    cas=Jx@Jx+Jz@Jz
    # Complete Jy for Casimir audit.
    Jy=np.zeros_like(Jx)
    for k in range(2*len(ce)-1):
        y=2*Jx[k,k+1]; Jy[k,k+1]=-0.5j*y; Jy[k+1,k]=0.5j*y
    j=(2*len(ce)-1)/2
    caserr=np.linalg.norm(Jx@Jx+Jy@Jy+Jz@Jz-j*(j+1)*np.eye(2*len(ce)),np.inf)
    return max(errs),caserr


def run(A=2.,two_j_bp=20,degree=14,qorder=12,Ns=(2,4,6,8,10,12,16)):
    zd=pb.fc.deficiency_data(two_j_bp,A); theta,alpha,rres=pb.derived_theta(zd)
    sol=pb.solve_breakpoint(A,zd["lam"],degree,qorder)
    zref=.5; zgrid=(1.,3.,6.,10.)
    base0=pb.bp_char(sol,zref,theta)
    print(f"A={A} lambda={zd['lam']:.12g} BP degree={degree} q={qorder}")
    print(f"BP cond=({sol['cond_e']:.6e},{sol['cond_o']:.6e}) res=({sol['res_e']:.3e},{sol['res_o']:.3e})")
    for N in Ns:
        ce,co=project_breakpoint(sol,N)
        g0=gal_char(A,ce,co,zref,theta)
        diffs=[abs(gal_char(A,ce,co,z,theta)/g0-pb.bp_char(sol,z,theta)/base0) for z in zgrid]
        terr,caserr=transport_check(A,ce,co)
        print(f"N={N:2d} spin={(2*N-1)/2:4.1f} max_projective_diff={max(diffs):.6e} diffs="+
              " ".join(f"{x:.6e}" for x in diffs)+
              f" transport_err={terr:.3e} casimir_err={caserr:.3e}")


if __name__=="__main__":
    for A in (1.5,2.,2.5): run(A)
