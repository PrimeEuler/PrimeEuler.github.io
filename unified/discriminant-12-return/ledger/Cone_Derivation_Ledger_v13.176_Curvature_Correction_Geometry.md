# Cone Derivation Ledger v13.176 — Geometric Meaning of the Terminal Curvature Correction

**Status:** Exact continuation of v13.175  
**Date:** 2026-09-03  
**Scope:** Geometric interpretation of the exact terminal correction
\[
\frac{\theta^2}{m\sqrt n-\theta}
\]
as the nonlinear departure of the constant-product hyperbola from its tangent line at the diagonal shell point.

## Audit convention

- **[D]** exact derived
- **[I]** interpretation
- **[O]** open
- **[Audit]** limitation / scope correction

---

## 1. Setup

Let

\[
r=\sqrt n.
\]

For the terminal active diagonal level at resolution `m`, write

\[
\theta=\{m(r-1)\}\in[0,1),
\]

and define the physical diagonal offset

\[
\boxed{d=\frac{\theta}{m}}.
\]

Then the terminal diagonal level is

\[
\boxed{u=r-d}.
\]

The corresponding row `y=u` meets the shell `xy=n=r^2` at

\[
\boxed{x=\frac{r^2}{r-d}}.
\]

The one-sided gnomon arm is

\[
g=x-u.
\]

v13.175 gave

\[
\boxed{mg=2\theta+\frac{\theta^2}{mr-\theta}}.
\]

We now identify the second term geometrically.

---

## 2. Tangent line to the shell at the diagonal point

The constant-product shell is

\[
xy=r^2.
\]

At its diagonal point

\[
(r,r),
\]

the gradient is `(r,r)`, so the tangent line is

\[
\boxed{x+y=2r}.
\]

On the terminal row

\[
y=u=r-d,
\]

the tangent line predicts the horizontal coordinate

\[
x_{\rm tan}=2r-(r-d)=r+d.
\]

Thus the tangent-line approximation to the one-sided arm from `(u,u)` is

\[
\begin{aligned}
g_{\rm lin}
&=x_{\rm tan}-u\\
&=(r+d)-(r-d)\\
&=\boxed{2d}.
\end{aligned}
\]

After scaling by `m`,

\[
\boxed{m g_{\rm lin}=2\theta}.
\]

**[D]** The leading term `2 theta` in the terminal phase law is exactly the arm length predicted by the tangent line to `xy=n` at `(sqrt n,sqrt n)`.

---

## 3. Exact nonlinear excess over the tangent prediction

The actual shell crossing is

\[
x=\frac{r^2}{r-d}.
\]

Use

\[
r^2=(r-d)(r+d)+d^2.
\]

Therefore

\[
\frac{r^2}{r-d}
=
 r+d+\frac{d^2}{r-d}.
\]

Hence

\[
\boxed{x-x_{\rm tan}=\frac{d^2}{r-d}}.
\]

The exact one-sided arm becomes

\[
\boxed{
g
=2d+\frac{d^2}{r-d}.
}
\]

Multiplying by `m`, with `d=theta/m`, gives

\[
\boxed{
mg
=2\theta+\frac{\theta^2}{mr-\theta}.
}
\]

Thus the term isolated in v13.175 is exactly

\[
\boxed{
\frac{\theta^2}{mr-\theta}
=
m\,(x-x_{\rm tan}).
}
\]

**[D] Curvature-correction theorem.** The finite-resolution correction in the terminal phase law is precisely the mesh-scaled horizontal excess of the true hyperbola over its tangent-line approximation at the diagonal shell point.

This is not merely analogous to curvature; it is the exact secant/tangent deviation for the relevant row intersection.

---

## 4. Cone interpretation

For the shell crossing `(x,u)`, Paper A uses

\[
X=\frac{x-u}{2},
\qquad
T=\frac{x+u}{2},
\qquad
Y=r.
\]

Since

\[
x-u
=2d+\frac{d^2}{r-d},
\]

we obtain

\[
\boxed{
X=d+\frac{d^2}{2(r-d)}.
}
\]

