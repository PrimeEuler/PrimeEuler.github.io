# Cone Derivation Ledger v13.960 — Sandbox: Critical-Shape Compactness at the Physical Crossing and Exact Stieltjes Representation

**Date:** 2026-10-02  
**Track:** Sandbox / untwisted Suzuki source-RG and critical-shape lane  
**Status:** [D] unconditional subsequential compactness of the physical crossover shape after scaling by the intrinsic crossing; [D] exact probability-measure/Stieltjes representation; [D] multiplicative Harnack control; [G] this closes shape precompactness but not the absolute location \(N_a\delta_\tau(a)\) or uniqueness of the shape limit; [O] identify the limit and prove source-RG location convergence  
**Authorization:** Jeremy, 2026-10-02 ("lets try and get those closed!")  
**Parents:** v13.956, v13.958–959  
**Collision check:** v13.960 was absent in the live tree immediately before this write.

---

## 0. Purpose

v13.958 separates the physical double-scaling problem into two pieces:

1. the **location** of the critical window,
   \[
   c_{a,\tau}:=N_a\delta_\tau(a),
   \qquad
   N_a=e^{2a},
   \]
2. the **shape** of the source-resolvent crossover inside that window.

The first piece remains operator-specific.

The second piece can be closed much further with no new spectral assumption.

Let

\[
\delta_a:=\delta_\tau(a)
\]

be the intrinsic first crossing defined by

\[
\frac{G_{a,-}(\delta_a)}{G_{a,+}(\delta_a)}
=
q_\tau,
\qquad
q_\tau=\tanh(\tau/2).
\]

Define the physical critical-shape ratio

\[
\boxed{
\Psi_a(s)
=
\frac{
G_{a,-}(s\delta_a)
}{
G_{a,+}(s\delta_a)
},
\qquad
s>0.
}
\tag{1}
\]

Then

\[
\boxed{
\Psi_a(1)=q_\tau
}
\tag{2}
\]

exactly.

The present entry proves that \(\{\Psi_a\}\) is locally uniformly precompact on \((0,\infty)\), and identifies every subsequential limit explicitly as a ratio of two normalized Stieltjes transforms.

No \(N^{-1}\) assumption is used.

---

## 1. Positive parity source measures [D]

Let

\[
d\sigma_{a,+},
\qquad
d\sigma_{a,-}
\]

be the positive even/odd source spectral measures of v13.956.

Then

\[
\boxed{
G_{a,\pm}(\delta)
=
\int_{[0,\infty)}
\frac{
d\sigma_{a,\pm}(\lambda)
}{
\lambda+\delta
},
\qquad
\delta>0.
}
\tag{3}
\]

At the intrinsic critical point,

\[
G_{a,+}(\delta_a)>0,
\qquad
G_{a,-}(\delta_a)>0,
\]

and

\[
G_{a,-}(\delta_a)
=
q_\tau G_{a,+}(\delta_a).
\]

---

## 2. Critical resolvent-weighted probability measures [D]

For each parity define a probability measure on the one-point compactification

\[
[0,\infty]
\]

by

\[
\boxed{
d\nu_{a,\pm}(u)
=
\frac1{
G_{a,\pm}(\delta_a)
}
\frac{
d\sigma_{a,\pm}(\lambda)
}{
\lambda+\delta_a
},
\qquad
u=\frac{\lambda}{\delta_a}.
}
\tag{4}
\]

More explicitly, for a Borel set \(S\subset[0,\infty)\),

\[
\nu_{a,\pm}(S)
=
\frac1{
G_{a,\pm}(\delta_a)
}
\int_{\lambda/\delta_a\in S}
\frac{
d\sigma_{a,\pm}(\lambda)
}{
\lambda+\delta_a
}.
\]

Because

\[
\int
\frac{
d\sigma_{a,\pm}(\lambda)
}{
\lambda+\delta_a
}
=
G_{a,\pm}(\delta_a),
\]

we have

\[
\boxed{
\nu_{a,\pm}([0,\infty])=1.
}
\tag{5}
\]

No tightness on \([0,\infty)\) is needed for compactness because the one-point compactification is compact.

---

## 3. Exact normalized Stieltjes shape [D]

For \(s>0\),

\[
\begin{aligned}
\frac{
G_{a,\pm}(s\delta_a)
}{
G_{a,\pm}(\delta_a)
}
&=
\frac{
\int
(\lambda+s\delta_a)^{-1}
d\sigma_{a,\pm}(\lambda)
}{
G_{a,\pm}(\delta_a)
}\\
&=
\int
\frac{
\lambda+\delta_a
}{
\lambda+s\delta_a
}
d\nu_{a,\pm}.
\end{aligned}
\]

Writing

\[
u=\frac{\lambda}{\delta_a},
\]

