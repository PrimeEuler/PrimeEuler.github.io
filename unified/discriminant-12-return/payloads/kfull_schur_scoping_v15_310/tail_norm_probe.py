#!/usr/bin/env python3
"""tail_norm_probe.py — sandbox [N] scoping probe for the v15.232
full-K transfer-alternative handoff, against Lane A's Schur gates
v15.303 / v15.304.

SCOPE: numerical scoping only. NOT a certificate, NOT Lane A's
analytic ||Q_N B Q_N|| bound. All tail "norms" below are norms of
FINITE-WINDOW compressions of B, hence LOWER bounds for the true
compression norms. z_n is the float model z_float of
coeff819/eval_seed_blocks.py; p_n is the float approximation
L*n/(n^2+t) of the exact floored p_n (fine for a probe).

Frozen kernel (DERIVATION.md sec. 0), per sector parity lattice:
  K_{N,m} = c*(m*z_N - N*z_m)/(N^2 - m^2) + 2*sigma*p_N*p_m  (N != m)
  K_{N,N} = d_N + 2*sigma*p_N^2,   c = 2/pi,  t = 1/pi^2.
B := off-diagonal part of K (B_{N,N} = 0).

Quantities:
 (a) ||Q_N B Q_N|| estimates: extremal eigenvalues of B compressed
     to the first W parity modes strictly above physical cutoff N.
 (b) ||V|| = ||Q B P|| for P = the v15.227 remote block (J = 100
     modes n = b + 2j), Q = all other sector-lattice modes,
     evaluated by chunked Gram accumulation (below-block part exact
     finite; above-block part truncated at a declared window with a
     labeled residual scale).
 (c) v15.304 stopping scales N_stop(b, M) = 4*exp(b + C + M) - 2,
     C = 1.745855454249828, and the coarse Schur residual
     ||V||^2 / g at the implied scales.
"""
import json
import time
from math import e as EULER, exp, log, pi, sqrt

import numpy as np
from scipy.linalg import eigvalsh

# ---------------------------------------------------------------- z model
# z_float copied verbatim from coeff819/eval_seed_blocks.py (audited
# float model of the certified remote z sequence).
W_Q = {q: (log(2) / 2 if q == 4 else log(q) / sqrt(q)) for q in (2, 3, 4, 5, 7)}
TH_Q = {q: pi * log(q) / 2 for q in (2, 3, 4, 5, 7)}
S0 = (1 / EULER) / (1 - np.exp(-4))


def z_float(n, sigma):
    n = np.asarray(n, dtype=np.float64)
    tot = np.full(n.shape, pi / 2) + (1 - 4 * sigma * S0) / (n * pi)
    for q in (2, 3, 4, 5, 7):
        tot = tot + 2 * W_Q[q] * np.sin(n * TH_Q[q])
    return tot


# ---------------------------------------------------------------- kernel
C_KERNEL = 2.0 / pi
T_PK = 1.0 / pi**2
ZBAR = 7.4232946911477145  # certified |z| bound (coeff819), for residual scale only
C_ENV = 1.745855454249828  # v15.227 certified uniform |d_n - log(n/4)| bound

SECTORS = {
    "odd-lattice_b512001_even-v": dict(
        sigma=+1, L=1.4357379705709206, b=512001, parity=1, b_int=10.45,
        gap_v15227=0.004150625992394043),
    "even-lattice_b512002_odd-v": dict(
        sigma=-1, L=0.6634791495304894, b=512002, parity=0, b_int=10.30,
        gap_v15227=0.012958023663653584),
}


def p_float(n, L):
    n = np.asarray(n, dtype=np.float64)
    return L * n / (n * n + T_PK)


