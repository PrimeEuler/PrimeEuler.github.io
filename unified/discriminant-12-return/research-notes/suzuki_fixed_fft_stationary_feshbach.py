#!/usr/bin/env python3
"""Fast stationary-Feshbach replay for the fixed full-lattice FFT solver.

Purpose: independently reproduce the protected/source scalar without the
O(N^2) full LDDD residual matvec.  The exact stationary identities are

  S = P^T A P - (A P)^T Y,
  g_f = P^T f - (A P)^T y_f,
  G_f = y_f^T f + g_f^T S^{-1} g_f,

where
  Q A Q Y = Q A P,   Q A Q y_f = Q f.

For the leading remote-coupling RHS b=w1,

  g_b = P^T b - (A P)^T y_b,
  M11 = y_b^T b + g_b^T S^{-1} g_b.

The frozen P has support only through N=4000.  Therefore P^T A P, P^T f,
and the base part of A P are evaluated in the existing double-double
arch-200 arithmetic on the fixed 4000 block.  The extension of A P to the
larger lattice is obtained with the validated fixed FFT action.  All global
scalar contractions are accumulated in longdouble and the 6x6 protected
solve is done in mpmath.

This is a diagnostic acceleration only.  It is accepted for 32k/64k only
if it first reproduces the promoted 8k/16k fixed-FFT capacities and shell
ratios far below the theorem sign scale.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_full_fft_fixed_capacity_replay import fixed_operator, DPS, ARCH
from suzuki_M8000_M16000_capacity_ratio_source_sensitivity import embedded_P, modes_for
from suzuki_ldd_refined_capacity_bracket import mp_inverse_split, dd_matrix_to_mp
from suzuki_ldd_source_operator import (
    LD, dot_columns as dd_dot_columns, hp_parity_data_ld as hp_parity_data,
    matvec as dd_matvec, ldd_to_mpf,
)
from suzuki_ldd_M11_direct_difference import w1_dd
from suzuki_endpoint_M3999_midpoint_effective_core import z_source_faithful, pole_vector

HERE=Path(__file__).resolve().parent
OUT=HERE/"fixed_fft_stationary_feshbach_result.json"
BASE=4000
TARGET_C={
 ("even-v",8000):7.527204146095217e-30,
 ("even-v",16000):7.499901498486917e-30,
 ("odd-v",8000):2.170029381845773e-25,
 ("odd-v",16000):2.1622076013239955e-25,
}
TARGET_ETA={
 "even-v":0.0036404008257719944,
 "odd-v":0.003617497467397701,
}

def ld_dot_vec(a,b):
    a=np.asarray(a,dtype=LD); b=np.asarray(b,dtype=LD)
    return np.sum(a*b,dtype=LD)

def ld_dot_cols(A,B):
    A=np.asarray(A,dtype=LD); B=np.asarray(B,dtype=LD)
    out=np.empty((A.shape[1],B.shape[1]),dtype=LD)
    for i in range(A.shape[1]):
        for j in range(B.shape[1]):
            out[i,j]=np.sum(A[:,i]*B[:,j],dtype=LD)
    return out

def mp_from_ld(x):
    return mp.mpf(str(x))

def mp_matrix_from_ld(A):
    return mp.matrix([[mp_from_ld(A[i,j]) for j in range(A.shape[1])]
                      for i in range(A.shape[0])])

def base_payload(sector):
    bm=modes_for(sector,BASE)
    P=embedded_P(sector,bm)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    data=hp_parity_data(bm,sector,dps=DPS,arch_terms=ARCH,correction_terms=50)
    APh,APl=dd_matvec(data,P,None)
    K0h,K0l=dd_dot_columns(P,None,APh,APl)
    pfh,pfl=dd_dot_columns(P,None,data.source_hi[:,None],data.source_lo[:,None])
    bh,bl=w1_dd(data,sector,DPS)
    pbh,pbl=dd_dot_columns(P,None,bh[:,None],bl[:,None])

    with mp.workdps(DPS):
        K0=dd_matrix_to_mp(K0h,K0l)
        Ptf=dd_matrix_to_mp(pfh,pfl)
        Ptb=dd_matrix_to_mp(pbh,pbl)
    return {
      "modes":bm,"P":P,"Gi":Gi,"data":data,
      "AP_ld":np.asarray(APh+APl,dtype=LD),
      "K0":K0,
      "Ptf":Ptf,
      "Ptb":Ptb,
      "b_ld":np.asarray(bh+bl,dtype=LD),
    }

def solve(sector,cutoff,base):
    modes=modes_for(sector,cutoff)
    P=embedded_P(sector,modes)
    raw_mv,proj,op,f=fixed_operator(modes,sector,P,base["Gi"])

    # Fixed-operator responses.
    AP=np.asarray(raw_mv(P),dtype=float)
    E=proj(AP)
    rhs=np.column_stack([E,proj(f)])

    # Full w1 right-hand side.
    z=np.asarray(z_source_faithful(modes),dtype=float)
    p,alpha=pole_vector(modes,sector)
    if sector=="even-v":
        gp=float(mp.cosh(mp.mpf("0.5")))
    else:
        gp=float(mp.sinh(mp.mpf("0.5")))
    b=-(2.0/np.pi)*z + alpha*(4.0*gp/np.pi)*p
    rhs=np.column_stack([rhs,proj(b)])

    sol=np.empty_like(rhs)
    iters=[]; residuals=[]
    for j in range(rhs.shape[1]):
        cnt=[0]
        x,info=cg(op,rhs[:,j],rtol=2e-14,atol=0,maxiter=30000,
                  callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
        if info!=0:
            raise RuntimeError(("CG failed",sector,cutoff,j,info))
        sol[:,j]=proj(x)
        iters.append(cnt[0])
        residuals.append(float(np.linalg.norm(rhs[:,j]-op@sol[:,j])))

    Y=sol[:,:6]; yf=sol[:,6]; yb=sol[:,7]

    # Replace base components of A P, f and b by the DD payload.
    nb=len(base["modes"])
    APld=np.asarray(AP,dtype=LD)
    APld[:nb,:]=base["AP_ld"]
    fld=np.asarray(f,dtype=LD)
    fld[:nb]=np.asarray(base["data"].source_hi+base["data"].source_lo,dtype=LD)
    bld=np.asarray(b,dtype=LD)
    bld[:nb]=base["b_ld"]

    APY=ld_dot_cols(APld,np.asarray(Y,dtype=LD))
    APyf=np.array([ld_dot_vec(APld[:,j],yf) for j in range(6)],dtype=LD)
    APyb=np.array([ld_dot_vec(APld[:,j],yb) for j in range(6)],dtype=LD)
    hyf=ld_dot_vec(yf,fld)
    hyb=ld_dot_vec(yb,bld)

    with mp.workdps(DPS):
        S=mp.matrix(base["K0"])
        for i in range(6):
            for j in range(6):
                S[i,j]-=mp_from_ld(APY[i,j])
        S=(S+S.T)/2

        gf=mp.matrix(6,1); gb=mp.matrix(6,1)
        for i in range(6):
            gf[i]=base["Ptf"][i,0]-mp_from_ld(APyf[i])
            gb[i]=base["Ptb"][i,0]-mp_from_ld(APyb[i])

        wf=mp.lu_solve(S,gf)
        wb=mp.lu_solve(S,gb)
        G=mp_from_ld(hyf)+(gf.T*wf)[0]
        M11=mp_from_ld(hyb)+(gb.T*wb)[0]
        C=1/G

        # Reconstruct finite source solution for L and A=C L^2.
        coeff=np.array([np.longdouble(str(wf[i])) for i in range(6)],dtype=LD)
        W=np.asarray(P-Y,dtype=LD)
        x=np.asarray(yf,dtype=LD)+W@coeff
        zld=np.asarray(z,dtype=LD)
        pld=np.asarray(p,dtype=LD)
        # Replace base z/p by DD payload.
        zld[:nb]=np.asarray(base["data"].z_hi+base["data"].z_lo,dtype=LD)
        pld[:nb]=np.asarray(base["data"].pole_hi+base["data"].pole_lo,dtype=LD)
        zx=mp_from_ld(ld_dot_vec(zld,x))
        px=mp_from_ld(ld_dot_vec(pld,x))
        if sector=="even-v":
            f_lead=4*mp.cosh(1)/mp.pi; g0=mp.cosh(mp.mpf("0.5")); amp=mp.mpf(2)
        else:
            f_lead=-4*mp.sinh(1)/mp.pi; g0=mp.sinh(mp.mpf("0.5")); amp=mp.mpf(-2)
        L=f_lead+(2/mp.pi)*zx-amp*(4*g0/mp.pi)*px
        Aamp=C*L*L
        evals,_=mp.eigsy(S)

    tgt=TARGET_C.get((sector,cutoff))
    row={
      "sector":sector,"cutoff":cutoff,"dimension":len(modes),
      "capacity_stationary":float(C),
      "capacity_target":tgt,
      "capacity_relative_error":None if tgt is None else abs(float(C)-tgt)/abs(tgt),
      "remote_leading_L":mp.nstr(L,50),
      "A_C_times_L_squared":mp.nstr(Aamp,50),
      "M11_direct":mp.nstr(M11,50),
      "protected_S_min_eig":mp.nstr(evals[0],40),
      "cg_iters":iters,
      "recomputed_residual_max":max(residuals),
      "guardrail":"Stationary-Feshbach diagnostic; consume beyond 16k only after 8k/16k calibration passes."
    }
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--cuts",default="8000,16000")
    a=ap.parse_args()
    cuts=[int(x) for x in a.cuts.split(",") if x.strip()]
    base=base_payload(a.sector)
    rows=[solve(a.sector,N,base) for N in cuts]
    out={"sector":a.sector,"rows":rows}
    if 8000 in cuts and 16000 in cuts:
        r8=next(r for r in rows if r["cutoff"]==8000)
        r16=next(r for r in rows if r["cutoff"]==16000)
        eta=r8["capacity_stationary"]/r16["capacity_stationary"]-1.0
        out["eta_8k16k"]=eta
        out["eta_target"]=TARGET_ETA[a.sector]
        out["eta_abs_error"]=abs(eta-TARGET_ETA[a.sector])
        print(json.dumps({"eta_8k16k":eta,"eta_target":TARGET_ETA[a.sector],
                          "eta_abs_error":out["eta_abs_error"]},indent=2),flush=True)
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
