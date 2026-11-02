#!/usr/bin/env python3
"""census.py — Route B prototype step B1: resonant census, odd sector.

PROTOTYPE GRADE [N]. NOT a certified run, NOT a certificate.
Setting frozen from v15.227: odd parity lattice, base b = 512001
(sigma = +1, L = 1.4357379705709206, c = 2/pi, t = 1/pi^2).
Target point x = 10.442302397081809, delta = 0.0010376564980985107,
target interval [a, b] = [x - delta, x + delta]. Guard rho = 2.5
(working M-hat 2.0 + 0.5 margin; DESIGN CHOICE, labeled).

Procedure:
  1. Float pre-filter: float d_n (SEED_FORMULA displayed model,
     coeff819/SEED_FORMULA.md "Diagonal" display) for ALL odd-lattice
     modes n = 512001 + 2j, j = 0.. up to the log-clearing index
     n_max = smallest lattice n with log(n/4) - C > b + rho,
     C = 1.745855454249828 (v15.227 certified uniform bound).
  2. Candidates: float d_n in [a - rho - 0.1, b + rho + 0.1]
     (0.1 = pre-filter slack, labeled).
  3. Certified classification: for each candidate (ascending n),
     evaluate the certified enclosure via the producer of record
     suzuki_certified_remote_diagonal.evaluate (laneA_modules);
     resonant iff the certified ENCLOSURE meets [a - rho, b + rho]
     (exact Fraction comparison; never decided on midpoints).
  4. HARD STOP: if the certified resonant count exceeds 20000,
     certified evaluation halts and the run reports no-go for
     Route B at rho = 2.5 (the full float census still completes,
     giving the scale of |R|).
  5. Stratified spot check: up to 200 candidates spread evenly over
     the candidate index range get certified evaluations too, to
     confirm float<->certified agreement at large n (labeled sample,
     NOT part of the count).

Note on the float model: the SEED_FORMULA displayed d_approx weights
the (2/(n pi)) sin term by w_q (2 - log q); the certified evaluator
weights it by w_q alone (v15.227 finding F1). The difference is
O(1/n) (~2e-6 at n ~ 5e5), far below the 0.1 pre-filter slack, and
classification never uses the float value.
"""
import json
import sys
import time
from fractions import Fraction as F
from math import exp, log, pi, sqrt

import numpy as np

sys.set_int_max_str_digits(1000000)
sys.path.insert(0, "/home/hatch/workspace/d12/laneA_modules")
import suzuki_certified_remote_diagonal as DG

RUN = "/home/hatch/workspace/d12/lane_b/sandbox/runs/20261102-routeB-prototype"

# ------------------------------------------------------------- frozen
SIGMA = +1
L_SEC = 1.4357379705709206
BASE = 512001
X = 10.442302397081809
DELTA = 0.0010376564980985107
A_INT = X - DELTA
B_INT = X + DELTA
RHO = 2.5
C_ENV = 1.745855454249828
SLACK = 0.1
HARD_STOP = 20000

W_Q = {q: (log(2) / 2 if q == 4 else log(q) / sqrt(q)) for q in (2, 3, 4, 5, 7)}
TH_Q = {q: pi * log(q) / 2 for q in (2, 3, 4, 5, 7)}


def d_float(n):
    """SEED_FORMULA displayed diagonal model, float64, vectorized."""
    n = np.asarray(n, dtype=np.float64)
    tot = np.log(n / 4.0) - 1.0 / (2.0 * n) \
        + 2.0 * ((-1.0) ** n) / (n * pi) ** 2
    for q in (2, 3, 4, 5, 7):
        coef = W_Q[q] * (2.0 - log(q))
        tot = tot - coef * (np.cos(n * TH_Q[q])
                            + (2.0 / (n * pi)) * np.sin(n * TH_Q[q]))
    return tot