def build_B(rows, cols, sigma, L):
    """Dense B[rows x cols] of the frozen kernel (float64).
    rows, cols: int arrays of physical mode values (sector lattice)."""
    r = np.asarray(rows, dtype=np.float64)
    c_ = np.asarray(cols, dtype=np.float64)
    zr = z_float(r, sigma)
    zc = z_float(c_, sigma)
    pr = p_float(r, L)
    pc = p_float(c_, L)
    N = r[:, None]
    M = c_[None, :]
    # (N^2 - M^2) as (N-M)(N+M): exact for these magnitudes, no cancellation.
    den = (N - M) * (N + M)
    with np.errstate(divide="ignore", invalid="ignore"):
        B = C_KERNEL * (M * zr[:, None] - N * zc[None, :]) / den
    B = B + 2.0 * sigma * pr[:, None] * pc[None, :]
    if rows is cols or (len(rows) == len(cols) and np.array_equal(rows, cols)):
        np.fill_diagonal(B, 0.0)
    return B


def sym_norm(B):
    """Operator norm of a symmetric dense matrix via extremal eigenvalues."""
    w = B.shape[0]
    lam_max = eigvalsh(B, subset_by_index=[w - 1, w - 1])[0]
    lam_min = eigvalsh(B, subset_by_index=[0, 0])[0]
    return float(max(abs(lam_max), abs(lam_min))), float(lam_min), float(lam_max)


def lattice_above(parity, cutoff, count):
    """First `count` sector-lattice mode values strictly above `cutoff`."""
    n0 = cutoff + 1
    if n0 % 2 != parity:
        n0 += 1
    return n0 + 2 * np.arange(count, dtype=np.int64)


# ---------------------------------------------------------------- (a)
def tail_norms(sec):
    out = []
    for cutoff in (1000, 10000, 100000, 500000):
        for W in (2000, 4000):
            if W == 4000 and cutoff not in (1000, 500000):
                continue  # window-size check only at the ladder ends
            modes = lattice_above(sec["parity"], cutoff, W)
            B = build_B(modes, modes, sec["sigma"], sec["L"])
            nrm, lmin, lmax = sym_norm(B)
            out.append(dict(cutoff_N=cutoff, window_W=W,
                            first_mode=int(modes[0]), last_mode=int(modes[-1]),
                            norm_est=nrm, lambda_min=lmin, lambda_max=lmax))
            print(f"  tail cutoff={cutoff} W={W}: ||QBQ||_est={nrm:.6f} "
                  f"(lam [{lmin:.4f}, {lmax:.4f}])", flush=True)
    return out


# ---------------------------------------------------------------- (b)
def gram_accumulate(row_blocks, cols, sigma, L):
    """G = sum over row blocks of V^T V for V = B[rows x cols]."""
    G = np.zeros((len(cols), len(cols)))
    for rows in row_blocks:
        V = build_B(rows, cols, sigma, L)
        G += V.T @ V
    return G


def offblock_norm(sec):
    b = sec["b"]
    parity = sec["parity"]
    block = b + 2 * np.arange(100, dtype=np.int64)  # v15.227 J=100 block
    # below-block part: all sector modes from lattice start to b-2 (finite, exact)
    start = 1 if parity == 1 else 2
    below = np.arange(start, b - 1, 2, dtype=np.int64)
    chunks = [below[i:i + 8192] for i in range(0, len(below), 8192)]
    G_below = gram_accumulate(chunks, block, sec["sigma"], sec["L"])
    res = {"block_first": int(block[0]), "block_last": int(block[-1]),
           "below_modes": int(len(below))}
    nrm_below = sqrt(float(eigvalsh(G_below)[-1]))
    res["norm_below_only"] = nrm_below
    print(f"  V below-block ({len(below)} modes): ||V||={nrm_below:.6f}", flush=True)
    # above-block windows
    for W in (2000, 20000):
        above = (b + 200) + 2 * np.arange(W, dtype=np.int64)
        G_above = gram_accumulate([above], block, sec["sigma"], sec["L"])
        nrm_above = sqrt(float(eigvalsh(G_above)[-1]))
        G_tot = G_below + G_above
        nrm_tot = sqrt(float(eigvalsh(G_tot)[-1]))
        res[f"above_W{W}"] = dict(modes=W, last_mode=int(above[-1]),
                                  norm_above_only=nrm_above,
                                  norm_combined=nrm_tot,
                                  frob_combined=sqrt(float(np.trace(G_tot))))
        print(f"  V above W={W}: ||V||_above={nrm_above:.6f} "
              f"combined={nrm_tot:.6f}", flush=True)
    # labeled residual scale for the dropped infinite tail beyond the
    # W=20000 window: per-column Gram bound ~ c^2 Zbar^2 /(2*(n_end - m))
    # (Hilbert-type 1/(n-m) majorant, parity step 2) — estimate, not a bound proof.
    n_end = b + 200 + 2 * 19999
    resid = C_KERNEL**2 * ZBAR**2 / (2.0 * (n_end - block[-1]))
    res["dropped_tail_gram_residual_scale_per_column"] = resid
    res["combined_norm_used"] = res["above_W20000"]["norm_combined"]
    return res


