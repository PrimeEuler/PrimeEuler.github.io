# Cone Derivation Ledger v13.170 — Rational Refinement and Continuous Completion of Divisor Shells

**Status:** Audited extension of v13.169; notation corrected after comparison with Paper A  
**Date:** 2026-09-03  
**Scope:** Fractional-lattice divisor shells, tangent points, rational completion, and rapidity parameterization.

## Audit convention

- **[S]** source-established
- **[D]** exact derived
- **[N-cert]** rigorous finite numerical/computer-assisted
- **[I]** interpretation
- **[O]** open
- **[Audit]** correction / limitation

---

## 1. Fractional-grid divisor shells

For `n>0` and positive integer `m`, define

\[
\mathcal D_m(n)=\left\{(x,y)\in\left(\frac1m\mathbb Z_{>0}\right)^2:xy=n\right\}.
\]

Writing `x=a/m`, `y=b/m` gives

\[
xy=n\iff ab=nm^2.
\]

Hence, whenever `nm^2` is integral,

\[
\boxed{\mathcal D_m(n)=\left\{\left(\frac am,\frac bm\right):ab=nm^2\right\}},
\]

and for ordered factor pairs

\[
\boxed{|\mathcal D_m(n)|=d(nm^2)}.
\]

**[D] Fractional-grid divisor theorem.** Fractional-grid shell points are exactly ordinary factor pairs of the dilated integer `nm^2`, rescaled by `1/m`.

---

## 2. Compatibility with Paper A coordinates

Paper A uses

\[
X=\frac{x-y}{2},\qquad Y=\sqrt{xy},\qquad T=\frac{x+y}{2}.
\]

For `(a/m,b/m)\in\mathcal D_m(n)`,

\[
X=\frac{a-b}{2m},\qquad Y=\sqrt n,\qquad T=\frac{a+b}{2m}.
\]

Thus every refinement level lies on the same exact section

\[
\boxed{X^2+Y^2=T^2},\qquad
\boxed{Y^2=n},\qquad
\boxed{T^2-X^2=n}.
\]

**[D]** Refinement changes the sampling lattice, not the underlying cone or hyperbola.

---

## 3. Nested refinements

If `m|M`, then

\[
\frac1m\mathbb Z\subset\frac1M\mathbb Z,
\qquad
\mathcal D_m(n)\subseteq\mathcal D_M(n).
\]

A convenient nested sequence is `m_j=j!`.

**[Audit]** The sequence of grids `1/2,1/3,1/4,...` is not pairwise nested. Use their union, or a divisibility-nested subsequence.

---

## 4. New shell points at a refinement level

Let `E_m(n)` be the number of shell points whose minimal common denominator is exactly `m`. Then

\[
|\mathcal D_m(n)|=\sum_{d\mid m}E_d(n),
\]

so Möbius inversion gives

\[
\boxed{E_m(n)=\sum_{d\mid m}\mu\!\left(\frac md\right)d(nd^2)}.
\]

For prime `p`,

\[
E_p(n)=d(np^2)-d(n).
\]

If `p\nmid n`, this reduces to

\[
\boxed{E_p(n)=2d(n)}.
\]

---

## 5. Rational completion

Define

\[
\mathcal D_{\mathbb Q}(n)=\bigcup_{m\ge1}\mathcal D_m(n).
\]

For rational `n>0`,

\[
\boxed{\mathcal D_{\mathbb Q}(n)=\{(x,y)\in\mathbb Q_{>0}^2:xy=n\}}.
\]

Since `Q_{>0}` is dense in `R_{>0}` and `x\mapsto n/x` is continuous,

\[
\boxed{\overline{\mathcal D_{\mathbb Q}(n)}=\{(x,y)\in\mathbb R_{>0}^2:xy=n\}}.
\]

**[D] Rational-completion theorem.** The rational shell points are dense in the positive real factor hyperbola.

**[Audit]** This does not extend the classical divisor function as a finite real-valued count. The full real shell contains uncountably many factor pairs.

---

## 6. Tangent-circle / vertex theorem

On

\[
T^2-X^2=n,
\]

the minimum `T` occurs at

\[
X=0,\qquad T=\sqrt n,
\]

corresponding to

\[
x=y=\sqrt n.
\]

In the flat `(X,Y)` projection, the constant-product line

\[
Y=\sqrt n
\]

is tangent to

\[
X^2+Y^2=n
\]

at

\[
\boxed{(X,Y)=(0,\sqrt n)}.
\]

**[D]** The AM-GM equality point is exactly the tangent point of the constant-product section with the smallest anti-diagonal circle meeting that shell.

---

## 7. Fractional-grid tangent criterion

The tangent point belongs to the `1/m` factor lattice iff