def main():
    t0 = time.time()
    # log-clearing index: smallest lattice n with log(n/4) - C > b + rho
    thresh = B_INT + RHO + C_ENV
    n_real = 4.0 * exp(thresh)
    n_max = int(np.ceil(n_real))
    if n_max % 2 == 0:
        n_max += 1
    while log(n_max / 4.0) - C_ENV <= B_INT + RHO:
        n_max += 2
    while log((n_max - 2) / 4.0) - C_ENV > B_INT + RHO:
        n_max -= 2
    J = (n_max - BASE) // 2 + 1
    print(f"n_max (log-clearing) = {n_max}; lattice modes = {J}", flush=True)

    win_lo, win_hi = A_INT - RHO, B_INT + RHO
    pre_lo, pre_hi = win_lo - SLACK, win_hi + SLACK

    # ------------------------------------------------ float census
    bands_edges = [BASE, 750_000, 1_000_000, 1_500_000, 2_000_000,
                   3_000_000, 4_000_000, 6_000_000, n_max + 2]
    bands = [dict(n_lo=bands_edges[i], n_hi=bands_edges[i + 1] - 2,
                  modes=0, candidates=0, float_in_window=0)
             for i in range(len(bands_edges) - 1)]
    cand_n = []          # candidate mode values (float pre-filter pass)
    cand_d = []
    n_float_in_window = 0
    CH = 1 << 18
    for j0 in range(0, J, CH):
        j1 = min(J, j0 + CH)
        n = BASE + 2 * np.arange(j0, j1, dtype=np.int64)
        d = d_float(n)
        m_cand = (d >= pre_lo) & (d <= pre_hi)
        m_win = (d >= win_lo) & (d <= win_hi)
        n_float_in_window += int(m_win.sum())
        if m_cand.any():
            cand_n.append(n[m_cand])
            cand_d.append(d[m_cand])
        for bd in bands:
            mb = (n >= bd["n_lo"]) & (n <= bd["n_hi"])
            if mb.any():
                bd["modes"] += int(mb.sum())
                bd["candidates"] += int((mb & m_cand).sum())
                bd["float_in_window"] += int((mb & m_win).sum())
    cand_n = np.concatenate(cand_n)
    cand_d = np.concatenate(cand_d)
    print(f"float candidates (slack window) = {len(cand_n)}; "
          f"float in exact guard window = {n_float_in_window}; "
          f"float pass {time.time() - t0:.1f}s", flush=True)

    # --------------------------------------- certified classification
    win_loF, win_hiF = F(str(win_lo)), F(str(win_hi))
    resonant = []        # (n, lo_str, hi_str)
    n_eval = 0
    hard_stop_hit = False
    for n in cand_n:
        n = int(n)
        r = DG.evaluate(n)
        n_eval += 1
        lo, hi = F(r["lower_rational"]), F(r["upper_rational"])
        if lo <= win_hiF and hi >= win_loF:
            resonant.append((n, r["lower_rational"], r["upper_rational"]))
            if len(resonant) > HARD_STOP:
                hard_stop_hit = True
                print(f"HARD STOP: certified resonant count exceeded "
                      f"{HARD_STOP} after {n_eval} certified evaluations "
                      f"(at n = {n}); halting certified pass.", flush=True)
                break
        if n_eval % 5000 == 0:
            print(f"  certified evals {n_eval}, resonant so far "
                  f"{len(resonant)}, {time.time() - t0:.0f}s", flush=True)
    print(f"certified pass done: evals = {n_eval}, resonant = "
          f"{len(resonant)}, hard_stop = {hard_stop_hit}", flush=True)

    # ------------------------------- stratified spot check (labeled)
    spot = []
    if len(cand_n) > 0:
        idx = np.unique(np.linspace(0, len(cand_n) - 1,
                                    num=min(200, len(cand_n))).astype(int))
        for i in idx:
            n = int(cand_n[i])
            r = DG.evaluate(n)
            lo, hi = F(r["lower_rational"]), F(r["upper_rational"])
            spot.append(dict(
                n=n, float_d=float(cand_d[i]),
                lo=r["lower_rational"], hi=r["upper_rational"],
                mid_minus_float=float((lo + hi) / 2) - float(cand_d[i]),
                enclosure_meets_window=bool(lo <= win_hiF and hi >= win_loF),
                float_in_window=bool(win_lo <= cand_d[i] <= win_hi)))
    spot_agree = sum(1 for s in spot
                     if s["enclosure_meets_window"] == s["float_in_window"])
    spot_max_dev = max((abs(s["mid_minus_float"]) for s in spot), default=None)

    out = {
        "meta": dict(
            scope="Route B prototype B1 [N]; prototype grade, NOT a "
                  "certificate; classification of evaluated candidates "
                  "uses certified enclosures (producer of record)",
            sector="odd lattice b=512001 (sigma=+1, L=1.4357379705709206)",
            x=X, delta=DELTA, interval=[A_INT, B_INT], rho=RHO,
            guard_window=[win_lo, win_hi],
            prefilter_window=[pre_lo, pre_hi], prefilter_slack=SLACK,
            C_env=C_ENV, n_max_log_clearing=n_max,
            total_lattice_modes=int(J),
            header_context_v15306_v15307="NOT PRESENT in local ledger "
                  "cache ~/workspace/d12/cache/ledger/ (cache tops out "
                  "at v13.813; no v15 entries). No Lane A certified "
                  "M-hat value recorded from them; prototype proceeds "
                  "with the frozen design guard rho = 2.5."),
        "candidate_count_float_prefilter": int(len(cand_n)),
        "float_in_exact_guard_window": int(n_float_in_window),
        "certified_evaluations_performed": int(n_eval),
        "certified_resonant_count": (
            f">{HARD_STOP} (halted at {len(resonant)}; certified lower "
            f"bound)" if hard_stop_hit else int(len(resonant))),
        "certified_resonant_count_value": int(len(resonant)),
        "hard_stop_triggered": bool(hard_stop_hit),
        "resonant_modes_evaluated": [
            dict(n=n, lo=lo, hi=hi) for (n, lo, hi) in resonant],
        "distribution_bands": bands,
        "spot_check": dict(count=len(spot),
                           classification_agreement=spot_agree,
                           max_abs_midpoint_minus_float=spot_max_dev,
                           rows=spot),
        "wall_seconds": time.time() - t0,
    }
    with open(RUN + "/census_output.json", "w") as f:
        json.dump(out, f, indent=1)
    print(f"done in {time.time() - t0:.1f}s -> census_output.json",
          flush=True)


if __name__ == "__main__":
    main()
