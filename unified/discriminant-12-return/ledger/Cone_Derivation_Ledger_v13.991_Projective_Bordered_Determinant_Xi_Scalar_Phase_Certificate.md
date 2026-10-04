# Cone Derivation Ledger v13.991 — Projective Bordered-Determinant Certificate for the Xi Scalar and Real-Axis Phase

**Date:** 2026-10-03  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact projective reduction eliminating the near-singular 6x6 inverse from both the scalar and phase observables; [D] inverse-free sign-box theorem via augmented singular values; [D] direct determinant-ratio enclosure for \(\kappa_a^\Xi\); [O] evaluate the bordered-matrix margins using the v13.990-corrected carrier/replay.  
**Parents:** v13.965–967, v13.980, v13.985, v13.987, v13.990.  
**Collision check:** immediately before the original v13.991 write, live HEAD was v13.990, commit 193607a2f808237ad8159724df4dcc674b78c9a7; no v13.991 entry was present. Immediately before this formatting repair, live HEAD was the original v13.991 commit 5921c225987d15d6644a78762f9834eefac34d5f.  
**Formatting repair:** the original GitHub write stripped LaTeX backslashes through the client string-escape layer. This repair changes formatting only, not the mathematical content.

---

## 0. Purpose

v13.987 proved that the direct source-energy route fails under the present certified perturbation budget because the corrected \(6\times6\) reduced source matrices have smallest singular values at machine-epsilon scale, while their certified perturbation radii are \(O(10^{-1})\).

That failure does **not** imply that the normalized Xi scalar or the real-axis Weyl sign is uncertifiable.

The reason is projective: the observables used by v13.965–967 and v13.966 depend only on ratios/signs of linear functionals of the source solution. The common near-singular determinant can therefore be canceled exactly before any perturbation estimate is made.

The present entry performs that cancellation.

---

## 1. One-parity static reduced solve

For one parity sector \(p\in\{e,o\}\), v13.985 gives a static exact reduced system

\[
\mathcal M_p w_p=f_p,
\qquad
w_p\in\mathbb R^6,
\]

and a reconstructed Fourier observable of the form

\[
\boxed{
F_p(t)=d_p(t)+g_p(t)^T w_p.
}
\tag{1}
\]

For the frozen-carrier notation of v13.985,

\[
d_p(t)=p_T(t)^T x_f,
\]

and

\[
g_p(t)=
\binom{
p_C(t)-X_C^Tp_T(t)
}{
Z^Tp_T(t)
}.
\]

No new solve is required as \(t\) varies.

---

## 2. Exact bordered-determinant identity

Let \(M\in\mathbb R^{n\times n}\) be invertible, \(Mw=f\), and let

\[
L=d+g^Tw.
\]

Define the bordered matrix

\[
\boxed{
\mathfrak B[L]
:=
\begin{pmatrix}
M & f\\
-g^T & d
\end{pmatrix}.
}
\tag{2}
\]

By the Schur-complement determinant identity,

\[
\det\mathfrak B[L]
=
\det M\,
\left(d+g^TM^{-1}f\right).
\]

Hence

\[
\boxed{
\det\mathfrak B[L]
=
(\det M)\,L.
}
\tag{3}
\]

This is exact.

Consequently, for two observables sharing the same reduced system,

\[
L_1=d_1+g_1^Tw,
\qquad
L_2=d_2+g_2^Tw,
\]

one has

\[
\boxed{
\frac{L_1}{L_2}
=
\frac{\det\mathfrak B[L_1]}
{\det\mathfrak B[L_2]}
}
\tag{4}
\]

whenever \(L_2\neq0\).

The factor \(\det M\) cancels **before** any inverse bound is used.

Therefore the tiny \(\sigma_{\min}(M)\) that killed v13.987 is not intrinsically part of the projective observable.

---

## 3. Two-parity block system

For the Xi source, combine the even and odd reduced systems into

\[
\boxed{
\mathcal M
=
\operatorname{diag}(\mathcal M_e,\mathcal M_o)
\in\mathbb R^{12\times12},
}
\tag{5}
\]

with

\[
w=\binom{w_e}{w_o},
\qquad
f=\binom{f_e}{f_o}.
\]

