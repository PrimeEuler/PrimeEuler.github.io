#!/usr/bin/env python3
"""A-posteriori binary64 certificate for the odd M=4000 cross low-rank cap.

This companion to `suzuki_odd_M4000_cross_outward_verifier.py` removes any
need to trust the SVD/eigensolver as an oracle.

1. Rebuild the explicit near cross matrix A_near.
2. Compute any numerical rank-12 SVD candidate U,S,V.
3. Verify its direct Frobenius residual A_near-U S V^T.
4. Build the 8-level remote inverse-power factor and verify its feature-Gram
   factorization a posteriori.
5. Concatenate the near and remote factors into W and certify

       ||W||_2 < 0.977255

   by Cholesky factorization of the 29x29 shifted Gram

       M = 0.977255^2 I - W^T W.

The Cholesky is itself checked by a verified-inverse style residual bound.
A deliberately loose 1e-8 allowance covers formation of the 29x29 Gram and
its binary64 arithmetic; the certified factor floor is about 5.98e-6.

This certifies only the point nominal low-rank factor.  Source perturbations,
near residual, remote geometric remainder, and the far tail are charged by the
main outward verifier.
"""
from __future__ import annotations

import numpy as np
from scipy.sparse.linalg import svds

from suzuki_odd_M4000_cross_midpoint_replay import (
    F, TNEAR, TREM,
    Z_even, near_matrix, remote_low_rank,
)

CAP = 0.977255
NEAR_RESIDUAL_CAP = 0.002308
GRAM_FORMATION_ALLOWANCE = 1.0e-8
REMOTE_GRAM_FACTOR_ALLOWANCE = 1.0e-12


def report():
    ZF = Z_even(F)
    ZT = Z_even(TNEAR)
    A = near_matrix(ZF, ZT)

    U, s, Vt = svds(A, k=12, which='LM', return_singular_vectors=True,
                    tol=1e-11, maxiter=1000)
    order = np.argsort(s)[::-1]
    U = U[:, order]
    s = s[order]
    Vt = Vt[order, :]

    R = A-(U*s)@Vt
    rnorm = float(np.linalg.norm(R, 'fro'))
    uorth = float(np.linalg.norm(U.T@U-np.eye(12), 'fro'))
    vorth = float(np.linalg.norm(Vt@Vt.T-np.eye(12), 'fro'))
    print('direct near rank-12 residual Fro =', repr(rnorm))
    print('U orthogonality defect Fro =', repr(uorth))
    print('V orthogonality defect Fro =', repr(vorth))
    assert rnorm < NEAR_RESIDUAL_CAP
    assert uorth < 1e-12
    assert vorth < 1e-12

    # Remote 8-level feature Gram.  Numerical eigendecomposition is used only
    # to obtain a candidate square-root factor; its reconstruction is checked.
    ZR = Z_even(TREM)
    Urem, Gfeat = remote_low_rank(ZF, ZR, 8)
    evals, Q = np.linalg.eigh(Gfeat)
    evals_pos = np.maximum(evals, 0.0)
    Wrem = Urem@Q@np.diag(np.sqrt(evals_pos))
    Grem = Urem@Gfeat@Urem.T
    remote_factor_resid = float(np.linalg.norm(Grem-Wrem@Wrem.T, 'fro'))
    print('remote Gram factor residual Fro =', repr(remote_factor_resid))
    assert remote_factor_resid < REMOTE_GRAM_FACTOR_ALLOWANCE

    Wnear = U*s
    W = np.column_stack((Wnear, Wrem))
    point_norm = float(np.linalg.svd(W, compute_uv=False)[0])
    print('combined low-rank point norm =', repr(point_norm))
    assert point_norm < 0.9772520

    K = W.T@W
    M = CAP*CAP*np.eye(K.shape[0])-K
    L = np.linalg.cholesky(M)
    X = np.linalg.solve(L, np.eye(len(L)))

    # A-posteriori factor checks, exactly parallel to the v13.424/v13.434
    # verified-inverse route, but only dimension 29 here.
    n = len(L)
    unit = 2.0**-53
    gamma = n*unit/(1.0-n*unit)
    recon_point = float(np.linalg.norm(M-L@L.T, 'fro'))
    recon_scale = float(np.linalg.norm(np.abs(L)@np.abs(L).T, 'fro'))
    recon_out = recon_point+gamma*recon_scale
    lx_point = float(np.linalg.norm(np.eye(n)-L@X, 'fro'))
    lx_scale = float(np.linalg.norm(np.abs(L)@np.abs(X), 'fro'))
    lx_out = lx_point+gamma*lx_scale
    xnorm = float(np.linalg.norm(X, 'fro'))

    print('shifted-Gram Cholesky point residual =', repr(recon_point))
    print('shifted-Gram reconstruction outward <', repr(recon_out))
    print('||X||_F =', repr(xnorm))
    print('verified ||I-LX||_2 upper <', repr(lx_out))

    assert recon_out < 1e-10
    assert xnorm < 409.0
    assert lx_out < 1e-10

    factor_floor = (1.0-1e-10)**2/(409.0**2)
    final_floor = (factor_floor-recon_out-GRAM_FORMATION_ALLOWANCE
                   -REMOTE_GRAM_FACTOR_ALLOWANCE)
    print('shifted-Gram factor floor >', repr(factor_floor))
    print('after formation/factor allowances >', repr(final_floor))
    assert final_floor > 5.9e-6

    print('PASS: nominal combined low-rank cross factor has ||W||_2 < 0.977255')
    print('PASS: direct near residual is < 0.002308')
    print('GUARDRAIL: source perturbation and non-low-rank tails are separate obligations')


if __name__ == '__main__':
    report()
