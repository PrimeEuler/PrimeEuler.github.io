#!/usr/bin/env python3
"""M=3999/4000 two-mode low-core endpoint Schur diagnostic.

This is a finite diagnostic, not an infinite low-core theorem.

For each parity and rho in {0.02,0.10}, split the source-faithful endpoint
pencil into
    core = first two parity modes,
    tail = remaining modes through 3999/4000.

The structured tail solve gives
    S_C = F_CC - F_CT F_TT^{-1} F_TC.

The script reports S_C, its two eigenvalues, determinant, structured solve
residual, and solution norm.  The observed pattern is

    minus endpoint: S_C > 0,
    plus endpoint : S_C < 0,

in both parities and at both radii.

No infinite remote correction is certified here.
"""
from __future__ import annotations

import math
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    offdiag,
    pole_vector,
    structured_ldl,
    ldl_solve,
)


def layout(sector):
    if sector=="even-v":
        return np.array([1,3],dtype=int), np.arange(5,4000,2,dtype=int)
    return np.array([2,4],dtype=int), np.arange(6,4001,2,dtype=int)


def apply_tail_rows(rows,tail,zrows,ztail,diag_tail,p_tail,alpha,X,row_offset):
    blk=offdiag(rows,tail,zrows,ztail)
    for local,global_i in enumerate(
        range(row_offset,row_offset+len(rows))
    ):
        blk[local,global_i]=diag_tail[global_i]
    blk+=alpha*np.outer(p_tail[row_offset:row_offset+len(rows)],p_tail)
    return blk@X


def one_case(sector,sign,rho):
    core,tail=layout(sector)
    modes=np.concatenate([core,tail])

    z,diag=endpoint_data(modes,sign=sign,rho=rho)
    zc,zf=z[:2],z[2:]
    dc,df=diag[:2],diag[2:]

    C0=offdiag(core,core,zc,zc)
    np.fill_diagonal(C0,dc)
    R0=offdiag(core,tail,zc,zf)

    L,D=structured_ldl(tail,zf,df)

    p,alpha=pole_vector(modes,sector)
    pc,pf=p[:2],p[2:]

    C=C0+alpha*np.outer(pc,pc)
    R=R0+alpha*np.outer(pc,pf)

    W=ldl_solve(L,D,R.T)
    yp=ldl_solve(L,D,pf)

    den=1.0+alpha*float(pf@yp)
    if abs(den)<1e-4:
        raise RuntimeError(("small Sherman denominator",sector,sign,rho,den))

    X=W-alpha*np.outer(yp,pf@W)/den

    S=C-R@X
    S=(S+S.T)/2
    vals=np.linalg.eigvalsh(S)

    # Independent chunked residual of the full tail solve.
    res2=0.0
    chunk=300
    for i0 in range(0,len(tail),chunk):
        i1=min(len(tail),i0+chunk)
        rows=tail[i0:i1]
        TX=apply_tail_rows(
            rows,
            tail,
            zf[i0:i1],
            zf,
            df,
            pf,
            alpha,
            X,
            i0,
        )
        rr=R.T[i0:i1]-TX
        res2+=float(np.sum(rr*rr))

    residual=math.sqrt(res2)

    if residual>=2.0e-14:
        raise RuntimeError(("tail solve residual",sector,sign,rho,residual))
    if np.linalg.norm(X,2)>=2.5:
        raise RuntimeError(("tail solve norm",sector,sign,rho,np.linalg.norm(X,2)))

    if sign==-1:
        if vals[0]<=0:
            raise RuntimeError(("minus core Schur not positive",sector,rho,vals))
    else:
        if vals[-1]>=0:
            raise RuntimeError(("plus core Schur not negative",sector,rho,vals))

    return {
        "matrix":S,
        "eigenvalues":vals,
        "determinant":float(np.linalg.det(S)),
        "tail_solve_residual":residual,
        "tail_solution_norm":float(np.linalg.norm(X,2)),
        "pole_denominator":den,
        "polefree_min_pivot":float(np.min(D)),
    }


def main():
    for rho in (0.02,0.10):
        print("\nrho =",rho)
        for sector in ("even-v","odd-v"):
            for sign,name in ((-1,"minus"),(+1,"plus")):
                out=one_case(sector,sign,rho)
                print("\n",sector,name)
                for k,v in out.items():
                    print(k,"=",v)

    print("\nPASS finite M3999/4000 low-core endpoint Schur diagnostic")
    print(
        "Guardrail: sign pattern is finite-section evidence only. "
        "Infinite remote low-core correction still needs certification."
    )


if __name__=="__main__":
    main()
