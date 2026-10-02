# Cone Derivation Ledger v13.968 — Sandbox: Protected Residual-to-Phase Certification Contract for the Xi Scalar

**Date:** 2026-10-02  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] exact protected residual-to-solution bound; [D] exact coefficient-to-Fourier uniform bound; [D] exact characteristic sign margin; [D] exact composition with the v13.967 phase-window budget; [G] avoids global division by the tiny ground energy; [O] instantiate with certified low-Schur and complement constants in both parity sectors  
**Authorization:** Jeremy, 2026-10-02 ("swwwt. letgs do it.")  
**Parents:** v13.392, v13.798, v13.801, v13.965, v13.966, v13.967  
**Collision check:** v13.968 was absent in the live tree immediately before this write.

---

## 0. Goal

v13.967 reduced certification of the no-twist Xi scalar to a bounded-window sign problem.

To certify

\[
\sigma_a(t)
=
\operatorname{sgn}m_a(t)
\]

on most of

\[
[0,T],
\]

it is enough to obtain a uniform enclosure for the one-source transform

\[
F_a(t)
=
\widehat{A_a^{-1}e^x}(t).
\]

A naive residual bound

\[
\|A_a^{-1}r\|
\le
\lambda_a^{-1}\|r\|
\]

is unusable on the Xi branch because

\[
\lambda_a
\]

is extremely small.

The present entry gives the correct protected/Feshbach error contract.

---

## 1. Block setup [D]

Let the source-faithful positive operator be split as

\[
\mathcal H
=
P\mathcal H
\oplus
Q\mathcal H.
\]

Write

\[
A
=
\begin{pmatrix}
A_{PP} & A_{PQ}\\
A_{QP} & B
\end{pmatrix},
\]

where

\[
B
=
QAQ.
\]

Assume the stiff complement satisfies

\[
\boxed{
B\succeq\gamma I,
\qquad
\gamma>0.
}
\tag{1}
\]

Define the exact Schur complement

\[
\boxed{
S
=
A_{PP}
-
A_{PQ}B^{-1}A_{QP}.
}
\tag{2}
\]

Assume

\[
\boxed{
S\succeq\sigma I,
\qquad
\sigma>0.
}
\tag{3}
\]

Set

\[
\boxed{
\chi
=
\|A_{PQ}\|
=
\|A_{QP}\|.
}
\tag{4}
\]

No lower bound on the full operator \(A\) is used.

---

## 2. Error equation [D]

Let

\[
v=A^{-1}f
\]

be the exact source solution and let

\[
\widehat v
\]

be any approximation.

Define the residual

\[
\boxed{
r
=
f-A\widehat v.
}
\tag{5}
\]

Then the solution error

\[
e=v-\widehat v
\]

satisfies

\[
Ae=r.
\]

Write

\[
e=
\binom{e_P}{e_Q},
\qquad
r=
\binom{r_P}{r_Q}.
\]

The block equations are

\[
A_{PP}e_P+A_{PQ}e_Q=r_P,
\]

\[
A_{QP}e_P+Be_Q=r_Q.
\]

---

## 3. Protected Schur error bound [D]

From the second equation,

\[
e_Q
=
B^{-1}
(r_Q-A_{QP}e_P).
\]

Substitute into the first:

\[
Se_P
=
r_P
-
A_{PQ}B^{-1}r_Q.
\]

Hence

\[
\|e_P\|
\le
\|S^{-1}\|
\left(
\|r_P\|
+
\|A_{PQ}\|
\|B^{-1}\|
\|r_Q\|
\right).
\]

Using

\[
\|S^{-1}\|\le\sigma^{-1},
\qquad
\|B^{-1}\|\le\gamma^{-1},
\]

we obtain

\[
\boxed{
\|e_P\|
\le
\frac{
\|r_P\|
+
(\chi/\gamma)\|r_Q\|
}{
\sigma
}.
}
\tag{6}
\]

Define

\[
\boxed{
E_P
=
\frac{
\|r_P\|
+
(\chi/\gamma)\|r_Q\|
}{
\sigma
}.
}
\tag{7}
\]

Then

\[
\|e_P\|\le E_P.
\]

---

## 4. Complement error bound [D]

From

\[
e_Q
=
B^{-1}
(r_Q-A_{QP}e_P),
\]

\[
\|e_Q\|
\le
\gamma^{-1}
\left(
\|r_Q\|
+
\chi\|e_P\|
\right).
\]

Therefore

\[
\boxed{
\|e_Q\|
\le
\frac{
\|r_Q\|
+
\chi E_P
}{
\gamma
}.
}
\tag{8}
\]

Define

