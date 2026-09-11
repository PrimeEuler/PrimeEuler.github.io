#!/usr/bin/env python3
"""Source-faithful terminal target for the six candidate-positive S10 directions.

Context
-------
After External Audit Round 20, the source-faithful rank-two off-diagonal
matrix is restored.  For the low core

    C = {1,3,...,19}

and a finite high block

    F_M = {21,23,...,M},

define the finite Schur complement

    S_F = A_CC - A_C,F A_F,F^{-1} A_F,C.

Let W be the span of the six finite-Schur eigenvectors corresponding to
indices 5,...,10 after ordering the ten eigenvalues increasingly.  If the
remaining tail operator after eliminating F satisfies

    T_eff >= delta I,

and R is the residual coupling from W into the remaining tail, then

    S_infty|_W >= S_F|_W - delta^{-1} R^* R.

Hence positivity of the six-dimensional candidate-positive sector follows
whenever

    delta > lambda_max(S_W^{-1/2} R_W^* R_W S_W^{-1/2}).

This is strictly sharper than demanding a uniform 10-column solve residual at
the 1e-11 scale, because the residual is strongly anisotropic and the dominant
remote-tail channel couples mostly into directions whose finite Schur values
are O(1), not into the tiny fifth direction.

Finite diagnostic sequence
--------------------------
Using an equal-width next tail band as a midpoint diagnostic gives

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

These are ordinary floating-point diagnostics only.

Tail-coercivity comparison target
---------------------------------
If one provisionally combines the previously targeted finite-high lower bound

    A0_[21,16001] >= 0.22 I

with the previously targeted source-faithful cross estimate

    ||G|| < 0.994

and the analytic raw tail lower bound

    alpha_16003 > 4.6732,

then the standard two-block Schur lower bound gives

    delta_tail > 4.6732 - 0.994^2/0.22
               = 0.182127272727...

This value is included only as a comparison target.  Because the earlier
v13.365 full-cross certificate was subsequently placed under audit, this file
DOES NOT promote delta_tail > 0.1821 as certified.  The next rigorous task is
to certify the six-dimensional residual Gram directly against a separately
revalidated tail-coercivity lower bound.

Guardrails
----------
* finite diagnostics are not infinite-operator proofs;
* the first four tiny Schur eigenvalues are not called exact kernels;
* no exact-zero, inertia, RH, or GRH conclusion follows;
* no v13.365/v13.366 claim is silently reinstated.
"""

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

ALPHA_TARGET = 4.6732
FINITE_HIGH_GAP_TARGET = 0.22
CROSS_NORM_TARGET = 0.994
PROVISIONAL_DELTA_COMPARISON = (
    ALPHA_TARGET - CROSS_NORM_TARGET**2 / FINITE_HIGH_GAP_TARGET
)

if __name__ == "__main__":
    print("equal-width diagnostic delta_crit:")
    for M, value in DIAGNOSTIC_DELTA_CRIT.items():
        print(f"  M={M:4d}: {value:.4f}")
    print("residual low-rank ratios sigma2/sigma1:")
    for M, value in SIGMA2_OVER_SIGMA1.items():
        print(f"  M={M:4d}: {value:.4e}")
    print("M=1199 sigma4 ~", SIGMA4_M1199)
    print("M=1199 sigma5 ~", SIGMA5_M1199)
    print("provisional comparison delta =", PROVISIONAL_DELTA_COMPARISON)
    assert 0.1821 < PROVISIONAL_DELTA_COMPARISON < 0.1822
    print("guardrail: comparison target only; audited cross closure not reinstated")
