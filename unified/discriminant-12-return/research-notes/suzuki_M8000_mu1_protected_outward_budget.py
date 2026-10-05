#!/usr/bin/env python3
"""Fail-closed outward budget for the M8000, mu=1 protected 6x6 block.

This script packages the theorem-scale inequalities needed after v14.031.

Inputs already certified/audited:
  * rigorous Euclidean complement floors delta_e, delta_o from v14.029/031;
  * 180-digit protected midpoint eigenvalues from the mu=1 LDDD graph replay;
  * all-4000-mode interval scalar representation radii from the successful
    fixed M8000 scalar interval audit;
  * analytic |z_n| <= 10 on all finite modes (a deliberately loose global
    version of the v14.025 digamma/prime/correction bound).

The exact source-faithful matrix has
  offdiag A_ij = c (z_i n_j - z_j n_i)/(n_i^2-n_j^2)
                  + alpha p_i p_j,
  diag    A_ii = d_i + alpha p_i^2.

For one parity lattice, |n_i-n_j|>=2|i-j| and hence the Schur row sum
from scalar representation errors is bounded by a harmonic sum.

The protected LDDD accumulation error is charged with the deliberately
conservative model

    E_DD <= C_DD * N * u^2 * QABS_CAP,

where u=2^-64, C_DD=32768, and QABS_CAP=4.  The audited midpoint positive
absolute-contribution sums are <1.95, so 4 is >2x inflation.  C_DD is a
large envelope for the error-free-transform primitive chains
(two_sum/Dekker two_prod plus the two sequential accumulations); the
associated proof obligation is recorded separately in the ledger entry.

The graph/Feshbach residual correction is charged with the intentionally
loose outward cap ||R||<=1e-20.  This is many orders above the observed
1e-27-class LDDD residuals and above the scalar/rounding action budgets,
but its quadratic correction is still negligible with the certified
complement floors.

This script is arithmetic packaging, not an independent source producer.
"""
from __future__ import annotations
import json, math
from pathlib import Path
from decimal import Decimal, getcontext

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_mu1_protected_outward_budget_result.json"

getcontext().prec=80

N=4000
U=Decimal(2) ** Decimal(-64)
C_DD=Decimal(32768)
QABS_CAP=Decimal(4)
RESIDUAL_CAP=Decimal("1e-20")

# Successful full 420-digit interval replay (run 37259189883).
SCALAR={
    "even-v":{
        "eps_z":Decimal("5.809110335412397e-39"),
        "eps_d":Decimal("3.0000001815446517e-32"),
        "eps_p":Decimal("7.365230177656668e-40"),
        "eps_c":Decimal("6.740593794183538e-42"),
    },
    "odd-v":{
        "eps_z":Decimal("5.829046823471421e-39"),
        "eps_d":Decimal("7.500001658183785e-33"),
        "eps_p":Decimal("4.987119893996533e-41"),
        "eps_c":Decimal("6.740593794183538e-42"),
    },
}

# v14.031 consumable Euclidean complement floors.
DELTA={
    "even-v":Decimal("7.795385618610192746e-6"),
    "odd-v":Decimal("3.262507025086259604e-5"),
}

# Protected midpoint eigenvalues from the successful mu=1 protected replay.
PIVOT={
    "even-v":Decimal(
        "5.695756110526945907914792675247768147491325089955846027732618793707184e-30"
    ),
    "odd-v":Decimal(
        "1.435697765205678076091228232724839810270536253531184899254363673675449e-26"
    ),
}

# ||W||_F^2 from the protected arithmetic budget.
WFROB2={
    "even-v":Decimal("6.001323151827835"),
    "odd-v":Decimal("6.009267708281584"),
}

# Positive-sum midpoint diagnostics; only used to check QABS_CAP inflation.
QABS_MID={
    "even-v":Decimal("1.743369069088472"),
    "odd-v":Decimal("1.9432706822225259"),
}

# Loose all-mode exact scalar bound.  The v14.025 formula is <9.18 at n=1.
ZCAP=Decimal(10)
CCAP=Decimal(1)  # exact 2/pi < 1

