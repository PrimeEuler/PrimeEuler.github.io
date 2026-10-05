#!/usr/bin/env python3
"""Fail-closed public budget for the v14.041 near/far closure inequality.

This script packages conservative outward caps from already certified/audited
ingredients plus deliberately loose validated-computation padding.

Inputs
------
1. Rigorous raw shifted near floors from the N8000 interval certificate:
     even  > 2.9800144235164838
     odd   > 2.9800844016128788

2. Rank-24 correlation-preserving near self-energy producer:
     midpoint btotal_e = 0.28960718078470812
     midpoint btotal_o = 0.25578087637545165
   The audited exact-front passage from v14.033 allows a common 1.02
   quadratic-form inflation.  We then add an intentionally large 0.005
   production/SVD/source-formation allowance.  This yields public caps
     b_nn <= 0.31 (even), <= 0.27 (odd).

3. Raw near-to-sep cross diagnostic:
     explicit low-rank core + near SVD residual
       even = 0.9772424085368333
       odd  = 0.8437524725666780
   We add:
     * 0.02 public source/arithmetic padding.  This is far larger than the
       arithmetic padding consumed by the historical validated N=16003 cross
       certificate and the source-primitive radii already certified through
       the M=16001 pipeline.
     * 2e-6 for the omitted r^16 geometric piece on 32000<=n<1e6.
       Analytically, with |z|<=8 and m/n<=1/2,
         ||R_geom||_HS
         <= (64/(3*pi))[
              sqrt(sum m^34 * sum n^-36)
             +sqrt(sum m^32 * sum n^-34)]
         < 1.64e-6
       in both parities; 2e-6 is the public cap.
     * 0.230 for n>=1e6, obtained without midpoint z-values:
       use |z_m|<=8, exact pole envelope p_m<=4g/(pi m), and the same-parity
       power-sum integral bound.  The resulting lead+remainder is <0.2295.
   Hence public caps
       d_sn <= 1.25 (even), <= 1.20 (odd).

4. v14.041 separated-tail constants:
       Delta_sep <= 0.941, delta_ss = 1.3457.

Closure
-------
Let
    delta_nn >= raw_shifted_floor - b_nn
because the exact near self-energy is PSD with norm <= b_nn.
Check
    (d_sn + sqrt(0.941*b_nn))^2 < 1.3457*delta_nn.

If both sectors pass, the v14.041 conditional theorem closes numerically under
the stated outward-computation model.

Guardrail: promotion to ledger theorem still requires an audit of the two public
padding statements (0.005 near-selfenergy production allowance, 0.02 cross-core
validated-computation/source allowance).  The analytic floor, geometric and
far-tail pieces are fail-closed here.
"""
from decimal import Decimal, getcontext
getcontext().prec=80

SEP=Decimal("0.941")
DELTA_SS=Decimal("1.3457")

RAW={
 "even-v":Decimal("2.9800144235164838344255497958502698405515830618064322637032474"),
 "odd-v": Decimal("2.9800844016128788245878489826868739531964458586210016061468578"),
}
B_MID={
 "even-v":Decimal("0.289607180784708112390439338549360259572108199937983796851841"),
 "odd-v": Decimal("0.255780876375451641329086958234398605822147124885910691527788"),
}
B_CAP={"even-v":Decimal("0.31"),"odd-v":Decimal("0.27")}

CROSS_CORE={
 "even-v":Decimal("0.9772424085368333"),
 "odd-v": Decimal("0.8437524725666780"),
}
CORE_PAD=Decimal("0.02")
GEOM_CAP=Decimal("0.000002")
FAR_CAP=Decimal("0.230")
D_CAP={"even-v":Decimal("1.25"),"odd-v":Decimal("1.20")}

FRONT_INFLATION=Decimal("1.02")
B_PROD_PAD=Decimal("0.005")

def sqrtD(x):
    return x.sqrt()

def one(sector):
    bcheck=FRONT_INFLATION*B_MID[sector]+B_PROD_PAD
    if not bcheck < B_CAP[sector]:
        raise RuntimeError((sector,"b cap failed",bcheck,B_CAP[sector]))
    dcheck=CROSS_CORE[sector]+CORE_PAD+GEOM_CAP+FAR_CAP
    if not dcheck < D_CAP[sector]:
        raise RuntimeError((sector,"d cap failed",dcheck,D_CAP[sector]))
    delta=RAW[sector]-B_CAP[sector]
    lhs=(D_CAP[sector]+sqrtD(SEP*B_CAP[sector]))**2
    rhs=DELTA_SS*delta
    if not lhs<rhs:
        raise RuntimeError((sector,"v14.041 closure failed",lhs,rhs))
    return {
      "sector":sector,
      "b_production_check":str(bcheck),
      "b_public_cap":str(B_CAP[sector]),
      "cross_production_check":str(dcheck),
      "d_sn_public_cap":str(D_CAP[sector]),
      "delta_nn_lower":str(delta),
      "closure_lhs_upper":str(lhs),
      "closure_rhs_lower":str(rhs),
      "closure_margin_lower":str(rhs-lhs),
      "closure_ratio_upper":str(lhs/rhs),
    }

def main():
    rows=[one("even-v"),one("odd-v")]
    for r in rows:
        print("\n",r["sector"])
        for k,v in r.items():
            if k!="sector": print(k,"=",v)
    print("\nPASS: v14.041 closure inequality passes in both parities")
    print("GUARDRAIL: audit public numerical padding before theorem promotion.")

if __name__=="__main__":
    main()
