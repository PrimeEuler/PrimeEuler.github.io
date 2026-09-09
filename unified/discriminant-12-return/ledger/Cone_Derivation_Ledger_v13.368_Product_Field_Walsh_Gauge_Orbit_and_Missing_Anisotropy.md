# Cone Derivation Ledger v13.368 — Product-Field Walsh Gauge Orbit and Missing Anisotropy

**Date:** 2026-09-09

## Purpose
Continue v13.367 by asking whether the complete four-channel Walsh data of \(F(u,v)=uv\) recovers the aspect ratio of a general rectangular coarse cell.

## Exact result 1: one algebraic constraint
For rectangle center \((U,V)\) and half-widths \((h_u,h_v)\), define
\[
A=UV,\quad B=-h_uV,\quad C=-Uh_v,\quad D=h_uh_v.
\]
Then
\[
\boxed{AD=BC}.
\]
Thus only three of the four Walsh coefficients are independent.

## Exact result 2: reciprocal-scaling invariance
For any \(\lambda>0\),
\[
(U,h_u)\mapsto \lambda(U,h_u),
\qquad
(V,h_v)\mapsto \lambda^{-1}(V,h_v)
\]
leaves \(A,B,C,D\) unchanged.

Therefore
\[
\boxed{\text{full product-field Walsh data determines a reciprocal-scaling orbit, not a unique rectangle}.}
\]

## Exact result 3: missing anisotropy coordinate
The aspect ratio
\[
\sqrt{\Delta u/\Delta v}=\sqrt{h_u/h_v}
\]
changes along the reciprocal-scaling orbit. Hence it cannot be reconstructed from the product-field Walsh invariants alone.

The mixed mode fixes
\[
D=\frac{\Delta u\Delta v}{4},
\]
while the remaining channels fix dimensionless center/width ratios such as
\[
\frac{B}{D}=-\frac{V}{h_v},
\qquad
\frac{C}{D}=-\frac{U}{h_u}.
\]

## Exact result 4: rank-one factorization freedom
The four Walsh coefficients can be arranged into a rank-one \(2\times2\) matrix, so the missing coordinate is the standard factorization freedom
\[
xy^T=(\lambda x)(\lambda^{-1}y)^T.
\]
This supplies a precise linear-algebra interpretation of the reciprocal scale.

## Exact result 5: rapidity-form action
With \(\lambda=e^s\), the orbit becomes
\[
(U,h_u)\mapsto e^s(U,h_u),
\qquad
(V,h_v)\mapsto e^{-s}(V,h_v),
\]
which has the same exact multiplicative product-preserving form as factor-coordinate rapidity.

Guardrail: same algebraic action does not by itself establish a literal physical/operator identification.

## Endpoint-strip consequence
For the divisor endpoint strip,
\[
\Delta u=R_q-k,\qquad \Delta v=q,
\]
the mixed invariant gives
\[
\boxed{q(R_q-k)=\Delta_k-\Delta_{R_q}}.
\]
The separate factors \(q\) and \(R_q-k\), and therefore strip aspect ratio, require additional quotient-block information.

## Main interpretation
The cone/Walsh product geometry naturally quotients out reciprocal factor rescaling. This explains how the quarter mixed mode can close the cone while remaining blind to coarse-cell anisotropy.

## Guardrails
1. Do not claim unique rectangle reconstruction from product-field Walsh data.
2. Do not call reciprocal rank-one factorization freedom a physical gauge symmetry without a physical carrier.
3. Rapidity correspondence is exact at the product-preserving action level only.
4. No arithmetic or spectral conclusion follows from the degeneracy itself.

## Companion note
`research-notes/Product_Field_Walsh_Gauge_Orbit_and_Missing_Anisotropy.md`
