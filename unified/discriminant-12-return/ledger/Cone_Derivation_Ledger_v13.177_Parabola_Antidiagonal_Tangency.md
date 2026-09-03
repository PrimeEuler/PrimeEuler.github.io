# Cone Derivation Ledger v13.177 — Parabola / Anti-Diagonal Tangency and Half-Scale Circles

**Status:** Exact continuation of v13.176  
**Date:** 2026-09-03  
**Scope:** Exact tangency between Paper A row/column parabolas and fixed-`T` anti-diagonal circles; half-scale structure; relation to mod-`1/m` refinement.

## Audit convention

- **[D]** exact derived
- **[I]** interpretation
- **[O]** open
- **[Audit]** limitation / scope correction

---

## 1. Paper A row and column parabolas in the flat `(X,Y)` view

For a fixed factor level `u>0`, the row `y=u` gives

\[
T-X=u,
\qquad
Y^2=u(T+X).
\]

Eliminating `T` using `T=X+u` gives

\[
\boxed{Y^2=u^2+2uX.}
\]

Equivalently,

\[
\boxed{X=\frac{Y^2-u^2}{2u}.}
\]

This parabola opens toward positive `X` and has Euclidean vertex

\[
\boxed{V_u^- = \left(-\frac u2,0\right).}
\]

The mirror column `x=u` gives

\[
\boxed{Y^2=u^2-2uX,}
\]

with vertex

\[
\boxed{V_u^+ = \left(+\frac u2,0\right).}
\]

The diagonal point `(x,y)=(u,u)` maps instead to

\[
(X,Y,T)=(0,u,u),
\]

which is a point on each parabola, not its Euclidean vertex.

**[D]** The row/column parabola vertices lie on the `X` axis at half the factor level.

---

## 2. Fixed-`T` anti-diagonals are circles

Paper A's Cone coordinates satisfy

\[
X^2+Y^2=T^2.
\]

Thus fixing `T=t>0` gives the anti-diagonal circle

\[
\boxed{C_t:\ X^2+Y^2=t^2.}
\]

In factor coordinates, fixed `T=t` is the anti-diagonal

\[
x+y=2t.
\]

Therefore the circle radius in the flat `(X,Y)` view is exactly one-half the corresponding factor-space anti-diagonal sum.

---

## 3. Exact tangency theorem

Consider the row parabola

\[
P_u^-:\quad Y^2=u^2+2uX
\]

and the circle

\[
C_t:\quad X^2+Y^2=t^2.
\]

Substituting the parabola into the circle gives

\[
X^2+u^2+2uX=t^2,
\]

hence

\[
\boxed{(X+u)^2=t^2.}
\]

The two intersections are therefore algebraically constrained by

\[
X=-u\pm t.
\]

For tangency, the gradients must be parallel. Write

\[
F(X,Y)=Y^2-u^2-2uX,
\]

\[
G(X,Y)=X^2+Y^2-t^2.
\]

Then

\[
\nabla F=(-2u,2Y),
\qquad
\nabla G=(2X,2Y).
\]

Their determinant is

\[
\det(\nabla F,\nabla G)
=-4Y(X+u).
\]

At a real tangency either `Y=0` or `X=-u`. The second possibility gives `Y^2=-u^2`, hence no real point. Therefore tangency requires

\[
Y=0.
\]

On the row parabola this forces

\[
X=-\frac u2.
\]

The circle through that point has radius

\[
t=\frac u2.
\]

Hence

\[
\boxed{
P_u^-\text{ is tangent to }C_{u/2}
\text{ at }
\left(-\frac u2,0\right).
}
\]

By reflection,

\[
\boxed{
P_u^+\text{ is tangent to }C_{u/2}
\text{ at }
\left(+\frac u2,0\right).
}
\]

**[D] Parabola / anti-diagonal tangency theorem.** The mirror row and column parabolas at factor level `u` are both tangent to the same fixed-`T` circle of radius `u/2`, at the two antipodal points of that circle on the `X` axis.

---

## 4. Factor-coordinate meaning of the tangency

At the left tangency point

\[
(X,Y,T)=\left(-\frac u2,0,\frac u2\right),
\]

recover factor coordinates from

\[
x=T+X,
\qquad
y=T-X.
\]

Thus

\[
(x,y)=(0,u).
\]

At the right tangency point

\[
(X,Y,T)=\left(+\frac u2,0,\frac u2\right),
\]

we obtain

\[
(x,y)=(u,0).
\]

