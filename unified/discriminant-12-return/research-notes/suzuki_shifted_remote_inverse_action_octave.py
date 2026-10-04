#!/usr/bin/env python3
"""Structured inverse-action diagnostic for the shifted remote octave.

For the M=8000 shifted finite front at mu_e=.10, mu_o=.40, let W be the
six dressed protected directions and R their coupling into the next octave

    Q1: 8000 < n <= 16000.

Build the source-faithful shifted remote block

    D1 = A_Q1Q1 - mu I

and compute the actual finite-octave self-energy

    H1 = R^T D1^{-1} R

using the pole-free structured LDL plus the parity rank-one Woodbury update.

Compare:
  * exact structured H1,
  * crude gamma^{-1} R^T R,
  * the protected lower matrix SL_8000 - H1.

By Schur associativity the last matrix should match a direct M=16000
protected reduction up to numerical/reduction errors.  This is a diagnostic
for the sharper remote inverse-action architecture; no infinite theorem is
claimed here.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M8000_shifted_shell_infinite_remote_gram import (
    DPS,
    TARGET_MU,
    rebuild_front,
    remote_rows,
)
from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    pole_vector,
    structured_ldl,
    ldl_solve,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"shifted_remote_inverse_action_octave_result.json"


def solve_full_shifted(modes,sector,mu,B):
    z,diag=endpoint_data(modes,sign=-1,rho=0.0)
    diag=np.asarray(diag,dtype=float)-mu

    L,D=structured_ldl(modes,z,diag)
    if np.min(D)<=0:
        raise RuntimeError((sector,"pole-free octave lost positivity",np.min(D)))

    X0=ldl_solve(L,D,B)
    p,alpha=pole_vector(modes,sector)
    yp=ldl_solve(L,D,p)
    den=1.0+alpha*float(p@yp)
    if den<=0:
        raise RuntimeError((sector,"Woodbury denominator failed",den))

    X=X0-alpha*np.outer(yp,p@X0)/den
    return X,dict(
        polefree_min_pivot=float(np.min(D)),
        woodbury_denominator=float(den),
    )


def one_sector(sector):
    mu=TARGET_MU[sector]
    payload=rebuild_front(sector,mu)
    start=8001 if sector=="even-v" else 8002
    stop=16001 if sector=="even-v" else 16000
    modes=np.arange(start,stop+1,2,dtype=int)

    R=remote_rows(payload,sector,modes)
    X,cond=solve_full_shifted(modes,sector,mu,R)
    H=(R.T@X)
    H=(H+H.T)/2
    G=(R.T@R)
    G=(G+G.T)/2

    # A conservative raw-octave floor estimate from the actual finite block.
    # Used only to display how loose gamma^{-1}G is.
    z,diag=endpoint_data(modes,sign=-1,rho=0.0)
    diag=np.asarray(diag)-mu
    L,D=structured_ldl(modes,z,diag)
    floor_proxy=float(np.min(D))

    with mp.workdps(DPS):
        Hmp=mp.matrix(6)
        Gmp=mp.matrix(6)
        for i in range(6):
            for j in range(6):
                Hmp[i,j]=mp.mpf(str(H[i,j]))
                Gmp[i,j]=mp.mpf(str(G[i,j]))
        Sstructured=(payload["SL"]-Hmp)
        Sstructured=(Sstructured+Sstructured.T)/2
        vals,_=mp.eigsy(Sstructured)

        Scrude=(payload["SL"]-Gmp/mp.mpf(str(floor_proxy)))
        Scrude=(Scrude+Scrude.T)/2
        vals_crude,_=mp.eigsy(Scrude)

    print("\n",sector)
    print("mu =",mu)
    print("octave dimension =",len(modes))
    print("polefree min pivot =",cond["polefree_min_pivot"])
    print("Woodbury denominator =",cond["woodbury_denominator"])
    print("H eigenvalues =",np.linalg.eigvalsh(H))
    print("G eigenvalues =",np.linalg.eigvalsh(G))
    print("structured protected min =",mp.nstr(vals[0],60))
    print("crude proxy protected min =",mp.nstr(vals_crude[0],60))

    return {
        "sector":sector,
        "mu":mu,
        "octave_start":int(modes[0]),
        "octave_stop":int(modes[-1]),
        "octave_dimension":len(modes),
        **cond,
        "H_eigenvalues":[float(x) for x in np.linalg.eigvalsh(H)],
        "G_eigenvalues":[float(x) for x in np.linalg.eigvalsh(G)],
        "structured_protected_eigenvalues":[mp.nstr(vals[j],60) for j in range(6)],
        "structured_protected_min":mp.nstr(vals[0],60),
        "crude_floor_proxy":floor_proxy,
        "crude_protected_min":mp.nstr(vals_crude[0],60),
    }


def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
        "rows":rows,
        "guardrail":(
            "Finite next-octave structured inverse-action diagnostic only. "
            "No outward rounding and no n>16000 contribution are included."
        ),
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)


if __name__=="__main__":
    main()
