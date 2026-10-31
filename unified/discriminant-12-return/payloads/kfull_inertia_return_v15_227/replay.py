#!/usr/bin/env python3
"""Exact-diagonal interval replay for the v15.192 handoff + M verification
+ uniform |d_n - log(n/4)| bound derivation.

Certificate path: exact rational interval arithmetic only (Fractions),
via the certified producers in ~/workspace/d12/laneA_modules/.
Floats appear ONLY as (a) decimal renderings for human comparison and
(b) the Lane A published float targets being checked.
"""
import sys, json, time
sys.set_int_max_str_digits(1000000)
sys.path.insert(0, "/home/hatch/workspace/d12/laneA_modules")
from fractions import Fraction as F
import suzuki_certified_remote_diagonal as DG
import suzuki_certified_remote_z as ZM

RUN = "/home/hatch/workspace/d12/lane_b/sandbox/runs/20261031-kfull-inertia"
CONST = json.load(open("/home/hatch/workspace/d12/dm490/far585/ctgate/constants.json"))

# Sector pairing (see BUILD_LOG): lattice base -> constants.json key.
SECTORS = {
    "odd_lattice_b512001":  {"b": 512001, "ckey": "even-v"},   # sigma=+1, L=1.4357...
    "even_lattice_b512002": {"b": 512002, "ckey": "odd-v"},    # sigma=-1, L=0.6634...
}
# Lane A v15.192 published float targets: five lowest sampled (value, n).
TARGETS = {
    "odd_lattice_b512001": [(10.44022730, 512035), (10.44437691, 512151),
                            (10.54281672, 512191), (10.61627262, 512053),
                            (10.64189646, 512013)],
    "even_lattice_b512002": [(10.28559769, 512082), (10.29855466, 512122),
                             (10.32751192, 512174), (10.40179968, 512024),
                             (10.43555101, 512064)],
}
STATED_GAP = {"odd_lattice_b512001": "0.00414962",
              "even_lattice_b512002": "0.01295697"}
ZBAR_HI = F(74233, 10000)          # v15.192 displayed certified bound Zbar < 7.4233
ZBAR_CERT = "7.4232946911477145"   # coeff819/zbar_moments.py certified value (project record)

def dec(fr, digits=12):
    """Decimal rendering of a Fraction (display only)."""
    return float(fr)

out = {"provenance": {
    "diagonal_evaluator": "laneA_modules/suzuki_certified_remote_diagonal.py evaluate(n)",
    "z_evaluator": "laneA_modules/suzuki_certified_remote_z.py evaluate(n, action_precision=True)",
    "constants": "dm490/far585/ctgate/constants.json",
    "targets": "ledger v15.192 text (fetched, sources/)"},
}

# ---------- pi / c enclosures from the z-module's own constants ----------
pi_lo, pi_hi = ZM.constants(256)[0]
c_lo, c_hi = 2 / pi_hi, 2 / pi_lo
out["c_enclosure"] = {"lo": str(c_lo), "hi": str(c_hi), "float": dec((c_lo + c_hi) / 2)}

# ---------- p_n formula cross-check at the spike modes ----------
pcheck = {}
for name, S in SECTORS.items():
    C = CONST[S["ckey"]]
    L = F(C["L_rational"]); t = F(C["t_rational"]); n = S["b"]
    p = (L * n / (n * n + t) * (1 << 256)) // 1  # floor of the rational
    p = F(int(p), 1 << 256)
    pcheck[name] = {"n": n, "computed_p": str(p),
                    "constants_p_m1": C["p_m1_rational"],
                    "exact_match": str(p) == C["p_m1_rational"]}
out["p_spike_crosscheck"] = pcheck

