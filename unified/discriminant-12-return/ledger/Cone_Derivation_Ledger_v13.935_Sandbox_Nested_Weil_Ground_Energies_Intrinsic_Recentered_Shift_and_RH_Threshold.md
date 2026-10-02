# Cone Derivation Ledger v13.935 — Sandbox: Nested Weil Ground Energies, Intrinsic Ground-Recentered Shift, and the RH Threshold Alignment

**Date:** 2026-10-01  
**Track:** Sandbox / source-faithful Suzuki shift-selection lane  
**Status:** [D] exact nested-ground-energy theorem and canonical recentered branch; [D] RH iff zero threshold alignment; [G] this does not prove RH; [O] uniqueness of the recentered Weyl limit and the regulator-removal limit remain open  
**Authorization:** Jeremy, 2026-10-01 ("cool. lerts push through the next gate")  
**Parents:** v13.274, v13.784, v13.789–794, v13.860, v13.868, v13.927, v13.929, v13.931, v13.933  
**Collision resolution:** This content was first committed under v13.934, but External Audit Round 141 had independently landed v13.934 immediately beforehand. Per the standing earlier-commit-wins rule, the audit keeps v13.934 and this ground-energy/shift-selection entry is renumbered v13.935. Mathematical content is unchanged.

---

## 0. Synchronization

Two recent corrections matter.

1. External Audit Round 140 (v13.930) independently PASSed v13.929's
   \[
   \mathrm{RH}
   \iff
   m_\infty^\Xi \text{ is Herglotz}
   \]
   theorem and the Montel–Vitali RH barrier.

2. v13.933 records that the v13.926 positive-gap claim was a quadrature artifact and reopens v13.910's continuum-if branch. That issue is orthogonal to the present shift-selection theorem.

v13.931 proved:

- every admissible shifted large-\(a\) sequence has Herglotz/Weyl subsequential limits;
- arbitrary large-negative shifts can trivialize the limit to
  \[
  m(z)\equiv i;
  \]
- therefore admissibility alone does not select the arithmetic carrier.

The present gate asks whether the auxiliary shift can be selected intrinsically.

---

## 1. Suzuki's localized forms are nested restrictions [P/D]

Suzuki's localized Weil form is the global Weil quadratic form restricted to functions supported in the finite interval:

\[
\boxed{
Q_W^a
=
Q_W\big|_{L^2(-a,a)}
}
\]

with form core

\[
C_c^\infty(-a,a).
\]

Equivalently, for a compactly supported test function \(f\) with

\[
\operatorname{supp}f\subset(-a,a)\subset(-b,b),
\]

the zero-extension of \(f\) to \((-b,b)\) satisfies

\[
\boxed{
Q_W^b[f]=Q_W^a[f]=Q_W[f].
}
\tag{1}
\]

The \(L^2\) norm is unchanged by zero extension.

Suzuki's lowest spectral point is

\[
\boxed{
\lambda_a
=
\inf_{0\ne f\in C_c^\infty(-a,a)}
\frac{Q_W[f]}{\|f\|_2^2},
}
\tag{2}
\]

using the form-core characterization of the Friedrichs extension \(A_a\).

---

## 2. Ground-energy monotonicity [D]

Let

\[
0<a<b.
\]

Then

\[
C_c^\infty(-a,a)
\subset
C_c^\infty(-b,b).
\]

Taking the infimum of the same Rayleigh quotient over the larger set gives

\[
\boxed{
\lambda_b\le\lambda_a.
}
\tag{3}
\]

Thus

\[
\boxed{
a\mapsto\lambda_a
\text{ is nonincreasing.}
}
\tag{4}
\]

Suzuki separately proves continuity of \(a\mapsto\lambda_a\); monotonicity here comes directly from nested localization.

Therefore the extended-real limit exists:

\[
\boxed{
\lambda_\infty
:=
\lim_{a\to\infty}\lambda_a
=
\inf_{a>0}\lambda_a
\in[-\infty,\infty).
}
\tag{5}
\]

---

## 3. The limit is the global Rayleigh bottom [D]

Because

\[
\bigcup_{a>0}C_c^\infty(-a,a)
=
C_c^\infty(\mathbb R),
\]

equations (2)–(5) give

