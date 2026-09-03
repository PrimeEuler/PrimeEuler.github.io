# Cone Derivation Ledger v13.170 — Rational Refinement and Continuous Completion of Divisor Shells

**Status:** Audited extension of v13.169  
**Date:** 2026-09-03  
**Scope:** Fractional-lattice divisor shells, tangent points, rational completion, and the logarithmic/rapidity parameterization.

## Audit convention

- **[S]** source-established
- **[D]** exact derived
- **[N-cert]** rigorous finite numerical/computer-assisted
- **[I]** interpretation
- **[O]** open
- **[Audit]** correction / limitation

---

## 1. Fractional-grid divisor shells

Fix `n>0` and a positive integer `m`. Define the `1/m`-grid divisor shell

\[
\mathcal D_m(n)
=
\left\{(x,y)\in\left(\frac1m\mathbb Z_{>0}\right)^2:xy=n\right\}.
\]

Write

\[
x=\frac a m,\qquad y=\frac b m,
\qquad a,b\in\mathbb Z_{>0}.
\]

Then

\[
xy=n
\iff
\frac{ab}{m^2}=n
\iff
\boxed{ab=nm^2}.
\]

Therefore, whenever `nm^2` is an integer,

\[
\boxed{
\mathcal D_m(n)
=
\left\{
\left(\frac a m,\frac b m\right):ab=nm^2
\right\}.
}
\]

**[D] Fractional-grid divisor theorem.** A divisor point on a `1/m` lattice is exactly an ordinary integer factor pair of the dilated integer `nm^2`, rescaled by `1/m`.

If ordered factor pairs are counted, then

\[
\boxed{|\mathcal D_m(n)|=d(nm^2)}
\]

for integral `nm^2`.

Examples:

\[
m=2:\qquad ab=4n,
\]

\[
m=3:\qquad ab=9n.
\]

Thus half-integer and third-integer divisor points are not ad hoc constructions; they are exact rescalings of ordinary factorization problems.

---

## 2. Compatibility with the Cone coordinates

Use Paper A's coordinates

\[
X=\frac{x-y}{2},\qquad
Y=\sqrt{xy},\qquad
T=\frac{x+y}{2}.
\]

For a point `(a/m,b/m)` on `\mathcal D_m(n)`,

\[
X=\frac{a-b}{2m},
\qquad
Y=\frac{\sqrt{ab}}m=\sqrt n,
\qquad
T=\frac{a+b}{2m}.
\]

Hence every refinement level satisfies the same shell equations

\[
\boxed{X^2+Y^2=T^2},
\]

\[
\boxed{Y^2=n},
\]

and

\[
\boxed{T^2-X^2=n}.
\]

**[D]** Refining the lattice changes only the discrete sampling of the shell; it does not change the underlying Cone section.

---

## 3. Nested refinements

If `m|M`, then

\[
\frac1m\mathbb Z\subset\frac1M\mathbb Z,
\]

so

\[
\boxed{\mathcal D_m(n)\subseteq\mathcal D_M(n)}.
\]

A convenient nested sequence is

\[
1,\ 2,\ 6,\ 24,\ldots,
\]

or generally `m_j=j!`, because every earlier grid is contained in every later one.

**[Audit]** The grids `1/2,1/3,1/4,...` are not pairwise nested unless the denominators divide one another. The correct global object is their union, or a divisibility-nested subsequence such as factorial denominators.

---

## 4. New points introduced at a refinement level

Let `E_m(n)` denote the number of points whose **minimal common grid denominator** is exactly `m`.

Since every point in `\mathcal D_m(n)` has a unique minimal denominator dividing `m`,

\[
|\mathcal D_m(n)|
=
\sum_{d\mid m}E_d(n).
\]

By Möbius inversion,

\[
\boxed{
E_m(n)=
\sum_{d\mid m}
\mu\!\left(\frac md\right)
 d(nd^2)
}
\]

whenever the displayed divisor counts are defined integrally.

For a prime refinement `p`,

\[
\boxed{E_p(n)=d(np^2)-d(n)}.
\]

If `p\nmid n`, then

\[
d(np^2)=3d(n),
\]

and therefore

\[
\boxed{E_p(n)=2d(n)}.
\]

**[D]** This gives an exact arithmetic measure of how many genuinely new shell points appear when passing to a prime-denominator refinement.

---

## 5. Rational completion

Define

