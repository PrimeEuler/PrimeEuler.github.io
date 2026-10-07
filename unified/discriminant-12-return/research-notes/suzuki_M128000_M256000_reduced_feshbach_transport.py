#!/usr/bin/env python3
"""Reduced Feshbach transport from the 128k protected anchor to 256k.

Diagnostic validation of the stable update formulas
    S2 = S1 - F^T H^{-1} F
    b2 = b1 - F^T H^{-1} r
    h2 = h1 + r^T H^{-1} r
without recomputing the tiny protected Schur block by cancellation.

All solves here are binary64 fixed-FFT midpoint diagnostics.  The intended
theorem use is to replace (S1,b1,h1) by the LDDD-certified 128k anchor while
keeping the octave update in its positive/well-conditioned form.
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
R=128000
R2=256000
RTOL=2e-13

def setup(sector,Rmax):
    modes=modes_for(sector,Rmax)
    P=embedded_P(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])
    raw,proj,op,_=fixed_operator(modes,sector,P,Gi)

    E=proj(raw(P))
    Y=np.empty_like(E)
    for j in range(6):
        y,info=cg(op,E[:,j],rtol=RTOL,atol=0.0,maxiter=40000)
        if info!=0: raise RuntimeError((sector,Rmax,"graph",j,info))
        Y[:,j]=proj(y)

    g=np.zeros(len(modes),dtype=float)
    mask=modes>N
    if sector=="even-v":
        g[mask]=1.0/modes[mask].astype(float)
    else:
        g[mask]=1.0/(modes[mask].astype(float)-1.0)

    q,info=cg(op,proj(g),rtol=RTOL,atol=0.0,maxiter=40000)
    if info!=0: raise RuntimeError((sector,Rmax,"target",info))
    q=proj(q)

    W=P-Y
    AW=raw(W)
    S=(W.T@AW); S=(S+S.T)/2
    b=W.T@g
    h=float(g@q)
    K=float(h+b@np.linalg.solve(S,b))
    return dict(modes=modes,P=P,raw=raw,proj=proj,op=op,Y=Y,W=W,g=g,q=q,S=S,b=b,h=h,K=K)

def one(sector):
    a=setup(sector,R)
    b2=setup(sector,R2)
    n1=len(a["modes"])

    # Embed old graph vectors and old complement target into the 256k lattice.
    Wpad=np.zeros((len(b2["modes"]),6),dtype=float)
    Wpad[:n1,:]=a["W"]
    qpad=np.zeros(len(b2["modes"]),dtype=float)
    qpad[:n1]=a["q"]

    # After eliminating the old complement, these are the coupling F and
    # reduced source r on the newly-added octave.
    F=b2["raw"](Wpad)[n1:,:]
    r=b2["g"][n1:]-b2["raw"](qpad)[n1:]

    # The M-components of the full 256k complement solves are H^{-1}F and H^{-1}r.
    Ym=b2["Y"][n1:,:]
    qm=b2["q"][n1:]

    # Validate the reduced equations through energy symmetry identities.
    dS=F.T@Ym
    dS=(dS+dS.T)/2
    db=F.T@qm
    dh=float(r@qm)

    S_up=a["S"]-dS
    b_up=a["b"]-db
    h_up=a["h"]+dh

    K_up=float(h_up+b_up@np.linalg.solve(S_up,b_up))

    out={
      "sector":sector,
      "R":R,"R2":R2,
      "K_R_direct":a["K"],
      "K_R2_direct":b2["K"],
      "K_R2_update":K_up,
      "K_update_abs_error":abs(K_up-b2["K"]),
      "S_update_vs_direct_fro":float(np.linalg.norm(S_up-b2["S"])),
      "b_update_vs_direct_l2":float(np.linalg.norm(b_up-b2["b"])),
      "h_update_vs_direct_abs":abs(h_up-b2["h"]),
      "delta_S_fro":float(np.linalg.norm(dS)),
      "delta_S_matrix":dS.tolist(),
      "delta_S_eigs":np.linalg.eigvalsh(dS).tolist(),
      "delta_b_vector":db.tolist(),
      "delta_b_l2":float(np.linalg.norm(db)),
      "delta_h":dh,
      "F_fro":float(np.linalg.norm(F)),
      "r_l2":float(np.linalg.norm(r)),
      "HinvF_fro":float(np.linalg.norm(Ym)),
      "Hinvr_l2":float(np.linalg.norm(qm)),
      "cross_identity_abs":float(np.linalg.norm(F.T@qm-Ym.T@r)),
      "guardrail":"binary64 midpoint validation of reduced update only"
    }
    print(json.dumps(out,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    one(a.sector)

if __name__=="__main__":
    main()