For real \(t\), use the parity-real decomposition of v13.985,

\[
F(t)=E(t)+iO(t),
\]

with

\[
E(t)=d_e(t)+g_e(t)^Tw_e,
\]

\[
O(t)=d_o(t)+g_o(t)^Tw_o,
\]

where the odd-sector Fourier factor \(i\) has been removed so that \(O(t)\in\mathbb R\).

Define

\[
R(t)=tE(t)+O(t),
\qquad
I(t)=tO(t)-E(t).
\]

Then

\[
R(t)=d_R(t)+g_R(t)^Tw,
\]

\[
I(t)=d_I(t)+g_I(t)^Tw,
\]

with

\[
\boxed{
d_R=t\,d_e+d_o,
\qquad
g_R=
\binom{t\,g_e}{g_o},
}
\tag{6}
\]

and

\[
\boxed{
d_I=t\,d_o-d_e,
\qquad
g_I=
\binom{-g_e}{t\,g_o}.
}
\tag{7}
\]

---

## 4. Exact inverse-free Weyl-sign formula

Define the two \(13\times13\) bordered matrices

\[
\boxed{
\mathfrak B_R(t)
=
\begin{pmatrix}
\mathcal M & f\\
-g_R(t)^T & d_R(t)
\end{pmatrix},
}
\tag{8}
\]

\[
\boxed{
\mathfrak B_I(t)
=
\begin{pmatrix}
\mathcal M & f\\
-g_I(t)^T & d_I(t)
\end{pmatrix}.
}
\tag{9}
\]

Equation (3) gives

\[
\det\mathfrak B_R(t)
=
(\det\mathcal M)R(t),
\]

\[
\det\mathfrak B_I(t)
=
(\det\mathcal M)I(t).
\]

Therefore

\[
R(t)I(t)
=
\frac{
\det\mathfrak B_R(t)\,
\det\mathfrak B_I(t)
}{
(\det\mathcal M)^2
}.
\]

Since \((\det\mathcal M)^2>0\),

\[
\boxed{
\operatorname{sgn}(R(t)I(t))
=
\operatorname{sgn}
\left(
\det\mathfrak B_R(t)\,
\det\mathfrak B_I(t)
\right).
}
\tag{10}
\]

Using v13.985,

\[
\sigma(t)=\operatorname{sgn}m(t)
=
-\operatorname{sgn}R(t)\operatorname{sgn}I(t),
\]

hence

\[
\boxed{
\sigma(t)
=
-\operatorname{sgn}
\left(
\det\mathfrak B_R(t)\,
\det\mathfrak B_I(t)
\right).
}
\tag{11}
\]

This is the decisive cancellation:

\[
\boxed{
\textbf{the real-axis phase sign requires no } \mathcal M^{-1},
\textbf{ no } \|\mathcal M^{-1}\|,
\textbf{ and not even the sign of }\det\mathcal M.
}
\]

The common near-singular factor disappears squared.

---

## 5. Exact projective formula for the Xi scalar

For complex \(z\), combine the parity transforms into

\[
F(z)=d_F(z)+g_F(z)^Tw,
\]

where

\[
d_F(z)=d_e(z)+d_o(z),
\qquad
g_F(z)=
\binom{g_e(z)}{g_o(z)}
\]

with the actual complex Fourier overlaps.

Define

\[
\boxed{
\mathfrak B_F(z)
=
\begin{pmatrix}
\mathcal M & f\\
-g_F(z)^T & d_F(z)
\end{pmatrix}.
}
\tag{12}
\]

Then

\[
F(z)=\frac{\det\mathfrak B_F(z)}{\det\mathcal M}.
\]

From v13.791 and v13.966,

\[
\kappa_a^\Xi
=
h_a(i)
=
\frac{F(i)}{F(-i)}.
\]

Therefore

\[
\boxed{
\kappa_a^\Xi
=
\frac{
\det\mathfrak B_F(i)
}{
\det\mathfrak B_F(-i)
}.
}
\tag{13}
\]

At \(z=\pm i\), all source functions and Fourier overlaps are real, so these are real bordered determinants.

Moreover,

\[
F(-i)
=
\|v_{a,+i}\|_{T_a}^2
>0,
\]

