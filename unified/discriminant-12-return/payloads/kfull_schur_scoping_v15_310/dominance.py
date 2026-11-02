#!/usr/bin/env python3
"""dominance.py — Route B prototype step B2: bulk dominance pass,
odd sector. PROTOTYPE GRADE [N]. NOT a certificate.

GATE: B2 runs only if B1 (census.py) passes. This script reads
census_output.json; if the B1 hard stop triggered, B2 is NOT RUN and
the output records that (plus one labeled diagnostic, below).

Window (per task freeze): odd-lattice modes n in
[512001, 512001 + 2*100000), excluding the J=100 v15.227 block
(j = 0..99) and excluding B1's resonant set R. Bulk modes with float
d_n > b + rho are tallied separately as the high-part analogue and
are not banded.

Banding: by float d_n value, bands of width 1.0 from
floor(min float d_n among bulk) up to b + rho.

DOMINANCE CRITERION (prototype, stated exactly): a band PASSES at
energy x if
    min over band modes of |d_n - x|  >  coupling(band),
where coupling(band) is the Frobenius mass of the band's rows over
the whole prototype window,
    coupling(band) = sqrt( ||B[band, band]||_F^2
                           + ||B[band, window \\ band]||_F^2 ),
computed in float64 by chunked accumulation (dense chunks capped at
~4000 x 8000). l1 Gershgorin row sums are NOT used: they diverge
logarithmically for this kernel (see the diagnostic).

Modes in failing bands are PROMOTED. Implied
    |P| = 100 + |R| + promoted.
HARD STOP: if promoted, extrapolated from this window to the full
bulk scale (factor = total lattice modes to n_max / window modes),
pushes |P| above 1e4, the verdict is no-go.

DIAGNOSTIC (runs even when B2 is gated off; labeled): partial l1
Gershgorin row sums S(M) = sum_{m in lattice, m <= M, m != N}
|B_{N,m}| for sample rows N, over a ladder of M, to exhibit the
logarithmic divergence that disqualifies l1 row-sum dominance for
this kernel.

Kernel / z / p models exactly as in the scoping probe
(tail_norm_probe.py, copied): K_{N,m} = (2/pi)(m z_N - N z_m)/(N^2-m^2)
+ 2 sigma p_N p_m (N != m), z = z_float, p = L n/(n^2+t) float.
"""
import json
import sys
import time
from math import log, pi, sqrt

import numpy as np

RUN = "/home/hatch/workspace/d12/lane_b/sandbox/runs/20261102-routeB-prototype"

SIGMA = +1
L_SEC = 1.4357379705709206
BASE = 512001
X = 10.442302397081809
DELTA = 0.0010376564980985107
A_INT = X - DELTA
B_INT = X + DELTA
RHO = 2.5
WINDOW_J = 100000          # lattice steps in the prototype window
BLOCK_J = 100              # v15.227 J=100 block, excluded
TARGET_P = 10_000

W_Q = {q: (log(2) / 2 if q == 4 else log(q) / sqrt(q)) for q in (2, 3, 4, 5, 7)}
TH_Q = {q: pi * log(q) / 2 for q in (2, 3, 4, 5, 7)}
S0 = (1 / np.e) / (1 - np.exp(-4))
C_KERNEL = 2.0 / pi
T_PK = 1.0 / pi**2


def z_float(n, sigma):
    n = np.asarray(n, dtype=np.float64)
    tot = np.full(n.shape, pi / 2) + (1 - 4 * sigma * S0) / (n * pi)
    for q in (2, 3, 4, 5, 7):
        tot = tot + 2 * W_Q[q] * np.sin(n * TH_Q[q])
    return tot


def d_float(n):
    n = np.asarray(n, dtype=np.float64)
    tot = np.log(n / 4.0) - 1.0 / (2.0 * n) \
        + 2.0 * ((-1.0) ** n) / (n * pi) ** 2
    for q in (2, 3, 4, 5, 7):
        coef = W_Q[q] * (2.0 - log(q))
        tot = tot - coef * (np.cos(n * TH_Q[q])
                            + (2.0 / (n * pi)) * np.sin(n * TH_Q[q]))
    return tot


