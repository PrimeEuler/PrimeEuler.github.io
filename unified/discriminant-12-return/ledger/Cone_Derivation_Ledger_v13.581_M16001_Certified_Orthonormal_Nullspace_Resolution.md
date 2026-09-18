# Cone Derivation Ledger v13.581 — M16001 Certified Orthonormal Nullspace Resolution

## Scope

Resolve the coordinate guardrail left by v13.571/v13.580.  The exact rational null basis N0 is retained as the algebraic certificate of ker(Q^T), but it is **not** used directly as the Euclidean four-plane in the downstream Schur calculation.

The chosen resolution is to certify an orthonormal realization of the same exact nullspace.  This is less invasive and less lossy than carrying a generalized Gram metric through every remote/far/Schur formula, and it preserves the mathematical meaning of the original SVD-based downstream calculation.

## 1. Exact algebraic anchor

Let N0 be the 10x4 rational matrix certified in v13.571:

[
Q^T N_0=0,qquad \operatorname{rank}N_0=4.
]

Its canonical exact payload hash is

`4531629478720802c14e36ae2775644a010b1ee50971d982214f3f5305cbf4d8`.

Form the exact rational Gram matrix

[
G_N=N_0^T N_0\in\mathbb Q^{4\times4}.
]

Because N0 has full column rank, G_N is exactly symmetric positive definite.  Certify this by exact LDL^T pivots or exact leading principal minors.

## 2. Orthonormal realization

Let R be the unique upper-triangular Cholesky factor with positive diagonal satisfying

[
G_N=R^T R.
]

Define

[
N_\perp=N_0R^{-1}.
]

Then mathematically

[
Q^TN_\perp=0,qquad
N_\perp^TN_\perp=I_4,qquad
\operatorname{col}(N_\perp)=\operatorname{col}(N_0).
]

R is generally irrational, so the proof artifact is an outward interval enclosure, not an exact-rational matrix.

The production certificate must provide midpoint/radius payloads

[
R\in[\widehat R\pm\rho_R],qquad
R^{-1}\in[\widehat U\pm\rho_U],qquad
N_\perp\in[\widehat N_\perp\pm\rho_N],
]

with directed outward arithmetic.

## 3. Required interval checks

The checker must certify:

1. exact SPD of G_N;
2. every interval diagonal of R has positive lower endpoint;
3. interval containment of R^T R-G_N contains zero entrywise;
4. interval containment of R U-I_4 contains zero entrywise;
5. interval containment of Q^T N_perp contains zero entrywise;
6. interval containment of N_perp^T N_perp-I_4 contains zero entrywise;
7. the enclosure is built from N0 U, so its columns lie in the certified exact nullspace up to the explicitly propagated arithmetic enclosure.

For stronger operator-level guards, report

[
\epsilon_{QN}\ge\|Q^T\widehat N_\perp\|_2+\text{interval charge},
]

and

[
\epsilon_N\ge\|\widehat N_\perp^T\widehat N_\perp-I\|_2+\text{interval charge}.
]

These are diagnostics/guards; the entrywise interval checks remain authoritative.

## 4. Replay basis

The downstream replay basis is now

[
\mathcal B_\perp=[P,N_\perp].
]

Do **not** use the rational B=[P,N0] from v13.571 as the numerical replay basis.  Its role is algebraic provenance only.

Accordingly v13.580's replay-handoff implementation is amended at the N block:

- P remains sourced from the exact v13.571 rational certificate;
- N is sourced from this certified orthonormal-nullspace interval;
- B_perp receives midpoint/radius data from both blocks;
- XB_perp and W_perp are recomputed from that interval basis.

## 5. Important P normalization check

The original source calls P=Q L0^{-T} the normalized six-plane.  Exact v13.571 proves P L0^T=Q, but that identity alone does not prove P^T P=I exactly for the frozen binary64 L0.

Before using ordinary Euclidean eigenvalue/norm bounds in the final Schur step, the production checker must therefore compute the exact rational

[
G_P=P^T P
]

and test whether G_P=I_6 exactly.

If it is not exactly I_6, do not silently treat P as orthonormal.  Either certify an orthonormal six-plane realization by the same small-Gram Cholesky construction, or carry the 6x6 metric G_P in the finite Q-block.  This is a separate normalization gate and must close before theorem promotion.

## 6. Downstream quantities that must be recomputed

Because the old SVD N and the new certified N_perp are different orthonormal bases of the same four-plane, scalar invariants of the **complete exact operator** are unchanged, but all stored coordinate payloads and arithmetic transcripts involving N must be regenerated.

Mandatory recomputation:

- B_perp=[P,N_perp] midpoint/radius payload;
- X B_perp and W_perp=[B_perp;-X B_perp];
- finite projected matrix B_perp^T S B_perp, including QQ/QN/NN arithmetic radii;
- explicit remote moments p, a_q, b_q;
- all 991,999 explicit remote row midpoint/radius vectors;
- remote residual Gram midpoint and pre-Gram operand enclosure;
- remote Gram reduction/chunk-addition transcript;
- far moments S_Z, S_J, S_J2Z and their radii;
- far L, B, C vectors;
- f_Q, f_N and f_X far-block upper bounds;
- lambda_Q lower endpoint if P itself is changed/renormalized; otherwise its arithmetic enclosure still must be regenerated consistently from the new complete replay;
- Q/N cross spectral-norm upper endpoint;
- N-block largest-eigenvalue endpoint used for the unresolved direction;
- final Schur penalty and final seven-plane lower endpoint.

No old N-coordinate midpoint or radius is transferable merely because both N choices span ker(Q^T).

## 7. Quantities that need not be recomputed from source

The following upstream objects are basis-independent and remain reusable with their existing certificates, subject to hash matching:

- finite source arrays Z, c and diag0;
- frozen structured-solve X and its structured residual/backward-error certificate;
- exact Q and L0 payloads;
- remote coercivity floor construction;
- exact remote/far index ranges;
- analytic/source-function uncertainty certificates that are stated in ambient coordinates rather than old N coordinates.

Their **projection into B_perp coordinates** must nevertheless be recomputed.

## 8. Why orthonormalization is chosen over carrying G_N

A rational-coordinate treatment would replace ordinary N-block eigenvalues by generalized eigenvalues relative to G_N, replace Euclidean coefficient norms by G_N-weighted norms, and insert metric factors into QN operator norms, remote/far block estimates, and the Schur complement.  It is mathematically valid but touches nearly every downstream inequality.

The certified Cholesky map is only 4x4.  Once its outward enclosure is closed, the existing Euclidean block architecture can be replayed essentially unchanged while preserving exact provenance back to N0.  Therefore the orthonormal route is the canonical M16001 path.

## 9. Production artifact

Implement

`research-notes/suzuki_M16001_orthonormal_nullspace_certificate.py`

with canonical exact G_N payload plus hashed dyadic midpoint/radius payloads for R, R^{-1}, and N_perp.  Terminal status:

`ORTHONORMAL NULLSPACE CERTIFICATE: PASS`

only after every exact and interval check above succeeds.

## Status

The non-orthonormal rational-N ambiguity is resolved at the architecture level: N0 is the exact algebraic anchor and N_perp=N0 R^{-1} is the required certified Euclidean replay basis.  Numerical interval payload generation remains the next arithmetic task.  The additional P^T P normalization check is explicitly open.

Certified inertia status is unchanged.  No index<=3, exact-zero, RH, or GRH claim follows from this entry.
