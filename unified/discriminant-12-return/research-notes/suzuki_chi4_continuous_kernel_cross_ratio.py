#!/usr/bin/env python3
"""Finite chi_-4 Suzuki W0/Wpi cross-ratio from fixed deficiency solves.

Implements ledger v13.685 on the existing compressed continuous-kernel
prototype.  This is a finite-a internal identity/regression test, NOT an
a->infinity theorem and NOT a beta-zero computation.

The weighted nodal representation solves the two fixed sources exp(+x) and
exp(-x).  Reflection supplies an independent check.  Once vp,vm are known,
all z-dependence is in cheap Fourier/source pairings.

Audited identities:
  W0  = (z-i)F_+(z) + (z+i)F_-(z)
  Wpi = (z-i)F_+(z) - (z+i)F_-(z)
  m   = -i W0/Wpi
  Delta(z,z*) = [W0(z)Wpi(z*)]/[Wpi(z)W0(z*)]
              = m(z)/m(z*).

The script checks:
  - solved vm against reflected vp;
  - reflected vp residual in the same reduced S system;
  - direct A/B cross-ratio against the W quotient;
  - W quotient against m(z)/m(z*);
  - base-point cocycle Delta(z,z1)Delta(z1,z2)=Delta(z,z2).
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location(
    "fc",HERE/"suzuki_chi4_zeeman_finite_characteristic.py")
fc=importlib.util.module_from_spec(sp); sp.loader.exec_module(fc)


def amplitudes(d,z,vm=None):
    """Return F_+,F_- in the weighted nodal representation."""
    if vm is None: vm=d["vm"]
    Fp=fc.fourier(d["vp"],d["x"],d["w"],z)
    Fm=fc.fourier(vm,d["x"],d["w"],z)
    return Fp,Fm


def AB(d,z,vm=None):
    Fp,Fm=amplitudes(d,z,vm)
    return (z-1j)*Fp,(z+1j)*Fm


def Wpair(d,z,vm=None):
    A,B=AB(d,z,vm)
    return A+B,A-B


def weyl(d,z,vm=None):
    W0,Wpi=Wpair(d,z,vm)
    return -1j*W0/Wpi


def delta_direct(d,z,zstar,vm=None):
    A,B=AB(d,z,vm); As,Bs=AB(d,zstar,vm)
    return ((A+B)/(A-B))*((As-Bs)/(As+Bs))


def delta_W(d,z,zstar,vm=None):
    W0,Wpi=Wpair(d,z,vm); W0s,Wpis=Wpair(d,zstar,vm)
    return W0*Wpis/(Wpi*W0s)


def delta_m(d,z,zstar,vm=None):
    return weyl(d,z,vm)/weyl(d,zstar,vm)


def reduced_system(d):
    B=d["B"]
    return B.T@(d["G"]-d["lam"]*d["K"])@B


def reflection_audit(d):
    """Compare independently solved vm with reflected vp and test residual."""
    vmR=d["vp"][::-1].copy()
    relvec=np.linalg.norm(d["vm"]-vmR)/max(np.linalg.norm(d["vm"]),1e-300)
    Sr=reduced_system(d)
    # Rebuild the reduced minus source exactly as deficiency_data does.
    fm=d["P"]@(np.sqrt(d["w"])*np.exp(-d["x"]))
    rhs=d["B"].T@fm
    cR=d["B"].T@vmR
    relres=np.linalg.norm(Sr@cR-rhs)/max(np.linalg.norm(rhs),1e-300)
    return vmR,relvec,relres


def relerr(a,b):
    return abs(a-b)/max(abs(a),abs(b),1e-300)


def audit(two_j=20,A=2.0,zstar=0.5+0.35j,
          zs=(0.25+0.2j,1.0+0.3j,3.0+0.4j,6.0+0.25j)):
    d=fc.deficiency_data(two_j,A)
    vmR,rvec,rres=reflection_audit(d)
    print(f"j={two_j/2:g} dim={two_j+1} A={A:g} lambda={d['lam']:.16g}")
    print(f"reflection vector relative error = {rvec:.3e}")
    print(f"reflection equation relative residual = {rres:.3e}")
    print("zstar =",zstar)
    worst=0.0
    for z in zs:
        dd=delta_direct(d,z,zstar,vmR)
        dw=delta_W(d,z,zstar,vmR)
        dm=delta_m(d,z,zstar,vmR)
        e1=relerr(dd,dw); e2=relerr(dw,dm); worst=max(worst,e1,e2)
        print(f"z={z!s:>12} Delta={dd.real:+.12e}{dd.imag:+.12e}j "
              f"err(direct,W)={e1:.3e} err(W,m)={e2:.3e}")
    # cocycle check with two distinct base points
    z=zs[-1]; z1=zstar; z2=0.75+0.55j
    lhs=delta_direct(d,z,z1,vmR)*delta_direct(d,z1,z2,vmR)
    rhs=delta_direct(d,z,z2,vmR)
    ec=relerr(lhs,rhs)
    print(f"cocycle relative error = {ec:.3e}")
    print(f"worst algebraic identity relative error = {worst:.3e}")
    return dict(reflection_vector_relerr=rvec,
                reflection_equation_relres=rres,
                cocycle_relerr=ec,identity_relerr=worst)


if __name__=="__main__":
    for A in (1.5,2.0,2.5):
        audit(A=A)
