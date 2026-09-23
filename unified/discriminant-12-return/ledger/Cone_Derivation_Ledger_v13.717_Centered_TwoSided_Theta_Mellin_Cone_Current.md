# Cone Derivation Ledger v13.717 — Centered Two-Sided Theta/Mellin Cone Current

Date: 2026-09-23

Status: exact Xi/Zeta cone-lane continuation. This entry closes the one-sided functional-equation-symmetry gap left explicitly open in v13.715 and independently confirmed by audit v13.716.

Status labels: **[D]** exact derived, **[O]** open, **[G]** guardrail.

## 0. Synchronization and collision check

Immediately before this write, the live repository head was v13.716 / External Audit Round 84 at commit \`c59db3851cae604ae259a644b763734819dcadbe\`. The intended v13.717 filename was absent. No collision was present.

The audit v13.716 independently passed v13.715, including high-precision checks of the digamma current and an end-to-end numerical test of the unified prime–archimedean one-sided current. It specifically confirmed that the remaining gap was real: the one-sided representation on \(r>0\) did not itself make \(s\mapsto1-s\) manifest. The present entry addresses exactly that gap.

## 1. Theta/Mellin starting point [D]

Let
\[
\vartheta(x)
=
\sum_{n\in\mathbb Z}e^{-\pi n^2x}
=
1+2\psi(x),
\]
where
\[
\psi(x)
=
\sum_{n\ge1}e^{-\pi n^2x}.
\]

Jacobi inversion is
\[
\boxed{
\vartheta(x)
=
x^{-1/2}\vartheta(1/x).
}
\]

For
\[
\Lambda(s)
=
\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]
the Mellin representation is
\[
\Lambda(s)
=
\int_0^\infty
\psi(x)x^{s/2}\frac{dx}{x}
\]
initially for \(\Re s>1\).

Split at \(x=1\), apply Jacobi inversion on \(0<x<1\), and analytically continue. One obtains
\[
\boxed{
\Lambda(s)
=
-\frac1s-\frac1{1-s}
+
\int_1^\infty
\psi(x)
\left(
x^{s/2}+x^{(1-s)/2}
\right)
\frac{dx}{x}.
}
\]

Since
\[
\xi(s)=\frac12s(s-1)\Lambda(s),
\]
the rational terms contribute exactly \(1/2\), giving
\[
\boxed{
\xi(s)
=
\frac12
+
\frac12s(s-1)
\int_1^\infty
\psi(x)
\left(
x^{s/2}+x^{(1-s)/2}
\right)
\frac{dx}{x}.
}
\]

This representation is entire after the explicit pole cancellation.

## 2. Center at the critical line [D]

Set
\[
\boxed{
s=\frac12+w,
\qquad
\Xi(w)=\xi\!\left(\frac12+w\right).
}
\]

Then
\[
s(s-1)=w^2-\frac14
\]
and
\[
x^{s/2}+x^{(1-s)/2}
=
2x^{1/4}
\cosh\!\left(\frac w2\log x\right).
\]

Hence
\[
\boxed{
\Xi(w)
=
\frac12
+
\left(w^2-\frac14\right)
\int_1^\infty
\psi(x)x^{-3/4}
\cosh\!\left(\frac w2\log x\right)\,dx.
}
\]

At this stage the functional-equation parity is already manifest:
\[
w^2-\frac14
\]
and
\[
\cosh\!\left(\frac w2\log x\right)
\]
are both even in \(w\).

Therefore
\[
\boxed{
\Xi(-w)=\Xi(w).
}
\]

## 3. Two-sided logarithmic radius [D]

Set
\[
x=e^{2r}.
\]

For \(x\ge1\), \(r\ge0\), and
\[
dx=2e^{2r}dr,
\qquad
x^{-3/4}dx=2e^{r/2}dr.
\]

Thus
\[
\boxed{
\Xi(w)
=
\frac12
+
2\left(w^2-\frac14\right)
\int_0^\infty
e^{r/2}\psi(e^{2r})\cosh(wr)\,dr.
}
\]

Define the even theta radial kernel
\[
\boxed{
K_\theta(r)
=
e^{|r|/2}\psi(e^{2|r|})
=
e^{|r|/2}
\sum_{n\ge1}e^{-\pi n^2e^{2|r|}}.
}
\]

By construction,
\[
\boxed{
K_\theta(-r)=K_\theta(r).
}
\]

Since
\[
\int_{\mathbb R}K_\theta(r)e^{wr}\,dr
=
2\int_0^\infty K_\theta(r)\cosh(wr)\,dr,
\]
we obtain the centered two-sided current
\[
\boxed{
\Xi(w)
=
\frac12
+
\left(w^2-\frac14\right)
\int_{-\infty}^{\infty}
K_\theta(r)e^{wr}\,dr.
}
\]

Equivalently,
\[
\boxed{
\xi\!\left(\frac12+w\right)
=
\frac12
+
\left(w^2-\frac14\right)
\int_{\mathbb R}
e^{|r|/2}
\sum_{n\ge1}e^{-\pi n^2e^{2|r|}}
e^{wr}\,dr.
}
\]

Because \(K_\theta\) decays super-exponentially as \(|r|\to\infty\), this bilateral transform converges for every complex \(w\).

## 4. Functional equation is now internal to the kernel [D]

Define
\[
I_\theta(w)
=
\int_{\mathbb R}
K_\theta(r)e^{wr}\,dr.
\]

Then
\[
I_\theta(-w)
=
\int_{\mathbb R}
K_\theta(r)e^{-wr}\,dr.
\]

Substitute \(r\mapsto-r\):
\[
I_\theta(-w)
=
\int_{\mathbb R}
K_\theta(-r)e^{wr}\,dr.
\]

Since \(K_\theta\) is even,
\[
\boxed{
I_\theta(-w)=I_\theta(w).
}
\]

Therefore
\[
\boxed{
\Xi(-w)=\Xi(w)
}
\]
follows directly from the two-sided current itself.

The fundamental interaction is invariant under the simultaneous reflection
\[
\boxed{
(w,r)\mapsto(-w,-r),
}
\]
because
\[
(-w)(-r)=wr.
\]

Thus
\[
\boxed{
e^{(-w)(-r)}=e^{wr}.
}
\]

The completed functional-equation reflection is therefore represented internally as orientation reversal of logarithmic radius.

## 5. Relation to centered cone coordinates [D]

For the centered cone atom use
\[
w=u+it,
\]
and choose the orientation convention
\[
\widehat\tau+\ell=-rw.
\]

Then
\[
e^{-rw}
=
e^{\widehat\tau+\ell}.
\]

Because \(K_\theta(r)\) is even, replacing \(r\) by \(-r\) converts the displayed bilateral transform between \(e^{wr}\) and \(e^{-wr}\) without changing the current.

For each \(r\), the exponential atom
\[
e^{-rw}
=
e^{-ur}e^{-itr}
\]
has the symmetric-square null lift
\[
\boxed{
Q_r(w)
=
e^{-ur}
\left(
\cos(tr),
-i\sin(tr),
1
\right),
}
\]
satisfying
\[
\boxed{
T_r^2-X_r^2-Y_r^2=0.
}
\]

Hence the theta/Mellin representation integrates the same centered null-cone exponential atoms over a two-sided logarithmic radius.

## 6. Odd derivative current [D]

Differentiate
\[
I_\theta(w)
=
\int_{\mathbb R}K_\theta(r)e^{wr}\,dr.
\]

Super-exponential decay justifies differentiation under the integral for all \(w\), giving
\[
\boxed{
I_\theta'(w)
=
\int_{\mathbb R}
rK_\theta(r)e^{wr}\,dr.
}
\]

Since \(K_\theta\) is even,
\[
rK_\theta(r)
\]
is odd. Therefore
\[
\boxed{
I_\theta'(-w)
=
-I_\theta'(w).
}
\]

Equivalently,
\[
\boxed{
I_\theta'(w)
=
2\int_0^\infty
rK_\theta(r)\sinh(wr)\,dr.
}
\]

Now
\[
\Xi(w)
=
\frac12+
\left(w^2-\frac14\right)I_\theta(w),
\]
so
\[
\boxed{
\Xi'(w)
=
2wI_\theta(w)
+
\left(w^2-\frac14\right)I_\theta'(w).
}
\]

The first term is odd because \(w\) is odd and \(I_\theta\) is even. The second is odd because \(w^2-\frac14\) is even and \(I_\theta'\) is odd. Hence
\[
\boxed{
\Xi'(-w)=-\Xi'(w).
}
\]

Away from zeros,
\[
\boxed{
\frac{\Xi'}{\Xi}(-w)
=
-\frac{\Xi'}{\Xi}(w).
}
\]

Since
\[
\frac{\Xi'}{\Xi}(w)
=
\frac{\xi'}{\xi}\!\left(\frac12+w\right),
\]
this yields directly
\[
\boxed{
\frac{\xi'}{\xi}(1-s)
=
-\frac{\xi'}{\xi}(s).
}
\]

Thus the oddness of the logarithmic derivative is derived from parity of the two-sided current, not imported afterward as an external analytic-continuation symmetry.

## 7. Character interpretation [D]

The chain is now
\[
\boxed{
K_\theta(r)\text{ even}
\Longrightarrow
I_\theta(w)\text{ even}
\Longrightarrow
I_\theta'(w)\text{ odd}
}
\]
and
\[
\boxed{
\Xi(w)\text{ even},
\qquad
\Xi'(w)/\Xi(w)\text{ odd}.
}
\]

This reproduces the functional-reflection part of the \(V_4\) character decomposition from v13.713 at the kernel/current level.

Reality is also manifest because \(K_\theta(r)\) is real:
\[
\overline{I_\theta(w)}
=
I_\theta(\bar w).
\]

Consequently
\[
\boxed{
\Xi(\bar w)=\overline{\Xi(w)},
}
\]
and the two generators
\[
w\mapsto-w,
\qquad
w\mapsto\bar w
\]
are both visible directly in the bilateral theta current.

## 8. What has been upgraded relative to v13.715 [D]

v13.715 gave the exact one-sided signed current
\[
d\nu_\xi(r)
=
W_\infty(r)dr-d\mu_\Lambda(r)
\]
for \(\xi'/\xi\) in \(\Re s>1\), but its \(s\mapsto1-s\) symmetry was not manifest in that representation.

The present theta/Mellin construction gives a different but complementary representation:
\[
\boxed{
\Xi(w)
=
\frac12+
\left(w^2-\frac14\right)
\int_{\mathbb R}K_\theta(r)e^{wr}\,dr
}
\]
that is globally convergent and has functional reflection built into
\[
K_\theta(-r)=K_\theta(r).
\]

Therefore the specific structural gap identified in v13.715 §9 and independently confirmed by v13.716 §5 is closed.

## 9. Important distinction between the two currents [G]

The v13.715 current exposes the finite-prime/archimedean decomposition explicitly:
\[
d\nu_\xi
=
\text{continuous archimedean density}
-
\text{atomic von-Mangoldt measure}.
\]

The present theta current exposes the global functional-equation symmetry explicitly:
\[
K_\theta(-r)=K_\theta(r).
\]

These are not presently proved to be the same measure/current under a direct transform.

[G] Therefore one must not yet claim that the atomic prime measure itself has been converted explicitly into the even theta density.

The open bridge is to derive, through Mellin/Poisson/explicit-formula machinery, an exact transformation connecting the v13.715 prime–archimedean current to the v13.717 symmetric theta current.

## 10. Main result

\[
\boxed{
K_\theta(r)
=
e^{|r|/2}
\sum_{n\ge1}e^{-\pi n^2e^{2|r|}}
}
\]
is a real, even, super-exponentially decaying logarithmic-radius kernel, and
\[
\boxed{
\xi\!\left(\frac12+w\right)
=
\frac12+
\left(w^2-\frac14\right)
\int_{\mathbb R}K_\theta(r)e^{wr}\,dr.
}
\]

The kernel-level involution is
\[
\boxed{
(w,r)\mapsto(-w,-r),
}
\]
and directly yields
\[
\boxed{
\Xi(-w)=\Xi(w),
\qquad
\frac{\Xi'}{\Xi}(-w)
=
-\frac{\Xi'}{\Xi}(w).
}
\]

Thus functional-equation reflection is realized as logarithmic-radius orientation reversal in the centered two-sided cone current.

## 11. Next gate [O]

There are now two exact Xi/Zeta currents:

1. v13.715: one-sided prime–archimedean current, with arithmetic content explicit;
2. v13.717: two-sided theta/Mellin current, with functional-equation symmetry explicit.

The next decisive gate is
\[
\boxed{
\text{derive an exact transform/explicit-formula bridge between these two currents.}
}
\]

A successful bridge should explain how the atomic radii
\[
r=\log n
\]
weighted by \(\Lambda(n)\), together with the continuous archimedean density, reorganize into the even theta kernel \(K_\theta(r)\), or else identify the precise distributional transform relating them.

Only after that bridge is explicit should the project compare this global Xi current with the independently constructed Suzuki/Fredholm-Weyl current.

## 12. Guardrails

- The theta current and the prime–archimedean current are complementary exact representations, not yet identified as the same measure.
- The bilateral theta transform is globally convergent because \(K_\theta\) decays super-exponentially.
- The logarithmic derivative formula is used away from zeros of \(\Xi\).
- No RH, zero-location, positivity, spectral-determinant, or Hilbert–Pólya conclusion follows from the evenness of this kernel alone.
- The Suzuki operator bridge remains open.
