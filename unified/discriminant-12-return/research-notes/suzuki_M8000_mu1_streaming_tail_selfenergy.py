#!/usr/bin/env python3
"""Streaming structured-LDL tail self-energy for the M8000, mu=1 front.

Purpose
-------
Avoid both failure modes already identified:
  * no scalar gamma^{-1} R^*R majorant;
  * no inverse-power approximation at the near boundary m/n -> 1.

For the certified M=8000 shifted front F at mu=1, let W be the six dressed
protected directions and R(n) their exact source-faithful coupling into the
raw tail n>8000.  On a finite tail principal section Q_M, write

    D_M = A_{Q_M Q_M} - I.

The pole-free Cauchy/displacement block admits the exact structured LDL
recursion.  For any RHS matrix R, if y=L^{-1}R then

    R^T D_0^{-1} R = sum_k y_k^T y_k / d_k.

The parity pole is then applied by Sherman-Morrison using the similarly
transformed pole vector.  Therefore we can accumulate the exact finite-tail
self-energy without storing L or using a norm proxy.

At checkpoints this script reports the eigenvalues of

    S_front - H_M,

where H_M is the finite-tail structured self-energy.  This is a midpoint
diagnostic of the correlated cancellation, not an outward infinite theorem.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np
import mpmath as mp

from suzuki_M8000_shifted_shell_infinite_remote_gram import (
    DPS, rebuild_front, remote_rows,
)
from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data, pole_vector,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_streaming_tail_selfenergy_result.json"

MU=1.0  # trigger replay after workflow installation
MAX_MODE=24000
CHECKPOINTS=(10000,12000,16000,20000,24000)
CHUNK=400


def exact_remote_rows_chunked(payload,sector,modes):
    R=np.empty((len(modes),6),dtype=float)
    for a in range(0,len(modes),CHUNK):
        b=min(a+CHUNK,len(modes))
        R[a:b]=remote_rows(payload,sector,modes[a:b])
        print(sector,"built exact remote rows",b,"/",len(modes))
    return R


def one_sector(sector):
    payload=rebuild_front(sector,MU)
    start=8001 if sector=="even-v" else 8002
    stop=MAX_MODE-1 if sector=="even-v" and MAX_MODE%2==0 else MAX_MODE
    if sector=="odd-v" and stop%2:
        stop-=1
    modes=np.arange(start,stop+1,2,dtype=int)

    R=exact_remote_rows_chunked(payload,sector,modes)
    z,diag=endpoint_data(modes,sign=-1,rho=0.0)
    dcur=np.asarray(diag,dtype=float)-MU
    x=modes.astype(float)**2
    u=np.asarray(z,dtype=float).copy()
    v=modes.astype(float).copy()

    p,alpha=pole_vector(modes,sector)
    yp=np.asarray(p,dtype=float).copy()
    Y=R.copy()

    H0=np.zeros((6,6),dtype=float)
    q=0.0
    t=np.zeros(6,dtype=float)

    cp_idx={}
    for c in CHECKPOINTS:
        # largest same-parity mode <= checkpoint
        cc=c
        want_even=(sector=="odd-v")
        if (cc%2==0)!=want_even:
            cc-=1
        if cc>=start:
            cp_idx[int(cc)]=None

    rows=[]
    min_pivot=float("inf")
    for k in range(len(modes)):
        pivot=float(dcur[k])
        min_pivot=min(min_pivot,pivot)
        if not pivot>0:
            raise RuntimeError((sector,"pole-free pivot lost positivity",k,int(modes[k]),pivot))

        y=Y[k].copy()
        pp=float(yp[k])
        H0 += np.outer(y,y)/pivot
        q += pp*pp/pivot
        t += pp*y/pivot

        den=1.0+alpha*q
        if not den>0:
            raise RuntimeError((sector,"Woodbury denominator failed",k,den))

        if int(modes[k]) in cp_idx:
            H=H0-alpha*np.outer(t,t)/den
            H=(H+H.T)/2
            with mp.workdps(DPS):
                Hmp=mp.matrix(6)
                for i in range(6):
                    for j in range(6):
                        Hmp[i,j]=mp.mpf(str(H[i,j]))
                S=(payload["SL"]-Hmp)
                S=(S+S.T)/2
                vals,_=mp.eigsy(S)
            row={
                "mode":int(modes[k]),
                "tail_dimension":k+1,
                "min_polefree_pivot_so_far":min_pivot,
                "woodbury_denominator":den,
                "H_eigenvalues":[float(vv) for vv in np.linalg.eigvalsh(H)],
                "protected_eigenvalues":[mp.nstr(vals[j],60) for j in range(6)],
                "protected_min":mp.nstr(vals[0],60),
            }
            rows.append(row)
            print("\n",sector,"checkpoint",row["mode"])
            print("min pivot =",min_pivot,"den =",den)
            print("H eig max =",row["H_eigenvalues"][-1])
            print("protected min =",row["protected_min"])

        if k+1<len(modes):
            b=(2.0/np.pi)*(u[k]*v[k+1:]-v[k]*u[k+1:])/(x[k]-x[k+1:])
            ell=b/pivot
            dcur[k+1:]-=b*ell
            u[k+1:]-=ell*u[k]
            v[k+1:]-=ell*v[k]
            Y[k+1:]-=ell[:,None]*y[None,:]
            yp[k+1:]-=ell*pp

    return {
        "sector":sector,
        "mu":MU,
        "front_last_mode":int(payload["modes"][-1]),
        "tail_start":int(modes[0]),
        "tail_stop":int(modes[-1]),
        "finite_front_protected_min":mp.nstr(mp.eigsy(payload["SL"])[0][0],60),
        "checkpoints":rows,
        "guardrail":(
            "Midpoint finite-tail structured self-energy diagnostic. Exact "
            "source-faithful finite rows and structured LDL/Woodbury are used, "
            "but no outward rounding or infinite remainder is certified."
        ),
    }


def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={"max_mode":MAX_MODE,"rows":rows}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)


if __name__=="__main__":
    main()
