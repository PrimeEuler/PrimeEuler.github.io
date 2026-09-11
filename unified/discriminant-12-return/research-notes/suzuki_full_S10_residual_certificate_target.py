#!/usr/bin/env python3
"""Source-faithful Suzuki S10 certification targets after Audit Round 24.

Status
------
v13.387 resolved External Audit Round 20's overlap mistake, and External Audit
Round 24 (ledger v13.390) independently confirmed that resolution from Suzuki's
pre-transformation source quadratic form. The valid archimedean off-diagonal
formula is the original source-faithful rank-two expression

    K_arch(m,n)=-(4/pi)(n H_m-m H_n)/(n^2-m^2).

Therefore the rank-four v13.373-v13.386 detour is superseded. The valid
source-faithful high-complement inputs are again

    A0_[21,16001] >= 0.22 I,
    A0_[16003,infinity) >= 4.6732 I,
    ||A0_[21,16001],[16003,infinity)|| < 0.994,

under the validated-computational/analytic-tail model of v13.362-v13.365.

For the whole high complement D={21,23,...}, the crude block-Schur margin is

    gamma_D = 0.22 - 0.994^2/4.6732 > 8e-3,

hence ||A_DD^{-1}|| < 1/gamma_D. This remains a valid generic residual bound.

Preferred terminal reduction (v13.391)
--------------------------------------
Split D=F+T with F={21,...,16001}, T={16003,...}. After eliminating F,

    S_infty = S_F - R^* T_eff^{-1} R,

where

    S_F = A_CC - A_CF A_FF^{-1} A_FC,
    R   = A_TC - A_TF A_FF^{-1} A_FC,
    T_eff = A_TT - A_TF A_FF^{-1} A_FT.

For the pole-free source-faithful operator,

    T_eff >= delta I,
    delta = 4.6732 - 0.994^2/0.22 > 0.182.

Adding the even-sector PSD pole cannot lower this effective-tail Schur
complement. Therefore the same delta lower bound applies to the full A.

If Q spans six candidate-positive low-core directions, it suffices to certify

    Q^T S_F Q - delta^{-1} (R Q)^*(R Q) > 0.

This quadratic/an\-isotropic six-plane condition supersedes the earlier
preferred strategy of demanding a uniform ~1e-11 residual on all ten infinite
high solves. The generic residual estimate below is retained as a fallback and
cross-check only.

Guardrails
----------
The source-faithful finite S10 fifth eigenvalue (~4e-8 at tested cutoffs) is
numerical only. The first four near-zero directions are not established exact
kernels. No exact-zero, RH, GRH, or final inertia conclusion follows here.
"""

FINITE_LOWER = 0.22
TAIL_LOWER = 4.6732
CROSS_UPPER = 0.994

GAMMA_D = FINITE_LOWER - CROSS_UPPER**2 / TAIL_LOWER
INVERSE_BOUND = 1.0 / GAMMA_D
EFFECTIVE_TAIL_DELTA = TAIL_LOWER - CROSS_UPPER**2 / FINITE_LOWER
TARGET_SCHUR_ERROR = 3e-9


def uniform_residual_target(Cnorm=1.0, eta=TARGET_SCHUR_ERROR):
    """Fallback linear residual target for a full ten-column solve."""
    return eta * GAMMA_D / Cnorm


if __name__ == '__main__':
    print('source-faithful whole-D gamma_D >', GAMMA_D)
    print('||A_DD^{-1}|| <', INVERSE_BOUND)
    print('effective-tail delta >=', EFFECTIVE_TAIL_DELTA)
    print('fallback residual target for Cnorm=1:', uniform_residual_target())
    assert EFFECTIVE_TAIL_DELTA > 0.182
    print('preferred target: certify Q^T S_F Q - delta^{-1}(RQ)^*(RQ) > 0')
    print('guardrail: no exact-zero, RH, or GRH conclusion follows')