gives the exact formula

\[
\boxed{
H_{a,\pm}(s)
:=
\frac{
G_{a,\pm}(s\delta_a)
}{
G_{a,\pm}(\delta_a)
}
=
\int_{[0,\infty]}
\frac{
u+1
}{
u+s
}
\,d\nu_{a,\pm}(u).
}
\tag{6}
\]

At \(u=\infty\), the kernel is interpreted continuously as

\[
\frac{\infty+1}{\infty+s}=1.
\]

Thus the possible escape of spectral mass to infinite scaled energy is already incorporated in the compactified representation.

---

## 4. Exact crossover-shape representation [D]

Using

\[
G_{a,-}(\delta_a)
=
q_\tau G_{a,+}(\delta_a),
\]

we obtain

\[
\boxed{
\Psi_a(s)
=
q_\tau
\frac{
H_{a,-}(s)
}{
H_{a,+}(s)
}.
}
\tag{7}
\]

Therefore

\[
\boxed{
\Psi_a(s)
=
q_\tau
\frac{
\displaystyle
\int
\frac{u+1}{u+s}
d\nu_{a,-}(u)
}{
\displaystyle
\int
\frac{u+1}{u+s}
d\nu_{a,+}(u)
}.
}
\tag{8}
\]

This is the exact dimensionless physical crossover shape.

---

## 5. Uniform scale-Harnack bounds [D]

Fix

\[
0<d<c.
\]

For every \(u\ge0\),

\[
\frac dc
\le
\frac{u+d}{u+c}
\le1.
\]

Equivalently,

\[
\frac dc
\le
\frac{
(u+1)/(u+c)
}{
(u+1)/(u+d)
}
\le1.
\]

Integrating against any positive probability measure gives

\[
\boxed{
\frac dc
\le
\frac{
H_{a,\pm}(c)
}{
H_{a,\pm}(d)
}
\le1.
}
\tag{9}
\]

Therefore

\[
\boxed{
\frac dc
\le
\frac{
\Psi_a(c)
}{
\Psi_a(d)
}
\le
\frac cd.
}
\tag{10}
\]

Taking logarithms,

\[
\boxed{
\left|
\log\Psi_a(c)
-
\log\Psi_a(d)
\right|
\le
\left|
\log c-\log d
\right|
}
\tag{11}
\]

whenever the ratio is finite and positive.

Thus in logarithmic scale,

\[
\log\Psi_a(e^t)
\]

is uniformly \(1\)-Lipschitz.

In particular, because

\[
\Psi_a(1)=q_\tau,
\]

on every compact interval

\[
0<\alpha\le s\le\beta<\infty,
\]

\[
\boxed{
q_\tau\min(\alpha,\beta^{-1})
\le
\Psi_a(s)
\le
q_\tau\max(\alpha^{-1},\beta).
}
\tag{12}
\]

So both collapse and blowup are uniformly excluded on compact \(s\)-intervals after scaling by the physical crossing.

---

## 6. Subsequence compactness of the critical measures [D]

The space of Borel probability measures on

\[
[0,\infty]
\]

is weak-* compact.

Therefore every sequence

\[
a_n\to\infty
\]

contains a subsequence, not relabeled, such that

\[
\boxed{
\nu_{a_n,+}
\Longrightarrow
\nu_+,
\qquad
\nu_{a_n,-}
\Longrightarrow
\nu_-.
}
\tag{13}
\]

For every compact \(K\Subset(0,\infty)\), the kernel

\[
K_s(u)
=
\frac{u+1}{u+s}
\]

is jointly continuous and uniformly bounded on

\[
[0,\infty]\times K.
\]

Hence weak convergence gives

\[
\boxed{
H_{a_n,\pm}(s)
\longrightarrow
H_\pm(s)
:=
\int
\frac{u+1}{u+s}
d\nu_\pm(u)
}
\tag{14}
\]

uniformly for \(s\in K\).

---

## 7. Local-uniform critical-shape compactness [D]

Combining (7) and (14),

\[
\boxed{
\Psi_{a_n}(s)
\longrightarrow
\Psi_\infty(s)
}
\tag{15}
\]

locally uniformly on \((0,\infty)\), where

\[
\boxed{
\Psi_\infty(s)
=
q_\tau
\frac{
\displaystyle
\int
\frac{u+1}{u+s}
d\nu_-(u)
}{
\displaystyle
\int
\frac{u+1}{u+s}
d\nu_+(u)
}.
}
\tag{16}
\]

The denominator is strictly positive for every \(s>0\).

Also

\[
\boxed{
\Psi_\infty(1)=q_\tau.
}
\tag{17}
\]

Thus the physical crossover shape is automatically subsequentially compact after scaling by its own critical regulator.

