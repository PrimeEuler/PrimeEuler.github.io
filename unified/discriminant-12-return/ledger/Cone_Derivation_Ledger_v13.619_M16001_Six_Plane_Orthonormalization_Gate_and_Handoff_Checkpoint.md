# Cone Derivation Ledger v13.619 — M16001 Six-Plane Orthonormalization Gate and Handoff Checkpoint

## Purpose

This is the handoff checkpoint for a fresh chat.  It closes the architectural six-plane normalization gate following v13.605 and records exactly what is implemented, what must be executed/frozen, and what the next M16001 production step is.

## Live implementation

New checker:

`research-notes/suzuki_M16001_orthonormal_sixplane_certificate.py`

implementation commit:

`c1fd13289374c9fe0b13b9d29bb94a4af437faa6`

CI hook commit:

`151b1e0f98e240b3afd23f9c2ae7bb7b8be2e64a`

The existing M16001 pull-request audit workflow now invokes the six-plane checker and captures its transcript as `/tmp/m16001-sixplane.txt`.

## Upstream facts to preserve

v13.571 exact rational basis certificate:
- P is the exact Fraction solution of P L0^T=Q.
- N0 is the deterministic exact rational null basis with Q^T N0=0 and rank 4.
- [P,N0] is nonsingular.

v13.605:
- the corrected 4x4 outward construction closes the N0 metric issue by N_perp=N0 R_N^{-1};
- Q^T N_perp contains zero and N_perp^T N_perp contains I4;
- frozen N_perp payload SHA-256:
  `0d4276f94eb5a876dc014e1accdcf812603f3d74929744c68d84aab058e94667`;
- exact test proves P^T P != I6, so raw P cannot be used as an Euclidean-orthonormal six-plane.

## Six-plane construction

The new checker reconstructs exact P and forms

[
G_P=P^TP\in\mathbb Q^{6\times6}.
]

It computes exact Fraction LDL^T pivots and requires all six to be strictly positive.  Hence G_P is certified SPD without floating eigenvalue calculations.

It then uses the corrected 120-digit outward Decimal interval machinery from the N certificate to construct

[
G_P\in R_P^T R_P,qquad
I_6\in R_P R_P^{-1},
]

and

[
P_\perp=P R_P^{-1}.
]

Required interval gates are

[
0\in R_P^T R_P-G_P,
]

[
0\in R_P R_P^{-1}-I_6,
]

[
0\in P_\perp^T P_\perp-I_6.
]

The checker independently reconstructs the corrected N_perp interval and also requires

[
0\in P_\perp^T N_\perp.
]

Finally it forms

[
\mathcal B_\perp=[P_\perp,N_\perp]
]

and requires

[
0\in\mathcal B_\perp^T\mathcal B_\perp-I_{10}.
]

Thus successful execution closes the entire 10-dimensional basis-metric problem, not merely the internal six-plane normalization.

## Payloads generated on successful execution

The checker writes and hashes:

- `M16001_P_Gram_exact_interval.interval`, 6x6;
- `M16001_P_Cholesky_R.interval`, 6x6;
- `M16001_P_Cholesky_Rinv.interval`, 6x6;
- `M16001_P_perp.interval`, 10x6;
- `M16001_B_perp.interval`, 10x10;
- `M16001_orthonormal_sixplane_certificate.json`.

The terminal success line is

`ORTHONORMAL SIX-PLANE CERTIFICATE: PASS`.

## Important execution-status distinction

At the moment of this ledger write the checker and CI execution hook are committed, but this chat has not received an independent CI transcript containing the numerical hashes and interval widths.  Therefore do NOT invent or freeze those numerical values here.

The next chat should first inspect commits/workflow results after `151b1e0f98e240b3afd23f9c2ae7bb7b8be2e64a`.  If the six-plane transcript exists and passes, freeze its exact G_P hash, six LDL pivots, five interval payload hashes, JSON hash, and maximum interval widths in the next ledger entry.  If it fails, repair the checker before any PASS promotion.

## Next M16001 step after PASS

Once B_perp is frozen, implement the v13.580 replay handoff using B_perp rather than raw [P,N0]:

[
\mathcal B_\perp
\longrightarrow
X\mathcal B_\perp
\longrightarrow
W_\perp=
\begin{bmatrix}
\mathcal B_\perp\\-X\mathcal B_\perp
\end{bmatrix}.
]

Generate midpoint/radius payloads for B_perp, XB_perp and W_perp, with exact nominal dyadic dot-product discrepancies and entrywise outward radii.

Then v13.568 consumes W_perp to certify p,a_q,b_q, followed by the 991,999 explicit remote rows, E_preGram, remote Gram, far moments/bounds and finally the seven-plane Schur endpoint.

## Downstream quantities that must be recomputed in the orthonormal basis

Do not reuse old SVD-N/raw-P coordinate numbers. Recompute:
- B_perp, X B_perp, W_perp;
- finite QQ/QN/NN projections and radii;
- p, a_q, b_q;
- all 991,999 explicit remote row midpoint/radius vectors;
- remote pre-Gram and Gram/reduction transcript;
- far S_Z, S_J, S_J2Z, L, B, C;
- f_Q, f_N, f_X;
- lambda_Q endpoint, QN spectral norm, N-block endpoint;
- final Schur penalty and seven-plane lower endpoint.

Ambient source payloads Z,c,diag0, frozen X and its structured residual certificate, Q,L0, index ranges, and ambient source-function uncertainty certificates remain reusable subject to hash matching.

## Theorem status

No theorem promotion at this checkpoint.  Existing certified inertia status remains unchanged.  In particular no index<=3, exact-zero, RH, or GRH claim follows until the complete outward replay and final Schur gate close.
