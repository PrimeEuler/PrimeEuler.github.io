#!/usr/bin/env python3
"""Independent Friedrichs-Galerkin W0/Wpi cross-ratio audit for chi_-4.

This ports the normalization-free observable of ledger v13.685 from the
Zeeman compressed carrier to the independently assembled endpoint-adapted
Friedrichs Galerkin discretization.

Important status:
- finite-a discretization comparison only;
- not a proof of continuous convergence;
- not a beta-zero computation;
- uses the augmented even/odd first-kind Galerkin equations already audited
  as a discretization diagnostic, so agreement with the Zeeman carrier is the
  gate of interest.

For the parity solution q_e,q_o on [0,A], reflection gives
  q_+ = q_e + q_o, q_- = q_e - q_o.
The full-interval Fourier amplitudes are
  F_+(z)=2 int_0^A [q_e cos(zx)+ i q_o sin(zx)] dx,
  F_-(z)=2 int_0^A [q_e cos(zx)- i q_o sin(zx)] dx.
Then W0,Wpi,m,Delta are formed exactly as in v13.685.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent

sg=importlib.util.spec_from_file_location(
    "ig",HERE/"suzuki_chi4_friedrichs_independent_galerkin.py")
ig=importlib.util.module_from_spec(sg); sg.loader.exec_module(ig)

sz=importlib.util.spec_from_file_location(
    "zc",HERE/"suzuki_chi4_continuous_kernel_cross_ratio.py")
zc=importlib.util.module_from_spec(sz); sz.loader.exec_module(zc)


def fg_amplitudes(sol,z,q=320):
    gx,gw=leggauss(q)
    x=.5*sol["A"]*(gx+1); w=.5*sol["A"]*gw
    qe=ig.basis(sol["A"],len(sol["ce"]),x,"e")@sol["ce"]
    qo=ig.basis(sol["A"],len(sol["co"]),x,"o")@sol["co"]
    C=np.cos(z*x); S=np.sin(z*x)
    Fp=2*np.sum(w*(qe*C+1j*qo*S))
    Fm=2*np.sum(w*(qe*C-1j*qo*S))
    return Fp,Fm


def AB(sol,z,q=320):
    Fp,Fm=fg_amplitudes(sol,z,q)
    return (z-1j)*Fp,(z+1j)*Fm


def Wpair(sol,z,q=320):
    a,b=AB(sol,z,q)
    return a+b,a-b


def weyl(sol,z,q=320):
    W0,Wpi=Wpair(sol,z,q)
    return -1j*W0/Wpi


def delta(sol,z,zstar,q=320):
    a,b=AB(sol,z,q); c,d=AB(sol,zstar,q)
    return ((a+b)/(a-b))*((c-d)/(c+d))


def relerr(a,b):
    return abs(a-b)/max(abs(a),abs(b),1e-300)


def run(A=2.0,Ns=(8,12,16,20),qasm=160,qeval=320,
        two_j=20,zstar=.5+.35j,
        zs=(.25+.2j,1+.3j,3+.4j,6+.25j)):
    # Freeze lambda to the same existing Zeeman finite-pair rule so the two
    # discretizations compare the same kernel pencil at the same finite lambda.
    zd=ig.pb.fc.deficiency_data(two_j,A)
    lam=zd["lam"]
    zdata=zc.fc.deficiency_data(two_j,A)

    print(f"A={A:g} lambda={lam:.16g} Zeeman_dim={two_j+1}")
    prev=None
    for N in Ns:
        sol=ig.assemble(A,lam,N,qasm)
        vals=[delta(sol,z,zstar,qeval) for z in zs]
        # Internal identity: Delta=m/mstar in the FG representation.
        ierr=max(relerr(vals[k],weyl(sol,zs[k],qeval)/weyl(sol,zstar,qeval))
                 for k in range(len(zs)))
        # N-refinement of the observable.
        nerr=float("nan") if prev is None else max(relerr(vals[k],prev[k])
                                                  for k in range(len(zs)))
        prev=vals
        print(f"N={N:2d} cond=({sol['cond_e']:.3e},{sol['cond_o']:.3e}) "
              f"res=({sol['res_e']:.2e},{sol['res_o']:.2e}) "
              f"identity={ierr:.3e} Nchange={nerr:.3e}")
        for z,v in zip(zs,vals):
            print(f"  z={z!s:>12} Delta_FG={v.real:+.10e}{v.imag:+.10e}j")

    # Cross-discretization comparison is deliberately reported, not asserted.
    fg=prev
    zz=[zc.delta_direct(zdata,z,zstar,zdata["vp"][::-1]) for z in zs]
    cerr=max(relerr(fg[k],zz[k]) for k in range(len(zs)))
    print(f"max relative FG(N={Ns[-1]}) vs Zeeman cross-ratio difference = {cerr:.6e}")
    for z,a,b in zip(zs,fg,zz):
        print(f"  z={z!s:>12} FG={a.real:+.8e}{a.imag:+.8e}j "
              f"Zeeman={b.real:+.8e}{b.imag:+.8e}j rel={relerr(a,b):.3e}")


if __name__=="__main__":
    for A in (1.5,2.0,2.5):
        run(A=A)