\[
\boxed{
\lambda_\infty
=
\inf_{0\ne f\in C_c^\infty(\mathbb R)}
\frac{Q_W[f]}{\|f\|_2^2}.
}
\tag{6}
\]

Thus the uniform fixed-shift question is exactly the semiboundedness question for the global Weil form.

If

\[
\lambda_\infty>-\infty,
\]

then every fixed

\[
\lambda_*<\lambda_\infty
\]

is admissible for every \(a\), with the uniform coercivity bound

\[
\boxed{
A_a-\lambda_* I
\ge
(\lambda_\infty-\lambda_*)I.
}
\tag{7}
\]

If

\[
\lambda_\infty=-\infty,
\]

then no fixed real shift is globally admissible.

Hence

\[
\boxed{
\text{a uniform fixed auxiliary shift exists}
\iff
Q_W\text{ is semibounded below on }C_c^\infty(\mathbb R).
}
\tag{8}
\]

This is stronger and sharper than merely observing that the ledger currently lacks an explicit global lower bound.

---

## 4. Intrinsic ground-recentered shift [D]

A fixed global shift is not actually necessary.

For every finite \(a\), the ground energy \(\lambda_a\) is intrinsic spectral data of \(A_a\).

Fix one regulator

\[
\delta>0.
\]

Define

\[
\boxed{
\lambda_{a,\delta}^{\circ}
:=
\lambda_a-\delta.
}
\tag{9}
\]

Then automatically

\[
\lambda_{a,\delta}^{\circ}<\lambda_a,
\]

so Suzuki's finite theory applies for every \(a\).

Define

\[
\boxed{
T_{a,\delta}^{\circ}
:=
A_a-\lambda_{a,\delta}^{\circ}I
=
A_a-\lambda_a I+\delta I.
}
\tag{10}
\]

Since

\[
A_a-\lambda_a I\ge0,
\]

we have the exact uniform coercivity

\[
\boxed{
T_{a,\delta}^{\circ}\ge\delta I
\qquad
\text{for every }a>0.
}
\tag{11}
\]

Thus the entire large-\(a\) shifted branch is now source-faithful and globally admissible with no assumption on RH and no assumed uniform lower bound on \(\lambda_a\).

---

## 5. This removes exactly the additive energy-origin ambiguity [D]

Suppose one changes the finite operator by an arbitrary scalar energy-origin shift

\[
A_a\mapsto A_a+c_a I.
\]

Then

\[
\lambda_a\mapsto\lambda_a+c_a.
\]

Therefore

\[
(A_a+c_aI)-(\lambda_a+c_a)I+\delta I
=
A_a-\lambda_a I+\delta I.
\]

Hence

\[
\boxed{
T_{a,\delta}^{\circ}
\text{ is invariant under }A_a\mapsto A_a+c_aI.
}
\tag{12}
\]

This is exactly the auxiliary ambiguity that v13.931 showed could trivialize the large-\(a\) Weyl limit.

So ground recentering is not merely another chosen shift:

\[
\boxed{
\textbf{it quotients out the additive shift freedom.}
}
\tag{13}
\]

The only remaining parameter is the positive distance \(\delta\) above the spectral floor.

---

## 6. Canonical regulated Weyl family [D]

Define the source-faithful deficiency response

\[
\boxed{
v_{a,\delta}^{\circ}
=
(T_{a,\delta}^{\circ})^{-1}e^x.
}
\tag{14}
\]

Then

\[
\|(T_{a,\delta}^{\circ})^{-1}\|
\le
\frac1\delta.
\tag{15}
\]

Define

\[
F_{a,\delta}^{\circ}(z)
=
\widehat{v_{a,\delta}^{\circ}}(z)
\]

and the canonical quotient

\[
\boxed{
h_{a,\delta}^{\circ}(z)
=
\frac{F_{a,\delta}^{\circ}(z)}
{F_{a,\delta}^{\circ}(-z)}.
}
\tag{16}
\]

For each fixed \(\delta>0\),

\[
\boxed{
h_{a,\delta}^{\circ}\in\mathcal S(\mathbb C_+)
\quad
\text{for every }a.
}
\tag{17}
\]

Therefore

\[
\boxed{
\{h_{a,\delta}^{\circ}:a>0\}
\text{ is a Montel-normal family.}
}
\tag{18}
\]

Every sequence \(a_n\to\infty\) admits a subsequence with