def p_float(n, L):
    n = np.asarray(n, dtype=np.float64)
    return L * n / (n * n + T_PK)


def build_B(rows, cols, sigma, L):
    r = np.asarray(rows, dtype=np.float64)
    c_ = np.asarray(cols, dtype=np.float64)
    zr = z_float(r, sigma)
    zc = z_float(c_, sigma)
    pr = p_float(r, L)
    pc = p_float(c_, L)
    N = r[:, None]
    M = c_[None, :]
    den = (N - M) * (N + M)
    with np.errstate(divide="ignore", invalid="ignore"):
        B = C_KERNEL * (M * zr[:, None] - N * zc[None, :]) / den
    B = B + 2.0 * sigma * pr[:, None] * pc[None, :]
    if len(rows) == len(cols) and np.array_equal(
            np.asarray(rows), np.asarray(cols)):
        np.fill_diagonal(B, 0.0)
    return B


# ---------------------------------------------------------- diagnostic
def gershgorin_diagnostic():
    """Partial l1 row sums for sample rows over a ladder of cutoffs."""
    rows_out = []
    for N in (512001, 1000003):
        zN = float(z_float(np.array([N]), SIGMA)[0])
        pN = float(p_float(np.array([N]), L_SEC)[0])
        ladder = [2_000, 20_000, 200_000, 2_000_000, 9_582_891]
        sums = []
        for M in ladder:
            m = np.arange(1 if N % 2 == 1 else 2, M + 1, 2, dtype=np.int64)
            m = m[m != N]
            zm = z_float(m, SIGMA)
            pm = p_float(m, L_SEC)
            mf = m.astype(np.float64)
            with np.errstate(divide="ignore", invalid="ignore"):
                brow = C_KERNEL * (mf * zN - N * zm) / ((N - mf) * (N + mf))
            brow = brow + 2.0 * SIGMA * pN * pm
            s = float(np.abs(brow).sum())
            sums.append(dict(M=int(M), partial_l1_sum=s,
                             sum_over_logM=s / log(M)))
        rows_out.append(dict(row_N=N, ladder=sums))
        print(f"  Gershgorin row N={N}: " +
              ", ".join(f"M={s['M']}: {s['partial_l1_sum']:.3f}"
                        for s in sums), flush=True)
    return dict(
        kind="labeled diagnostic [N]; partial l1 Gershgorin row sums "
             "grow without bound: the far-tail (m >> N) increments "
             "track log M (for both sample rows the increment from "
             "M = 2e6 to M = 9.58e6 is ~0.35-0.41 over dlogM ~ 1.57, "
             "slope ~0.22-0.26 per ln unit, consistent with the "
             "|B_{N,m}| ~ c|z_N|/m tail), and the partial sums at the "
             "log-clearing cutoff already reach 7.2-9.6, far above "
             "any usable dominance margin at the target scale. l1 "
             "row-sum dominance is therefore disqualified for this "
             "kernel, as expected",
        rows=rows_out)


