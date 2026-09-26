#!/usr/bin/env python3
"""N=96 generalized tail Ritz diagnostic after the certified cluster theorem.

Reuses the source-faithful v13.801 full form and smooth bulk, discards the
first two parity modes, and solves

    A_tail q = delta B_sm,tail q

by symmetric bulk normalization.

The values are finite-section diagnostics only.  They are not used to prove
the sector-wise rank-four cluster theorem, which is already certified by the
rho=0.02/rho=0.10 endpoint inertias.
"""
from __future__ import annotations

import mpmath as mp
import numpy as np

from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    smooth_bulk,
)


def to_numpy(M):
    return np.array(
        [[float(M[i,j]) for j in range(M.cols)] for i in range(M.rows)],
        dtype=float,
    )


def generalized_tail_ritz(sector, max_mode=96, core_dim=2):
    data=parity_components(max_mode,sector)
    ns=data[0]
    A=to_numpy(data[-1])
    B=to_numpy(smooth_bulk(ns))

    At=A[core_dim:,core_dim:]
    Bt=B[core_dim:,core_dim:]

    beta,U=np.linalg.eigh((Bt+Bt.T)/2)
    if beta[0] <= 0:
        raise RuntimeError("smooth tail bulk not positive")

    invsqrt=np.diag(1/np.sqrt(beta))
    J=invsqrt@(U.T@At@U)@invsqrt
    J=(J+J.T)/2
    delta,V=np.linalg.eigh(J)

    ids=np.argsort(np.abs(delta))
    return beta[0],delta[ids],V[:,ids]


def main():
    with mp.workdps(50):
        for sector in ("even-v","odd-v"):
            bmin,delta,_=generalized_tail_ritz(sector)
            print("\nsector =",sector)
            print("Btail min =",bmin)
            print("first six delta by |delta| =",delta[:6])

            assert np.all(delta[:4] > -1e-12)
            assert np.max(np.abs(delta[:4])) < 0.02
            assert abs(delta[4]) > 0.10

        print("\nPASS N=96 generalized tail Ritz diagnostic")
        print(
            "Guardrail: finite-section sign evidence only. "
            "No theorem that the four infinite tail eigenvalues are positive "
            "is claimed."
        )


if __name__=="__main__":
    main()