\[
h_{a_{n_k},\delta}^{\circ}\to h_{\infty,\delta}^{\circ}
\]

locally uniformly, and the corresponding Weyl functions converge to a Herglotz limit

\[
m_{\infty,\delta}^{\circ},
\qquad
m_{\infty,\delta}^{\circ}(i)=i.
\]

So v13.931's unconditional compactness is now available on a **single intrinsically selected branch** rather than arbitrary admissible shifts.

What remains open is uniqueness of the subsequential limit.

---

## 7. Threshold behavior of the intrinsic shift [D]

By monotonicity,

\[
\lambda_a\downarrow\lambda_\infty.
\]

Hence for fixed \(\delta>0\),

\[
\boxed{
\lambda_{a,\delta}^{\circ}
=
\lambda_a-\delta
\longrightarrow
\lambda_\infty-\delta
}
\tag{19}
\]

in the extended-real sense.

Thus ground recentering separates the two questions cleanly:

1. **regulated canonical-system question**
   \[
   \delta>0;
   \]

2. **absolute threshold alignment**
   \[
   \delta\downarrow0,
   \qquad
   \lambda_a\to\lambda_\infty.
   \]

The regulator-removal limit approaches the intrinsic global spectral floor

\[
\boxed{
\lambda_\infty,
}
\]

not automatically the absolute value \(0\).

---

## 8. RH implies \(\lambda_\infty=0\) [D]

Assume RH.

By Weil's criterion,

\[
Q_W[f]\ge0
\qquad
(f\in C_c^\infty(\mathbb R)),
\]

so

\[
\lambda_\infty\ge0.
\tag{20}
\]

Under RH, the zero-side representation is a positive discrete sum

\[
Q_W[f]
=
\sum_{\gamma}
m_\gamma
|\widehat f(\gamma)|^2
\]

with real nonzero ordinates \(\gamma\).

Fix a nonzero

\[
\varphi\in C_c^\infty(\mathbb R)
\]

and set

\[
\boxed{
f_R(x)
=
R^{-1/2}\varphi(x/R).
}
\tag{21}
\]

Then

\[
\|f_R\|_2=\|\varphi\|_2,
\]

while

\[
\widehat f_R(\gamma)
=
R^{1/2}\widehat\varphi(R\gamma).
\]

Because \(\widehat\varphi\) is Schwartz, for every \(N\),

\[
|\widehat\varphi(R\gamma)|
\le
C_N(1+R|\gamma|)^{-N}.
\]

Therefore

\[
Q_W[f_R]
\le
C_N^2
R
\sum_{\gamma}
m_\gamma
(1+R|\gamma|)^{-2N}.
\]

Using the Riemann–von Mangoldt zero-counting bound, the sum

\[
\sum_\gamma m_\gamma|\gamma|^{-2N}
\]

converges for sufficiently large \(N\). Hence

\[
\boxed{
Q_W[f_R]\to0
\qquad(R\to\infty).
}
\tag{22}
\]

Since the \(L^2\) norm stays fixed,

\[
\lambda_\infty\le0.
\]

Together with (20),

\[
\boxed{
\mathrm{RH}
\Longrightarrow
\lambda_\infty=0.
}
\tag{23}
\]

---

## 9. Zero threshold implies RH [D]

Conversely, suppose

\[
\lambda_\infty=0.
\]

By (6),

\[
\inf_{0\ne f\in C_c^\infty(\mathbb R)}
\frac{Q_W[f]}{\|f\|_2^2}
=
0.
\]

If there were a test function \(f\) with

\[
Q_W[f]<0,
\]

then its Rayleigh quotient would be a negative number, forcing

\[
\lambda_\infty<0.
\]

Therefore

\[
Q_W[f]\ge0
\qquad
\text{for every }f\in C_c^\infty(\mathbb R).
\]

By Weil's positivity criterion,

\[
\boxed{
\lambda_\infty=0
\Longrightarrow
\mathrm{RH}.
}
\tag{24}
\]

Combining (23) and (24):

\[
\boxed{
\mathrm{RH}
\iff
\lambda_\infty=0.
}
\tag{25}
\]

No simplicity assumption is involved.

If RH is false, then necessarily

\[
\boxed{
\lambda_\infty<0
}
\tag{26}
\]

with \(-\infty\) allowed.

This is an exact scalar ground-energy reformulation of the global Weil criterion.

