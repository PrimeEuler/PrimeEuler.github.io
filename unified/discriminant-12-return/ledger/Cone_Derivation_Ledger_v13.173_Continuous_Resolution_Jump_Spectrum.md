# Cone Derivation Ledger v13.173 — Continuous-Resolution Jump Spectrum

**Status:** Exact continuation of v13.172  
**Date:** 2026-09-03  
**Scope:** Continuous resolution `m>0`, explicit jump locations, monotonicity, tangent-entry events, and the `n=11` phase portrait.

## Audit convention

- **[D]** exact derived
- **[I]** interpretation
- **[O]** open
- **[Audit]** limitation / scope correction

---

## 1. Continuous-resolution Paper-A lattice

For real resolution parameter `m>0`, use the anchored lattice

\[
\Lambda_m=1+\frac1m\mathbb Z_{\ge0},
\]

so the Paper-A boundary `x=y=1` remains fixed while the cell width `1/m` varies continuously.

For the `j`-th diagonal level,

\[
\boxed{u_j(m)=1+\frac jm},\qquad j=0,1,2,\ldots
\]

and it is active while

\[
u_j(m)\le \sqrt n.
\]

Equivalently,

\[
0\le j\le \lfloor m(\sqrt n-1)\rfloor.
\]

The one-sided continuous gnomon arm is

\[
g_n(u)=\frac nu-u,
\]

and its resolution-scaled length is

\[
\boxed{A_{n,j}(m)=m\,g_n(u_j(m)).}
\]

Using `u_j=(m+j)/m`, this simplifies to

\[
\boxed{
A_{n,j}(m)=\frac{nm^2}{m+j}-(m+j).
}
\]

The continuous-resolution count is therefore

\[
\boxed{
\mathscr D_n(m)=
\sum_{j=0}^{\lfloor m(\sqrt n-1)\rfloor}
\left(2\lfloor A_{n,j}(m)\rfloor+1\right).
}
\]

At integer `m`, this agrees with the exact `1/m` fractional-grid count from v13.171. For noninteger `m`, `m` is a resolution parameter rather than an arithmetic denominator.

---

## 2. Exact modular phase

Define

\[
\boxed{
\phi_{n,j}(m)=\{A_{n,j}(m)\}
}
\]

so that

\[
A_{n,j}(m)=\lfloor A_{n,j}(m)\rfloor+\phi_{n,j}(m).
\]

Because the physical cell width is `1/m`, the unresolved physical arm displacement is

\[
\boxed{
R_{n,j}(m)=\frac{\phi_{n,j}(m)}{m}
=g_n(u_j)\bmod\frac1m.
}
\]

Since `g_n(u)=2X_u`, equivalently

\[
\boxed{
\phi_{n,j}(m)=\{2mX_{u_j}\}.
}
\]

Thus all mod-`1/m` refinements are slices of one normalized phase variable in `[0,1)`.

---

## 3. Exact arm-jump spectrum

For a fixed active level `j`, a symmetric pair of new arm points appears whenever

\[
A_{n,j}(m)=k,
\qquad k\in\mathbb Z_{\ge0}.
\]

Substitute the exact formula:

\[
\frac{nm^2}{m+j}-(m+j)=k.
\]

After clearing the denominator,

\[
(n-1)m^2-(2j+k)m-j(j+k)=0.
\]

The positive solution is

\[
\boxed{
 m_{j,k}
 =
 \frac{2j+k+\sqrt{k^2+4n j(j+k)}}{2(n-1)}.
}
\]

**[D] Jump-spectrum theorem.** Every floor jump of every continuously refined Paper-A gnomon occurs at an explicitly solvable algebraic resolution `m_{j,k}`. Crossing such a value increases that gnomon's contribution by `2`, corresponding to the mirror pair of arm points.

For `j=0`,

\[
A_{n,0}(m)=(n-1)m,
\]

so the jump sequence reduces to

\[
\boxed{m_{0,k}=\frac{k}{n-1}}.
\]

---

## 4. Tangent-entry spectrum

A new diagonal level `j` enters the sum exactly when

\[
u_j(m)=\sqrt n.
\]

Thus

\[
1+\frac jm=\sqrt n,
\]

and therefore

\[
\boxed{
 m_j^{\rm tan}=\frac{j}{\sqrt n-1}
 =\frac{j(\sqrt n+1)}{n-1}.
}
\]

At this resolution,

\[
g_n(u_j)=g_n(\sqrt n)=0,
\]

so

\[
A_{n,j}(m_j^{\rm tan})=0.
\]

The newly appearing gnomon therefore contributes exactly its single diagonal vertex:

\[
\boxed{2\lfloor0\rfloor+1=1.}
\]

**[D] Tangent-entry theorem.** Under continuous resolution, new diagonal levels are born exactly at the shell tangent point, one point at a time, at the resolutions `m_j^{tan}`.

This gives the tangent point a third exact interpretation: it is not only the AM--GM vertex and the zero-length endpoint of the gnomon profile, but also the birth location of each new gnomon under continuous resolution flow.

---

## 5. Integer arithmetic slices versus real tangent-entry slices

If `n` is an integer nonsquare, `sqrt(n)` is irrational. Then every

\[
m_j^{\rm tan}=\frac{j}{\sqrt n-1}
\]

is irrational for `j>0`.

Therefore no integer-resolution slice lands exactly on these tangent-entry events.