Also

\[
T
=\frac{x+u}{2}
=r+\frac{d^2}{2(r-d)}.
\]

Therefore

\[
\boxed{
T-r
=
X-d
=
\frac{d^2}{2(r-d)}.
}
\]

Equivalently,

\[
\boxed{
x-x_{\rm tan}=2(T-r)=2(X-d).}
\]

**[D]** Half of the factor-space curvature correction is exactly the vertical lift of the side-view hyperbola above its vertex level `T=r`.

Thus the same correction is visible in three exactly equivalent ways:

\[
\boxed{
\text{factor-space horizontal excess}
=2\times\text{Cone time lift}
=2\times\text{Cone }X\text{-excess over the linear tangent prediction}.
}
\]

---

## 5. Side-view hyperbola and vertex sag

On the shell `Y=r`, the Cone side view satisfies

\[
\boxed{T^2-X^2=r^2}.
\]

Hence

\[
T=\sqrt{r^2+X^2}.
\]

Relative to the vertex `(X,T)=(0,r)`, the vertical sag is

\[
T-r
=\frac{X^2}{T+r}.
\]

From the terminal-row relation

\[
T-X=u=r-d,
\]

we also have

\[
\boxed{d=X-(T-r)}.
\]

Rearranging,

\[
\boxed{X=d+(T-r)}.
\]

This is the Cone-side version of

\[
g=2d+\frac{d^2}{r-d}.
\]

**[D]** The linearized tangent geometry contributes `X≈d`; the exact shell curvature adds the vertex sag `T-r`.

---

## 6. Flat row-parabola interpretation

For the terminal row `y=u`, the flat `(X,Y)` projection obeys

\[
Y^2=u^2+2uX.
\]

On the shell `Y=r`, solving for `X` gives

\[
X
=
\frac{r^2-u^2}{2u}.
\]

With `u=r-d`,

\[
\begin{aligned}
X
&=\frac{r^2-(r-d)^2}{2(r-d)}\\
&=\frac{2rd-d^2}{2(r-d)}\\
&=d+\frac{d^2}{2(r-d)}.
\end{aligned}
\]

So the same curvature correction is built directly into the row parabola:

\[
\boxed{
X-d=\frac{d^2}{2(r-d)}.
}
\]

**[D]** The factor hyperbola, the Cone side-view hyperbola, and the Paper-A row parabola all encode exactly the same nonlinear correction.

---

## 7. Mesh-scaled form and terminal phase law

Because

\[
d=\frac{\theta}{m},
\]

we have

\[
m(T-r)
=
\frac{\theta^2}{2(mr-\theta)}.
\]

Therefore

\[
\boxed{
mg
=2\theta+2m(T-r).
}
\]

Equivalently,

\[
\boxed{
A_{\rm term}
=2\theta+2m(T-r).
}
\]

The terminal modular phase is

\[
\boxed{
\phi_{\rm term}
=
\left\{2\theta+2m(T-r)\right\}.
}
\]

This is a cleaner geometric statement than the raw rational correction term.

**[D]** The exact terminal phase decomposes into:

\[
\boxed{
\text{linear tangent contribution}
+
\text{twice the mesh-scaled hyperbolic vertex sag}.
}
\]

---

## 8. Fine-resolution curvature expansion

For fixed shell radius `r` and fixed phase `theta`, as `m->infinity`,

\[
\frac{\theta^2}{mr-\theta}
=
\frac{\theta^2}{mr}
+O(m^{-2}).
\]

Hence

\[
\boxed{
A_{\rm term}
=2\theta+
\frac{\theta^2}{m\sqrt n}
+O(m^{-2}).
}
\]

The correction is quadratic in the intra-cell displacement and inverse-linear in the shell radius.

This is exactly the expected local behavior of a smooth conic near a tangent point: the first-order term is tangent-linear, while the first nonlinear departure is quadratic.

**[I]** It is therefore natural to call the second term a curvature correction. The exact theorem, however, is the tangent-deviation identity above; no differential-geometric curvature normalization is required for that statement.

---

## 9. Cell-center case

