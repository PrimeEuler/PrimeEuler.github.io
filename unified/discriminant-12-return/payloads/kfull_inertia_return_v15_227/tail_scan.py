#!/usr/bin/env python3
"""Certified tail-diagonal scan for the inertia transfer test.

Per sector, scan the first W tail modes beyond the J=100 block
(n = b+202, b+204, ..., b+202+2(W-1)) with the certified diagonal
evaluator and count, with exact Fraction comparisons against the
declared (x, delta) from the replay:
  - enclosures ENTIRELY below x - delta  (proof: d_n < x - delta;
    these are eigenvalues of the diagonal-preserving cutoff K_R
    below the strip, omitted by the J=100 section);
  - enclosures ENTIRELY below x          (proof: d_n < x);
  - enclosures FULLY INSIDE [x-delta, x+delta] (proof: d_n in strip;
    these are eigenvalues of K_R inside the strip);
  - enclosures intersecting the strip;
  - the enclosure minimizing dist(x, [lo,hi]) -> rigorous lower
    bound tau_S(x) >= 1 / max(|lo - x|, |hi - x|) for that mode,
    hence a lower bound on the v15.155 bracket term M * tau_S.
All counts are rigorous LOWER bounds on the full tail counts
(window-limited; the window is stated exactly).
"""
import sys, json, time
sys.set_int_max_str_digits(1000000)
sys.path.insert(0, "/home/hatch/workspace/d12/laneA_modules")
from fractions import Fraction as F
import suzuki_certified_remote_diagonal as DG

RUN = "/home/hatch/workspace/d12/lane_b/sandbox/runs/20261031-kfull-inertia"
SECTORS = {"odd_lattice_b512001": 512001, "even_lattice_b512002": 512002}
W = 20000
M_FRAC = F(15)

replay = json.load(open(RUN + "/replay_output.json"))
out = {}
for name, b in SECTORS.items():
    srt = sorted(replay["replay"][name]["rows"], key=lambda r: F(r["lo"]))
    hi1, lo2 = F(srt[0]["hi"]), F(srt[1]["lo"])
    x = (hi1 + lo2) / 2; delta = (lo2 - hi1) / 4
    t0 = time.time()
    below_strip, below_x, in_strip, touch_strip = [], [], [], []
    best = None  # (upper bound on |d_n - x|, n, lo, hi)
    for j in range(W):
        n = b + 202 + 2 * j
        r = DG.evaluate(n)
        lo, hi = F(r["lower_rational"]), F(r["upper_rational"])
        if hi < x - delta: below_strip.append((n, r["lower_rational"], r["upper_rational"]))
        if hi < x: below_x.append((n, r["lower_rational"], r["upper_rational"]))
        if lo >= x - delta and hi <= x + delta: in_strip.append((n, r["lower_rational"], r["upper_rational"]))
        if lo <= x + delta and hi >= x - delta: touch_strip.append(n)
        ub = max(abs(lo - x), abs(hi - x))
        if best is None or ub < best[0]: best = (ub, n, r["lower_rational"], r["upper_rational"])
    tau_lb = 1 / best[0]
    res = {"b": b, "W": W, "window": f"n in [{b + 202}, {b + 202 + 2 * (W - 1)}] step 2",
           "x_float": float(x), "delta_float": float(delta),
           "count_enclosures_below_x_minus_delta": len(below_strip),
           "count_enclosures_below_x": len(below_x),
           "count_enclosures_fully_in_strip": len(in_strip),
           "count_enclosures_touching_strip": len(touch_strip),
           "first5_below_x_minus_delta": below_strip[:5],
           "first5_fully_in_strip": in_strip[:5],
           "closest_mode": {"n": best[1], "lo": best[2], "hi": best[3],
                            "upper_bound_on_abs_d_n_minus_x": str(best[0]),
                            "float": float(best[0])},
           "tau_S_at_x_lower_bound": str(tau_lb), "tau_S_at_x_lower_bound_float": float(tau_lb),
           "M_times_tau_S_lower_bound_float": float(M_FRAC * tau_lb),
           "scan_seconds": round(time.time() - t0, 1)}
    out[name] = res
    print(name, "below x-d:", len(below_strip), " below x:", len(below_x),
          " in strip:", len(in_strip), " touching:", len(touch_strip),
          " closest |d_n - x| <=", float(best[0]), "at n =", best[1],
          " M*tau_S >=", float(M_FRAC * tau_lb))
json.dump(out, open(RUN + "/tail_scan_output.json", "w"), indent=1)
print("saved tail_scan_output.json")
