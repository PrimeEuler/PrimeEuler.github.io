# Cone Derivation Ledger v13.580 — M16001 Replay Handoff Contract

## Scope

Continue the M16001 outward-certification chain after the exact P/N/B closure of v13.571 and its independent bit-for-bit audit in External Audit Round 52.

This entry freezes the machine-checkable interface that converts the exact rational basis

[
\mathcal B=[P,N]\in\mathbb Q^{10\times10}
]

into certified replay intervals for

[
Y=X\mathcal B\in\mathbb R^{7991\times10},\qquad
W=\begin{bmatrix}\mathcal B\\-Y\end{bmatrix}\in\mathbb R^{8001\times10}.
]

This is a specification checkpoint. It does not claim that the replay payloads or their numerical radii have already been generated.

## 1. Audited upstream identities

External Audit Round 52 independently re-executed `suzuki_M16001_exact_basis_certificate.py` and reproduced all five canonical hashes and all exact assertions. The replay handoff therefore takes the following exact-rational identities as frozen inputs:

- Q: `a618214572ad6b7cc7313b481ba4632098baa2a93c558dc8ac88277be3c75b50`
- L0: `d0816474d25f90c1e674556cbd23c09030191f14ab688235f4be7ccd5ebd35e7`
- P: `c44eacee75a8c81509190f19f7b874be9a7be0ed6283e4413725498b4c2c2690`
- N: `4531629478720802c14e36ae2775644a010b1ee50971d982214f3f5305cbf4d8`
- B: `95361d587004e215e2cae74a5e9eb430a16d150626375e45f5d996f601fb6a0a`

The exact relations are

[
PL_0^T=Q,qquad Q^TN=0,qquad \operatorname{rank}N=4,qquad \det\mathcal B\ne0.
]

The frozen X payload remains the v13.533 object; binary64-to-longdouble conversion of that frozen payload was already certified with zero conversion radius. Its structured-solve residual is a separate backward-error object and must not be silently reinterpreted as entrywise X conversion uncertainty.

## 2. Canonical replay scalar

For proof artifacts, do not hash decimal strings or platform-dependent `str(np.longdouble)` output. Decode each finite replay value to its exact dyadic rational and serialize it canonically as

[
(-1)^s m2^e,
]

with integer m>=0 and integer e, using one canonical zero representation.

Recommended payload header:

`M16001-DYADIC-FLOAT-v1`

Required fields are name, rows, cols, scalar source, row-major entries, Unix newlines, and exactly one terminal newline. NaN and infinity are forbidden. Radius payloads additionally require every entry to be nonnegative.

## 3. Exact B -> replay B conversion

For each exact rational basis entry b_ki, let bhat_ki be the chosen replay midpoint, decoded back to its exact dyadic value. Compute

[
e^B_{ki}=|b_{ki}-\widehat b_{ki}|
]

in exact rational arithmetic. The stored dyadic radius rho^B_ki must satisfy

[
\boxed{\rho^B_{ki}\ge e^B_{ki}}
]

for all 100 entries. If the rational entry is exactly representable, its conversion radius is zero.

The checker must recompute the exact B hash before accepting any replay payload.

## 4. Certified XB product

Set

[
Y=X\mathcal B.
]

For each of the 79,910 entries define the exact nominal dyadic dot product

[
D_{ri}=\sum_{k=1}^{10}\widehat X_{rk}\widehat B_{ki}.
]

Decode the actual replay midpoint yhat_ri to its exact dyadic value and compute

[
E^{eval}_{ri}=|D_{ri}-\widehat Y_{ri}|
]

exactly.

For the present handoff, the frozen-X conversion radius is zero. Therefore the basis-conversion operand term is

[
E^B_{ri}=\sum_{k=1}^{10}|\widehat X_{rk}|\rho^B_{ki}.
]

The authoritative stored radius must obey

[
\boxed{\rho^Y_{ri}\ge E^B_{ri}+E^{eval}_{ri}}.
]

A generic implementation may retain the full two-operand formula

[
\sum_k\left(
|\widehat X_{rk}|\rho^B_{ki}
+|\widehat B_{ki}|\rho^X_{rk}
+\rho^X_{rk}\rho^B_{ki}
\right),
]

but must report that the present X conversion contribution is exactly zero.

