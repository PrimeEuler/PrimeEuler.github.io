# Cone Derivation Ledger v13.993 — Shared-Null Wedge Factorization and Pre-Elimination Projective Border Theorem

**Date:** 2026-10-03  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact finite-dimensional shared-wedge factorization of bordered observables; [D] exact compatibility of bordered determinants with arbitrary-carrier Schur/Feshbach elimination; [N] v13.988 diagnostic shows the naive whole-border singular-value gate remains at machine-epsilon scale; [G] reduced KKT payload is therefore not the correct place to certify the projective ratio; [O] move the projective border before complement elimination and establish a finite-section/relative-determinant tail theorem.  
**Parents:** v13.980, v13.987–992.  
**Diagnostic commits:** fd51e45a2985c8f41635cb845d5b51d0e814d5ee, 3e956dffd967404db9666024bee9e15cbed50529.  
**Collision check:** immediately before this write, live HEAD was 3e956dffd967404db9666024bee9e15cbed50529; no v13.993 ledger entry was present.

---

## 0. Purpose

v13.991 showed that for a reduced source system

\[
Mw=f
\]

and one affine observable

\[
L=d+g^Tw,
\]

the bordered matrix

\[
\mathfrak B(g,d)
=
\begin{pmatrix}
M&f\\
-g^T&d
\end{pmatrix}
\]

satisfies

\[
\det\mathfrak B(g,d)
=
(\det M)L.
\]

Therefore ratios of observables cancel \(\det M\).

The first proposed certificate was to prove each bordered matrix itself safely nonsingular via

\[
\sigma_{\min}(\widehat{\mathfrak B})
>
\varepsilon_{\mathfrak B}.
\]

The present entry shows two things.

First, that direct singular-value gate does not improve the current v13.988 numerical conditioning: the bordered matrices still carry several common near-null factors.

Second, those common factors can be removed algebraically one level earlier. In finite dimensions, the bordered determinant commutes exactly with the complement Schur elimination. Hence the KKT/complement determinant is itself a common factor and need not be certified separately in an observable ratio.

---

## 1. Corrected v13.988 reduced matrices [N]

For one parity sector, use the corrected arbitrary-carrier data of v13.978/v13.988:

\[
M_p
=
\begin{pmatrix}
H_{C,p}&K_{{\rm eff},p}^T\\
K_{{\rm eff},p}&J_{{\rm eff},p}
\end{pmatrix},
\]

\[
f_p
=
\binom{
f_{C,p}
}{
s_{{\rm eff},p}
},
\]

and regular source background

\[
h_p=h_{{\rm reg},p}.
\]

The replay reproduces the v13.987 reduced singular minima:

\[
\boxed{
\sigma_{\min}(M_e)
\approx
2.2161\times10^{-16},
}
\]

\[
\boxed{
\sigma_{\min}(M_o)
\approx
2.0177\times10^{-16}.
}
\]

Thus the source matrices remain catastrophically close to singular in the nominal frozen payload.

---

## 2. One-parity energy borders remain nearly singular [N]

The nominal parity source energy is represented by

\[
G_p
=
h_p
+
f_p^TM_p^{-1}f_p.
\]

Its bordered matrix is

\[
\mathfrak B_p
=
\begin{pmatrix}
M_p&f_p\\
-f_p^T&h_p
\end{pmatrix}.
\]

The singular spectra show that augmentation by the source row and column does not remove all near-null directions.

Even:

\[
\boxed{
\sigma_{\min}(\mathfrak B_e)
\approx
7.12\times10^{-17}.
}
\]

Odd:

\[
\boxed{
\sigma_{\min}(\mathfrak B_o)
\approx
3.60\times10^{-16}.
}
\]

Therefore the one-border singular-value criterion is not the missing stability mechanism.

---

## 3. Combined Xi borders remain at machine-epsilon scale [N]

Combine the two parity systems:

\[
M
=
M_e\oplus M_o,
\qquad
f=
\binom{f_e}{f_o}.
\]

The two deficiency-overlap observables are nominally

\[
F(-i)=G_e+G_o,
\]

\[
F(i)=G_e-G_o.
\]

Hence define

\[
g_-=
\binom{f_e}{f_o},
\qquad
d_-=h_e+h_o,
\]

and