so the denominator is nonzero.

Equation (13) is an exact, scale-free replacement for the failed separate parity-energy inversion.

---

## 6. Inverse-free sign certification from singular-value margins

Let \(\widehat{\mathfrak B}\) be a numerical bordered matrix and suppose the exact bordered matrix satisfies

\[
\|\mathfrak B-\widehat{\mathfrak B}\|_2
\le
\varepsilon_{\mathfrak B}.
\]

If

\[
\boxed{
\sigma_{\min}(\widehat{\mathfrak B})
>
\varepsilon_{\mathfrak B},
}
\tag{14}
\]

then every matrix on the segment

\[
\widehat{\mathfrak B}
+s(\mathfrak B-\widehat{\mathfrak B}),
\qquad 0\le s\le1,
\]

is nonsingular by Weyl's singular-value inequality.

Hence the real determinant cannot cross zero along the segment, and

\[
\boxed{
\operatorname{sgn}\det\mathfrak B
=
\operatorname{sgn}\det\widehat{\mathfrak B}.
}
\tag{15}
\]

Crucially, this uses the conditioning of the **bordered observable matrix**, not the conditioning of \(\mathcal M\).

The near-singular source matrix may therefore remain catastrophically ill-conditioned while the projective observable is still certifiable.

---

## 7. Adaptive sign boxes without reconstructed-vector norms

Let

\[
J=[c-h,c+h].
\]

Suppose

\[
\|\mathfrak B_R(t)-\widehat{\mathfrak B}_R(t)\|_2
\le
\varepsilon_R(J)
\]

for all \(t\in J\), and similarly for \(I\).

Because only the final bordered row varies with \(t\),

\[
\|
\widehat{\mathfrak B}_R(t)
-
\widehat{\mathfrak B}_R(c)
\|_2
=
\left\|
\bigl(
g_R(t)-g_R(c),
d_R(t)-d_R(c)
\bigr)
\right\|_2.
\]

Hence, with any certified row-derivative bound

\[
\left\|
\frac{d}{dt}
(g_R(t),d_R(t))
\right\|_2
\le
L_R(J),
\]

one has

\[
\|
\widehat{\mathfrak B}_R(t)
-
\widehat{\mathfrak B}_R(c)
\|_2
\le
hL_R(J).
\]

Therefore the sufficient box criterion is

\[
\boxed{
\sigma_{\min}
\left(
\widehat{\mathfrak B}_R(c)
\right)
>
\varepsilon_R(J)+hL_R(J).
}
\tag{16}
\]

Likewise,

\[
\boxed{
\sigma_{\min}
\left(
\widehat{\mathfrak B}_I(c)
\right)
>
\varepsilon_I(J)+hL_I(J).
}
\tag{17}
\]

When both hold, the exact signs of both bordered determinants are constant throughout \(J\), and

\[
\boxed{
\sigma_J
=
-\operatorname{sgn}
\det\widehat{\mathfrak B}_R(c)
\,
\operatorname{sgn}
\det\widehat{\mathfrak B}_I(c).
}
\tag{18}
\]

This replaces v13.985's reconstructed-vector sign margin

\[
|\widehat R(c)|>\varepsilon+hL_R
\]

by a **distance-to-singularity margin for the projective observable itself**.

No bound on \(\|\widehat v\|\) is needed.

---

## 8. Direct determinant-ratio interval for \(\kappa_a^\Xi\)

Let

\[
\widehat B_\pm
=
\widehat{\mathfrak B}_F(\pm i)
\]

and suppose

\[
\|B_\pm-\widehat B_\pm\|_2\le\varepsilon_\pm.
\]

Let the singular values of \(\widehat B_\pm\) be

\[
\widehat\sigma_{\pm,1},
\dots,
\widehat\sigma_{\pm,13}.
\]

If

\[
\widehat\sigma_{\pm,\min}>\varepsilon_\pm,
\]

then Weyl gives

\[
\widehat\sigma_{\pm,j}-\varepsilon_\pm
\le
\sigma_j(B_\pm)
\le
\widehat\sigma_{\pm,j}+\varepsilon_\pm.
\]

Thus

