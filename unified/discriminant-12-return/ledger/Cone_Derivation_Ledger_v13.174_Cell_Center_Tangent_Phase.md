# Cone Derivation Ledger v13.174 — Cell-Center Tangency and Rational Phase Refinement

**Status:** Exact continuation of v13.173  
**Date:** 2026-09-03  
**Scope:** Diagonal cell centers, exact Cone tangency, mod-`1/m` tangent phase, and refinement of rational intra-cell phases.

## Audit convention

- **[D]** exact derived
- **[I]** interpretation
- **[O]** open
- **[Audit]** limitation / scope correction

---

## 1. A diagonal grid cell and its center

Fix a resolution `m>0` and write the cell width as

\[
\delta=\frac1m.
\]

On the boundary-anchored Paper-A grid, consecutive diagonal levels are

\[
u_j=1+\frac jm,
\qquad
u_{j+1}=u_j+\delta.
\]

The diagonal square cell in factor coordinates is

\[
C_{j,m}=[u_j,u_j+\delta]\times[u_j,u_j+\delta].
\]

Its Euclidean center is

\[
\boxed{
(c,c),
\qquad
c=u_j+\frac{\delta}{2}
=1+\frac{j+1/2}{m}.
}
\]

This is the precise local object behind the half-cell observation.

---

## 2. Exact cell-center tangent theorem

Paper A uses

\[
X=\frac{x-y}{2},
\qquad
Y=\sqrt{xy},
\qquad
T=\frac{x+y}{2}.
\]

At the diagonal cell center `(c,c)`,

\[
\boxed{X=0,\qquad Y=c,\qquad T=c.}
\]

The anti-diagonal through the center is

\[
x+y=2c,
\]

so its flat Cone section is the circle

\[
\boxed{X^2+Y^2=c^2.}
\]

The constant-product shell through the same point is

\[
xy=c^2,
\]

which in the flat `(X,Y)` projection is

\[
\boxed{Y=c.}
\]

The line `Y=c` is tangent to the circle `X^2+Y^2=c^2` exactly at

\[
\boxed{(X,Y)=(0,c).}
\]

Equivalently, in side view the shell

\[
T^2-X^2=c^2
\]

has vertex

\[
\boxed{(X,T)=(0,c).}
\]

**[D] Cell-center tangent theorem.** The center of every diagonal factor-grid cell maps exactly to the AM--GM tangent point of the shell

\[
\boxed{n=c^2}
\]

and to the apex of the anti-diagonal circle of radius `c`.

Thus the visually observed cell-centered tangent configuration is not accidental: it is forced by the Paper-A coordinate map for every mesh size.

---

## 3. The coarse cell center becomes a refined grid point

Because

\[
c=1+\frac{2j+1}{2m},
\]

the same center lies exactly on the doubled-resolution grid

\[
\Lambda_{2m}=1+\frac1{2m}\mathbb Z_{\ge0}.
\]

Therefore

\[
\boxed{
\text{center of an }m\text{-cell}
\quad\longrightarrow\quad
\text{exact diagonal grid point at resolution }2m.
}
\]

At the shell value

\[
\boxed{
n=c^2,
}
\]

the coarse `m`-grid sees an exact cell-center tangency, while the doubled `2m`-grid resolves that same tangency as an exact lattice vertex.

**[D] Center-refinement theorem.** Every coarse diagonal cell-center tangent is promoted to an exact diagonal grid tangent by doubling the resolution.

This gives an exact reason that half-integer tangencies appear naturally when the original integer grid is refined to halves.

---

## 4. The consecutive 5, 6, 7 cells

At the ordinary integer scale `m=1`, the diagonal cells `[5,6]^2` and `[6,7]^2` have centers

\[
\boxed{c=\frac{11}{2},\qquad c=\frac{13}{2}.}
\]

Their exact tangent shell values are

\[
\boxed{n=\frac{121}{4}=30.25,}
\]

and

\[
\boxed{n=\frac{169}{4}=42.25.}
\]

In Cone coordinates the tangent points are

\[
\boxed{(X,Y,T)=\left(0,\frac{11}{2},\frac{11}{2}\right),}
\]

and

