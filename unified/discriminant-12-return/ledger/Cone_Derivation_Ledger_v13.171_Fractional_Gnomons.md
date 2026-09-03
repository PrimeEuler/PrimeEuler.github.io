# Cone Derivation Ledger v13.171 — Fractional Gnomons and the Continuum Limit of Paper A

**Status:** Exact continuation of v13.170, grounded in Paper A Section 5  
**Date:** 2026-09-03

## 1. Source identity from Paper A

Paper A Section 5 writes the divisor summatory function as nested diagonal gnomons:

\[
\boxed{
D(n)=\sum_{u=1}^{\lfloor\sqrt n\rfloor}
\left[
2\left\lfloor\frac{n-u^2}{u}\right\rfloor+1
\right].
}
\]

The vertex of the `u`-th gnomon is `(u,u)`. One arm lies on the row `y=u`, which is one of Paper A's row parabolas. It terminates where that row meets `xy=n`.

The continuous one-sided arm length is

\[
\boxed{
\ell_n(u)=\frac nu-u=\frac{n-u^2}{u}.
}
\]

The exact integer arm count is `floor(ell_n(u))`.

Thus each summand has the literal form

\[
\boxed{2\lfloor\ell_n(u)\rfloor+1},
\]

meaning two mirror arms plus their shared diagonal vertex.

---

## 2. Refine the same gnomons, not a different counting problem

Let the mesh be

\[
\delta=\frac1m.
\]

To refine Paper A while preserving its original bounded region, keep

\[
x\ge1,\qquad y\ge1,\qquad xy\le n,
\]

but allow coordinates on the `1/m` lattice.

Define

\[
\boxed{
D_m^*(n)=
\#\left\{(x,y)\in\left(\frac1m\mathbb Z\right)^2:
 x\ge1,\ y\ge1,\ xy\le n
\right\}.
}
\]

For `m=1`, this is exactly the ordinary divisor summatory count:

\[
D_1^*(n)=D(n).
\]

Write

\[
x=\frac am,\qquad y=\frac bm.
\]

Then the refined region is equivalent to

\[
a\ge m,\qquad b\ge m,\qquad ab\le nm^2.
\]

**[D]** This is the exact fractional refinement of Paper A's lattice region with the lower cutoff `x,y>=1` retained.

---

## 3. Exact fractional-gnomon formula

The diagonal vertices are now

\[
u=\frac jm,
\qquad
j=m,m+1,\ldots,\lfloor m\sqrt n\rfloor.
\]

At a fixed refined level `u=j/m`, the row `y=u` reaches the hyperbola at

\[
x=\frac nu.
\]

Measured in mesh steps of size `1/m`, the one-sided arm contains

\[
\left\lfloor
m\left(\frac nu-u\right)
\right\rfloor
=
\left\lfloor
m\frac{n-u^2}{u}
\right\rfloor
\]

points beyond the vertex.

Therefore

\[
\boxed{
D_m^*(n)
=
\sum_{j=m}^{\lfloor m\sqrt n\rfloor}
\left[
2\left\lfloor
m\frac{n-(j/m)^2}{j/m}
\right\rfloor+1
\right].
}
\]

Equivalently, with `u=j/m`,

\[
\boxed{
D_m^*(n)
=
\sum_{
 u\in(1/m)\mathbb Z,
 1\le u\le\sqrt n}
\left[
2\left\lfloor m\frac{n-u^2}{u}\right\rfloor+1
\right].
}
\]

**[D] Fractional-gnomon theorem.** Paper A's integer formula extends exactly to every uniform rational mesh by multiplying the continuous arm length by the mesh density `m` before flooring.

This is the direct mathematical version of refining the visible gnomonic/parabolic cells from integers to half-integers, thirds, and finer divisions.

---

## 4. Scaled-integer form

Because `j=mu`,

\[
\left\lfloor
m\left(\frac nu-u\right)
\right\rfloor
=
\left\lfloor\frac{nm^2}{j}\right\rfloor-j.
\]

Hence