\[
\boxed{m\sqrt n\in\mathbb Z},
\]

equivalently iff `nm^2` is a perfect square integer.

Thus exact centered grid tangencies occur at positive rational-square shell values

\[
\boxed{n=(a/m)^2}.
\]

Since positive rational squares are dense in `R_{>0}`, these exact fractional-grid tangent shells are dense among all positive real shells.

For integer nonsquare `n`, including `n=11`, no rational grid contains the exact central tangent point, although rational shell points approach it arbitrarily closely.

---

## 8. Notation correction: Paper A keeps `u`

**[Audit — notation correction.]** Paper A already uses `u` as the diagonal/gnomon/parabola level in its divisor-summatory construction. That notation has priority throughout the project.

Paper A Section 5 anchors each nested gnomon at

\[
\boxed{(u,u)},\qquad 1\le u\le\lfloor\sqrt n\rfloor,
\]

with a row-parabola arm terminating at the constant-product hyperbola. Its one-sided continuous arm length is

\[
\boxed{\frac nu-u=\frac{n-u^2}{u}},
\]

and its exact lattice count is

\[
\boxed{\left\lfloor\frac{n-u^2}{u}\right\rfloor}.
\]

Accordingly, the logarithmic Lorentz parameter introduced in the first version of this ledger is renamed from `u` to

\[
\boxed{s}.
\]

Do not identify Paper A's `u` numerically with rapidity `s`.

---

## 9. Hyperbolic rapidity parameterization

Parameterize the positive real shell `xy=n` by

\[
\boxed{x=\sqrt n\,e^s,\qquad y=\sqrt n\,e^{-s}}.
\]

Then

\[
X=\sqrt n\,\sinh s,
\qquad
T=\sqrt n\,\cosh s,
\]

so

\[
T^2-X^2=n.
\]

Factor exchange becomes

\[
\boxed{s\mapsto-s},
\]

and the tangent point is `s=0`.

**[D]** The completed real divisor shell carries a canonical additive rapidity coordinate `s`.

---

## 10. Logarithm as rapidity width

From

\[
x=\sqrt n\,e^s
\]

we have

\[
\boxed{ds=\frac{dx}{x}}.
\]

The shell segment from `(1,n)` to `(n,1)` spans

\[
-\frac12\log n\le s\le\frac12\log n,
\]

so

\[
\boxed{\Delta s=\log n}.
\]

Therefore

\[
\int_1^n\frac n{x}\,dx=n\log n=n\,\Delta s.
\]

**[D]** `n log n` is `n` times the rapidity width of the symmetric continuous factor interval.

**[Audit]** This rapidity variable `s` is distinct from Paper A's gnomon variable `u`. Their relation depends on which point of the shell/row geometry is being parameterized and must be stated explicitly when used.

---

## 11. The n=11 shell

For `n=11`, the real tangent point is

\[
(x,y)=(\sqrt{11},\sqrt{11}),
\qquad
(X,Y,T)=(0,\sqrt{11},\sqrt{11}).
\]

The integer factor endpoints `(1,11)` and `(11,1)` occur at

\[
\boxed{s=\mp\tfrac12\log11},
\]

with

\[
(X,T)=(\mp5,6).
\]

Thus the 11-shell has rapidity interval

\[
\boxed{[-\tfrac12\log11,+\tfrac12\log11]}.
\]

---

## 12. Research consequences and next step

### [D] Established

1. `1/m` shell points are rescaled integer factors of `nm^2`.
2. Rational shell points are dense in the real factor hyperbola.
3. Exact centered tangency on a `1/m` grid occurs iff `m sqrt(n)` is integral.
4. Rational-square tangent shells are dense in positive real shell values.
5. Paper A's `u` is the diagonal vertex / row-parabola / gnomon level.
6. Paper A's one-sided gnomon profile is exactly `(n-u^2)/u=n/u-u`.
7. Rapidity is denoted `s`, not `u`, with `x=sqrt(n)e^s`, `y=sqrt(n)e^{-s}`.
8. `log n` is the rapidity width of the complete continuous factor interval.

### [O] Immediate continuation

Refine Paper A's own nested-gnomon count on a `1/m` lattice and determine its exact continuum limit before introducing any independent measure on the shell. This is carried out in ledger v13.171.

---

## Publication guardrails

1. Reserve `u` for Paper A's established diagonal/gnomon/parabola parameter.
2. Use `s` for Lorentz rapidity.
3. Do not identify real factor pairs with classical integer divisors.
4. Do not claim all denominator grids are nested.
5. Do not infer arithmetic equivalence with the discriminant-12 Pell lattice from the shared Lorentz form.
6. Any normalized limiting count must be derived from an explicitly stated refined region and lattice.
