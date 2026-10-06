#!/usr/bin/env python3
"""Sandbox direct quadratic-form attack for v14.093 handoff.

Proves an exact algebraic identity that rewrites the bare oscillatory
quadratic form as an inner product, then establishes a rigorous
summation-by-parts (SBP) framework. The SBP bound is evaluated
numerically; the remaining open lemma (rigorous S_max bound) is
precisely stated as a quantified obstruction.

Exact identity (Theorem, bare case):
    <w_o, (T_o - T_e) w_e> = <u, w_e - w_o>
where T_p w_p = u (bare near-block solves), by symmetry of T_p.

SBP framework (rigorous):
    |<u,d>| <= |u_{J-1}| |S_{J-1}| + S_max * sum_{j<J-1} |u_j - u_{j+1}|
where d = w_e - w_o, S_j = sum_{i<=j} d_i, S_max = max_j |S_j|.

The u-terms are bounded rigorously by calculus. S_max is computed
numerically; a rigorous bound remains the open lemma.
"""
from __future__ import annotations
import sys, math, json
import numpy as np

sys.path.insert(0, '/tmp/d12work')
from osc_full_near import solve, N, C_D, M_PRIMARY

A_E = 1200.4587051950723327
TARGET = 1e-8

def main():
    J = 16000
    n = N + 1 + 2 * np.arange(J, dtype=int)
    m = n + 1
    u = 1.0 / n.astype(float)

    we, mve, ite, re = solve(n, "even-v", u)
    wo, mvo, ito, ro = solve(m, "odd-v", u)

    # --- Exact identity verification ---
    # <w_o, (T_o - T_e) w_e> should equal <u, w_e - w_o>
    lhs = float(wo @ (mvo(we) - mve(we)))  # <w_o, T_o w_e> - <w_o, T_e w_e>
    # Note: mve(we) = u by solve; use directly for clarity
    lhs_check = float(wo @ mvo(we)) - float(wo @ u)
    rhs = float(u @ (we - wo))
    identity_err = abs(lhs_check - rhs)

    # --- Direct quadratic form (bare) ---
    delta = mvo(we) - mve(we) - C_D * u * float(u @ we)
    qf_bare = float(wo @ delta)
    cd_term = -C_D * float(u @ wo) * float(u @ we)

    # --- SBP quantities ---
    d = we - wo
    S = np.cumsum(d)
    Smax = float(np.max(np.abs(S)))
    S_last = float(abs(S[-1]))
    u_last = float(u[-1])
    sum_du = float(np.sum(np.abs(u[:-1] - u[1:])))
    sbp_bound = u_last * S_last + Smax * sum_du

    # --- Rigorous u-term bounds (calculus) ---
    # sum_{j} |1/n_j - 1/n_{j+1}|, n_j = 32001 + 2j
    # |1/a - 1/(a+2)| = 2/(a(a+2)) <= 2/a^2
    # sum <= sum_{j>=0} 2/(32001+2j)^2 <= integral bound
    a0 = 32001.0
    # integral_0^inf 2/(a0+2x)^2 dx = 1/a0
    sum_du_rig = 1.0 / a0 + 2.0 / a0**2  # integral + first term correction
    u_last_rig = 1.0 / (a0 + 2 * (J - 1))

    # --- Norms ---
    norm_u = float(np.linalg.norm(u))
    norm_we = float(np.linalg.norm(we))
    norm_wo = float(np.linalg.norm(wo))
    norm_prod = norm_we * norm_wo
    norm_d = float(np.linalg.norm(d))

    # --- Effective constant ---
    ceff = abs(qf_bare) / norm_prod if norm_prod > 0 else float('inf')

    out = {
        "J": J,
        "identity_lhs": lhs_check,
        "identity_rhs": rhs,
        "identity_abs_err": identity_err,
        "qf_bare": qf_bare,
        "A_e_abs_qf": A_E * abs(qf_bare),
        "qf_over_Mprimary": A_E * abs(qf_bare) / M_PRIMARY,
        "qf_over_target": abs(qf_bare) / TARGET,
        "C_D_term": cd_term,
        "S_max_numerical": Smax,
        "S_last": S_last,
        "u_last": u_last,
        "sum_abs_du_numerical": sum_du,
        "sum_abs_du_rigorous": sum_du_rig,
        "u_last_rigorous": u_last_rig,
        "sbp_bound_numerical": sbp_bound,
        "sbp_bound_over_target": sbp_bound / TARGET,
        "norm_u": norm_u,
        "norm_we": norm_we,
        "norm_wo": norm_wo,
        "norm_product": norm_prod,
        "norm_d": norm_d,
        "effective_constant": ceff,
        "cg_iters": [ite, ito],
        "cg_residuals": [re, ro],
    }
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
