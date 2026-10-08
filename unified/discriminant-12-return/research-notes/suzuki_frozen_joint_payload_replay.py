#!/usr/bin/env python3
"""Replay serialized midpoint reductions with exact rational elimination.

This validates the frozen payloads, not their relation to the exact source.
Only Python's standard library is required.
"""
import argparse
import hashlib
import json
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path


def solve_spd(a, b):
    n = len(a)
    a = [row[:] for row in a]
    b = b[:]
    for k in range(n):
        if a[k][k] <= 0:
            raise RuntimeError("serialized J failed exact positive-pivot test")
        for i in range(k+1, n):
            q = a[i][k]/a[k][k]
            for j in range(k+1, n):
                a[i][j] -= q*a[k][j]
            b[i] -= q*b[k]
    x = [F(0)]*n
    for i in reversed(range(n)):
        x[i] = (b[i]-sum(a[i][j]*x[j] for j in range(i+1, n)))/a[i][i]
    return x


def decimal(x):
    with localcontext() as c:
        c.prec = 100
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--payload-root", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    root = args.payload_root
    manifest = json.loads((root/"artifact_manifest.json").read_text())
    for item in manifest:
        raw = (root/item["filename"]).read_bytes()
        if hashlib.sha256(raw).hexdigest() != item["json_sha256"]:
            raise RuntimeError("frozen JSON byte hash mismatch")
        if item["producer_commit"] != "14face275435522599ed73a74a5758e9f9b5699f":
            raise RuntimeError("wrong producer provenance")
    values = {}
    identifiers = {}
    for parity in ("even-v", "odd-v"):
        for cutoff in (64000, 128000):
            obj = json.loads((root/f"joint-{cutoff}-{parity}.json").read_text())
            if obj["certification_ready"] is not False or len(obj["rows"]) != 1:
                raise RuntimeError("wrong certification label or row count")
            normalizer = dict(obj["normalizer"])
            recorded = normalizer.pop("normalizer_sha256")
            canonical = json.dumps(normalizer, sort_keys=True, separators=(",", ":")).encode()
            if hashlib.sha256(canonical).hexdigest() != recorded:
                raise RuntimeError("frozen normalizer hash mismatch")
            row = obj["rows"][0]
            if (row["sector"], row["cutoff"], row["remote_start"]) != (parity, cutoff, 32000):
                raise RuntimeError("wrong parity/cutoff/source frontier")
            if row["normalizer_sha256"] != recorded:
                raise RuntimeError("row normalizer mismatch")
            if row["certification"]["ready"] is not False:
                raise RuntimeError("unsupported source certificate")
            key = (recorded, row["frozen_base_P_sha256"])
            if parity in identifiers and identifiers[parity] != key:
                raise RuntimeError("coordinates changed between cutoffs")
            identifiers[parity] = key
            m = [[F(x) for x in line] for line in row["M_trial_midpoint"]]
            if len(m) != 7 or any(len(line) != 7 for line in m):
                raise RuntimeError("wrong affine shape")
            if any(m[i][j] != m[j][i] for i in range(7) for j in range(7)):
                raise RuntimeError("serialized matrix not symmetric")
            j = [line[:6] for line in m[:6]]
            beta = [-m[i][6] for i in range(6)]
            x = solve_spd(j, beta)
            values[parity, cutoff] = -m[6][6]+sum(beta[i]*x[i] for i in range(6))
    even = values["even-v", 128000]-values["even-v", 64000]
    odd = values["odd-v", 128000]-values["odd-v", 64000]
    paired = json.loads((root/"normalized-joint-pair-64000-128000.json").read_text())
    for name, exact in (("even_increment", even), ("odd_increment", odd),
                        ("odd_minus_even_increment", odd-even)):
        if abs(F(paired[name])-exact) >= F("1e-98"):
            raise RuntimeError("CI scalar disagrees with exact serialized-matrix elimination")
    if F(paired["paired_bound_min_choices"]) < abs(odd-even):
        raise RuntimeError("serialized midpoint paired bound failed")
    out = {"schema": "cone.frozen-joint-payload-replay.v1", "passed": True,
           "positive_serialized_J_matrices": 4,
           "even_increment_exact_serialized_decimal": decimal(even),
           "odd_increment_exact_serialized_decimal": decimal(odd),
           "odd_minus_even_exact_serialized_decimal": decimal(odd-even),
           "CI_pair_scalar_tolerance": "1e-98", "source_certification_ready": False,
           "scope": "Exact Fraction check of serialized midpoint matrices; not an exact-source certificate"}
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