\[
g_+=
\binom{f_e}{-f_o},
\qquad
d_+=h_e-h_o.
\]

The two \(13\times13\) borders are

\[
\mathfrak B_\pm
=
\begin{pmatrix}
M&f\\
-g_\pm^T&d_\pm
\end{pmatrix}.
\]

The CI replay gives

\[
\boxed{
\sigma_{\min}(\mathfrak B_-)
\approx
1.0385\times10^{-16},
}
\]

\[
\boxed{
\sigma_{\min}(\mathfrak B_+)
\approx
1.9561\times10^{-16}.
}
\]

Thus the direct v13.991 whole-border condition

\[
\sigma_{\min}(\widehat{\mathfrak B}_\pm)
>
\varepsilon_\pm
\]

does not close on the current reduced payload.

This is not a contradiction of v13.991. The determinant ratio identity remains exact. What fails is only the proposed method of certifying each numerator and denominator determinant independently.

---

## 4. The nominal determinant ratio is not a scalar claim [G]

The diagnostic high-precision determinant ratio of the present frozen approximate payload is

\[
\frac{\det\mathfrak B_+}{\det\mathfrak B_-}
\approx
2.0738060568.
\]

This lies outside the exact Schur interval \((-1,1)\).

That is expected to be possible for the present **uncertified nominal reduced data** because v13.987 already proved that the KKT/Feshbach perturbation radius is enormously larger than the smallest singular values.

Therefore

\[
\boxed{
2.0738060568\ldots
}
\]

is not promoted as \(\kappa_a^\Xi\), not even as a reliable approximation to it.

Its only role is to demonstrate that one must remove the shared near-null factors before interpreting a determinant ratio numerically.

---

## 5. Shared source matrix and cofactor line [D]

For a general \(n\times n\) reduced matrix \(M\) and source \(f\), define the common \(n\times(n+1)\) source matrix

\[
\boxed{
C=[\,M\ \ f\,].
}
\tag{1}
\]

Every observable border has the form

\[
\boxed{
\mathfrak B(r)
=
\begin{pmatrix}
C\\
r
\end{pmatrix},
}
\tag{2}
\]

where

\[
r=(-g^T,d).
\]

Assume for the moment that

\[
\operatorname{rank}C=n.
\]

Then

\[
\dim\ker C=1.
\]

Let

\[
\nu\neq0
\]

span the right nullspace:

\[
C\nu=0.
\]

The alternating \(n\)-fold row wedge of \(C\) is a vector normal to the row space. Therefore there is a nonzero scalar \(\alpha_C\), depending only on \(C\), such that

\[
\boxed{
\det\mathfrak B(r)
=
\alpha_C\,
r\nu.
}
\tag{3}
\]

Equivalently, if \(\nu\) is unit-normalized,

\[
\boxed{
|\det\mathfrak B(r)|
=
\sqrt{\det(CC^T)}
\,|r\nu|.
}
\tag{4}
\]

Thus for any two observable rows \(r_1,r_2\),

\[
\boxed{
\frac{
\det\mathfrak B(r_1)
}{
\det\mathfrak B(r_2)
}
=
\frac{
r_1\nu
}{
r_2\nu
}.
}
\tag{5}
\]

All common singular-volume factors of \(C\) cancel exactly.

When \(M\) is invertible,

\[
\nu
\propto
\binom{M^{-1}f}{-1},
\]

so (5) is simply the projective form of the source solution.

The important point is that determinant magnitudes themselves are irrelevant. Only the projective source line matters.

---

## 6. The current reduced source line is not separated [N/G]

For the v13.988 combined source matrix

\[
C=[\,M\ \ f\,]
\in\mathbb R^{12\times13},
\]

the singular values are approximately

\[
2.17748,\,
1.00674\times10^{-2},\,
2.49391\times10^{-4},\,
4.17054\times10^{-6},
\]

\[
6.56726\times10^{-8},\,
2.573997\times10^{-10},\,
1.64828\times10^{-12},
\]

followed by

\[
6.45294\times10^{-15},\,
1.50289\times10^{-15},\,
1.05210\times10^{-15},\,
2.97024\times10^{-16},\,
1.65317\times10^{-16}.
\]

Hence the one-dimensional null line is not cleanly separated from the nominal near-null row-space cluster under the current reduced-payload uncertainty.

