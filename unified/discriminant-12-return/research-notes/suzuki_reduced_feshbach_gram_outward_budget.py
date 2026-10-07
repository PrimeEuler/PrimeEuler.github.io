#!/usr/bin/env python3
"""Residual-budgeted reduced Feshbach transport on one dyadic octave.

Runs the stable reduced transport at R->2R, reports the well-conditioned
Gram payload D,c,d, and converts complement-solve residuals into conservative
Gram radii using the promoted gamma=1 coercive interface.

The radii deliberately apply a 1000x stress to every measured CG residual.
A hard CROSS_CAP=128 bounds propagation of old-front solution error into the
new octave coupling/source.  The cap is intentionally coarse; the actual
cross block is orders smaller.

This is an audit target, not self-promotion.
"""
from __future__ import annotations
import argparse,json,math
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P,modes_for
from suzuki_full_fft_fixed_capacity_replay import fixed_operator,DPS
from suzuki_ldd_refined_capacity_bracket import mp_inverse_split
from suzuki_ldd_source_operator import dot_columns as dd_dot_columns

N=32000
RTOL=2e-13
STRESS=1000.0
GAMMA=1.0
CROSS_CAP=128.0

def setup(sector,Rmax):
    modes=modes_for(sector,Rmax)
    P=embedded_P(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])
    raw,proj,op,_=fixed_operator(modes,sector,P,Gi)

    E=proj(raw(P))
    Y=np.empty_like(E)
    graph_iters=[]
    for j in range(6):
        cnt=[0]
        y,info=cg(op,E[:,j],rtol=RTOL,atol=0.0,maxiter=40000,
                  callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
        if info!=0: raise RuntimeError((sector,Rmax,"graph",j,info))
        Y[:,j]=proj(y); graph_iters.append(cnt[0])

    g=np.zeros(len(modes),dtype=float)
    mask=modes>N
    if sector=="even-v":
        g[mask]=1.0/modes[mask].astype(float)
    else:
        g[mask]=1.0/(modes[mask].astype(float)-1.0)

    rhs=proj(g)
    cnt=[0]
    q,info=cg(op,rhs,rtol=RTOL,atol=0.0,maxiter=40000,
              callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
    if info!=0: raise RuntimeError((sector,Rmax,"target",info))
    q=proj(q)

    graph_res=np.array([
        np.linalg.norm(op@Y[:,j]-E[:,j]) for j in range(6)
    ],dtype=float)
    target_res=float(np.linalg.norm(op@q-rhs))

    W=P-Y
    AW=raw(W)
    S=(W.T@AW);S=(S+S.T)/2
    b=W.T@g
    h=float(g@q)
    return dict(
        modes=modes,P=P,raw=raw,proj=proj,op=op,Y=Y,W=W,g=g,q=q,
        S=S,b=b,h=h,graph_res=graph_res,target_res=target_res,
        graph_iters=graph_iters,target_iters=cnt[0]
    )

def one(sector,R):
    R2=2*R
    a=setup(sector,R)
    z=setup(sector,R2)
    n1=len(a["modes"])

    Wpad=np.zeros((len(z["modes"]),6),dtype=float)
    Wpad[:n1,:]=a["W"]
    qpad=np.zeros(len(z["modes"]),dtype=float)
    qpad[:n1]=a["q"]

    F=z["raw"](Wpad)[n1:,:]
    r=z["g"][n1:]-z["raw"](qpad)[n1:]
    X=z["Y"][n1:,:]
    y=z["q"][n1:]

    D=F.T@X;D=(D+D.T)/2
    c=F.T@y
    d=float(r@y)

    # 1000x-stressed residual -> solution errors via gamma=1.
    eW=(STRESS/GAMMA)*float(np.linalg.norm(a["graph_res"]))
    eqold=(STRESS/GAMMA)*a["target_res"]
    eX=(STRESS/GAMMA)*float(np.linalg.norm(z["graph_res"]))
    ey=(STRESS/GAMMA)*z["target_res"]

    # Old solve error enters the octave only through the cross block.
    eF=CROSS_CAP*eW
    er=CROSS_CAP*eqold

    Fn=float(np.linalg.norm(F))
    rn=float(np.linalg.norm(r))
    Xn=float(np.linalg.norm(X))
    yn=float(np.linalg.norm(y))

    # Frobenius/l2 radii.
    D_rad=eF*(Xn+eX)+Fn*eX
    c_rad=eF*(yn+ey)+Fn*ey
    d_rad=er*(yn+ey)+rn*ey

    lam=float(np.linalg.eigvalsh(D)[-1])
    cn=float(np.linalg.norm(c))
    # Fail-closed outward orthogonal-leakage upper bound using scalar radii.
    d_hi=d+d_rad
    c_lo=max(0.0,cn-c_rad)
    lam_hi=lam+D_rad
    sigma_perp_hi=d_hi-(c_lo*c_lo)/lam_hi if lam_hi>0 else math.inf

    out={
      "sector":sector,"R":R,"R2":R2,
      "graph_residual_old":a["graph_res"].tolist(),
      "target_residual_old":a["target_res"],
      "graph_residual_new":z["graph_res"].tolist(),
      "target_residual_new":z["target_res"],
      "stress_factor":STRESS,"gamma_used":GAMMA,"cross_cap":CROSS_CAP,
      "F_fro":Fn,"r_l2":rn,"HinvF_fro":Xn,"Hinvr_l2":yn,
      "D_matrix":D.tolist(),"D_fro":float(np.linalg.norm(D)),
      "D_lambda_max":lam,"D_radius_fro":D_rad,
      "c_vector":c.tolist(),"c_l2":cn,"c_radius_l2":c_rad,
      "d":d,"d_radius_abs":d_rad,
      "sigma_perp_mid_upper":d-cn*cn/lam,
      "sigma_perp_stressed_upper":sigma_perp_hi,
      "passes_orthogonal_1e-9":sigma_perp_hi<1e-9,
      "guardrail":"1000x residual-stressed reduced Gram audit target; no self-promotion"
    }
    print(json.dumps(out,indent=2),flush=True)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--R",type=int,choices=[64000,128000],required=True)
    a=ap.parse_args()
    one(a.sector,a.R)

if __name__=="__main__":
    main()