\[
\boxed{(X,Y,T)=\left(0,\frac{13}{2},\frac{13}{2}\right).}
\]

At resolution `m=2` these centers are no longer merely cell centers: `11/2` and `13/2` are exact diagonal grid levels.

Thus the half-grid exactly resolves the coarse cell-center tangencies between 5 and 6 and between 6 and 7.

---

## 5. Thirds and arbitrary rational positions inside a cell

More generally, take a point at normalized fraction

\[
\theta=\frac pq,
\qquad 0\le p<q,
\]

inside an `m`-cell:

\[
c_{p/q}=u_j+\frac{p}{qm}.
\]

Then

\[
c_{p/q}
=1+\frac{qj+p}{qm},
\]

so it lies exactly on the `qm` refinement.

Its shell

\[
\boxed{n=c_{p/q}^2}
\]

is tangent at the diagonal point `(c_{p/q},c_{p/q})`.

Therefore

\[
\boxed{
\text{rational phase }\frac pq
\text{ at scale }m
\quad\longrightarrow\quad
\text{exact grid alignment at scale }qm.
}
\]

For thirds (`q=3`), the points one-third and two-thirds through an integer cell become exact on the `m=3` grid.

For example, between 5 and 6:

\[
\boxed{c=\frac{16}{3},\ \frac{17}{3}},
\]

with tangent shells

\[
\boxed{n=\frac{256}{9},\ \frac{289}{9}}.
\]

Between 6 and 7:

\[
\boxed{c=\frac{19}{3},\ \frac{20}{3}},
\]

with tangent shells

\[
\boxed{n=\frac{361}{9},\ \frac{400}{9}}.
\]

---

## 6. Tangent phase: the mod-1/m quantity that directly measures cell position

For a fixed shell `n>0`, let

\[
r=\sqrt n.
\]

The relevant diagonal tangent point is `(r,r)`.

On the anchored resolution-`m` grid define the tangent-cell index and normalized tangent phase by

\[
\boxed{
j_m(n)=\lfloor m(r-1)\rfloor,}
\]

\[
\boxed{
\theta_m(n)=\{m(r-1)\}.
}
\]

Then

\[
r
=1+\frac{j_m(n)+\theta_m(n)}{m}.
\]

Equivalently, the physical displacement from the lower diagonal grid level is

\[
\boxed{
r-\left(1+\frac{j_m}{m}\right)
=\frac{\theta_m(n)}{m}
=(r-1)\bmod\frac1m.
}
\]

This is distinct from the arm phase `phi={2mX}` introduced in v13.172--v13.173. It measures the position of the **tangent point itself** inside its diagonal cell.

**[D] Tangent-phase theorem.** The normalized mod-`1/m` phase

\[
\boxed{\theta_m(n)=\{m(\sqrt n-1)\}}
\]

is exactly the fractional position of the AM--GM tangent point across its diagonal grid cell.

---

## 7. Distinguished tangent phases

Exact tangent-grid alignment occurs iff

\[
\boxed{\theta_m(n)=0.}
\]

This gives

\[
m(\sqrt n-1)\in\mathbb Z,
\]

which is precisely the continuous tangent-entry condition from v13.173.

Exact cell-center tangency occurs iff

\[
\boxed{\theta_m(n)=\frac12.}
\]

Equivalently,

\[
\boxed{
\sqrt n
=1+\frac{j+1/2}{m}.
}
\]

At twice the resolution,

\[
2m(\sqrt n-1)=2j+1\in\mathbb Z,
\]

so

\[
\boxed{
\theta_m(n)=\frac12
\Longrightarrow
\theta_{2m}(n)=0.
}
\]

More generally, if

\[
\theta_m(n)=\frac pq
\]

in lowest terms, then

\[
\boxed{
\theta_{qm}(n)=0.
}
\]

This is the phase version of the rational refinement theorem in Section 5.

---

## 8. Continuous m turns tangent phase into a sawtooth flow

For fixed shell `n`,

\[
\theta_m(n)=\{m(\sqrt n-1)\}
\]

is a sawtooth function of real `m`.

Grid-alignment events occur at

\[
\boxed{
m_j^{\rm tan}=\frac{j}{\sqrt n-1},}
\]

and cell-center events occur halfway between them:

