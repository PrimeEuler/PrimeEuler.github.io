#!/usr/bin/env python3
"""Paired frozen-128k residual-difference diagnostic on 128k<n<=256k.

Reconstructs the same fast finite-128k Feshbach midpoint solutions in both
parities, evaluates the frozen residual source on the next octave, and then
pairs odd/even residuals by their common index j.

Reports the exact Euclidean source-difference contribution bound
  ||drho|| (||rho_e||+||rho_o||)
that enters the paired resolvent identity before the operator-difference term.
Diagnostic only; binary64/Feshbach midpoint arithmetic.
"""
from __future__ import annotations
import json
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P,modes_for
from suzuki_full_fft_fixed_capacity_replay import fixed_operator,DPS
from suzuki_ldd_refined_capacity_bracket import mp_inverse_split
from suzuki_ldd_source_operator import dot_columns as dd_dot_columns
from suzuki_remote_fft_matvec_validation import fft_offdiag
from suzuki_endpoint_M3999_midpoint_effective_core import z_source_faithful,pole_vector

N=32000
R=128000
EXT=256000

def frozen(sector):
    modes=modes_for(sector,R)
    P=embedded_P(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    raw_mv,proj,op,_=fixed_operator(modes,sector,P,Gi)
    E=proj(raw_mv(P))
    Y=np.empty_like(E)
    for j in range(6):
        y,info=cg(op,E[:,j],rtol=2e-13,atol=0.0,maxiter=30000)
        if info!=0: raise RuntimeError((sector,"graph",j,info))
        Y[:,j]=proj(y)

    g=np.zeros(len(modes),dtype=float)
    mask=modes>N
    if sector=="even-v":
        g[mask]=1.0/modes[mask].astype(float)
    else:
        g[mask]=1.0/(modes[mask].astype(float)-1.0)

    q,info=cg(op,proj(g),rtol=2e-13,atol=0.0,maxiter=30000)
    if info!=0: raise RuntimeError((sector,"target",info))
    q=proj(q)

    W=P-Y
    AW=raw_mv(W)
    S=(W.T@AW); S=(S+S.T)/2
    b=W.T@g
    a=np.linalg.solve(S,b)
    x=q+W@a

    ext_modes=modes_for(sector,EXT)
    xpad=np.zeros(len(ext_modes),dtype=float)
    xpad[:len(modes)]=x
    z=z_source_faithful(ext_modes)
    p,alpha=pole_vector(ext_modes,sector)
    y=fft_offdiag(ext_modes,z,xpad)+alpha*p*float(p@xpad)

    gext=np.zeros(len(ext_modes),dtype=float)
    maskext=ext_modes>N
    if sector=="even-v":
        gext[maskext]=1.0/ext_modes[maskext].astype(float)
    else:
        gext[maskext]=1.0/(ext_modes[maskext].astype(float)-1.0)

    tail=ext_modes>R
    rho=gext[tail]-y[tail]
    return {
      "rho":rho,
      "modes":ext_modes[tail],
      "K":float(g@x),
      "finite_residual":float(np.linalg.norm(raw_mv(x)-g)),
    }

def main():
    e=frozen("even-v")
    o=frozen("odd-v")
    if len(e["rho"])!=len(o["rho"]):
        raise RuntimeError("paired residual length mismatch")

    re=e["rho"]; ro=o["rho"]
    d=ro-re
    s=ro+re
    ne=float(np.linalg.norm(re)); no=float(np.linalg.norm(ro)); nd=float(np.linalg.norm(d))
    dot_ds=float(d@s)
    energy_diff=float(ro@ro-re@re)
    source_bound=nd*(ne+no)

    # Exact algebraic decomposition of Euclidean energy difference.
    # Also report average/difference correlations and cumulative smoothness.
    avg=0.5*(ro+re)
    out={
      "R":R,"EXT":EXT,"dimension":len(re),
      "even_first_mode":int(e["modes"][0]),
      "odd_first_mode":int(o["modes"][0]),
      "K_even_mid":e["K"],"K_odd_mid":o["K"],
      "finite_residual_even_mid":e["finite_residual"],
      "finite_residual_odd_mid":o["finite_residual"],
      "rho_even_norm":ne,
      "rho_odd_norm":no,
      "delta_rho_norm":nd,
      "sum_rho_norm":float(np.linalg.norm(s)),
      "avg_rho_norm":float(np.linalg.norm(avg)),
      "energy_even":float(re@re),
      "energy_odd":float(ro@ro),
      "energy_odd_minus_even":energy_diff,
      "delta_dot_sum":dot_ds,
      "energy_identity_abs_error":abs(energy_diff-dot_ds),
      "coercive_source_difference_bound":source_bound,
      "source_difference_bound_over_5e9":source_bound/5e-9,
      "delta_rho_max_abs":float(np.max(np.abs(d))),
      "delta_rho_l1":float(np.sum(np.abs(d))),
      "delta_rho_partial_sum_max":float(np.max(np.abs(np.cumsum(d)))),
      "avg_rho_partial_sum_max":float(np.max(np.abs(np.cumsum(avg)))),
      "rho_cross_dot":float(re@ro),
      "rho_cosine":float((re@ro)/(ne*no)),
      "guardrail":"binary64 fixed-FFT/Feshbach midpoint diagnostic only"
    }
    print(json.dumps(out,indent=2),flush=True)

if __name__=="__main__":
    main()
