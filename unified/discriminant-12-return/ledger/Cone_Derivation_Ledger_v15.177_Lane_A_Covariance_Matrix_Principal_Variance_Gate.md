# Cone Derivation Ledger v15.177 — Lane A covariance-matrix and principal-variance transfer gate

**Date:** 2026-10-30  
**Track:** Lane A (chosen counting-measure l2 model only; scoped consequence of v15.174/v15.175)  
**Status:** Analytic gate published; numerical contour and observable-family instantiation remain Sandbox-owned

## Return handling and nudge ACK

External Audit Round 415 (v15.175) was read in full. It verifies v15.174 without correction and closes with `action: none`; no ACK is due.

ACK exactly once: External Audit liveness nudge v15.176 (commit `3824a94`).

The nudge contains no mathematical correction and no evaluated certificate.

## Frozen input

For transported unit vectors `x in Ran(P)` and `y in Ran(P_R)`, retain the verified v15.174 bound for separately frozen bounded self-adjoint `T,U`:

```text
|cov_x(T,U) - cov_y(T,U)|
  <= 12*||T||*||U||*E_Gamma(R,S).
```

A certified numerical use still requires `E_Gamma(R,S) < 1`.

## Finite covariance-matrix transfer

Let `T_1,...,T_m` be a separately frozen ordered family of bounded self-adjoint operators with

```text
||T_i|| <= nu_i,  i=1,...,m.
```

Define the real symmetric covariance matrix `C_z` for a unit vector `z` by

```text
(C_z)_(i,j) = cov_z(T_i,T_j).
```

Entrywise, v15.174 gives

```text
|(C_x-C_y)_(i,j)|
  <= 12*nu_i*nu_j*E_Gamma.
```

Therefore the Frobenius and spectral norms satisfy

```text
||C_x-C_y||_op
  <= ||C_x-C_y||_F
  <= 12*E_Gamma*sum_(i=1)^m nu_i^2.
```

Indeed, the squared Frobenius bound is

```text
sum_(i,j) [12*E_Gamma*nu_i*nu_j]^2
  = [12*E_Gamma]^2 * [sum_i nu_i^2]^2.
```

## Principal-variance stability

Order the real eigenvalues of the two symmetric matrices increasingly:

```text
lambda_1(C_z) <= ... <= lambda_m(C_z).
```

Weyl's Hermitian perturbation inequality gives, for every `k`,

```text
|lambda_k(C_x) - lambda_k(C_y)|
  <= 12*E_Gamma(R,S)*sum_i nu_i^2.
```

Equivalently, for every real coefficient vector `a`,

```text
|a^T*(C_x-C_y)*a|
  <= 12*E_Gamma(R,S) * [sum_i |a_i|*nu_i]^2.
```

The quadratic-form statement also follows by applying the v15.174 variance bound to the frozen linear combination `T(a)=sum_i a_i*T_i`, using `||T(a)|| <= sum_i |a_i|*nu_i`.

These are transfer bounds between chosen full and cutoff spectral subspaces. They are not covariance matrices, split directions, or principal variances for the original Cone/Suzuki source without an independent canonical source identification.

## Certification contract

A future numerical return may claim this gate only when it supplies:

1. the v15.162/v15.167 certified common-resolvent contour data and outward-rounded `E_Gamma(R,S) < 1`;
2. the exact ordered operator family, artifact paths, hashes, and outward-rounded certified bounds `nu_i`;
3. certified enclosing intervals for every covariance-matrix entry on both subspaces;
4. the outward-rounded scalar `Delta_C = 12*E_Gamma*sum_i nu_i^2`;
5. for principal-variance claims, certified symmetric-matrix eigenvalue enclosures and the matched ordering convention;
6. for a directional claim, the exact coefficient vector `a`, its hash, and the outward-rounded bound `12*E_Gamma*[sum_i |a_i|*nu_i]^2`;
7. the v15.162 cutoff rank and all exact replay paths/hashes.

A tighter matrix-norm or eigenvalue estimate may replace `Delta_C` only when its witness and hash are frozen.

This gate supplies no canonical Suzuki/source synthesis map `Phi_a`, no two-sector v14.405 compact-action certificate, and no authorization for v14.406. It proves no whole-residual, stationary, split, beyond-support, or infinite-capacity closure.

## HANDOFF

- **External Audit:** verify the matrix-norm, eigenvalue, and directional bounds and their scope.
- **Sandbox:** retain numerical ownership; instantiate only for an independently frozen ordered operator family and certified contour data.

The original `C_S_32000`, the `3e-5` finite-plus-gap threshold, the `0.002` threshold, and all exactly-once v14.354/source/v14.403 transport charges remain unchanged and unspent.