As an independent diagnostic only, retain the conventional dot-product check

[
E^{eval}_{ri}\le
\gamma_{10}\sum_k|\widehat X_{rk}\widehat B_{ki}|,
\qquad
\gamma_{10}=\frac{10u}{1-10u}.
]

The direct exact-dyadic discrepancy, not gamma_10, is the primary evaluation certificate.

## 5. W assembly

Construct, by copying and exact sign change,

[
\widehat W=
\begin{bmatrix}
\widehat B\\-\widehat Y
\end{bmatrix},
\qquad
\rho_W=
\begin{bmatrix}
\rho_B\\\rho_Y
\end{bmatrix}.
]

Dimensions are exactly 8001x10. Rows 0..9 are B; rows 10..8000 are -Y. IEEE finite-value negation introduces no new rounding radius.

The checker must verify payload equality for the top block and exact sign reversal for the lower midpoint block.

## 6. Required payloads and hashes

Materialize and hash at least:

- `M16001_B_replay_midpoint.dyadic`, shape 10x10;
- `M16001_B_replay_radius.dyadic`, shape 10x10;
- `M16001_XB_midpoint.dyadic`, shape 7991x10;
- `M16001_XB_radius.dyadic`, shape 7991x10;
- `M16001_W_midpoint.dyadic`, shape 8001x10;
- `M16001_W_radius.dyadic`, shape 8001x10.

A manifest must bind all six hashes to the exact-B hash and frozen-X payload identity. The manifest must not contain a self-hash.

## 7. Global guard fields

Accumulate the squared entrywise radii exactly:

[
S_B=\sum_{ki}(\rho^B_{ki})^2,qquad
S_Y=\sum_{ri}(\rho^Y_{ri})^2,qquad
S_W=S_B+S_Y.
]

Store each exact squared sum as a reduced rational or canonical dyadic, then separately store outward upper endpoints for

[
\|\Delta B\|_F\le\sqrt{S_B},quad
\|\Delta Y\|_F\le\sqrt{S_Y},quad
\|\Delta W\|_F\le\sqrt{S_W}.
]

These norm guards are summaries only; downstream moment propagation must retain the entrywise rho_W payload.

## 8. Machine-checkable transcript

The production checker must report at least:

- exact B hash MATCH;
- frozen X hash MATCH;
- runtime replay format MATCH;
- B exact-rational containment 100/100 PASS;
- X conversion radius = 0;
- XB exact nominal reductions 79910/79910 PASS;
- XB interval containment 79910/79910 PASS;
- gamma_10 diagnostic PASS;
- W top block equality PASS;
- W lower sign/copy equality PASS;
- all values finite PASS;
- all radii nonnegative PASS;
- all six output hashes MATCH;
- exact S_B, S_Y, S_W;
- outward Frobenius upper endpoints;
- maximum B and XB radii with their row/column indices.

The terminal line is `ARITHMETIC HANDOFF CERTIFICATE: PASS` only if every required recomputation succeeds.

## 9. Basis-coordinate guardrail

v13.571's N is a deterministic rational null basis, not the old orthonormal SVD N. Therefore this handoff deliberately freezes a new coordinate realization. Old N-block, QN-block, remote-Gram, far-tail, and Schur numerical endpoints remain non-transferable.

In particular, nonsingularity of B does not by itself justify reusing Euclidean-coordinate eigenvalue or spectral-norm statements derived in the old orthonormal coordinates. Any final Schur argument must either:

1. construct and certify an orthonormal realization of the same exact null subspace; or
2. formulate the downstream positivity test with the appropriate Gram/metric factors for the rational N coordinates.

That metric issue is now an explicit downstream gate rather than an implicit assumption.

## 10. Next production step

Implement the replay-handoff checker and generate the six hashed midpoint/radius payloads. Once (What,rho_W) is numerically frozen, v13.568's finite-moment interface can consume that exact payload to certify p, a_q, b_q, followed by the 991,999 explicit remote-row radii and E_preGram.

## Status

Exact P/N/B construction remains closed and independently audited. The B->XB->W arithmetic contract is now frozen, but numerical replay radii are still open. No remote Gram, far-tail endpoint, final Schur inequality, index<=3, exact-zero, RH, or GRH claim follows.
