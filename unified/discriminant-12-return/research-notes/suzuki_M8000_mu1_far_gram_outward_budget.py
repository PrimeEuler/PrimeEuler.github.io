#!/usr/bin/env python3
"""Fail-closed coarse outward budget for the M8000 mu=1 far four-channel Gram.

The raw four channel vectors are badly scaled, so the theorem consumer is the
weighted absolute budget

    Delta4 = sum_ij |M_ij| f_i f_j,

where f_i are rigorous far-lattice l2 norms of the scalar channels.

This script deliberately uses coarse public caps:
  * midpoint Delta4 from the high-precision shifted-front replay;
  * raw target residual <= 1e-6;
  * graph residual <= 1e-24;
  * scaled target norm <= 4;
  * complement floor = v14.031 theorem floor;
  * production-front global floor >= 3e-30 (even), 1e-26 (odd);
  * exact-source operator perturbation <= 3.01e-32 / 7.51e-33;
  * total production-computation additive allowance 0.15;
  * exact-source inverse inflation <= 1.02;
  * final public cap = 1.5 * midpoint Delta4.

The ledger derives each cap.  This script only performs the fail-closed
arithmetic and records the headroom.
"""
from decimal import Decimal, getcontext
import json
from pathlib import Path

getcontext().prec=60
HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_far_gram_outward_budget_result.json"

MID={
 "even-v":Decimal("1.2428000003133971099168903145159792109213780832571222956965"),
 "odd-v":Decimal("1.18697001357594196541848310141866452718068768961120512442902"),
}
RAW_SHIFTED={
 "even-v":Decimal("2.2867753186523356094"),
 "odd-v":Decimal("2.2869152822833307687"),
}
DELTA={
 "even-v":Decimal("7.795385618610192746e-6"),
 "odd-v":Decimal("3.262507025086259604e-5"),
}
GLOBAL_FLOOR={
 "even-v":Decimal("3e-30"),
 "odd-v":Decimal("1e-26"),
}
SOURCE_OP={
 "even-v":Decimal("3.01e-32"),
 "odd-v":Decimal("7.51e-33"),
}

RAW_TARGET_RESID=Decimal("1e-6")
FAR_NORM_MAX=Decimal("0.008")
GRAPH_RESID=Decimal("1e-24")
SCALED_TARGET_NORM=Decimal(4)
PRODUCTION_ADD=Decimal("0.15")
SOURCE_INFLATION=Decimal("1.02")
FINAL_FACTOR=Decimal("1.5")

def one(sec):
    # Scaled target residual and complement-energy Cauchy budget.
    r=RAW_TARGET_RESID*FAR_NORM_MAX
    sqrt_delta=DELTA[sec].sqrt()
    a=r/sqrt_delta
    sqrt_h=SCALED_TARGET_NORM/sqrt_delta
    h_entry_err=sqrt_h*a

    # Graph residual effects in the reduced protected data.
    ay=GRAPH_RESID/sqrt_delta
    S_err=ay*ay
    g_err=ay*sqrt_h

    theta=SOURCE_OP[sec]/GLOBAL_FLOOR[sec]
    inv_infl=Decimal(1)/(Decimal(1)-theta)

    # The theorem uses the coarser public 1.02 inflation and 0.15 additive cap.
    pre_source=MID[sec]+PRODUCTION_ADD
    coarse_exact=SOURCE_INFLATION*pre_source
    public=FINAL_FACTOR*MID[sec]
    margin=RAW_SHIFTED[sec]-public

    if not (inv_infl < SOURCE_INFLATION):
        raise RuntimeError((sec,"source inflation cap failed",inv_infl))
    if not (coarse_exact < public):
        raise RuntimeError((sec,"1.5x public cap does not dominate coarse budget",
                            coarse_exact,public))
    if not margin>0:
        raise RuntimeError((sec,"far Gram margin failed",margin))

    return {
      "sector":sec,
      "scaled_target_residual_cap":str(r),
      "target_complement_a":str(a),
      "single_h_entry_error_cap":str(h_entry_err),
      "graph_S_error_cap":str(S_err),
      "graph_g_error_norm_cap":str(g_err),
      "production_additive_budget":str(PRODUCTION_ADD),
      "global_front_floor_cap":str(GLOBAL_FLOOR[sec]),
      "source_operator_radius":str(SOURCE_OP[sec]),
      "source_relative_theta":str(theta),
      "source_inverse_inflation_exact_cap":str(inv_infl),
      "source_inverse_inflation_public":str(SOURCE_INFLATION),
      "midpoint_Delta4":str(MID[sec]),
      "coarse_exact_Delta4_before_public_rounding":str(coarse_exact),
      "public_Delta4_upper":str(public),
      "rigorous_shifted_raw_floor":str(RAW_SHIFTED[sec]),
      "margin_before_geometric_remainder":str(margin),
      "passes":True,
    }

def main():
    rows=[one("even-v"),one("odd-v")]
    out={"rows":rows}
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    for r in rows:
        print("\n",r["sector"])
        print("h-entry residual cap =",r["single_h_entry_error_cap"])
        print("source inverse inflation =",r["source_inverse_inflation_exact_cap"])
        print("coarse exact Delta4 =",r["coarse_exact_Delta4_before_public_rounding"])
        print("PUBLIC Delta4 <=",r["public_Delta4_upper"])
        print("MARGIN before geo =",r["margin_before_geometric_remainder"])
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
