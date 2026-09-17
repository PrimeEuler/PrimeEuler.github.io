#!/usr/bin/env python3
"""M16001 Q/N outward-formation transcript.

Fail-closed arithmetic certificate scaffold.  This file deliberately contains
no accepted Q/N radius literal.  It turns *emitted* long-double dot-product
magnitude transcripts into entrywise gamma_k radii and a Frobenius/operator
majorant.

The producer/replay must supply an NPZ with arrays:
    qn_mid      : (m,n) long-double-compatible midpoint entries
    qn_absprod  : (m,n) nonnegative sum_i |x_i y_i| for each dot product
    qn_k        : scalar or (m,n) positive integer operation/dot lengths

Optional metadata strings/integers may be included; they are printed but do
not enter the certificate.  No theorem is promoted by this helper alone.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np


def gamma(k: np.ndarray, u: np.longdouble) -> np.ndarray:
    kk = np.asarray(k, dtype=np.longdouble)
    ku = kk * u
    if np.any(kk <= 0) or np.any(ku >= 1):
        raise ValueError("invalid gamma_k regime")
    return ku / (np.longdouble(1) - ku)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript", type=Path)
    args = ap.parse_args()

    # The v13.510 arithmetic model is binary extended precision with a
    # 64-bit significand.  Fail closed on platforms that do not provide it.
    finfo = np.finfo(np.longdouble)
    p = int(finfo.nmant + 1)
    if p < 64:
        raise RuntimeError(f"longdouble significand too small: p={p}")
    u = np.longdouble(2) ** np.longdouble(-p)

    with np.load(args.transcript, allow_pickle=False) as z:
        required = {"qn_mid", "qn_absprod", "qn_k"}
        missing = required.difference(z.files)
        if missing:
            raise RuntimeError(f"missing emitted fields: {sorted(missing)}")
        mid = np.asarray(z["qn_mid"], dtype=np.longdouble)
        sabs = np.asarray(z["qn_absprod"], dtype=np.longdouble)
        kval = np.asarray(z["qn_k"])

    if mid.ndim != 2 or sabs.shape != mid.shape:
        raise RuntimeError("qn_mid/qn_absprod shape mismatch")
    if not np.all(np.isfinite(mid)) or not np.all(np.isfinite(sabs)):
        raise RuntimeError("nonfinite Q/N transcript")
    if np.any(sabs < 0):
        raise RuntimeError("negative absolute-product majorant")
    if kval.ndim == 0:
        kval = np.full(mid.shape, int(kval), dtype=np.int64)
    elif kval.shape != mid.shape:
        raise RuntimeError("qn_k must be scalar or match qn_mid")
    if not np.issubdtype(kval.dtype, np.integer):
        if not np.all(kval == np.floor(kval)):
            raise RuntimeError("nonintegral qn_k")
        kval = kval.astype(np.int64)

    rad = gamma(kval, u) * sabs
    # Every entry lies in [mid-rad,mid+rad].  For the unknown exact block B,
    # ||B||_2 <= ||mid||_2 + ||rad||_F.  np.linalg on longdouble is not
    # portable, so use the Frobenius midpoint majorant as a conservative
    # theorem-safe fallback; a separately certified spectral midpoint bound
    # can sharpen this later without changing entry radii.
    mid_frob = np.sqrt(np.sum(mid * mid, dtype=np.longdouble))
    rad_frob = np.sqrt(np.sum(rad * rad, dtype=np.longdouble))
    op_upper = mid_frob + rad_frob

    out = {
        "status": "PASS",
        "longdouble_significand_bits": p,
        "unit_roundoff": str(u),
        "shape": list(mid.shape),
        "k_min": int(np.min(kval)),
        "k_max": int(np.max(kval)),
        "max_absprod": str(np.max(sabs)),
        "max_entry_radius": str(np.max(rad)),
        "radius_frobenius": str(rad_frob),
        "midpoint_frobenius": str(mid_frob),
        "QN_operator_upper_frobenius_majorant": str(op_upper),
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
