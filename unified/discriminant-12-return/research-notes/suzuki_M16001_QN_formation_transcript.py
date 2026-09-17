#!/usr/bin/env python3
"""Fail-closed M16001 Q/N arithmetic transcript checker; no accepted radius literals."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np

def gamma(k, u):
    kk=np.asarray(k,dtype=np.longdouble); ku=kk*u
    if np.any(kk<=0) or np.any(ku>=1): raise ValueError("invalid gamma_k regime")
    return ku/(np.longdouble(1)-ku)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("transcript",type=Path); a=ap.parse_args()
    p=int(np.finfo(np.longdouble).nmant+1)
    if p<64: raise RuntimeError(f"longdouble significand too small: p={p}")
    u=np.longdouble(2)**np.longdouble(-p)
    with np.load(a.transcript,allow_pickle=False) as z:
        missing={"qn_mid","qn_absprod","qn_k"}.difference(z.files)
        if missing: raise RuntimeError(f"missing emitted fields: {sorted(missing)}")
        mid=np.asarray(z["qn_mid"],dtype=np.longdouble); s=np.asarray(z["qn_absprod"],dtype=np.longdouble); k=np.asarray(z["qn_k"])
    if mid.ndim!=2 or s.shape!=mid.shape or not np.all(np.isfinite(mid)) or not np.all(np.isfinite(s)) or np.any(s<0): raise RuntimeError("invalid Q/N transcript")
    if k.ndim==0: k=np.full(mid.shape,int(k),dtype=np.int64)
    elif k.shape!=mid.shape: raise RuntimeError("qn_k shape mismatch")
    if not np.issubdtype(k.dtype,np.integer):
        if not np.all(k==np.floor(k)): raise RuntimeError("nonintegral qn_k")
        k=k.astype(np.int64)
    r=gamma(k,u)*s
    mf=np.sqrt(np.sum(mid*mid,dtype=np.longdouble)); rf=np.sqrt(np.sum(r*r,dtype=np.longdouble))
    print(json.dumps({"status":"PASS","longdouble_significand_bits":p,"shape":list(mid.shape),"k_min":int(np.min(k)),"k_max":int(np.max(k)),"max_absprod":str(np.max(s)),"max_entry_radius":str(np.max(r)),"radius_frobenius":str(rf),"midpoint_frobenius":str(mf),"QN_operator_upper_frobenius_majorant":str(mf+rf)},indent=2,sort_keys=True))
    return 0
if __name__=="__main__": sys.exit(main())
