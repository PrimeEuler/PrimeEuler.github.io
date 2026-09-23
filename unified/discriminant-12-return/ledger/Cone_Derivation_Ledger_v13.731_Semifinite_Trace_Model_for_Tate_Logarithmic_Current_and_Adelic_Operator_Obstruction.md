# Cone Derivation Ledger v13.731 — Semifinite Trace Model for the Tate Logarithmic Current and Adelic-Operator Obstruction

**Date:** 2026-09-23  
**Status:** exact commutative/semifinite trace realization; canonical adelic Hilbert-space operator remains open  
**Parent:** v13.730

## 1. Finite-place trace realization

For each prime \(p\), let
\[
\mathcal H_p=\ell^2(\mathbb N_{\ge1}),
\qquad
H_p e_k=k(\log p)e_k,
\qquad
A_p=(\log p)I.
\]
Then for \(\Re s>0\),
\[
\operatorname{Tr}_{\mathcal H_p}(A_pe^{-sH_p})
=
(\log p)\sum_{k\ge1}p^{-ks}
=
-\frac{L_p'}{L_p}(s).
\]
Thus the finite Tate logarithmic current has the exact trace realization
\[
\boxed{
-\frac{L_p'}{L_p}(s)
=
\operatorname{Tr}(A_pe^{-sH_p}).
}
\]

On
\[
\mathcal H_{\rm fin}=\bigoplus_p\mathcal H_p,
\quad
H_{\rm fin}=\bigoplus_pH_p,
\quad
A_{\rm fin}=\bigoplus_pA_p,
\]
the operator \(A_{\rm fin}e^{-sH_{\rm fin}}\) is trace class for \(\Re s>1\), because
\[
\operatorname{Tr}(A_{\rm fin}e^{-sH_{\rm fin}})
=
\sum_{p,k\ge1}(\log p)p^{-ks}
=
\sum_{n\ge2}\Lambda_{\rm vM}(n)n^{-s}.
\]
Therefore
\[
\boxed{
P(s):=-\frac{\zeta'}{\zeta}(s)
=
\operatorname{Tr}(A_{\rm fin}e^{-sH_{\rm fin}}),
\qquad \Re s>1.
}
\]

The spectral measure of \(H_{\rm fin}\), with insertion \(A_{\rm fin}\), is exactly
\[
\boxed{
d\mu_\Lambda(r)
=
\sum_{n\ge2}\Lambda_{\rm vM}(n)\delta_{\log n}(dr).
}
\]

Differentiating,
\[
-\frac{d}{ds}P(s)
=
\operatorname{Tr}(A_{\rm fin}H_{\rm fin}e^{-sH_{\rm fin}})
=
\sum_n\Lambda_{\rm vM}(n)\log n\,n^{-s}.
\]
This exactly realizes the weighted prime current of v13.730.

## 2. Important interpretation limit

This finite trace model is exact, but it is not yet a canonical adelic representation.

The local space \(\ell^2(\mathbb N_{\ge1})\) is a convenient prime-power/Fock-like counting space. Its Hamiltonian records valuation level:
\[
k\mapsto k\log p.
\]
The insertion \(A_p=\log p\) removes the extra factor \(k\) that would arise from tracing \(H_p e^{-sH_p}\).

Hence the prime current is a genuine ordinary trace, but calling this construction "the adelic Tate operator" would be premature.

## 3. Archimedean relative trace

The v13.730 archimedean difference is
\[
A_\infty(s)-A_\infty(s_0)
=
\int_0^\infty
(e^{-sr}-e^{-s_0r})W_\infty(r)\,dr,
\]
for a basepoint such as \(s_0=2\), with
\[
W_\infty(r)=1+e^r-\frac1{1-e^{-2r}}.
\]

Near zero,
\[
W_\infty(r)=-\frac1{2r}+\frac32+O(r),
\]
while
\[
e^{-sr}-e^{-s_0r}=-(s-s_0)r+O(r^2).
\]
Thus their product is bounded at zero. At infinity the difference is integrable for \(\Re s,\Re s_0>1\).

This gives an exact **relative** trace functional in the commutative semifinite algebra of multiplication operators:
\[
\mathcal M_\infty=L^\infty(\mathbb R_+,|W_\infty(r)|dr).
\]
Let
\[
H_\infty=M_r,\qquad
J_\infty=M_{\operatorname{sgn}W_\infty}.
\]
With the canonical semifinite integration trace
\[
\tau_\infty(M_f)=\int_0^\infty f(r)|W_\infty(r)|\,dr
\]
on its natural positive domain,
\[
\boxed{
A_\infty(s)-A_\infty(s_0)
=
\tau_\infty\!\left[
J_\infty(e^{-sH_\infty}-e^{-s_0H_\infty})
\right].
}
\]

This is a semifinite von-Neumann-algebra trace, not the ordinary Hilbert-space trace of a multiplication operator. A nonzero multiplication operator on a nonatomic \(L^2\) space is generally not trace class, so replacing \(\tau_\infty\) by an ordinary operator trace would be incorrect.

## 4. Global relative trace formula

Combine the finite ordinary trace with the archimedean semifinite relative trace. For \(\Re s,\Re s_0>1\),
\[
\frac{\xi'}{\xi}(s)-\frac{\xi'}{\xi}(s_0)
=
\left[A_\infty(s)-A_\infty(s_0)\right]
-\left[P(s)-P(s_0)\right].
\]

Hence
\[
\boxed{
\frac{\xi'}{\xi}(s)-\frac{\xi'}{\xi}(s_0)
=
\tau_\infty\!\left[
J_\infty(e^{-sH_\infty}-e^{-s_0H_\infty})
\right]
-
\operatorname{Tr}_{\mathcal H_{\rm fin}}\!\left[
A_{\rm fin}(e^{-sH_{\rm fin}}-e^{-s_0H_{\rm fin}})
\right].
}
\]

This is an exact operator/trace realization of the anchored v13.715 current.

It is, however, a direct-sum model built from the already-known current; it is not yet a derivation from a canonical representation of \(\mathbb A^\times/\mathbb Q^\times\).

## 5. Why the naive single Hamiltonian fails

A tempting model is a bosonic partition function
\[
Z_p(s)=\operatorname{Tr}(e^{-sH_p})
=
\sum_{k\ge0}p^{-ks}
=
L_p(s).
\]
This identity is exact if the vacuum \(k=0\) is included.

But
\[
-\partial_s\log Z_p(s)
=
\frac{\operatorname{Tr}(H_pe^{-sH_p})}
{\operatorname{Tr}(e^{-sH_p})}
=
(\log p)\sum_{k\ge1}p^{-ks},
\]
whereas the unnormalized trace
\[
\operatorname{Tr}(H_pe^{-sH_p})
=
(\log p)\sum_{k\ge1}k\,p^{-ks}
\]
has an unwanted factor \(k\).

Therefore the logarithmic derivative is naturally a normalized thermal expectation, not the ordinary trace of the Hamiltonian. The alternative insertion \(A_p=(\log p)I\) on positive levels gives the desired ordinary trace exactly.

This distinction must be retained in any future canonical operator construction.

## 6. Relation to the explicit-formula distribution

The finite trace spectral measure is
\[
d\mu_{\rm fin}(r)
=
\sum_{p,k\ge1}(\log p)\delta_{k\log p}(dr).
\]
The archimedean semifinite spectral density is
\[
W_\infty(r)\,dr
\]
with finite-part/relative normalization at the origin.

Thus the signed spectral distribution of the combined relative trace model is exactly
\[
\boxed{
d\nu_\xi(r)
=
W_\infty(r)\,dr
-
\sum_{p,k\ge1}(\log p)\delta_{k\log p}(dr).
}
\]

This is the v13.715 distribution itself. In this limited but exact sense, the prime-plus-archimedean current is a trace/character distribution.

What is not established is that this trace distribution is the character of a natural irreducible/unitary adelic representation, or that it arises from a canonical global operator before inserting the known local factors.

## 7. Correction/refinement to v13.726 local-global comparison

The real spherical Knapp-Stein scalar relevant to the standard SL2 Eisenstein constant term is
\[
m_\infty(s)
=
\sqrt\pi\,\frac{\Gamma(s-\frac12)}{\Gamma(s)}.
\]
Writing
\[
\Gamma_{\mathbb R}(u)=\pi^{-u/2}\Gamma(u/2),
\]
one has the exact identity
\[
\boxed{
m_\infty(s)
=
\frac{\Gamma_{\mathbb R}(2s-1)}
{\Gamma_{\mathbb R}(2s)}.
}
\]

At a finite prime,
\[
m_p(s)
=
\frac{1-p^{-2s}}{1-p^{1-2s}}
=
\frac{L_p(2s-1)}{L_p(2s)}.
\]
Therefore
\[
\boxed{
m_{\mathbb A}(s)
=
m_\infty(s)\prod_pm_p(s)
=
\frac{\Lambda(2s-1)}{\Lambda(2s)}.
}
\]

So the real Knapp-Stein factor is **exactly the archimedean local factor of the global Eisenstein scattering coefficient at doubled adjacent arguments**.

This refines v13.726 Section 7. The direct zeta reflection ratio
\[
\Gamma_{\mathbb R}(1-s)/\Gamma_{\mathbb R}(s)
\]
is a different object; comparing it directly with \(m_\infty(s)\) does not negate the exact local-global Eisenstein factorization above.

## 8. Current status

**EXACT**
- finite prime current as an ordinary trace on prime-power counting spaces;
- weighted prime current via insertion of \(H_{\rm fin}\);
- archimedean anchored current as a commutative semifinite relative trace;
- global anchored \(\xi'/\xi\) as the difference of these traces;
- signed spectral distribution equals the v13.715 current;
- real Knapp-Stein scalar is the archimedean factor in \(\Lambda(2s-1)/\Lambda(2s)\).

**NOT YET ESTABLISHED**
- a single canonical Hilbert-space trace-class operator realizing both finite and infinite places;
- a derivation of the above trace model from the regular representation of the idele class group rather than from local-factor data;
- identification of the current as the character of a natural irreducible adelic representation;
- a linear trace construction whose spectrum is the nontrivial zero set of xi;
- Hilbert-Polya/RH consequences.

## 9. Next discriminating gates

1. Compare the exact relative trace above with the standard Weil explicit-formula distribution on the idele class group. Determine whether the prime-power and archimedean terms are the same distribution after test-function normalization.
2. If yes, identify the precise test-function transform taking the current \(d\nu_\xi\) into the conventional explicit formula; this would upgrade the direct-sum trace model to a canonical adelic trace-formula interpretation.
3. If no, record the normalization obstruction rather than forcing an adelic operator.
4. Separately test whether the positive Xi kernel \(\Phi\) can be obtained as a positive matrix coefficient of the Weil representation; do not infer this from positivity alone.

**Guardrail:** v13.731 constructs an exact trace realization of the logarithmic current, but not a canonical Hilbert-Polya operator. The archimedean trace is semifinite/relative, not an ordinary trace-class multiplication operator.
