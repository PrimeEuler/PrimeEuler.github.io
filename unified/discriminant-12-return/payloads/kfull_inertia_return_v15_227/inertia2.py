#!/usr/bin/env python3
"""Interval inertia, attempt 2: cached interval matrices + symmetric
greedy pivoting (order fixed from float midpoints, design D7).

Runs, per sector:
  - pivoted interval LDL^T at x_diag - delta, x_diag, x_diag + delta
    (primary declared point: midpoint of the certified replay gap);
  - for the odd sector additionally at x_alt (midpoint of the finite
    section's float spectral gap nearest below x_diag; declared
    secondary point, exact Fraction from the probe decimals).
All certificate statements come only from the interval runs.
"""
import sys, json, time, os
sys.set_int_max_str_digits(1000000)
sys.path.insert(0, "/home/hatch/workspace/d12/laneA_modules")
from fractions import Fraction as F
import numpy as np
import suzuki_certified_remote_z as ZM

RUN = "/home/hatch/workspace/d12/lane_b/sandbox/runs/20261031-kfull-inertia"
CONST = json.load(open("/home/hatch/workspace/d12/dm490/far585/ctgate/constants.json"))
SECTORS = {"odd_lattice_b512001": {"b": 512001, "ckey": "even-v"},
           "even_lattice_b512002": {"b": 512002, "ckey": "odd-v"}}
GRID = 1 << 512