def harmonic(n:int)->Decimal:
    # Upward-safe public cap: H_3999 < 9.
    return Decimal(9)

def pole_l2_cap(sector:str)->Decimal:
    # p_n = 2 k g/(k^2+1/4) <= 4g/(pi n).
    # even-v uses odd n: sum odd 1/n^2 = pi^2/8 => ||p|| <= sqrt(2) cosh(1/2).
    # odd-v uses even n: sum even 1/n^2 = pi^2/24 => ||p|| <= 4 sinh(1/2)/sqrt(24).
    if sector=="even-v":
        return Decimal(str(math.sqrt(2)*math.cosh(0.5)))
    return Decimal(str(4*math.sinh(0.5)/math.sqrt(24)))

def sector_budget(sector:str):
    e=SCALAR[sector]
    H=harmonic(N-1)

    # Displacement/Cauchy representation error row sum:
    # delta q_ij <= eps_z / |n_i-n_j|;
    # |q_mid_ij| <= ZCAP / |n_i-n_j|.
    e_disp=H*((CCAP+e["eps_c"])*e["eps_z"] + e["eps_c"]*ZCAP)

    # Rank-one pole representation error:
    # |alpha|=2 in both sectors.
    pnorm=pole_l2_cap(sector)
    dpnorm=Decimal(str(math.sqrt(N)))*e["eps_p"]
    e_pole=Decimal(2)*(Decimal(2)*pnorm*dpnorm + dpnorm*dpnorm)

    e_op=e["eps_d"]+e_disp+e_pole
    e_source_form=e_op*WFROB2[sector]

    e_dd=C_DD*Decimal(N)*(U*U)*QABS_CAP
    e_res=(RESIDUAL_CAP*RESIDUAL_CAP)/DELTA[sector]

    total=e_source_form+e_dd+e_res
    lower=PIVOT[sector]-total

    return {
        "sector":sector,
        "harmonic_cap":str(H),
        "pole_l2_cap":str(pnorm),
        "pole_error_l2_cap":str(dpnorm),
        "displacement_operator_radius":str(e_disp),
        "pole_operator_radius":str(e_pole),
        "exact_source_operator_radius":str(e_op),
        "exact_source_protected_form_radius":str(e_source_form),
        "dd_rounding_radius":str(e_dd),
        "residual_quadratic_radius":str(e_res),
        "total_protected_radius":str(total),
        "midpoint_protected_min":str(PIVOT[sector]),
        "outward_protected_lower":str(lower),
        "fraction_of_midpoint_remaining":str(lower/PIVOT[sector]),
        "qabs_midpoint":str(QABS_MID[sector]),
        "qabs_cap":str(QABS_CAP),
        "qabs_inflation_factor":str(QABS_CAP/QABS_MID[sector]),
        "passes":bool(lower>0),
    }

def main():
    rows=[sector_budget("even-v"),sector_budget("odd-v")]
    out={
        "N":N,
        "unit_roundoff_longdouble":str(U),
        "C_DD":str(C_DD),
        "QABS_CAP":str(QABS_CAP),
        "RESIDUAL_CAP":str(RESIDUAL_CAP),
        "rows":rows,
        "guardrail":(
            "The numerical inequalities are fail-closed. Promotion additionally "
            "requires the ledger proof of the C_DD=32768 LDDD primitive-chain "
            "envelope and confirmation that the same stored P/graph vectors are "
            "used as in v14.031."
        ),
    }
    if not all(r["passes"] for r in rows):
        raise RuntimeError(("protected outward budget failed",rows))
    OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    for r in rows:
        print("\n",r["sector"])
        print("source operator radius =",r["exact_source_operator_radius"])
        print("source form radius =",r["exact_source_protected_form_radius"])
        print("DD rounding radius =",r["dd_rounding_radius"])
        print("residual quadratic radius =",r["residual_quadratic_radius"])
        print("protected midpoint =",r["midpoint_protected_min"])
        print("OUTWARD LOWER =",r["outward_protected_lower"])
        print("fraction remaining =",r["fraction_of_midpoint_remaining"])
    print("\nwrote",OUT)

if __name__=="__main__":
    main()