\[
\mathcal D_{\mathbb Q}(n)
=
\bigcup_{m\ge1}\mathcal D_m(n).
\]

For rational `n>0`, this is precisely

\[
\boxed{
\mathcal D_{\mathbb Q}(n)
=
\{(x,y)\in\mathbb Q_{>0}^2:xy=n\}.
}
\]

Indeed, if `(x,y)` is a positive rational factor pair, choosing a common denominator `m` puts both coordinates in `(1/m)Z`.

Because positive rationals are dense in positive reals and the map

\[
x\longmapsto\frac nx
\]

is continuous on `(0,\infty)`,

\[
\boxed{
\overline{\mathcal D_{\mathbb Q}(n)}
=
\{(x,y)\in\mathbb R_{>0}^2:xy=n\}.
}
\]

**[D] Rational-completion theorem.** For rational `n>0`, the ordinary divisor shell admits a canonical dense rational refinement whose closure is the full positive real hyperbola.

**[Audit]** The usual divisor function `d(n)` does not extend as a finite counting function on the real shell; the real shell has uncountably many factor pairs. The surviving object is the geometry, not the finite arithmetic count.

---

## 6. Tangent-circle / vertex theorem

On the shell

\[
T^2-X^2=n,
\]

the minimum value of `T` occurs at

\[
X=0,
\qquad
T=\sqrt n.
\]

In the original factor variables this is

\[
x=y=\sqrt n.
\]

In the flat `(X,Y)` projection, the constant-product line

\[
Y=\sqrt n
\]

is tangent to the circle

\[
X^2+Y^2=n
\]

at

\[
\boxed{(X,Y)=(0,\sqrt n)}.
\]

Equivalently, the side-view hyperbola has vertex

\[
\boxed{(X,T)=(0,\sqrt n)}.
\]

**[D] Tangent-circle theorem.** The AM-GM equality point `x=y=sqrt(n)` is exactly the tangency point of the constant-product section with the smallest anti-diagonal circle that meets that shell.

---

## 7. When does the tangent point lie on a fractional lattice?

The tangent point lies on the `1/m` factor lattice exactly when

\[
\sqrt n\in\frac1m\mathbb Z,
\]

or equivalently

\[
\boxed{m\sqrt n\in\mathbb Z}.
\]

Equivalently,

\[
\boxed{nm^2\text{ is a perfect square integer}.}
\]

Thus:

- integer-grid tangent shells are `n=s^2` with `s\in Z_{>0}`;
- half-grid tangent shells are `n=(a/2)^2`;
- third-grid tangent shells are `n=(a/3)^2`;
- the union over all rational grids gives all positive **rational-square** shell values.

**[D]** A centered fractional-grid divisor point exists exactly for rational-square shell values.

For integer nonsquare `n`, `sqrt(n)` is irrational, so no rational refinement ever contains the exact tangent point. Nevertheless the rational shell points approach it arbitrarily closely.

---

## 8. Dense tangent-shell values

The set

\[
\{r^2:r\in\mathbb Q_{>0}\}
\]

of positive rational squares is dense in `R_{>0}` because `Q_{>0}` is dense and the squaring map is continuous and strictly monotone there.

Therefore the fractional-grid tangent shells themselves are dense among all positive real shells:

\[
\boxed{
\overline{\{(a/m)^2:a,m\in\mathbb Z_{>0}\}}
=
\mathbb R_{>0}.
}
\]

**[D]** Half-integer, third-integer, and higher-denominator tangent constructions form a systematic approximation to the tangent geometry of every positive real shell.

**[I]** This is the precise sense in which the observed half-integer tangent-circle construction extends toward all real shell values: exact centered grid points occur on rational-square shells, while arbitrary real shells appear in the closure.

---

## 9. Hyperbolic rapidity parameterization

Parameterize the positive real shell `xy=n` by

\[
\boxed{x=\sqrt n\,e^u,\qquad y=\sqrt n\,e^{-u}}.
\]

Then

\[
X=\frac{x-y}{2}=\sqrt n\,\sinh u,
\]

\[
T=\frac{x+y}{2}=\sqrt n\,\cosh u,
\]

so

\[
\boxed{T^2-X^2=n}
\]

is the standard Lorentz hyperbola and `u` is its rapidity coordinate.

The factor exchange `x<->y` becomes

\[
\boxed{u\mapsto-u}.
\]

The tangent point `x=y=sqrt(n)` is exactly

\[
\boxed{u=0}.
\]