\[
\boxed{
D_m^*(n)
=
\sum_{j=m}^{\lfloor m\sqrt n\rfloor}
\left[
2\left(\left\lfloor\frac{nm^2}{j}\right\rfloor-j\right)+1
\right].
}
\]

This is exactly the ordinary diagonal-gnomon identity applied to the dilated hyperbola `ab<=nm^2`, but with the lower cutoff `a,b>=m` corresponding to `x,y>=1`.

---

## 5. Continuous profile behind every mesh

Define

\[
\boxed{g_n(u)=\frac{n-u^2}{u}=\frac nu-u},
\qquad 1\le u\le\sqrt n.
\]

Then

\[
g_n(\sqrt n)=0,
\]

and

\[
g_n'(u)=-\frac n{u^2}-1<0.
\]

So the one-sided gnomon arm length decreases strictly from

\[
g_n(1)=n-1
\]

to zero at the central tangent level `u=sqrt(n)`.

Every finite mesh is simply a discretization of this same fixed profile:

\[
\boxed{
\text{mesh count at }u
=
\lfloor m g_n(u)\rfloor.
}
\]

This makes the discrete-to-continuous relation explicit rather than metaphorical.

---

## 6. Continuum limit of the refined Paper-A count

Normalize by the lattice density `m^2`. Since the mesh area is `1/m^2`, the expected continuum quantity is

\[
\frac{D_m^*(n)}{m^2}.
\]

Using the exact gnomon formula, the `+1` diagonal terms contribute only `O(m)` points, hence vanish after division by `m^2`. The floor errors also contribute at most `O(m)` in total.

The remaining Riemann sum is

\[
\frac{2}{m}
\sum_{
 u\in(1/m)\mathbb Z,
 1\le u\le\sqrt n}
\left(\frac nu-u\right).
\]

Therefore

\[
\boxed{
\lim_{m\to\infty}
\frac{D_m^*(n)}{m^2}
=
2\int_1^{\sqrt n}\left(\frac nu-u\right)\,du.
}
\]

Evaluate:

\[
2\int_1^{\sqrt n}\left(\frac nu-u\right)du
=
2\left[n\log u-\frac{u^2}{2}\right]_1^{\sqrt n}
\]

\[
=
\boxed{n\log n-n+1}.
\]

Thus

\[
\boxed{
\lim_{m\to\infty}
\frac{D_m^*(n)}{m^2}
=n\log n-n+1.
}
\]

**[D] Continuum gnomon theorem.** The normalized fractional refinement of Paper A's exact gnomon count converges to the Euclidean area of the bounded continuous region

\[
\{(x,y):x\ge1,\ y\ge1,\ xy\le n\}.
\]

---

## 7. Why this gives `n log n - n + 1`, not just `n log n`

The continuous region retained by Paper A has lower boundary `y=1`. Its area is

\[
\int_1^n\left(\frac nx-1\right)dx
=
\boxed{n\log n-n+1}.
\]

By contrast,

\[
\int_1^n\frac nx\,dx=n\log n
\]

is the area under the hyperbola measured down to `y=0`.

So the two quantities differ by the rectangle

\[
\boxed{n-1}.
\]

**[Audit]** When discussing the continuum limit of the actual Paper-A divisor region, the exact geometric area is `n log n - n + 1`. The term `n log n` remains the reciprocal-profile integral and the leading asymptotic scale, but it is not by itself the full bounded-region area.

---

## 8. Half-integer and third-integer cases

For `m=2`, the exact refined count is

\[
\boxed{
D_2^*(n)
=
\sum_{
 u\in\frac12\mathbb Z,
 1\le u\le\sqrt n}
\left[
2\left\lfloor
2\frac{n-u^2}{u}
\right\rfloor+1
\right].
}
\]

For `m=3`,

\[
\boxed{
D_3^*(n)
=
\sum_{
 u\in\frac13\mathbb Z,
 1\le u\le\sqrt n}
\left[
2\left\lfloor
3\frac{n-u^2}{u}
\right\rfloor+1
\right].
}
\]

The same row-parabolas, diagonal spine, and constant-product hyperbola are present at every scale. Only the sampling frequency changes.

