# Product-Field Walsh Gauge Orbit and Missing Anisotropy

## Status
Exact continuation of v13.367. This note determines whether the full four-channel Walsh data of the product field \(F(u,v)=uv\) determines an arbitrary rectangular cell. It does not: there is an exact one-parameter reciprocal-scaling degeneracy.

## 1. Rectangular Walsh data
For center \((U,V)\) and half-widths \((h_u,h_v)\),
\[
F_{\pm\pm}=(U\pm h_u)(V\pm h_v).
\]
The normalized Walsh coefficients are
\[
A:=\widehat F_0=UV,
\]
\[
B:=\widehat F_5=-h_uV,
\qquad
C:=\widehat F_7=-Uh_v,
\]
\[
D:=\widehat F_{11}=h_uh_v.
\]
They obey
\[
\boxed{AD=BC}.
\]
Hence the four coefficients contain only three independent scalar degrees of freedom.

## 2. Reciprocal scaling orbit
For any \(\lambda>0\), define
\[
U\mapsto \lambda U,
\qquad
h_u\mapsto \lambda h_u,
\]
\[
V\mapsto \lambda^{-1}V,
\qquad
h_v\mapsto \lambda^{-1}h_v.
\]
Then
\[
UV,\ h_uV,\ Uh_v,\ h_uh_v
\]
are all unchanged. Therefore
\[
\boxed{(A,B,C,D)\text{ is invariant under this one-parameter action}.}
\]
The complete four-corner product data cannot determine the separate \(u\)- and \(v\)-scales.

## 3. Aspect-ratio degeneracy
The rectangle aspect ratio is
\[
\lambda_{\rm rect}=\sqrt{\frac{\Delta u}{\Delta v}}=\sqrt{\frac{h_u}{h_v}}.
\]
Under reciprocal scaling it changes by the same scale factor:
\[
\lambda_{\rm rect}\mapsto \lambda\,\lambda_{\rm rect}.
\]
Thus aspect ratio lies along the product-field gauge orbit rather than in the Walsh invariants.

The mixed mode
\[
D=h_uh_v=\frac{\Delta u\Delta v}{4}
\]
fixes area, but even the full set \((A,B,C,D)\) fixes only reciprocal-scale-invariant combinations.

## 4. Exact invariant ratios
When denominators are nonzero,
\[
\frac{B}{D}=-\frac{V}{h_v},
\qquad
\frac{C}{D}=-\frac{U}{h_u},
\]
\[
\frac{B}{A}=-\frac{h_u}{U},
\qquad
\frac{C}{A}=-\frac{h_v}{V}.
\]
These determine center-to-half-width ratios but not an absolute split between the two factor directions.

## 5. Rapidity form of the gauge orbit
Write the reciprocal scale as \(\lambda=e^s\). Then
\[
(U,h_u)\mapsto e^s(U,h_u),
\qquad
(V,h_v)\mapsto e^{-s}(V,h_v).
\]
This is exactly the same multiplicative action as factor-coordinate rapidity
\[
u=\rho e^s,\qquad v=\rho e^{-s}.
\]
The product field is invariant because it only sees products of one \(u\)-sector factor and one \(v\)-sector factor.

Exact statement:
\[
\boxed{\text{the Walsh product data lives on reciprocal-scaling orbits}.}
\]

Guardrail: this is an algebraic orbit equivalence. It does not by itself identify the rectangle gauge parameter with a physical Lorentz boost parameter in an operator representation.

## 6. Rank-one matrix form
Arrange the Walsh coefficients as
\[
W=
\begin{pmatrix}
A & C\\
B & D
\end{pmatrix}
=
\begin{pmatrix}
V\\ h_v
\end{pmatrix}
\begin{pmatrix}
U & -h_u
\end{pmatrix}
\]
up to the chosen sign convention for \(B,C\). Hence
\[
\boxed{\det W=0}.
\]
The reciprocal gauge is exactly the standard rank-one factorization freedom
\[
x y^T=(\lambda x)(\lambda^{-1}y)^T.
\]
This gives a clean linear-algebra interpretation of the missing anisotropy coordinate.

## 7. Consequence for cone reconstruction
The centered cone variables reconstructed from the Walsh coefficients remain gauge invariant because they depend on invariant combinations. The cone therefore records the rank-one product geometry while quotienting out reciprocal factor rescaling.

This explains why the quarter mixed mode closes the cone without determining rectangle aspect ratio.

## 8. Endpoint-strip consequence
For a divisor endpoint strip,
\[
\Delta u=R_q-k,
\qquad
\Delta v=q,
\]
so the mixed mode determines only
\[
q(R_q-k)=\Delta_k-\Delta_{R_q}.
\]
The separate factors \(q\) and \(R_q-k\) are additional quotient-block data. The shell-defect reduction alone does not recover the strip aspect ratio
\[
\sqrt{\frac{R_q-k}{q}}.
\]

## 9. Guardrails
- Full Walsh data of \(F=uv\) is not enough to reconstruct all four rectangle parameters.
- The missing degree of freedom is exact reciprocal rank-one factorization freedom, not numerical error.
- The product-field gauge orbit should not be called a physical gauge symmetry without specifying a physical model.
- The analogy with rapidity is exact at the multiplicative-action level, but carrier distinctions remain essential.