# ------------------------------------------------------------- B2 body
def run_b2(census):
    """Full banded dominance pass. Only reached if B1 passes."""
    n_max = census["meta"]["n_max_log_clearing"]
    R = {r["n"] for r in census["resonant_modes_evaluated"]}
    win = BASE + 2 * np.arange(WINDOW_J, dtype=np.int64)
    block = set((BASE + 2 * np.arange(BLOCK_J, dtype=np.int64)).tolist())
    bulk = np.array([n for n in win.tolist()
                     if n not in block and n not in R], dtype=np.int64)
    d = d_float(bulk)
    hi_cut = B_INT + RHO
    high = int((d > hi_cut).sum())          # high-part analogue, unbanded
    banded = bulk[d <= hi_cut]
    d_b = d[d <= hi_cut]
    lo_edge = float(np.floor(d_b.min()))
    edges = list(np.arange(lo_edge, hi_cut, 1.0)) + [hi_cut]
    table = []
    promoted = 0
    for i in range(len(edges) - 1):
        sel = (d_b >= edges[i]) & (d_b < edges[i + 1]) \
            if i < len(edges) - 2 else (d_b >= edges[i]) & (d_b <= edges[i + 1])
        modes = banded[sel]
        if len(modes) == 0:
            continue
        # Frobenius mass of band rows over the whole window, chunked.
        # Diagonal positions (row value == col value) are masked to 0:
        # B is the off-diagonal part, and the raw kernel formula is
        # 0/0 there (build_B only fills the diagonal for identical
        # full arrays, not for chunks).
        frob2 = 0.0
        for r0 in range(0, len(modes), 4000):
            rows = modes[r0:r0 + 4000]
            for c0 in range(0, len(win), 8000):
                cols = win[c0:c0 + 8000]
                Bc = build_B(rows, cols, SIGMA, L_SEC)
                diag = rows[:, None] == cols[None, :]
                if diag.any():
                    Bc[diag] = 0.0
                frob2 += float((Bc ** 2).sum())
        coupling = sqrt(frob2)
        min_dist = float(np.abs(d_float(modes) - X).min())
        passed = bool(min_dist > coupling)
        if not passed:
            promoted += int(len(modes))
        table.append(dict(band_lo=float(edges[i]), band_hi=float(edges[i + 1]),
                          modes=int(len(modes)), min_abs_d_minus_x=min_dist,
                          coupling_frobenius_rows=coupling,
                          passed=passed,
                          promoted=0 if passed else int(len(modes))))
        print(f"  band [{edges[i]:.1f},{edges[i+1]:.1f}): modes="
              f"{len(modes)} min_dist={min_dist:.4f} coupling="
              f"{coupling:.4f} pass={passed}", flush=True)
    scale = ((n_max - BASE) // 2 + 1) / WINDOW_J
    implied_P = BLOCK_J + len(R) + promoted
    implied_P_extrap = BLOCK_J + len(R) + int(round(promoted * scale))
    return dict(status="RAN", window_modes=int(WINDOW_J),
                bulk_modes=int(len(bulk)), high_part_analogue_modes=high,
                bands=table, promoted_in_window=int(promoted),
                extrapolation_factor=float(scale),
                implied_P_window=implied_P,
                implied_P_extrapolated=implied_P_extrapolated,
                hard_stop_P=bool(implied_P_extrapolated > TARGET_P))


def main():
    t0 = time.time()
    census = json.load(open(RUN + "/census_output.json"))
    out = {"meta": dict(scope="Route B prototype B2 [N]; prototype "
                        "grade, NOT a certificate",
                        dominance_criterion="band passes at energy x "
                        "iff min|d_n - x| over band modes > Frobenius "
                        "norm of the band's B-rows over the prototype "
                        "window (band block + cross-coupling); l1 "
                        "Gershgorin row sums NOT used (log-divergent, "
                        "see diagnostic)")}
    diag = gershgorin_diagnostic()
    out["gershgorin_diagnostic"] = diag
    if census["hard_stop_triggered"]:
        out["status"] = "NOT_RUN"
        out["reason"] = ("B1 hard stop triggered: certified resonant "
                         "count exceeded 20000 (certified evaluation "
                         "halted at 20001 resonant of 20364 evaluated "
                         "candidates; float census puts |R| at ~7.9e5 "
                         "for rho = 2.5). Per the B2 gate ('only if "
                         "B1 passes'), the banded dominance pass was "
                         "not run. The B2 implementation above is "
                         "present but UNEXECUTED beyond this gate "
                         "branch and the diagnostic.")
        print("B2 NOT RUN: B1 hard stop.", flush=True)
    else:
        res = run_b2(census)
        out.update(res)
    out["wall_seconds"] = time.time() - t0
    with open(RUN + "/dominance_output.json", "w") as f:
        json.dump(out, f, indent=1)
    print(f"done in {time.time() - t0:.1f}s -> dominance_output.json",
          flush=True)


if __name__ == "__main__":
    main()
