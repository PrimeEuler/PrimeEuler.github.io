# Coarse-Grained V4 Rank-One Mixed Mode and Cone Closure

## Scope

This note tests whether the local four-corner rank-one / V4-Walsh quarter-mode structure survives coarse graining from one elementary factor cell to an arbitrary axis-aligned rectangle.

The answer is exact but requires one refinement: rank-one closure and cone reconstruction survive for every rectangle, while the local `1/4` becomes the product of the two half-widths. The familiar Casimir value `delta^2/4` is the isotropic square-cell specialization.

No claim is made that coarse rectangles define new oscillator representations or new Casimir operators.

---

## 1. Arbitrary rectangle

Let

\[
R=[a,b]\times[c,d],\qquad a<b,\ c<d.
\]

Define center coordinates and half-widths

\[
U=\frac{a+b}{2},\qquad V=\frac{c+d}{2},
\]

\[
h_u=\frac{b-a}{2},\qquad h_v=\frac{d-c}{2}.
\]

The four product-corner values of `F(u,v)=uv` are

\[
F_{00}=ac,\quad F_{10}=bc,\quad F_{01}=ad,\quad F_{11}=bd.
\]

They obey the exact rank-one relation

\[
\boxed{F_{00}F_{11}=F_{10}F_{01}}.
\]

---

## 2. Normalized four-point Walsh/V4 transform

Using the same normalized Hadamard convention as the elementary cell,

\[
\widehat F_{0}=\frac14(F_{00}+F_{10}+F_{01}+F_{11}),
\]

\[
\widehat F_{5}=\frac14(F_{00}-F_{10}+F_{01}-F_{11}),
\]

\[
\widehat F_{7}=\frac14(F_{00}+F_{10}-F_{01}-F_{11}),
\]

\[
\widehat F_{11}=\frac14(F_{00}-F_{10}-F_{01}+F_{11}).
\]

Direct evaluation gives

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

Thus the elementary quarter mode generalizes to the half-width product.

---

## 3. Coarse rank-one determinant identity

The Walsh coefficients satisfy

\[
\boxed{
\widehat F_0\widehat F_{11}
=
\widehat F_5\widehat F_7.
}
\]

Indeed,

\[
(UV)(h_uh_v)=(-h_uV)(-Uh_v).
\]

Therefore the rank-one closure from the elementary factor cell survives arbitrary axis-aligned coarse graining exactly.

---

## 4. Cone reconstruction for unequal side lengths

The center factor coordinates are recovered from the first-order Walsh modes by

\[
\boxed{U=-\frac{\widehat F_7}{h_v}},
\qquad
\boxed{V=-\frac{\widehat F_5}{h_u}}.
\]

Define the usual centered cone coordinates

\[
T_c=\frac{U+V}{2},\qquad
X_c=\frac{U-V}{2},\qquad
Y_c^2=UV=\widehat F_0.
\]

Then

\[
\boxed{T_c^2-X_c^2=UV=Y_c^2},
\]

hence

\[
\boxed{T_c^2-X_c^2-Y_c^2=0}.
\]

So cone closure is not restricted to elementary square cells. What changes under anisotropic coarse graining is the scale carried by the mixed Walsh coefficient.

---

## 5. Square-cell specialization and Casimir quarter shift

For an isotropic square cell of side `delta`,

\[
h_u=h_v=\frac\delta2.
\]

Therefore

\[
\boxed{
\widehat F_{11}=h_uh_v=\frac{\delta^2}{4}=M_F^2.
}
\]

This is precisely the quarter invariant used in the null-diamond and Casimir completion.

Thus `delta^2/4` is not an arbitrary universal constant attached to every coarse rectangle. It is the isotropic specialization of the more general mixed quantity

\[
\boxed{
\widehat F_{11}=\frac{\Delta u\,\Delta v}{4}.
}
\]

---

## 6. Exact additivity under lattice tiling

Suppose the coarse rectangle spans `m` elementary columns and `r` elementary rows of lattice spacing `delta`:

\[
\Delta u=m\delta,\qquad \Delta v=r\delta.
\]

Then

\[
\boxed{
\widehat F_{11}^{\rm coarse}
=\frac{mr\delta^2}{4}.
}
\]

Since each elementary cell contributes

\[
M_F^2=\frac{\delta^2}{4},
\]

and the rectangle contains `mr` elementary cells,

\[
\boxed{
\widehat F_{11}^{\rm coarse}
=mr\,M_F^2
=\sum_{C\subset R}M_F^2(C).
}
\]

Hence the mixed Walsh mode is exactly additive under rectangular coarse graining.

This is the normalized version of the telescoping raw mixed-difference identity

\[
F_{11}-F_{10}-F_{01}+F_{00}
=\Delta u\,\Delta v.
\]

---

## 7. When does the coarse mode look like one Casimir shift?

If the coarse block is square, `m=r=s`, then

\[
\widehat F_{11}^{\rm coarse}
=\frac{s^2\delta^2}{4}
=\frac{(s\delta)^2}{4}.
\]

Thus a square coarse block has the same formal quarter-shift shape at effective spacing

\[
\delta_{\rm eff}=s\delta.
\]

For a genuinely rectangular block, `m\ne r`,

\[
\widehat F_{11}^{\rm coarse}
=\frac{mr\delta^2}{4},
\]

which is not naturally a single isotropic Casimir shift without introducing an artificial effective spacing `sqrt(mr) delta`.

Therefore the oscillator/Casimir interpretation should remain attached to isotropic square cells (or square coarse blocks), while mixed-curvature additivity is valid for arbitrary rectangles.

---

## 8. Relation to divisor-shell endpoint strips

The endpoint strips of the quotient-block transport have dimensions

\[
\Delta u=R_q-k,\qquad \Delta v=q
\]

on the unit lattice. Their coarse mixed mode is therefore

\[
\boxed{
\widehat F_{11}^{\rm strip}
=\frac{q(R_q-k)}4.
}
\]

Using

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

This is exactly the accumulated elementary quarter-mode identity established earlier, now recovered directly as the coarse four-corner Walsh coefficient of the entire endpoint rectangle.

Thus there are two equivalent descriptions:

1. sum `M_F^2=1/4` over all elementary cells in the strip;
2. compute one coarse four-corner mixed Walsh coefficient of the strip.

They agree exactly by mixed-difference telescoping.

---

## Guardrails

- Rank-one closure survives arbitrary rectangular coarse graining.
- The numerical `1/4` is the unit-square specialization; in general the normalized mixed mode is `Delta u Delta v / 4`.
- The Casimir interpretation is canonical for isotropic square spacing, not arbitrary anisotropic rectangles.
- Coarse mixed-mode additivity is a finite-difference/telescoping fact; it does not construct a new oscillator representation.
- Local V4/Walsh cell-position labels remain distinct from global mod-12 Dirichlet-character carriers.

## Interpretation

The quarter invariant is elementary but not fragile. Its correct coarse-grained object is the normalized mixed area `Delta u Delta v/4`. Rank-one closure and cone reconstruction persist exactly at every rectangular scale, and the coarse mixed mode equals the sum of elementary quarter modes. The Casimir value `delta^2/4` is the isotropic square-cell member of this larger mixed-curvature family.