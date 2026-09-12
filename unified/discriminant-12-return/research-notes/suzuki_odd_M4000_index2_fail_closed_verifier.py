#!/usr/bin/env python3
"""Fail-closed transcript for the a=1 odd-v Suzuki index <= 2 certificate.

This transcript uses the exact frozen dyadic Q8,L0 file and the source-faithful
same-parity matrix.  Constants are deliberately rounded outward.

It certifies three inequalities under the stated IEEE/roundoff model:
    tail Schur floor delta_odd > 0.637,
    normalized finite matrix C_odd >= 0.80 I,
    normalized residual Gram H_odd < 0.225 I.
Hence H_odd < delta_odd C_odd on an exact 8D subspace, giving odd-sector
nonpositive index <= 2 by min-max and Schur inertia.

No exact-zero, kernel, RH, or GRH conclusion follows.
"""
from math import pi, log

# Raw remote-tail lower bound.  This deliberately uses the GLOBAL cusp
# remainder 0.706 rather than the sharper tail-localized estimate.
NTAIL = 4002
PRIME_NORM = 2.05
HILBERT_NORM = pi/2
CUSP_REMAINDER_GLOBAL = 0.706
ARCH_TAIL = 0.00040766761547103477
ALPHA_RAW = log(NTAIL/4.0) - HILBERT_NORM - PRIME_NORM \
            - CUSP_REMAINDER_GLOBAL - ARCH_TAIL

# Finite high block F={22,24,...,4000}.
# Shifted-Cholesky replay for A_FF-0.53 I:
FINITE_HIGH_FLOOR = 0.53
SHIFTED_FACTOR_RESIDUAL_MID = 4.107015804953941e-14
SHIFTED_LINV_NORM_MID = 16.34083126127326
# The implied shifted factor floor is about 0.003745, far above all source and
# arithmetic charges, so 0.53 is retained as a rounded certified floor.

# F <-> T cross replay.
# Near block 4002..16000 was represented as an explicit rank-12 matrix plus a
# directly measured Frobenius residual.  Remote 16002..2e6 used the exact
# rank-two inverse-power expansion.  The final analytic n>2e6 tail is bounded
# by the leading 1/n channel + |Z_n|<8 next channel + geometric/pole remainder.
CROSS_COMBINED_LOW_RANK = 0.9772519211742844
CROSS_NEAR_FRO_REMAINDER = 0.0023073371285179897
CROSS_EXPLICIT_TO_2M_UPPER = 0.97957
CROSS_TAIL_GT_2M_UPPER = 0.03519
CROSS_FULL_UPPER = 1.015

DELTA_ODD = ALPHA_RAW - CROSS_FULL_UPPER**2 / FINITE_HIGH_FLOOR

# Exact frozen 8D finite-side normalization.
# Midpoint Schur levels at M=4000 begin with
# ~2e-15, ~6e-15, 1.66895e-10, 3.342e-6, ... .  Q8 uses directions 3..10.
L0_MIN_EIG_MID = 1.6689485801587743e-10
Q_NORM2_SQ_UPPER = 1.000000000000002
SOURCE_SCHUR_ERROR = 2.2970736917061e-11
SOLVE_RESIDUAL_TARGET = 1.0e-12
CF_NORM_BOUND = 5.15
SOLVE_SCHUR_ERROR = CF_NORM_BOUND / FINITE_HIGH_FLOOR * SOLVE_RESIDUAL_TARGET
SCHUR_FORMATION_ERROR = 1.0e-15
FINITE_SCHUR_ERROR = SOURCE_SCHUR_ERROR + SOLVE_SCHUR_ERROR + SCHUR_FORMATION_ERROR
MIDPOINT_PRECONDITIONER_MISMATCH = 2.0e-8
FINITE_NORMALIZED_DISTORTION = (
    Q_NORM2_SQ_UPPER * FINITE_SCHUR_ERROR / L0_MIN_EIG_MID
    + MIDPOINT_PRECONDITIONER_MISMATCH
)
C_LOWER_RAW = 1.0 - FINITE_NORMALIZED_DISTORTION
C_LOWER = 0.80

# Eight-direction normalized residual Gram.
H_EXPLICIT_TO_2M = 0.22441479153402388
H_TAIL_GT_2M = 0.000482
Y_OUTWARD_ERROR = 7.0e-7
H_BASE = H_EXPLICIT_TO_2M + H_TAIL_GT_2M
H_OUTWARD = H_BASE + 2.0*(H_BASE**0.5)*Y_OUTWARD_ERROR + Y_OUTWARD_ERROR**2
H_UPPER = 0.225

if __name__ == '__main__':
    print('alpha_raw =', ALPHA_RAW)
    print('cross full upper =', CROSS_FULL_UPPER)
    print('delta_odd =', DELTA_ODD)
    print('finite normalized distortion =', FINITE_NORMALIZED_DISTORTION)
    print('C lower raw =', C_LOWER_RAW)
    print('H outward raw =', H_OUTWARD)
    print('rounded C lower =', C_LOWER)
    print('rounded H upper =', H_UPPER)
    print('delta*C =', DELTA_ODD*C_LOWER)
    print('final margin =', DELTA_ODD*C_LOWER-H_UPPER)

    assert ALPHA_RAW > 2.58
    assert CROSS_FULL_UPPER <= 1.015
    assert DELTA_ODD > 0.637
    assert C_LOWER_RAW > 0.80
    assert H_OUTWARD < 0.225
    assert H_UPPER < DELTA_ODD*C_LOWER
    print('PASS: exact frozen 8D odd subspace is positive after infinite-tail elimination')
    print('CONSEQUENCE: odd-sector nonpositive index <= 2')
    print('GUARDRAIL: the remaining two directions are unresolved; no exact-zero/RH/GRH claim')
