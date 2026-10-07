#!/usr/bin/env python3
"""Pair fixed-normalizer seven-column midpoint reductions; never certify."""
import argparse
import json
import hashlib
from pathlib import Path
import mpmath as mp

DPS = 180


def norm(x):
    return mp.sqrt(mp.fsum(abs(x[i])**2 for i in range(x.rows)))


def snorm(a):
    e, _ = mp.eigsy((a+a.T)/2)
    return max(abs(e[0]), abs(e[e.rows-1]))


def state(path, sector, cutoff):
    obj = json.loads(Path(path).read_text())
    if obj.get("schema") != "cone.normalized-joint-reduction.midpoint.v1":
        raise RuntimeError("wrong producer schema")
    if obj.get("certification_ready") is not False:
        raise RuntimeError("midpoint consumer refuses unsupported certification label")
    if obj["normalizer"]["sector"] != sector:
        raise RuntimeError("normalizer sector mismatch")
    normal = dict(obj["normalizer"])
    recorded = normal.pop("normalizer_sha256")
    canonical = json.dumps(normal, sort_keys=True, separators=(",", ":")).encode()
    if hashlib.sha256(canonical).hexdigest() != recorded:
        raise RuntimeError("normalizer content hash mismatch")
    matches = [r for r in obj["rows"] if r["cutoff"] == cutoff and r["sector"] == sector]
    if len(matches) != 1:
        raise RuntimeError(("cutoff/sector row missing or duplicated", path, sector, cutoff))
    r = matches[0]
    if r["normalizer_sha256"] != recorded:
        raise RuntimeError("row normalizer hash mismatch")
    if r["certification"]["ready"] is not False:
        raise RuntimeError("unexpected certification claim")
    m = mp.matrix(r["M_trial_midpoint"])
    if (m.rows, m.cols) != (7, 7):
        raise RuntimeError("wrong affine matrix shape")
    j = m[:6, :6]; beta = -m[:6, 6]; eta = -m[6, 6]
    eig, _ = mp.eigsy(j)
    if eig[0] <= 0:
        raise RuntimeError(("normalized J not positive in midpoint", sector, cutoff, str(eig[0])))
    inverse = j**-1
    return dict(obj=obj, row=r, m=m, j=j, beta=beta, eta=eta, inverse=inverse,
                k=eta+(beta.T*inverse*beta)[0])


def pair_bound(e, o, xkey):
    re, ro = e["inverse"], o["inverse"]
    xe, xo = e[xkey], o[xkey]
    da, dx = o["j"]-e["j"], xo-xe
    be = snorm(da)*norm(ro*xo)*norm(re*xo)+norm(dx)*(norm(re*xo)+norm(re*xe))
    bo = snorm(da)*norm(ro*xe)*norm(re*xe)+norm(dx)*(norm(ro*xo)+norm(ro*xe))
    return min(be, bo), be, bo


def analyze(e0, e1, o0, o1):
    for a, b in ((e0, e1), (o0, o1)):
        for key in ("normalizer_sha256", "frozen_base_P_sha256", "remote_start"):
            if a["row"][key] != b["row"][key]:
                raise RuntimeError(("frozen-coordinate/source mismatch", key))
    if e0["row"]["remote_start"] != o0["row"]["remote_start"]:
        raise RuntimeError("parity source-frontier mismatch")
    ds = (o0["m"]-o1["m"])[6, 6]-(e0["m"]-e1["m"])[6, 6]
    after, ae, ao = pair_bound(e1, o1, "beta")
    before, be, bo = pair_bound(e0, o0, "beta")
    actual = (o1["k"]-o0["k"])-(e1["k"]-e0["k"])
    bound = abs(ds)+after+before
    if bound < abs(actual):
        raise RuntimeError("midpoint anchor-aware paired inequality failed")
    return {"schema": "cone.normalized-joint-pair.midpoint.v1",
            "R": e0["row"]["cutoff"], "R2": e1["row"]["cutoff"],
            "remote_start": e0["row"]["remote_start"],
            "even_increment": mp.nstr(e1["k"]-e0["k"], 100),
            "odd_increment": mp.nstr(o1["k"]-o0["k"], 100),
            "odd_minus_even_increment": mp.nstr(actual, 100),
            "delta_sigma": mp.nstr(ds, 100),
            "next_anchor_paired_bound": mp.nstr(after, 100),
            "old_anchor_paired_bound": mp.nstr(before, 100),
            "paired_bound_min_choices": mp.nstr(bound, 100),
            "bound_over_abs_actual": mp.nstr(bound/abs(actual), 70) if actual else None,
            "certification_ready": False,
            "guardrail": "Midpoint only. Includes both anchor-defect terms; no imported full-Q gamma, no outward theorem claim."}


def main():
    p = argparse.ArgumentParser()
    for label in ("even-old", "even-new", "odd-old", "odd-new"):
        p.add_argument("--"+label, required=True)
    p.add_argument("--R", type=int, default=64000)
    p.add_argument("--R2", type=int, default=128000)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    with mp.workdps(DPS):
        out = analyze(state(a.even_old, "even-v", a.R), state(a.even_new, "even-v", a.R2),
                      state(a.odd_old, "odd-v", a.R), state(a.odd_new, "odd-v", a.R2))
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
