#!/usr/bin/env python3
"""Full-tail raw cross diagnostic for the v14.041 d_sn term.

Finite side = exact near block 8000<n<16000.
Tail side   = same-parity modes n>=16000 (first mode adjusted by parity).

Architecture mirrors the validated historical cross certificates:
  * explicit adjacent band through 32000, compressed by rank-12 SVD;
  * inverse-power low-rank expansion from 32000 through 1,000,000;
  * analytic leading 1/n + coarse B/n^2+C/n^3 completion after 1,000,000.

The parity rank-one pole is included in every piece.

This is a midpoint/provenance diagnostic, not yet an outward certificate.
The purpose is to establish the scale needed by v14.041; the closure only
needs d_sn about <2.1, so a later outward cap can be intentionally coarse.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import svds
from scipy.special import zeta as hurwitz_zeta

from suzuki_endpoint_M3999_midpoint_effective_core import (
    z_source_faithful, pole_vector,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N16000_raw_cross_fulltail_diagnostic_result.json"
NEAR_END=32000
REMOTE_END=1_000_000
LEVELS=8
RANK=12

def lattice(sector,a,b=None):
    start=int(a)
    want_even=(sector=="odd-v")
    if (start%2==0)!=want_even: start+=1
    if b is None:
        return start
    end=int(b)-1
    if (end%2==0)!=want_even: end-=1
    return np.arange(start,end+1,2,dtype=int)

def cross_matrix(F,T,sector):
    m=F.astype(float)[:,None]
    n=T.astype(float)[None,:]
    zm=z_source_faithful(F)[:,None]
    zn=z_source_faithful(T)[None,:]
    A=(2.0/np.pi)*(zn*m-n*zm)/(n*n-m*m)
    pF,alpha=pole_vector(F,sector)
    pT,_=pole_vector(T,sector)
    A+=alpha*np.outer(pF,pT)
    return A

def rank12_near(A):
    U,s,_=svds(A,k=RANK,which="LM",return_singular_vectors=True,
               tol=1e-10,maxiter=3000)
    order=np.argsort(s)[::-1]
    U=U[:,order]; s=s[order]
    fro=float(np.linalg.norm(A,"fro"))
    resid=math.sqrt(max(0.0,fro*fro-float(np.dot(s,s))))
    return U,s,fro,resid

def remote_lowrank(F,T,sector):
    scale=16000.0
    xF=F.astype(float)/scale
    xT=scale/T.astype(float)
    zF=z_source_faithful(F)
    zT=z_source_faithful(T)
    U=[]; C=[]
    for r in range(LEVELS):
        U.append(-(2.0/np.pi)*zF*xF**(2*r))
        C.append(xT**(2*r)/T)
        U.append((2.0/np.pi)*xF**(2*r+1))
        C.append(xT**(2*r+1)*zT/T)
    pF,alpha=pole_vector(F,sector)
    pT,_=pole_vector(T,sector)
    U.append(alpha*pF); C.append(pT)
    U=np.column_stack(U); C=np.vstack(C)
    return U,C@C.T

def parity_sum_upper(n0,p):
    # same-parity n=n0,n0+2,... : first term + integral with step 2
    n=float(n0)
    return n**(-p) + n**(-(p-1))/(2.0*(p-1))

def far_bound(F,sector,n0):
    zF=z_source_faithful(F)
    pF,alpha=pole_vector(F,sector)
    g=math.cosh(0.5) if sector=="even-v" else math.sinh(0.5)
    # p_n = 4g/(pi n) + O(n^-3)
    L=-(2.0/np.pi)*zF + alpha*(4.0*g/np.pi)*pF
    S2=parity_sum_upper(n0,2)
    lead=float(np.linalg.norm(L))*math.sqrt(S2)

    rho=float(F[-1])/float(n0)
    # Coarse |z_n|,|z_m|<=8 geometric correction after leading term.
    B=(16.0/np.pi)/(1-rho*rho)*float(np.linalg.norm(F.astype(float)))
    C=(2.0/np.pi)/(1-rho*rho)*8.0*float(np.linalg.norm(F.astype(float)**2))
    # pole next term is much smaller; absorb a coarse finite-side amount
    C+=1.0
    S4=parity_sum_upper(n0,4)
    S5=parity_sum_upper(n0,5)
    S6=parity_sum_upper(n0,6)
    rem=math.sqrt(B*B*S4+2*B*C*S5+C*C*S6)
    return lead,rem,lead+rem

def one_sector(sector):
    F=lattice(sector,8001,16000)
    t0=lattice(sector,16000)
    Tnear=lattice(sector,t0,NEAR_END)
    Trem=lattice(sector,NEAR_END,REMOTE_END)
    nfar=lattice(sector,REMOTE_END)

    A=cross_matrix(F,Tnear,sector)
    U,s,fro,resid=rank12_near(A)
    Gnear=(U*(s*s))@U.T

    Urem,Gfeat=remote_lowrank(F,Trem,sector)
    Grem=Urem@Gfeat@Urem.T
    combined=math.sqrt(float(np.linalg.eigvalsh(Gnear+Grem)[-1]))
    explicit=combined+resid

    lead,farrem,far=far_bound(F,sector,nfar)
    total=explicit+far

    row={
      "sector":sector,
      "finite_dimension":len(F),
      "tail_near_dimension":len(Tnear),
      "tail_remote_dimension":len(Trem),
      "finite_first":int(F[0]),"finite_last":int(F[-1]),
      "tail_first":int(Tnear[0]),
      "near_last":int(Tnear[-1]),
      "remote_last":int(Trem[-1]),
      "rank12_top":float(s[0]),
      "near_frobenius":fro,
      "near_rank12_residual_fro":resid,
      "combined_near12_remote_lowrank_norm":combined,
      "explicit_plus_near_residual":explicit,
      "far_leading":lead,
      "far_remainder":farrem,
      "far_total":far,
      "full_midpoint_upper_diagnostic":total,
      "target_for_later_outward_cap":1.5,
      "passes_midpoint_target":bool(total<1.5),
    }
    print("\n",json.dumps(row,indent=2))
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v","both"],default="both")
    args=ap.parse_args()
    ss=["even-v","odd-v"] if args.sector=="both" else [args.sector]
    rows=[one_sector(s) for s in ss]
    OUT.write_text(json.dumps({"rows":rows},indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