\[
\boxed{
m_j^{\rm center}=\frac{j+1/2}{\sqrt n-1}.}
\]

The spacing between consecutive exact alignment events is

\[
\boxed{\Delta m=\frac1{\sqrt n-1}.}
\]

Thus continuous resolution reveals an exact alternating sequence

\[
\boxed{
\text{grid tangent}
\to
\text{cell-center tangent}
\to
\text{grid tangent}
\to\cdots
}
\]

for every fixed shell.

---

## 9. Integer-resolution arithmetic dichotomy

If `sqrt(n)` is rational, then `sqrt(n)-1` is rational and the integer-resolution sequence

\[
\theta_m(n)=\{m(\sqrt n-1)\},
\qquad m\in\mathbb Z_{>0},
\]

is periodic. Some integer refinement aligns the tangent exactly.

If `n` is an integer nonsquare, then `sqrt(n)-1` is irrational. No integer `m` gives exact tangent alignment.

By the standard equidistribution theorem for irrational rotations, the sequence

\[
\boxed{
\{m(\sqrt n-1)\},
\qquad m=1,2,3,\ldots
}
\]

is equidistributed in `[0,1)`.

**[D, using the standard irrational-rotation theorem].** For nonsquare integer shells, arithmetic refinements never hit the tangent exactly but sample its intra-cell phase densely and uniformly in the long run.

For `n=11`,

\[
\boxed{
\theta_m(11)=\{m(\sqrt{11}-1)\}.
}
\]

So the integer refinement sequence approaches both grid alignment (`theta=0`) and cell-center phase (`theta=1/2`) arbitrarily closely, though neither is attained exactly at finite integer `m`.

---

## 10. Local relation to the last Paper-A gnomon

Let `r=sqrt(n)` and suppose the last active diagonal level below the tangent is

\[
u=r-\frac{\theta}{m},
\qquad
\theta=\theta_m(n)\in[0,1).
\]

The Paper-A continuous arm is

\[
g_n(u)=\frac{r^2}{u}-u.
\]

Substituting `u=r-theta/m` gives the exact terminal scaled arm

\[
\boxed{
 m g_n(u)
 =2\theta+\frac{\theta^2}{mr-\theta}.
}
\]

Hence near the tangent,

\[
\boxed{
 m g_n(u)=2\theta+O(m^{-1}).
}
\]

So the tangent-cell phase controls the terminal gnomon arm to first order.

In particular, at exact cell-center phase `theta=1/2`,

\[
\boxed{
 m g_n(u)
 =1+\frac{1}{4mr-2}
>1.
}
\]

This supplies an exact bridge between the newly isolated tangent phase and Paper A's floor-gnomon mechanism.

---

## 11. Synthesis

There are now two complementary modular phases attached to the same geometry:

\[
\boxed{
\theta_m(n)=\{m(\sqrt n-1)\}
}
\]

measures where the shell tangent lies inside its diagonal cell, while

\[
\boxed{
\phi_{n,j}(m)=\{2mX_{u_j}\}
}
\]

measures where a row/hyperbola crossing lies inside its gnomon arm cell.

The first controls the diagonal/tangent geometry; the second controls the floor count away from the diagonal.

Together they give a natural two-phase description of the refined Paper-A region:

\[
\boxed{
\text{tangent phase }\theta
\quad+\quad
\text{arm phase }\phi.
}
\]

**[I]** This appears to be the correct exact framework for testing whether the previously noticed local circles encode only diagonal cell-center tangency or a stronger relation tying tangent phase and arm phase together.

---

## Publication guardrails

1. The cell-center tangent theorem above is exact for diagonal square cells under Paper A's coordinate map.
2. Do not infer that every visually drawn small circle in a prior figure is this anti-diagonal circle unless its center/radius are matched explicitly.
3. Keep tangent phase `theta_m(n)={m(sqrt(n)-1)}` distinct from arm phase `phi={2mX}`.
4. Equidistribution applies to integer refinement indices when `sqrt(n)-1` is irrational; it does not mean any finite integer grid contains the irrational tangent point.
5. Rational intra-cell phase becoming exact on a denominator-multiplied refinement is an exact grid statement, not by itself evidence of additional number-theoretic structure.
