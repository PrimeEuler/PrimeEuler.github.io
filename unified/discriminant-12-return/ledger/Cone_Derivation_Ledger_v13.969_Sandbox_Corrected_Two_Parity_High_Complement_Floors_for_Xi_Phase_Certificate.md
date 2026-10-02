# Cone Derivation Ledger v13.969 — Sandbox: Corrected Two-Parity High-Complement Floors for the Xi Phase Certificate

**Date:** 2026-10-02  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [D] exact block-floor reduction; [D] corrected odd negative-pole comparison theorem; [N-cert] reuse of older certified inequalities only as auxiliary operator bounds; [D] explicit corrected stiffness floors \(\gamma_+>0.008208\), \(\gamma_->0.068980\); [G] historical odd theorem remains on HOLD; [I] new R-statistic reproducer is cross-lane context only and not a proof input  
**Authorization:** Jeremy, 2026-10-02 ("swwwt. letgs do it.")  
**Parents:** v13.392, v13.434, v13.443, v13.799, v13.967–968  
**Cross-lane note:** the newly committed sieve-flow R-statistic reproducer in research-notes/ (commit 8d261838f18fb650284a7892155b61607dadb0aa) is relevant as an independent arithmetic-frequency diagnostic, but supplies no operator inequality used below.  
**Collision check:** v13.969 was absent in the live tree immediately before this write.

---

## 0. Purpose

v13.968 reduces proof-grade certification of the Xi scalar to the constants

\[
\gamma_\pm,\qquad
\sigma_\pm,\qquad
\chi_\pm,
\qquad
r_{P,\pm},r_{Q,\pm},
\]

for protected parity decompositions.

The first target is the stiff-complement floor

\[
\gamma_\pm.
\]

The even parity is compatible with the old certified lineage.

The odd parity requires care because v13.799 corrected the pole sign from

\[
+2dd^T
\]

to

\[
-2dd^T.
\]

The present entry derives new lower bounds for the corrected source-faithful high complements without reinstating the held odd theorem.

---

## 1. Generic two-block lower bound [D]

Let

\[
M=
\begin{pmatrix}
A&G\\
G^*&B
\end{pmatrix}
\]

with

\[
A\succeq aI,
\qquad
B\succeq bI,
\qquad
\|G\|\le c.
\]

For

\[
u=x\oplus y,
\]

\[
\langle Mu,u\rangle
\ge
a\|x\|^2
+b\|y\|^2
-2c\|x\|\|y\|.
\]

Therefore

\[
M
\succeq
\begin{pmatrix}
a&-c\\
-c&b
\end{pmatrix}
\]

at the quadratic-form level in the radial variables.

Hence

\[
\boxed{
M\succeq
\mu(a,b,c) I,
}
\tag{1}
\]

where

\[
\boxed{
\mu(a,b,c)
=
\frac{
a+b-\sqrt{(a-b)^2+4c^2}
}{2}.
}
\tag{2}
\]

---

## 2. Even high-complement floor [D/N-cert]

For the independently certified even-v high-complement lineage, v13.392 gives

\[
A_F\succeq0.22I,
\]

\[
A_T\succeq
4.673332491014484\,I,
\]

and

\[
\|G_{F,T}\|<0.994.
\]

These estimates are for the pole-free high complement.

The actual even pole is

\[
+2cc^T\succeq0,
\]

so adding it cannot lower the spectrum.

Apply (2):

\[
\gamma_+
>
\mu(
0.22,
4.673332491014484,
0.994
).
\]

Numerically,

\[
\boxed{
\gamma_+
>
0.008208009473391176.
}
\tag{3}
\]

For subsequent outward work it is safe to retain

\[
\boxed{
\gamma_+>0.00820.
}
\tag{4}
\]

---

## 3. Odd sign correction and auxiliary operator [D/G]

v13.799 proves the exact odd pole identity

\[
\boxed{
A_{\rm pole}^{(-)}
=
-2dd^T.
}
\tag{5}
\]

The old odd lineage had instead used the auxiliary sign

\[
+2dd^T.
\]

Let

\[
A_{\rm high}^{\rm aux}
\]

denote that old plus-pole auxiliary high operator and

\[
A_{\rm high}^{\rm corr}
\]

the corrected source-faithful high operator.

Because all non-pole source terms are identical,

\[
\boxed{
A_{\rm high}^{\rm corr}
=
A_{\rm high}^{\rm aux}
-
4dd^T.
}
\tag{6}
\]

This identity is exact.

The historical odd theorem remains on HOLD.

The only old inequalities used below are reinterpreted as certified inequalities for the explicitly defined auxiliary operator \(A_{\rm high}^{\rm aux}\), not as statements about the corrected Suzuki operator.

---

## 4. Certified auxiliary odd block floor [D/N-cert]

The old auxiliary plus-pole finite/high/tail certificate provides:

\[
A_F^{\rm aux}\succeq0.53I,
\tag{7}
\]

\[
A_T^{\rm aux}\succeq
2.5810511596134207\,I,
\tag{8}
\]

and

\[
\|G_{F,T}^{\rm aux}\|<1.015.
\tag{9}
\]

Apply (2):

