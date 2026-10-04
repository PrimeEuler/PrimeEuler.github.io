#!/usr/bin/env python3
"""LDDD Gram of the first four remote-coupling moment vectors at N=4000.

For a remote row n>N, the source-faithful finite-to-remote coupling has

 B_p(n,.)
   = w1_p / n
     + z_n w2 / n^2
     + w3_p / n^3
     + z_n w4 / n^4
     + O(n^-5),

where, on finite modes m<=N,

 w1_p = -(2/pi) z + alpha_p (4 g_p/pi) pole_p,
 w2   =  (2/pi) m,
 w3_p = -(2/pi) z m^2 - alpha_p (4 g_p/pi^3) pole_p,
 w4   =  (2/pi) m^3.

This script computes the correlated 4x4 coefficient matrix

 M_ij = w_i^T A_{p,N}^{-1} w_j

using the unchanged frozen-P4 protected/complement LDDD Feshbach machinery.
It never forms A^{-1}.  The matrix is the finite payload needed for a
Schur-level coercivity bound on

 S_{p,N}=D_p-B_p A_{p,N}^{-1} B_p^*.

Diagnostic only: complement floors are midpoint finite values; final outward
intervals for M require residual/error propagation.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,
    full_source_matrix,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    dd_matrix_to_mp,
    dd_project,
    mp_inverse_split,
    solve_correction,
)
from suzuki_ldd_source_operator import (
    LD,
    add as dd_add,
    dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf,
    matvec as dd_matvec,
    norm2 as dd_norm2,
    split_mpf_ld,
    sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_remote_coupling_moment_gram_ldd_result.json"
NMAX=4000
DPS=180


def channel_matrix_dd(data,modes,sector):
    n=len(modes)
    Bh=np.empty((n,4),dtype=LD)
    Bl=np.empty((n,4),dtype=LD)

    with mp.workdps(DPS):
        alpha=mp.mpf(2 if sector=="even-v" else -2)
        g=mp.cosh(mp.mpf(".5")) if sector=="even-v" else mp.sinh(mp.mpf(".5"))
        c=mp.mpf(2)/mp.pi

        for i,mm in enumerate(modes):
            m=mp.mpf(int(mm))
            z=ldd_to_mpf(data.z_hi[i],data.z_lo[i])
            p=ldd_to_mpf(data.pole_hi[i],data.pole_lo[i])

            vals=[
                -c*z + alpha*(4*g/mp.pi)*p,
                c*m,
                -c*z*m*m - alpha*(4*g/mp.pi**3)*p,
                c*m**3,
            ]
            for j,v in enumerate(vals):
                Bh[i,j],Bl[i,j]=split_mpf_ld(v)
    return Bh,Bl


def coupling_residuals(data,P,Gih,Gil,Yh,Yl):
    Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
    AWh,AWl=dd_matvec(data,Wh,Wl)
    Rh,Rl=dd_project(P,Gih,Gil,AWh,AWl)
    norms=[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(6)]
    return Wh,Wl,AWh,AWl,Rh,Rl,norms


def target_residuals(data,P,Gih,Gil,Xh,Xl,Bh,Bl):
    AXh,AXl=dd_matvec(data,Xh,Xl)
    Rh,Rl=dd_sub(AXh,AXl,Bh,Bl)
    Rh,Rl=dd_project(P,Gih,Gil,Rh,Rl)
    norms=[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(Bh.shape[1])]
    return AXh,AXl,Rh,Rl,norms


def one_sector(sector):
    modes=np.arange(1 if sector=="even-v" else 2,NMAX+1,2,dtype=int)
    P,_=frozen_protected_basis(sector,modes)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,_=full_source_matrix(modes,sector)
    data=hp_parity_data(
        modes,sector,dps=DPS,arch_terms=160,correction_terms=50
    )
    Bh,Bl=channel_matrix_dd(data,modes,sector)
    Bfloat=np.asarray(Bh+Bl,dtype=float)

    # First target initializes the common complement operator and graph solve.
    op,proj,gamma,evals,Y0,x0,initial=build_double_complement(
        A,P,Gi,Bfloat[:,0],rtol=2e-14
    )

    X0=np.empty((len(modes),4),dtype=float)
    X0[:,0]=x0
    init_target=[initial[-1]]
    for j in range(1,4):
        rhs=proj(Bfloat[:,j])
        x,info=cg(op,rhs,rtol=2e-14,atol=0.0,maxiter=30000)
        if info!=0:
            raise RuntimeError((sector,"target CG failed",j,info))
        x=proj(x)
        X0[:,j]=x
        init_target.append(float(np.linalg.norm(rhs-op@x)))

    Yh=Y0.astype(LD)
    Yl=np.zeros_like(Yh,dtype=LD)
    Xh=X0.astype(LD)
    Xl=np.zeros_like(Xh,dtype=LD)

    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    history=[]
    for step in range(2):
        Wh,Wl,AWh,AWl,RYh,RYl,ny=coupling_residuals(
            data,P,Gih,Gil,Yh,Yl
        )
        AXh,AXl,RXh,RXl,nx=target_residuals(
            data,P,Gih,Gil,Xh,Xl,Bh,Bl
        )
        history.append({"coupling":ny,"targets":nx})
        print(sector,"refinement",step,
              "max coupling",max(ny),"max target",max(nx))

        if step==0:
            for j in range(6):
                delta=solve_correction(
                    op,proj,RYh[:,j]+RYl[:,j],rtol=2e-14
                )
                Yh[:,j],Yl[:,j]=dd_add(
                    Yh[:,j],Yl[:,j],
                    delta,np.zeros_like(delta,dtype=LD)
                )
            for j in range(4):
                delta=solve_correction(
                    op,proj,-(RXh[:,j]+RXl[:,j]),rtol=2e-14
                )
                Xh[:,j],Xl[:,j]=dd_add(
                    Xh[:,j],Xl[:,j],
                    delta,np.zeros_like(delta,dtype=LD)
                )
            Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
            Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    # Recompute final graph quantities after refinement.
    Wh,Wl,AWh,AWl,RYh,RYl,ny=coupling_residuals(
        data,P,Gih,Gil,Yh,Yl
    )
    AXh,AXl,RXh,RXl,nx=target_residuals(
        data,P,Gih,Gil,Xh,Xl,Bh,Bl
    )

    Sh,Sl=dd_dot_columns(Wh,Wl,AWh,AWl)
    gh,gl=dd_dot_columns(Wh,Wl,Bh,Bl)
    hh,hl=dd_dot_columns(Bh,Bl,Xh,Xl)

    with mp.workdps(DPS):
        S=dd_matrix_to_mp(Sh,Sl)
        S=(S+S.T)/2
        g=dd_matrix_to_mp(gh,gl)
        h=dd_matrix_to_mp(hh,hl)
        h=(h+h.T)/2
        Sinv_g=mp.matrix(6,4)
        for j in range(4):
            sol=mp.lu_solve(S,g[:,j])
            for i in range(6):
                Sinv_g[i,j]=sol[i]
        M=h+g.T*Sinv_g
        M=(M+M.T)/2
        vals,_=mp.eigsy(M)

        Mstr=[
            [mp.nstr(M[i,j],70) for j in range(4)]
            for i in range(4)
        ]

        # Conservative operator bound for the four retained far scalar
        # channels on n>=8001/8002.  For a same-parity lattice,
        # sum n^-p <= n0^-p + n0^(-(p-1))/(2(p-1)).
        n0=mp.mpf(8001 if sector=="even-v" else 8002)
        def psum(p):
            return n0**(-p)+n0**(-(p-1))/(2*(p-1))
        fnorm=[
            mp.sqrt(psum(2)),
            8*mp.sqrt(psum(4)),
            mp.sqrt(psum(6)),
            8*mp.sqrt(psum(8)),
        ]
        far_abs=mp.fsum(
            abs(M[i,j])*fnorm[i]*fnorm[j]
            for i in range(4) for j in range(4)
        )
        scaled=mp.matrix(4)
        for i in range(4):
            for j in range(4):
                scaled[i,j]=fnorm[i]*M[i,j]*fnorm[j]
        seigs,_=mp.eigsy((scaled+scaled.T)/2)

    print(sector,"M =")
    for row in Mstr:
        print(row)
    print(sector,"M eigs =",[mp.nstr(vals[j],40) for j in range(4)])
    print(sector,"far scalar norms =",[mp.nstr(v,30) for v in fnorm])
    print(sector,"far 4-channel absolute operator bound =",mp.nstr(far_abs,40))

    return {
        "sector":sector,
        "dimension":len(modes),
        "complement_floor_midpoint":gamma,
        "complement_low_eigenvalues":[float(x) for x in evals],
        "initial_target_residuals":init_target,
        "ldd_residual_history":history,
        "final_max_coupling_residual":max(ny),
        "final_max_target_residual":max(nx),
        "channel_order":[
            "w1 / n",
            "z_n*w2 / n^2",
            "w3 / n^3",
            "z_n*w4 / n^4",
        ],
        "M_midpoint":Mstr,
        "M_eigenvalues":[mp.nstr(vals[j],60) for j in range(4)],
        "far_start":int(n0),
        "far_scalar_norm_upper":[mp.nstr(v,50) for v in fnorm],
        "far_four_channel_abs_operator_bound":mp.nstr(far_abs,60),
        "far_scaled_M_eigenvalues":[mp.nstr(seigs[j],50) for j in range(4)],
    }


def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
        "N":NMAX,
        "dps":DPS,
        "rows":rows,
        "guardrail":(
            "Correlated finite-moment Gram diagnostic. LDDD residuals are "
            "reported, but the complement floor and M entries are not yet "
            "promoted as outward exact-source intervals."
        ),
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)


if __name__=="__main__":
    main()
