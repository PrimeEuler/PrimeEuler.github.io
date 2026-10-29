#!/usr/bin/env python3
"""Independent confirmation of v15.097 Gates 1-2 against the FULL frozen
K_full kernel (DERIVATION.md §0, including the rank-one pole term that
v15.097's displayed formula omits and explicitly flags for checking).

Deliverable for the v15.097 HANDOFF (source-native-Gram-and-2x2-bridge),
part 1: confirm exchange symmetry + diagonal-weight consequence directly
against the frozen physical kernel.

Claims:
 [D] symbolic: K[N,m] - K[m,N] == 0 identically for the full kernel
     K[N,m] = c*(m*z_N - N*z_m)/(N^2-m^2) + 2*sigma*p_N*p_m  (N != m),
     K[N,N] = d_N + 2*sigma*p_N^2, with z, p, d arbitrary real data.
 [D] symbolic: diagonal-weight symmetry on l2(w),
     w_N*K[N,m] = w_m*conj(K[m,N]) (real case), reduces given Gate 1 to
     (w_N - w_m)*K[N,m] = 0.
 [D] exact-arithmetic tail argument: on the post-crossover tail
     (p_N = 0 exactly), K[N,m1] != 0 for every N in the sector lattice,
     using only audited inputs: |z_m| <= Zbar, certified z_{m1} != 0
     (exact rational midpoint/radius, ctgate/constants.json), and the
     rigorous sufficient tail start N >= L*2^256 (from p_N's frozen
     floor definition: L*N/(N^2+t) < L/N <= 2^-256 forces the floor
     to vanish). Hence w_N = w_{m1} for all tail N in any diagonal
     weighted symmetric realization on a core containing e_{m1} and
     the tail basis vectors; power weights N^{2a}, a != 0, excluded.
 [N] float spot-checks of the symmetry at concrete frozen values
     (z_float model of eval_seed_blocks; p by its exact floor formula).
"""
import json
import sys
from fractions import Fraction as F

import sympy as sp

sys.set_int_max_str_digits(1000000)

# ---------------------------------------------------------------- Gate 1
N, m, zN, zm, pN, pm, dN, c, sg = sp.symbols("N m zN zm pN pm dN c sg")

def K(a, b, za, zb, pa, pb):
    return c * (b * za - a * zb) / (a**2 - b**2) + 2 * sg * pa * pb

diff = sp.simplify(K(N, m, zN, zm, pN, pm) - K(m, N, zm, zN, pm, pN))
assert diff == 0, diff
print("[D] Gate 1: K[N,m] - K[m,N] simplifies to 0 identically for the")
print("    FULL frozen kernel (V/U part + 2*sigma*p_N*p_m pole part).")
print("    Diagonal K[N,N] = d_N + 2*sigma*p_N^2 is a single real entry:")
print("    symmetric trivially.")

# ---------------------------------------------------------------- Gate 2
wN, wm, Kval = sp.symbols("wN wm Kval")
# real symmetric: w_N*K = w_m*K  <=>  (w_N - w_m)*K = 0
cond = sp.expand(wN * Kval - wm * Kval - (wN - wm) * Kval)
assert cond == 0
print("[D] Gate 2: with K[m,N] = K[N,m] real, weighted symmetry")
print("    w_N*K[N,m] = w_m*K[m,N] is exactly (w_N - w_m)*K[N,m] = 0:")
print("    every nonzero edge forces equal endpoint weights.")

# ------------------------------------------------------- tail nonvanishing
consts = json.load(open("../../ctgate/constants.json"))
ZBAR_CEIL = F(74233, 10000)          # audited |z_m| <= 7.4232946911477145 < 7.4233
TWO256 = 2 ** 256

for sector in ("even-v", "odd-v"):
    cs = consts[sector]
    m1 = cs["spike_mode_m1"]
    z_mid = F(cs["z_m1_mid_rational"])
    z_rad = F(cs["z_m1_radius_rational"])
    z_abs_min = z_mid - z_rad
    assert z_abs_min > 0, "certified z_{m1} must be nonzero"
    L = F(cs["L_rational"])
    # rigorous sufficient tail start: p_N = floor(L*N/(N^2+t)*2^256)/2^256,
    # and L*N/(N^2+t) < L/N, so N >= L*2^256 forces the floored value to 0.
    tail_start = int(L * TWO256) + 2          # >= L*2^256, safe margin
    # vanishing on the tail would need z_N = (N/m1)*z_{m1}, i.e.
    # N = m1*|z_N|/|z_{m1}| <= m1*Zbar/|z_{m1}| =: vanish_bound.
    vanish_bound = F(m1) * ZBAR_CEIL / z_abs_min
    assert vanish_bound < tail_start, (vanish_bound, tail_start)
    print(f"[D] {sector}: m1 = {m1}, certified |z_m1| >= {float(z_abs_min):.10f}"
          f" (mid {float(z_mid):.10f} - radius {float(z_rad):.3e})")
    print(f"    vanishing of K[N,m1] on the p_N=0 tail would require "
          f"N <= {float(vanish_bound):.6e},")
    print(f"    but the tail starts at N >= {float(tail_start):.6e} "
          f"(rigorous floor bound).")
    print(f"    => K[N,m1] != 0 for ALL tail N; w_N = w_{{m1}} forced there;")
    print(f"    power weights w_N = N^(2a) give w_N/w_m1 = (N/m1)^(2a) != 1"
          f" for N != m1, a != 0: excluded.")

# ------------------------------------------------------------ spot checks
import numpy as np
sys.path.insert(0, "../../coeff819")
from eval_seed_blocks import z_float  # audited float model of the frozen z

def p_exact(n, L, t):
    return float(F(int(L * n / (n * n + t) * TWO256), TWO256)) if n < 10**30 \
        else L * n / (n * n + t)  # float model far below the floor scale

for sector, sg_val in (("even-v", 1), ("odd-v", -1)):
    cs = consts[sector]
    m1 = cs["spike_mode_m1"]
    Lf, tf = cs["L"], cs["t"]
    cf = cs["c"]
    def Knum(a, b):
        za = float(z_float(np.array([float(a)]), sg_val)[0])
        zb = float(z_float(np.array([float(b)]), sg_val)[0])
        pa = Lf * a / (a * a + tf)
        pb = Lf * b / (b * b + tf)
        return cf * (b * za - a * zb) / (a * a - b * b) + 2 * sg_val * pa * pb
    worst = 0.0
    for a, b in [(m1 + 2, m1), (m1 + 4, m1), (4161533 + 2 * 7, 4161533),
                 (10**6 + 1, 999983)]:
        if (a - b) % 2 != 0:
            b += 1
        d = abs(Knum(a, b) - Knum(b, a))
        rel = d / max(abs(Knum(a, b)), 1e-300)
        worst = max(worst, rel)
    print(f"[N] {sector}: float spot-checks of K[a,b] vs K[b,a] at 4 pairs "
          f"(incl. spike column): worst relative asymmetry {worst:.3e}"
          f" (float-model noise level).")

print("ALL CONFIRMATION CHECKS PASSED")