---

## 10. Meaning for the shift-selection problem [D/I]

The intrinsic regulated shift tends to

\[
\lambda_\infty-\delta.
\]

Therefore the absolute Suzuki \(\lambda=0\) Xi branch aligns with the regulator-free intrinsic threshold exactly when

\[
\lambda_\infty=0.
\]

By (25),

\[
\boxed{
\textbf{the canonical spectral floor aligns with Suzuki's }\lambda=0\textbf{ Xi normalization iff RH.}
}
\tag{27}
\]

This explains why the auxiliary shift problem kept returning at the same logical wall.

The finite theory can remove arbitrary shift freedom unconditionally by subtracting \(\lambda_a\).

What cannot be done unconditionally is assert that the limiting spectral floor itself is \(0\).

That statement is RH.

---

## 11. Under RH the canonical regulated branch approaches fixed shift \(-\delta\) [D]

From (23),

\[
\lambda_a\downarrow0
\]

under RH.

Therefore

\[
\boxed{
\lambda_{a,\delta}^{\circ}
=
\lambda_a-\delta
\longrightarrow
-\delta.
}
\tag{28}
\]

So conditional on RH, the canonical recentered branch becomes asymptotically the ordinary fixed-shift family

\[
A_a+\delta I.
\]

Then the formal regulator removal

\[
\delta\downarrow0
\]

approaches Suzuki's unshifted Xi branch from below.

This gives a non-arbitrary two-step architecture:

\[
\boxed{
\text{first }a\to\infty\text{ at fixed }\delta>0,
\qquad
\text{then }\delta\downarrow0.
}
\tag{29}
\]

The first stage is unconditionally admissible.

The statement that the second stage lands at absolute shift \(0\) is exactly the threshold condition (25).

---

## 12. What this does and does not close

### Closed [D]

1. The localized ground energies are nested:
   \[
   \lambda_b\le\lambda_a\quad(b>a).
   \]

2. Their limit is the global Weil Rayleigh bottom:
   \[
   \lambda_\infty
   =
   \inf Q_W[f]/\|f\|_2^2.
   \]

3. A fixed global shift exists iff the global Weil form is semibounded below.

4. The auxiliary additive shift ambiguity can be removed unconditionally by
   \[
   A_a\mapsto A_a-\lambda_a I.
   \]

5. For every \(\delta>0\),
   \[
   T_{a,\delta}^{\circ}
   =
   A_a-\lambda_a I+\delta I
   \]
   is globally admissible and uniformly coercive.

6. The absolute threshold alignment obeys
   \[
   \mathrm{RH}\iff\lambda_\infty=0.
   \]

### Still open [O]

1. For fixed \(\delta>0\), does
   \[
   h_{a,\delta}^{\circ}
   \]
   have a **unique** large-\(a\) limit, rather than only subsequential limits?

2. What is the spectral type of the resulting \(m_{\infty,\delta}^{\circ}\)?

3. Does the family of unique regulated limits, if established, possess a controlled
   \[
   \delta\downarrow0
   \]
   limit?

4. Can that regulator-free limit be identified with the Xi Weyl target without importing the RH-hard Herglotz property? v13.929 says a direct positive answer would prove RH.

---

## 13. Result

The shift-selection problem is now separated into an unconditional finite normalization and an RH-hard absolute alignment.

The canonical finite normalization is

\[
\boxed{
T_{a,\delta}^{\circ}
=
A_a-\lambda_a I+\delta I.
}
\]

It is:

- source-faithful;
- admissible for every \(a\);
- uniformly coercive;
- invariant under arbitrary additive shifts of the finite energy origin;
- free from the large-negative-shift trivialization mechanism of v13.931.

The only remaining scalar threshold is

\[
\lambda_\infty
=
\lim_{a\to\infty}\lambda_a.
\]

And

\[
\boxed{
\mathrm{RH}
\iff
\lambda_\infty=0.
}
\]

Thus the next genuinely nonredundant gate is no longer "choose \(\lambda\)."

It is:

\[
\boxed{
\textbf{prove uniqueness of the large-}a\textbf{ Weyl/canonical-system limit for the intrinsic regulated family }T_{a,\delta}^{\circ}\textbf{ at fixed }\delta>0.
}
\]

Only after that should the project attack the regulator-removal limit \(\delta\downarrow0\).