---

## 8. No separate noncollapse theorem is needed for shape [D/I]

Before this entry, one possible concern was that the parity capacities might collapse too quickly to leave a meaningful dimensionless profile.

Equation (12) shows this cannot happen after normalization at the physical crossing.

On every compact \(s\)-interval,

\[
\Psi_a(s)
\]

is uniformly bounded above and below by positive constants depending only on \(\tau\) and the interval.

Therefore:

\[
\boxed{
\textbf{critical-shape noncollapse is automatic.}
}
\tag{18}
\]

What remains unresolved is the **absolute location** of the critical scale relative to the cone/sieve variable \(N_a\).

---

## 9. Relation to the critical matrix state [D]

v13.956 defines the matrix-valued critical state

\[
d\Pi_{a,\tau}(\lambda)
=
\frac1{R_a(\delta_a)}
\frac{
d\Sigma_a(\lambda)
}{
\lambda+\delta_a
}.
\]

In the parity basis, its two diagonal components are proportional to

\[
d\nu_{a,+},
\qquad
d\nu_{a,-}.
\]

Thus the present probability measures are exactly the normalized parity components of the v13.956 critical matrix state.

Consequently the subsequential shape limit in (16) is not a new auxiliary object.

It is the scalar parity-ratio observable of the critical matrix-state limit.

---

## 10. Tightness on \([0,\infty)\) vs compactified convergence [G]

Mass at

\[
u=\infty
\]

is allowed in \(\nu_\pm\).

If

\[
\nu_\pm(\{\infty\})>0,
\]

that part contributes the constant \(1\) to \(H_\pm(s)\).

Therefore compactified critical-shape convergence does **not** require the no-escape condition of v13.956.

Tightness on the ordinary half-line remains relevant only if one wants the limiting measure to encode a genuine finite scaled-energy distribution.

So two different questions must be kept separate:

\[
\boxed{
\text{shape convergence on }s>0
}
\]

is compact without tightness, whereas

\[
\boxed{
\text{finite-energy measure interpretation}
}
\]

requires no mass at \(u=\infty\).

---

## 11. Uniqueness criterion [C]

The shape limit is unique if and only if every subsequential pair

\[
(\nu_+,\nu_-)
\]

produces the same ratio

\[
\frac{
\int (u+1)(u+s)^{-1}d\nu_-
}{
\int (u+1)(u+s)^{-1}d\nu_+
}
\]

for all \(s>0\).

A sufficient condition is uniqueness of each limiting critical parity measure:

\[
\boxed{
\nu_{a,\pm}\Longrightarrow\nu_\pm
}
\tag{Huniq}
\]

without passing to subsequences.

A weaker sufficient condition is uniqueness only of the ratio of their normalized Stieltjes transforms.

No isolated eigenvalue assumption is required.

---

## 12. Location and shape are now rigorously separated [D/I]

The physical source-RG problem has two independent coordinates:

### Location

\[
\boxed{
c_{a,\tau}
=
N_a\delta_\tau(a).
}
\]

v13.958 shows this is not fixed by the universal source matrix alone.

### Shape

\[
\boxed{
\Psi_a(s)
=
\frac{
G_{a,-}(s\delta_\tau)
}{
G_{a,+}(s\delta_\tau)
}.
}
\]

The present entry proves subsequential local-uniform compactness and noncollapse of this shape unconditionally.

Therefore the unresolved physical theorem has been reduced to:

1. prove the absolute location \(c_{a,\tau}\) converges;
2. prove uniqueness of the normalized critical parity measures or of their Stieltjes-ratio limit.

---

## 13. Result

At the intrinsic physical crossing, define

\[
\Psi_a(s)
=
\frac{
G_{a,-}(s\delta_\tau)
}{
G_{a,+}(s\delta_\tau)
}.
\]

Then

\[
\boxed{
\Psi_a(1)=q_\tau
}
\]

and

\[
\boxed{
\frac dc
\le
\frac{
\Psi_a(c)
}{
\Psi_a(d)
}
\le
\frac cd
}
\qquad(c>d>0).
\]

Every sequence \(a_n\to\infty\) has a subsequence for which

\[
\boxed{
\Psi_{a_n}
\to
\Psi_\infty
}
\]

locally uniformly on \((0,\infty)\), with

\[
\boxed{
\Psi_\infty(s)
=
q_\tau
\frac{
\displaystyle
\int
\frac{u+1}{u+s}d\nu_-(u)
}{
\displaystyle
\int
\frac{u+1}{u+s}d\nu_+(u)
}.
}
\]

Thus critical-shape noncollapse and subsequential convergence are closed.

The remaining hard problems are absolute \(N^{-1}\) location and uniqueness of the source-RG fixed-point shape.
