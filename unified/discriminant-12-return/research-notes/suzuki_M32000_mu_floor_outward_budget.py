#!/usr/bin/env python3
"""Deterministic outward-budget target for the M=32000 finite-section floor.

Inputs are drawn from the completed arch-200/LDDD fixed-FFT 32k replay,
the v14.029 M=8000 frozen-complement theorem, the v14.071 nested remote
coercivity theorem, and the M32000 graph/Qcomp diagnostic.

This producer is a certificate TARGET, not a theorem by itself. It:
  * derives a cross-block cap below the public B<=40;
  * uses C_DD=8192 (the conservative v14.034 EFT interpretation);
  * uses Qcomp<=12 (midpoints 6.83147 even, 2.42000 odd);
  * uses per-column LDDD residual <=1e-25 as the primary budget;
  * stress-tests a doubled residual cap 2e-25;
  * uses shear tau<=0.04 even, <=0.11 odd;
  * uses ||W||_F^2<=8.

It computes the 32k complement floor, protected outward floor, full
finite-section mu_32k, theta=eps/(mu-eps), and the resulting 16k->32k
and cumulative 4k->32k intervals.
"""
from decimal import Decimal, getcontext
import math
getcontext().prec=80
D=Decimal

NPTS=D(16000)
U=D(2) ** D(-64)
CDD=D(8192)
QCAP=D(12)
WFROB2_CAP=D(8)
RCOL_CAP=D("1e-25")
RCOL_STRESS=D("2e-25")
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
    return (D(2)/((tau*tau+D(4)).sqrt()+tau))**2

def neglog1m(x):
    s=D(0); p=x
    for k in range(1,80):
        s += p/D(k)
        p *= x
    return s

def harmonic(n):
    return sum(1.0/k for k in range(1,n+1))

def derive_cross_block_cap():
    # |z|<=10 gives displacement entry <=20/(pi*|n-m|).
    # Same parity means |n-m|=2k, hence row sums <=10/pi H_K.
    row = (10.0/math.pi)*harmonic(12000)
    col = (10.0/math.pi)*harmonic(4000)
    disp = math.sqrt(row*col)
    # even is worst: 2 ||p_base|| ||p_shell|| <= 2||p||^2,
    # ||p||<=sqrt(2)cosh(1/2).
    pole = 4.0*math.cosh(0.5)**2
    return {
      "displacement_row_sum_cap": row,
      "displacement_col_sum_cap": col,
      "displacement_spectral_cap": disp,
      "pole_cross_cap_even": pole,
      "derived_total_cap": disp+pole,
    }

def sector_budget(sector, rcol_cap=RCOL_CAP):
    d=DELTA8[sector]
    tau_q=B_CROSS_CAP/d
    gamma32=d*shear_sigma2(tau_q)

    source_form=EOP32[sector]*WFROB2_CAP
    dd_round=CDD*NPTS*(U*U)*QCAP
    residual_op_sq=NCOLS*(rcol_cap*rcol_cap)
    residual_corr=residual_op_sq/gamma32
    protected_lower=PIVOT32[sector]-source_form-dd_round-residual_corr

    sigma2=shear_sigma2(TAU_CAP[sector])
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
      "residual_cap_per_column":rcol_cap,
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

def report_case(label, rcap):
    rows={s:sector_budget(s,rcap) for s in ("even-v","odd-v")}
    eta_e,eta_o,mid,W,lo,hi=shell_interval(
        rows["even-v"]["theta_32k"], rows["odd-v"]["theta_32k"]
    )
    cum_lo=BASE_4K16_LO+lo
    cum_hi=BASE_4K16_HI+hi
    print("\n===",label,"===")
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
      "observed_residual_even_below_case_cap":LDD_RESIDUAL_OBS["even-v"]<rcap,
      "observed_residual_odd_below_case_cap":LDD_RESIDUAL_OBS["odd-v"]<rcap,
      "mu_even_above_target":rows["even-v"]["mu_32k_lower"]>TARGET_MU,
      "mu_odd_above_target":rows["odd-v"]["mu_32k_lower"]>TARGET_MU,
      "theta_even_below_v14080_max":rows["even-v"]["theta_32k"]<THETA_E_MAX,
      "shell_strictly_negative":hi<0,
      "cumulative_strictly_negative":cum_hi<0,
    }
    print("\nchecks")
    for k,v in checks.items(): print(k,"=",v)
    if not all(checks.values()):
        raise RuntimeError(("certificate target failed",label,checks))
    return rows,(lo,hi,cum_lo,cum_hi)

def main():
    print("M32000 finite-section floor certificate target")
    cross=derive_cross_block_cap()
    print("\nanalytic cross-block cap derivation")
    for k,v in cross.items(): print(k,"=",v)
    print("public_B_cap =",B_CROSS_CAP)
    if not D(str(cross["derived_total_cap"])) < B_CROSS_CAP:
        raise RuntimeError(("derived B cap does not fit",cross))

    primary,_=report_case("primary residual cap 1e-25",RCOL_CAP)
    stress,ints=report_case("stress residual cap 2e-25",RCOL_STRESS)

    print("\nrobustness summary")
    print("stress_even_mu =",stress["even-v"]["mu_32k_lower"])
    print("stress_even_mu_headroom =",stress["even-v"]["mu_target_headroom"])
    print("stress_even_theta =",stress["even-v"]["theta_32k"])
    print("stress_cumulative_upper =",ints[3])
    print("ALL PRIMARY + DOUBLED-RESIDUAL STRESS CHECKS PASS")

if __name__=="__main__":
    main()
