#!/usr/bin/env python3
"""Analytic cross-octave operator cap for v14.128.

For same-parity old modes m<=R and new modes R<n<=2R,

 (2/pi)(z_n m - n z_m)/(n^2-m^2)
 = (1/pi)[(z_n-z_m)/(n-m) - (z_n+z_m)/(n+m)].

With |z|<=ZCAP, row and column sums are bounded by
 (2 ZCAP/pi) [ 1/2 H_M + 1/2 ],
M<=R/2, using same-parity spacing 2 and the crude bound
sum 1/(n+m) <= 1/2.

The pole cross block is rank one and is bounded analytically from
|p(n)| <= 4 cosh(1/2)/(pi n), |alpha|<=2.

FAIL CLOSED unless the total analytic cap is < 128 for R=64k and 128k.
"""
from __future__ import annotations
import json,math
import numpy as np
from suzuki_endpoint_M3999_midpoint_effective_core import z_source_faithful

ZCAP=16.0
PUBLIC_CAP=128.0

def one(R):
    M=R//2
    Hcap=1.0+math.log(M)
    cauchy=(2.0*ZCAP/math.pi)*(0.5*Hcap+0.5)

    h=math.cosh(0.5)
    # All-integer old sum: sum 1/n^2 <= pi^2/6.
    p_old=(4*h/math.pi)*math.sqrt(math.pi**2/6.0)
    # All-integer tail: sum_{n>R}1/n^2 <= 2/R.
    p_new=(4*h/math.pi)*math.sqrt(2.0/R)
    pole=2.0*p_old*p_new

    total=cauchy+pole

    # Finite source-formula sanity check with enormous margin to ZCAP.
    modes=np.arange(1,2*R+1,dtype=int)
    zmax=float(np.max(np.abs(z_source_faithful(modes))))
    return {
      "R":R,
      "ZCAP":ZCAP,
      "nominal_zmax_through_2R":zmax,
      "harmonic_cap":Hcap,
      "cauchy_cross_operator_cap":cauchy,
      "pole_cross_operator_cap":pole,
      "total_cross_operator_cap":total,
      "public_cross_cap":PUBLIC_CAP,
      "passes_zcap":zmax<ZCAP,
      "passes_cross_cap":total<PUBLIC_CAP,
      "headroom_factor":PUBLIC_CAP/total,
    }

def main():
    rows=[one(64000),one(128000)]
    print(json.dumps(rows,indent=2))
    if not all(r["passes_zcap"] and r["passes_cross_cap"] for r in rows):
        raise RuntimeError(rows)

if __name__=="__main__":
    main()