\[
\mu_{\rm odd}^{\rm aux}
>
\mu(
0.53,
2.5810511596134207,
1.015
).
\]

Therefore

\[
\boxed{
A_{\rm high}^{\rm aux}
\succeq
0.11263690952133865\,I.
}
\tag{10}
\]

Again, this is a statement only about the auxiliary plus-pole operator.

---

## 5. Global high-mode norm of the odd pole vector [D]

For even Dirichlet mode number

\[
n\ge22,
\]

write

\[
k_n=\frac{n\pi}{2}.
\]

The exact odd pole vector is

\[
d_n
=
\frac{
2k_n\sinh(1/2)
}{
k_n^2+1/4
}.
\]

Since

\[
k_n^2+\frac14
>
k_n^2,
\]

\[
d_n
<
\frac{
2\sinh(1/2)
}{
k_n
}
=
\frac{
4\sinh(1/2)
}{
\pi n
}.
\tag{11}
\]

Set

\[
n=2m,
\qquad
m\ge11.
\]

Then

\[
d_{2m}^2
<
\frac{
4\sinh^2(1/2)
}{
\pi^2m^2
}.
\]

Therefore

\[
4\|d_{\ge22}\|_2^2
<
\frac{
16\sinh^2(1/2)
}{
\pi^2
}
\sum_{m=11}^\infty
\frac1{m^2}.
\tag{12}
\]

Use

\[
\sum_{m=11}^\infty
\frac1{m^2}
\le
\frac1{11^2}
+
\int_{11}^{\infty}
\frac{dx}{x^2}
=
\frac1{121}
+
\frac1{11}.
\tag{13}
\]

Hence

\[
\boxed{
4\|d_{\ge22}\|_2^2
<
0.04365665274661503.
}
\tag{14}
\]

This includes the entire infinite odd high complement.

---

## 6. Corrected odd high-complement floor [D]

From (6),

\[
A_{\rm high}^{\rm corr}
=
A_{\rm high}^{\rm aux}
-
4dd^T.
\]

Because

\[
\|4dd^T\|
=
4\|d\|^2,
\]

\[
\lambda_{\min}
(
A_{\rm high}^{\rm corr}
)
\ge
\lambda_{\min}
(
A_{\rm high}^{\rm aux}
)
-
4\|d\|^2.
\]

Using (10) and (14),

\[
\lambda_{\min}
(
A_{\rm high}^{\rm corr}
)
>
0.11263690952133865
-
0.04365665274661503.
\]

Thus

\[
\boxed{
\gamma_-
>
0.06898025677472361.
}
\tag{15}
\]

For subsequent outward work it is safe to retain

\[
\boxed{
\gamma_->0.06898.
}
\tag{16}
\]

This is a new source-faithful comparison bound for the corrected negative-pole odd high complement.

---

## 7. Why this does not restore the old odd theorem [G]

v13.799 placed the historical odd/full-parity theorem chain on HOLD.

That status remains unchanged.

The present argument proves only a high-complement coercivity statement.

It does not restore:

- the historical odd frozen-eight low-core theorem;
- the historical normalized residual-Gram estimate;
- the old odd index promotion;
- the dependent full-parity index theorem.

The new derivation uses the old plus-pole certificate only as a bounded auxiliary comparison operator and then pays the entire sign correction by the explicit global rank-one norm (14).

---

## 8. Compatibility with v13.968 [D]

The protected residual contract of v13.968 needs

\[
B_\pm\succeq\gamma_\pm I.
\]

The present entry supplies

\[
\boxed{
\gamma_+>0.00820,
}
\tag{17}
\]

\[
\boxed{
\gamma_->0.06898.
}
\tag{18}
\]

Therefore the stiff-complement part of the Xi phase certificate is closed in both parity channels.

The remaining certification inputs are

\[
\boxed{
\sigma_\pm,\quad
\chi_\pm,\quad
\|r_{P,\pm}\|,\quad
\|r_{Q,\pm}\|.
}
\tag{19}
\]

---

## 9. Relation to the new R-statistic reproducer [I/G]

The newly landed sieve-flow R-statistic pipeline tracks spectral concentration in log-coordinate arithmetic sequences at frequencies

\[
\gamma_j/(2\pi).
\]

This is structurally consonant with the phase-window scalar lane because both emphasize low-height zeta frequencies.

However,

\[
\boxed{
\textbf{the R-statistic supplies no operator lower bound, residual bound, or Weyl-sign enclosure used in this certificate.}
}
\tag{20}
\]

It remains an independent cross-lane diagnostic.

---

## 10. Result

The corrected no-twist Suzuki high complements satisfy

\[
\boxed{
\gamma_+>0.00820,
}
\]

and

\[
\boxed{
\gamma_->0.06898.
}
\]

The odd result follows from

\[
A_{\rm high}^{\rm corr}
=
A_{\rm high}^{\rm aux}
-
4dd^T
\]

and

\[
4\|d_{\ge22}\|^2
<
0.043656653.
\]

Thus the phase-certificate architecture no longer lacks a high-complement floor in either parity.

The next nonredundant gate is the low protected Schur floor and residual budget required to instantiate v13.968.
