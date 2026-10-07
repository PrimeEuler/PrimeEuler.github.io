#!/usr/bin/env python3
"""Unified exact-source bare full-near QF certificate at N=128000.

This is the direct dyadic lift of the audited N=32000 certificate to the
full octave 128000<n<=256000.  It uses the same fail-closed architecture:
validated FFT candidate, independent chunked dense nominal action,
exact-vs-LDDD scalar inflation, 1000x stress, residual->solution control
through T_p^F >= I, exact Abel telescope, and |C_D|<=4.4.

The public scalar caps are the v14.058/v14.059 caps.  Their transport through
128k is checked independently by suzuki_M128000_scalar_interval_incremental_arch200.py.
No infinite-tail inference is made here.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

from osc_full_near_fft_multicutoff import solve
from suzuki_remote_fft_matvec_validation import arch_diag_vector
from suzuki_endpoint_M3999_midpoint_effective_core import (
    cusp_diag, prime_diag, z_source_faithful, pole_vector,
)
from suzuki_ldd_source_operator import hp_parity_data_ld as hp_parity_data
from suzuki_M32000_bare_exact_residual_bridge import (
    direct_nominal_action, gamma, CAPS, ZMAX, DPS, ARCH, CORR, U,
)

N=128000
J=64000
PUBLIC_RESIDUAL_CAP=1.0e-9
STRESS=1000.0
TARGET=1.0e-8
CD_ABS_CAP=4.4

HERE=Path(__file__).resolve().parent
OUT=HERE/"M128000_bare_fullnear_outward_certificate_result.json"

def certified_candidate(sector):
    if sector=="even-v":
        modes=N+1+2*np.arange(J,dtype=int)
    else:
        modes=N+2+2*np.arange(J,dtype=int)
    paired=N+1+2*np.arange(J,dtype=int)
    u=1.0/paired.astype(float)

    x,mv,it,res_fft=solve(modes,sector,u)

    z_nom=z_source_faithful(modes)
    d_nom=cusp_diag(modes)+prime_diag(modes)+arch_diag_vector(modes)
    p_nom,alpha=pole_vector(modes,sector)
    p_nom=np.asarray(p_nom,dtype=float)
    c_nom=2.0/math.pi

    y_dir,row_major=direct_nominal_action(
        modes,z_nom,d_nom,p_nom,float(alpha),c_nom,x
    )
    rdir_mid=float(np.linalg.norm(y_dir-u))

    gdir=gamma(64+2*J)
    direct_round_l2=math.sqrt(J)*gdir*row_major+1e-15

    data=hp_parity_data(
        modes,sector,dps=DPS,arch_terms=ARCH,correction_terms=CORR
    )
    z_ld=np.asarray(data.z_hi+data.z_lo,dtype=np.longdouble)
    d_ld=np.asarray(data.diag_hi+data.diag_lo,dtype=np.longdouble)
    p_ld=np.asarray(data.pole_hi+data.pole_lo,dtype=np.longdouble)
    c_ld=np.longdouble(data.c_hi+data.c_lo)

    dz_store=float(np.max(np.abs(z_ld-z_nom.astype(np.longdouble))))
    dd_store=float(np.max(np.abs(d_ld-d_nom.astype(np.longdouble))))
    dp_store=float(np.max(np.abs(p_ld-p_nom.astype(np.longdouble))))
    dc_store=float(abs(c_ld-np.longdouble(c_nom)))

    cap=CAPS[sector]
    ez=dz_store+cap["z"]
    ed=dd_store+cap["d"]
    ep=dp_store+cap["p"]
    ec=dc_store+cap["c"]

    Hcap=1.0+math.log(J)
    disp_op=(ec*ZMAX+(abs(c_nom)+ec)*ez)*Hcap

    dp_norm=math.sqrt(J)*ep
    pnorm=float(np.linalg.norm(p_nom))
    pole_op=abs(float(alpha))*(2.0*pnorm*dp_norm+dp_norm*dp_norm)
    eop=ed+disp_op+pole_op

    rhs_round=math.sqrt(J)*(U/(1-U))*float(np.max(np.abs(u)))

    raw_bound=rdir_mid+direct_round_l2+eop*float(np.linalg.norm(x))+rhs_round
    stressed=STRESS*raw_bound

    row={
      "sector":sector,
      "candidate":x,
      "fft_cg_iters":it,
      "fft_recomputed_residual":res_fft,
      "direct_nominal_residual_mid":rdir_mid,
      "direct_round_l2_cap":direct_round_l2,
      "stored_vs_ldd_max_z":dz_store,
      "stored_vs_ldd_max_diag":dd_store,
      "stored_vs_ldd_max_pole":dp_store,
      "stored_vs_ldd_two_over_pi":dc_store,
      "exact_vs_nominal_operator_radius":eop,
      "solution_norm":float(np.linalg.norm(x)),
      "rhs_round_cap":rhs_round,
      "unstressed_exact_residual_upper":raw_bound,
      "stress_factor":STRESS,
      "stressed_exact_residual_upper":stressed,
      "public_residual_cap":PUBLIC_RESIDUAL_CAP,
      "passes_residual_cap":stressed<PUBLIC_RESIDUAL_CAP,
    }
    if not row["passes_residual_cap"]:
        raise RuntimeError(("stressed exact residual failed",sector,row))
    return row

def main():
    e=certified_candidate("even-v")
    o=certified_candidate("odd-v")

    d=e["candidate"]-o["candidate"]
    Smax_cand=float(np.max(np.abs(np.cumsum(d))))

    S_error=math.sqrt(J)*(PUBLIC_RESIDUAL_CAP+PUBLIC_RESIDUAL_CAP)
    Smax_out=Smax_cand+S_error

    n0=N+1
    nlast=N+1+2*(J-1)
    u_last=1.0/nlast
    sum_du=1.0/n0-1.0/nlast
    abel_coeff=u_last+sum_du
    q_linear=Smax_out*abel_coeff

    u2_bound=1.0/n0**2 + 0.5*(1.0/n0-1.0/nlast)
    q_rank=CD_ABS_CAP*u2_bound*u2_bound
    q_total=q_linear+q_rank

    out={
      "N":N,
      "J":J,
      "even":{k:v for k,v in e.items() if k!="candidate"},
      "odd":{k:v for k,v in o.items() if k!="candidate"},
      "candidate_Smax":Smax_cand,
      "public_solution_error_each":PUBLIC_RESIDUAL_CAP,
      "partial_sum_error_cap":S_error,
      "exact_Smax_outward":Smax_out,
      "abel_u_last":u_last,
      "abel_sum_du_exact":sum_du,
      "abel_coefficient":abel_coeff,
      "abel_expected_1_over_n0":1.0/n0,
      "linear_inner_product_bound":q_linear,
      "u_norm_squared_bound":u2_bound,
      "C_D_abs_public_cap":CD_ABS_CAP,
      "rank_one_term_bound":q_rank,
      "exact_bare_Rosc_qf_bound":q_total,
      "public_qf_target":TARGET,
      "qf_headroom_factor":TARGET/q_total,
      "guardrail":"Consumes through-256k scalar-cap transport; no infinite-tail inference.",
    }
    checks={
      "even_residual":e["passes_residual_cap"],
      "odd_residual":o["passes_residual_cap"],
      "abel_telescopes":abs(abel_coeff-1.0/n0)<1e-20,
      "qf_target":q_total<TARGET,
    }
    out["checks"]=checks
    print(json.dumps(out,indent=2),flush=True)
    if not all(checks.values()):
        raise RuntimeError(("M128000 bare full-near certificate failed",checks))
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("PASS: M128000 exact-source bare full-near QF certificate target")

if __name__=="__main__":
    main()
