# Cone Derivation Ledger v13.823 — Certified Four-Channel Tail Projector and Two-Mode Low-Core Feshbach Reduction

Date: 2026-09-26.

Lane: A.

Status: [C] exact rank-four tail spectral projector from the nested \(\rho=0.02/0.10\) inertia theorems; [C] exact \(0.08\) spectral moat for the nonresonant tail complement across the inner window; [D] exact two-mode meromorphic Feshbach reduction with at most four nonremovable tail pole channels and positive-semidefinite residues; [N] cross-radius endpoint trial-space diagnostic; [N] N=96 generalized-Ritz sign/location diagnostic; [G] no low-core zero count or \(\kappa_0\) convergence theorem yet.

Parents: v13.801, v13.816, v13.821–822.

Research artifacts:

- research-notes/suzuki_endpoint_rho010_rho002_negative_space_angles.py
  - commit 162d3b2953cf9d0aae530d1243cf30ddc844b2c7

- research-notes/suzuki_four_channel_low_core_feshbach_reduction.md
  - commit 769de81642345238d7b4aaf700d0b0d056daee42

- research-notes/suzuki_tail_generalized_ritz_N96.py
  - commit 79ba2e16ded4760a3c97fac8db16cad3b88cc466

External Audit Round 107 is v13.822 and independently executes/passes the \(\rho=0.02\) theorem and cap program used below.

No GitHub workflow/status run is attached.

## 1. Nested certified window implies an exact spectral projector

Fix one parity sector and write

\[
J_T=B_T^{-1/2}A_TB_T^{-1/2},
\qquad
B_T=B_{{\rm sm},T}>0.
\]

From v13.816 and v13.821,

\[
\operatorname{rank}
\mathbf 1_{(-0.10,0.10)}(J_T)=4,
\]

and

\[
\operatorname{rank}
\mathbf 1_{(-0.02,0.02)}(J_T)=4.
\]

The endpoint kernels at

\[
\delta=\pm0.10,\qquad \delta=\pm0.02
\]

are all zero.

Define

\[
\boxed{
P_4=\mathbf 1_{(-0.02,0.02)}(J_T),
}
\]

and

\[
Q_4=I-P_4.
\]

Then

\[
\boxed{\operatorname{rank}P_4=4}
\]

and, because the larger window contains no additional spectrum,

\[
\boxed{
\sigma(J_T|_{\operatorname{Ran}Q_4})
\cap[-0.10,0.10]
=
\varnothing.
}
\]

Thus the four-channel cluster is now an exact basis-free spectral object.

## 2. Exact nonresonant resolvent moat

For every real

\[
|\delta|\le0.02,
\]

the complementary spectrum is at least \(0.08\) away.  Therefore

\[
\boxed{
\left\|
Q_4(J_T-\delta)^{-1}Q_4
\right\|
<
12.5.
}
\]

At the center,

\[
\boxed{
\|Q_4J_T^{-1}Q_4\|<10.
}
\]

This replaces the old finite-section four-versus-fifth separation by an exact infinite-tail regularity bound.

All infinitely many nonresonant tail modes can therefore contribute only through a uniformly bounded analytic background throughout the certified inner window.

## 3. Restore the two omitted low modes

Restore the first two parity modes and split

\[
\mathcal H
=
\mathcal H_C\oplus\mathcal H_T,
\qquad
\dim\mathcal H_C=2.
\]

For generalized spectral parameter \(\delta\), define

\[
F(\delta)
=
A-\delta B_{\rm sm}.
\]

In block form,

\[
F(\delta)
=
\begin{pmatrix}
F_{CC}(\delta)&F_{CT}(\delta)\\
F_{TC}(\delta)&F_{TT}(\delta)
\end{pmatrix}.
\]

The tail block is

\[
F_{TT}(\delta)
=
B_T^{1/2}
(J_T-\delta)
B_T^{1/2}.
\]

Whenever \(\delta\) is not one of the four cluster eigenvalues,

\[
F_{TT}(\delta)^{-1}
=
B_T^{-1/2}
(J_T-\delta)^{-1}
B_T^{-1/2}.
\]

## 4. Exact two-dimensional Feshbach map

The low-core Schur/Feshbach map is

