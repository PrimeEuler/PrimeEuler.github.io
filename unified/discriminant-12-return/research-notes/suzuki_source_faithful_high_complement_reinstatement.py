#!/usr/bin/env python3
"""Post-audit source-faithful high-complement reinstatement.

After v13.387 resolved the overlap mistake in External Audit Round 20, the
rank-two Z_n matrix used in the original finite-high and cross certificates is
again the source-faithful Suzuki operator.

Inputs, each separately established under its stated validated-computational
or analytic model:

    A_F >= 0.22 I,          F = odd modes 21..16001,
    A_T >= 4.673332491014484 I,  T = odd modes >=16003,
    ||G_FT|| < 0.994.

The Schur complement of F in F direct-sum T therefore obeys

    A_T - G^* A_F^{-1} G
      >= (alpha_T - ||G||^2 / 0.22) I.

No exact-zero, RH, GRH, or global low-mode inertia claim follows from this file.
"""

ALPHA_F = 0.22
ALPHA_T = 4.673332491014484
CROSS = 0.994

DELTA_T = ALPHA_T - CROSS*CROSS/ALPHA_F

if __name__ == '__main__':
    print('alpha_F >=', ALPHA_F)
    print('alpha_T >=', ALPHA_T)
    print('cross <', CROSS)
    print('remote Schur floor >', DELTA_T)
    assert DELTA_T > 0.1822
    print('PASS: source-faithful high complement is positive under stated certificate models')
    print('guardrail: no exact-zero, RH, GRH, or final low-mode inertia conclusion')
