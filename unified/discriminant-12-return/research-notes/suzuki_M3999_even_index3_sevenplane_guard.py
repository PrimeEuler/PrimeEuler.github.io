#!/usr/bin/env python3
"""Fail-closed seven-plane guard for the M3999 even-sector index<=3 attempt.

The earlier directional budget for one unresolved vector v_* is necessary but
not sufficient for an index<=3 theorem: positivity on the certified six-plane Q
and positivity on v_* separately do not imply positivity on span(Q,v_*).
The cross block must also be controlled.

This diagnostic reuses the source-faithful M3999 replay and the certified
coercivity floor delta_T.  It forms the conservative lower bound

    S_infty >= S_F - delta_T^{-1} R^* R

on the ten-dimensional low core, normalizes the certified six-plane by L0,
and then Schur-eliminates that six-plane.  The resulting 4x4 matrix is the
coercivity-floor lower bound on the unresolved complement after accounting for
all six-plane cross terms.

Status: midpoint diagnostic plus certified delta_T.  This file intentionally
fails closed against the incomplete scalar-only promotion.  No stronger inertia,
exact-zero, RH, or GRH claim follows.
"""
from __future__ import annotations
import numpy as np

from suzuki_M3999_unresolved_fourplane_residual_gram_replay import (
    finite_solve, residual_gram, Q_HEX, L0_HEX, DELTA_T,
)


def fmat(H):
    return np.array([[float.fromhex(x) for x in row] for row in H], dtype=float)


def report():
    modes, Z, c, X, S, piv = finite_solve()
    Q = fmat(Q_HEX)
    L0 = fmat(L0_HEX)

    # Numerical orthonormal complement of the frozen exact-dyadic six-plane.
    _, _, vh = np.linalg.svd(Q.T, full_matrices=True)
    N = vh[6:].T

    # Regenerate the whole residual Gram on Q plus its four-dimensional complement.
    B10 = np.column_stack([Q, N])
    G10, _, _ = residual_gram(B10, modes, Z, c, X)
    GQQ, GQN, GNN = G10[:6, :6], G10[:6, 6:], G10[6:, 6:]

    # Certified-six-plane conservative lower block under only the coercivity floor.
    AQQ = Q.T @ S @ Q
    MQQ = np.linalg.solve(L0, AQQ - GQQ / DELTA_T) @ np.linalg.inv(L0.T)
    MQQ = (MQQ + MQQ.T) / 2

    # Cross and unresolved blocks in the same lower-bound matrix.
    BQN = np.linalg.solve(L0, Q.T @ S @ N - GQN / DELTA_T)
    FNN = N.T @ S @ N - GNN / DELTA_T
    FNN = (FNN + FNN.T) / 2

    # Proper Schur complement after eliminating the six-plane.
    K = FNN - BQN.T @ np.linalg.solve(MQQ, BQN)
    K = (K + K.T) / 2

    # Reproduce the scalar-only largest finite unresolved direction v_*.
    NF = (N.T @ S @ N + (N.T @ S @ N).T) / 2
    ev, U = np.linalg.eigh(NF)
    ustar = U[:, -1]
    scalar_before_cross = float(ustar @ FNN @ ustar)
    scalar_after_cross = float(ustar @ K @ ustar)

    print('certified-six-plane lower-block eigenvalues (midpoint G payload) =',
          np.linalg.eigvalsh(MQQ))
    print('unresolved lower block before six-plane cross =', np.linalg.eigvalsh(FNN))
    print('six-plane/unresolved normalized cross norm =', np.linalg.norm(BQN, 2))
    print('proper unresolved Schur-complement eigenvalues =', np.linalg.eigvalsh(K))
    print('v_* scalar before six-plane cross =', scalar_before_cross)
    print('v_* scalar after six-plane cross =', scalar_after_cross)

    # Regression guards matching the M3999 replay.
    ek = np.linalg.eigvalsh(K)
    assert scalar_before_cross > 6.0e-13
    assert scalar_after_cross < -2.0e-11
    assert ek[0] < -2.0e-11
    assert ek[-1] > 5.0e-15
    assert np.linalg.norm(BQN, 2) < 9.0e-7

    print('FAIL-CLOSED RESULT: scalar positivity of v_* is insufficient for index<=3')
    print('OPEN: a 7D theorem needs the Q-v cross block, not only the v_* Rayleigh scalar')
    print('GUARDRAIL: present theorem remains ind_{<=0}(A_even(1)) <= 4')


if __name__ == '__main__':
    report()
