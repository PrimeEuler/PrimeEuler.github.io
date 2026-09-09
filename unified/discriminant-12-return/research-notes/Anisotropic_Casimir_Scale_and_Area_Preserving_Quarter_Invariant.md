# Anisotropic Casimir Scale and Area-Preserving Quarter Invariant

## Status
Exact algebraic continuation of v13.364--v13.366. This note separates the invariant that survives arbitrary rectangular coarse graining from the extra isotropy required by the usual one-spacing Casimir interpretation.

## 1. Rectangular four-corner cell
Let an axis-aligned rectangle have side lengths
\[
\Delta u>0,\qquad \Delta v>0,
\]
center
\[
U=\frac{u_-+u_+}{2},\qquad V=\frac{v_-+v_+}{2},
\]
and half-widths
\[
h_u=\frac{\Delta u}{2},\qquad h_v=\frac{\Delta v}{2}.
\]
For the product field \(F(u,v)=uv=Y^2\), the normalized four-corner Walsh coefficients are
\[
\widehat F_0=UV,
\]
\[
\widehat F_5=-h_uV,\qquad \widehat F_7=-Uh_v,
\]
\[
\boxed{\widehat F_{11}=h_uh_v=\frac{\Delta u\,\Delta v}{4}}.
\]
The rank-one relation remains
\[
\boxed{\widehat F_0\widehat F_{11}=\widehat F_5\widehat F_7}.
\]

## 2. Geometric-mean effective spacing
Define
\[
\boxed{\delta_{\rm gm}:=\sqrt{\Delta u\,\Delta v}}.
\]
Then the mixed coefficient always has the formal quarter-square representation
\[
\boxed{\widehat F_{11}=\frac{\delta_{\rm gm}^2}{4}}.
\]
This is exact for every rectangle.

However, \(\delta_{\rm gm}\) is an **area-equivalent scale**, not in general an actual lattice step in either coordinate. Only in the isotropic case
\[
\Delta u=\Delta v=\delta
\]
do we have
\[
\delta_{\rm gm}=\delta
\]
and recover the canonical local Casimir/null-diamond value
\[
M_F^2=\frac{\delta^2}{4}.
\]
Thus rectangular coarse cells admit an exact Casimir-*form* quarter square, but a canonical one-spacing Casimir interpretation requires additional isotropic structure.

## 3. Aspect ratio versus mixed invariant
Introduce the aspect ratio
\[
\lambda:=\sqrt{\frac{\Delta u}{\Delta v}}.
\]
Then
\[
\Delta u=\delta_{\rm gm}\lambda,
\qquad
\Delta v=\frac{\delta_{\rm gm}}{\lambda}.
\]
Hence
\[
\boxed{\widehat F_{11}=\frac{\delta_{\rm gm}^2}{4}}
\]
is independent of \(\lambda\).

Therefore the normalized mixed mode detects rectangular area but is blind to aspect ratio.

This gives a useful decomposition of rectangular coarse geometry into:

1. an **area/mixed scale** \(\delta_{\rm gm}^2=\Delta u\Delta v\), and
2. an **anisotropy coordinate** \(\lambda=\sqrt{\Delta u/\Delta v}\).

The quarter invariant carries the first but not the second.

## 4. Area-preserving anisotropic deformation
Consider
\[
\Delta u\mapsto e^s\Delta u,
\qquad
\Delta v\mapsto e^{-s}\Delta v.
\]
Then
\[
\Delta u\Delta v\mapsto\Delta u\Delta v,
\]
so
\[
\boxed{\widehat F_{11}\mapsto\widehat F_{11}}.
\]
Meanwhile
\[
\lambda\mapsto e^s\lambda.
\]
Thus the mixed quarter mode is invariant under reciprocal area-preserving stretch of the factor rectangle.

This is an exact algebraic invariance of the mixed coefficient. It should not yet be identified with a physical Lorentz boost or with an operator symmetry without an explicit carrier map.