# ---------------------------------------------------------------- (c)
def n_stop(b_int, M):
    return 4.0 * exp(b_int + C_ENV + M) - 2.0


def stopping_tables(sec, measured_M):
    rows = []
    for M in (15.0, 10.0, 7.0, 5.0, 3.0, 2.0, 1.0):
        rows.append(dict(M_N=M, kind="hypothetical", N_stop=n_stop(sec["b_int"], M)))
    for M, tag in measured_M:
        rows.append(dict(M_N=M, kind=tag, N_stop=n_stop(sec["b_int"], M)))
    return rows


def main():
    t0 = time.time()
    results = {"meta": dict(
        scope="sandbox [N] scoping probe; finite-window estimates are LOWER "
              "bounds for the true compression norms; NOT a certificate",
        kernel="K_{N,m} = c*(m*z_N - N*z_m)/(N^2-m^2) + 2*sigma*p_N*p_m, "
               "c=2/pi, t=1/pi^2, z = z_float model, p = L*n/(n^2+t) float",
        C_env=C_ENV)}
    for name, sec in SECTORS.items():
        print(f"[{name}] sigma={sec['sigma']} L={sec['L']} b={sec['b']}", flush=True)
        entry = {"sector": name, "sigma": sec["sigma"], "L": sec["L"],
                 "b": sec["b"], "b_int_top": sec["b_int"]}
        entry["tail_norms_QBQ"] = tail_norms(sec)
        entry["offblock_V"] = offblock_norm(sec)
        # measured M_N anchors: window estimates at the two largest cutoffs
        meas = []
        for r in entry["tail_norms_QBQ"]:
            if r["window_W"] == 2000 and r["cutoff_N"] in (100000, 500000):
                meas.append((r["norm_est"],
                             f"measured window est. (lower bound), cutoff "
                             f"{r['cutoff_N']}, W=2000"))
        entry["stopping"] = stopping_tables(sec, meas)
        # coarse Schur residual ||V||^2 / g at implied scales for measured M
        V2 = entry["offblock_V"]["combined_norm_used"] ** 2
        resid_rows = []
        for M, tag in meas:
            for g in (0.1, 0.5, 1.0, 2.0):
                Ng = 4.0 * exp(sec["b_int"] + C_ENV + M + g) - 2.0
                resid_rows.append(dict(M_N=M, anchor=tag, g=g, N=Ng,
                                       V2_over_g=V2 / g))
        entry["coarse_schur_residual"] = resid_rows
        entry["v15227_gap_scale"] = sec["gap_v15227"]
        results[name] = entry
        for r in entry["stopping"]:
            print(f"  stop M={r['M_N']:.4f} ({r['kind']}): N>{r['N_stop']:.4e}",
                  flush=True)
    results["meta"]["wall_seconds"] = time.time() - t0
    with open("probe_output.json", "w") as f:
        json.dump(results, f, indent=1)
    print(f"done in {time.time() - t0:.1f}s -> probe_output.json", flush=True)


if __name__ == "__main__":
    main()