At exact terminal cell center,

\[
\theta=\frac12,
\qquad
 d=\frac1{2m}.
\]

Then

\[
\boxed{
mg
=1+\frac{1}{4mr-2}.
}
\]

The tangent-line contribution is exactly one mesh step:

\[
2\theta=1.
\]

The true shell lies slightly beyond it by

\[
\boxed{
\frac{1}{4mr-2}
=2m(T-r).
}
\]

Thus the first symmetric arm pair has already entered at cell center because positive curvature pushes the shell just beyond the tangent prediction.

**[D]** This gives an exact geometric explanation for v13.175's observation that the first arm-pair jump occurs slightly before `theta=1/2`.

At `theta=1/2`, the tangent line is exactly at the one-step threshold, while the true hyperbola is strictly beyond it.

---

## 10. Why the first jump occurs before cell center

The first pair appears when

\[
mg=1.
\]

But

\[
mg
=2\theta+
\underbrace{\frac{\theta^2}{mr-\theta}}_{>0\text{ for }\theta>0}.
\]

Therefore the equality `mg=1` must occur at

\[
\boxed{\theta<\frac12}.
\]

This is not an accidental floor-function effect. It follows directly from the fact that the hyperbola bows beyond its tangent line.

The exact threshold from v13.175,

\[
\theta_1(M)
=
\frac{2M+1-\sqrt{4M^2+1}}2,
\qquad M=mr,
\]

therefore has the geometric interpretation:

\[
\boxed{
\text{the first arm pair enters at the unique pre-center phase where hyperbolic curvature makes up the remaining tangent-line deficit.}
}
\]

---

## 11. n=11 specialization

For the 11-shell,

\[
r=\sqrt{11}.
\]

Let

\[
\theta_m=\{m(\sqrt{11}-1)\},
\qquad
 d_m=\frac{\theta_m}{m}.
\]

Then the terminal crossing satisfies

\[
\boxed{
X_m
=d_m+
\frac{d_m^2}{2(\sqrt{11}-d_m)},
}
\]

and

\[
\boxed{
T_m-\sqrt{11}
=
\frac{d_m^2}{2(\sqrt{11}-d_m)}.
}
\]

The scaled terminal arm is

\[
\boxed{
A_{11,\rm term}(m)
=2\theta_m
+2m(T_m-\sqrt{11}).
}
\]

Thus every integer refinement of the 11-shell carries an exact decomposition into tangent phase plus hyperbolic vertex sag.

---

## 12. Structural synthesis

The local terminal geometry is now exact:

\[
\boxed{
\text{diagonal offset }d
\longrightarrow
\text{tangent prediction }2d
\longrightarrow
\text{curvature excess }\frac{d^2}{r-d}
\longrightarrow
\text{exact gnomon arm}.
}
\]

In Cone coordinates:

\[
\boxed{
X=d+(T-r),
}
\]

and therefore

\[
\boxed{
mg
=2\theta+2m(T-r).
}
\]

This gives a direct exact bridge among:

- the mod-`1/m` tangent-cell phase `theta`;
- the Paper-A floor gnomon;
- the row parabola;
- the constant-product hyperbola;
- the Cone side-view hyperbola;
- the tangent/vertex geometry at `(sqrt n,sqrt n)`.

---

## 13. Audit conclusion

**[D] Established:** the correction

\[
\frac{\theta^2}{m\sqrt n-\theta}
\]

is exactly the mesh-scaled nonlinear excess of the shell crossing beyond the tangent-line prediction, equivalently twice the mesh-scaled Cone vertex sag `T-sqrt(n)`.

**[Audit]** This justifies the phrase "curvature correction" geometrically. It does not by itself assign arithmetic or physical significance to curvature beyond the exact conic geometry already present in Paper A.

## Next problem

**[O]** Compare this exact local sag with the small cell-centered circle construction. Determine whether the observed circle radius is exactly the tangent-line deficit, the Cone vertex sag, the cell half-width, or a simple function of these. If so, solve the circle/parabola or circle/hyperbola tangency condition algebraically for general `m`.