So the tangency circle is the fixed-sum anti-diagonal

\[
\boxed{x+y=u}
\]

and the parabola vertices are precisely the two axis endpoints of that anti-diagonal.

**[D]** The factor-level `u` parabola pair is tangent to the anti-diagonal circle whose factor-space sum equals that same `u`.

---

## 5. Why half-integers appear automatically

If `u` is an integer factor level, then the tangent circle has

\[
\boxed{T=\frac u2.}
\]

Hence integer factor levels generate the radius sequence

\[
\frac12,1,\frac32,2,\frac52,3,\ldots
\]

in the flat `(X,Y)` view.

For the consecutive levels `u=5,6,7`, the exact tangent-circle radii are

\[
\boxed{\frac52,3,\frac72.}
\]

Thus the visually prominent half-unit circle spacing is not an added modular rule. It is forced by the Cone coordinate

\[
T=\frac{x+y}{2}.
\]

**[D] Half-scale theorem.** Integer spacing in factor level becomes half-integer spacing in anti-diagonal circle radius.

---

## 6. General `1/m` refinement

For a refined factor level

\[
u=1+\frac jm
\]

or, on an origin-anchored arithmetic grid, simply

\[
u=\frac jm,
\]

the tangent circle has radius

\[
\boxed{T=\frac u2.}
\]

Therefore a `1/m` factor refinement induces a `1/(2m)` radius refinement in the fixed-`T` circle family.

For arithmetic levels `u=j/m`,

\[
\boxed{T=\frac{j}{2m}.}
\]

This gives an exact denominator-doubling relation:

\[
\boxed{
\text{factor mesh }\frac1m
\quad\Longrightarrow\quad
\text{circle-radius mesh }\frac1{2m}.
}
\]

At `m=1`, circle radii are half-integers. At `m=2`, circle radii lie on quarter-integers. At `m=3`, they lie on sixths.

**[D]** The earlier mod-`0.5` phenomenon has an independent exact geometric source: fixed-`T` circles are naturally half-scaled relative to factor levels.

---

## 7. Continuous resolution `m>0`

For the boundary-anchored continuous-resolution family

\[
u_j(m)=1+\frac jm,
\]

the corresponding tangent-circle radius is

\[
\boxed{
t_j(m)=\frac12+\frac{j}{2m}.
}
\]

Thus as real `m` varies continuously, the entire tangent-circle family moves continuously even though integer and rational values of `m` remain distinguished arithmetic slices.

The spacing between consecutive radii is exactly

\[
\boxed{\Delta t=\frac1{2m}.}
\]

So the continuous resolution flow acts linearly on these tangent circles.

---

## 8. Tangency is unique among fixed-`T` circles

For fixed `u`, the intersection equation

\[
(X+u)^2=t^2
\]

shows that the circle family `C_t` changes from no real contact near the parabola vertex to transverse intersection once `t>u/2`.

The minimum Euclidean distance from the origin to the row-parabola vertex is exactly

\[
\frac u2.
\]

Hence `C_{u/2}` is the unique origin-centered circle tangent to the row parabola at its vertex.

**[D]** There is no second positive-radius fixed-`T` circle tangent to the positive-`Y` branch of `P_u^-`; the only real tangency is the vertex contact at `Y=0`.

---

## 9. Relation to the shell tangent studied in v13.174--v13.176

There are now two distinct exact tangency mechanisms and they must not be conflated.

### Shell tangent

For a constant-product shell

\[
xy=n,
\]

the diagonal tangent occurs at

\[
(x,y)=(\sqrt n,\sqrt n),
\]

which maps to

\[
(X,Y,T)=(0,\sqrt n,\sqrt n).
\]

In the flat view, the line `Y=sqrt(n)` is tangent to the circle

\[
X^2+Y^2=n
\]

at its top point.

### Parabola / anti-diagonal tangent

For fixed factor level `u`, the row/column parabola vertices occur at

\[
(X,Y)=\left(\mp\frac u2,0\right)
\]

and are tangent to the circle

\[
X^2+Y^2=\frac{u^2}{4}.
\]

Thus one tangency lives at the **top** of a shell circle, while the other lives at the **left/right axis endpoints** of a half-scale anti-diagonal circle.

**[D]** Both arise from the same Cone equation `X^2+Y^2=T^2`, but they represent different sections of the factor geometry.

---

## 10. A four-point cross structure for each `u`

The factor level `u` produces four distinguished points in the flat Cone geometry:

