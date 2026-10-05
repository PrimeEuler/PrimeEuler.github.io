#!/usr/bin/env python3
"""Final arithmetic envelope for the M8000, mu=1 protected 6x6 front.

This is the pre-cancellation version of the protected outward budget.

Public constants:
  u = 2^-64                      (x87 long-double unit roundoff)
  C_DD = 4096                    (primitive-chain + two-level accumulation cap)
  QCOMP_CAP = 32                 (pre-cancellation positive magnitude cap)
  ||R|| <= 1e-20                (very loose outward graph-residual cap)

The successful component-magnitude replay found Qcomp_max < 6.832 even and
< 2.421 odd, so QCOMP_CAP=32 has factors 4.68 and 13.2 headroom.

The scalar-to-operator radii come from the successful 420-digit all-mode
interval audit.  Complement floors are the theorem-level v14.029/v14.031
penalized-Cholesky floors.

The ledger supplies the proof of C_DD=4096 from error-free transformations:
two_sum and Dekker two_prod are exact (normal range), and all non-EFT
rounding occurs only on low components; a conservative primitive and
sequential-accumulation count is <4096*N*u^2 times the positive component
majorant.

Fail closed if either protected lower bound is nonpositive.
"""
from __future__ import annotations
import json, math
from pathlib import Path
from decimal import Decimal, getcontext

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_protected_outward_certificate_result.json"
getcontext().prec=80

N=4000
U=Decimal(2)**Decimal(-64)
C_DD=Decimal(4096)
QCOMP_CAP=Decimal(32)
RESIDUAL_CAP=Decimal("1e-20")
ZCAP=Decimal(10)
CCAP=Decimal(1)

SCALAR={
 "even-v":{
  "eps_z":Decimal("5.809110335412397e-39"),
  "eps_d":Decimal("3.0000001815446517e-32"),
  "eps_p":Decimal("7.365230177656668e-40"),
  "eps_c":Decimal("6.740593794183538e-42")},
 "odd-v":{
  "eps_z":Decimal("5.829046823471421e-39"),
  "eps_d":Decimal("7.500001658183785e-33"),
  "eps_p":Decimal("4.987119893996533e-41"),
  "eps_c":Decimal("6.740593794183538e-42")},
}
DELTA={
 "even-v":Decimal("7.795385618610192746e-6"),
 "odd-v":Decimal("3.262507025086259604e-5"),
}
PIVOT={
 "even-v":Decimal("5.695756110526945907914792675247768147491325089955846027732618793707184e-30"),
 "odd-v":Decimal("1.435697765205678076091228232724839810270536253531184899254363673675449e-26"),
}
WFROB2={
 "even-v":Decimal("6.001323151827835"),
 "odd-v":Decimal("6.009267708281584"),
}
QCOMP_MID={
 "even-v":Decimal("6.8314689507182935"),
 "odd-v":Decimal("2.419996208244608"),
}

def pnorm_cap(sector):
    if sector=="even-v":
        return Decimal(str(math.sqrt(2)*math.cosh(0.5)))
    return Decimal(str(4*math.sinh(0.5)/math.sqrt(24)))

def one(sector):
    e=SCALAR[sector]
    H=Decimal(9)  # H_3999 < 9
    edisp=H*((CCAP+e["eps_c"])*e["eps_z"]+e["eps_c"]*ZCAP)
    dp=Decimal(str(math.sqrt(N)))*e["eps_p"]
    epole=Decimal(2)*(Decimal(2)*pnorm_cap(sector)*dp+dp*dp)
    eop=e["eps_d"]+edisp+epole
    esource=eop*WFROB2[sector]

    eround=C_DD*Decimal(N)*(U*U)*QCOMP_CAP
    eres=(RESIDUAL_CAP*RESIDUAL_CAP)/DELTA[sector]
    etot=esource+eround+eres
    lower=PIVOT[sector]-etot

    return {
      "sector":sector,
      "exact_source_operator_radius":str(eop),
      "exact_source_form_radius":str(esource),
      "dd_rounding_radius":str(eround),
      "graph_residual_quadratic_radius":str(eres),
      "total_radius":str(etot),
      "midpoint_protected_min":str(PIVOT[sector]),
      "outward_protected_lower":str(lower),
      "fraction_remaining":str(lower/PIVOT[sector]),
      "Qcomp_mid":str(QCOMP_MID[sector]),
      "Qcomp_cap":str(QCOMP_CAP),
      "Qcomp_inflation":str(QCOMP_CAP/QCOMP_MID[sector]),
      "passes":bool(lower>0),
    }

def main():
    rows=[one("even-v"),one("odd-v")]
    if not all(r["passes"] for r in rows):
        raise RuntimeError(("protected certificate budget failed",rows))
    out={
      "N":N,
      "unit_roundoff":str(U),
      "C_DD":str(C_DD),
      "QCOMP_CAP":str(QCOMP_CAP),
      "RESIDUAL_CAP":str(RESIDUAL_CAP),
      "rows":rows,
    }
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    for r in rows:
        print("\n",r["sector"])
        print("source form =",r["exact_source_form_radius"])
        print("DD rounding =",r["dd_rounding_radius"])
        print("residual correction =",r["graph_residual_quadratic_radius"])
        print("midpoint =",r["midpoint_protected_min"])
        print("OUTWARD LOWER =",r["outward_protected_lower"])
        print("fraction remaining =",r["fraction_remaining"])
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
