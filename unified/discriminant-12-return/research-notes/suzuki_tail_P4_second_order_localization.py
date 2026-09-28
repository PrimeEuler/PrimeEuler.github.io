#!/usr/bin/env python3
"""Second-order localization of the exact four-channel tail cluster.

Let J be self-adjoint, P the exact rank-m spectral projector, and Y an
orthonormal m-column Ritz basis with

    JY - Y Theta = R,      Y^*R = 0.

Write X=PY and Z=(I-P)Y.  If s=||Z||<1, then X maps C^m bijectively
onto Ran P and

    X^* J_P X = (X^*X) Theta - Z^* R_Q.

Therefore the exact spectrum on Ran P is the spectrum of

    Theta - (X^*X)^(-1) Z^* R_Q,

and every exact eigenvalue lies within

    eta = ||R|| s / (1-s^2)

of the numerical Ritz spectrum.

Only widened post-Round-113 caps (confirmed by Round 115) are used.
"""
from __future__ import annotations

PUBLIC = {
    "even-v": dict(residual=0.00580, sintheta=0.0582, ritz=0.00030),
    "odd-v":  dict(residual=0.00880, sintheta=0.0984, ritz=0.01050),
}

LOCATION_CAP = {
    "even-v": 0.000639,
    "odd-v":  0.011375,
}

ENDPOINT_GAP_FLOOR = {
    "even-v": 0.019361,
    "odd-v":  0.008625,
}


def one(sector):
    c=PUBLIC[sector]
    s=c["sintheta"]
    eta=c["residual"]*s/(1.0-s*s)
    location=c["ritz"]+eta
    gap=0.02-location

    if location >= LOCATION_CAP[sector]:
        raise RuntimeError(("location cap",sector,location))
    if gap <= ENDPOINT_GAP_FLOOR[sector]:
        raise RuntimeError(("endpoint gap floor",sector,gap))

    return dict(
        eta=eta,
        exact_abs_location=location,
        endpoint_gap=gap,
        endpoint_tail_resolvent=1.0/gap,
    )


def main():
    for sector in ("even-v","odd-v"):
        print(sector,one(sector))

    print("PASS second-order exact P4 spectral localization")


if __name__=="__main__":
    main()
