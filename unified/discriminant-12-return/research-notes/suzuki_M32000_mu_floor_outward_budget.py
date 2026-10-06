#!/usr/bin/env python3
"""Deterministic outward-budget target for the M=32000 finite-section floor.

Inputs are drawn from the completed arch-200/LDDD fixed-FFT 32k replay,
the v14.029 M=8000 frozen-complement theorem, the v14.071 nested remote
coercivity theorem, and the M32000 graph/Qcomp diagnostic.

This producer is a certificate TARGET, not a theorem by itself.  It applies
public padding constants:
  * cross-block norm B<=40 for the Q8-to-(8k,32k] complement extension;
  * C_DD=8192 (the conservative interpretation of the v14.034 EFT count);
  * Qcomp<=12 (midpoints: 6.83147 even, 2.42000 odd);
  * per protected-column LDDD residual <=1e-25;
  * shear tau<=0.04 even, <=0.11 odd;
  * ||W||_F^2<=8.

It then computes:
  1. a coarse rigorous-target complement floor at 32k;
  2. protected Schur outward lower bounds;
  3. full finite-section mu_32k via graph congruence;
  4. theta=eps/(mu-eps);
  5. the resulting coarse 16k->32k shell interval and cumulative 4k->32k interval.

The accompanying ledger entry supplies the analytic proofs/justifications
for the public caps and identifies which padding statements still require
independent audit.
"""
from decimal import Decimal, getcontext
getcontext().prec=80
D=Decimal

NPTS=D(16000)
U=D(2) ** D(-64)
CDD=D(8192)
QCAP=D(12)
WFROB2_CAP=D(8)
RCOL_CAP=D("1e-25")
NCOLS=D(6)
B_CROSS_CAP=D(40)
TARGET_MU=D("1.2e-31")
RCAP=D("1e-7")
THETA_E_MAX=D("1.174454e-5")

DELTA8={
 "even-v":D("7.795385618610192746e-6"),
 "odd-v":D("3.262507025086259604e-5"),
}
PIVOT32={
 "even-v":D("5.67126816594919256613793717097e-30"),
 "odd-v":D("1.42959091963877922082616902732e-26"),
}
EOP32={
 "even-v":D("1.0914650487773005e-36"),
 "odd-v":D("8.786870658639323e-38"),
}
QCOMP_MID={
 "even-v":D("6.831462611825017"),
 "odd-v":D("2.4199994307658286"),
}
TAU_MID={
 "even-v":D("0.036359790380966414"),
 "odd-v":D("0.09601786333514431"),
}
TAU_CAP={
 "even-v":D("0.04"),
 "odd-v":D("0.11"),
}
LDD_RESIDUAL_OBS={
 "even-v":D("6.28414475481085e-26"),
 "odd-v":D("1.435106127025862e-26"),
}

C16={
 "even-v":D("7.499901498486917e-30"),
 "odd-v":D("2.1622076013239955e-25"),
}
C32={
 "even-v":D("7.485609640013522e-30"),
 "odd-v":D("2.158138843073839e-25"),
}
BASE_4K16_LO=D("3.45557892442104e-7")
BASE_4K16_HI=D("1.97545933653356e-6")

def shear_sigma2(tau):
    # Stable exact formula for the unit-triangular 2x2 worst case.
    return (D(2)/( (tau*tau+D(4)).sqrt()+tau ))**2

def neglog1m(x):
    s=D(0); p=x
    for k in range(1,80):
        s += p/D(k)
        p *= x
    return s

def sector_budget(sector):
    d=DELTA8[sector]

    # Complement extension:
    # C8>=delta I; the shell Schur complement is >=I.
    # tau_Q <= ||B||/delta <= 40/delta.
    tau_q=B_CROSS_CAP/d
    gamma32=d*shear_sigma2(tau_q)

    source_form=EOP32[sector]*WFROB2_CAP
    dd_round=CDD*NPTS*(U*U)*QCAP
    residual_op_sq=NCOLS*(RCOL_CAP*RCOL_CAP)
    residual_corr=residual_op_sq/gamma32
    protected_lower=PIVOT32[sector]-source_form-dd_round-residual_corr

    sigma2= shear_sigma2(TAU_CAP[sector])
    mu=min(protected_lower,gamma32)*sigma2
    theta=EOP32[sector]/(mu-EOP32[sector])

    return {
      "delta8":d,
      "complement_extension_tau_cap":tau_q,
      "complement_floor_32k":gamma32,
      "source_form_radius":source_form,
      "dd_rounding_radius":dd_round,
      "residual_quadratic_radius":residual_corr,
      "protected_pivot_mid":PIVOT32[sector],
      "protected_lower":protected_lower,
      "graph_tau_mid":TAU_MID[sector],
      "graph_tau_cap":TAU_CAP[sector],
      "graph_sigma2":sigma2,
      "mu_32k_lower":mu,
      "mu_target_headroom":mu/TARGET_MU,
      "operator_epsilon_32k":EOP32[sector],
      "theta_32k":theta,
      "qcomp_mid":QCOMP_MID[sector],
      "qcomp_cap":QCAP,
      "ldd_residual_observed":LDD_RESIDUAL_OBS[sector],
      "residual_cap_per_column":RCOL_CAP,
    }

def shell_interval(theta_e,theta_o):
    eta_e=C16["even-v"]/C32["even-v"]-D(1)
    eta_o=C16["odd-v"]/C32["odd-v"]-D(1)
    mid=eta_o-eta_e
    def rad(eta,theta):
        L=D(2)*neglog1m(theta)+D(2)*neglog1m(RCAP)
        return (D(1)+eta)*(L+L*L)
    W=rad(eta_e,theta_e)+rad(eta_o,theta_o)
    return eta_e,eta_o,mid,W,mid-W,mid+W

def main():
    rows={s:sector_budget(s) for s in ("even-v","odd-v")}
    eta_e,eta_o,mid,W,lo,hi=shell_interval(
        rows["even-v"]["theta_32k"], rows["odd-v"]["theta_32k"]
    )
    cum_lo=BASE_4K16_LO+lo
    cum_hi=BASE_4K16_HI+hi

    print("M32000 finite-section floor certificate target")
    for s,r in rows.items():
        print("\n",s)
        for k,v in r.items():
            print(k,"=",v)

    print("\n16k->32k")
    print("eta_e =",eta_e)
    print("eta_o =",eta_o)
    print("mid =",mid)
    print("half_width =",W)
    print("interval =",lo,hi)
    print("cumulative_4k_32k =",cum_lo,cum_hi)

    checks={
      "qcomp_even_below_cap":QCOMP_MID["even-v"]<QCAP,
      "qcomp_odd_below_cap":QCOMP_MID["odd-v"]<QCAP,
      "residual_even_below_cap":LDD_RESIDUAL_OBS["even-v"]<RCOL_CAP,
      "residual_odd_below_cap":LDD_RESIDUAL_OBS["odd-v"]<RCOL_CAP,
      "mu_even_above_target":rows["even-v"]["mu_32k_lower"]>TARGET_MU,
      "mu_odd_above_target":rows["odd-v"]["mu_32k_lower"]>TARGET_MU,
      "theta_even_below_v14080_max":rows["even-v"]["theta_32k"]<THETA_E_MAX,
      "shell_strictly_negative":hi<0,
      "cumulative_strictly_negative":cum_hi<0,
    }
    print("\nchecks")
    for k,v in checks.items(): print(k,"=",v)
    if not all(checks.values()):
        raise RuntimeError(("certificate target failed",checks))

if __name__=="__main__":
    main()
