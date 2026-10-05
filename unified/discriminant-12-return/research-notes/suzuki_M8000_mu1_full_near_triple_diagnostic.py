#!/usr/bin/env python3
"""Full v14.041 near-block triple midpoint diagnostic.

Compute the finite near quantities for
  front: m <= 8000,
  near:  8000 < n < 16000,
  sep sample: 16000 <= n < 24000.

This is deliberately a midpoint viability test before outward promotion.

For each parity:
  F = shifted M=8000 front (mu=1),
  Bn = exact source-faithful front-to-near coupling,
  Hn = Bn F^{-1} Bn^*,
  Ann = (Dnn-I) - Hn.

Report
  b_nn = lambda_max(Hn),
  delta_nn = lambda_min(Ann),
  d_sn_sample = ||D_sn|| for near x sep-sample,
and test the v14.041 closure inequality with the sampled d_sn.

The front inverse is evaluated with the exact structured pole-free LDL plus
Sherman-Morrison parity pole, as in the already-crosschecked near-window
diagnostic.  Because the Woodbury denominator is near binary64 resolution,
all values here are DIAGNOSTIC ONLY and must be re-evaluated/certified through
the protected/Feshbach architecture before theorem promotion.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
from scipy.linalg import solve_triangular
from scipy.sparse.linalg import eigsh, svds, LinearOperator

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data, structured_ldl, pole_vector, z_source_faithful,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_full_near_triple_diagnostic_result.json"
MU=1.0
SEP_SAMPLES_END=24000
CHUNK=200
SEP_BOUND=0.941
# workflow trigger: full near-triple viability replay
DELTA_SS=1.3457

def lattice(sector,a,b):
    start=a
    want_even=(sector=="odd-v")
    if (start%2==0)!=want_even: start+=1
    end=b-1
    if (end%2==0)!=want_even: end-=1
    return np.arange(start,end+1,2,dtype=int)

def exact_cross(rows,cols,sector):
    # Matrix with shape len(rows) x len(cols): A[rows,cols].
    rr=rows.astype(float); cc=cols.astype(float)
    zr=z_source_faithful(rows); zc=z_source_faithful(cols)
    pr,alpha=pole_vector(rows,sector); pc,_=pole_vector(cols,sector)
    out=np.empty((len(rows),len(cols)),dtype=float)
    for a in range(0,len(rows),CHUNK):
        b=min(a+CHUNK,len(rows))
        r=rr[a:b]; z=zr[a:b]; p=pr[a:b]
        den=r[:,None]**2-cc[None,:]**2
        C=(2.0/np.pi)*(z[:,None]*cc[None,:]-r[:,None]*zc[None,:])/den
        C+=alpha*np.outer(p,pc)
        out[a:b]=C
        print(sector,"cross rows",b,"/",len(rows))
    return out

def raw_block(modes,sector,shift=0.0):
    z,diag=endpoint_data(modes,sign=-1,rho=0.0)
    mm=modes.astype(float)
    Z=np.asarray(z,dtype=float)
    den=mm[:,None]**2-mm[None,:]**2
    safe=den.copy()
    np.fill_diagonal(safe,1.0)
    A=(2.0/np.pi)*(Z[:,None]*mm[None,:]-mm[:,None]*Z[None,:])/safe
    p,alpha=pole_vector(modes,sector)
    A+=alpha*np.outer(p,p)
    np.fill_diagonal(A,np.asarray(diag,dtype=float)+alpha*p*p-shift)
    return (A+A.T)/2

def front_inverse_apply_factory(sector):
    front=lattice(sector,1,8001)
    shell_start=np.searchsorted(front,4001 if sector=="even-v" else 4002)
    z,diag=endpoint_data(front,sign=-1,rho=0.0)
    diag=np.asarray(diag,dtype=float)
    diag[shell_start:]-=MU
    L,D=structured_ldl(front,z,diag)
    p,alpha=pole_vector(front,sector)

    def solve0(B):
        B=np.asarray(B,dtype=float)
        one=(B.ndim==1)
        if one: B=B[:,None]
        y=solve_triangular(L,B,lower=True,unit_diagonal=True,check_finite=False)
        y=y/D[:,None]
        x=solve_triangular(L.T,y,lower=False,unit_diagonal=True,check_finite=False)
        return x[:,0] if one else x

    yp=solve0(p)
    den=1.0+alpha*float(p@yp)
    def solve(B):
        B=np.asarray(B,dtype=float)
        one=(B.ndim==1)
        if one: B=B[:,None]
        X0=solve0(B)
        corr=p@X0
        X=X0-alpha*np.outer(yp,corr)/den
        return X[:,0] if one else X
    meta={
      "front_dimension":len(front),
      "polefree_min_abs_pivot":float(np.min(np.abs(D))),
      "polefree_negative_pivots":int(np.sum(D<0)),
      "woodbury_denominator":float(den),
    }
    return front,solve,meta

def one_sector(sector):
    front,Finv,meta=front_inverse_apply_factory(sector)
    near=lattice(sector,8001,16000)
    sep=lattice(sector,16000,SEP_SAMPLES_END)
    print(sector,"dims",len(front),len(near),len(sep))

    Bn=exact_cross(near,front,sector)
    Dnn=raw_block(near,sector,shift=1.0)

    # Do not materialize Hn; use operator actions to keep memory moderate.
    def Hmv(x):
        t=Bn.T@x
        y=Finv(t)
        return Bn@y
    Hop=LinearOperator((len(near),len(near)),matvec=Hmv,dtype=float)
    bnn=float(eigsh(Hop,k=1,which="LA",return_eigenvectors=False,tol=2e-9,maxiter=5000)[0])

    def Amv(x):
        return Dnn@x-Hmv(x)
    Aop=LinearOperator((len(near),len(near)),matvec=Amv,dtype=float)
    delta=float(eigsh(Aop,k=1,which="SA",return_eigenvectors=False,tol=2e-9,maxiter=10000)[0])

    Dsn=exact_cross(sep,near,sector)
    # Largest singular value of finite adjacent sep sample.
    dsn=float(svds(Dsn,k=1,which="LM",return_singular_vectors=False,tol=1e-9,maxiter=5000)[0])

    lhs=(dsn+np.sqrt(SEP_BOUND*max(bnn,0.0)))**2
    rhs=DELTA_SS*delta
    row={
      "sector":sector,
      **meta,
      "near_dimension":len(near),
      "near_first":int(near[0]),"near_last":int(near[-1]),
      "sep_sample_dimension":len(sep),
      "sep_sample_first":int(sep[0]),"sep_sample_last":int(sep[-1]),
      "b_nn_midpoint":bnn,
      "delta_nn_midpoint":delta,
      "d_sn_sample_midpoint":dsn,
      "closure_lhs_sample":float(lhs),
      "closure_rhs_midpoint":float(rhs),
      "closure_ratio_sample":float(lhs/rhs) if rhs>0 else float("inf"),
      "sample_closes":bool(rhs>0 and lhs<rhs),
      "guardrail":(
        "Midpoint viability diagnostic only. d_sn_sample is a LOWER diagnostic "
        "for the infinite d_sn, while b_nn/delta_nn use the binary64 structured "
        "front inverse whose Woodbury denominator is near resolution."
      )
    }
    print("\n",json.dumps(row,indent=2))
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v","both"],default="both")
    args=ap.parse_args()
    sectors=["even-v","odd-v"] if args.sector=="both" else [args.sector]
    rows=[one_sector(s) for s in sectors]
    out={"rows":rows}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
