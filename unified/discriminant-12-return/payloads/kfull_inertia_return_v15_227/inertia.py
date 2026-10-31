#!/usr/bin/env python3
"""Interval-inertia build for the v15.192 handoff (route PRIMARY).

Per sector: finite section K_J (J=100, replay modes) with interval
entries as exact Fraction pairs, outward-rounded to a 2^-512 grid
after every operation (valid enclosures; grid error 2^-512 << all
physical widths). Interval LDL^T of K_J - xI at x-delta, x, x+delta,
where x = midpoint of the certified replay gap interval and
delta = certified gap / 4. Pivot intervals excluding 0 certify the
Sylvester inertia count for K_J.

Float numpy eigenvalues of the midpoint matrix are computed as a
LABELED CONTEXT PROBE ONLY (design sanity; nothing rests on them).
"""
import sys, json, time
sys.set_int_max_str_digits(1000000)
sys.path.insert(0, "/home/hatch/workspace/d12/laneA_modules")
from fractions import Fraction as F
import suzuki_certified_remote_z as ZM

RUN = "/home/hatch/workspace/d12/lane_b/sandbox/runs/20261031-kfull-inertia"
CONST = json.load(open("/home/hatch/workspace/d12/dm490/far585/ctgate/constants.json"))
SECTORS = {"odd_lattice_b512001": {"b": 512001, "ckey": "even-v"},
           "even_lattice_b512002": {"b": 512002, "ckey": "odd-v"}}
GRID = 1 << 512

def rout(iv):
    lo, hi = iv
    lo2 = F(lo.numerator * GRID // lo.denominator, GRID)
    hi2 = F(-((-hi.numerator * GRID) // hi.denominator), GRID)
    return (lo2, hi2)
def iadd(a, b): return rout((a[0] + b[0], a[1] + b[1]))
def isub(a, b): return rout((a[0] - b[1], a[1] - b[0]))
def imul(a, b):
    v = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return rout((min(v), max(v)))
def iscale(a, q):  # q Fraction/int, exact sign handling
    return rout((a[0] * q, a[1] * q)) if q >= 0 else rout((a[1] * q, a[0] * q))
def isq(a):
    if a[0] >= 0: return rout((a[0] * a[0], a[1] * a[1]))
    if a[1] <= 0: return rout((a[1] * a[1], a[0] * a[0]))
    return (F(0), max(a[0] * a[0], a[1] * a[1]))
def irecip(a):
    assert a[0] > 0 or a[1] < 0
    return rout((1 / a[1], 1 / a[0]))
def pt(q): return (F(q), F(q))

pi_lo, pi_hi = ZM.constants(256)[0]
C_IV = (2 / pi_hi, 2 / pi_lo)   # c = 2/pi enclosure

def build_sector(name, S, drows):
    C = CONST[S["ckey"]]
    sigma = C["sigma"]; L = F(C["L_rational"]); t = F(C["t_rational"])
    modes = [S["b"] + 2 * j for j in range(100)]
    ziv = {}
    for n in modes:
        r = ZM.evaluate(n, action_precision=True)
        ziv[n] = (F(r["lower_rational"]), F(r["upper_rational"]))
    piv = {}
    for n in modes:
        piv[n] = F(int(L * n / (n * n + t) * (1 << 256)), 1 << 256)
    div = {r["n"]: (F(r["lo"]), F(r["hi"])) for r in drows}
    J = len(modes)
    A = [[None] * J for _ in range(J)]
    for i, N in enumerate(modes):
        for j, m in enumerate(modes):
            if i == j:
                A[i][j] = iadd(div[N], pt(2 * sigma * piv[N] * piv[N]))
            else:
                num = isub(iscale(ziv[N], m), iscale(ziv[m], N))
                den = N * N - m * m
                term = iscale(imul(C_IV, num), F(1, den))
                A[i][j] = iadd(term, pt(2 * sigma * piv[N] * piv[m]))
    return modes, A

def ldl_count(A, x):
    """Interval LDL^T of A - xI. Returns dict with counts or failure."""
    J = len(A)
    M = [[A[i][j] if i != j else isub(A[i][j], pt(x)) for j in range(J)] for i in range(J)]
    D = [None] * J; L = [[pt(0)] * J for _ in range(J)]
    minmargin = None
    for k in range(J):
        s = M[k][k]
        for j in range(k):
            s = isub(s, imul(isq(L[k][j]), D[j]))
        D[k] = s
        if s[0] <= 0 <= s[1]:
            return {"ok": False, "fail_pivot": k, "pivot_interval": (str(s[0]), str(s[1]))}
        margin = s[0] if s[0] > 0 else -s[1]
        minmargin = margin if minmargin is None else min(minmargin, margin)
        for i in range(k + 1, J):
            tt = M[i][k]
            for j in range(k):
                tt = isub(tt, imul(imul(L[i][j], D[j]), L[k][j]))
            L[i][k] = imul(tt, irecip(D[k]))
    neg = sum(1 for d in D if d[1] < 0)
    pos = sum(1 for d in D if d[0] > 0)
    return {"ok": True, "neg": neg, "pos": pos, "min_pivot_margin": str(minmargin),
            "min_pivot_margin_float": float(minmargin)}

replay = json.load(open(RUN + "/replay_output.json"))
out = {}
for name, S in SECTORS.items():
    t0 = time.time()
    rows = replay["replay"][name]["rows"]
    srt = sorted(rows, key=lambda r: F(r["lo"]))
    hi1, lo2 = F(srt[0]["hi"]), F(srt[1]["lo"])
    gap = lo2 - hi1
    x = (hi1 + lo2) / 2
    delta = gap / 4
    modes, A = build_sector(name, S, rows)
    res = {"b": S["b"], "x": str(x), "x_float": float(x), "delta": str(delta),
           "delta_float": float(delta), "certified_gap": str(gap),
           "build_seconds": round(time.time() - t0, 1)}
    for label, xx in (("x_minus_delta", x - delta), ("x", x), ("x_plus_delta", x + delta)):
        res[label] = ldl_count(A, xx)
    # context probe (float, NOT part of the certificate)
    import numpy as np
    Am = np.array([[float((A[i][j][0] + A[i][j][1]) / 2) for j in range(100)] for i in range(100)])
    ev = np.linalg.eigvalsh(Am)
    res["context_probe_float"] = {
        "note": "numpy eigvalsh of midpoint matrix; context only, no certificate weight",
        "lowest_eigs": [float(v) for v in ev[:6]],
        "count_below_x_float": int(sum(1 for v in ev if v < float(x))),
        "eigs_in_strip_float": [float(v) for v in ev if abs(v - float(x)) <= float(delta)]}
    out[name] = res
    print(name, "x=", float(x), "delta=", float(delta),
          {k: (v.get("neg"), v.get("ok")) for k, v in res.items() if isinstance(v, dict) and "ok" in v},
          "probe count<x:", res["context_probe_float"]["count_below_x_float"],
          "probe strip:", res["context_probe_float"]["eigs_in_strip_float"])
json.dump(out, open(RUN + "/inertia_output.json", "w"), indent=1)
print("saved inertia_output.json")