# ---------- M verification from v15.129 displayed inequality ----------
mres = {}
for name, S in SECTORS.items():
    C = CONST[S["ckey"]]
    b = S["b"]; L = F(C["L_rational"])
    b0 = 2 * ZBAR_HI + c_hi * ZBAR_HI / (2 * b)          # |c|pi Zbar = 2 Zbar exactly
    # pole: 2||p||^2 <= 2 L^2 * sum_{lattice n>=b} 1/n^2 <= 2 L^2 (1/b^2 + 1/(2b))
    pole = 2 * L * L * (F(1, b * b) + F(1, 2 * b))
    lanea_pole = F(4, b - 2)                              # v15.192 displayed bound
    mres[name] = {"B0_bound": str(b0), "B0_bound_float": dec(b0),
                  "pole_bound_exactL": str(pole), "pole_bound_exactL_float": dec(pole),
                  "pole_bound_v15192_displayed": str(lanea_pole),
                  "M_total": str(b0 + pole), "M_total_float": dec(b0 + pole),
                  "M_le_15": (b0 + pole) < 15,
                  "laneA_claim_B0_lt": "14.84661", "consistent": dec(b0) < 14.84661}
out["M_verification"] = mres

# ---------- Uniform |d_n - log(n/4)| bound from SEED_FORMULA Sdiag ----------
# |D_osc(n)| <= |cusp_n| + sum_q w_q (2 - log q) (1 + 2/(n pi)) + evaluator
# remainder terms (arch 43*invk^2, cusp err 3*ix^3), for all n >= 512001.
pi256 = ZM.constants(256)
weights = pi256[2]
amp = F(0)
for q, (wp, dw) in zip(ZM.QS, weights):
    lq_lo, lq_hi = ZM.log_interval(q, 256)
    w_hi = wp + dw
    coef_hi = 2 - lq_lo
    amp += w_hi * coef_hi
n0 = 512001
invk_hi = 2 / (n0 * pi_lo)                 # 2/(n pi) upper at smallest n
ix_hi = 1 / (n0 * pi_lo)
cusp_hi = F(1, 2 * n0) + 2 * ix_hi * ix_hi
arch_hi = 43 * invk_hi * invk_hi
cusperr_hi = 3 * ix_hi ** 3
# Module-faithful term bound (FINDING F1): |term_q| <= w_q(2-log q)*|cos|
# + w_q * invk * |sin| <= w_q(2-log q) + w_q*invk.
wsum = F(0)
for (wp, dw) in weights:
    wsum += wp + dw
C_unif = cusp_hi + amp + wsum * invk_hi + arch_hi + cusperr_hi
out["uniform_bound"] = {
    "sum_q wq(2-logq) upper": str(amp), "float": dec(amp),
    "C_total": str(C_unif), "C_total_float": dec(C_unif),
    "claim": "|d_n - log(n/4)| <= C_total for all lattice n >= 512001 (both sectors)",
    "lt_3": C_unif < 3, "lt_2": C_unif < 2, "lt_1_76": C_unif < F(176, 100)}

