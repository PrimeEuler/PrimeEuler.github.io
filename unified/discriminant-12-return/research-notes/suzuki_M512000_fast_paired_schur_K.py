#!/usr/bin/env python3
"""Fast finite-512k paired-Schur K midpoint payload.

Uses the validated fixed-FFT/Feshbach six-plane architecture, skipping the
expensive dense LDDD refinement. Diagnostic only. Intended to compute the
exact finite-octave correlated increment
    K_512k^fin - K_128k^fin
at midpoint scale before the long certification replay.
"""
from __future__ import annotations
import argparse, json
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P,modes_for
from suzuki_full_fft_fixed_capacity_replay import fixed_operator,DPS
from suzuki_ldd_refined_capacity_bracket import mp_inverse_split
from suzuki_ldd_source_operator import dot_columns as dd_dot_columns

N=32000
R=512000

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
        y,info=cg(op,E[:,j],rtol=2e-13,atol=0.0,maxiter=40000,
                  callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
        if info!=0: raise RuntimeError((sector,"graph",j,info))
        Y[:,j]=proj(y); graph_iters.append(cnt[0])

    g=np.zeros(len(modes),dtype=float)
    mask=modes>N
    if sector=="even-v":
        g[mask]=1.0/modes[mask].astype(float)
    else:
        g[mask]=1.0/(modes[mask].astype(float)-1.0)

    rhs=proj(g)
    cnt=[0]
    q,info=cg(op,rhs,rtol=2e-13,atol=0.0,maxiter=40000,
              callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
    if info!=0: raise RuntimeError((sector,"target",info))
    q=proj(q)

    W=P-Y
    AW=raw_mv(W)
    S=(W.T@AW); S=(S+S.T)/2
    b=W.T@g
    a=np.linalg.solve(S,b)
    x=q+W@a

    h=float(g@q)
    protected=float(b@a)
    K=float(g@x)
    residual=float(np.linalg.norm(raw_mv(x)-g))

    out={
      "sector":sector,
      "maxmode":R,
      "dimension":len(modes),
      "remote_dimension":int(np.sum(mask)),
      "graph_cg_iters":graph_iters,
      "target_cg_iters":cnt[0],
      "protected_S_eigs":np.linalg.eigvalsh(S).tolist(),
      "K_complement_mid":h,
      "K_protected_mid":protected,
      "K_total_mid":K,
      "K_internal_sum_error":abs(K-(h+protected)),
      "finite_raw_residual_mid":residual,
      "guardrail":"binary64 fixed-FFT/Feshbach midpoint diagnostic only"
    }
    print(json.dumps(out,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    one(a.sector)

if __name__=="__main__":
    main()
