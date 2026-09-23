# Cone Derivation Ledger v13.730 — Tate Local Logarithmic Currents and v13.715 Place-by-Place Closure

**Date:** 2026-09-23  
**Status:** exact local-factor closure with explicit open operator-level questions  
**Parent:** v13.729

## 1. Result

The v13.715 prime-plus-archimedean current is exactly the inverse-Laplace/logarithmic-derivative shadow, place by place, of the Tate local factors together with the xi completion polynomial.

Write
\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\xi(s)=\frac12s(s-1)\Lambda(s).
\]
Then
\[
\frac{\xi'}{\xi}(s)
=
\frac1s+\frac1{s-1}
+\frac{L_\infty'}{L_\infty}(s)
+\sum_p\frac{L_p'}{L_p}(s).
\]

## 2. Finite places

For
\[
L_p(s)=(1-p^{-s})^{-1},
\]
\[
\frac{L_p'}{L_p}(s)
=
-(\log p)\sum_{k\ge1}p^{-ks}.
\]
Define
\[
d\nu_p(r)=-(\log p)\sum_{k\ge1}\delta_{k\log p}(dr).
\]
Then
\[
\boxed{\mathcal L[d\nu_p](s)=L_p'(s)/L_p(s).}
\]
Summing over p,
\[
\sum_p d\nu_p
=
-\sum_{n\ge2}\Lambda_{\rm vM}(n)\delta_{\log n},
\]
hence
\[
\boxed{
\sum_p\frac{L_p'}{L_p}(s)
=
-\sum_{n\ge2}\Lambda_{\rm vM}(n)n^{-s}
=
\frac{\zeta'}{\zeta}(s).
}
\]

Thus the prime atomic current of v13.715 is exactly the sum of the finite-place Tate logarithmic currents.

## 3. Real place and xi polynomial

The real Tate factor is
\[
L_\infty(s)=\pi^{-s/2}\Gamma(s/2),
\]
so
\[
\boxed{
\frac{L_\infty'}{L_\infty}(s)
=
-\frac12\log\pi+\frac12\psi(s/2).
}
\]
The xi polynomial contributes
\[
\boxed{
\frac d{ds}\log\!\left[\frac12s(s-1)\right]
=
\frac1s+\frac1{s-1}.
}
\]
Therefore the v13.715 archimedean term
\[
A_\infty(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi+\frac12\psi(s/2)
\]
is exactly
\[
\boxed{
A_\infty(s)
=
\partial_s\log\!\left[\frac12s(s-1)L_\infty(s)\right].
}
\]

This separates the smooth current into:
- pure real Tate gamma current;
- xi/Cartan completion-polynomial current.

## 4. Anchored inverse Laplace distribution

The exact v13.715 kernel is
\[
W_\infty(r)
=
1+e^r-\frac1{1-e^{-2r}},
\]
with
\[
W_\infty(r)=-\frac1{2r}+\frac32+O(r)
\]
near zero.

At basepoint \(s=2\),
\[
A_\infty(2)
=
\frac32-\frac12(\log\pi+\gamma),
\]
and
\[
\boxed{
A_\infty(s)-A_\infty(2)
=
\int_0^\infty(e^{-sr}-e^{-2r})W_\infty(r)\,dr.
}
\]

Distributionally,
\[
\boxed{
\mathcal L^{-1}[A_\infty]
=
A_\infty(2)\delta_0+\operatorname{Pf}_2W_\infty.
}
\]

The regular kernel splits visibly:
\[
\boxed{
W_\infty(r)
=
\underbrace{1+e^r}_{\text{xi polynomial}}
-
\underbrace{\frac1{1-e^{-2r}}}_{\text{real Tate gamma term}}.
}
\]
The gamma term requires the origin finite-part/contact normalization.

## 5. Full place decomposition

Define
\[
d\nu_\infty
=
A_\infty(2)\delta_0+\operatorname{Pf}_2W_\infty.
\]
Then, in the anchored Laplace sense,
\[
\boxed{
d\nu_\xi
=
d\nu_\infty+\sum_p d\nu_p.
}
\]
Equivalently,
\[
\boxed{
d\nu_\xi(r)
=
W_\infty(r)\,dr
-
\sum_{n\ge2}\Lambda_{\rm vM}(n)\delta_{\log n}(dr)
}
\]
with the understood finite-part prescription at the origin.

Thus
\[
\boxed{
\frac{\xi'}{\xi}(s)-\frac{\xi'}{\xi}(2)
=
\int_0^\infty(e^{-sr}-e^{-2r})\,d\nu_\xi(r).
}
\]

This is exactly v13.715, now derived directly from the Tate local factors.

## 6. Second logarithmic derivative

Differentiating the current gives
\[
d\eta_\xi(r)
=
-rW_\infty(r)\,dr
+
\sum_{n\ge2}\Lambda_{\rm vM}(n)\log n\,\delta_{\log n}(dr).
\]
Then
\[
\boxed{
\left(\frac{\xi'}{\xi}\right)'(s)
=
\int_0^\infty e^{-sr}\,d\eta_\xi(r).
}
\]

Prime by prime,
\[
\frac{d^2}{ds^2}\log L_p(s)
=
(\log p)^2\sum_{k\ge1}k\,p^{-ks},
\]
and for \(n=p^k\),
\[
k(\log p)^2
=
\Lambda_{\rm vM}(n)\log n.
\]
Hence the weighted atomic current is exactly the sum of the second logarithmic derivatives of the finite Tate factors.

## 7. Exact bridge to the positive Xi kernel

From v13.722,
\[
\Xi(w)=\int_{\mathbb R}\Phi(r)e^{wr}\,dr.
\]
Set
\[
M_k(w)=\int_{\mathbb R}r^k\Phi(r)e^{wr}\,dr.
\]
Then
\[
\frac{\Xi'}{\Xi}=\frac{M_1}{M_0},
\]
and
\[
\boxed{
\left(\frac{\Xi'}{\Xi}\right)'
=
\frac{M_2M_0-M_1^2}{M_0^2}.
}
\]
Since \(w=s-\frac12\), \(d/dw=d/ds\), and therefore
\[
\boxed{
\int_0^\infty e^{-sr}\,d\eta_\xi(r)
=
\frac{M_2(w)M_0(w)-M_1(w)^2}{M_0(w)^2},
\qquad w=s-\frac12.
}
\]

This exactly joins the place-by-place Tate logarithmic current to the nonlinear cumulant of the positive Xi kernel.

It does NOT give a linear measure identity between \(d\nu_\xi\) or \(d\eta_\xi\) and \(\Phi(r)\,dr\).

## 8. Exact vs open

**EXACT**
- finite-place Tate log derivatives = prime-power delta trains;
- their sum = von-Mangoldt current;
- real Tate log derivative = gamma/digamma current;
- xi polynomial log derivative = \(1/s+1/(s-1)\);
- v13.715 current = sum of these local currents;
- differentiated current = second local log derivatives;
- its Laplace transform = Xi-kernel second logarithmic cumulant.

**OPEN / NOT ESTABLISHED**
- a linear distributional transform taking \(d\nu_\xi\) directly to \(\Phi(r)dr\);
- a single canonical adelic operator whose local pieces produce all prime and real logarithmic currents;
- any spectral-determinant or Hilbert–Pólya interpretation of Xi.

## 9. Next gates

1. Construct an adelic operator candidate using the infinitesimal idele-norm generator / logarithm of local modulus, and determine whether the local logarithmic derivatives arise as matrix coefficients or traces rather than merely derivatives of scalar zeta factors.
2. Test whether the explicit-formula distribution is the natural global trace/character distribution of this candidate.
3. Keep the positive Xi kernel on the nonlinear cumulant side unless a genuine linear intertwiner is derived.

**Guardrail:** the local-factor merger is exact at the level of Tate zeta factors, logarithmic derivatives, anchored distributions, and Xi cumulants. No unified adelic spectral operator has yet been constructed.
