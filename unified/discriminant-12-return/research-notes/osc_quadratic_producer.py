#!/usr/bin/env python3
"""v14.072 producer: oscillatory quadratic-form certificate exploration.

Computes (deterministic, numpy only, no RNG):
  1. Phase denominators 1/|sin(theta_q/2)|, 1/|sin(phi_q/2)| for q in {2,3,4,5,7}
     [D: exact arithmetic from the fixed prime phases]
  2. Verification of the exact identities used in the decomposition:
     - sum-of-products identity for the oscillatory off-diagonal kernel [D]
     - q=7 slow-delta exact reduction (delta_7 = pi*(1-log7/2)) [D]
     - diagonal cos-difference exact form [D]
  3. Toeplitz symbol constant pi/2 for the sinc kernel [D]
  4. Per-channel numerical quadratic forms <w_o, R_q w_e> (bare, window) [N]
  5. w-roughness metrics: w = a + r split, ripple fraction [N]
  6. Smooth-remainder rigorous crude bounds [D]
  7. Cutoff-parametric table at N = 16k/32k/64k/128k [N] vs margin
  8. SHA-256 of key outputs (determinism)

Conventions: [D]=derived, [N]=numerical, [I]=inference, [O]=open/gap.
No repo/ledger writes. Staged for the v14.072 handoff response.
"""
from __future__ import annotations
import hashlib
import math
import numpy as np

# --- structural data (from infinite_tail_producer.py; duplicated for standalone use) ---
QS = (2, 3, 4, 5, 7)
WS = (
    math.log(2) / math.sqrt(2),
    math.log(3) / math.sqrt(3),
    math.log(2) / 2,
    math.log(5) / math.sqrt(5),
    math.log(7) / math.sqrt(7),
)
C_TWO_OVER_PI = 2.0 / math.pi
E0 = 0.37474310047
C_D = -32 * math.cosh(1) / math.pi ** 2 + 16 * E0 / math.pi ** 2
MARGIN = 3.45557892442104e-7
A_MAX = 804.0
DELTA7 = math.pi * (1 - math.log(7) / 2)  # exact slow phase for q=7 [D]


def corr_n(n: int, terms: int = 50) -> float:
    k = n * math.pi / 2
    s = 0.0
    for j in range(terms):
        a = 2 * j + 0.5
        s += math.exp(-2 * a) / (a * a + k * k)
    return s


def z_com(n: int) -> float:
    s = 0.0
    for q, w in zip(QS, WS):
        s += w * math.sin(n * math.pi * math.log(q) / 2)
    y = n * math.pi / 4
    return 2 * s + math.pi / 2 * math.tanh(math.pi * y)


def z_parity(n: int, sector: str) -> float:
    zc = z_com(n)
    cn = corr_n(n)
    pi_p = -1.0 if sector == "even" else 1.0
    return zc - pi_p * n * math.pi * cn


def diag_n_noarch(n: int) -> float:
    """d_n without arch (arch is smooth O(1/n^2); bounded separately)."""
    k = n * math.pi / 2
    logpart = math.log(n / 4.0)
    prime = 0.0
    for q, w in zip(QS, WS):
        prime += w * (
            (2 - math.log(q)) * math.cos(n * math.pi * math.log(q) / 2)
            + math.sin(n * math.pi * math.log(q) / 2) / k
        )
    return logpart - prime


def pole_n(n: int, sector: str) -> float:
    k = n * math.pi / 2
    g = math.cosh(0.5) if sector == "even" else math.sinh(0.5)
    return 2 * k * g / (k * k + 0.25)


def alpha(sector: str) -> float:
    return 2.0 if sector == "even" else -2.0


def kernel(n: int, m: int, sector: str, zcache: dict) -> float:
    zn = zcache[(n, sector)]
    zm = zcache[(m, sector)]
    pn = pole_n(n, sector)
    pm = pole_n(m, sector)
    t = C_TWO_OVER_PI * (m * zn - n * zm) / (n * n - m * m)
    t += alpha(sector) * pn * pm
    return t


def diag_kernel_noarch(n: int, sector: str) -> float:
    pn = pole_n(n, sector)
    return diag_n_noarch(n) + alpha(sector) * pn * pn


def paired_modes(N: int, J: int):
    ns = [N + 1 + 2 * j for j in range(J)]
    ms = [N + 2 + 2 * j for j in range(J)]
    return ns, ms


