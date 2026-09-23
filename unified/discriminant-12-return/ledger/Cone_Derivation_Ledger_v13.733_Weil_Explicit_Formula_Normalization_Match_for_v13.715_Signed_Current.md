# Cone Derivation Ledger v13.733 — Weil Explicit-Formula Normalization Match for the v13.715 Signed Current

**Date:** 2026-09-23  
**Status:** exact finite-place/centering match; exact archimedean match as principal-value distributions; canonical-operator identification still open  
**Parent:** v13.731  
**Audit context:** External Audit Round 86 (commit 1c080f3f8c2b8524a1a3da93c84dd1b54a7aff0b) independently passed v13.724–731 with no errors. A concurrent Suzuki entry uses v13.732; this lane therefore advances to v13.733.

## 1. Canonical Weil test-function normalization

Let
\[
C_{\mathbb Q}=\mathbb A^\times/\mathbb Q^\times.
\]
For a suitable multiplicative test function \(h\), write its Mellin transform as
\[
\widehat h(s)=\int_{C_{\mathbb Q}}h(u)|u|^s\,d^\times u.
\]

Restrict to the norm coordinate
\[
|u|=e^r
\]
and introduce the centered additive test function \(g\) by
\[
\boxed{h(e^r)=e^{-r/2}g(r).}
\]
Then
\[
\widehat h(s)
=
\int_{\mathbb R}g(r)e^{(s-1/2)r}\,dr.
\]
On the critical line
\[
s=\frac12+it,
\]
define
\[
\widehat g(t)=\int_{\mathbb R}g(r)e^{itr}\,dr.
\]
Therefore
\[
\boxed{\widehat h(\tfrac12+it)=\widehat g(t).}
\]
The inverse convention is
\[
g(r)=\frac1{2\pi}\int_{\mathbb R}\widehat g(t)e^{-itr}\,dt.
\]

Thus the conversion from the v13.715 one-sided Laplace coordinate to the canonical centered Weil Fourier coordinate is exactly the rho/half-density shift \(s\mapsto1/2+it\).

## 2. Finite places term by term

At a finite prime \(p\), the centered local contribution is
\[
\boxed{
W_p(g)
=
(\log p)\sum_{k\ge1}p^{-k/2}
\left[g(k\log p)+g(-k\log p)\right].
}
\]
Writing \(n=p^k\), this becomes
\[
\boxed{
W_{\rm fin}(g)
=
\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\sqrt n}
\left[g(\log n)+g(-\log n)\right].
}
\]

The v13.715 measure was
\[
d\mu_\Lambda(r)
=
\sum_{n\ge2}\Lambda_{\rm vM}(n)\delta_{\log n}(dr).
\]
Hence the exact conversion is
\[
\boxed{
d\mu_{\rm Weil}^{\rm fin}(r)
=
\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\sqrt n}
\left(\delta_{\log n}+\delta_{-\log n}\right).
}
\]

Equivalently:
1. shift to the critical center, producing the half-density \(e^{-|r|/2}\);
2. symmetrize under inversion \(r\mapsto-r\).

Thus the \(n^{-1/2}\) factor in the standard explicit formula is not a discrepancy with v13.715. It is exactly the half-density from \(s=1/2+it\).

## 3. Pole/completion terms

The canonical explicit formula contains the two evaluations
\[
\widehat h(0)+\widehat h(1).
\]
Under the centered substitution,
\[
\widehat h(0)
=
\int g(r)e^{-r/2}\,dr
=
\widehat g(i/2),
\]
and
\[
\widehat h(1)
=
\int g(r)e^{r/2}\,dr
=
\widehat g(-i/2).
\]
Therefore
\[
\boxed{
\widehat h(0)+\widehat h(1)
=
\widehat g(i/2)+\widehat g(-i/2).
}
\]

These are exactly the two terms represented in the uncentered logarithmic derivative by
\[
\frac1s+\frac1{s-1}
=
\partial_s\log[s(s-1)].
\]
Their one-sided Laplace densities are
\[
1+e^r.
\]

Thus the v13.730 split
\[
W_\infty(r)
=
\underbrace{1+e^r}_{\text{xi completion polynomial}}
-
\underbrace{\frac1{1-e^{-2r}}}_{\text{gamma/Tate term}}
\]
matches the pole/completion structure of the canonical explicit formula.

## 4. Archimedean gamma term

