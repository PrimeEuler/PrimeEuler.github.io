#!/usr/bin/env python3
"""N=4000 source residual + K=10 absolute-moment certificate target.

Purpose
-------
Prepare the final outward inputs required by v14.022 / v14.027 §6(c).

For each parity:
  * reconstruct the same one-refinement LDDD N=4000 finite source solution;
  * directly evaluate its finite-row LDDD residual A x - f;
  * report ||x||_2 and the K=10 absolute moments
        S^z_22 = sum |z_m| m^22 |x_m|,
        S_23   = sum m^23 |x_m|;
  * report C_N and sqrt(C_N);
  * report Cauchy-Schwarz weights sqrt(sum m^46) and
        sqrt(sum |z_m|^2 m^44)
    needed to propagate one l2 source-solution error ball to the moments.

This remains a certificate target until the ledger charges exact-source
operator/source representation and LDDD arithmetic around the reported
midpoints.
"""
from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,
    full_source_matrix,
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
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,
    dd_project,
    form_Ktilde,
    form_trial,
    mp_inverse_split,
    refine_once,
    residuals_dd,
)
from suzuki_ldd_remote_source_lead_diagnostic import dd_linear_combination

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_K10_moment_residual_certificate_target_result.json"

N=4000
DPS=180

def parity_modes(sector):
    return np.arange(1 if sector=="even-v" else 2,N+1,2,dtype=int)

def source_dd(modes):
    fh=np.empty(len(modes),dtype=LD)
    fl=np.empty(len(modes),dtype=LD)
    with mp.workdps(DPS):
        for i,n0 in enumerate(modes):
            n=mp.mpf(int(n0))
            k=n*mp.pi/2
            parity=mp.mpf(1 if int(n0)%2==0 else -1)
            f=k*(mp.e**(-1)-parity*mp.e)/(1+k*k)
            fh[i],fl[i]=split_mpf_ld(f)
    return fh,fl

def one_sector(sector):
    modes=parity_modes(sector)
    P,_=frozen_protected_basis(sector,modes)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,f=full_source_matrix(modes,sector)
    op,proj,gamma,evals,Y0,yf0,initial=build_double_complement(
        A,P,Gi,f,rtol=2e-14
    )

    data=hp_parity_data(
        modes,sector,dps=DPS,arch_terms=160,correction_terms=50
    )
    Yh=Y0.astype(LD); Yl=np.zeros_like(Yh,dtype=LD)
    yfh=yf0.astype(LD); yfl=np.zeros_like(yfh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)

    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,norms0=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Yh,Yl,yfh,yfl=refine_once(op,proj,Yh,Yl,yfh,yfl,Rh,Rl)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)

    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,norms1=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Kt=form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)

    with mp.workdps(DPS):
        S=Kt[:6,:6]
        g=-Kt[:6,6]
        h=-Kt[6,6]
        w=mp.lu_solve(S,g)
        G=h+(g.T*w)[0]
        C=1/G
        coeff=[w[j] for j in range(6)]+[mp.mpf(1)]
        xh,xl=dd_linear_combination(Uh,Ul,coeff)

    # Direct finite-row residual of reconstructed x.
    Axh,Axl=dd_matvec(data,xh[:,None],xl[:,None])
    Axh=Axh[:,0]; Axl=Axl[:,0]
    fh,fl=source_dd(modes)
    rrh,rrl=dd_sub(Axh,Axl,fh,fl)
    rnorm=dd_norm2(rrh,rrl)

    with mp.workdps(DPS):
        x=[ldd_to_mpf(xh[i],xl[i]) for i in range(len(modes))]
        z=[ldd_to_mpf(data.z_hi[i],data.z_lo[i]) for i in range(len(modes))]
        mm=[mp.mpf(int(m)) for m in modes]

        xnorm=mp.sqrt(mp.fsum(xx*xx for xx in x))
        Sz22=mp.fsum(abs(zz)*(m**22)*abs(xx)
                     for m,zz,xx in zip(mm,z,x))
        S23=mp.fsum((m**23)*abs(xx) for m,xx in zip(mm,x))

        weight23=mp.sqrt(mp.fsum(m**46 for m in mm))
        weightz22=mp.sqrt(mp.fsum((abs(zz)**2)*(m**44) for m,zz in zip(mm,z)))
        weightz22_zcap10=10*mp.sqrt(mp.fsum(m**44 for m in mm))

        # Source-vector magnitude and a direct high-precision source midpoint.
        fnorm=mp.sqrt(mp.fsum(
            (mp.mpf(int(n0))*mp.pi/2 *
             (mp.e**(-1)-mp.mpf(1 if int(n0)%2==0 else -1)*mp.e) /
             (1+(mp.mpf(int(n0))*mp.pi/2)**2))**2
            for n0 in modes
        ))

    row={
      "sector":sector,
      "dimension":len(modes),
      "capacity":mp.nstr(C,70),
      "sqrt_capacity":mp.nstr(mp.sqrt(C),60),
      "x_l2":mp.nstr(xnorm,60),
      "finite_source_residual_l2_ldd":rnorm,
      "joint_basis_residual_max_before":max(norms0),
      "joint_basis_residual_max_after":max(norms1),
      "S_z_22_midpoint":mp.nstr(Sz22,70),
      "S_23_midpoint":mp.nstr(S23,70),
      "weight_S23_l2":mp.nstr(weight23,70),
      "weight_Sz22_l2_midpoint_z":mp.nstr(weightz22,70),
      "weight_Sz22_l2_zcap10":mp.nstr(weightz22_zcap10,70),
      "source_l2":mp.nstr(fnorm,50),
      "complement_floor_midpoint_diagnostic":gamma,
    }
    print("\n",sector)
    for k,v in row.items():
        if k!="sector": print(k,"=",v)
    return row

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
      "N":N,
      "dps":DPS,
      "rows":rows,
      "guardrail":(
        "LDDD midpoint certificate target. Ledger must add exact-source "
        "operator/source and LDDD arithmetic radii before using residual/floor "
        "to enclose the exact source solution."
      ),
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
