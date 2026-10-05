#!/usr/bin/env python3
"""Adversarial check of the four-channel M=8000 far coupling near n=8000.

The v14.027/v14.033 far coupling uses the four channels
  w1/n + z_n w2/n^2 + w3/n^3 + z_n w4/n^4
for the finite shifted front m<=8000.

A geometric expansion in m/n is not uniformly small immediately above the
front because m/n -> 1.  This replay is intentionally triggered after the
workflow exists on the branch.  This diagnostic compares the exact source-faithful
coupling row with the four-channel approximation at selected same-parity far
modes.  It is intentionally a theorem-assumption audit, not a certificate.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_N4000_remote_coupling_moment_gram_ldd import channel_matrix_dd
from suzuki_ldd_source_operator import hp_parity_data_ld as hp_parity_data
from suzuki_endpoint_M3999_midpoint_effective_core import (
    pole_vector, z_source_faithful,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_fourchannel_near_boundary_check_result.json"
PI=np.pi
DPS=180

def one_sector(sector):
    _,modes,_,_,_=embedded_protected_basis(sector)
    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=160,correction_terms=50)
    Bh,Bl=channel_matrix_dd(data,modes,sector)
    W=np.asarray(Bh+Bl,dtype=float) # front x 4

    m=modes.astype(float)
    zm=z_source_faithful(m)
    pfin,alpha=pole_vector(m,sector)

    last=int(modes[-1])
    # Same-parity distances from the boundary, then separated factors.
    ns=[last+2,last+4,last+10,last+20,last+100,last+500,
        10001 if sector=="even-v" else 10002,
        12001 if sector=="even-v" else 12002,
        16001 if sector=="even-v" else 16002,
        24001 if sector=="even-v" else 24002,
        32001 if sector=="even-v" else 32002]
    rows=[]
    for n0 in ns:
        n=float(n0)
        zn=float(z_source_faithful(np.array([n]))[0])
        den=n*n-m*m
        exact=(2.0/PI)*(zn*m-n*zm)/den
        pn,_=pole_vector(np.array([n]),sector)
        exact=exact+alpha*float(pn[0])*pfin

        u=np.array([1/n,zn/n**2,1/n**3,zn/n**4])
        approx=W@u
        rem=exact-approx

        # Also K=10 Cauchy-only truncation to show convergence recovery.
        cauchy10=np.zeros_like(m)
        for k in range(11):
            cauchy10+=(2.0/PI)*(zn*m**(2*k+1)/n**(2*k+2)
                                -zm*m**(2*k)/n**(2*k+1))
        # Pole is exact here; four-channel pole approximation has only two terms.
        exact_c=(2.0/PI)*(zn*m-n*zm)/den
        rem_c10=exact_c-cauchy10

        row={
          "n":n0,
          "max_m_over_n":float(m[-1]/n),
          "exact_row_l2":float(np.linalg.norm(exact)),
          "four_channel_row_l2":float(np.linalg.norm(approx)),
          "remainder_row_l2":float(np.linalg.norm(rem)),
          "remainder_over_exact":float(np.linalg.norm(rem)/np.linalg.norm(exact)),
          "remainder_max_abs":float(np.max(np.abs(rem))),
          "cauchy_K10_remainder_l2":float(np.linalg.norm(rem_c10)),
          "cauchy_K10_remainder_over_exact_cauchy":float(
             np.linalg.norm(rem_c10)/np.linalg.norm(exact_c)
          ),
        }
        rows.append(row)
        print(sector,row)

    return {"sector":sector,"front_last_mode":last,"rows":rows}

def main():
    rows=[one_sector("even-v"),one_sector("odd-v")]
    out={
      "rows":rows,
      "guardrail":(
        "Diagnostic theorem-assumption audit only. A large near-boundary "
        "remainder means v14.027 section 6(c) requires a near/far split or "
        "an exact correlated treatment; it is not itself evidence against "
        "positivity of the true Schur complement."
      )
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("wrote",OUT)

if __name__=="__main__":
    main()
