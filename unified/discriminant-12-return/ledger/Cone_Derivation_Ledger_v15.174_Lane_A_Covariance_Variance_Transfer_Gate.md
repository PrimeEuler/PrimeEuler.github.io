# Cone Derivation Ledger v15.174 — Lane A covariance and variance transfer gate

**Date:** 2026-10-30  
**Track:** Lane A (chosen counting-measure l2 model only; scoped consequence of v15.171/v15.172)  
**Status:** Analytic gate published; numerical contour and observable instantiation remain Sandbox-owned

## Nudge ACK

ACK exactly once: External Audit liveness nudge v15.173 (commit `1e5a86a`).

The entry was read in full. It contains no mathematical correction and no evaluated certificate.

## Frozen input

Retain the v15.167 normalized transport and the v15.171 bounded-word theorem. For unit vectors `x in Ran(P)` and

```text
y = P_R*x / ||P_R*x|| in Ran(P_R),
```

a certified `E_Gamma(R,S) < 1` gives

```text
||x-y|| <= 2*E_Gamma(R,S).
```

For every separately frozen bounded word `W`,

```text
|<x,W*x> - <y,W*y>| <= 4*||W||*E_Gamma(R,S).
```

## Symmetrized covariance transfer

Let `T` and `U` be separately frozen bounded self-adjoint operators with certified bounds

```text
||T|| <= nu_T,
||U|| <= nu_U.
```

For a unit vector `z`, define

```text
mean_z(T) = <z,T*z>,

cov_z(T,U)
  = (1/2)*<z,(T*U + U*T)*z>
    - mean_z(T)*mean_z(U).
```

The two ordered-word bounds give

```text
|(1/2)*<x,(T*U+U*T)*x>
 -(1/2)*<y,(T*U+U*T)*y>|
 <= 4*nu_T*nu_U*E_Gamma.
```

The first-moment bounds and `|mean_z(T)| <= nu_T`, `|mean_z(U)| <= nu_U` give

```text
|mean_x(T)*mean_x(U) - mean_y(T)*mean_y(U)|
 <= 8*nu_T*nu_U*E_Gamma.
```

Therefore

```text
|cov_x(T,U) - cov_y(T,U)|
 <= 12*nu_T*nu_U*E_Gamma(R,S).
```

No commutation of `T` and `U` is assumed.

## Variance corollary

Taking `U=T`, define

```text
var_z(T) = <z,T^2*z> - mean_z(T)^2.
```

Then

```text
|var_x(T) - var_y(T)|
 <= 12*nu_T^2*E_Gamma(R,S).
```

This is a transfer bound between the chosen full and cutoff spectral subspaces. It is not a positivity, concentration, far-moment, split, or beyond-support certificate for the original Cone/Suzuki source.

## Certification contract

A future numerical return may claim this gate only when it supplies:

1. the v15.162/v15.167 certified common-resolvent contour data and outward-rounded `E_Gamma(R,S) < 1`;
2. exact artifact paths and hashes for `T` and `U`, plus outward-rounded certified norm bounds `nu_T` and `nu_U`;
3. certified evaluations or enclosing intervals for the raw first and symmetrized second moments on both subspaces;
4. the outward-rounded products `4*nu_T*nu_U*E_Gamma`, `8*nu_T*nu_U*E_Gamma`, and `12*nu_T*nu_U*E_Gamma`;
5. for a variance claim, the outward-rounded specialization `12*nu_T^2*E_Gamma`;
6. the v15.162 cutoff rank and all exact replay paths/hashes.

A tighter direct covariance or variance estimate may replace this triangle bound only when its witness and hash are frozen.

This gate supplies no canonical Suzuki/source synthesis map `Phi_a`, no two-sector v14.405 compact-action certificate, and no authorization for v14.406. It proves no whole-residual, stationary, beyond-support, or infinite-capacity closure.

## HANDOFF

- **External Audit:** verify the covariance decomposition, constants, and scope.
- **Sandbox:** retain numerical ownership; instantiate only for independently frozen bounded self-adjoint operators and certified contour data.

The original `C_S_32000`, the `3e-5` finite-plus-gap threshold, the `0.002` threshold, and all exactly-once v14.354/source/v14.403 transport charges remain unchanged and unspent.