\[
\boxed{
L_\pm
:=
\prod_{j=1}^{13}
(\widehat\sigma_{\pm,j}-\varepsilon_\pm)
\le
|\det B_\pm|
\le
\prod_{j=1}^{13}
(\widehat\sigma_{\pm,j}+\varepsilon_\pm)
=:U_\pm.
}
\tag{19}
\]

The determinant signs are fixed by (15), so equation (13) yields a rigorous ratio interval. In particular, for positive sign ratio,

\[
\boxed{
\kappa_a^\Xi
\in
\left[
\frac{L_+}{U_-},
\frac{U_+}{L_-}
\right].
}
\tag{20}
\]

If the determinant-sign ratio is negative, the corresponding signed interval is obtained by applying the certified determinant signs to the magnitude interval.

Again, no \(\|\mathcal M^{-1}\|\) appears.

---

## 9. Why this survives v13.987

v13.987 attempted to certify absolute source energies by first proving stability of the near-singular \(6\times6\) inverse.

That requires a condition of the form

\[
\|\Delta\mathcal M\|
<
\sigma_{\min}(\mathcal M),
\]

which fails by roughly \(10^{14}\)–\(10^{15}\).

The bordered formulation never asks for that inequality.

Instead it asks whether the **observable-augmented matrices**

\[
\mathfrak B_R(t),
\qquad
\mathfrak B_I(t),
\qquad
\mathfrak B_F(\pm i)
\]

remain a certified positive distance from singularity.

This is mathematically the correct conditioning question for a projective observable.

A tiny common denominator in the underlying source solve is harmless if it cancels from the normalized quantity.

---

## 10. Interaction with v13.990

v13.990 cancels the leading remote \(1/n\) residual moment in the four-dimensional carrier at fixed Ritz value and upgrades the far-tail decay from

\[
O(N^{-1/2})
\]

to

\[
O(N^{-3/2}).
\]

That construction does not by itself certify the Xi scalar.

Its role here is to reduce the model-error contribution to the exact bordered matrices, especially the carrier/Fourier-row terms entering

\[
\varepsilon_R(J),
\qquad
\varepsilon_I(J),
\qquad
\varepsilon_\pm.
\]

The two gates therefore compose naturally:

1. v13.990 improves the exact-operator approximation of the carrier;
2. v13.991 removes the catastrophic source-inverse amplification from the consumer.

---

## 11. Next numerical gate

Using the v13.990-corrected M3 carrier, build the nominal \(12\times12\) block system and the \(13\times13\) bordered matrices

\[
\widehat{\mathfrak B}_R(t),
\qquad
\widehat{\mathfrak B}_I(t),
\qquad
\widehat{\mathfrak B}_F(\pm i).
\]

Then report:

1. \(\sigma_{\min}(\widehat{\mathfrak B}_F(i))\) and \(\sigma_{\min}(\widehat{\mathfrak B}_F(-i))\);
2. the full singular spectra needed for (19);
3. the exact propagated bordered-matrix error radii \(\varepsilon_\pm\);
4. the resulting direct interval for \(\kappa_a^\Xi\), if the margins close;
5. on the real axis, adaptive minima of \(\sigma_{\min}(\widehat{\mathfrak B}_R(t))\) and \(\sigma_{\min}(\widehat{\mathfrak B}_I(t))\), with the unresolved phase-weight budget of v13.967/v13.985.

If the bordered singular-value margins fail, that failure is itself diagnostic: it identifies a genuinely projective near-zero rather than the already-known common source amplitude.

---

## 12. Result

The Xi scalar and real-axis phase observables admit exact projective formulations in which the near-singular source determinant cancels identically:

\[
\boxed{
\kappa_a^\Xi
=
\frac{
\det\mathfrak B_F(i)
}{
\det\mathfrak B_F(-i)
}.
}
\]

and

\[
\boxed{
\sigma(t)
=
-\operatorname{sgn}
\left(
\det\mathfrak B_R(t)
\det\mathfrak B_I(t)
\right).
}
\]

Therefore the v13.987 inverse-stability failure is **not** an obstruction to these normalized observables.

The correct certification problem is now the singular-value separation of a handful of \(13\times13\) bordered matrices, with v13.990 supplying the improved remote-tail error budget.