So replacing the determinant ratio by a direct SVD nullvector of \([M\ f]\) does **not** solve the certification problem.

Again, the obstruction is the already-known reduced KKT/Feshbach uncertainty.

---

## 7. Exact pre-elimination block setup [D]

Now return to the arbitrary-carrier three-block system of v13.980.

Group the retained core-plus-carrier space into one block \(R\), and the numerical complement into \(Q\).

Write the exact finite-dimensional block operator as

\[
\boxed{
\mathcal A
=
\begin{pmatrix}
A_R&E^*\\
E&D
\end{pmatrix},
}
\tag{6}
\]

with source

\[
\boxed{
b=
\binom{b_R}{b_Q}.
}
\tag{7}
\]

For an observable row, write

\[
\boxed{
p^*=
\begin{pmatrix}
p_R^*&p_Q^*
\end{pmatrix}.
}
\tag{8}
\]

Assume

\[
D
\]

is invertible.

Define the usual Schur data

\[
\boxed{
S
=
A_R-E^*D^{-1}E,
}
\tag{9}
\]

\[
\boxed{
b_{\rm eff}
=
b_R-E^*D^{-1}b_Q,
}
\tag{10}
\]

\[
\boxed{
p_{\rm eff}^*
=
p_R^*-p_Q^*D^{-1}E,
}
\tag{11}
\]

and

\[
\boxed{
d
=
p_Q^*D^{-1}b_Q.
}
\tag{12}
\]

Then the exact source observable is

\[
\boxed{
F
=
p^*\mathcal A^{-1}b
=
d
+
p_{\rm eff}^*S^{-1}b_{\rm eff}.
}
\tag{13}
\]

This is exactly the v13.980/v13.978 KKT/Feshbach architecture.

---

## 8. Full bordered matrix before complement elimination [D]

Define the full bordered matrix in the block order \(R\), border, \(Q\):

\[
\boxed{
\mathfrak B_{\rm full}(p)
=
\begin{pmatrix}
A_R & b_R & E^*\\
-p_R^* & 0 & -p_Q^*\\
E & b_Q & D
\end{pmatrix}.
}
\tag{14}
\]

Take the Schur complement of \(D\).

The upper-left block becomes

\[
A_R-E^*D^{-1}E=S.
\]

The source column becomes

\[
b_R-E^*D^{-1}b_Q=b_{\rm eff}.
\]

The observable row becomes

\[
-p_R^*
+
p_Q^*D^{-1}E
=
-p_{\rm eff}^*.
\]

The border scalar becomes

\[
0
-
(-p_Q^*)D^{-1}b_Q
=
d.
\]

Therefore

\[
\boxed{
\mathfrak B_{\rm full}(p)/D
=
\begin{pmatrix}
S&b_{\rm eff}\\
-p_{\rm eff}^*&d
\end{pmatrix}
=
\mathfrak B_{\rm red}(p).
}
\tag{15}
\]

Hence the determinant identity is

\[
\boxed{
\det\mathfrak B_{\rm full}(p)
=
(\det D)
\det\mathfrak B_{\rm red}(p).
}
\tag{16}
\]

Likewise,

\[
\boxed{
\det\mathcal A
=
(\det D)\det S.
}
\tag{17}
\]

Combining (13), (16), and (17),

\[
\boxed{
F
=
\frac{
\det\mathfrak B_{\rm red}(p)
}{
\det S
}
=
\frac{
\det\mathfrak B_{\rm full}(p)
}{
\det\mathcal A
}.
}
\tag{18}
\]

Thus the KKT/Feshbach complement determinant is a **common multiplicative factor**.

---

## 9. Observable ratios eliminate the entire base operator determinant [D]

For two observables \(p_1,p_2\) with the same operator \(\mathcal A\) and source \(b\),

\[
F_j
=
p_j^*\mathcal A^{-1}b.
\]

Equation (18) gives

\[
\boxed{
\frac{F_1}{F_2}
=
\frac{
\det\mathfrak B_{\rm full}(p_1)
}{
\det\mathfrak B_{\rm full}(p_2)
}.
}
\tag{19}
\]

Both

\[
\det D
\]

and

\[
\det S
\]

have disappeared.

Equivalently, the whole base determinant

\[
\det\mathcal A
\]

