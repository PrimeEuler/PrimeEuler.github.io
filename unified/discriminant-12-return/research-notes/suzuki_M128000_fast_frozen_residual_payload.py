#!/usr/bin/env python3
"""Fast finite-128k Feshbach + frozen 128k->256k residual midpoint payload.

Purpose: decide quickly whether the v14.117 residual-energy closure is viable.
Uses the validated fixed-FFT/Feshbach architecture but intentionally skips the
expensive dense LDDD residual refinement.  Diagnostic only; long LDDD jobs
remain the certification path.

Outputs:
  * finite K_128k midpoint,
  * reconstructed full finite inverse vector x,
  * finite residual ||A x-g||,
  * frozen residual rho on 128k<n<=256k,
  * rho energy/partial sums,
  * signed/absolute moments through K=10 for later n>=256k tail work.
"""
from __future__ import annotations
import argparse, json, math
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P,modes_for
from suzuki_full_fft_fixed_capacity_replay import fixed_operator,DPS
from suzuki_ldd_refined_capacity_bracket import mp_inverse_split
from suzuki_ldd_source_operator import dot_columns as dd_dot_columns
from suzuki_remote_fft_matvec_validation import fft_offdiag
from suzuki_endpoint_M3999_midpoint_effective_core import (
    z_source_faithful,pole_vector,
)

N=32000
R=128000
EXT=256000

def one(sector):
    modes=modes_for(sector,R)
    P=embedded_P(sector,modes)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    raw_mv,proj,op,_=fixed_operator(modes,sector,P,Gi)
    E=proj(raw_mv(P))

    Y=np.empty_like(E)
    graph_iters=[]
    for j in range(6):
        cnt=[0]
        y,info=cg(op,E[:,j],rtol=2e-13,atol=0.0,maxiter=30000,
                  callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
        if info!=0: raise RuntimeError((sector,"graph",j,info))
        Y[:,j]=proj(y)
        graph_iters.append(cnt[0])

    g=np.zeros(len(modes),dtype=float)
    mask=modes>N
    if sector=="even-v":
        g[mask]=1.0/modes[mask].astype(float)
    else:
        g[mask]=1.0/(modes[mask].astype(float)-1.0)

    rhs=proj(g)
    cnt=[0]
    q,info=cg(op,rhs,rtol=2e-13,atol=0.0,maxiter=30000,
              callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
    if info!=0: raise RuntimeError((sector,"target",info))
    q=proj(q)

    W=P-Y
    AW=raw_mv(W)
    S=(W.T@AW)
    S=(S+S.T)/2
    b=W.T@g
    a=np.linalg.solve(S,b)
    x=q+W@a

    K=float(g@x)
    h=float(g@q)
    protected=float(b@a)
    finite_res=float(np.linalg.norm(raw_mv(x)-g))

    # Frozen residual on next octave.  Tail rows need only offdiag + pole
    # because x is padded by zero outside R, so the diagonal contributes zero.
    ext_modes=modes_for(sector,EXT)
    xpad=np.zeros(len(ext_modes),dtype=float)
    xpad[:len(modes)]=x
    zext=z_source_faithful(ext_modes)
    pext,alpha=pole_vector(ext_modes,sector)
    yext=fft_offdiag(ext_modes,zext,xpad)+alpha*pext*float(pext@xpad)

    gext=np.zeros(len(ext_modes),dtype=float)
    extmask=ext_modes>N
    if sector=="even-v":
        gext[extmask]=1.0/ext_modes[extmask].astype(float)
    else:
        gext[extmask]=1.0/(ext_modes[extmask].astype(float)-1.0)

    tailmask=ext_modes>R
    rho=gext[tailmask]-yext[tailmask]
    rho_norm=float(np.linalg.norm(rho))
    rho_sq=rho_norm*rho_norm

    # Signed and absolute K=10 moment payload for the frozen source x.
    LD=np.longdouble
    mm=modes.astype(LD)
    xx=x.astype(LD)
    zz=z_source_faithful(modes).astype(LD)
    moments=[]
    for j in range(11):
        pM=2*j+1
        pZ=2*j
        M=np.sum((mm**pM)*xx,dtype=LD)
        Z=np.sum(zz*(mm**pZ)*xx,dtype=LD)
        Sabs=np.sum((mm**(2*j+3))*np.abs(xx),dtype=LD)
        SZabs=np.sum(np.abs(zz)*(mm**(2*j+2))*np.abs(xx),dtype=LD)
        moments.append({
          "j":j,
          "M_2j1":str(M),
          "Z_2j":str(Z),
          "Sabs_2j3":str(Sabs),
          "SZabs_2j2":str(SZabs),
        })

    out={
      "sector":sector,
      "finite_maxmode":R,
      "extended_maxmode":EXT,
      "dimension":len(modes),
      "graph_cg_iters":graph_iters,
      "target_cg_iters":cnt[0],
      "protected_S_min":float(np.linalg.eigvalsh(S)[0]),
      "K_complement_mid":h,
      "K_protected_mid":protected,
      "K_total_mid":K,
      "K_internal_sum_error":abs(K-(h+protected)),
      "finite_raw_residual_mid":finite_res,
      "tail_first_mode":int(ext_modes[tailmask][0]),
      "tail_last_mode":int(ext_modes[tailmask][-1]),
      "tail_dimension":int(np.sum(tailmask)),
      "rho_M_norm_mid":rho_norm,
      "rho_M_energy_mid":rho_sq,
      "rho_M_max_abs_mid":float(np.max(np.abs(rho))),
      "rho_M_l1_mid":float(np.sum(np.abs(rho))),
      "rho_M_partial_sum_max_mid":float(np.max(np.abs(np.cumsum(rho)))),
      "v14117_total_energy_close_target":4.96e-9,
      "rho_M_fraction_of_total_close_budget":rho_sq/4.96e-9,
      "pole_dot_px":float(pext[:len(modes)]@x),
      "moments_K10":moments,
      "guardrail":"binary64 fixed-FFT/Feshbach midpoint diagnostic only; no theorem promotion"
    }
    print(json.dumps(out,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    one(a.sector)

if __name__=="__main__":
    main()
