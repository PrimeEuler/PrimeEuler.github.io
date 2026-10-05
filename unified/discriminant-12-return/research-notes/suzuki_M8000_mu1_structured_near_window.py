#!/usr/bin/env python3
"""Structured direct-inverse diagnostic for the M8000 near boundary window.

Build the full pole-free M=8000 shifted front F0 using its Cauchy/displacement
structured LDL factorization, then apply the parity rank-one pole by
Sherman-Morrison.

For exact source-faithful coupling rows from the front to
    8000 < n <= 10000,
compute the full finite Gram
    H = C F^{-1} C^*
in one batched triangular solve.

The first 16 principal rows are cross-checked against the LDDD/Feshbach
diagnostic:
    even lambda_max ~= 0.06294224450849
    odd  lambda_max ~= 0.10366466666525.

If the direct structured solve agrees, the full-window trace/lambda_max give
a useful midpoint scale for the exact near-shell correction.

Diagnostic only: this is binary64 structured inversion, not an outward theorem.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from scipy.linalg import solve_triangular

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data, structured_ldl, pole_vector, z_source_faithful,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_structured_near_window_result.json"
MU=1.0
WINDOW_MAX=10000
CHUNK=100

REF={"even-v":0.06294224450849424,"odd-v":0.1036646666652521}


def exact_coupling(front,remote,sector):
    m=front.astype(float)
    zm=z_source_faithful(front)
    pm,alpha=pole_vector(front,sector)
    B=np.empty((len(front),len(remote)),dtype=float)
    for a in range(0,len(remote),CHUNK):
        b=min(a+CHUNK,len(remote))
        ns=remote[a:b].astype(float)
        zn=z_source_faithful(remote[a:b])
        pn,_=pole_vector(remote[a:b],sector)
        den=ns[:,None]**2-m[None,:]**2
        C=(2.0/np.pi)*(zn[:,None]*m[None,:]-ns[:,None]*zm[None,:])/den
        C+=alpha*np.outer(pn,pm)
        B[:,a:b]=C.T
        print(sector,"coupling rows",b,"/",len(remote))
    return B


def one_sector(sector):
    front=np.arange(1 if sector=="even-v" else 2,8001,2,dtype=int)
    shell_start=np.searchsorted(front,4001 if sector=="even-v" else 4002)
    remote=np.arange(8001 if sector=="even-v" else 8002,WINDOW_MAX+1,2,dtype=int)

    z,diag=endpoint_data(front,sign=-1,rho=0.0)
    diag=np.asarray(diag,dtype=float)
    diag[shell_start:]-=MU

    L,D=structured_ldl(front,z,diag)
    minpivot=float(np.min(np.abs(D)))
    sign_counts={
      "negative":int(np.sum(D<0)),
      "positive":int(np.sum(D>0)),
      "zero":int(np.sum(D==0)),
    }

    p,alpha=pole_vector(front,sector)
    # Batched structured solve helper using BLAS triangular solves.
    def solve0(B):
        y=solve_triangular(L,B,lower=True,unit_diagonal=True,check_finite=False)
        y=y/D[:,None]
        return solve_triangular(L.T,y,lower=False,unit_diagonal=True,check_finite=False)

    yp=solve0(p[:,None])[:,0]
    den=1.0+alpha*float(p@yp)

    B=exact_coupling(front,remote,sector)
    X0=solve0(B)
    corr=(p@X0)
    X=X0-alpha*np.outer(yp,corr)/den

    H=B.T@X
    H=(H+H.T)/2
    vals=np.linalg.eigvalsh(H)
    H16=H[:16,:16]
    v16=np.linalg.eigvalsh(H16)
    diagH=np.diag(H)

    row={
      "sector":sector,
      "front_dimension":len(front),
      "window_dimension":len(remote),
      "window_first_mode":int(remote[0]),
      "window_last_mode":int(remote[-1]),
      "polefree_min_abs_pivot":minpivot,
      "polefree_pivot_sign_counts":sign_counts,
      "woodbury_denominator":den,
      "first16_lambda_max":float(v16[-1]),
      "first16_reference":REF[sector],
      "first16_relative_error":float((v16[-1]-REF[sector])/REF[sector]),
      "window_lambda_max":float(vals[-1]),
      "window_trace":float(np.trace(H)),
      "window_min_eigenvalue":float(vals[0]),
      "diag_energy_max":float(np.max(diagH)),
      "diag_energy_sum":float(np.sum(diagH)),
      "diag_first16":[float(x) for x in diagH[:16]],
    }
    print("\n",sector,row)
    return row


def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
      "rows":rows,
      "guardrail":(
        "Binary64 structured direct-inverse diagnostic. First16 agreement with "
        "the independent LDDD/Feshbach result is required before interpreting "
        "the full-window scale."
      )
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("wrote",OUT)

if __name__=="__main__":
    main()