## 5. Relation to rapidity-like parametrization
Writing
\[
s=\frac12\log\frac{\Delta u}{\Delta v}=\log\lambda,
\]
gives
\[
\Delta u=\delta_{\rm gm}e^s,
\qquad
\Delta v=\delta_{\rm gm}e^{-s}.
\]
This has the same reciprocal-exponential form as the factor-coordinate parametrization
\[
u=\rho e^s,\qquad v=\rho e^{-s},
\]
with invariant product.

The exact common algebra is:
\[
\boxed{\text{reciprocal scaling preserves the product}.}
\]
For the rectangle, the preserved product is \(\Delta u\Delta v\), hence the mixed quarter coefficient.

Guardrail: this establishes a structural analogy and an exact scaling identity, not a literal identification of cell aspect ratio with the point rapidity of Paper A/B.

## 6. Coarse square as isotropic section
The isotropic locus is
\[
\lambda=1\quad\Longleftrightarrow\quad \Delta u=\Delta v.
\]
On this locus,
\[
\delta_{\rm gm}=\Delta u=\Delta v,
\]
and the mixed coefficient becomes the canonical quarter shift
\[
\boxed{\widehat F_{11}=M_F^2=\frac{\delta^2}{4}}.
\]
Thus the usual Casimir quarter shift is naturally the isotropic section of the more general rectangular mixed invariant
\[
\frac{\Delta u\Delta v}{4}.
\]

This statement is exact as an algebraic specialization. It does not imply that every anisotropic rectangle defines a new Casimir representation.

## 7. Endpoint strips
For a divisor endpoint strip,
\[
\Delta u=R_q-k,
\qquad
\Delta v=q.
\]
Therefore
\[
\boxed{\delta_{{\rm gm},k,q}^2=q(R_q-k)=\Delta_k-\Delta_{R_q}}.
\]
The coarse mixed coefficient is
\[
\boxed{
\widehat F_{11}^{\rm strip}
=\frac{\delta_{{\rm gm},k,q}^2}{4}
=\frac{\Delta_k-\Delta_{R_q}}{4}.
}
\]
So Euclidean shell-defect reduction itself is the square of the strip's area-equivalent spacing:
\[
\boxed{
\Delta_k-\Delta_{R_q}=\delta_{{\rm gm},k,q}^2.
}
\]
The associated strip anisotropy is
\[
\lambda_{k,q}=\sqrt{\frac{R_q-k}{q}}.
\]
Hence shell-defect transport fixes the product/area scale but does not by itself determine the strip aspect ratio.

## 8. What this adds to the unification
The quarter-shift chain can now be refined:

\[
\boxed{
\frac{\Delta u\Delta v}{4}
=\text{coarse normalized mixed mode}
=\sum_{\text{elementary cells}}\frac{\delta^2}{4}.
}
\]

On the isotropic elementary carrier,
\[
\boxed{
\frac{\delta^2}{4}
=M_F^2
=\text{null-diamond midpoint norm}
=\text{Casimir centering correction}
=\text{local V4 mixed mode}.
}
\]

On a general rectangle, the exact survivor is the area-normalized mixed invariant \(\Delta u\Delta v/4\). The ordinary one-spacing Casimir interpretation is recovered on the isotropic section.

## 9. Guardrails
- The geometric-mean scale \(\delta_{\rm gm}\) is exact but generally auxiliary; it need not be a physical or lattice edge length.
- Do not claim a new anisotropic Casimir representation from the algebra alone.
- The mixed mode is blind to aspect ratio; additional channels or geometry are required to recover anisotropy.
- Reciprocal side-length scaling and factor-coordinate rapidity share exact product-preserving algebra, but their carriers are distinct.
- The local V4/Walsh position labels remain distinct from global mod-12 Dirichlet-character carriers.
- No primality, spectral, or asymptotic claim follows from this checkpoint.
