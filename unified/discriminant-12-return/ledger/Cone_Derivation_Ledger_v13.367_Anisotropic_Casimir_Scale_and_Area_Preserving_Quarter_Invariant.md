# Cone Derivation Ledger v13.367 — Anisotropic Casimir Scale and Area-Preserving Quarter Invariant

**Date:** 2026-09-09

## Purpose
Continue v13.364--v13.366 by determining what part of the Casimir/quarter-shift structure survives arbitrary rectangular coarse graining and what part specifically requires isotropy.

## Exact result 1: general rectangular mixed quarter
For a rectangle with side lengths \(\Delta u,\Delta v\), the product field \(F=uv=Y^2\) has normalized mixed Walsh coefficient
\[
\boxed{\widehat F_{11}=\frac{\Delta u\Delta v}{4}}.
\]
The four-corner rank-one relation remains exact:
\[
\boxed{\widehat F_0\widehat F_{11}=\widehat F_5\widehat F_7}.
\]

## Exact result 2: geometric-mean effective scale
Define
\[
\boxed{\delta_{\rm gm}=\sqrt{\Delta u\Delta v}}.
\]
Then
\[
\boxed{\widehat F_{11}=\frac{\delta_{\rm gm}^2}{4}}.
\]
Thus every rectangle has an exact quarter-square representation in terms of its area-equivalent geometric-mean scale.

The canonical Casimir/null-diamond interpretation is stronger: it uses a single actual spacing \(\delta\) in both directions. Therefore
\[
\Delta u=\Delta v=\delta
\]
is the isotropic locus on which
\[
\delta_{\rm gm}=\delta,
\qquad
\widehat F_{11}=M_F^2=\frac{\delta^2}{4}.
\]

## Exact result 3: area scale and anisotropy separate
Let
\[
\lambda=\sqrt{\frac{\Delta u}{\Delta v}}.
\]
Then
\[
\Delta u=\delta_{\rm gm}\lambda,
\qquad
\Delta v=\delta_{\rm gm}/\lambda.
\]
The mixed mode depends only on \(\delta_{\rm gm}\):
\[
\boxed{\widehat F_{11}=\delta_{\rm gm}^2/4}
\]
and is blind to \(\lambda\).

Hence rectangular coarse geometry separates into:
- product/area scale \(\delta_{\rm gm}^2\), carried by the mixed quarter mode;
- anisotropy \(\lambda\), not carried by that mode.

## Exact result 4: reciprocal stretch invariance
Under
\[
\Delta u\mapsto e^s\Delta u,
\qquad
\Delta v\mapsto e^{-s}\Delta v,
\]
we have
\[
\boxed{\widehat F_{11}\mapsto\widehat F_{11}}.
\]
Equivalently, with
\[
s=\frac12\log(\Delta u/\Delta v),
\]
\[
\Delta u=\delta_{\rm gm}e^s,
\qquad
\Delta v=\delta_{\rm gm}e^{-s}.
\]
This is the same exact product-preserving algebraic form as the factor-coordinate rapidity parametrization, but the carriers must not be identified without an explicit map.

## Exact result 5: divisor endpoint strip effective scale
For the endpoint strip
\[
\Delta u=R_q-k,
\qquad
\Delta v=q,
\]
Euclidean transport gives
\[
\Delta_k-\Delta_{R_q}=q(R_q-k).
\]
Therefore
\[
\boxed{\delta_{{\rm gm},k,q}^2=\Delta_k-\Delta_{R_q}}
\]
and
\[
\boxed{
\widehat F_{11}^{\rm strip}
=\frac{\Delta_k-\Delta_{R_q}}4
=\frac{\delta_{{\rm gm},k,q}^2}{4}.
}
\]
The strip anisotropy is
\[
\lambda_{k,q}=\sqrt{(R_q-k)/q}.
\]
Thus the shell-defect reduction determines the area-equivalent scale but not the aspect ratio.

## Refined unification statement
The invariant that survives arbitrary rectangular coarse graining is
\[
\boxed{\frac{\Delta u\Delta v}{4}}.
\]
It is additive over elementary cells and is the normalized mixed four-corner coefficient.

On the isotropic elementary carrier this specializes to
\[
\boxed{
\frac{\delta^2}{4}
=M_F^2
=\text{null-diamond midpoint norm}
=\text{Casimir centering correction}
=\text{local V4/Walsh mixed mode}.
}
\]
Therefore the usual Casimir quarter shift is the isotropic specialization of a more general area-normalized mixed invariant.

## Guardrails
1. \(\delta_{\rm gm}\) is an exact area-equivalent scale, not generally an actual lattice spacing.
2. Do not infer a new anisotropic Casimir representation from the quarter-square algebra alone.
3. The mixed mode does not encode aspect ratio.
4. Reciprocal rectangle scaling and factor rapidity have the same product-preserving algebra but distinct carriers.
5. Local V4/Walsh labels remain distinct from global mod-12 character carriers.
6. No primality, spectral, or asymptotic conclusion is asserted.

## Companion note
`research-notes/Anisotropic_Casimir_Scale_and_Area_Preserving_Quarter_Invariant.md`
