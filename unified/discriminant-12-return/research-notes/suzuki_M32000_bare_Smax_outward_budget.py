#!/usr/bin/env python3
"""Hardened outward acceptance budget for Sandbox v14.094's bare S_max lemma.

This is an arithmetic/theorem-interface target, not by itself a source-arithmetic
certificate.  Inputs:
  * audited full-near numerical S_max from v14.094 / v14.096;
  * exact theorem T_p >= S_p >= I on the N=32000 near compression:
      S_p>=I by v14.071,
      T_p=S_p+B^*A_front^{-1}B>=S_p because the promoted 32k front is SPD;
  * a deliberately huge exact residual cap R_CAP for each computed bare solve.

If ||T_p x_p-u|| <= R_CAP and T_p>=I, then
  ||x_p-w_p||_2 <= R_CAP.
For d=w_e-w_o and J coordinates, every partial-sum error is at most
  sqrt(J)*(R_CAP_e+R_CAP_o).

For u_j=1/(32001+2j), Abel summation simplifies exactly:
  u_{J-1}+sum_{j=0}^{J-2}(u_j-u_{j+1}) = u_0 = 1/32001.
Thus |<u,d>| <= S_max/32001.

The C_D rank-one term is bounded without numerical K values:
  K_p=<u,T_p^{-1}u> <= ||u||^2
because T_p>=I.

FAIL CLOSED unless the resulting bare Rosc quadratic-form bound is <1e-8.
"""
from __future__ import annotations
import math

N=32000
J=16000
N0=32001
NLAST=63999
S_MAX_MID=1.567017588900339e-5  # v14.094, independently reproduced v14.096
R_CAP=5.0e-7                    # deliberately huge exact residual cap, each parity
TARGET=1.0e-8

E0=0.37474310047
C_D=-32*math.cosh(1)/math.pi**2 + 16*E0/math.pi**2

# Exact-vector partial-sum inflation from two solve errors.
s_err=math.sqrt(J)*(R_CAP+R_CAP)
s_out=S_MAX_MID+s_err

# Exact telescoping SBP coefficient.
u_last=1.0/NLAST
sum_du=1.0/N0-1.0/NLAST
sbp_coeff=u_last+sum_du
sbp_bound=s_out*sbp_coeff

# Rigorous simple same-parity finite-octave ||u||^2 bound:
# f(j)=1/(N0+2j)^2 decreasing,
# sum_{j=0}^{J-1} f(j) <= f(0)+int_0^{J-1} f(x) dx.
u2_bound=1.0/N0**2 + 0.5*(1.0/N0-1.0/(N0+2*(J-1)))
cd_bound=abs(C_D)*u2_bound*u2_bound

q_bound=sbp_bound+cd_bound

print("N =",N)
print("J =",J)
print("S_max_mid =",S_MAX_MID)
print("exact_residual_cap_each =",R_CAP)
print("partial_sum_error_cap =",s_err)
print("S_max_outward_target =",s_out)
print("u_last =",u_last)
print("sum_du_exact =",sum_du)
print("SBP coefficient =",sbp_coeff," expected 1/N0 =",1.0/N0)
print("SBP inner-product bound =",sbp_bound)
print("u_norm_sq_bound =",u2_bound)
print("|C_D|K_oK_e bound =",cd_bound)
print("bare Rosc qf bound =",q_bound)
print("public target =",TARGET)
print("headroom factor =",TARGET/q_bound)

checks={
 "telescoping_exact":abs(sbp_coeff-1.0/N0)<1e-20,
 "Smax_below_v14094_sufficient":s_out<6.4e-5,
 "qf_below_target":q_bound<TARGET,
}
for k,v in checks.items(): print(k,"=",v)
if not all(checks.values()):
    raise RuntimeError(("bare Smax outward acceptance target failed",checks))
print("PASS: exact residual <=5e-7 per sector is sufficient for bare |Q|<1e-8")