For
\[
L_\infty(s)=\pi^{-s/2}\Gamma(s/2),
\]
\[
\frac{L_\infty'}{L_\infty}(s)
=
-\frac12\log\pi+\frac12\psi(s/2).
\]
At \(s=1/2+it\),
\[
\boxed{
\frac{L_\infty'}{L_\infty}(\tfrac12+it)
=
-\frac12\log\pi
+
\frac12\psi(\tfrac14+\tfrac{it}{2}).
}
\]
After inversion pairing \(t\leftrightarrow-t\), the real archimedean multiplier is
\[
\boxed{
-\frac12\log\pi
+
\frac12\Re\psi(\tfrac14+\tfrac{it}{2}).
}
\]

This is the standard gamma/digamma multiplier in the Riemann-Weil explicit formula.

The corresponding \(r\)-space object is NOT obtained by treating
\[
e^{-|r|/2}W_\infty(|r|)\,dr
\]
as an ordinary measure, because \(W_\infty(r)\sim-1/(2r)\) at the origin.

The correct identification is distributional:
- v13.715 uses an anchored finite-part Laplace distribution;
- the canonical Weil local term uses its canonical principal-value distribution.

After the pole terms are separated, these are the same gamma-factor distribution under the centered Fourier/Mellin transform.

Hence:
\[
\boxed{\text{archimedean match is exact as distributions, not as ordinary densities}.}
\]

## 5. Centered explicit formula

With the above conventions, the Riemann-Weil formula takes the centered form
\[
\boxed{
\begin{aligned}
\sum_\rho
\widehat g\!\left(\frac{\rho-\frac12}{i}\right)
={}&
\widehat g(i/2)+\widehat g(-i/2)
\\
&-
\sum_{n\ge2}
\frac{\Lambda_{\rm vM}(n)}{\sqrt n}
\left[g(\log n)+g(-\log n)\right]
\\
&+
W_\infty^\Gamma(g),
\end{aligned}
}
\]
where \(W_\infty^\Gamma\) is the canonical principal-value gamma distribution in the stated Fourier convention.

The sign placement depends only on which side of the equality one calls the "Weil distribution"; the term-by-term normalization above is fixed.

## 6. Exact map from v13.715 to Weil form

The conversion is
\[
\boxed{
\text{one-sided Laplace current}
\to
\text{critical-line center}
\to
\text{half-density}
\to
\text{inversion symmetrization}
\to
\text{Weil PV at }r=0.
}
\]

Explicitly:
\[
e^{-sr}
\quad\mapsto\quad
e^{-r/2}e^{-itr},
\]
and
\[
\Lambda_{\rm vM}(n)\delta_{\log n}
\quad\mapsto\quad
\frac{\Lambda_{\rm vM}(n)}{\sqrt n}
\left(\delta_{\log n}+\delta_{-\log n}\right).
\]

The involution
\[
r\mapsto-r
\]
is the logarithmic form of idele inversion
\[
u\mapsto u^{-1}.
\]

Thus the same rank-one reflection already visible in the cone, theta, and centered xi lanes appears canonically in the idele-class explicit formula.

## 7. Consequence for v13.731

v13.731 constructed a direct-sum/semifinite relative trace model whose signed spectral distribution is the v13.715 current.

The present comparison shows:
\[
\boxed{
\text{the distribution realized by that trace model is canonical}
}
\]
after the exact centering/half-density/PV conversion above: it is the arithmetic distribution occurring in Weil's explicit formula.

This does NOT make the particular prime-power Hilbert spaces
\[
\bigoplus_p\ell^2(\mathbb N)
\]
canonical. The distribution is canonical; the v13.731 realization of it remains one convenient model.

## 8. Relation to adelic trace-formula constructions

Known adelic constructions interpret the same explicit-formula distribution as a trace/character distribution for the idele-class action on adelic or adele-class spaces (in Connes/Meyer-type formulations).

The correct next question is therefore no longer whether a trace distribution exists. It does.

The discriminating question is whether the v13.731 relative trace model factors through, or is naturally equivalent to, one of these canonical idele-class virtual/cohomological representations.

That equivalence has NOT been established here.

## 9. Status

**EXACT**
- Mellin/Fourier conversion \(\widehat h(1/2+it)=\widehat g(t)\);
- finite prime \(n^{-1/2}\) half-density;
- inversion symmetrization;
- pole terms \(\widehat g(\pm i/2)\);
- gamma/digamma multiplier;
- identification of the v13.715 signed current with the uncentered logarithmic-derivative presentation of the Weil arithmetic distribution.

**EXACT AS DISTRIBUTIONS**
- archimedean anchored finite-part current = centered Weil principal-value gamma distribution under the stated transform normalization.

**OPEN**
- canonical equivalence between the v13.731 direct-sum trace operators and an idele-class representation;
- a linear map from the Weil character distribution to the positive Xi kernel \(\Phi\);
- a spectral operator whose eigenvalues are the nontrivial zeros;
- Hilbert-Polya/RH consequences.

## 10. Next gates

1. Write the v13.731 finite trace model as a representation of the norm semigroup and compare its character with the restriction of the canonical idele-class distribution to the norm direction.
2. Determine exactly what information is lost by projecting \(C_{\mathbb Q}\) to \(|u|\in\mathbb R_+^\times\); this is the likely obstruction to upgrading the prime-power model itself to a canonical adelic representation.
3. Compare the Weil distribution with the theta/Weil representation from v13.729. The shared word "Weil" is not sufficient: determine whether the explicit-formula character and the oscillator theta representation are linked by an actual functor/intertwiner or are distinct constructions.
4. Keep the positive Xi kernel on the nonlinear Mellin/cumulant side unless such an intertwiner is explicitly derived.

**Guardrail:** the arithmetic distribution is now canonically identified. The particular v13.731 Hilbert-space realization is not.