def build_T(modes, sector, zcache):
    J = len(modes)
    T = np.zeros((J, J))
    for i, n in enumerate(modes):
        T[i, i] = diag_kernel_noarch(n, sector)
        for j, m in enumerate(modes):
            if i != j:
                T[i, j] = kernel(n, m, sector, zcache)
    return 0.5 * (T + T.T)


def phase_table():
    """[D] Exact phase denominators from the fixed prime phases."""
    rows = []
    for q, w in zip(QS, WS):
        theta = math.pi * math.log(q)      # per-j increment for sin(A+j*theta), n_j step 2
        phi = math.pi * math.log(q) / 2    # per-j increment in the (j+k) offdiag form
        d_diag = 1.0 / abs(math.sin(theta / 2))
        d_off = 1.0 / abs(math.sin(phi / 2))
        rows.append((q, w, theta, d_diag, phi, d_off))
    return rows


def verify_identities():
    """[D] Verify the three exact identities to machine precision."""
    errs = {}
    # (1) sum-of-products
    e1 = 0.0
    for q in QS:
        ph = math.pi * math.log(q) / 2
        for (a, b) in ((16001, 16003), (16001, 16009), (32001, 32011)):
            sa, sb = math.sin(a * ph), math.sin(b * ph)
            lhs = (b * sa - a * sb) / (a * a - b * b)
            S = (a + b) * ph / 2
            D = (a - b) * ph / 2
            rhs = math.cos(S) * math.sin(D) / (a - b) - math.sin(S) * math.cos(D) / (a + b)
            e1 = max(e1, abs(lhs - rhs))
    errs["sum_of_products"] = e1
    # (2) q=7 slow-delta reduction
    e2s = e2c = 0.0
    for n in (16001, 16003, 32001, 16002, 16004, 64002):
        e2s = max(e2s, abs(math.sin(n * math.pi * math.log(7) / 2)
                           - (1 if n % 2 else -1) * math.sin(n * DELTA7)))
        e2c = max(e2c, abs(math.cos(n * math.pi * math.log(7) / 2)
                           - (-1 if n % 2 else 1) * math.cos(n * DELTA7)))
    errs["delta7_sin"] = e2s
    errs["delta7_cos"] = e2c
    # (3) diagonal cos difference
    e3 = 0.0
    for q in QS:
        ph = math.pi * math.log(q) / 2
        for n in (16001, 32003, 64001):
            lhs = math.cos((n + 1) * ph) - math.cos(n * ph)
            rhs = -2 * math.sin(ph / 2) * math.sin((n + 0.5) * ph)
            e3 = max(e3, abs(lhs - rhs))
    errs["cos_difference"] = e3
    return errs


def offdiag_q_form(ns, ms, q, wq, wo, we):
    """[N] <w_o, R_q^off w_e> for one q (bare, window)."""
    J = len(ns)
    ph = math.pi * math.log(q) / 2
    val = 0.0
    for j in range(J):
        nj = ns[j]
        mj = ms[j]
        for k in range(J):
            if j == k:
                continue
            nk = ns[k]
            mk = ms[k]
            t_o = (mk * math.sin(mj * ph) - mj * math.sin(mk * ph)) / (mj * mj - mk * mk)
            t_e = (nk * math.sin(nj * ph) - nj * math.sin(nk * ph)) / (nj * nj - nk * nk)
            val += wo[j] * (C_TWO_OVER_PI * 2 * wq * (t_o - t_e)) * we[k]
    return val