def rout(iv):
    lo, hi = iv
    return (F(lo.numerator * GRID // lo.denominator, GRID),
            F(-((-hi.numerator * GRID) // hi.denominator), GRID))
def iadd(a, b): return rout((a[0] + b[0], a[1] + b[1]))
def isub(a, b): return rout((a[0] - b[1], a[1] - b[0]))
def imul(a, b):
    v = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return rout((min(v), max(v)))
def iscale(a, q):
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
C_IV = (2 / pi_hi, 2 / pi_lo)

def build_matrix(name, S, drows):
    cache = RUN + f"/matrix_cache_{name}.json"
    if os.path.exists(cache):
        raw = json.load(open(cache))
        return [[(F(a), F(b)) for a, b in row] for row in raw]
    C = CONST[S["ckey"]]
    sigma = C["sigma"]; L = F(C["L_rational"]); t = F(C["t_rational"])
    modes = [S["b"] + 2 * j for j in range(100)]
    ziv = {}
    for n in modes:
        r = ZM.evaluate(n, action_precision=True)
        ziv[n] = (F(r["lower_rational"]), F(r["upper_rational"]))
    piv = {n: F(int(L * n / (n * n + t) * (1 << 256)), 1 << 256) for n in modes}
    div = {r["n"]: (F(r["lo"]), F(r["hi"])) for r in drows}
    A = [[None] * 100 for _ in range(100)]
    for i, N in enumerate(modes):
        for j, m in enumerate(modes):
            if i == j:
                A[i][j] = iadd(div[N], pt(2 * sigma * piv[N] * piv[N]))
            else:
                num = isub(iscale(ziv[N], m), iscale(ziv[m], N))
                A[i][j] = iadd(iscale(imul(C_IV, num), F(1, N * N - m * m)),
                               pt(2 * sigma * piv[N] * piv[m]))
    json.dump([[(str(a), str(b)) for a, b in row] for row in A], open(cache, "w"))
    return A

def greedy_perm(Af, x):
    """Greedy symmetric pivot order from the float midpoint matrix."""
    M = Af - x * np.eye(len(Af)); idx = list(range(len(Af))); perm = []
    Mc = M.copy()
    for k in range(len(Af)):
        j = k + int(np.argmax(np.abs(np.diag(Mc)[k:])))
        if j != k:
            Mc[[k, j], :] = Mc[[j, k], :]; Mc[:, [k, j]] = Mc[:, [j, k]]
            idx[k], idx[j] = idx[j], idx[k]
        perm.append(idx[k])
        if Mc[k, k] != 0:
            f = Mc[k + 1:, k] / Mc[k, k]
            Mc[k + 1:, k + 1:] -= np.outer(f, Mc[k, k + 1:])
    return perm

def ldl_count(A, x, perm):
    J = len(A)
    P = [[A[perm[i]][perm[j]] for j in range(J)] for i in range(J)]
    M = [[P[i][j] if i != j else isub(P[i][j], pt(x)) for j in range(J)] for i in range(J)]
    D = [None] * J; L = [[pt(0)] * J for _ in range(J)]
    minmargin = None
    for k in range(J):
        s = M[k][k]
        for j in range(k):
            s = isub(s, imul(isq(L[k][j]), D[j]))
        D[k] = s
        if s[0] <= 0 <= s[1]:
            return {"ok": False, "fail_pivot": k,
                    "pivot_interval": (str(s[0]), str(s[1])),
                    "pivot_interval_float": (float(s[0]), float(s[1]))}
        margin = s[0] if s[0] > 0 else -s[1]
        minmargin = margin if minmargin is None else min(minmargin, margin)
        for i in range(k + 1, J):
            tt = M[i][k]
            for j in range(k):
                tt = isub(tt, imul(imul(L[i][j], D[j]), L[k][j]))
            L[i][k] = imul(tt, irecip(D[k]))
    neg = sum(1 for d in D if d[1] < 0); pos = sum(1 for d in D if d[0] > 0)
    return {"ok": True, "neg": neg, "pos": pos,
            "min_pivot_margin_float": float(minmargin)}

replay = json.load(open(RUN + "/replay_output.json"))
out = {}
for name, S in SECTORS.items():
    t0 = time.time()
    rows = replay["replay"][name]["rows"]
    srt = sorted(rows, key=lambda r: F(r["lo"]))
    hi1, lo2 = F(srt[0]["hi"]), F(srt[1]["lo"])
    x = (hi1 + lo2) / 2; delta = (lo2 - hi1) / 4
    A = build_matrix(name, S, rows)
    Af = np.array([[float((A[i][j][0] + A[i][j][1]) / 2) for j in range(100)] for i in range(100)])
    ev = np.linalg.eigvalsh(Af)
    res = {"x_diag": str(x), "x_diag_float": float(x), "delta": str(delta),
           "delta_float": float(delta)}
    perm = greedy_perm(Af, float(x))
    res["perm_from_float_greedy"] = perm
    for label, xx in (("x_minus_delta", x - delta), ("x", x), ("x_plus_delta", x + delta)):
        res[label] = ldl_count(A, xx, perm)
    if name.startswith("odd"):
        # secondary point: midpoint of the float spectral gap containing
        # the two probe eigenvalues bracketing x_diag from below/above
        below = max(v for v in ev if v < float(x)); above = min(v for v in ev if v > float(x))
        xa = F(str(round((below + above) / 2, 9))); da = F(str(round((above - below) / 4, 9)))
        res["x_alt"] = {"x": str(xa), "x_float": float(xa), "delta": str(da),
                        "delta_float": float(da),
                        "bracketing_probe_eigs": (float(below), float(above)),
                        "perm": greedy_perm(Af, float(xa))}
        for label, xx in (("x_minus_delta", xa - da), ("x", xa), ("x_plus_delta", xa + da)):
            res["x_alt"][label] = ldl_count(A, xx, res["x_alt"]["perm"])
    res["seconds"] = round(time.time() - t0, 1)
    out[name] = res
    print(name, {k: (v.get("neg"), v.get("ok"), v.get("fail_pivot")) for k, v in res.items()
                 if isinstance(v, dict) and "ok" in v},
          "x_alt:", {k: (v.get("neg"), v.get("ok"), v.get("fail_pivot")) for k, v in
                     res.get("x_alt", {}).items() if isinstance(v, dict) and "ok" in v})
json.dump(out, open(RUN + "/inertia2_output.json", "w"), indent=1)
print("saved inertia2_output.json")
