#!/usr/bin/env python3
"""Deterministic near-block coupling SVD producer for the compression-error certificate.

Builds the exact front-to-near coupling matrix B (binary64, deterministic) for
both parities and computes its full SVD via LAPACK (numpy.linalg.svd, no ARPACK,
no randomness). Reports sigma_1 and sigma_{r+1} for the rank-sweep ranks.

B[near, front] with near = parity modes in (8000,16000], front = parity modes
in [1,8000], via the exact_cross formula (pole-free off-diagonal + pole rank-1).

Determinism: numpy.linalg.svd uses LAPACK dgesdd — fully deterministic, no
seeding required. Byte-reproducibility is verified by running twice and
comparing SHA-256 of the singular-value arrays.
"""
from __future__ import annotations
import hashlib
import json
import os
import sys

import numpy as np

# Import from the committed repository module (lives alongside this script in
# research-notes/). v14.070 audit finding: the previous version imported from
# an uncommitted /tmp/eff_core.py, which is byte-identical to this module.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from suzuki_endpoint_M3999_midpoint_effective_core import (  # noqa: E402
    z_source_faithful, pole_vector)


def lattice(sector, a, b):
    start = a
    want_even = (sector == "odd-v")
    if (start % 2 == 0) != want_even:
        start += 1
    end = b - 1
    if (end % 2 == 0) != want_even:
        end -= 1
    return np.arange(start, end + 1, 2, dtype=int)


def exact_cross(rows, cols, sector, chunk=200):
    rr = rows.astype(float)
    cc = cols.astype(float)
    zr = z_source_faithful(rows)
    zc = z_source_faithful(cols)
    pr, alpha = pole_vector(rows, sector)
    pc, _ = pole_vector(cols, sector)
    out = np.empty((len(rows), len(cols)), dtype=float)
    for a in range(0, len(rows), chunk):
        b = min(a + chunk, len(rows))
        r = rr[a:b]
        z = zr[a:b]
        p = pr[a:b]
        den = r[:, None] ** 2 - cc[None, :] ** 2
        C = (2.0 / np.pi) * (z[:, None] * cc[None, :] - r[:, None] * zc[None, :]) / den
        C += alpha * np.outer(p, pc)
        out[a:b] = C
    return out


def parity_modes(sector, max_mode):
    start = 1 if sector == "even-v" else 2
    return np.arange(start, max_mode + 1, 2, dtype=int)


RANKS = [24, 32, 48, 64, 96]


def one_sector(sector):
    near = lattice(sector, 8001, 16000)
    front = parity_modes(sector, 8000)
    # even-v: 4000 near modes; odd-v: 3999 (range (8000,16000] lattice convention)
    assert len(front) == 4000 and len(near) in (3999, 4000), (len(near), len(front))
    B = exact_cross(near, front, sector)
    # Full SVD via LAPACK dgesdd — deterministic, no randomness.
    s = np.linalg.svd(B, compute_uv=False)
    assert np.all(np.diff(s) <= 0), "singular values not descending"
    return {
        "sector": sector,
        "n_near": len(near),
        "n_front": len(front),
        "sigma_1": float(s[0]),
        "sigma_min": float(s[-1]),
        "sigma_rplus1": {str(r): float(s[r]) for r in RANKS},  # s[r] = sigma_{r+1} (0-based)
        "spectrum_head": [float(x) for x in s[:12]],
        "spectrum_tail_sample": [float(s[i]) for i in [24, 32, 48, 64, 96, 128, 256, 512, 1000, 2000, len(s)-1]],
        "s_hash": hashlib.sha256(s.tobytes()).hexdigest(),
    }


def main():
    import sys as _sys
    out = {}
    for sector in ("even-v", "odd-v"):
        print(f"building B and SVD for {sector} ...", file=_sys.stderr, flush=True)
        out[sector] = one_sector(sector)
        print(f"  sigma_1 = {out[sector]['sigma_1']:.6e}", file=_sys.stderr, flush=True)
        for r in RANKS:
            print(f"  sigma_{r+1} = {out[sector]['sigma_rplus1'][str(r)]:.6e}", file=_sys.stderr, flush=True)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
