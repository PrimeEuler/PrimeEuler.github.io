#!/usr/bin/env python3
"""Structured inertia diagnostic for the M=8000, mu=1 shifted front.

Goal: certify positivity of the frozen-six-plane complement without forming
the projected dense operator.

Let H = A_shift be the finite M=8000 shifted front and P the frozen six-plane.
For Lambda>0 define the Euclidean projector Pi=P(P^T P)^{-1}P^T and

    H_L = H + Lambda Pi.

If H_L > 0, then the restriction of H to Ran(P)^perp is positive.

Write H_L as

    B0 + V C V^T,

where B0 is the pole-free structured Cauchy matrix with the mu=1 shell
diagonal shift, V=[p,U] with U an orthonormal basis for Ran(P), and
C=diag(alpha,Lambda,...,Lambda).

For invertible B0 and C, Haynsworth gives

    inertia(H_L)
      = inertia(B0)
        + inertia(C^{-1}+V^T B0^{-1}V)
        - inertia(C^{-1}).

This diagnostic reports the structured LDL pivots of B0 and the 7x7
Haynsworth matrix for several Lambda values.

Diagnostic only.  Outward certification of the base factor residual and
7x7 matrix remains separate.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    ldl_solve,
    pole_vector,
    structured_ldl,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_penalized_inertia_diagnostic_result.json"


def inertia(vals, tol=0.0):
    vals=np.asarray(vals,dtype=float)
    return {
        "neg":int(np.sum(vals < -tol)),
        "zero":int(np.sum(np.abs(vals) <= tol)),
        "pos":int(np.sum(vals > tol)),
    }


def one_sector(sector, lambdas):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes)

    # Euclidean orthonormal protected basis.
    G=(P.T@P+P.T@P.T.T)/2 if False else P.T@P
    ew,EV=np.linalg.eigh((G+G.T)/2)
    U=P@(EV@np.diag(1/np.sqrt(ew))@EV.T)
    orth=np.linalg.norm(U.T@U-np.eye(6),2)

    z,diag=endpoint_data(modes,sign=-1,rho=0.0)
    d0=diag.copy()
    d0[shell_start:]-=1.0

    L,D=structured_ldl(modes,z,d0)
    base_inertia=inertia(D)
    min_abs_pivot=float(np.min(np.abs(D)))
    min_pivot=float(np.min(D))
    max_pivot=float(np.max(D))

    p,alpha=pole_vector(modes,sector)
    V=np.column_stack([p,U])

    X=np.empty_like(V)
    solve_res=[]
    for j in range(7):
        X[:,j]=ldl_solve(L,D,V[:,j])
        # reconstruct residual with structured base matrix action using
        # factorization itself: B0 X = L D L^T X
        r=V[:,j]-L@(D*(L.T@X[:,j]))
        solve_res.append(float(np.linalg.norm(r)))

    Gsmall=(V.T@X + X.T@V)/2

    rows=[]
    for lam in lambdas:
        Cinv=np.diag([1.0/alpha]+[1.0/lam]*6)
        K=(Cinv+Gsmall+Cinv.T+Gsmall.T)/2
        kvals=np.linalg.eigvalsh(K)
        cinv_vals=np.diag(Cinv)
        ib=base_inertia
        ik=inertia(kvals)
        ic=inertia(cinv_vals)
        total={
            "neg":ib["neg"]+ik["neg"]-ic["neg"],
            "zero":ib["zero"]+ik["zero"]-ic["zero"],
            "pos":ib["pos"]+ik["pos"]-ic["pos"],
        }
        rows.append({
            "Lambda":lam,
            "K_eigenvalues":[float(x) for x in kvals],
            "K_inertia":ik,
            "Cinv_inertia":ic,
            "predicted_full_inertia":total,
            "positive_midpoint":bool(total["neg"]==0 and total["zero"]==0),
        })

    return {
        "sector":sector,
        "dimension":len(modes),
        "shell_start_index":shell_start,
        "protected_orthogonality_defect":float(orth),
        "alpha":float(alpha),
        "base_inertia":base_inertia,
        "base_min_pivot":min_pivot,
        "base_max_pivot":max_pivot,
        "base_min_abs_pivot":min_abs_pivot,
        "base_solve_residuals":solve_res,
        "Gsmall":Gsmall.tolist(),
        "rows":rows,
    }


def main():
    lambdas=[0.1,1.0,10.0,100.0]
    rows=[one_sector("even-v",lambdas),one_sector("odd-v",lambdas)]
    out={
        "mu":1.0,
        "lambdas":lambdas,
        "rows":rows,
        "guardrail":"Midpoint structured-inertia diagnostic only.",
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    for r in rows:
        print("\n",r["sector"])
        print("base inertia",r["base_inertia"])
        print("base min pivot",r["base_min_pivot"])
        print("base min abs pivot",r["base_min_abs_pivot"])
        print("base max solve residual",max(r["base_solve_residuals"]))
        for q in r["rows"]:
            print("Lambda",q["Lambda"],
                  "K min",min(q["K_eigenvalues"]),
                  "K inertia",q["K_inertia"],
                  "full",q["predicted_full_inertia"],
                  "positive",q["positive_midpoint"])
    print("\nwrote",OUT)


if __name__=="__main__":
    main()
