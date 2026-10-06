#!/usr/bin/env python3
"""Common-mode arch-200 source sensitivity of C_8000/C_16000.

This is the outer-finite analogue of
suzuki_N4000_M8000_capacity_ratio_source_sensitivity.py.

Both cutoffs use the identical frozen N=4000 six-plane, zero-extended.
Base-mode sensitivity gradients are subtracted before absolute values.
Only M=16000 shell gradients remain unmatched.

The scalar radii below are provisionally copied from the successful M=8000
arch-200 audit.  Promotion requires the M=16000 interval replay to confirm
that these radii remain valid through 16000.
"""
from __future__ import annotations
import argparse,json,gc
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,full_source_matrix,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,dd_project,form_Ktilde,form_trial,
    mp_inverse_split,refine_once,residuals_dd,
)
from suzuki_ldd_remote_source_lead_diagnostic import dd_linear_combination
from suzuki_ldd_source_operator import (
    LD,dot_columns as dd_dot_columns,hp_parity_data_ld as hp_parity_data,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_M16000_capacity_ratio_source_sensitivity_result.json"
DPS=180
ARCH=200
BASE=4000
A_CUT=8000
B_CUT=16000
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

def embedded_P(sector,modes):
    base_modes=modes_for(sector,BASE)
    Pbase,_=frozen_protected_basis(sector,base_modes)
    if not np.array_equal(modes[:len(base_modes)],base_modes):
        raise RuntimeError("base prefix mismatch")
    P=np.zeros((len(modes),6),dtype=float)
    P[:len(base_modes)]=Pbase
    return P

def state(sector,maxmode):
    modes=modes_for(sector,maxmode)
    P=embedded_P(sector,modes)
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
    ret={
      "modes":modes,"x":x,"z":z,"p":p,"c":c,
      "alpha":float(data.alpha),"G":float(G),"C":float(C),
      "joint_residual_max":max(n1),"gamma_mid":gamma,
    }
    del A,f,data,Y0,yf0,Yh,Yl,yfh,yfl,Uh,Ul,AUh,AUl,Rh,Rl
    gc.collect()
    return ret

def gradients(st):
    n=np.asarray(st["modes"],dtype=np.longdouble)
    x=st["x"];z=st["z"];p=st["p"];c=st["c"]
    G=np.longdouble(st["G"])
    gd=x*x/G
    gp=np.longdouble(2*st["alpha"])*(np.dot(p,x))*x/G
    gf=-2*x/G
    gz=np.empty(len(n),dtype=np.longdouble)
    disp_energy=np.longdouble(0)
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

def combine(gA,gB,nA):
    out={}
    for k in ("d","p","f","z"):
        diff=np.empty(len(gB[k]),dtype=np.longdouble)
        diff[:nA]=gA[k]-gB[k][:nA]
        diff[nA:]=-gB[k][nA:]
        out[k]=diff
    out["c"]=gA["c"]-gB["c"]
    return out

def one(sector):
    print("building A",sector,flush=True)
    A=state(sector,A_CUT)
    print("building B",sector,flush=True)
    B=state(sector,B_CUT)
    print("gradients",sector,flush=True)
    gA=gradients(A);gB=gradients(B)
    dg=combine(gA,gB,len(A["modes"]))
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
    nonlinear=4*theta*theta/(1-theta)
    eta=A["C"]/B["C"]-1
    row={
      "sector":sector,
      "C_8000_mid":A["C"],"C_16000_mid":B["C"],"eta_mid":eta,
      "first_order_components":terms,
      "first_order_log_ratio_abs_bound_provisional":first,
      "nonlinear_log_ratio_abs_bound_provisional":nonlinear,
      "total_log_ratio_source_bound_provisional":first+nonlinear,
      "eta_absolute_source_bound_provisional":(1+eta)*(np.exp(first+nonlinear)-1),
      "A_joint_residual_max":A["joint_residual_max"],
      "B_joint_residual_max":B["joint_residual_max"],
      "theta_global_provisional":theta,
      "guardrail":(
        "M16000 scalar interval audit pending. Values are certificate targets "
        "only until its uniform radii are confirmed."
      )
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
