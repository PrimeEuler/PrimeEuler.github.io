#!/usr/bin/env python3
"""Fail-closed outward complement certificate for the M=8000, mu=1 front.

For each parity let
    H = A_8000 - Pi_{4000<n<=8000}
and P be the frozen six-column source-active carrier.  With Lambda=1 set
    Hplus = H + P P^T.

For every x with P^T x=0 the penalty vanishes, hence
    x^T H x = x^T Hplus x.
Therefore any certified lower bound Hplus >= delta I proves the same delta
for the Euclidean frozen-carrier complement of H.

The certificate treats the binary64 Cholesky factor L as exact payload data
and charges:
  1. a rigorous upper bound on ||L^{-1}||_inf via a positive recurrence
     evaluated with directed nextafter and a gamma_n dot-product envelope;
  2. the standard Cholesky backward-error theorem
         |Delta H| <= gamma_{n+1}|L||L|^T;
  3. exact-vs-nominal source-operator uncertainty 2.1e-13;
  4. binary64 shell-shift, PP^T formation, addition, and symmetrization
     rounding.

The resulting lower bound is
    delta >= 1/(n ||L^{-1}||_inf^2)
             - chol_backward
             - source_uncertainty
             - formation_uncertainty.

No midpoint eigensolver enters the PASS criterion.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_penalized_cholesky_outward_result.json"

LD=np.longdouble
U64=LD(2.0)**LD(-53)
ULD=LD(np.finfo(np.longdouble).eps)/LD(2)
EPS_SOURCE=LD("2.1e-13")
LAMBDA=LD(1)


def up(x):
    return np.nextafter(LD(x), LD(np.inf), dtype=LD)


def down(x):
    return np.nextafter(LD(x), LD(-np.inf), dtype=LD)


def gamma_up(k: int, u: LD):
    ku=up(LD(k)*u)
    if ku >= 1:
        raise RuntimeError(("gamma invalid",k,str(ku)))
    return up(ku/down(LD(1)-ku))


def positive_dot_upper(a,b):
    """Upper bound for exact dot(a,b), for nonnegative LD arrays.

    a,b are represented longdouble values.  Multiplication and summation are
    charged by the conservative standard gamma_{2m+1} model; nextafter makes
    the final division directed upward.
    """
    a=np.asarray(a,dtype=LD)
    b=np.asarray(b,dtype=LD)
    if len(a)==0:
        return LD(0)
    if np.any(a<0) or np.any(b<0):
        raise RuntimeError("positive_dot_upper received negative input")
    fl=np.sum(a*b,dtype=LD)
    g=gamma_up(2*len(a)+1,ULD)
    return up(fl/down(LD(1)-g))


def linv_inf_upper(L):
    """Certified row-sum upper bound for the inverse of exact binary64 L."""
    n=L.shape[0]
    y=np.empty(n,dtype=LD)
    for i in range(n):
        s=positive_dot_upper(
            np.abs(L[i,:i].astype(LD)),
            y[:i],
        )
        num=up(LD(1)+s)
        den=LD(L[i,i])  # binary64 value is exact in longdouble
        if den<=0:
            raise RuntimeError(("nonpositive Cholesky diagonal",i,float(den)))
        y[i]=up(num/den)
    return up(np.max(y))


def frob_sq_upper_binary64_matrix(X):
    """Upper bound for exact sum of squares of binary64 entries."""
    x=np.asarray(X,dtype=float).ravel()
    # Process in chunks to avoid a full longdouble matrix copy.
    total=LD(0)
    count=0
    chunk=1_000_000
    for i in range(0,len(x),chunk):
        q=x[i:i+chunk].astype(LD)
        # Each square + sum.  Local gamma then directed accumulation.
        fl=np.sum(q*q,dtype=LD)
        g=gamma_up(2*len(q)+1,ULD)
        local=up(fl/down(LD(1)-g))
        total=up(total+local)
        count+=len(q)
    # Cross-chunk additions are explicitly nextafter-up, already outward.
    return total


def vector_sq_sum_upper(x):
    q=np.asarray(x,dtype=float).astype(LD)
    return positive_dot_upper(np.abs(q),np.abs(q))


def one_sector(sector):
    base_modes,modes,P,_,_=embedded_protected_basis(sector)
    n=len(modes)
    shell_start=len(base_modes)

    A,_=full_source_matrix(modes,sector)

    # Mathematical nominal shifted matrix is exact(binary64 A) - I_shell.
    # Stored subtraction receives an explicit diagonal rounding charge.
    H=A.copy()
    olddiag=np.diag(A)[shell_start:].copy()
    idx=np.arange(shell_start,n)
    H[idx,idx]-=1.0
    H=(H+H.T)/2.0

    # Shift-rounding: |fl(a-1)-(a-1)| <= u/(1-u)(|a|+1).
    diag_mag=np.abs(olddiag)+1.0
    shift_entry_factor=up(U64/down(LD(1)-U64))
    shift_frob=up(
        shift_entry_factor
        * np.sqrt(vector_sq_sum_upper(diag_mag),dtype=LD)
    )

    # Penalty formation from exact frozen binary64 P.
    Pfrob2=frob_sq_upper_binary64_matrix(P)
    g6=gamma_up(6,U64)
    penalty_mult=up(g6*Pfrob2)  # ||E_PP||_2 <= gamma_6 ||P||_F^2

    Cfl=P@P.T

    # Addition/symmetrization rounding, bounded in Frobenius norm.
    Hfrob=up(np.sqrt(frob_sq_upper_binary64_matrix(H),dtype=LD))
    Cfrob=up(np.sqrt(frob_sq_upper_binary64_matrix(Cfl),dtype=LD))
    # One binary64 addition plus one symmetrizing addition; division by 2 exact.
    # 4u is a deliberately conservative first-order envelope; denominator
    # turns it into a standard gamma-style bound.
    form_factor=up((LD(4)*U64)/down(LD(1)-LD(4)*U64))
    add_sym=up(form_factor*up(Hfrob+Cfrob))

    HP=H+Cfl
    HP=(HP+HP.T)/2.0

    L=np.linalg.cholesky(HP)

    # Exact lower bound for the computed-factor Gram LL^T.
    linv=linv_inf_upper(L)
    denom=up(LD(n)*up(linv*linv))
    factor_lower=down(LD(1)/denom)

    # Standard Cholesky backward error.
    m=n*(n+1)//2
    # Frobenius square only needs triangular L entries.
    Ltri=L[np.tril_indices(n)]
    Lfrob2=frob_sq_upper_binary64_matrix(Ltri)
    gchol=gamma_up(n+1,U64)
    chol_backward=up(gchol*Lfrob2)

    formation=up(shift_frob+up(penalty_mult+add_sym))
    total_charge=up(
        chol_backward
        + up(EPS_SOURCE+formation)
    )
    exact_lower=down(factor_lower-total_charge)

    row={
        "sector":sector,
        "dimension":n,
        "base_last_mode":int(base_modes[-1]),
        "target_last_mode":int(modes[-1]),
        "Lambda":1.0,
        "linv_inf_upper":str(linv),
        "factor_gram_lower":str(factor_lower),
        "cholesky_gamma":str(gchol),
        "L_frob_sq_upper":str(Lfrob2),
        "cholesky_backward_upper":str(chol_backward),
        "source_operator_uncertainty":str(EPS_SOURCE),
        "shell_shift_rounding_upper":str(shift_frob),
        "penalty_matmul_rounding_upper":str(penalty_mult),
        "addition_sym_rounding_upper":str(add_sym),
        "formation_rounding_upper":str(formation),
        "total_charge_upper":str(total_charge),
        "certified_complement_lower":str(exact_lower),
        "PASS":bool(exact_lower>0),
    }
    print("\n",sector)
    for k,v in row.items():
        if k!="sector":
            print(k,"=",v)
    if not row["PASS"]:
        raise RuntimeError((sector,"outward penalized Cholesky gate failed",row))
    return row


def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
        "mu":1.0,
        "Lambda":1.0,
        "rows":rows,
        "theorem_scope":(
            "PASS certifies a positive Euclidean lower bound for the shifted "
            "M8000 operator restricted to the Euclidean orthogonal complement "
            "of the frozen six-plane.  It does not by itself certify the "
            "six-dimensional protected Schur block."
        ),
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nPASS: outward penalized-Cholesky complement certificate")
    print("wrote",OUT)


if __name__=="__main__":
    main()
