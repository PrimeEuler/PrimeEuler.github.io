#!/usr/bin/env python3
"""Exact-rational consumer of audited base/remote complement certificates.

Derives a coarse full-Q floor through cutoff 256000. This does not certify
the normalized producer's source/trace/assembly/residual arithmetic.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def harmonic_upper(n):
    # Each rational ceiling upper-bounds 1/k; only integer arithmetic occurs.
    q = 10**12
    return F(sum((q+k-1)//k for k in range(1, n+1)), q)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base-replay", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    raw = args.base_replay.read_bytes()
    base = json.loads(raw)
    if base["mu"] != 1 or base["Lambda"] != 1:
        raise RuntimeError("wrong base certificate geometry")
    bysector = {r["sector"]: r for r in base["rows"]}
    if set(bysector) != {"even-v", "odd-v"}:
        raise RuntimeError("wrong base sectors")
    nold, nnew = 4000, 124000
    hold, hnew = harmonic_upper(nold), harmonic_upper(nnew)
    assert hold < 9 and hnew < 13
    pi_lower = F(157, 50)
    displacement_squared_upper = (F(10)/pi_lower)**2 * 9 * 13
    assert displacement_squared_upper < F(69, 2)**2
    # cosh(1/2) <= 1+1/8+(1/384)/(1-1/120) < 8/7.
    cosh_upper = 1+F(1, 8)+F(1, 384)/(1-F(1, 120))
    assert cosh_upper < F(8, 7)
    pole_upper = 4*F(8, 7)**2
    assert pole_upper < F(11, 2)
    cross_upper = F(40)
    assert F(69, 2)+F(11, 2) == cross_upper
    rows = []
    for sector, gamma0, public in (("even-v", F("7.79e-6"), F("2.95e-19")),
                                    ("odd-v", F("3.26e-5"), F("2.16e-17"))):
        r = bysector[sector]
        if r["dimension"] != 4000 or r["PASS"] is not True:
            raise RuntimeError("base replay failed")
        if F(r["certified_complement_lower"]) <= gamma0:
            raise RuntimeError("rounded-down base floor not supported")
        floor = gamma0/(1+cross_upper/gamma0)**2
        if floor <= public:
            raise RuntimeError("public full-Q floor not below exact rational bound")
        rows.append({"sector": sector, "base_floor_used": str(gamma0),
                     "base_replay_floor": r["certified_complement_lower"],
                     "partial_shell_Schur_floor": "1", "cross_block_norm_cap": "40",
                     "full_Q_floor_exact_rational": str(floor),
                     "full_Q_floor_public": "2.95e-19" if sector == "even-v" else "2.16e-17"})
    out = {"schema": "cone.fullq-coercivity-bridge.v1", "passed": True,
           "cutoff_scope": "8000 <= R <= 256000; frozen base six-plane embedded by zeros",
           "base_replay_sha256": hashlib.sha256(raw).hexdigest(), "rows": rows,
           "harmonic_4000_upper": str(hold), "harmonic_124000_upper": str(hnew),
           "displacement_squared_upper": str(displacement_squared_upper),
           "pole_norm_upper": str(pole_upper),
           "theorem_inputs": ["v14.029/v14.031 exact shifted-8k complementary floor",
                              "v14.034/v14.036 exact full 8k front positivity",
                              "v14.044/v14.071 nested remote Schur unit floor",
                              "v14.025/v14.034 exact scalar majorants |z|<=10 and parity pole norm"],
           "audit_status": "derived certificate awaiting independent bridge/provenance audit",
           "normalized_joint_certification_ready": False}
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
