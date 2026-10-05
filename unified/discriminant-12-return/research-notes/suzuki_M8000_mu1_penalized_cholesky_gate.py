#!/usr/bin/env python3
"""Dense penalized-Cholesky gate for the M=8000, mu=1 shifted front.

Let H=A_8000-Pi_shell with shell 4000<n<=8000, and P the six-column frozen
protected basis used by the LDDD Feshbach gate.  For Lambda>0 define

    H_L = H + Lambda P P^T.

For every x with P^T x=0 the penalty vanishes, so any rigorous lower bound

    H_L >= delta I

implies the same Euclidean lower bound delta for H restricted to the frozen
six-plane complement.

This script explores Lambda and builds a conservative a-posteriori certificate
around a binary64 Cholesky factor L:

    H_nom = L L^T + E.

For the triangular inverse use the rigorous algebraic recursion target

    y_i = (1 + sum_{j<i}|L_ij| y_j)/L_ii,

which bounds ||L^{-1}||_inf in exact arithmetic.  The present replay evaluates
that recursion in longdouble and pads it by a conservative floating reserve.

Then

    lambda_min(L L^T)
      >= 1/(n ||L^{-1}||_inf^2).

For the Cholesky backward error use the standard componentwise model

    |Delta H| <= gamma_{n+1} |L||L|^T,

hence

    ||Delta H||_2 <= gamma_{n+1} ||L||_F^2.

We also subtract the established exact-vs-nominal source-operator uncertainty
2.1e-13.  PASS requires the resulting lower bound to remain positive.

This is intentionally conservative.  It is designed to certify the stiff
complement only; the tiny protected Schur matrix is handled separately.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_penalized_cholesky_gate_result.json"

U=2.0**-53
EPS_SOURCE=2.1e-13


def gamma_n(n,u=U):
    nu=n*u
    if nu>=1:
        raise RuntimeError("gamma_n invalid")
    return nu/(1-nu)


def linv_inf_recursion(L):
    n=L.shape[0]
    y=np.empty(n,dtype=np.longdouble)
    for i in range(n):
        if i==0:
            s=np.longdouble(0)
        else:
            s=np.dot(
                np.abs(L[i,:i].astype(np.longdouble)),
                y[:i],
            )
        y[i]=(np.longdouble(1)+s)/np.longdouble(L[i,i])
    # The recurrence itself uses longdouble.  Pad heavily relative to its
    # observed arithmetic sensitivity; final certificate has orders of
    # magnitude more room if viable.
    mid=float(np.max(y))
    pad=1.0+1e-12
    return mid*pad


def one_sector(sector,lambdas):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    shell_start=len(base_modes)
    A,_=full_source_matrix(modes,sector)
    H=A.copy()
    idx=np.arange(shell_start,len(modes))
    H[idx,idx]-=1.0
    H=(H+H.T)/2

    rows=[]
    for lam in lambdas:
        HP=H+lam*(P@P.T)
        HP=(HP+HP.T)/2
        row={"Lambda":lam}
        try:
            L=np.linalg.cholesky(HP)
        except np.linalg.LinAlgError as e:
            row.update({"cholesky":False,"error":str(e)})
            rows.append(row)
            continue

        linv_inf=linv_inf_recursion(L)
        n=len(modes)
        factor_lower=1.0/(n*linv_inf*linv_inf)

        # Standard worst-case factorization backward-error budget.
        g=gamma_n(n+1)
        l_frob_sq=float(np.sum(L*L,dtype=np.float64))
        chol_backward=g*l_frob_sq

        exact_lower=factor_lower-chol_backward-EPS_SOURCE
        row.update({
            "cholesky":True,
            "min_cholesky_diag":float(np.min(np.diag(L))),
            "max_cholesky_diag":float(np.max(np.diag(L))),
            "linv_inf_bound_padded":linv_inf,
            "factor_lower_bound":factor_lower,
            "gamma_n":g,
            "L_frob_sq":l_frob_sq,
            "cholesky_backward_budget":chol_backward,
            "source_operator_uncertainty":EPS_SOURCE,
            "exact_lower_bound_conservative":exact_lower,
            "pass_conservative":bool(exact_lower>0),
        })
        rows.append(row)
        print(sector,"Lambda",lam,
              "factor lower",factor_lower,
              "backward",chol_backward,
              "exact lower",exact_lower,
              "PASS",exact_lower>0)

        del L,HP

    return {
        "sector":sector,
        "dimension":len(modes),
        "shell_dimension":len(modes)-shell_start,
        "rows":rows,
    }


def main():
    lambdas=[0.1,1.0,10.0,100.0]
    rows=[one_sector("even-v",lambdas),one_sector("odd-v",lambdas)]
    out={
        "mu":1.0,
        "lambdas":lambdas,
        "rows":rows,
        "guardrail":(
            "Conservative dense-Cholesky complement gate.  The only remaining "
            "proof obligation if PASS is to validate the stated longdouble "
            "inverse-recursion padding; all other budgets are analytic or "
            "previously certified."
        ),
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)


if __name__=="__main__":
    main()
