#!/usr/bin/env python3
"""v14.071 handoff: update the v14.069 conditional enclosure with theorem gamma_N=1.

Recomputes (all with rigorous gamma=1, replacing exploratory gamma~6.38):
  K^{up}_N = 1/(2N)            [coarse theorem bound on K_{p,N}]
  dU(N)    = 2*A_max/(sqrt(12)*N^2)   [coarse delta-u remainder]
  cross(N) parametrized in C_rho, C_p
  subleading(N) parametrized in C_rho, C_p
and the feasibility budgets |dA|, |C_S| at 32k/64k using the diagonal K.
"""
import math

MARGIN = 3.45557892442104e-7
A_MAX = 804.0
GAMMA = 1.0  # theorem from v14.071 (nested Schur inheritance)

# diagonal-approx K from v14.069 s5 (numerical, for feasibility budgets only)
K_DIAG = {8000: 7.42e-6, 16000: 3.42e-6, 32000: 1.59e-6,
          64000: 7.42e-7, 128000: 3.48e-7}

print("=== v14.071 gamma=1 enclosure constants ===")
print(f"margin m* = {MARGIN:.4e}, A_max = {A_MAX}, gamma = {GAMMA} (theorem)")
print()
print(f"{'N':>8} {'K_up=1/2N':>12} {'dU(coarse)':>12} {'dU/margin':>10} {'K_diag':>10}")
for N in (8000, 16000, 32000, 64000, 128000):
    Kup = 1.0 / (2 * N * GAMMA)
    dU = 2 * A_MAX / (GAMMA * math.sqrt(12) * N ** 2)
    print(f"{N:>8} {Kup:>12.4e} {dU:>12.4e} {dU / MARGIN:>10.3f} {K_DIAG[N]:>10.2e}")

print()
print("=== cross / subleading (parametrized in C_rho, C_p; gamma=1) ===")
print("  |cross| <= 2*sqrt(A_max)*||u||*||eps||  (v14.069 s7)")
print("  |subleading| <= ||eps||^2")
for N in (16000, 32000, 64000):
    u_norm = 1.0 / math.sqrt(2 * N)
    logN = math.log(N)
    # ||eps|| <= sqrt(C_p)*C_rho*logN/sqrt(3 N^3)
    eps_coeff = logN / math.sqrt(3 * N ** 3)
    cross_coeff = 2 * math.sqrt(A_MAX) * u_norm * eps_coeff
    sub_coeff = eps_coeff ** 2
    print(f"  N={N}: ||u||<={u_norm:.3e}, ||eps||<={eps_coeff:.3e}*sqrt(C_p)*C_rho")
    print(f"         |cross| <= {cross_coeff:.3e}*sqrt(C_p)*C_rho  ({cross_coeff/MARGIN:.3f} x margin if C's=1)")
    print(f"         |subleading| <= {sub_coeff:.3e}*C_p*C_rho^2")

print()
print("=== feasibility budgets at 64k (diagonal K; after coarse dU reserve) ===")
N = 64000
K = K_DIAG[N]
dU = 2 * A_MAX / (GAMMA * math.sqrt(12) * N ** 2)
remaining = MARGIN - dU
# split: T1 <- 35%, T2 <- 50%, reserve 15% for cross/subleading/R_osc
b1, b2 = 0.35 * remaining, 0.50 * remaining
dA_budget = b1 / K
CS_budget = b2 / (A_MAX * K ** 2)
print(f"  dU(coarse) = {dU:.3e} ({dU/MARGIN:.2%} of margin)")
print(f"  remaining for T1+T2+rest = {remaining:.3e}")
print(f"  |dA| < {b1:.2e}/{K:.2e} = {dA_budget:.3f}")
print(f"  |C_S| < {b2:.2e}/({A_MAX}*{K:.2e}^2) = {CS_budget:.1f}")
print()
print("=== 32k verdict (coarse) ===")
N = 32000
dU32 = 2 * A_MAX / (GAMMA * math.sqrt(12) * N ** 2)
print(f"  dU(coarse,32k) = {dU32:.3e} = {dU32/MARGIN:.2f} x margin  -> coarse enclosure CANNOT fit at 32k")