\[
\boxed{
S_C(\delta)
=
F_{CC}(\delta)
-
F_{CT}(\delta)
F_{TT}(\delta)^{-1}
F_{TC}(\delta).
}
\]

Whenever \(F_{TT}(\delta)\) is invertible,

\[
\boxed{
F(\delta)\text{ invertible}
\iff
S_C(\delta)\text{ invertible}.
}
\]

Moreover,

\[
\boxed{
\dim\ker F(\delta)
=
\dim\ker S_C(\delta).
}
\]

A core null vector \(u\) lifts to the full graph vector

\[
\boxed{
\binom{
u
}{
-F_{TT}(\delta)^{-1}F_{TC}(\delta)u
}.
}
\]

Therefore the full parity problem, away from the four tail poles, is exactly a \(2\times2\) matrix-valued spectral problem.

## 5. Exact four-channel tail resolvent decomposition

Let the distinct cluster eigenvalues be

\[
\delta_1,\ldots,\delta_s,
\qquad
1\le s\le4,
\]

with orthogonal projectors \(P_j\) satisfying

\[
P_4=\sum_{j=1}^{s}P_j,
\]

and

\[
\sum_{j=1}^{s}\operatorname{rank}P_j=4.
\]

Then for

\[
|\delta|<0.10,
\]

away from the \(\delta_j\),

\[
\boxed{
(J_T-\delta)^{-1}
=
\sum_{j=1}^{s}
\frac{P_j}{\delta_j-\delta}
+
R_T(\delta),
}
\]

where

\[
R_T(\delta)
=
Q_4(J_T-\delta)^{-1}Q_4
\]

is analytic throughout the entire larger window.

For the inner window,

\[
\boxed{
\|R_T(\delta)\|<12.5
\qquad
(|\delta|\le0.02).
}
\]

## 6. Four-pole meromorphic low-core normal form

Define

\[
C(\delta)
=
B_T^{-1/2}F_{TC}(\delta).
\]

Then

\[
S_C(\delta)
=
F_{CC}(\delta)
-
C(\delta)^*
(J_T-\delta)^{-1}
C(\delta).
\]

Substitution of the spectral decomposition gives

\[
S_C(\delta)
=
F_{CC}(\delta)
-
C(\delta)^*R_T(\delta)C(\delta)
-
\sum_j
\frac{
C(\delta)^*P_jC(\delta)
}{
\delta_j-\delta
}.
\]

Because \(C(\delta)\) is affine in \(\delta\), the numerator difference

\[
C(\delta)^*P_jC(\delta)
-
C(\delta_j)^*P_jC(\delta_j)
\]

is divisible by

\[
\delta-\delta_j.
\]

Hence all divisible terms can be absorbed into a holomorphic \(2\times2\) background, yielding the exact local/global meromorphic normal form

\[
\boxed{
S_C(\delta)
=
S_{\rm hol}(\delta)
+
\sum_{j=1}^{s}
\frac{R_j}{\delta-\delta_j},
}
\]

where the residue matrices are

\[
\boxed{
R_j
=
C(\delta_j)^*
P_j
C(\delta_j)
\succeq0.
}
\]

Their ranks satisfy

\[
\operatorname{rank}R_j
\le
\min\{
2,\operatorname{rank}P_j
\}.
\]

A nominal tail pole is removable from the core Schur map exactly when the corresponding tail eigenspace is decoupled from the low core.

Thus there are at most four nonremovable tail pole channels in the entire certified \(\pm0.10\) window.

## 7. Uniform analytic-background bound

For

\[
|\delta|\le0.02,
\]

the nonresonant tail term satisfies

\[
\boxed{
\left\|
C(\delta)^*
R_T(\delta)
C(\delta)
\right\|
\le
12.5
\|C(\delta)\|^2.
}
\]

Therefore the only possible singular tail contribution across the inner window is the exact rank-four projector \(P_4\).

The infinite tail has now been reduced to

\[
\boxed{
4\ \text{resonant channels}
+
\text{bounded analytic background}.
}
\]

## 8. Exact source-resolvent factorization

For a source

\[
f=
\binom{f_C}{f_T},
\]

define

\[
g_C(\delta)
=
f_C
-
F_{CT}(\delta)
F_{TT}(\delta)^{-1}
f_T.
\]

Whenever both blocks are invertible,

