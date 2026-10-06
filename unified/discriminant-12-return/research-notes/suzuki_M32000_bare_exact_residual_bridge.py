#!/usr/bin/env python3
"""Exact-source residual bridge for the N=32000 full-near bare solves.

Purpose
-------
Turn the audited FFT midpoint vectors from v14.093/v14.094 into theorem-grade
bare-solve residual caps without relying on FFT roundoff.

For each parity on the full octave N<n<=2N:
  1. solve the nominal stored-payload operator with the validated FFT route;
  2. recompute the nominal action independently by a chunked dense Cauchy
     matvec (no FFT);
  3. bound direct binary64 arithmetic with a conservative gamma envelope;
  4. compare the stored nominal scalar payload to the arch-200 LDDD payload;
  5. add the public exact-vs-LDDD scalar interval caps (through 64k once the
     incremental interval audit is promoted);
  6. convert scalar radii to an operator-norm radius;
  7. bound the exact-source residual.

Acceptance target from suzuki_M32000_bare_Smax_outward_budget.py:
    exact residual <= 5e-7 per sector.

This producer is an audit target until the through-64k scalar caps are
independently promoted.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import mpmath as mp
import numpy as np

from osc_full_near_fft_diagnostic import solve, N
from suzuki_remote_fft_matvec_validation import arch_diag_vector
from suzuki_endpoint_M3999_midpoint_effective_core import (
    cusp_diag, prime_diag, z_source_faithful, pole_vector,
)
from suzuki_ldd_source_operator import (
    hp_parity_data_ld as hp_parity_data,
    ldd_to_mpf,
)

J=16000
HI=64000
DPS=180
ARCH=200
CORR=50
R_CAP=5.0e-7
U=2.0**-53
ZMAX=10.0
CHUNK=64
# Stored exact-vs-LDDD public caps from the 32k package, intended to be
# transported through 64k by the parallel incremental interval replay.
CAPS={
 "even-v":{"z":5.88e-39,"d":4.318e-37,"p":7.366e-40,"c":6.741e-42},
 "odd-v":{"z":5.88e-39,"d":1.176e-38,"p":4.988e-41,"c":6.741e-42},
}
HERE=Path(__file__).resolve().parent
OUT=HERE/"M32000_bare_exact_residual_bridge_result.json"

def gamma(k):
    ku=k*U
    if ku>=1: raise RuntimeError(("gamma overflow",k))
    return ku/(1-ku)

def mp_ldd_array(hi,lo):
    return np.array(
        [np.longdouble(str(ldd_to_mpf(hi[i],lo[i]))) for i in range(len(hi))],
        dtype=np.longdouble,
    )

def direct_nominal_action(modes,z,diag,p,alpha,c,x):
    """Chunked dense action of the nominal stored-payload symmetric matrix.

    Also returns a positive majorant for every row's arithmetic sensitivity.
    """
    modes=np.asarray(modes,dtype=float)
    z=np.asarray(z,dtype=float)
    diag=np.asarray(diag,dtype=float)
    p=np.asarray(p,dtype=float)
    x=np.asarray(x,dtype=float)
    n=len(modes)
    y=np.empty(n,dtype=float)
    row_major_max=0.0
    pole_dot=float(p@x)
    pole_abs_dot=float(np.abs(p)@np.abs(x))
    mj=modes[None,:]
    zj=z[None,:]
    ax=np.abs(x)[None,:]

    for i0 in range(0,n,CHUNK):
        i1=min(i0+CHUNK,n)
        mi=modes[i0:i1,None]
        zi=z[i0:i1,None]
        den=mi*mi-mj*mj
        rr=np.arange(i1-i0)
        gg=np.arange(i0,i1)
        den[rr,gg]=1.0

        num=mj*zi-mi*zj
        K=c*num/den
        K[rr,gg]=0.0
        yy=K@x
        yy+=diag[i0:i1]*x[i0:i1]
        yy+=alpha*p[i0:i1]*pole_dot
        y[i0:i1]=yy

        # Positive operation majorant.  This bounds cancellation-free
        # numerator formation and the final row dot.
        kmag=abs(c)*(mj*np.abs(zi)+mi*np.abs(zj))/np.abs(den)
        kmag[rr,gg]=0.0
        maj=kmag@np.abs(x)
        maj+=np.abs(diag[i0:i1]*x[i0:i1])
        maj+=abs(alpha)*np.abs(p[i0:i1])*pole_abs_dot
        row_major_max=max(row_major_max,float(np.max(maj)))

    return y,row_major_max

def one(sector):
    if sector=="even-v":
        modes=N+1+2*np.arange(J,dtype=int)
    else:
        modes=N+2+2*np.arange(J,dtype=int)
    # Common paired source u_j=1/(32001+2j), also for odd sector.
    npaired=N+1+2*np.arange(J,dtype=int)
    u_exact_den=npaired.astype(float)
    u=1.0/u_exact_den

    x,mv,it,res_fft=solve(modes,sector,u)

    # Nominal stored payload used by the fast solve.
    z_nom=z_source_faithful(modes)
    d_nom=cusp_diag(modes)+prime_diag(modes)+arch_diag_vector(modes)
    p_nom,alpha=pole_vector(modes,sector)
    p_nom=np.asarray(p_nom,dtype=float)
    c_nom=2.0/math.pi

    y_dir,row_major=direct_nominal_action(
        modes,z_nom,d_nom,p_nom,float(alpha),c_nom,x
    )
    rdir=y_dir-u
    rdir_mid=float(np.linalg.norm(rdir))

    # Conservative direct-arithmetic envelope:
    # <= 64 primitive operations per kernel contribution plus a length-J dot.
    gdir=gamma(64+2*J)
    direct_round_l2=math.sqrt(J)*gdir*row_major + 1e-15

    # Arch-200 LDDD payload on the same high-mode octave.
    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=ARCH,correction_terms=CORR)
    z_ld=np.asarray(data.z_hi+data.z_lo,dtype=np.longdouble)
    d_ld=np.asarray(data.diag_hi+data.diag_lo,dtype=np.longdouble)
    p_ld=np.asarray(data.pole_hi+data.pole_lo,dtype=np.longdouble)
    c_ld=np.longdouble(data.c_hi+data.c_lo)

    # Treat nominal binary64 payload entries as exact stored numbers here.
    dz_store=float(np.max(np.abs(z_ld-z_nom.astype(np.longdouble))))
    dd_store=float(np.max(np.abs(d_ld-d_nom.astype(np.longdouble))))
    dp_store=float(np.max(np.abs(p_ld-p_nom.astype(np.longdouble))))
    dc_store=float(abs(c_ld-np.longdouble(c_nom)))

    cap=CAPS[sector]
    ez=dz_store+cap["z"]
    ed=dd_store+cap["d"]
    ep=dp_store+cap["p"]
    ec=dc_store+cap["c"]

    # Symmetric displacement operator row-sum bound.
    # Same-parity spacing is 2, and sum_{j!=i} 1/|n_i-n_j| <= H_{J-1}.
    Hcap=1.0+math.log(J)
    disp_op=(ec*ZMAX+abs(c_nom)*ez)*Hcap

    # Pole rank-one operator difference.
    dp_norm=math.sqrt(J)*ep
    pnorm=float(np.linalg.norm(p_nom))
    pole_op=abs(float(alpha))*(2.0*pnorm*dp_norm+dp_norm*dp_norm)

    eop=ed+disp_op+pole_op

    # RHS binary64 representation of exact 1/n.
    rhs_round=math.sqrt(J)*(U/(1-U))*float(np.max(np.abs(u)))

    exact_residual_upper=(
        rdir_mid+direct_round_l2+eop*float(np.linalg.norm(x))+rhs_round
    )

    row={
      "sector":sector,
      "dimension":J,
      "first_mode":int(modes[0]),
      "last_mode":int(modes[-1]),
      "fft_cg_iters":it,
      "fft_recomputed_residual":res_fft,
      "direct_nominal_residual_mid":rdir_mid,
      "direct_row_major_max":row_major,
      "direct_round_l2_cap":direct_round_l2,
      "stored_vs_ldd_max_z":dz_store,
      "stored_vs_ldd_max_diag":dd_store,
      "stored_vs_ldd_max_pole":dp_store,
      "stored_vs_ldd_two_over_pi":dc_store,
      "exact_vs_nominal_eps_z":ez,
      "exact_vs_nominal_eps_diag":ed,
      "exact_vs_nominal_eps_pole":ep,
      "exact_vs_nominal_eps_c":ec,
      "displacement_operator_radius":disp_op,
      "pole_operator_radius":pole_op,
      "total_exact_vs_nominal_operator_radius":eop,
      "solution_norm":float(np.linalg.norm(x)),
      "rhs_round_cap":rhs_round,
      "exact_source_residual_upper_target":exact_residual_upper,
      "public_residual_cap":R_CAP,
      "passes_residual_cap":exact_residual_upper<R_CAP,
      "guardrail":(
        "Consumes through-64k exact-vs-LDDD scalar caps; those caps must be "
        "promoted independently before this residual bridge is theorem input."
      ),
    }
    print(json.dumps(row,indent=2),flush=True)
    if not row["passes_residual_cap"]:
        raise RuntimeError(("bare exact residual bridge failed",row))
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=one(a.sector)
    OUT.write_text(json.dumps(row,indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
