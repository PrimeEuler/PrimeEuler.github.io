#!/usr/bin/env python3
"""Finite chi_-4 Suzuki deficiency/characteristic prototype on a Zeeman carrier.

Builds on suzuki_chi4_zeeman_kernel_compression.py.  The finite carrier is the
spin-j Jz grid.  The continuous Neumann inverse is sampled on the same nodes.
For a chosen lambda below the finite generalized spectrum, S=G-lambda K is
solved against projected e^{+x}, e^{-x} source vectors.  Their quadrature
Fourier transforms are inserted into the Section-7.8/Suzuki characteristic
combination

    W_j(theta;z) = (z-i) F_+(z) + exp(i theta)(z+i) F_-(z).

At theta=pi this is the finite object to compare, after scalar normalization,
with Xi_-4(z)/E_-4(z).  This script does NOT claim that its zeros are already
L(s,chi_-4) zeros; it is the first finite characteristic experiment.

Numerical guardrail: the historical v13.287 Ritz scale was superseded by
v13.288.  Therefore lambda is chosen relative to the ACTUAL finite generalized
spectrum of each compressed pair, with an explicit margin, not inherited from
the stale lambda=-5 discussion.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import numpy as np
from scipy.linalg import eigh

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "chi4kernel", HERE / "suzuki_chi4_zeeman_kernel_compression.py")
ck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ck)


def neumann_kernel(x: float, y: float, A: float) -> float:
    return (x*x+y*y)/(4*A) - abs(x-y)/2 + A/6


def mean_zero_projector(w: np.ndarray) -> np.ndarray:
    """Euclidean projector corresponding to quadrature-weighted constants."""
    q = np.sqrt(w)
    q = q / np.linalg.norm(q)
    return np.eye(len(w)) - np.outer(q, q)


def compressed_pair(two_j: int, A: float = 2.0):
    x, w, Jz, Jx, G = ck.compress_kernel(two_j, A)
    K = np.empty_like(G)
    for r, xr in enumerate(x):
        for s, ys in enumerate(x):
            K[r,s] = np.sqrt(w[r]*w[s])*neumann_kernel(float(xr),float(ys),A)
    P = mean_zero_projector(w)
    return x,w,Jz,Jx,P@G@P,P@K@P,P


def mean_zero_basis(w: np.ndarray) -> np.ndarray:
    q = np.sqrt(w)
    q /= np.linalg.norm(q)
    # eigenvectors of projector with eigenvalue one
    P = np.eye(len(w))-np.outer(q,q)
    vals, vecs = np.linalg.eigh(P)
    return vecs[:, vals > 0.5]


def generalized_spectrum(G,K,w):
    B=mean_zero_basis(w)
    Gr=B.T@G@B
    Kr=B.T@K@B
    kval=np.linalg.eigvalsh(Kr)
    if kval[0] <= 0:
        raise RuntimeError("compressed K is not positive on mean-zero space")
    return eigh(Gr,Kr,eigvals_only=True), B, Gr, Kr


def deficiency_data(two_j: int=12,A: float=2.0,margin: float=1.0):
    x,w,Jz,Jx,G,K,P=compressed_pair(two_j,A)
    ev,B,Gr,Kr=generalized_spectrum(G,K,w)
    lam=float(ev[0]-abs(margin))
    Sr=Gr-lam*Kr
    # Source vectors in the weighted nodal representation.
    fp=P@(np.sqrt(w)*np.exp(x))
    fm=P@(np.sqrt(w)*np.exp(-x))
    cp=np.linalg.solve(Sr,B.T@fp)
    cm=np.linalg.solve(Sr,B.T@fm)
    vp=B@cp
    vm=B@cm
    return dict(x=x,w=w,Jz=Jz,Jx=Jx,G=G,K=K,P=P,B=B,
                generalized_eigs=ev,lam=lam,vp=vp,vm=vm)


def fourier(v,x,w,z):
    # v already contains sqrt(w) nodal scaling, so use sqrt(w) once more.
    return np.sum(np.sqrt(w)*v*np.exp(1j*z*x))


def characteristic(data,z,theta=np.pi):
    Fp=fourier(data["vp"],data["x"],data["w"],z)
    Fm=fourier(data["vm"],data["x"],data["w"],z)
    return (z-1j)*Fp + np.exp(1j*theta)*(z+1j)*Fm


def audit(two_j=12,A=2.0):
    d=deficiency_data(two_j,A)
    ev=d["generalized_eigs"]
    print(f"j={two_j/2:g}, dim={two_j+1}, A={A:g}")
    print("finite generalized spectral bottom =",repr(float(ev[0])))
    print("chosen lambda =",repr(d["lam"]))
    print("lambda gap =",repr(float(ev[0]-d["lam"])))
    print("reflection deficiency residual =",
          np.linalg.norm(d["vm"]-d["vp"][::-1])/max(np.linalg.norm(d["vm"]),1e-300))
    for z in (0.0,1.0,5.0,10.0):
        print("W_pi",z,characteristic(d,z))


if __name__=="__main__":
    audit()
