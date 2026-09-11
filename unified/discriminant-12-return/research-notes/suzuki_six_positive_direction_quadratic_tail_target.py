#!/usr/bin/env python3
"""Source-faithful terminal target for the six candidate-positive S10 directions.

Context
-------
After v13.387 restored the source-faithful rank-two Suzuki matrix and v13.392
reinstated the high-complement positivity chain, let

    C = {1,3,...,19}

and a finite high block

    F_M = {21,23,...,M}.

Define

    S_F = A_CC - A_C,F A_F,F^{-1} A_F,C.

Let W be the span of the six finite-Schur eigenvectors corresponding to
indices 5,...,10.  If the remaining tail operator after eliminating F obeys

    T_eff >= delta I

and R_W is the residual coupling from W into that remaining tail, then

    S_infty|_W >= S_F|_W - delta^{-1} R_W^* R_W.

Thus positivity of the six-dimensional candidate-positive sector follows if

    delta > lambda_max(S_W^{-1/2} R_W^* R_W S_W^{-1/2}).

This anisotropic quadratic test is sharper than demanding a uniform ten-column
solve residual at the 1e-11 scale.

Finite diagnostic sequence
--------------------------
Using an equal-width next tail band as an ordinary floating-point diagnostic:

    M      delta_crit(next equal-width band)
    199    0.4702
    399    0.3978
    799    0.2713
    1199   0.2108

The residual singular spectrum simultaneously becomes very low rank.  The
ratio sigma_2/sigma_1 was observed as

    M=199   5.0e-3
    M=399   2.1e-3
    M=799   9.1e-4
    M=1199  5.5e-4

and at M=1199,

    sigma_4 ~ 8.5e-10,
    sigma_5 ~ 1.7e-11.

These values are diagnostics only, not interval enclosures.

Certified tail comparison after v13.392
---------------------------------------
The source-faithful constituent certificates are again mutually consistent:

    A_[21,16001] >= 0.22 I,
    ||G_[21,16001],[16003,infinity)|| < 0.994,
    alpha_16003 > 4.673332491014484.

Therefore the Schur tail remaining after elimination of the finite-high block
has the certified lower floor

    delta_tail
      > 4.673332491014484 - 0.994^2/0.22
      = 0.18225976374175623.

The remaining proof task is now exact and fail-closed:

    certify delta_crit(full n>=16003 residual Gram) < 0.18225976374175623.

Empirical scaling diagnostic
----------------------------
A log-log least-squares fit of the four finite midpoint diagnostics to

    delta_crit(M) ~= C M^{-p}

gives approximately

    p ~= 0.45184,
    C ~= 5.45089.

This fit predicts crossing of the certified 0.182259... floor near M~1846 and
predicts delta_crit(16001)~0.0687.  This is useful only for implementation
planning; no extrapolated value is used as proof.

Guardrails
----------
* finite diagnostics and fitted scaling are not infinite-operator proofs;
* the first four tiny Schur eigenvalues are not called exact kernels;
* the fifth finite-section eigenvalue is not yet a certified infinite positive
  eigenvalue;
* no exact-zero, final inertia, RH, or GRH conclusion follows.
"""

import math

DIAGNOSTIC_DELTA_CRIT = {
    199: 0.4702,
    399: 0.3978,
    799: 0.2713,
    1199: 0.2108,
}

SIGMA2_OVER_SIGMA1 = {
    199: 5.0e-3,
    399: 2.1e-3,
    799: 9.1e-4,
    1199: 5.5e-4,
}

SIGMA4_M1199 = 8.5e-10
SIGMA5_M1199 = 1.7e-11

ALPHA_T = 4.673332491014484
FINITE_HIGH_GAP = 0.22
CROSS_NORM = 0.994
CERTIFIED_DELTA_TAIL = ALPHA_T - CROSS_NORM**2 / FINITE_HIGH_GAP


def loglog_fit(data):
    xs = [math.log(float(M)) for M in data]
    ys = [math.log(float(v)) for v in data.values()]
    xm = sum(xs)/len(xs)
    ym = sum(ys)/len(ys)
    slope = sum((x-xm)*(y-ym) for x, y in zip(xs, ys)) / sum((x-xm)**2 for x in xs)
    intercept = ym - slope*xm
    p = -slope
    C = math.exp(intercept)
    return p, C


FIT_P, FIT_C = loglog_fit(DIAGNOSTIC_DELTA_CRIT)
FIT_CROSSING_M = (FIT_C/CERTIFIED_DELTA_TAIL)**(1.0/FIT_P)
FIT_AT_16001 = FIT_C * 16001.0**(-FIT_P)


if __name__ == "__main__":
    print("equal-width diagnostic delta_crit:")
    for M, value in DIAGNOSTIC_DELTA_CRIT.items():
        print(f"  M={M:4d}: {value:.4f}")
    print("certified Schur-tail floor >", CERTIFIED_DELTA_TAIL)
    print("fit p =", FIT_P)
    print("fit C =", FIT_C)
    print("diagnostic fitted crossing M ~=", FIT_CROSSING_M)
    print("diagnostic fitted delta_crit(16001) ~=", FIT_AT_16001)
    assert CERTIFIED_DELTA_TAIL > 0.18225
    assert FIT_CROSSING_M < 2000.0
    print("guardrail: fitted crossing is diagnostic only; full residual Gram still open")
