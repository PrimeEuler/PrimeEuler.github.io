#!/usr/bin/env python3
"""Exact-source perturbation budget for arch-200 N=4000/M=8000 capacities.

This isolates ONLY the exact-source representation uncertainty; it does not
claim the LDDD finite-arithmetic capacity bracket is outward yet.

Inputs already theorem-level / interval-certified:
  * v14.034 exact M=8000 shifted-front protected graph lower bounds;
  * v14.031 complement floors;
  * v14.034 public graph-coordinate allowance ||B-I|| <= 1e-12 and
    residual cap ||R|| <= 1e-20;
  * v14.034 graph Frobenius norms;
  * successful arch-200 420-digit scalar interval audit through mode 8000.

From the graph-Schur factorization,
    F = T^* diag(S,D) T,
and a conservative shear bound gives a global Euclidean floor for the exact
M=8000 shifted front.  Since A_M = F + Pi_shell >= F and A_N is the retained
principal compression of F, the same floor applies to exact A_N and A_M.

If ||A_exact-A_rep|| <= eps and A_exact >= mu I, then
    A_rep >= (mu-eps) I
and with theta=eps/(mu-eps),
    (1-theta) A_rep <= A_exact <= (1+theta) A_rep.
Hence capacities with the same source inherit the same relative bracket.
The two-longdouble source split error is bounded separately and is negligible.

Guardrail: the output certifies the exact-source REPRESENTATION share of the
normalization error only.  LDDD reduced-form arithmetic / residual Loewner
bracketing remains a separate finite-arithmetic obligation.
"""
from decimal import Decimal, getcontext
getcontext().prec=80

D=Decimal

# v14.034 exact protected graph lower bounds B^* S B.
LAMBDA_GRAPH={
 "even-v":D("3.9749575208499314e-30"),
 "odd-v": D("1.4355391835167209e-26"),
}
DELTA_Q={
 "even-v":D("7.795385618610192746e-6"),
 "odd-v": D("3.262507025086259604e-5"),
}
WFROB2={
 "even-v":D("6.001323151827835"),
 "odd-v": D("6.009267708281584"),
}
BDEV=D("1e-12")
RCAP=D("1e-20")

# arch-200 full 420-digit scalar interval audit.
SCALAR={
 "even-v":{
   "ez":D("5.809110335412397e-39"),
   "ed":D("4.317700732362615e-37"),
   "ep":D("7.365230177656668e-40"),
   "ec":D("6.740593794183538e-42"),
 },
 "odd-v":{
   "ez":D("5.829046823471421e-39"),
   "ed":D("1.172753572346704e-38"),
   "ep":D("4.987119893996533e-41"),
   "ec":D("6.740593794183538e-42"),
 },
}
NMAX=D(4000)
H=D(9)
ZCAP=D(10)

# Conservative analytic pole l2 caps rounded upward.
PNORM={"even-v":D("1.60"),"odd-v":D("0.43")}

# Represented arch-200 capacity midpoints, used only to quantify source-vector
# split sensitivity; source perturbation is so tiny that coarse values suffice.
CAP={
 "even-v":D("7.57730059350868404698706140797708806292461022158871986805118e-30"),
 "odd-v": D("2.184523983828947262792726883366744308218489682334387458762e-25"),
}

U=D(2) ** D(-64)

def dsqrt(x:D)->D:
    return x.sqrt()

def one(sector):
    # B bounds from ||B-I|| <= BDEV.
    bnorm=D(1)+BDEV
    binv=D(1)/(D(1)-BDEV)

    # S >= lambda_graph / ||B||^2.
    sfloor=LAMBDA_GRAPH[sector]/(bnorm*bnorm)

    # Exact graph shear K=D^{-1}E.  From normalized numerical graph W B^{-1}
    # and residual correction:
    # ||K|| <= ||W|| ||B^{-1}|| + ||P|| + delta^{-1}||R||||B^{-1}||.
    wnorm=dsqrt(WFROB2[sector])
    kcap=wnorm*binv + D(1) + RCAP*binv/DELTA_Q[sector]

    # Full front floor from T-shear, ||T^{-1}|| <= 1+||K||.
    mu=min(sfloor,DELTA_Q[sector])/(D(1)+kcap)**2

    e=SCALAR[sector]
    edisp=H*((D(1)+e["ec"])*e["ez"] + ZCAP*e["ec"])
    dp=dsqrt(NMAX)*e["ep"]
    epole=D(2)*(D(2)*PNORM[sector]*dp + dp*dp)
    eps=e["ed"]+edisp+epole

    if eps>=mu:
        raise RuntimeError((sector,"operator radius exceeds floor",eps,mu))
    theta=eps/(mu-eps)

    # Two-longdouble source split.  For round-to-nearest hi, then lo,
    # |df_i| <= u^2 |f_i|/(1-u).  Use |f_i|<1.55 and 4000 modes.
    fmax=D("1.55")
    df_l2=(U*U/(D(1)-U))*fmax*dsqrt(NMAX)
    mu_rep=mu-eps
    G=D(1)/CAP[sector]
    # relative G error from f -> f+df at fixed A_rep.
    a=df_l2/dsqrt(mu_rep*G)
    rel_G_source=D(2)*a+a*a
    # capacity relative source error <= rel_G/(1-rel_G).
    rel_C_source=rel_G_source/(D(1)-rel_G_source)

    # sqrt(C) relative half-width induced by an overall capacity relative
    # radius r is <= r/(2(1-r)) for r<1.
    total_rel=theta+rel_C_source
    sqrt_rel=total_rel/(D(2)*(D(1)-total_rel))

    row={
      "sector":sector,
      "protected_S_floor":str(sfloor),
      "graph_shear_cap":str(kcap),
      "global_exact_operator_floor":str(mu),
      "displacement_radius":str(edisp),
      "pole_radius":str(epole),
      "arch200_operator_radius":str(eps),
      "operator_relative_capacity_radius":str(theta),
      "source_split_l2_radius":str(df_l2),
      "source_relative_capacity_radius":str(rel_C_source),
      "total_exact_source_capacity_relative_radius":str(total_rel),
      "sqrt_capacity_relative_radius":str(sqrt_rel),
      "sandbox_required_sqrt_relative":str(D("7e-5")),
      "passes_source_share":bool(sqrt_rel<D("7e-5")),
    }
    if not row["passes_source_share"]:
        raise RuntimeError(("source share fails",row))
    return row

def main():
    rows=[one("even-v"),one("odd-v")]
    for r in rows:
        print("\n",r["sector"])
        for k,v in r.items():
            if k!="sector": print(k,"=",v)
    print("\nPASS: exact-source representation share is below Sandbox normalization threshold.")
    print("GUARDRAIL: LDDD finite-arithmetic capacity certification remains separate.")

if __name__=="__main__":
    main()