**[I]** The observed half-integer and third-integer central cell/tangent patterns should therefore be analyzed as local geometry inside these exact refined gnomons, rather than as a separate divisor construction.

---

## 9. Relation to the tangent point

The gnomon profile terminates at

\[
u=\sqrt n,
\]

because

\[
g_n(\sqrt n)=0.
\]

This is the same diagonal point

\[
(x,y)=(\sqrt n,\sqrt n)
\]

that gives the tangent/vertex point of the constant-product shell.

Thus the tangent point has a second exact interpretation:

\[
\boxed{
\text{it is the zero-length endpoint of the nested gnomon family.}
}
\]

For rational-square `n`, some finite rational grid contains that endpoint exactly. For nonsquare integer `n`, finite rational grids approach it but never land on it.

---

## 10. Relation to rapidity `s`

Rapidity remains

\[
x=\sqrt n e^s,\qquad y=\sqrt n e^{-s}.
\]

Paper A's `u` is not rapidity. Along the row-hyperbola crossing used by the `u`-gnomon,

\[
y=u,\qquad x=\frac nu.
\]

Therefore its rapidity is

\[
\boxed{
s(u)=\frac12\log\frac{x}{y}
=\frac12\log\frac{n}{u^2}
=\log\frac{\sqrt n}{u}.
}
\]

This gives the exact conversion

\[
\boxed{u=\sqrt n\,e^{-s}}.
\]

At the outermost gnomon `u=1`,

\[
s=\frac12\log n,
\]

while at the tangent endpoint `u=\sqrt n`,

\[
s=0.
\]

**[D]** Paper A's nested gnomon parameter `u` and the shell rapidity `s` are different coordinates on the same row/hyperbola crossing family, related exponentially.

Under this substitution,

\[
\frac nu-u
=
\sqrt n\,(e^s-e^{-s})
=
\boxed{2\sqrt n\sinh s}.
\]

So the continuous one-sided gnomon arm is exactly a hyperbolic-sine displacement in rapidity coordinates.

This is a stronger and cleaner bridge than identifying `u` with rapidity.

---

## 11. New exact identity: gnomon arm and Cone `X`

At the crossing point

\[
(x,y)=\left(\frac nu,u\right),
\]

Paper A's Cone coordinate is

\[
X=\frac{x-y}{2}
=\frac12\left(\frac nu-u\right).
\]

Therefore

\[
\boxed{
\frac{n-u^2}{u}=2X.
}
\]

This means the continuous one-sided gnomon arm length is exactly twice the Cone's horizontal displacement of the row/hyperbola crossing from the diagonal axis.

Consequently Paper A's summand can be written geometrically as

\[
\boxed{
2\left\lfloor2X_u\right\rfloor+1,
}
\]

where

\[
X_u=\frac12\left(\frac nu-u\right)
\]

is the `X` coordinate of the `u`-th row's intersection with `xy=n`.

**[D]** The floor-gnomon count is literally quantizing the Cone's horizontal displacement at each row-parabola / divisor-hyperbola crossing.

For a `1/m` refinement,

\[
\boxed{
\text{one-sided mesh count}
=\lfloor 2mX_u\rfloor.
}
\]

This appears to be the most direct exact formulation of the user's observation that finer fractional squares resolve the same tangent/parabolic geometry.

---

## 12. Immediate open problem: cell-centered tangency

The remaining geometric question is now sharply posed.

For each mesh `1/m`, Paper A gives exact crossing coordinates and exact arm counts. What remains to determine is whether the visually observed circles centered in the fractional cells are canonically tangent to the relevant row-parabola, anti-diagonal circle, constant-product shell, or some combination of these.

### [O]

Construct the actual `m=2` and `m=3` cell geometry around consecutive levels such as 5, 6, 7 and solve the tangency conditions exactly. If the centers satisfy a scale-independent formula, generalize it to arbitrary `m` and then take the real limit.

### Publication guardrail

Do not call the cell-centered circle construction an exact theorem until its center, radius, and tangent curve(s) have been identified algebraically. The fractional-gnomon formulas above are exact independently of that still-open local circle construction.