# ---------- The replay ----------
replay = {}
for name, S in SECTORS.items():
    b = S["b"]
    t0 = time.time()
    rows = []
    for j in range(100):
        n = b + 2 * j
        r = DG.evaluate(n)
        lo, hi = F(r["lower_rational"]), F(r["upper_rational"])
        rows.append({"n": n, "lo": str(lo), "hi": str(hi),
                     "lo_f": dec(lo), "hi_f": dec(hi),
                     "mid_f": dec((lo + hi) / 2), "radius_f": dec((hi - lo) / 2)})
    rows_sorted = sorted(rows, key=lambda r: F(r["lo"]))
    # certified gap between 1st and 2nd sorted enclosures
    lo1, hi1 = F(rows_sorted[0]["lo"]), F(rows_sorted[0]["hi"])
    lo2, hi2 = F(rows_sorted[1]["lo"]), F(rows_sorted[1]["hi"])
    gap_cert = lo2 - hi1
    gap_mid = (lo2 + hi2) / 2 - (lo1 + hi1) / 2
    # target comparison: same n's in same order? value within enclosure
    # widened by display rounding 5e-9 + approx-vs-exact remainder arch_hi?
    tol = F(5, 10**9) + (hi1 - lo1)  # generous display tolerance per value
    tcomp = []
    for k, (tv, tn) in enumerate(TARGETS[name]):
        row = rows_sorted[k]
        tvF = F(str(tv))
        inside = F(row["lo"]) <= tvF <= F(row["hi"])
        dist = F(0) if inside else min(abs(tvF - F(row["lo"])), abs(tvF - F(row["hi"])))
        tcomp.append({"rank": k + 1, "target_value": tv, "target_n": tn,
                      "replay_n": row["n"], "n_match": row["n"] == tn,
                      "target_inside_enclosure": bool(inside),
                      "dist_target_to_enclosure": dec(dist),
                      "within_display_tol": bool(dist <= tol)})
    replay[name] = {
        "b": b, "eval_seconds": round(time.time() - t0, 2),
        "rows": rows,
        "five_lowest": [{"n": r["n"], "lo": r["lo"], "hi": r["hi"],
                         "mid_f": r["mid_f"]} for r in rows_sorted[:5]],
        "certified_first_gap": str(gap_cert), "certified_first_gap_float": dec(gap_cert),
        "midpoint_first_gap_float": dec(gap_mid),
        "laneA_stated_gap": STATED_GAP[name],
        "target_comparison": tcomp,
        "all_five_n_match": all(t["n_match"] for t in tcomp),
        "all_five_within_display_tol": all(t["within_display_tol"] for t in tcomp),
    }
out["replay"] = replay

# ---------- FINDING F1: discrepancy identity verification (mpmath, 50 digits) ----------
# certified d_n - displayed-formula d_n  =?=  sum_q w_q (1 - log q) (2/(n pi)) sin(theta_q n)
from mpmath import mp, mpf, log as mplog, sin as mpsin, pi as mppi, sqrt as mpsqrt
mp.dps = 50
def F2mp(fr): return mpf(fr.numerator) / mpf(fr.denominator)
wq_mp = {q: (mplog(2) / 2 if q == 4 else mplog(q) / mpsqrt(q)) for q in (2, 3, 4, 5, 7)}
f1 = {}
for name, S in SECTORS.items():
    rows_by_n = {r["n"]: r for r in replay[name]["rows"]}
    checks = []
    for tv, tn in TARGETS[name]:
        r = rows_by_n[tn]
        mid = (F(r["lo"]) + F(r["hi"])) / 2
        pred = sum(wq_mp[q] * (1 - mplog(q)) * (2 / (tn * mppi)) *
                   mpsin(mppi * mplog(q) / 2 * tn) for q in (2, 3, 4, 5, 7))
        actual = F2mp(mid) - mpf(str(tv))
        checks.append({"n": tn, "certified_mid_minus_laneA_float": float(actual),
                       "predicted_by_F1_identity": float(pred),
                       "abs_residual": float(abs(actual - pred))})
    f1[name] = checks
out["F1_identity_check"] = f1

json.dump(out, open(RUN + "/replay_output.json", "w"), indent=1)
print("p crosscheck:", {k: v["exact_match"] for k, v in pcheck.items()})
print("M:", {k: (v["M_total_float"], v["M_le_15"]) for k, v in mres.items()})
print("uniform C:", dec(C_unif), "lt3:", C_unif < 3)
for name, R in replay.items():
    print(name, "certified gap:", R["certified_first_gap_float"],
          "mid gap:", R["midpoint_first_gap_float"], "stated:", R["laneA_stated_gap"],
          "n-match:", R["all_five_n_match"], "tol:", R["all_five_within_display_tol"])
    for t in R["target_comparison"]:
        print("   rank", t["rank"], "n", t["replay_n"], "inside:", t["target_inside_enclosure"],
              "dist:", t["dist_target_to_enclosure"])
print("uniform C (module-faithful):", dec(C_unif))
for name, checks in f1.items():
    print("F1", name, "max |residual|:", max(c["abs_residual"] for c in checks))
