# Four-Channel Tail Projector and Two-Mode Low-Core Feshbach Reduction

Lane A research note following the certified \(\rho=0.02\) and \(\rho=0.10\) parity-tail inertia theorems.

Status: analytic consequence of the certified tail spectrum; no claim about the separate low-core zero set, \(\kappa_0\) convergence, or RH/GRH.

## 1. Certified tail spectral moat

Fix one parity sector and write the positive smooth tail metric as

\[
B_T=B_{{\rm sm},T}>0,
\]

and the tail generalized operator as

\[
J_T=B_T^{-1/2}A_TB_T^{-1/2}.
\]

The certified endpoint theorems give

\[
\operatorname{rank}\mathbf 1_{(-0.02,0.02)}(J_T)=4,
\]

and

\[
\operatorname{rank}\mathbf 1_{(-0.10,0.10)}(J_T)=4.
\]

The four endpoint pencils at \(\pm0.02,\pm0.10\) have zero kernel.

Hence, with

\[
P_4=\mathbf 1_{(-0.02,0.02)}(J_T),
\qquad
Q_4=I-P_4,
\]

one has

\[
\boxed{\operatorname{rank}P_4=4}
\]

and

\[
\boxed{
\sigma(J_T|_{\operatorname{Ran}Q_4})\cap[-0.10,0.10]
=
\varnothing.
}
\]

In particular, for every real \(\delta\) with \(|\delta|\le0.02\),

\[
\boxed{
\left\|
Q_4(J_T-\delta)^{-1}Q_4
\right\|
<
\frac1{0.10-0.02}
=
12.5.
}
\]

At \(\delta=0\),

\[
\left\|Q_4J_T^{-1}Q_4\right\|<10.
\]

Thus the nonresonant tail complement is uniformly regular across the entire certified inner window.

## 2. Low-core / tail block pencil

Restore the two parity modes omitted from the certified tail theorem and split

\[
\mathcal H
=
\mathcal H_C\oplus\mathcal H_T,
\qquad
\dim\mathcal H_C=2.
\]

For the generalized spectral parameter \(\delta\), define

\[
F(\delta)=A-\delta B_{\rm sm}.
\]

Write

\[
F(\delta)
=
\begin{pmatrix}
F_{CC}(\delta)&F_{CT}(\delta)\\
F_{TC}(\delta)&F_{TT}(\delta)
\end{pmatrix}.
\]

On the tail,

\[
F_{TT}(\delta)
=
B_T^{1/2}(J_T-\delta)B_T^{1/2}.
\]

Therefore, whenever \(\delta\) is not one of the four certified tail eigenvalues,

\[
F_{TT}(\delta)^{-1}
=
B_T^{-1/2}(J_T-\delta)^{-1}B_T^{-1/2}.
\]

The exact two-dimensional Feshbach/Schur map is

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

Whenever the tail block is invertible,

\[
F(\delta)\text{ is invertible}
\iff
S_C(\delta)\text{ is invertible},
\]

and

\[
\dim\ker F(\delta)
=
\dim\ker S_C(\delta).
\]

The full kernel vector is reconstructed from a core vector \(u\in\ker S_C(\delta)\) by

\[
\binom{u}{
-F_{TT}(\delta)^{-1}F_{TC}(\delta)u
}.
\]

Thus every non-tail-pole spectral question in the full parity problem is reduced exactly to a \(2\times2\) matrix-valued function.

## 3. Exact four-channel tail resolvent decomposition

Let the distinct tail eigenvalues in \((-0.02,0.02)\) be

\[
\delta_1,\ldots,\delta_s,
\qquad
1\le s\le4,
\]

with orthogonal spectral projectors \(P_j\) satisfying

\[
\sum_{j=1}^s\operatorname{rank}P_j=4,
\qquad
P_4=\sum_{j=1}^sP_j.
\]

Then throughout the larger window \(|\delta|<0.10\), away from these eigenvalues,

