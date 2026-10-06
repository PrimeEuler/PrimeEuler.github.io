#!/usr/bin/env python3
"""Common-mode exact-source sensitivity of the N=4000/M=8000 capacity ratio.

The independent exact-source capacity radius (~3.9e-6 even) is deliberately
too pessimistic for the near-shell ratio C_N/C_M because the same scalar
producer errors act on the shared retained block.

For represented arch-200 operators, reconstruct the LDDD variational source
solutions x_N and x_M and evaluate the first variation

  d log C = (x^T dA x - 2 x^T df)/G,  G=f^T A^{-1} f.

For base modes, subtract the N and M sensitivities BEFORE absolute values.
For shell modes only the M sensitivity remains.

Scalar variables:
  d_n, z_n, pole p_n, common c=2/pi, source f_n.
Uniform outward scalar radii are taken from the successful 420-digit arch-200
audit.  This script reports the resulting first-order absolute bound on

  d log(C_N/C_M).

The nonlinear remainder is separately budgeted from the certified global
relative operator radius theta=eps/(mu-eps): Neumann expansion gives an
O(theta^2/(1-theta)) remainder for each log-energy.  The script reports the
conservative sum of the N and M remainders.

Diagnostic/certificate target: the midpoint source solutions are LDDD
variational reconstructions.  A final theorem wrapper must also charge their
small residual-energy defect when evaluating the first-order sensitivity.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,full_source_matrix,
)
from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,dd_project,form_Ktilde,form_trial,
    mp_inverse_split,refine_once,residuals_dd,
)
from suzuki_ldd_remote_source_lead_diagnostic import dd_linear_combination
from suzuki_ldd_source_operator import (
    LD,dot_columns as dd_dot_columns,hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_M8000_capacity_ratio_source_sensitivity_result.json"
DPS=180
ARCH=200
NMAX=4000
MMAX=8000
CHUNK=160

SCALAR={
 "even-v":{"ez":5.809110335412397e-39,"ed":4.317700732362615e-37,
           "ep":7.365230177656668e-40,"ec":6.740593794183538e-42,
           "theta":3.8992701466513013e-6},
 "odd-v":{"ez":5.829046823471421e-39,"ed":1.172753572346704e-38,
          "ep":4.987119893996533e-41,"ec":6.740593794183538e-42,
          "theta":9.692586810135521e-11},
}
U=float(2.0**-64)
EF=U*U*1.55/(1-U)

def modes_for(sector,maxmode):
    return np.arange(1 if sector=="even-v" else 2,maxmode+1,2,dtype=int)

def state(sector,maxmode):
    modes=modes_for(sector,maxmode)
    if maxmode==NMAX:
        P,_=frozen_protected_basis(sector,modes)
    elif maxmode==MMAX:
        _,m2,P,_,_=embedded_protected_basis(sector)
        if not np.array_equal(modes,m2): raise RuntimeError("mode mismatch")
    else:
        raise ValueError(maxmode)

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])
    A,f=full_source_matrix(modes,sector)
    op,proj,gamma,evals,Y0,yf0,initial=build_double_complement(
        A,P,Gi,f,rtol=2e-14
    )
    data=hp_parity_data(
        modes,sector,dps=DPS,arch_terms=ARCH,correction_terms=50
    )
    Yh=Y0.astype(LD);Yl=np.zeros_like(Yh,dtype=LD)
    yfh=yf0.astype(LD);yfl=np.zeros_like(yfh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)

    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n0=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Yh,Yl,yfh,yfl=refine_once(op,proj,Yh,Yl,yfh,yfl,Rh,Rl)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)
    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n1=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    K=form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)
    with mp.workdps(DPS):
        S=K[:6,:6];g=-K[:6,6];h=-K[6,6]
        w=mp.lu_solve(S,g)
        G=h+(g.T*w)[0]
        C=1/G
        coeffs=[w[j] for j in range(6)]+[mp.mpf(1)]
    xh,xl=dd_linear_combination(Uh,Ul,coeffs)
    x=np.asarray(xh+xl,dtype=np.longdouble)
    z=np.asarray(data.z_hi+data.z_lo,dtype=np.longdouble)
    p=np.asarray(data.pole_hi+data.pole_lo,dtype=np.longdouble)
    c=np.longdouble(data.c_hi+data.c_lo)
    return {
      "modes":modes,"x":x,"z":z,"p":p,"c":c,
      "alpha":float(data.alpha),"G":float(G),"C":float(C),
      "joint_residual_max":max(n1),"gamma_mid":gamma,
    }

def gradients(st):
    n=np.asarray(st["modes"],dtype=np.longdouble)
    x=st["x"];z=st["z"];p=st["p"];c=st["c"]
    G=np.longdouble(st["G"])
    gd=x*x/G
    gp=np.longdouble(2*st["alpha"])*(np.dot(p,x))*x/G
    gf=-2*x/G
    gz=np.empty(len(n),dtype=np.longdouble)
    disp_energy=np.longdouble(0)

    # z gradient and displacement energy in chunks.
    for a in range(0,len(n),CHUNK):
        b=min(a+CHUNK,len(n))
        ni=n[a:b,None]
        den=ni*ni-n[None,:]*n[None,:]
        rows=np.arange(a,b)
        den[np.arange(b-a),rows]=np.longdouble(np.inf)
        kern=n[None,:]/den
        sums=kern@x
        gz[a:b]=2*c*x[a:b]*sums/G

        Arows=c*(z[a:b,None]*n[None,:]-ni*z[None,:])/den
        Arows[np.arange(b-a),rows]=0
        disp_energy += np.dot(x[a:b],Arows@x)

    gc=disp_energy/(c*G)
    return {"d":gd,"p":gp,"f":gf,"z":gz,"c":gc}

def combine(gN,gM,nN):
    out={}
    for k in ("d","p","f","z"):
        diff=np.empty(len(gM[k]),dtype=np.longdouble)
        diff[:nN]=gN[k]-gM[k][:nN]
        diff[nN:]=-gM[k][nN:]
        out[k]=diff
    out["c"]=gN["c"]-gM["c"]
    return out

def one(sector):
    print("building N",sector,flush=True)
    N=state(sector,NMAX)
    print("building M",sector,flush=True)
    M=state(sector,MMAX)
    print("gradients",sector,flush=True)
    gN=gradients(N);gM=gradients(M)
    dg=combine(gN,gM,len(N["modes"]))
    e=SCALAR[sector]
    terms={
      "diag":float(np.sum(np.abs(dg["d"]),dtype=np.longdouble)*e["ed"]),
      "z":float(np.sum(np.abs(dg["z"]),dtype=np.longdouble)*e["ez"]),
      "pole":float(np.sum(np.abs(dg["p"]),dtype=np.longdouble)*e["ep"]),
      "source_split":float(np.sum(np.abs(dg["f"]),dtype=np.longdouble)*EF),
      "two_over_pi":float(abs(dg["c"])*e["ec"]),
    }
    first=sum(terms.values())

    theta=e["theta"]
    # Safe coarse log-remainder envelope for two cutoffs.  For |h|<=theta,
    # inverse Neumann remainder is <=theta^2/(1-theta); convert to log with
    # another factor 2 for generous headroom and sum N+M.
    nonlinear=4*theta*theta/(1-theta)

    eta=N["C"]/M["C"]-1
    row={
      "sector":sector,
      "C_N_mid":N["C"],"C_M_mid":M["C"],"eta_mid":eta,
      "first_order_components":terms,
      "first_order_log_ratio_abs_bound":first,
      "nonlinear_log_ratio_abs_bound":nonlinear,
      "total_log_ratio_source_bound_diagnostic":first+nonlinear,
      "eta_absolute_source_bound_diagnostic":(1+eta)*(np.exp(first+nonlinear)-1),
      "N_joint_residual_max":N["joint_residual_max"],
      "M_joint_residual_max":M["joint_residual_max"],
      "theta_global":theta,
      "source_split_uniform_radius":EF,
      "guardrail":(
        "First-order gradients use refined LDDD trial solutions. Final outward "
        "promotion must charge the trial-vs-exact source-solution energy defect; "
        "the nonlinear operator remainder is already budgeted separately."
      ),
    }
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=one(a.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