**[D]** The divisor shell therefore carries a canonical real additive coordinate `u` after continuous completion.

---

## 10. Logarithm as rapidity length

From

\[
x=\sqrt n\,e^u,
\]

we have

\[
\boxed{du=\frac{dx}{x}}.
\]

The segment of the shell with factor coordinate `1<=x<=n` corresponds to

\[
-\frac12\log n\le u\le\frac12\log n.
\]

Its rapidity width is therefore

\[
\boxed{\Delta u=\log n}.
\]

Hence the classical hyperbolic area term

\[
\int_1^n\frac n{x}\,dx
=n\log n
\]

can be written as

\[
\boxed{n\log n=n\,\Delta u}.
\]

**[D]** The `n log n` term is exactly `n` times the rapidity length of the symmetric factor interval from `(1,n)` to `(n,1)` on the continuous divisor shell.

This gives the previously observed hierarchy

\[
n\log n\longrightarrow nH_n\longrightarrow D(n)
\]

a sharper geometric interpretation:

- `n log n`: continuous rapidity-area term;
- `nH_n`: discrete sampling of the continuous reciprocal profile;
- `D(n)`: integer-lattice quantization obtained by flooring.

**[I]** This rapidity reading may be useful in comparing Paper A's divisor geometry with the project's independent Lorentz/Pell structures, but no arithmetic equivalence follows from the shared hyperbolic coordinate alone.

---

## 11. Relation to the n=11 shell

For `n=11`, the real shell has tangent/vertex point

\[
\boxed{x=y=\sqrt{11}},
\]

or

\[
\boxed{(X,Y,T)=(0,\sqrt{11},\sqrt{11})}.
\]

Because `sqrt(11)` is irrational, this central tangent point is not present on any rational `1/m` lattice.

However the integer factor endpoints

\[
(1,11),\qquad(11,1)
\]

occur at rapidities

\[
\boxed{u=\mp\tfrac12\log11},
\]

with

\[
(X,T)=(\mp5,6).
\]

Thus the `n=11` divisor shell spans the symmetric rapidity interval

\[
\boxed{[-\tfrac12\log11,\,+\tfrac12\log11]}.
\]

Its total rapidity width is exactly `log 11`.

---

## 12. Research consequences and open directions

### [D] Established

1. Fractional divisor points at denominator `m` are rescaled factors of `nm^2`.
2. Divisibility-nested denominators produce nested finite shell samplings.
3. The union over all denominators equals the rational factor shell for rational `n`.
4. The rational factor shell is dense in the positive real hyperbola.
5. The tangent point is `(sqrt(n),sqrt(n))` and lies on a `1/m` grid iff `m sqrt(n)` is integral.
6. Rational-square tangent shells are dense in all positive real shell values.
7. The continuous shell has Lorentz rapidity coordinate `u`, with `x=sqrt(n)e^u`, `y=sqrt(n)e^{-u}`.
8. `log n` is the rapidity width between the extreme factor points `(1,n)` and `(n,1)`.

### [O] To investigate

1. Whether the user's observed cell-centered tangent-circle patterns admit a canonical Voronoi/cell decomposition for general `1/m` grids.
2. Whether a normalized counting measure on `\mathcal D_m(n)` converges to a natural measure on the real shell under a carefully chosen refinement sequence.
3. Whether rapidity spacing, rather than Euclidean spacing, gives the natural normalization for such a limit.
4. Whether the correction `nH_n-D(n)=sum {n/k}` has a clean geometric interpretation as cumulative sub-cell displacement in the refined Cone picture.
5. Whether the half-integral phenomena here interact canonically with the independent dyadic/cyclotomic gluing already present in the discriminant-12 work.

---

## Publication guardrails added in v13.170

1. Do not redefine the classical divisor function on `R` as a finite count; the real shell has uncountably many factor pairs.
2. Do not call arbitrary real factor pairs ordinary integer divisors. Use terms such as **real factor pair**, **fractional-grid divisor point**, or **rational shell point**.
3. Do not claim the `1/m` grids are nested unless the denominators divide one another.
4. Exact grid-centered tangency occurs only when `m sqrt(n)` is integral; for integer nonsquares such as 11, rational refinements only approximate the central tangent point.
5. The rapidity parameterization is an exact geometric bridge to Lorentz form, not an arithmetic identification with the discriminant-12 Pell lattice.
6. Any limiting measure obtained from refined divisor counts requires normalization and must be proved separately.