has disappeared.

For the Xi scalar at the finite-section level,

\[
\boxed{
\kappa_a^\Xi
=
\frac{F(i)}{F(-i)}
=
\frac{
\det\mathfrak B_{\rm full}(p_i)
}{
\det\mathfrak B_{\rm full}(p_{-i})
}.
}
\tag{20}
\]

For real-axis phase carriers, the same squared-denominator cancellation gives

\[
\boxed{
\operatorname{sgn}(R(t)I(t))
=
\operatorname{sgn}
\left[
\det\mathfrak B_{\rm full}(p_R(t))
\det\mathfrak B_{\rm full}(p_I(t))
\right],
}
\tag{21}
\]

whenever the finite-dimensional determinant signs are defined.

This is the pre-elimination version of v13.991.

---

## 10. Meaning for the KKT residual problem [I]

The KKT solves of v13.982/v13.988 numerically approximate

\[
D^{-1}E,
\qquad
D^{-1}b_Q,
\]

and thereby construct

\[
S,\quad
b_{\rm eff},\quad
p_{\rm eff},\quad
d.
\]

v13.987 showed that the resulting absolute reduced matrix and source uncertainties are too large for direct inverse stability.

Equations (16)–(20) show that this elimination is **not algebraically necessary** for a projective observable.

At finite dimension one may instead form the observable border before eliminating \(D\).

Therefore

\[
\boxed{
\textbf{the large KKT inverse-action residuals are not fundamental factors of the finite-dimensional projective observable.}
}
\]

They are artifacts of choosing to evaluate the Schur complement first.

This does not yet mean the exact infinite operator has been certified without KKT. It identifies the route by which that certification should be attempted.

---

## 11. Determinant-category guardrail [G]

The identities above are exact ordinary-determinant statements for finite matrices.

The v13.980 numerical complement is an infinite-dimensional operator.

Therefore one must **not** simply write

\[
\det D
\]

for the exact infinite complement without proving that the relevant determinant or relative determinant exists.

The project already distinguishes ordinary finite determinants, rank-one boundary perturbation determinants, and regularized/Fredholm determinants in the v13.661 and v13.708–712 lineage.

Thus the infinite-dimensional promotion requires one of two rigorous routes:

1. a finite-section theorem showing that the full bordered determinant **ratio** converges with a certified remote-tail error; or
2. a relative/Fredholm determinant construction in the correct operator category, with the common complement factor cancelled there.

Until one of these is supplied,

\[
\boxed{
\text{(20) is a finite-section exact theorem and a proof architecture, not yet the exact infinite-\(a\) certificate.}
}
\]

---

## 12. Correct next gate [O]

The next computation should not rebuild a more complicated KKT payload.

Instead:

1. work in the source-faithful finite parity basis before complement elimination;
2. form the two full augmented source/observable borders for \(F(i)\) and \(F(-i)\);
3. exploit the existing structured \(A/B\) displacement-rank and rank-one pole formulas;
4. identify and factor the common source/operator wedge analytically or by a protected low-dimensional quotient;
5. certify only the **relative projective quantity**;
6. separately bound the finite-section-to-infinite tail.

A parallel analytic gate is to determine whether the required ratio sits naturally in an already-established relative/Fredholm determinant category.

---

## 13. Result

The current reduced \(13\times13\) borders are still nearly singular:

\[
\boxed{
\sigma_{\min}(\mathfrak B_-)
\approx1.04\times10^{-16},
\qquad
\sigma_{\min}(\mathfrak B_+)
\approx1.96\times10^{-16}.
}
\]

So the naive whole-border singular-value gate of v13.991 fails on the present v13.988 payload.

However the exact algebra is stronger than that failed gate.

For any finite arbitrary-carrier decomposition,

\[
\boxed{
\det\mathfrak B_{\rm full}(p)
=
(\det D)\det\mathfrak B_{\rm red}(p),
}
\]

and

\[
\boxed{
F
=
\frac{
\det\mathfrak B_{\rm full}(p)
}{
\det\mathcal A
}.
}
\]

Therefore all complement and base-operator determinant factors cancel from observable ratios.

The certification problem has moved again:

\[
\boxed{
\textbf{do not stabilize the reduced inverse or its whole border; certify the common-factor-quotiented full projective border.}
}
\]
