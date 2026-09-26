#!/usr/bin/env python3
"""Fresh M=3999/4000 midpoint anatomy for rho=0.02 endpoint pair.

Uses the parameterized source-faithful endpoint builder with rho=0.02.

Layouts:
  even-v core {5,7,...,23}, buffer {25,27,...,3999}
  odd-v  core {6,8,...,24}, buffer {26,28,...,4000}

Reports both endpoint signs:
  sign=-1: A - 0.02 B_sm
  sign=+1: A + 0.02 B_sm

This is a midpoint gate only.  No infinite endpoint theorem is promoted here.
"""
from __future__ import annotations

import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import effective_core


RHO = 0.02


def layouts():
    return [
        (
            "even-v",
            np.arange(5,24,2,dtype=int),
            np.arange(25,4000,2,dtype=int),
        ),
        (
            "odd-v",
            np.arange(6,25,2,dtype=int),
            np.arange(26,4001,2,dtype=int),
        ),
    ]


def inertia(vals,tol=1e-10):
    vals=np.asarray(vals)
    return (
        int(np.sum(vals < -tol)),
        int(np.sum(np.abs(vals) <= tol)),
        int(np.sum(vals > tol)),
    )


def main():
    print("rho=0.02 M3999/4000 endpoint midpoint anatomy")
    for sign,name in ((-1,"minus"),(+1,"plus")):
        print("\nendpoint =",name)
        for sector,core,buffer_ in layouts():
            out=effective_core(
                core,
                buffer_,
                sector,
                sign=sign,
                rho=RHO,
            )
            vals=out["eigenvalues"]
            piv=out["polefree_pivots"]

            print("\nsector =",sector)
            print("min pole-free pivot =",float(np.min(piv)))
            print("pole denominator =",out["pole_woodbury_denominator"])
            print("eigenvalues =",[f"{x:.15g}" for x in vals])
            print("inertia =",inertia(vals))

            assert np.min(piv) > 0
            assert out["pole_woodbury_denominator"] > 0

            if sign == -1:
                assert inertia(vals) == (4,0,6)
            else:
                assert inertia(vals) == (0,0,10)

    print("\nPASS rho=0.02 midpoint anatomy")
    print("minus: four negative + six positive in both parities")
    print("plus: ten positive in both parities")
    print(
        "Guardrail: midpoint only; exact-dyadic freezes and outward "
        "finite/remote certificates are still required."
    )


if __name__=="__main__":
    main()