This is fully consistent with v13.170: for integer denominator `m`, exact centered tangency requires `m sqrt(n)` integral, impossible for nonsquare integer `n`.

**[D]** Continuous resolution does not contradict the rational-grid tangent criterion. Instead it fills the gaps between arithmetic slices and exposes an infinite sequence of exact tangent-entry resolutions that are generally non-arithmetic.

---

## 6. Monotonicity of each active arm count

For fixed `j`, differentiate

\[
A_{n,j}(m)=\frac{nm^2}{m+j}-(m+j).
\]

Then

\[
A'_{n,j}(m)
=
 n\frac{m(m+2j)}{(m+j)^2}-1.
\]

Let

\[
q=1+\frac jm=u_j(m).
\]

On the active range `1<=q<=sqrt(n)`, this becomes

\[
A'_{n,j}(m)
=
 n\frac{2q-1}{q^2}-1
=
\frac{-q^2+2nq-n}{q^2}.
\]

For `n>1`, the numerator is positive on `1<=q<=sqrt(n)`. Hence

\[
\boxed{A'_{n,j}(m)>0}
\]

throughout the active life of the level.

Thus each existing floor count is nondecreasing with `m`, and each newly born level enters with contribution `+1`.

Therefore

\[
\boxed{\mathscr D_n(m)\text{ is nondecreasing for }m>0.}
\]

**[D] Monotone staircase theorem.** The continuous-resolution divisor count is an integer-valued monotone staircase. Its jumps are the union of:

1. tangent-entry jumps of size `1` at `m_j^{tan}`;
2. symmetric arm-pair jumps of size `2` at `m_{j,k}`;
3. larger jumps only when several exact events coincide.

---

## 7. The `n=11` tangent-entry spectrum

For `n=11`,

\[
\boxed{
 m_j^{\rm tan}
 =\frac{j}{\sqrt{11}-1}
 =\frac{j(\sqrt{11}+1)}{10}.
}
\]

Numerically,

\[
\frac{1}{\sqrt{11}-1}\approx0.43166248.
\]

So tangent-entry events occur at approximately

\[
0.43166j,
\qquad j=1,2,3,\ldots
\]

and none occur at an integer resolution.

At `m=2`, the active levels are

\[
\boxed{u=1,\frac32,2,\frac52,3.}
\]

Their scaled arm lengths are exactly

\[
\boxed{
20,
\frac{35}{3},
7,
\frac{19}{5},
\frac43
}
\]

with normalized phases

\[
\boxed{
0,
\frac23,
0,
\frac45,
\frac13.
}
\]

Thus the half-grid slice contains exact arm alignments at `u=1` and `u=2`, but the other active levels occupy nonzero intra-cell phases.

At `m=3`, the active levels are

\[
\boxed{
1,\frac43,\frac53,2,\frac73,\frac83,3
}
\]

with scaled arm lengths

\[
\boxed{
30,
\frac{83}{4},
\frac{74}{5},
\frac{21}{2},
\frac{50}{7},
\frac{35}{8},
2
}
\]

and phases

\[
\boxed{
0,
\frac34,
\frac45,
\frac12,
\frac17,
\frac38,
0.
}
\]

The corresponding total counts are

\[
\boxed{\mathscr D_{11}(1)=29,}
\]

\[
\boxed{\mathscr D_{11}(2)=89,}
\]

\[
\boxed{\mathscr D_{11}(3)=181.}
\]

These are counts on progressively finer anchored lattices in the same bounded Paper-A region; they should not be compared as ordinary divisor counts without the `m^2` normalization.

---

## 8. What the half-grid does and does not establish

At `m=2`, the exact phases show that the half-grid does have multiple exact arm-boundary alignments, but there is not yet evidence that `m=2` is uniquely selected by the local cell-centered tangent-circle geometry.

In particular, the phase pattern is not uniformly `0`, `1/2`, or any other single distinguished phase.

**[Audit]** Do not infer the observed half-grid circle tangencies solely from the modular phase data. The modular flow precisely locates gnomon arm alignment, while the local circle construction still requires an independent algebraic tangency calculation.

---

## 9. New structural picture

The continuously refined Paper-A count can now be viewed as a one-parameter flow:

\[
\boxed{
 m\in\mathbb R_{>0}
 \longmapsto
 \mathscr D_n(m).
}
\]

The underlying hyperbola, parabolas, Cone coordinates, and continuous arm profile remain fixed. Only the sampling resolution changes.

The exact event structure is:

\[
\boxed{
\text{tangent birth}
\quad\to\quad
\text{phase flow }\{2mX\}
\quad\to\quad
\text{pairwise arm jumps}.
}
\]

The integer values of `m` are distinguished arithmetic slices. The noninteger values interpolate the geometry and reveal the complete jump spectrum between those arithmetic slices.

---

## 10. Next exact problem

**[O]** Overlay the local cell-centered circle construction on the continuous-resolution flow. For each observed circle, identify its center and radius in `(x,y)` and `(X,Y,T)` coordinates, then test whether tangency occurs at:

- a tangent-entry resolution `m_j^{tan}`;
- an arm-alignment resolution `m_{j,k}`;
- a distinguished modular phase `phi=1/2` or another rational phase;
- or an independent geometric condition.

This calculation should be done before assigning arithmetic significance to the visually special half-grid case.
