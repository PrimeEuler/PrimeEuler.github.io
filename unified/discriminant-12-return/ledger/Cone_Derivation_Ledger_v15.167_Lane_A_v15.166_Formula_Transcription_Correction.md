# Cone Derivation Ledger v15.167 — Lane A v15.166 formula-transcription correction

**Date:** 2026-10-30  
**Track:** Lane A (additive correction; chosen counting-measure l2 model only)  
**Status:** Supersedes the formula display in v15.166; v15.166 nudge ACKs remain valid and are not repeated

## Correction

Post-write replay of v15.166 found that Markdown publication removed most backslashes from its displayed formulas. The prose scope and the exactly-once ACKs in v15.166 remain valid, but no certificate should cite the malformed formula display there. The following plain-text formulas are the canonical statement of that gate.

Let Gamma be contained in rho(D) intersect rho(K) intersect rho(K_R), and define the Riesz projectors

```text
P   = (1 / (2*pi*i)) integral_Gamma (K   - z)^(-1) dz
P_R = (1 / (2*pi*i)) integral_Gamma (K_R - z)^(-1) dz
```

Using the v15.162 quantity

```text
E_Gamma(R,S)
  = [length(Gamma) / (2*pi)]
    * A_R(Gamma) * [1 + M*A(Gamma)]
    * [h_(R,S)(Gamma) + M*tau_S(Gamma) + M*tau_R(Gamma)],
```

the frozen prior gate is

```text
||P - P_R|| <= E_Gamma(R,S).
```

For every separately frozen bounded operator T on the chosen counting-measure l2 space,

```text
P*T*P - P_R*T*P_R
  = (P - P_R)*T*P + P_R*T*(P - P_R),

||P*T*P - P_R*T*P_R|| <= 2*||T||*E_Gamma(R,S).
```

No commutation of T with P or P_R is assumed.

If E_Gamma(R,S) < 1 and x is a unit vector in Ran(P), then

```text
y = P_R*x / ||P_R*x||
```

is well-defined in Ran(P_R), because

```text
||x - P_R*x|| <= E_Gamma,
||P_R*x|| >= 1 - E_Gamma > 0,
||x - y|| <= 2*E_Gamma.
```

For bounded self-adjoint T this yields

```text
|<x,T*x> - <y,T*y>| <= 4*||T||*E_Gamma(R,S).
```

The symmetric statement holds after interchanging P and P_R.

## Certification contract and scope

The v15.166 certification contract is retained with this correction: a numerical return must provide certified common-resolvent contour data, outward-rounded E_Gamma(R,S) < 1, the exact path/hash and certified norm bound of a separately frozen bounded T, the outward-rounded products 2*||T||*E_Gamma and (when used) 4*||T||*E_Gamma, the v15.162 cutoff rank, and all replay hashes.

This is only a chosen-l2 bounded-observable transfer statement. It supplies no canonical Suzuki/source identification, does not repair the missing source-prescribed synthesis map Phi_a, does not provide the absent two-sector v14.405 compact-action certificate, and does not authorize v14.406. It proves no whole-residual, stationary, or infinite-capacity closure.

## HANDOFF

- **External Audit:** verify these canonical plain-text formulas and the correction scope.
- **Sandbox:** retain numerical-contour ownership; instantiate this gate only for an independently frozen bounded T.

The original C_S_32000, the 3e-5 finite-plus-gap threshold, the 0.002 threshold, and all exactly-once v14.354/source/v14.403 transport charges remain unchanged and unspent.
