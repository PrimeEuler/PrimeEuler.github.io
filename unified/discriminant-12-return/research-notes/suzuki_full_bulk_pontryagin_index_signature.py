#!/usr/bin/env python3
"""Full smooth-bulk Pontryagin index and finite generalized-signature diagnostic.

The certified parity tail smooth bulk is positive:
    B_T > beta I.

Restoring the first two parity modes gives
    B_sm = [[B_CC, B_CT],[B_TC,B_T]].

The 2x2 core block B_CC is already strictly negative definite.  Therefore
the exact Schur complement
    S_B = B_CC - B_CT B_T^{-1} B_TC
is even more negative, and block congruence gives exact Pontryagin index 2
for the full smooth bulk.

The second half is an N=96 diagnostic only.  It verifies that the six
near-zero generalized Ritz roots span a subspace on which B_sm has inertia
(2 negative, 4 positive), while the endpoint inertia difference is 2.
This illustrates why the positive-tail inertia count cannot be copied
unchanged to the full indefinite pencil.
"""
from __future__ import annotations

import math
import mpmath as mp
import numpy as np
from scipy.linalg import eig

from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    smooth_bulk,
)


def to_numpy(M):
    return np.array(
        [[float(M[i,j]) for j in range(M.cols)] for i in range(M.rows)],
        dtype=float,
    )


def exact_core_block_intervals(sector):
    iv=mp.iv
    iv.dps=80

    if sector=="even-v":
        m1,m2=iv.mpf(1),iv.mpf(3)
    elif sector=="odd-v":
        m1,m2=iv.mpf(2),iv.mpf(4)
    else:
        raise ValueError(sector)

    a=iv.log(m1/4)-1/(2*m1)
    d=iv.log(m2/4)-1/(2*m2)
    b=-1/(m1+m2)
    det=a*d-b*b
    tr=a+d

    if not a < 0:
        raise RuntimeError(("core a not negative",sector,a))
    if not d < 0:
        raise RuntimeError(("core d not negative",sector,d))
    if not det > 0:
        raise RuntimeError(("core determinant not positive",sector,det))
    if not tr < 0:
        raise RuntimeError(("core trace not negative",sector,tr))

    return a,b,d,tr,det


def n96_signature_diagnostic(sector):
    with mp.workdps(60):
        ns,*_,full=parity_components(96,sector)
        B=to_numpy(smooth_bulk(ns))
        A=to_numpy(full)

    bvals=np.linalg.eigvalsh((B+B.T)/2)
    bneg=int(np.sum(bvals<0))
    if bneg != 2:
        raise RuntimeError(("N96 bulk index",sector,bneg))

    vals,V=eig(A,B,right=True)
    real=np.abs(vals.imag)<1e-8
    inner=real & (np.abs(vals.real)<0.02)

    roots=np.sort(vals.real[inner])
    if len(roots) != 6:
        raise RuntimeError(("expected six N96 inner roots",sector,roots))

    W=np.real(V[:,inner])
    G=(W.T@B@W)
    G=(G+G.T)/2
    sigvals=np.linalg.eigvalsh(G)

    nneg=int(np.sum(sigvals<0))
    npos=int(np.sum(sigvals>0))
    if (nneg,npos)!=(2,4):
        raise RuntimeError(("cluster Krein inertia",sector,sigvals))

    endpoint={}
    for rho in (0.02,0.10):
        fm=A-rho*B
        fp=A+rho*B
        im=int(np.sum(np.linalg.eigvalsh((fm+fm.T)/2)<0))
        ip=int(np.sum(np.linalg.eigvalsh((fp+fp.T)/2)<0))
        if im-ip != 2:
            raise RuntimeError(("signed endpoint count",sector,rho,im,ip))
        endpoint[rho]=(im,ip,im-ip)

    return {
        "roots":roots,
        "cluster_B_eigenvalues":sigvals,
        "cluster_signature":(nneg,npos),
        "full_B_negative_index":bneg,
        "endpoint_inertias":endpoint,
    }


def main():
    for sector in ("even-v","odd-v"):
        a,b,d,tr,det=exact_core_block_intervals(sector)
        print("\nsector =",sector)
        print("B_CC intervals")
        print(" a =",a)
        print(" b =",b)
        print(" d =",d)
        print(" trace =",tr)
        print(" det =",det)
        print(
            "THEOREM: B_CC<0 and B_T>0 imply "
            "B_CC-B_CT B_T^{-1}B_TC<0, hence full ind_-(B_sm)=2."
        )

        out=n96_signature_diagnostic(sector)
        print("N96 six inner generalized roots =",out["roots"])
        print(
            "B restricted to six-root invariant subspace eigs =",
            out["cluster_B_eigenvalues"],
        )
        print("cluster B inertia (-,+) =",out["cluster_signature"])
        print("full N96 B negative index =",out["full_B_negative_index"])
        print("endpoint inertias (F-,F+,difference) =",out["endpoint_inertias"])

    print("\nPASS full smooth-bulk Pontryagin-index / signature diagnostic")
    print(
        "Guardrail: exact theorem is only ind_-(B_sm)=2. "
        "The six-root/signature split is a finite N=96 diagnostic."
    )


if __name__=="__main__":
    main()