\[
\left(-\frac u2,0\right),
\qquad
\left(+\frac u2,0\right),
\qquad
(0,u),
\qquad
(0,-u)
\]

if the full algebraic circle is considered.

The first two are the row/column parabola vertices on the circle of radius `u/2`. The point `(0,u)` is the diagonal factor point `(u,u)` and lies on the larger circle of radius `u` corresponding to `T=u`.

Therefore the same factor level naturally generates two circle scales:

\[
\boxed{T=\frac u2}
\]

at the parabola vertices, and

\[
\boxed{T=u}
\]

at the diagonal point.

Their ratio is exactly

\[
\boxed{2:1.}
\]

**[I]** This two-scale structure is a plausible source of the visually repeated nested-circle / half-cell patterns in Paper A figures.

---

## 11. Consecutive levels `5,6,7`

For `u=5`,

\[
P_5^\pm
\text{ are tangent to }
C_{5/2}.
\]

For `u=6`,

\[
P_6^\pm
\text{ are tangent to }
C_3.
\]

For `u=7`,

\[
P_7^\pm
\text{ are tangent to }
C_{7/2}.
\]

The three tangent circles are evenly spaced in radius by

\[
\boxed{\frac12.}
\]

Meanwhile the corresponding diagonal points lie at radii

\[
5,6,7.
\]

So the `5,6,7` geometry contains an exact nested pair of scales:

\[
\boxed{
2.5,3,3.5
\quad\leftrightarrow\quad
5,6,7.
}
\]

This is not a numerical coincidence; it is the exact map `T=u/2` at parabola vertices versus `T=u` at diagonal points.

---

## 12. Connection to mod `1/m`

The factor-to-circle map

\[
u\mapsto\frac u2
\]

means a factor-grid remainder modulo `1/m` becomes a circle-radius remainder modulo `1/(2m)`.

If

\[
u=q+\rho,
\qquad
0\le\rho<\frac1m,
\]

then

\[
\frac u2=\frac q2+\frac\rho2,
\qquad
0\le\frac\rho2<\frac1{2m}.
\]

Hence the half-scale circle family carries the same normalized phase but at doubled resolution.

Define the factor phase

\[
\psi_m(u)=\{mu\}.
\]

Then for the circle radius `t=u/2`,

\[
\boxed{\{2mt\}=\{mu\}=\psi_m(u).}
\]

**[D] Phase-preservation theorem.** The map from factor level to tangent-circle radius preserves normalized modular phase when the radius scale is measured at resolution `2m`.

---

## 13. What this resolves from the open cell-circle question

The phrase "small circles" can now be separated into at least two mathematically distinct candidates:

1. origin-centered fixed-`T` anti-diagonal circles `X^2+Y^2=T^2`;
2. genuinely cell-centered Euclidean circles with centers away from the origin.

For candidate (1), the tangency problem is now completely solved:

\[
\boxed{
T=\frac u2
}
\]

is the unique tangent circle to the level-`u` row/column parabola pair.

For candidate (2), no canonical center/radius law has yet been established from the source geometry alone.

**[Audit]** Do not identify a visually drawn cell-centered circle with the fixed-`T` circle unless its actual center is the Cone origin. The exact theorem above concerns anti-diagonal circles centered at `(X,Y)=(0,0)`.

---

## 14. New synthesis

We now have three exact scale laws:

\[
\boxed{\text{factor level }u}
\]

\[
\boxed{\downarrow}
\]

\[
\boxed{\text{parabola-vertex circle radius }u/2}
\]

and independently

\[
\boxed{\text{diagonal point radius }u.}
\]

Together with the terminal-shell phase work,

\[
\boxed{
\text{factor mesh }1/m
\to
\text{anti-diagonal radius mesh }1/(2m)
\to
\text{phase-preserving half-scale geometry}.
}
\]

This gives an exact geometric origin for the recurring factor `1/2` that is separate from, but compatible with, the mod-`0.5` floor refinement.

---

## 15. Next exact problem

**[O]** Compare the exact origin-centered tangent circles `C_{u/2}` with the specific small circles visible in the Paper A figure. If the drawn centers are not the Cone origin, reconstruct their centers/radii directly from the figure-generation code or source geometry and test whether they are:

- translated copies of `C_{u/2}`;
- incircles of factor-grid cells;
- osculating circles of the row parabolas;
- or independent decorative/auxiliary circles.

Only after that source-level identification should any stronger claim about "cell-centered tangent circles" be made.