\[
\boxed{
\langle f,F(\delta)^{-1}f\rangle
=
\langle f_T,F_{TT}(\delta)^{-1}f_T\rangle
+
\langle
g_C(\delta),
S_C(\delta)^{-1}g_C(\delta)
\rangle.
}
\]

The tail-source term itself decomposes as

\[
\boxed{
\langle f_T,F_{TT}(\delta)^{-1}f_T\rangle
=
\sum_j
\frac{
\|P_jB_T^{-1/2}f_T\|^2
}{
\delta_j-\delta
}
+
h_{\rm reg}(\delta),
}
\]

with \(h_{\rm reg}\) analytic on \(|\delta|<0.10\).

This rigorously formalizes the v13.801 numerical two-stage amplification:

\[
\boxed{
\text{four tail channels}
\longrightarrow
\text{two-mode low-core response}.
}
\]

## 9. Endpoint trial bases are not canonical resonance coordinates [N]

The frozen negative endpoint eigenspaces at \(\rho=0.10\) and \(\rho=0.02\) were compared directly in ordinary coefficient-space geometry.

The principal angles are approximately

even-v:

\[
\boxed{
0.00185^\circ,\ 
0.01529^\circ,\ 
0.39922^\circ,\ 
36.93593^\circ,
}
\]

odd-v:

\[
\boxed{
0.00070^\circ,\ 
0.00449^\circ,\ 
0.09716^\circ,\ 
2.24905^\circ.
}
\]

Thus one even-v endpoint trial direction rotates strongly as the endpoint radius changes.

This is not a contradiction: both bases are only inertia witnesses.

The canonical resonance object is \(P_4\), not either endpoint negative basis.

Any future four-channel numerical reduction should therefore either use \(P_4\) directly or separately certify an approximate basis by a residual/gap theorem.

## 10. N=96 generalized-Ritz handoff [N]

Rewriting the v13.801 normalized interaction eigenvalues as the generalized tail eigenvalues

\[
\delta=1+\mu,
\]

the \(N=96\) finite-section values closest to zero are:

even-v:

\[
\boxed{
9.1\times10^{-16},\
2.2098\times10^{-12},\
8.5207\times10^{-8},\
3.5635\times10^{-4},
}
\]

with fifth value

\[
\boxed{
0.1505554.
}
\]

odd-v:

\[
\boxed{
4.96\times10^{-15},\
2.7334\times10^{-10},\
4.9485\times10^{-6},\
1.26997\times10^{-2},
}
\]

with fifth value

\[
\boxed{
0.2883123.
}
\]

Thus the finite Ritz cluster lies on the positive side at \(N=96\).

This is only a finite-section sign diagnostic.

No theorem that the four infinite \(\delta_j\) are positive is promoted.

## 11. Strategic consequence

The tail multiplicity problem is closed.

The unstable raw protected-rank question from v13.800 should no longer be revisited.

The active problem is now the two-dimensional meromorphic function

\[
S_C(\delta),
\]

fed by an exact four-dimensional tail projector.

The next gates are:

1. construct a residual-certified approximation to \(\operatorname{Ran}P_4\) using the exact \(0.08\) moat;
2. evaluate the grouped or individual residue matrices \(R_j\);
3. quantify the bounded analytic background;
4. replay the \(2\times2\) determinant/source response in \(|\delta|\le0.02\);
5. determine whether the four certified tail eigenvalues can be proven positive;
6. only after the low-core structure stabilizes revisit \(\kappa_0\) convergence and \(\kappa_1\).

## Guardrails

No claim is made here that:

- the endpoint negative trial bases equal the resonance subspace;
- the four infinite tail eigenvalues are positive;
- the low-core Schur determinant has any particular zero count;
- \(\kappa_0\) has converged;
- \(\kappa_1\) is unblocked;
- RH or GRH follows.

## Result

The nested certified endpoint theorems yield the exact operator reduction

\[
\boxed{
\operatorname{rank}P_4=4,
\qquad
\|Q_4(J_T-\delta)^{-1}Q_4\|<12.5
\quad(|\delta|\le0.02),
}
\]

and the full parity problem away from the four tail poles is exactly equivalent to a

\[
\boxed{
2\times2
}
\]

meromorphic Feshbach map with at most four nonremovable positive-semidefinite pole residues.

The next unresolved object is no longer the tail multiplicity; it is the two-mode low-core response.
