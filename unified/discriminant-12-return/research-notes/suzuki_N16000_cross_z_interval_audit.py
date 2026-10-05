#!/usr/bin/env python3
"""Interval audit of z_n on the full v14.041 cross band 8000<n<32000.

Only z_n and 2/pi enter the raw off-diagonal cross block D_sn, so this audit
avoids the expensive diagonal/arch machinery of the full M8000 scalar audit.

For every same-parity mode in [8001,31999] / [8002,31998], enclose the exact
source-faithful
    z_n = 2 prime_sine + Im psi(1/4+i n pi/4)
          - parity*n*pi*sum_{j>=0} exp(-2a_j)/(a_j^2+k^2)
with interval arithmetic, including the omitted exponential tail, and compare
against the binary64 z_source_faithful payload used by the cross diagnostic.

A deliberately coarse public target max |Delta z| < 1e-10 is sufficient:
the induced cross-matrix Frobenius perturbation is then far below the 0.02
public cross-core allowance.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M8000_scalar_interval_audit import digamma_im_iv, sym
from suzuki_doubledouble_source_operator import QS
from suzuki_endpoint_M3999_midpoint_effective_core import z_source_faithful

HERE=Path(__file__).resolve().parent
OUT=HERE/"N16000_cross_z_interval_audit_result.json"
IVDPS=140
CORR_TERMS=20

def modes_for(sector):
    start=8001 if sector=="even-v" else 8002
    stop=32000
    return np.arange(start,stop,2,dtype=int)

def exact_z_iv(n):
    nn=mp.iv.mpf(int(n))
    k=nn*mp.iv.pi/2
    parity=1 if int(n)%2==0 else -1
    weights=(
        mp.iv.log(2)/mp.iv.sqrt(2),
        mp.iv.log(3)/mp.iv.sqrt(3),
        mp.iv.log(2)/2,
        mp.iv.log(5)/mp.iv.sqrt(5),
        mp.iv.log(7)/mp.iv.sqrt(7),
    )
    prime=mp.iv.mpf(0)
    for q,w in zip(QS,weights):
        prime += w*mp.iv.sin(nn*mp.iv.pi*mp.iv.log(q)/2)
    psi=digamma_im_iv(int(n))
    corr=mp.iv.mpf(0)
    for j in range(CORR_TERMS):
        a=mp.iv.mpf(2*j)+mp.iv.mpf("0.5")
        corr += mp.iv.exp(-2*a)/(a*a+k*k)
    a0=mp.iv.mpf(2*CORR_TERMS)+mp.iv.mpf("0.5")
    tail=nn*mp.iv.pi*mp.iv.exp(-2*a0)/(a0*a0)/(1-mp.iv.exp(-4))
    z=2*prime+psi-parity*nn*mp.iv.pi*corr
    return z+sym(tail)

def upper_abs_err(ivv,mid):
    p=mp.iv.mpf(repr(float(mid)))
    return float(abs(ivv-p).b)

def one_sector(sector):
    modes=modes_for(sector)
    mids=z_source_faithful(modes,correction_terms=CORR_TERMS)
    best=(0.0,None)
    for i,n in enumerate(modes):
        e=upper_abs_err(exact_z_iv(int(n)),mids[i])
        if e>best[0]: best=(e,int(n))
        if (i+1)%500==0:
            print(sector,"checked",i+1,"/",len(modes),"max",best)
    row={
      "sector":sector,
      "dimension":len(modes),
      "first_mode":int(modes[0]),
      "last_mode":int(modes[-1]),
      "max_z_abs_error":best[0],
      "max_error_mode":best[1],
      "public_target":1e-10,
      "passes":bool(best[0]<1e-10),
    }
    if not row["passes"]:
        raise RuntimeError(("z interval target failed",row))
    print("\n",row)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    old=mp.iv.dps
    mp.iv.dps=IVDPS
    try:
        row=one_sector(a.sector)
    finally:
        mp.iv.dps=old
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
