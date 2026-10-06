#!/usr/bin/env python3
"""Adversarial hardening of the M32000 bare exact-source residual bridge.

Consumes the completed bridge outputs and multiplies BOTH:
  * direct binary64 action-rounding charge;
  * exact-vs-nominal operator-radius contribution;
by 1000 before comparing with the public residual cap 1e-9.

This is intentionally much broader than any known arithmetic ambiguity.
"""
STRESS=1000.0
RCAP=1.0e-9
ROWS={
 "even-v":{
   "direct_res":2.4857283933833366e-15,
   "direct_round":5.480001385370464e-14,
   "eop":8.448739206095237e-10,
   "xnorm":0.00031334010019573756,
   "rhs":4.388404698074063e-19,
 },
 "odd-v":{
   "direct_res":2.532056738262667e-15,
   "direct_round":5.759611541467941e-14,
   "eop":8.713058606002403e-10,
   "xnorm":0.00031344907296467807,
   "rhs":4.388404698074063e-19,
 },
}

for sector,r in ROWS.items():
    hard=(
      r["direct_res"]
      + STRESS*r["direct_round"]
      + STRESS*r["eop"]*r["xnorm"]
      + STRESS*r["rhs"]
    )
    print(sector)
    print("stress_factor =",STRESS)
    print("hardened_exact_residual =",hard)
    print("public_cap =",RCAP)
    print("headroom =",RCAP/hard)
    ok=hard<RCAP
    print("PASS =",ok)
    if not ok:
        raise RuntimeError((sector,"1000x residual hardening failed",hard))
print("PASS: both sectors survive 1000x arithmetic/operator-radius stress")
