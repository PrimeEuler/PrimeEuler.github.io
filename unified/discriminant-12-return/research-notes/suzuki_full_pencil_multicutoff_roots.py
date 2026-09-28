#!/usr/bin/env python3
"""Multi-cutoff full generalized-pencil root diagnostic.

Diagnostic only.  For several parity cutoffs, solve

    A_N q = delta B_sm,N q

for the full parity pencil, count roots in |delta|<0.02, report the largest
imaginary part there, and compute the inertia of B_sm restricted to the
entire inner generalized invariant subspace.

The invariant-subspace B inertia is the meaningful Krein diagnostic.
Individual signatures for nearly coincident machine-zero eigenvectors are
not reported.
"""
from __future__ import annotations

import mpmath as mp
import numpy as np
from scipy.linalg import eig

from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    smooth_bulk,
)


CUTS=(96,192,384)
WINDOW=0.02


def to_numpy(M):
    return np.array(
        [[float(M[i,j]) for j in range(M.cols)] for i in range(M.rows)],
        dtype=float,
    )


def one(sector,N):
    with mp.workdps(60):
        ns,*_,full=parity_components(N,sector)
        A=to_numpy(full)
        B=to_numpy(smooth_bulk(ns))

    vals,V=eig(A,B,right=True)

    inner=np.abs(vals)<WINDOW
    vin=vals[inner]
    Win=V[:,inner]

    # Real/imag diagnostics for the whole enclosed finite cluster.
    real_count=int(np.sum(np.abs(vin.imag)<1e-8))
    max_imag=float(np.max(np.abs(vin.imag))) if len(vin) else float("nan")

    # The invariant subspace can be arbitrarily based when roots coalesce.
    # QR first, then inspect the restricted Hermitian bulk form.
    Q,_=np.linalg.qr(Win)
    G=Q.conj().T@B@Q
    G=(G+G.conj().T)/2
    ge=np.linalg.eigvalsh(G)
    nneg=int(np.sum(ge<-1e-10))
    nzero=int(np.sum(np.abs(ge)<=1e-10))
    npos=int(np.sum(ge>1e-10))

    ordered=vin[np.argsort(np.abs(vin))]

    return {
        "dimension":len(ns),
        "inner_count":len(vin),
        "real_count":real_count,
        "max_imag":max_imag,
        "inner_roots":ordered,
        "cluster_B_inertia":(nneg,nzero,npos),
        "cluster_B_eigs":ge,
    }


def main():
    for sector in ("even-v","odd-v"):
        print("\nSECTOR",sector)
        for N in CUTS:
            out=one(sector,N)
            print("\ncutoff",N,"dimension",out["dimension"])
            print("inner count",out["inner_count"])
            print("real count",out["real_count"])
            print("max |imag|",out["max_imag"])
            print("inner roots",out["inner_roots"])
            print("cluster B inertia (-,0,+)",out["cluster_B_inertia"])
            print("cluster B eigs",out["cluster_B_eigs"])

            assert out["inner_count"]==6
            assert out["real_count"]==6
            assert out["max_imag"]<1e-8
            assert out["cluster_B_inertia"]==(2,0,4)

    print("\nPASS multi-cutoff six-root diagnostic")
    print(
        "Guardrail: finite-section evidence only; exact six-root count "
        "requires the v13.836 six-dimensional winding/Riesz certificate."
    )


if __name__=="__main__":
    main()