\[
\boxed{
E_Q
=
\frac{
\|r_Q\|
+
\chi E_P
}{
\gamma
}.
}
\tag{9}
\]

Then

\[
\|e_Q\|\le E_Q.
\]

Consequently

\[
\boxed{
\|e\|
\le
E
:=
\sqrt{
E_P^2+E_Q^2
}.
}
\tag{10}
\]

This is the protected residual-to-solution contract.

---

## 5. Why this is better than the global inverse bound [D/I]

A global estimate would use

\[
\|A^{-1}\|
=
\lambda_{\min}(A)^{-1}.
\]

On the no-twist branch that quantity is catastrophically large.

The protected estimate instead uses:

- the low-dimensional Schur floor
  \[
  \sigma;
  \]
- the stiff-complement floor
  \[
  \gamma;
  \]
- the cross norm
  \[
  \chi;
  \]
- the split residuals
  \[
  r_P,r_Q.
  \]

Thus the near-null geometry is handled explicitly rather than charged uniformly to every residual component.

---

## 6. Fourier functional in the orthonormal Dirichlet basis [D]

Let

\[
\{\psi_n\}_{n\ge1}
\]

be the orthonormal Dirichlet basis in

\[
L^2(-a,a).
\]

For real \(t\), define

\[
p_n(t)
=
\int_{-a}^{a}
\psi_n(x)e^{itx}\,dx.
\]

By Bessel's inequality,

\[
\sum_{n\ge1}
|p_n(t)|^2
\le
\|e^{itx}\|_{L^2(-a,a)}^2.
\]

Since

\[
|e^{itx}|=1,
\]

\[
\boxed{
\sum_{n\ge1}
|p_n(t)|^2
\le
2a.
}
\tag{11}
\]

Therefore the Fourier-evaluation functional has the uniform coefficient-space norm bound

\[
\boxed{
\|\ell_t\|_{\ell^2\to\mathbb C}
\le
\sqrt{2a}.
}
\tag{12}
\]

This bound is independent of \(t\).

---

## 7. Uniform source-transform error [D]

Let

\[
F_a(t)
=
\langle
v,e^{-itx}
\rangle,
\]

and

\[
\widehat F_a(t)
=
\langle
\widehat v,e^{-itx}
\rangle.
\]

Then

\[
F_a(t)-\widehat F_a(t)
=
\ell_t(e).
\]

Using (10) and (12),

\[
\boxed{
|F_a(t)-\widehat F_a(t)|
\le
\sqrt{2a}\,E
}
\tag{13}
\]

for every real \(t\).

Thus one coefficient-space error bound controls the entire real characteristic window.

---

## 8. Uniform characteristic error [D]

Define

\[
Z_a(t)
=
(t-i)F_a(t),
\]

\[
\widehat Z_a(t)
=
(t-i)\widehat F_a(t).
\]

For

\[
|t|\le T,
\]

\[
|t-i|
\le
\sqrt{1+T^2}.
\]

Hence

\[
\boxed{
|Z_a(t)-\widehat Z_a(t)|
\le
\eta_T,
}
\tag{14}
\]

where

\[
\boxed{
\eta_T
=
\sqrt{
2a(1+T^2)
}\,
E.
}
\tag{15}
\]

Therefore separately,

\[
\boxed{
|
\operatorname{Re}Z_a(t)
-
\operatorname{Re}\widehat Z_a(t)
|
\le
\eta_T,
}
\tag{16}
\]

\[
\boxed{
|
\operatorname{Im}Z_a(t)
-
\operatorname{Im}\widehat Z_a(t)
|
\le
\eta_T.
}
\tag{17}
\]

---

## 9. Fail-closed sign criterion [D]

Recall

\[
m_a(t)
=
-
\frac{
\operatorname{Re}Z_a(t)
}{
\operatorname{Im}Z_a(t)
}.
\]

At a point \(t\), if

\[
\boxed{
|
\operatorname{Re}\widehat Z_a(t)
|
>
\eta_T
}
\tag{18}
\]

and

\[
\boxed{
|
\operatorname{Im}\widehat Z_a(t)
|
>
\eta_T,
}
\tag{19}
\]

then neither exact component can cross zero.

Therefore

\[
\boxed{
\operatorname{sgn}m_a(t)
=
-
\operatorname{sgn}
\operatorname{Re}\widehat Z_a(t)
\,
\operatorname{sgn}
\operatorname{Im}\widehat Z_a(t).
}
\tag{20}
\]

Whenever either margin test fails, that point is declared uncertain.

No guess is made.

---

## 10. Certified uncertainty set [D]

Define

