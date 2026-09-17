# Cone Derivation Ledger v13.571 — M16001 Exact P/N/B Basis Certificate

## Scope

Close the first genuinely numerical/exact upstream gate from v13.568: replace the opaque floating `inv`/SVD basis construction by deterministic exact rational algebra on the frozen binary64 payloads `Q_HEX` and `L0_HEX`.

New checker:

`research-notes/suzuki_M16001_exact_basis_certificate.py`

No floating linear algebra is used by the certificate.

## 1. Exact source interpretation

Every hexadecimal binary64 entry of the frozen 10x6 `Q` and 6x6 lower-triangular `L0` is decoded to its exact dyadic rational value. `L0` is checked lower triangular and all six diagonal entries are checked nonzero.

Canonical rational-matrix payload format is

`M16001-RATIONAL-MATRIX-v1`

with reduced `numerator/denominator` entries in row-major order.

Canonical SHA-256 identities produced by the exact reconstruction are:

- `Q`: `a618214572ad6b7cc7313b481ba4632098baa2a93c558dc8ac88277be3c75b50`
- `L0`: `d0816474d25f90c1e674556cbd23c09030191f14ab688235f4be7ccd5ebd35e7`

These hashes refer to the canonical exact-rational serialization, not to source-file bytes.

## 2. Exact normalized six-plane P

Instead of evaluating

\[
P=Q L_0^{-T}
\]

through a numerical inverse, the checker solves row by row by exact lower-triangular substitution:

\[
L_0 p_r^T=q_r^T.
\]

It then verifies every one of the 60 rational identities

\[
\boxed{P L_0^T-Q=0_{10\times6}}.
\]

Canonical exact `P` payload SHA-256:

`c44eacee75a8c81509190f19f7b874be9a7be0ed6283e4413725498b4c2c2690`

Thus the six-plane coordinate construction is now exact for the frozen Q/L0 payload; no `np.linalg.inv` certificate is required.

## 3. Deterministic exact null complement N

Write `Q^T=[A C]` using coordinate rows 0..5 as pivots and rows 6..9 as free coordinates. The checker computes `det(A)` exactly and verifies it is nonzero. For each free coordinate e_t it solves

\[
A x_t=-C e_t
\]

exactly and forms

\[
N=\begin{bmatrix}-A^{-1}C\\I_4\end{bmatrix}.
\]

The checker independently verifies

\[
\boxed{Q^T N=0_{6\times4}}
\]

and that the free 4x4 block is exactly `I4`. Therefore `rank(N)=4` exactly, without an SVD or numerical singular-value threshold.

Canonical exact `N` payload SHA-256:

`4531629478720802c14e36ae2775644a010b1ee50971d982214f3f5305cbf4d8`

## 4. Exact complete basis B=[P,N]

Set

\[
\mathcal B=[P,N]\in\mathbb Q^{10\times10}.
\]

The checker evaluates its determinant exactly and obtains a nonzero rational. Numerically only for orientation,

\[
\det \mathcal B\approx 1.1094160324919792\times10^{19},
\]

but the proof is the exact nonzero rational test, not this decimal approximation.

Canonical exact `B` payload SHA-256:

`95361d587004e215e2cae74a5e9eb430a16d150626375e45f5d996f601fb6a0a`

Hence

\[
\boxed{\det\mathcal B\ne0},\qquad
\boxed{\mathcal B=[P,N]\text{ is an exact basis of }\mathbb R^{10}}
\]

for the frozen rational payload.

## 5. What is now closed

Closed exactly for the frozen payload:

1. `L0` triangular nonsingularity;
2. `P L0^T = Q`;
3. deterministic four-dimensional `N subset ker(Q^T)`;
4. `rank(N)=4`;
5. `B=[P,N]` nonsingularity;
6. immutable canonical exact payload identities for Q, L0, P, N, B.

This removes the current `np.linalg.inv(L0.T)` and `np.linalg.svd(Q.T)` operations from the proof dependency chain at the subspace-construction level.

## 6. Important basis-coordinate guardrail

The exact `N` is a deterministic rational null basis, not the previous numerical orthonormal SVD basis. Therefore no old N-block, QN-block, remote-Gram, far-tail, or Schur numerical endpoint may be reused unchanged. All downstream quantities must be replayed in this newly frozen exact basis, or the metric/normalization must be explicitly certified before comparison with old coordinates.

Likewise, this entry does not yet certify the floating realization of B, `X B`, or

\[
W=\begin{bmatrix}B\\-XB\end{bmatrix}.
\]

The next upstream arithmetic gate is the exact-rational-to-replay conversion of B followed by an entrywise outward certificate for `XB` and W.

## 7. Status

This is a real exact-algebra closure, not merely a specification checkpoint. It closes the P/N/B construction gate for the frozen source payload.

It does **not** close finite source-function uncertainty, the remote `tail_Z(n)` source/evaluation gate, the far-tail endpoint, the explicit remote Gram, or the final seven-plane Schur inequality.

Certified inertia status therefore remains unchanged:

\[
\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4,\qquad
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]

No index<=3, exact-zero, RH, or GRH claim follows from this entry.