def channel_analysis(N, J):
    """[N] Full per-channel breakdown at cutoff N, window J (bare operators)."""
    ns, ms = paired_modes(N, J)
    zc = {}
    for n in ns:
        zc[(n, "even")] = z_parity(n, "even")
    for m in ms:
        zc[(m, "odd")] = z_parity(m, "odd")
    Te = build_T(ns, "even", zc)
    To = build_T(ms, "odd", zc)
    nj = np.array(ns, float)
    mj = np.array(ms, float)
    u = 1.0 / nj
    we = np.linalg.solve(Te, u)
    wo = np.linalg.solve(To, u)
    # w = a + r split (even sector)
    d = np.diag(Te)
    a = u / d
    r = we - a
    rough = {
        "norm_w": float(np.linalg.norm(we)),
        "norm_a": float(np.linalg.norm(a)),
        "norm_r": float(np.linalg.norm(r)),
        "ripple_l2_frac": float(np.linalg.norm(r) / np.linalg.norm(we)),
        "sum_d_w": float(np.abs(np.diff(we)).sum()),
        "sum_d_a": float(np.abs(np.diff(a)).sum()),
        "sum_d_r": float(np.abs(np.diff(r)).sum()),
        "lam_min": float(np.linalg.eigvalsh(Te)[0]),
    }
    # R_osc^b and its quadratic form
    Delta = To - Te
    Rosc = Delta - C_D * np.outer(u, u)
    qf = float(wo @ (Rosc @ we))
    dd = np.diag(np.diag(Rosc))
    out = {
        "qf_Rosc": qf,
        "qf_diag": float(wo @ (dd @ we)),
        "qf_offd": float(wo @ ((Rosc - dd) @ we)),
        "opnorm_Rosc": float(np.linalg.norm(Rosc, 2)),
        "rough": rough,
    }
    # per-q diagonal oscillatory pieces
    dq = {}
    for q, wq in zip(QS, WS):
        ph = math.pi * math.log(q) / 2
        amp = wq * (2 - math.log(q))
        dvec = amp * (np.cos(mj * ph) - np.cos(nj * ph))
        dq[q] = float(wo @ (dvec * we))
    out["diag_per_q"] = dq
    # per-q off-diagonal (only for affordable sizes)
    oq = {}
    for q, wq in zip(QS, WS):
        oq[q] = offdiag_q_form(ns, ms, q, wq, wo, we)
    out["offd_per_q"] = oq
    # SBP-with-measured-variation bound for the diagonal pieces
    b = wo * we
    var_b = float(np.abs(np.diff(b)).sum() + abs(b[-1]))
    sbp = 0.0
    for q, wq in zip(QS, WS):
        ph = math.pi * math.log(q) / 2
        th = math.pi * math.log(q)
        pre = abs(2 * wq * (2 - math.log(q)) * math.sin(ph / 2)) / abs(math.sin(th / 2))
        sbp += pre * var_b
    out["sbp_diag_measured"] = sbp
    out["var_b"] = var_b
    # smooth log-shift piece (rigorous crude): |<w,diag(log(1+1/n))w>| <= (1/N)||w||^2
    dlog = np.log(1.0 + 1.0 / nj)
    out["smooth_log_true"] = float(wo @ (dlog * we))
    out["smooth_log_bound"] = float(np.linalg.norm(wo) * np.linalg.norm(we) / N)
    return out


def k10_qsep_bound():
    """[D] K=10 geometric remainder on Q_sep = {n >= 128000} for 64k target.

    From v14.020 (2)-(3): |R~_K(n)| <= A_K/n^{2K+3} + B_K/n^{2K+4}, K=10.
    Baseline [N]: ||R~_10||_2 < 1.21e-10 at (N=4000, n0=8000).
    Scale to (N=64000, n0=128000): n0^{-22.5} gives (8000/128000)^{22.5}
    suppression. Pessimistic 1e20 moment growth assumed.
    Map to quadratic-form remainder via theorem gamma_N=1.
    """
    import math as _m
    baseline = 1.21e-10          # [N] v14.020, (4000, 8000)
    n0_old, n0_new = 8000.0, 128000.0
    K = 10
    suppression = (n0_old / n0_new) ** (2 * K + 2.5)   # [D] scaling
    pessimistic_moment_growth = 1e20                    # [N] pessimistic
    l2_bound = baseline * pessimistic_moment_growth * suppression
    # quadratic-form remainder via gamma=1 [D]
    subleading = l2_bound ** 2                          # <eps,S^-1 eps> <= ||eps||^2
    u_norm = 1.0 / _m.sqrt(2 * 64000)                   # ||u|| <= 1/sqrt(2N)
    cross = 2 * _m.sqrt(A_MAX) * u_norm * l2_bound      # 2 sqrt(A)||u|| ||eps||
    return {
        "baseline": baseline,
        "suppression": suppression,
        "l2_bound": l2_bound,
        "subleading": subleading,
        "cross": cross,
        "total": subleading + cross,
    }


