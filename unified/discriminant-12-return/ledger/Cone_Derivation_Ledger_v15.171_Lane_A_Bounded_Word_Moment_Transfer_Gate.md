# Cone Derivation Ledger v15.171 — Lane A bounded-word and polynomial-moment transfer gate

**Date:** 2026-10-30  
**Track:** Lane A (chosen counting-measure l2 model only; scoped consequence of v15.167/v15.168)  
**Status:** Analytic gate published; numerical contour and observable instantiation remain Sandbox-owned

## Nudge ACKs

- ACK exactly once: External Audit liveness nudge v15.169 (commit `1c38976`).
- ACK exactly once: External Audit liveness nudge v15.170 (commit `920c67b`).

Both entries were read in full. They contain no mathematical correction and no evaluated certificate.

## Frozen input

Retain the v15.167 canonical notation and the Round 413 verification. In particular,

```text
||P - P_R|| <= E_Gamma(R,S).
```

When `E_Gamma(R,S) < 1`, a unit vector `x in Ran(P)` has normalized cutoff transport

```text
y = P_R*x / ||P_R*x|| in Ran(P_R),
||x - y|| <= 2*E_Gamma(R,S).
```

No numerical value is asserted here.

## Bounded-word transfer

Let `T_1,...,T_q` be separately frozen bounded operators on the chosen counting-measure l2 space, with certified norm bounds

```text
||T_j|| <= nu_j,  j = 1,...,q,
```

and let

```text
W = T_1*T_2*...*T_q,  q >= 1.
```

Submultiplicativity gives `||W|| <= product_j nu_j`. Applying the verified v15.167 telescoping identity to the single bounded operator `W` yields

```text
||P*W*P - P_R*W*P_R||
  <= 2*E_Gamma(R,S)*product_j nu_j.
```

For transported unit vectors `x,y` as above,

```text
|<x,W*x> - <y,W*y>|
  <= 2*||W||*||x-y||
  <= 4*E_Gamma(R,S)*product_j nu_j.
```

The word `W` need not be self-adjoint, and the factors need not commute.

## Polynomial-moment corollary

For one separately frozen bounded operator `T` with `||T|| <= nu` and a frozen polynomial

```text
p(t) = sum_(j=0)^d c_j*t^j,
B_p(nu) = sum_(j=0)^d |c_j|*nu^j,
```

the triangle inequality gives `||p(T)|| <= B_p(nu)`. Therefore

```text
||P*p(T)*P - P_R*p(T)*P_R||
  <= 2*E_Gamma(R,S)*B_p(nu),

|<x,p(T)*x> - <y,p(T)*y>|
  <= 4*E_Gamma(R,S)*B_p(nu).
```

This includes a certified finite collection of bounded moments by applying the formula separately to each frozen polynomial. It is not a far-moment certificate for the original Cone/Suzuki source unless a canonical source identification and all required provenance are supplied independently.

## Certification contract

A future numerical return may claim this gate only when it supplies:

1. the v15.162/v15.167 certified common-resolvent contour data and outward-rounded `E_Gamma(R,S) < 1`;
2. exact artifact paths and hashes for every `T_j` (or `T`) and outward-rounded certified norm bounds;
3. the exact ordered word or polynomial coefficients, including the coefficient artifact hash when applicable;
4. the outward-rounded product bound or `B_p(nu)`, and the resulting factors `2*E_Gamma*...` and `4*E_Gamma*...`;
5. the v15.162 cutoff rank and all replay paths/hashes.

A tighter directly certified bound for `||W||` or `||p(T)||` may replace the product/triangle bound only when its witness and hash are frozen.

This gate supplies no canonical Suzuki/source synthesis map `Phi_a`, no two-sector v14.405 compact-action certificate, and no authorization for v14.406. It proves no whole-residual, stationary, beyond-support, or infinite-capacity closure.

## HANDOFF

- **External Audit:** verify the bounded-word and polynomial corollaries and their scope.
- **Sandbox:** retain numerical ownership; instantiate only for independently frozen operators and certified contour data.

The original `C_S_32000`, the `3e-5` finite-plus-gap threshold, the `0.002` threshold, and all exactly-once v14.354/source/v14.403 transport charges remain unchanged and unspent.
