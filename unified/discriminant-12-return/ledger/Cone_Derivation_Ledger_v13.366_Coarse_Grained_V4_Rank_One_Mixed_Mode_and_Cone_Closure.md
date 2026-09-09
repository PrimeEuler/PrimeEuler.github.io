# Cone Derivation Ledger v13.366 — Coarse-Grained V4 Rank-One Mixed Mode and Cone Closure

## Scope

This checkpoint tests the stability of the v13.365 local rank-one / V4-Walsh quarter-mode cone closure under coarse graining from one elementary factor cell to an arbitrary axis-aligned rectangle.

Companion note:

`research-notes/Coarse_Grained_V4_Rank_One_Mixed_Mode_and_Cone_Closure.md`

The result is exact: rank-one closure and cone reconstruction survive arbitrary rectangular coarse graining. The elementary `1/4` is the unit-square specialization of the general normalized mixed quantity `Delta u Delta v / 4`. The Casimir interpretation remains canonical for isotropic square spacing.

---

## 1. Coarse rectangle

Let

\[
R=[a,b]\times[c,d],
\]

with center coordinates

\[
U=\frac{a+b}{2},\qquad V=\frac{c+d}{2},
\]

and half-widths

\[
h_u=\frac{b-a}{2},\qquad h_v=\frac{d-c}{2}.
\]

For `F(u,v)=uv`, the four corners are

\[
F_{00}=ac,\quad F_{10}=bc,\quad F_{01}=ad,\quad F_{11}=bd,
\]

and satisfy

\[
\boxed{F_{00}F_{11}=F_{10}F_{01}}.
\]

---

## 2. Coarse V4/Walsh coefficients

With the normalized four-point Hadamard transform,

\[
\boxed{\widehat F_0=UV},
\]

\[
\boxed{\widehat F_5=-h_uV},
\]

\[
\boxed{\widehat F_7=-Uh_v},
\]

\[
\boxed{\widehat F_{11}=h_uh_v=\frac{(b-a)(d-c)}4}.
\]

Hence

\[
\boxed{
\widehat F_0\widehat F_{11}
=\widehat F_5\widehat F_7.
}
\]

The local rank-one determinant identity therefore survives coarse graining exactly.

---

## 3. Cone reconstruction

Recover

\[
U=-\frac{\widehat F_7}{h_v},\qquad
V=-\frac{\widehat F_5}{h_u}.
\]

Define

\[
T_c=\frac{U+V}{2},\qquad
X_c=\frac{U-V}{2},\qquad
Y_c^2=UV=\widehat F_0.
\]

Then

\[
\boxed{T_c^2-X_c^2-Y_c^2=0}.
\]

Thus exact cone closure is scale-stable for arbitrary axis-aligned rectangles.

---

## 4. Quarter-mode refinement

For an isotropic square cell of side `delta`,

\[
h_u=h_v=\frac\delta2,
\]

so

\[
\boxed{
\widehat F_{11}=\frac{\delta^2}{4}=M_F^2.
}
\]

For a general rectangle,

\[
\boxed{
\widehat F_{11}=\frac{\Delta u\,\Delta v}{4}.
}
\]

Therefore the numerical quarter shift is the square-cell specialization of a more general normalized mixed-area invariant.

---

## 5. Exact additivity over elementary cells

If the rectangle spans `m` columns and `r` rows of lattice spacing `delta`, then

\[
\Delta u=m\delta,\qquad \Delta v=r\delta,
\]

and

\[
\boxed{
\widehat F_{11}^{\rm coarse}
=\frac{mr\delta^2}{4}
=mr\,M_F^2.
}
\]

Since there are `mr` elementary cells,

\[
\boxed{
\widehat F_{11}^{\rm coarse}
=\sum_{C\subset R}M_F^2(C).
}
\]

Thus the coarse mixed Walsh mode is exactly additive and equals the tiled sum of elementary quarter modes.

---

## 6. Square versus rectangular coarse blocks

For a square `s x s` coarse block,

\[
\widehat F_{11}^{\rm coarse}
=\frac{(s\delta)^2}{4},
\]

so it has the same formal Casimir-quarter form at effective spacing `s delta`.

For an anisotropic `m x r` rectangle with `m\ne r`,

\[
\widehat F_{11}^{\rm coarse}
=\frac{mr\delta^2}{4},
\]

and there is no canonical single isotropic Casimir spacing associated with it.

Therefore:

- mixed-curvature/Walsh coarse graining is fully rectangular;
- the oscillator/Casimir quarter interpretation is naturally isotropic.

---

## 7. Endpoint-strip specialization

For a divisor-shell endpoint strip,

\[
\Delta u=R_q-k,\qquad \Delta v=q
\]

on the unit lattice. Therefore

\[
\boxed{
\widehat F_{11}^{\rm strip}
=\frac{q(R_q-k)}4.
}
\]

Using the Euclidean transport identity

\[
\Delta_k-\Delta_{R_q}=q(R_q-k),
\]

gives

\[
\boxed{
\widehat F_{11}^{\rm strip}
=\frac{\Delta_k-\Delta_{R_q}}4.
}
\]

Hence the earlier sum-over-elementary-cells formula and the one-shot coarse four-corner Walsh coefficient are exactly the same object by telescoping.

---

## Relation to prior checkpoints

- v13.362: Euclidean defect loss equals accumulated mixed curvature over endpoint strips.
- v13.364: elementary mixed curvature, null-diamond norm, and Casimir quarter shift unified at `delta^2/4`.
- v13.365: local rank-one V4/Walsh determinant identity closes the centered cone.
- v13.366: the same rank-one closure survives arbitrary rectangular coarse graining; the quarter mode becomes `Delta u Delta v / 4` and is exactly additive over tiled elementary cells.

---

## Guardrails

- The `1/4` is not a universal scalar independent of scale; it is the unit-square/equal-spacing specialization.
- The general coarse mixed mode is `Delta u Delta v / 4`.
- Arbitrary rectangular coarse blocks do not automatically define new oscillator/Casimir systems.
- Square coarse blocks preserve the formal `delta_eff^2/4` Casimir shape.
- Local V4/Walsh position algebra remains distinct from global mod-12 residue characters.
- No new divisor asymptotic, primality theorem, factorization algorithm, RH/GRH, spectral, positivity, or Fredholm claim is made.

## Interpretation

The quarter invariant is scale-stable in the correct sense: rank-one closure and the null cone survive every rectangular coarse graining, while the normalized mixed mode scales exactly with rectangle area and equals the sum of elementary quarter modes. The Casimir shift is the isotropic square-cell realization of this broader mixed-curvature invariant.