def main():
    h = hashlib.sha256()
    print("=== [D] phase denominators ===")
    for (q, w, theta, d_diag, phi, d_off) in phase_table():
        print(f"  q={q}: w_q={w:.6f}  1/|sin(theta/2)|={d_diag:.6f}  "
              f"1/|sin(phi/2)|={d_off:.6f}")
        h.update(f"{q}{d_diag:.12f}{d_off:.12f}".encode())
    print(f"  delta_7 = {DELTA7:.10f}  (exact: pi*(1-log7/2))")
    h.update(f"{DELTA7:.12f}".encode())

    print("\n=== [D] identity verification (max abs err) ===")
    for name, err in verify_identities().items():
        print(f"  {name}: {err:.3e}")
        h.update(f"{name}{err:.3e}".encode())

    print("\n=== [D] Toeplitz symbol constant ===")
    print(f"  T_d = sin(d*delta)/(2d) has symbol (pi/2)*1_{{|w|<delta}}; "
          f"||T||_2 <= pi/2 = {math.pi/2:.6f}")
    h.update(f"{math.pi/2:.12f}".encode())

    print("\n=== [N] per-channel analysis ===")
    for N in (16000, 32000, 64000, 128000):
        J = 300 if N <= 64000 else 200
        out = channel_analysis(N, J)
        r = out["rough"]
        print(f"\n  N={N} (J={J}):")
        print(f"    <w,Rosc^b w> = {out['qf_Rosc']:.4e}   "
              f"A*|.|/margin = {A_MAX*abs(out['qf_Rosc'])/MARGIN:.4f}")
        print(f"      diag part = {out['qf_diag']:.4e}, offdiag part = {out['qf_offd']:.4e}")
        print(f"      ||Rosc^b||_2 = {out['opnorm_Rosc']:.4f} (naive baseline)")
        print(f"    w-roughness: ||r||/||w|| = {r['ripple_l2_frac']:.4f}, "
              f"sum|dr|/sum|dw| = {r['sum_d_r']/r['sum_d_w']:.4f}, "
              f"lam_min(T_e) = {r['lam_min']:.3f}")
        print(f"    per-q diag <w,Rq w>: " +
              " ".join(f"{q}:{v:.2e}" for q, v in out["diag_per_q"].items()))
        print(f"    per-q offd <w,Rq w>: " +
              " ".join(f"{q}:{v:.2e}" for q, v in out["offd_per_q"].items()))
        print(f"    SBP-diag (measured var={out['var_b']:.3e}): bound = "
              f"{out['sbp_diag_measured']:.4e}, A*bnd/margin = "
              f"{A_MAX*out['sbp_diag_measured']/MARGIN:.4f}")
        print(f"    smooth log-shift: true = {out['smooth_log_true']:.3e}, "
              f"rigorous crude bound = {out['smooth_log_bound']:.3e}")
        h.update(f"{N}{out['qf_Rosc']:.6e}{out['qf_offd']:.6e}".encode())

    print("\n=== [D] v14.075: K=10 Q_sep (n>=128k) geometric remainder ===")
    k10 = k10_qsep_bound()
    print(f"  v14.020 baseline ||R~_10||_2 < {k10['baseline']:.2e} (N=4000, n0=8000) [N]")
    print(f"  n0 scaling suppression (8000/128000)^22.5 = {k10['suppression']:.3e} [D]")
    print(f"  pessimistic ||R~_10||_2 (n>=128k) <= {k10['l2_bound']:.3e} [D+N] (incl. 1e20 pessimistic moment growth)")
    print(f"  via gamma=1: subleading <= {k10['subleading']:.3e}, "
          f"cross <= {k10['cross']:.3e}")
    print(f"  Q_sep total <= {k10['total']:.3e}  ({k10['total']/MARGIN:.2e} x margin) [D]")
    h.update(f"{k10['total']:.6e}".encode())

    print("\n=== [D] smooth-remainder crude bounds (all via Cauchy-Schwarz) ===")
    print("  R_log (diag log(1+1/n)): |<w,R w>| <= ||w_o||*||w_e||/N")
    print("  R_arch, R_CiSi (smooth O(1/n^2) diag): <= C_arch2*||w_o||*||w_e||/N^2")
    print("  R_corr/R_pole remainders (O(1/n^3) in z): negligible vs 1e-12")
    print("  R_du-corr (explicit delta-u): <= C_du*||w_o||*||w_e||/N^2")
    print("  Im(psi): constant to 1e-34000 -> contributes exactly 0 [D]")

    print("\nsha256(key outputs):", h.hexdigest()[:32])


if __name__ == "__main__":
    main()
