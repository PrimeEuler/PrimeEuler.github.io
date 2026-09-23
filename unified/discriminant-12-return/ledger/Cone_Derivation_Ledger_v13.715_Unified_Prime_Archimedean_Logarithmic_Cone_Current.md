# Cone Derivation Ledger v13.715 — Unified Prime–Archimedean Logarithmic Cone Current

Date: 2026-09-23

Status: exact Xi/Zeta cone-lane continuation following v13.713 and its independent audit v13.714.

Status labels: **[D]** exact derived, **[O]** open, **[G]** guardrail.

## 0. Synchronization and collision check

Immediately before this write, the live repository head was v13.714 / External Audit Round 83 at commit \`fe622918957ec41a1f3871179db211bace361051\`. The intended v13.715 filename was absent. No collision was present.

The audit v13.714 independently passed all substantive claims in v13.713, including the Dirichlet-atom null lift, cone-deficit identity, centered Xi \(V_4\), complete four-character table, critical-line fixed locus, and the guardrail that the result is representation-theoretic rather than an operator bridge.

## 1. Completed logarithmic derivative [D]

Use
\[
\xi(s)
=
\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Then
\[
\boxed{
L(s):=\frac{\xi'}{\xi}(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi\!\left(\frac s2\right)
+\frac{\zeta'}{\zeta}(s),
}
\]
where
\[
\psi=\Gamma'/\Gamma.
\]

For \(\Re s>1\),
\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=
\sum_p\sum_{k\ge1}(\log p)p^{-ks}.
\]

Define
\[
P(s):=-\frac{\zeta'}{\zeta}(s).
\]

Then
\[
\boxed{
L(s)=A_\infty(s)-P(s),
}
\]
with
\[
\boxed{
A_\infty(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2).
}
\]

Thus the completed logarithmic derivative is the archimedean current minus the finite-prime current.

## 2. Prime/von-Mangoldt cone current [D]

Let
\[
r_{p,k}=k\log p.
\]

Each prime-power term is
\[
(\log p)e^{-sr_{p,k}}.
\]

Its symmetric-square cone lift is
\[
\boxed{
Q^\Lambda_{p,k}(s)
=
(\log p)e^{-\sigma r_{p,k}}
\left(
\cos(tr_{p,k}),
-i\sin(tr_{p,k}),
1
\right).
}
\]

Hence the prime side is an atomic logarithmic cone current
\[
\boxed{
Q_\Lambda(s)
=
\sum_{p,k}Q^\Lambda_{p,k}(s),
\qquad \Re s>1.
}
\]

Equivalently introduce the von-Mangoldt radial measure
\[
\boxed{
d\mu_\Lambda(r)
=
\sum_{n\ge2}\Lambda(n)\,
\delta_{\log n}(dr).
}
\]

Then
\[
\boxed{
P(s)
=
\int_0^\infty e^{-sr}\,d\mu_\Lambda(r).
}
\]

The arithmetic multiplicative data have therefore become an atomic additive current on logarithmic radius.

## 3. Digamma as a continuous logarithmic radial current [D]

For \(\Re z>0\),
\[
\psi(z)
=
-\gamma
+
\int_0^\infty
\frac{e^{-t}-e^{-zt}}{1-e^{-t}}\,dt.
\]

Set
\[
z=s/2,\qquad t=2r.
\]

Then
\[
\boxed{
\frac12\psi(s/2)
=
-\frac{\gamma}{2}
+
\int_0^\infty
\frac{e^{-2r}-e^{-sr}}
{1-e^{-2r}}\,dr.
}
\]

This is already a continuous superposition of the same exponential atoms \(e^{-sr}\) that occur discretely on the prime side.

The subtraction by \(e^{-2r}\) is essential: near \(r=0\) it regularizes the apparent singularity of \((1-e^{-2r})^{-1}\).

## 4. Elementary factors are also logarithmic radial currents [D]

For \(\Re s>1\),
\[
\frac1s
=
\int_0^\infty e^{-sr}\,dr,
\]
and
\[
\frac1{s-1}
=
\int_0^\infty e^{-(s-1)r}\,dr
=
\int_0^\infty e^{-sr}e^r\,dr.
\]

Therefore the elementary \(s(s-1)\) factor and the gamma factor live in the same radial Laplace/exponential language as the prime current.

Direct substitution gives
\[
\boxed{
A_\infty(s)
=
-\frac12(\log\pi+\gamma)
+
\int_0^\infty
\left[
e^{-sr}
\left(
1+e^r-\frac1{1-e^{-2r}}
\right)
+
\frac{e^{-2r}}{1-e^{-2r}}
\right]dr.
}
\]

The two displayed pieces inside the integral must not be separated at \(r=0\); their singular terms cancel in the sum.

Indeed the full integrand has the expansion
\[
\boxed{
1+\frac{s}{2}+O(r)
\qquad(r\downarrow0).
}
\]

Thus the archimedean contribution is itself a regularized continuous logarithmic current.

## 5. Canonical basepoint subtraction at s=2 [D]

A cleaner formulation removes the reference term and exposes a single \(s\)-independent radial density.

Define
\[
\boxed{
W_\infty(r)
=
1+e^r-\frac1{1-e^{-2r}}.
}
\]

At the convenient basepoint \(s_0=2\),
\[
A_\infty(2)
=
\frac32-\frac12(\log\pi+\gamma).
\]

Subtracting \(A_\infty(2)\) gives the exact identity
\[
\boxed{
A_\infty(s)-A_\infty(2)
=
\int_0^\infty
\left(e^{-sr}-e^{-2r}\right)
W_\infty(r)\,dr,
\qquad
\Re s>1.
}
\]

Near zero,
\[
W_\infty(r)
=
-\frac1{2r}
+\frac32
+O(r),
\]
while
\[
e^{-sr}-e^{-2r}
=
(2-s)r+O(r^2),
\]
so their product is finite.

At infinity,
\[
W_\infty(r)\sim e^r,
\]
and the integral converges for \(\Re s>1\).

This is the clean archimedean analogue of the basepoint-subtracted prime current.

## 6. Unified completed signed radial current [D]

The prime current satisfies
\[
\boxed{
P(s)-P(2)
=
\int_0^\infty
\left(e^{-sr}-e^{-2r}\right)
d\mu_\Lambda(r).
}
\]

Since
\[
L=A_\infty-P,
\]
subtracting at \(s=2\) gives
\[
\boxed{
L(s)-L(2)
=
\int_0^\infty
\left(e^{-sr}-e^{-2r}\right)
\left[
W_\infty(r)\,dr-d\mu_\Lambda(r)
\right].
}
\]

Define the signed completed radial current
\[
\boxed{
d\nu_\xi(r)
=
W_\infty(r)\,dr
-
d\mu_\Lambda(r).
}
\]

Then
\[
\boxed{
\frac{\xi'}{\xi}(s)
-
\frac{\xi'}{\xi}(2)
=
\int_0^\infty
\left(e^{-sr}-e^{-2r}\right)
d\nu_\xi(r),
\qquad
\Re s>1.
}
\]

This is the main result of the gate.

The completed logarithmic derivative is therefore not merely a prime cone current plus an unrelated correction: after basepoint regularization it is the Laplace transform of one signed logarithmic radial current containing

- a continuous archimedean density \(W_\infty(r)\,dr\);
- a discrete arithmetic measure \(-d\mu_\Lambda(r)\).

## 7. Cone interpretation [D]

For each continuous radius \(r>0\), define the null atom
\[
\boxed{
Q_r(s)
=
e^{-\sigma r}
\left(
\cos(tr),
-i\sin(tr),
1
\right).
}
\]

It satisfies
\[
T_r^2-X_r^2-Y_r^2=0.
\]

The prime current samples these null rays discretely at
\[
r=\log n
\]
with von-Mangoldt weights.

The archimedean current integrates over the same null-ray family continuously with density \(W_\infty(r)\).

Thus both finite and infinite places now occupy the same logarithmic cone-current language:
\[
\boxed{
\text{finite primes}
\leftrightarrow
\text{atomic logarithmic radii},
}
\]
\[
\boxed{
\text{archimedean completion}
\leftrightarrow
\text{continuous logarithmic radial density}.
}
\]

Their signed combination is \(d\nu_\xi\).

## 8. Centered coordinate form [D]

With
\[
w=s-\frac12,
\]
one has
\[
e^{-sr}
=
e^{-r/2}e^{-wr}.
\]

Therefore
\[
\boxed{
L\!\left(\frac12+w\right)-L(2)
=
\int_0^\infty
\left(
e^{-r/2}e^{-wr}-e^{-2r}
\right)
d\nu_\xi(r)
}
\]
in the original convergence half-plane \(\Re w>1/2\).

This explicitly places the centered variable \(w\) in the same additive-exponential pairing as the centered cone coordinate
\[
\widehat\tau+\ell=-rw.
\]

## 9. V4 behavior and the present limitation [D/G]

Every constituent has the standard reality property under
\[
C:s\mapsto\bar s
\]
because the radial weights are real:
\[
P(\bar s)=\overline{P(s)},
\qquad
A_\infty(\bar s)=\overline{A_\infty(s)}.
\]

For the completed sum, analytic continuation and the xi functional equation give
\[
\boxed{
L(1-s)=-L(s).
}
\]

Hence
\[
\boxed{
\Re L\in\chi_{+,-},
\qquad
\Im L\in\chi_{-,+},
}
\]
as established in v13.713.

However, the one-sided Laplace representation
\[
\int_0^\infty(e^{-sr}-e^{-2r})\,d\nu_\xi(r)
\]
converges directly only for \(\Re s>1\). Reflection \(s\mapsto1-s\) moves this region to \(\Re s<0\).

[G] Therefore the \(V_4\) functional-equation oddness is **not yet manifest term-by-term in this one-sided current representation**. It enters through analytic continuation of the completed function.

This is the remaining structural gap.

## 10. Exact arithmetic–archimedean balance law [D]

Because
\[
L(s)=A_\infty(s)-P(s)
\]
and
\[
L(1-s)=-L(s),
\]
analytic continuation gives
\[
\boxed{
P(s)+P(1-s)
=
A_\infty(s)+A_\infty(1-s),
}
\]
where both sides are interpreted meromorphically.

Thus the failure of the finite-prime current to be odd under the functional-equation reflection is exactly compensated by the archimedean completion.

This is an exact arithmetic–archimedean reflection balance.

## 11. Result and scope

The gate succeeds at the level requested:

\[
\boxed{
d\nu_\xi(r)
=
\left(
1+e^r-\frac1{1-e^{-2r}}
\right)dr
-
\sum_{n\ge2}\Lambda(n)\delta_{\log n}(dr)
}
\]

is a single signed logarithmic radial current for which
\[
\boxed{
\frac{\xi'}{\xi}(s)
-
\frac{\xi'}{\xi}(2)
=
\int_0^\infty
(e^{-sr}-e^{-2r})\,d\nu_\xi(r),
\qquad
\Re s>1.
}
\]

Both the prime and archimedean pieces are built from the same exponential/null-cone atoms.

[G] This is an exact current representation in the convergence half-plane, not yet a globally convergent symmetric cone representation of \(\xi'/\xi\).

## 12. Next gate [O]

The next target is now sharply defined:

\[
\boxed{
\text{construct a two-sided or theta/Mellin-symmetrized cone current in the centered variable }w=s-\frac12
}
\]

such that
\[
w\mapsto-w
\]
is manifest at the level of the kernel/current itself, rather than supplied afterward by analytic continuation.

Natural candidates are:

1. the Jacobi-theta/Mellin integral for completed zeta/xi;
2. a two-sided logarithmic-radius variable \(r\in\mathbb R\) obtained by pairing \(r\) and \(-r\);
3. differentiation of such a symmetric representation to recover the odd kernel for \(\xi'/\xi\).

Passing that gate would upgrade the current result from a one-sided prime–archimedean Laplace representation to a **manifestly functional-equation-equivariant centered cone current**.

## 13. Guardrails

- The prime Dirichlet series and the unified Laplace current above are directly convergent only for \(\Re s>1\).
- \(d\nu_\xi\) is a signed/regularized current, not a positive measure.
- The basepoint subtraction at \(s=2\) is part of the convergent representation.
- The global \(s\mapsto1-s\) symmetry currently uses analytic continuation.
- No RH, zero-location, positivity, spectral-determinant, or Hilbert–Pólya conclusion follows from this current representation alone.
