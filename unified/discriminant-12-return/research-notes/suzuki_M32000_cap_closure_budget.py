#!/usr/bin/env python3
"""Audit-hardened closure budget for the M=32000 finite-section floor.

Consumes the completed refined-graph replay and deliberately enlarges every
remaining representation/numerical allowance before feeding the already
audited v14.085 stressed mu_32k consumer.

This is a promotion TARGET, not a theorem by itself.

Public hardening:
  * shear numerical reserve: 1e-4 absolute (vs ~1e-12 summation scale);
  * H_component operator-norm cap: 512;
  * Qcomp representation/source reserve: +1.0 absolute;
  * residual arithmetic stage constant: C_RES=32768 = 4*C_DD;
  * exact per-column residual cap remains 2e-25;
  * C_DD = 16*64*8 = 8192 from the explicit protected-form path count.

Fail closed unless all hardened caps survive and the v14.085 stressed
finite cumulative interval remains strictly negative.
"""
from __future__ import annotations
import math
from decimal import Decimal as D

import suzuki_M32000_mu_floor_outward_budget as base

N=16000
U=2.0**-64
NCOLS=6
CDD=16*64*8
CRES=4*CDD
HCOMP_NORM_CAP=512.0
WFROB2_CAP=8.0
RCOL_CAP=2.0e-25
SHEAR_NUMERIC_RESERVE=1.0e-4
QCOMP_REPRESENTATION_RESERVE=1.0

ROWS={
 "even-v":{
   "y_frob":0.03636979047186905,
   "w_frob":2.4497597354963134,
   "graph_residual_obs":1.1940024608359023e-27,
   "gamma":2.9606892578456873e-19,
   "qcomp_mid":6.831462611825016,
   "eop":1.0914650487773005e-36,
   "tau_cap":0.04,
 },
 "odd-v":{
   "y_frob":0.096280209978998,
   "w_frob":2.4513812185854738,
   "graph_residual_obs":6.546813560795987e-27,
   "gamma":2.170373029008779e-17,
   "qcomp_mid":2.4199994307658317,
   "eop":8.786870658639323e-38,
   "tau_cap":0.11,
 },
}

def one(sector):
    r=ROWS[sector]
    dy=math.sqrt(NCOLS)*RCOL_CAP/r["gamma"]

    tau_out=r["y_frob"]+dy+SHEAR_NUMERIC_RESERVE
    w_exact_frob_cap=r["w_frob"]+dy+SHEAR_NUMERIC_RESERVE
    w2_cap=w_exact_frob_cap*w_exact_frob_cap

    q_graph=HCOMP_NORM_CAP*(2*r["w_frob"]*dy+dy*dy)
    q_out=(r["qcomp_mid"]+q_graph+QCOMP_REPRESENTATION_RESERVE)

    # Residual evaluation: use a deliberately broad 64-stage path
    # (4 times the protected-form C_DD path) and Hcomp norm <=512.
    res_arith=CRES*N*(U*U)*HCOMP_NORM_CAP*math.sqrt(WFROB2_CAP)
    res_source=r["eop"]*math.sqrt(WFROB2_CAP)
    res_exact=r["graph_residual_obs"]+res_arith+res_source

    out={
      "sector":sector,
      "exact_graph_correction_frob_cap":dy,
      "hardened_tau_out":tau_out,
      "tau_public_cap":r["tau_cap"],
      "hardened_exact_W_frob_sq_cap":w2_cap,
      "Qcomp_mid_refined":r["qcomp_mid"],
      "Qcomp_graph_inflation_Hcap512":q_graph,
      "Qcomp_representation_reserve":QCOMP_REPRESENTATION_RESERVE,
      "Qcomp_hardened_out":q_out,
      "Qcomp_public_cap":12.0,
      "residual_observed_ldd":r["graph_residual_obs"],
      "residual_arithmetic_cap":res_arith,
      "residual_source_cap":res_source,
      "residual_exact_upper":res_exact,
      "residual_public_cap":RCOL_CAP,
    }
    checks={
      "tau":tau_out<r["tau_cap"],
      "Wfrob2":w2_cap<WFROB2_CAP,
      "Qcomp":q_out<12.0,
      "residual":res_exact<RCOL_CAP,
    }
    out["checks"]=checks
    if not all(checks.values()):
        raise RuntimeError(("hardened cap closure failed",out))
    return out

def main():
    print("C_DD =",CDD)
    print("C_RES =",CRES)
    if CDD!=8192 or CRES!=32768:
        raise RuntimeError(("stage count constants wrong",CDD,CRES))

    rows={s:one(s) for s in ("even-v","odd-v")}
    for s,r in rows.items():
        print("\n",s)
        for k,v in r.items(): print(k,"=",v)

    # Consume the existing audited stressed budget with r_col=2e-25.
    stress={s:base.sector_budget(s,base.RCOL_STRESS)
            for s in ("even-v","odd-v")}
    eta_e,eta_o,mid,W,lo,hi=base.shell_interval(
        stress["even-v"]["theta_32k"],
        stress["odd-v"]["theta_32k"],
    )
    cum_lo=base.BASE_4K16_LO+lo
    cum_hi=base.BASE_4K16_HI+hi

    print("\nSTRESSED CONSUMER")
    print("mu_even =",stress["even-v"]["mu_32k_lower"])
    print("mu_odd =",stress["odd-v"]["mu_32k_lower"])
    print("theta_even =",stress["even-v"]["theta_32k"])
    print("theta_odd =",stress["odd-v"]["theta_32k"])
    print("shell_interval =",lo,hi)
    print("cumulative_4k_32k =",cum_lo,cum_hi)

    if not (stress["even-v"]["mu_32k_lower"]>base.TARGET_MU
            and stress["even-v"]["theta_32k"]<base.THETA_E_MAX
            and hi<0 and cum_hi<0):
        raise RuntimeError("stressed finite sign flip failed")

    print("\nPASS: hardened cap closure target survives all reserves")

if __name__=="__main__":
    main()
