# Cone Derivation Ledger v13.763 — Lane B Centered Prime-Orbit Trace and Exact Cross-Lane Weil Bridge

Date: 2026-09-24

Lane: B — Norm-Quotient / Idele-Class Representation, with an exact cross-lane consequence for Lane A.

Status: [D] exact finite-place distributional trace; [X] exact Lane-B/Lane-A finite-current identification; [N] canonical norm-line spectrum remains continuous and Lane-A Schur nonresonance is not affected.

Parents: v13.731, v13.734, v13.736, v13.739, v13.744, v13.746, v13.760–762.

## 0. Synchronization

The live ledger and recent commits were checked immediately before this write. Current ledger head is v13.762 (External Audit Round 93); recent repository head is commit `0a83714b8786c4bd843a43acc90049d97f17cbd9`. No v13.763 exists and no numbering collision is present.

Round 93 confirms Lane A v13.761 and says Lane B still has no new commits. This entry is therefore the first post-v13.760 Lane-B commit.

## 1. Imported facts — do not rederive

From v13.731, on
[
\mathcal H_{\rm fin}=\bigoplus_p\ell^2(\mathbb N_{\ge1}),
]
[
H_{\rm fin}e_{p,k}=k\log p\,e_{p,k},\qquad
A_{\rm fin}e_{p,k}=\log p\,e_{p,k}.
]
For \(\Re s>1\),
[
\operatorname{Tr}(A_{\rm fin}e^{-sH_{\rm fin}})
=-\frac{\zeta'}{\zeta}(s).
]

From v13.736/739, this prime-power Hilbert space is an auxiliary arithmetic trace realization, not the canonical quotient representation. The trivial-\(C_{\mathbb Q}^1\) norm carrier is the continuous regular representation on \(L^2(\mathbb R,dr)\).

From v13.744/746, the centered finite Weil distribution is
[
\mu_{\rm Weil}^{\rm fin}
=
\sum_{p,k\ge1}(\log p)p^{-k/2}
(\delta_{k\log p}+\delta_{-k\log p}),
]
and Suzuki's common current satisfies
[
\mathscr W_{S,{\rm fin}}=-\mu_{\rm Weil}^{\rm fin}.
]

## 2. Gate B.1 — exact centered finite-place trace [D]

Let \(\phi\in C_c^\infty(\mathbb R)\). Define
[
T_\phi
:=
A_{\rm fin}e^{-H_{\rm fin}/2}
\bigl[\phi(H_{\rm fin})+\phi(-H_{\rm fin})\bigr].
]

Because \(\phi\) has compact support and the set of prime powers with \(k\log p\) in a bounded interval is finite, \(T_\phi\) has finite rank. Hence its ordinary trace is unambiguous:
[
\begin{aligned}
\operatorname{Tr}T_\phi
&=
\sum_{p,k\ge1}
(\log p)p^{-k/2}
\left[
\phi(k\log p)+\phi(-k\log p)
\right]\\
&=
\left\langle\mu_{\rm Weil}^{\rm fin},\phi\right\rangle.
\end{aligned}
]

Therefore
[
\boxed{
\left\langle\mu_{\rm Weil}^{\rm fin},\phi\right\rangle
=
\operatorname{Tr}\!\left[
A_{\rm fin}e^{-H_{\rm fin}/2}
(\phi(H_{\rm fin})+\phi(-H_{\rm fin}))
\right].
}
]

This is stronger than a formal diagonal analogy: on \(C_c^\infty(\mathbb R)\) it is an exact ordinary finite-rank trace formula.

For larger test spaces one must impose sufficient decay or interpret the expression distributionally. In particular, arbitrary Schwartz decay in the variable \(r\) is not by itself a blanket trace-class theorem for the prime sum; no such extension is claimed here.

## 3. Local Lefschetz factorization [D]

For the positive \(k\)-fold \(p\)-orbit, the local multiplicative linearization at the fixed additive point has denominator
[
|1-p^k|_p=1.
]
The centered half-density contributes
[
|p^k|_p^{1/2}=p^{-k/2},
]
and the primitive valuation period/Haar step contributes
[
\ell_p=\log p.
]
Thus
[
(\log p)\frac{|p^k|_p^{1/2}}{|1-p^k|_p}
=(\log p)p^{-k/2}.
]

For the inverse orientation,
[
|1-p^{-k}|_p=p^k,\qquad |p^{-k}|_p^{1/2}=p^{k/2},
]
so
[
(\log p)\frac{p^{k/2}}{p^k}
=(\log p)p^{-k/2}.
]

Hence inversion symmetrization gives the same coefficient on \(\pm k\log p\).

The provenance is therefore:
[
\boxed{
\text{primitive period }\log p
\times
\text{Lefschetz denominator}
\times
\text{critical half-density}
=
(\log p)p^{-k/2}.
}
]
The factor \(p^{-k/2}\) is not, by itself, the positive-orientation Lefschetz Jacobian.

## 4. Gate B.2 — exact operator dictionary [D]

The v13.731 pair now has the exact centered finite-place dictionary
[
H_{\rm fin}:\quad \text{iterated orbit length }k\log p,
]
[
A_{\rm fin}:\quad \text{primitive orbit/Haar weight }\log p,
]
[
e^{-H_{\rm fin}/2}:\quad \text{critical half-density }p^{-k/2}.
]

Thus the centered arithmetic insertion is
[
\boxed{A_{\rm fin}e^{-H_{\rm fin}/2}.}
]

This upgrades v13.731 from merely reproducing the uncentered logarithmic current to an exact finite-place carrier for the centered Weil prime train.

It does NOT upgrade \(\mathcal H_{\rm fin}\) into the canonical norm-quotient representation: v13.739's continuous-spectrum obstruction remains in force.

## 5. Gate B.3 / Lane-A bridge — exact common finite current [X]

Combining §2 with the independently established Lane-A identity from v13.744/746,
[
\mathscr W_{S,{\rm fin}}=-\mu_{\rm Weil}^{\rm fin},
]
gives, for every \(\phi\in C_c^\infty(\mathbb R)\),
[
\boxed{
\left\langle\mathscr W_{S,{\rm fin}},\phi\right\rangle
=
-
\operatorname{Tr}\!\left[
A_{\rm fin}e^{-H_{\rm fin}/2}
(\phi(H_{\rm fin})+\phi(-H_{\rm fin}))
\right].
}
]

This is a genuine cross-lane identity [X]: Lane B's centered prime-orbit trace is exactly the negative finite arithmetic component of Lane A's common Suzuki–Weil current.

Using v13.746,
[
\mathscr W_S
=
\mathscr W_{S,\infty/0}
-
\mu_{\rm Weil}^{\rm fin},
]
where
[
\mathscr W_{S,\infty/0}
=
-\frac12\operatorname{Pf}|r|^{-1}
-(2A+1)\delta_0
-r_1''.
]
Therefore
[
\boxed{
\mathscr W_S+\mu_{\rm Weil}^{\rm fin}
=
-\frac12\operatorname{Pf}|r|^{-1}
-(2A+1)\delta_0-r_1''.
}
]

So after removing the exact Lane-B prime-orbit trace, what remains in the Lane-A full-line current is precisely the already-audited origin/archimedean package. There is no finite-prime atom at \(r=0\); the origin contact term belongs to the archimedean/finite-part normalization.

## 6. What this does and does not do for Lane A [X/N]

This bridge is directly relevant to Lane A's full-line bulk current and gives an exact operator realization of its finite arithmetic part.

It does NOT repair the open v13.761/v13.762 Schur-denominator problem. Round 93 established that
[
1+M_{00},\qquad1+M_{1x}
]
are finite-\(A\) basepoint boundary-transfer quantities whose nonresonance is not implied by bulk Weil/helix spectral control.

Accordingly:
[
\boxed{
\text{exact prime-orbit trace bridge}
\not\Rightarrow
\text{finite-}A\text{ Schur nonresonance}.
}
]

This records the cross-lane relevance without creating a false dependency or collision with Lane A's earliest open gate.

## 7. Status of the canonical adelic question [N/D]

The bare norm-line representation
[
(U_\tau f)(r)=f(r-\tau)
]
still has continuous generator \(-i\partial_r\), no nonzero fixed points, and no intrinsic prime-power spectrum. Its canonical translation-invariant trace density is supported at the identity.

The arithmetic prime train becomes canonical only after retaining the local adelic valuation/orbit data before collapse to the bare norm line. The prime label \(p\), primitive period \(\log p\), and repetition \(k\) are then pushed to the common norm coordinate \(k\log p\).

Thus:
[
\boxed{
\text{canonical norm carrier} \neq \text{prime-power Hilbert spectrum},
}
]
while
[
\boxed{
\text{local adelic orbit data}
\xrightarrow{\text{centered trace}}
\mu_{\rm Weil}^{\rm fin}
}
]
is exact at the finite-place distribution level.

## 8. Next Lane-B gates

1. Formulate the preceding finite-place trace as the finite part of a single relative/semifinite adelic trace by adjoining the v13.731/v13.746 archimedean-origin carrier, with one common test-function convention.
2. Determine whether that combined trace is merely a direct-sum realization of already-known local factors or is unitarily/intertwining-equivalent to a canonical representation on an adelic quotient/class space. Do not promote the former to the latter without an explicit intertwiner.
3. Compare the resulting full trace functional with Lane A's screw/Weil quadratic form, while preserving v13.761's boundary-feedback obstruction.

## 9. Guardrails

No RH, Hilbert–Pólya, pure-point norm-generator, or Lane-A Schur-nonresonance conclusion follows.

The exact new content is:
[
\boxed{
\mu_{\rm Weil}^{\rm fin}
=
\text{centered prime-orbit trace of }
A_{\rm fin}e^{-H_{\rm fin}/2}
}
]
on compactly supported test functions, and
[
\boxed{
\mathscr W_{S,{\rm fin}}
=
-\mu_{\rm Weil}^{\rm fin}
}
]
is now an explicit operator-level cross-lane bridge.