\[
\boxed{
(J_T-\delta)^{-1}
=
\sum_{j=1}^s
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

is analytic on \(|\delta|<0.10\).

For \(|\delta|\le0.02\),

\[
\boxed{\|R_T(\delta)\|<12.5.}
\]

This is the basis-free replacement for the old finite-section "four closest modes" construction.

## 4. Four-channel meromorphic two-mode Schur map

Define the normalized tail-to-core coupling

\[
C(\delta)
=
B_T^{-1/2}F_{TC}(\delta):
\mathcal H_C\to\mathcal H_T.
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

Substituting the certified spectral decomposition gives

\[
S_C(\delta)
=
F_{CC}(\delta)
-
C(\delta)^*R_T(\delta)C(\delta)
-
\sum_{j=1}^s
\frac{
C(\delta)^*P_jC(\delta)
}{
\delta_j-\delta
}.
\]

Since \(C(\delta)\) is affine in \(\delta\), each numerator is analytic.  Expanding at \(\delta_j\) and absorbing the divisible remainder into the holomorphic part yields the exact meromorphic normal form

\[
\boxed{
S_C(\delta)
=
S_{\rm hol}(\delta)
+
\sum_{j=1}^s
\frac{R_j}{\delta-\delta_j},
}
\]

where

\[
\boxed{
R_j
=
C(\delta_j)^*P_jC(\delta_j)
\succeq0.
}
\]

Moreover

\[
\operatorname{rank}R_j
\le
\min\{2,\operatorname{rank}P_j\},
\]

and

\[
\sum_j\operatorname{rank}P_j=4.
\]

A pole is removable exactly when the corresponding tail eigenspace is decoupled from the two-mode core.

Thus the low-core problem has at most four nonremovable tail pole channels in the entire certified \(\pm0.10\) window.

## 5. Uniform bound on the analytic tail background

For \(|\delta|\le0.02\),

\[
\left\|
C(\delta)^*R_T(\delta)C(\delta)
\right\|
\le
12.5\,\|C(\delta)\|^2.
\]

Hence the only potentially singular tail contribution in the inner window is the certified four-dimensional projector \(P_4\).

All remaining infinitely many tail modes enter through a uniformly bounded analytic \(2\times2\) correction.

This is the exact operator-level version of the v13.801 numerical observation

\[
\text{smooth bulk}
\longrightarrow
\text{four tail resonances}
\longrightarrow
\text{two-mode core}.
\]

## 6. Source-resolvent decomposition

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

Whenever \(F_{TT}(\delta)\) and \(S_C(\delta)\) are invertible,

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

The tail-source term has the exact decomposition

\[
\langle f_T,F_{TT}(\delta)^{-1}f_T\rangle
=
\sum_{j=1}^s
\frac{
\|P_jB_T^{-1/2}f_T\|^2
}{
\delta_j-\delta
}
+
h_{\rm reg}(\delta),
\]

where \(h_{\rm reg}\) is analytic on \(|\delta|<0.10\).

Thus the previously observed huge source-resolvent amplification has an exact structural route:

\[
\boxed{
\text{four certified tail channels}
\quad+\quad
\text{a }2\times2\text{ meromorphic low-core response}.
}
\]

This does not yet prove convergence of the scalar \(\kappa_0\).

## 7. Cross-radius endpoint trial-space caution

The frozen negative endpoint trial spaces at \(\rho=0.10\) and \(\rho=0.02\) are inertia witnesses, not the canonical spectral projector.

A direct ordinary coefficient-space comparison gives principal angles approximately

even-v:
\[
0.00185^\circ,\quad
0.01529^\circ,\quad
0.39922^\circ,\quad
36.93593^\circ,
\]

odd-v:
\[
0.00070^\circ,\quad
0.00449^\circ,\quad
0.09716^\circ,\quad
2.24905^\circ.
\]

In particular, one even-v endpoint trial direction rotates strongly with radius.

Therefore subsequent reduced models must be formulated using the basis-free spectral projector \(P_4\), or a separately residual-certified approximation to it, rather than identifying either frozen endpoint negative basis with the resonance basis.

## 8. Next gates

The tail spectral multiplicity question is now closed.

The next unresolved object is the two-mode meromorphic Schur map \(S_C(\delta)\).

The natural gates are:

1. obtain a residual-certified numerical basis for \(\operatorname{Ran}P_4\) using the \(0.08\) moat;
2. evaluate the four residue matrices \(R_j\), or grouped cluster residues if eigenvalues are not individually separated;
3. isolate the bounded analytic background using the \(12.5\) resolvent bound;
4. replay the \(2\times2\) low-core determinant/source response across \(|\delta|\le0.02\);
5. only then revisit \(\kappa_0\) convergence and unblock any \(\kappa_1\) work.

## Result

The certified nested endpoint counts imply an exact four-channel Fredholm/Feshbach reduction:

\[
\boxed{
\operatorname{rank}P_4=4,
\qquad
\|Q_4(J_T-\delta)^{-1}Q_4\|<12.5
\ \ (|\delta|\le0.02),
}
\]

and the full parity problem away from the four tail poles is exactly equivalent to a \(2\times2\) meromorphic Schur map with positive-semidefinite pole residues.

No low-core zero count, \(\kappa_0\) convergence theorem, \(\kappa_1\) theorem, RH, or GRH claim is made.