\[
\boxed{
U_T
=
\left\{
t\in[0,T]:
\min
\left(
|
\operatorname{Re}\widehat Z_a(t)
|,
|
\operatorname{Im}\widehat Z_a(t)
|
\right)
\le
\eta_T
\right\}.
}
\tag{21}
\]

Its complement

\[
C_T
=
[0,T]\setminus U_T
\]

has certified Weyl sign.

Thus

\[
\boxed{
K_C
=
2
\int_{C_T}
\sigma_a(t)
\frac{t}{(1+t^2)^2}\,dt
}
\tag{22}
\]

is a certified scalar contribution.

If interval arithmetic encloses \(U_T\) by disjoint intervals

\[
U_T
\subset
\bigcup_j[u_j,v_j],
\]

then v13.967 gives

\[
\boxed{
\left|
\kappa_a^\Xi
-
K_C
\right|
\le
\sum_j
\left[
\frac1{1+u_j^2}
-
\frac1{1+v_j^2}
\right]
+
\frac1{1+T^2}.
}
\tag{23}
\]

This is the complete protected residual-to-phase certificate.

---

## 11. Separate parity solves [D]

The source-faithful implementation naturally solves even and odd blocks separately.

Let

\[
E^{(+)}
\]

and

\[
E^{(-)}
\]

be certified \(L^2\)-errors for the two parity source components.

Then the full source-vector error satisfies

\[
\boxed{
E
\le
\sqrt{
(E^{(+)})^2
+
(E^{(-)})^2
}.
}
\tag{24}
\]

Because the Fourier transforms of the parity pieces contribute orthogonally as real and imaginary parts on the real axis, one can sharpen (16)–(17) further by propagating separate parity errors.

The coarse bound (15) is already sufficient for a first certificate.

---

## 12. Connection with existing Feshbach certificates [D/I]

The project already has precisely the ingredients needed for this contract in several certified finite/high-complement lanes:

- stiff-complement lower bounds
  \[
  \gamma;
  \]
- cross-block norm bounds
  \[
  \chi;
  \]
- residual-certified Schur solves;
- low-dimensional effective cores.

For example, v13.392 reinstates a source-faithful high-complement Schur floor after eliminating the finite high block.

The present theorem does **not** claim that those historical constants can be copied unchanged into the current two-parity Xi scalar calculation.

Their sector, cutoff, and low-core hypotheses must be matched exactly.

The important point is structural:

\[
\boxed{
\textbf{the existing certificate architecture already has the right variables.}
}
\]

No new infinite-dimensional inverse theorem is required.

---

## 13. Required first instantiation [O]

For one fixed \(a\), preferably the already-developed \(a=1\) branch, the first proof-grade run should freeze:

1. a protected projector \(P\) in each parity;
2. a certified complement floor
   \[
   \gamma_\pm;
   \]
3. a certified low Schur floor
   \[
   \sigma_\pm;
   \]
4. certified cross norms
   \[
   \chi_\pm;
   \]
5. outward residual bounds
   \[
   \|r_{P,\pm}\|,
   \qquad
   \|r_{Q,\pm}\|;
   \]
6. the resulting
   \[
   E_\pm;
   \]
7. the phase margin
   \[
   \eta_T.
   \]

Then interval evaluation of

\[
\operatorname{Re}\widehat Z_a(t),
\qquad
\operatorname{Im}\widehat Z_a(t)
\]

on \([0,T]\) gives \(U_T\), and equation (23) gives the scalar interval.

---

## 14. Result

The no-twist Xi scalar can now be certified from protected residual data without dividing by the tiny global ground energy.

If

\[
B\succeq\gamma I,
\qquad
S\succeq\sigma I,
\qquad
\|A_{PQ}\|\le\chi,
\]

then the source-solution residual gives the explicit \(L^2\) error

\[
\boxed{
E_P
=
\frac{
\|r_P\|
+
(\chi/\gamma)\|r_Q\|
}{
\sigma
},
}
\]

\[
\boxed{
E_Q
=
\frac{
\|r_Q\|
+
\chi E_P
}{
\gamma
},
}
\]

\[
\boxed{
E
=
\sqrt{
E_P^2+E_Q^2
}.
}
\]

This yields the uniform characteristic error

\[
\boxed{
\eta_T
=
\sqrt{
2a(1+T^2)
}\,E.
}
\]

Every point with both approximate characteristic components farther than \(\eta_T\) from zero has certified Weyl sign.

The remaining uncertain windows are charged exactly by the v13.967 phase budget.

The next computational gate is therefore fully specified: instantiate these constants for the source-faithful \(a=1\) two-parity problem and produce the first proof-grade finite-\(a\) scalar enclosure.
