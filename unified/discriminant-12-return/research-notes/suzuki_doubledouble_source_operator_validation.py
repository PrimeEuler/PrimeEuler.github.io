#!/usr/bin/env python3
"""Fail-closed validation of the double-double source-operator engine.

Compare the independent DD displacement-rank evaluator against the existing
arbitrary-precision componentwise source-faithful matrix producer on a small
finite section.  This checks:
  * exact same-parity off-diagonal formula;
  * high-precision z_n generator;
  * cusp/prime/archimedean diagonal;
  * parity pole sign and vector;
  * source coefficients.

The validation is deliberately small because the reference producer uses
arbitrary-precision quadrature.  Once entrywise agreement is established,
the DD engine can be used matrix-free at M3999/4000.
"""
from __future__ import annotations

import argparse

import mpmath as mp
import numpy as np

from suzuki_doubledouble_source_operator import (
    dd_column,
    dd_to_mpf,
    hp_parity_data,
)
from suzuki_form_core_bulk_subtracted_resonance import (
    parity_components,
    source_overlap,
)


def one_sector(max_mode: int, sector: str, dps: int):
    modes = np.arange(
        1 if sector == "even-v" else 2,
        max_mode + 1,
        2,
        dtype=int,
    )

    data = hp_parity_data(
        modes,
        sector,
        dps=dps,
        arch_terms=140,
        correction_terms=40,
    )

    with mp.workdps(dps):
        ns, _, _, _, _, ref = parity_components(max_mode, sector)
        if list(modes) != ns:
            raise RuntimeError((sector, "reference mode mismatch"))

        max_abs = mp.mpf(0)
        max_rel = mp.mpf(0)
        worst = None

        for j in range(len(modes)):
            ah, al = dd_column(data, j)
            for i in range(len(modes)):
                got = dd_to_mpf(ah[i], al[i])
                want = ref[i, j]
                err = abs(got - want)
                scale = max(abs(want), mp.mpf("1e-80"))
                rel = err / scale
                if err > max_abs:
                    max_abs = err
                    worst = (i, j, modes[i], modes[j], got, want)
                if rel > max_rel:
                    max_rel = rel

        source_abs = mp.mpf(0)
        for i, n in enumerate(modes):
            got = dd_to_mpf(data.source_hi[i], data.source_lo[i])
            want = source_overlap(int(n))
            source_abs = max(source_abs, abs(got - want))

        print("\nsector =", sector)
        print("dimension =", len(modes))
        print("max matrix abs error =", mp.nstr(max_abs, 30))
        print("max matrix rel error =", mp.nstr(max_rel, 30))
        print("max source abs error =", mp.nstr(source_abs, 30))
        if worst is not None:
            print(
                "worst entry =",
                (worst[2], worst[3]),
                "got =", mp.nstr(worst[4], 30),
                "want =", mp.nstr(worst[5], 30),
            )

        # The Taylor truncation, 40-term exponential correction, and
        # two-float arithmetic should comfortably clear this threshold.
        if not max_abs < mp.mpf("5e-25"):
            raise RuntimeError((sector, "DD matrix validation failed", max_abs))
        if not source_abs < mp.mpf("5e-31"):
            raise RuntimeError((sector, "DD source validation failed", source_abs))

        return max_abs, source_abs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-mode", type=int, default=32)
    parser.add_argument("--dps", type=int, default=120)
    args = parser.parse_args()

    rows = [
        one_sector(args.max_mode, "even-v", args.dps),
        one_sector(args.max_mode, "odd-v", args.dps),
    ]

    print("\nPASS: double-double source operator matches the independent")
    print("arbitrary-precision componentwise producer on both parity sections.")
    print(
        "Guardrail: midpoint arithmetic validation only; no outward interval "
        "or M3999 capacity theorem is asserted."
    )


if __name__ == "__main__":
    main()
