# Cone Derivation Ledger v13.603 — M16001 Orthonormal-Nullspace Certificate Implementation

## Scope

Implement the v13.581 resolution of the non-orthonormal rational null basis.  The production checker is now

`research-notes/suzuki_M16001_orthonormal_nullspace_certificate.py`.

This entry records the implementation contract and deliberately distinguishes implementation from execution: the GitHub connector used for this write cannot execute repository Python, so no numerical PASS transcript or generated interval payload hash is promoted in this ledger entry.

## Exact layer

The checker reconstructs the v13.571 exact rational N0 from the frozen Q payload and deterministic pivot/free-variable construction, then forms

[
G_N=N_0^TN_0\in\mathbb Q^{4\times4}.
]

It performs an exact Fraction LDL^T factorization and requires all four exact pivots to be strictly positive.  This certifies G_N positive definite without floating linear algebra.

## Outward interval layer

The checker uses 120-digit Decimal interval arithmetic with directed ROUND_FLOOR / ROUND_CEILING operations.

It constructs the upper Cholesky enclosure R satisfying

[
G_N\in R^TR,
]

then a triangular inverse enclosure U satisfying

[
I_4\in RU,
]

and finally

[
N_\perp=N_0U.
]

The generated interval matrices are:

- exact-G interval image, 4x4;
- R, 4x4;
- R^{-1}, 4x4;
- N_perp, 10x4.

Every generated payload is serialized and SHA-256 hashed by the checker.

## Authoritative verification gates

Execution fails closed unless all of the following hold entrywise:

[
0\in R^TR-G_N,
]

[
0\in RR^{-1}-I_4,
]

[
0\in Q^TN_\perp,
]

and

[
0\in N_\perp^TN_\perp-I_4.
]

The exact upstream relation Q^T N0=0 is also rechecked before interval work begins.

The terminal line is

`ORTHONORMAL NULLSPACE CERTIFICATE: PASS`

only after all exact and interval assertions succeed.

## Generated certificate

On successful execution the checker writes

`research-notes/certificates/M16001_orthonormal_nullspace_certificate.json`

plus four canonical interval payloads and reports their SHA-256 hashes and maximum interval widths.

## Downstream effect

After an execution transcript is captured, the replay basis is B_perp=[P,N_perp], not the raw rational [P,N0] and not the old SVD basis.  B_perp, X B_perp, W_perp, finite QN/NN projections, p/a_q/b_q, remote rows and Gram, far moments, block tail bounds, and the final Schur endpoint must then be recomputed.

The independent P^T P normalization gate from v13.581 remains open and should be checked before ordinary Euclidean six-plane bounds are promoted.

## Status

Implementation complete.  Numerical execution and payload freezing are explicitly pending; this entry does not claim a successfully executed interval certificate.  Certified inertia status is unchanged.  No index<=3, exact-zero, RH, or GRH claim follows.
