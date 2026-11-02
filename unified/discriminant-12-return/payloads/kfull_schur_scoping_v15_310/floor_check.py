#!/usr/bin/env python3
"""floor_check.py — v15.305 validation companion to tail_norm_probe.py.

Lane A v15.305 [D]: inf_N ||Q_N B Q_N|| >= (|c|/4)*sqrt(A) > 0 and
limsup_N ||Q_N B P_N|| >= (|c|/4)*sqrt(A) for sharp prefixes, where
  A = 8 * sum_{q in {2,3,4,5,7}} w_q^2 sin^2(theta_q),
  theta_q = pi ln q / 2,  w_q = ln q / sqrt(q)  (w_4 = ln 2 / 2),
via B_{n+2,n} = (c/4)(z_{n+2} - z_n) + O(1/n) and the exact Cesaro
mean of |Delta_n|^2 = A on either parity lattice.

This script: (1) evaluates A and the floor in 50-digit arithmetic;
(2) estimates the Cesaro mean of |z_{n+2} - z_n|^2 from the z_float
evaluator over long windows on both sector lattices and compares;
(3) tabulates the probe's finite-window ||Q_N B Q_N|| estimates
against the floor. Sandbox [N] numerics; not a certificate.
"""
import json
from math import log, pi, sqrt

import numpy as np
from mpmath import mp, mpf
from mpmath import log as mlog
from mpmath import pi as mpi
from mpmath import sin as msin
from mpmath import sqrt as msqrt

from tail_norm_probe import SECTORS, z_float

mp.dps = 50


def closed_form_A():
    tot = mpf(0)
    terms = {}
    for q in (2, 3, 4, 5, 7):
        w = mlog(2) / 2 if q == 4 else mlog(q) / msqrt(q)
        th = mpi * mlog(q) / 2
        terms[q] = w**2 * msin(th) ** 2
        tot += terms[q]
    A = 8 * tot
    c = 2 / mpi
    return A, (c / 4) * msqrt(A), terms


def cesaro(sec, n_lo, n_hi, checkpoints):
    """Cesaro mean of |z_{n+2}-z_n|^2 over sector lattice n in [n_lo, n_hi)."""
    parity = sec["parity"]
    n0 = n_lo if n_lo % 2 == parity else n_lo + 1
    ns = np.arange(n0, n_hi, 2, dtype=np.int64)
    z = z_float(ns, sec["sigma"])
    d2 = (z[1:] - z[:-1]) ** 2  # z_{n+2} - z_n on consecutive lattice points
    run = np.cumsum(d2)
    out = {"n_start": int(ns[0]), "samples": int(len(d2))}
    for cp in checkpoints:
        k = min(cp, len(d2))
        out[f"cesaro_first_{cp}"] = float(run[k - 1] / k)
    out["cesaro_full"] = float(run[-1] / len(d2))
    return out


def main():
    A, floor, terms = closed_form_A()
    A_f, floor_f = float(A), float(floor)
    print(f"A (50-digit)      = {mp.nstr(A, 30)}")
    print(f"(|c|/4)*sqrt(A)   = {mp.nstr(floor, 30)}")
    res = {"A_high_precision": mp.nstr(A, 30),
           "floor_high_precision": mp.nstr(floor, 30),
           "A_float": A_f, "floor_float": floor_f,
           "terms_w2_sin2": {str(q): float(t) for q, t in terms.items()},
           "sectors": {}}
    probe = json.load(open("probe_output.json"))
    for name, sec in SECTORS.items():
        cz = cesaro(sec, 100_000, 4_100_000, (50_000, 200_000, 500_000, 1_000_000))
        cz["relative_error_full_vs_A"] = (cz["cesaro_full"] - A_f) / A_f
        rows = []
        for r in probe[name]["tail_norms_QBQ"]:
            rows.append(dict(cutoff_N=r["cutoff_N"], window_W=r["window_W"],
                             norm_est=r["norm_est"],
                             ratio_to_floor=r["norm_est"] / floor_f,
                             below_floor=bool(r["norm_est"] < floor_f)))
        res["sectors"][name] = {"cesaro_Delta_z": cz, "window_vs_floor": rows}
        print(f"[{name}] Cesaro |dz|^2 full = {cz['cesaro_full']:.6f} "
              f"(A = {A_f:.6f}, rel.err {cz['relative_error_full_vs_A']:+.2e})")
        for r in rows:
            print(f"  cutoff={r['cutoff_N']} W={r['window_W']}: "
                  f"norm={r['norm_est']:.4f} = {r['ratio_to_floor']:.2f} x floor"
                  f"{'  <-- BELOW FLOOR' if r['below_floor'] else ''}")
    with open("floor_check_output.json", "w") as f:
        json.dump(res, f, indent=1)
    print("-> floor_check_output.json")


if __name__ == "__main__":
    main()
