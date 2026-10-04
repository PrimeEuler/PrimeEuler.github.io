# Cone Derivation Ledger v13.992 — Remote-Moment/Re-Ritz Compatibility Gate and Finite-Shell Obstruction

**Date:** 2026-10-03  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact diagnosis of why the v13.990 fixed-\(\theta\) moment cancellation does not survive re-Ritz; [D] subspace-invariant nonlinear moment condition; [N] successful self-consistent cancellation after re-Ritz; [N] finite-shell and constrained-graph realizations fail the low-residual carrier gate; [G] do not rebuild KKT/Feshbach on these corrected carriers.  
**Parents:** v13.987–991.  
**Research commits:** 99fbce44bdbb600a55f5c561088c139470298098, f3171abed94cacfe0e0d11939f88855a0e2259a2, a3db527be519704bfe2a2fe78028e641366eb954.  
**Workflow commits:** 073cc5c606b5c290ec6581e117386e1862c7c0ad, fe3c29479289b3d01e2b19c00bf0ffe043b275fa, a46ec9b8a91b56950cc22ff10097d68c486cdd5d.  
**Collision check:** immediately before this write, live HEAD was a46ec9b8a91b56950cc22ff10097d68c486cdd5d; no v13.992 ledger entry was present.

---

## 0. Purpose

v13.990 constructs a finite remote-shell correction that cancels the exact signed \(1/n\) residual moment at a fixed Ritz value \(\theta\),

\[
\mathcal L_\theta(q+y)=0.
\]

v13.996 showed that this moment dominates more than \(99.7\%\) of the certified far-tail bound for the M3 carrier.

The unresolved question was whether that cancellation is compatible with the operations required to produce a proof-grade four-dimensional carrier:

1. \(B\)-orthonormalization;
2. Rayleigh–Ritz recomputation;
3. low finite residual;
4. retention of all four Ritz values inside \((-0.02,0.02)\).

The answer is mixed:

\[
\boxed{
\text{the moment can be cancelled exactly and invariantly, but the tested finite-shell realizations are too expensive in the local residual.}
}
\]

---

## 1. Naive fixed-\(\theta\) cancellation does not survive re-Ritz [N]

The first replay reconstructed the v13.996 M3 carrier and appended the v13.990 constant finite shell through

\[
M_4=
\begin{cases}
32001,&\text{even},\\
32002,&\text{odd}.
\end{cases}
\]

Before re-Ritz, cancellation is exact to roundoff.

Even:

\[
\|\mathcal L_{\Theta_3}(X_4)\|_2
=
2.57\times10^{-15}.
\]

Odd:

\[
\|\mathcal L_{\Theta_3}(X_4)\|_2
=
8.29\times10^{-15}.
\]

After \(B\)-orthonormalization and re-Ritzing, however,

\[
\Theta_3\mapsto\Theta_4,
\]

and the leading moment returns:

\[
\boxed{
\|\mathcal L_{\Theta_4}(Z_4)\|_2
=
1.33015\times10^{-3}
\quad\text{(even)},
}
\]

\[
\boxed{
\|\mathcal L_{\Theta_4}(Z_4)\|_2
=
2.93895\times10^{-2}
\quad\text{(odd)}.
}
\]

Thus fixed-\(\theta\) cancellation is not itself a subspace property.

The carrier quality also deteriorates badly.

Even transformed residual:

\[
0.0258747
\longrightarrow
0.748805.
\]

Odd transformed residual:

\[
0.0267740
\longrightarrow
0.757777.
\]

The far-tail bounds improve sharply,

\[
2.39393\times10^{-4}
\to
1.11191\times10^{-5}
\]

even, and

\[
1.23137\times10^{-3}
\to
6.82379\times10^{-5}
\]

odd, but that gain is overwhelmed by the finite residual.

The top odd Ritz value also exits the certified inner window:

\[
0.0103757
\longrightarrow
0.0239451>0.02.
\]

Therefore the naive v13.990 finite-shell carrier must not be used for a fresh KKT/Feshbach payload.

---

## 2. Subspace-invariant moment condition [D]

Let

\[
X\in\mathbb R^{N\times4}
\]

be any full-rank carrier basis.

Define

\[
G(X)=X^TBX,
\qquad
H(X)=X^TAX,
\]

and the reduced operator

\[
\boxed{
T(X)=G(X)^{-1}H(X).
}
\tag{1}
\]

Let \(\ell^T\) be the row functional supplying the \(A\)-side leading remote coefficient. The full leading \(1/n\) residual row is

\[
\boxed{
\mathscr L(X)
=
\ell^T X
+
(\mathbf 1^TX)\,T(X).
}
\tag{2}
\]

For a Ritz basis, \(T=\Theta\), and (2) reduces columnwise to the v13.996/v13.990 \(\mathcal L_{\theta_j}\).

Under an invertible basis change \(X\mapsto XV\),

\[
G(XV)=V^TG(X)V,
\qquad
H(XV)=V^TH(X)V,
\]

so

\[
T(XV)=V^{-1}T(X)V.
\]

Therefore

\[
\boxed{
\mathscr L(XV)=\mathscr L(X)V.
}
\tag{3}
\]

Consequently,

\[
\boxed{
\mathscr L(X)=0
}
\tag{4}
\]

is a subspace-invariant condition.

If a span satisfies (4), every later \(B\)-orthonormalization and Rayleigh–Ritz rotation of that same span also has zero leading moment.

This is the correct invariant formulation of the v13.990 idea.

---

## 3. Self-consistent constant-shell solve closes the invariant moment equation [N]

Restrict the corrected span to

\[
X(c)
=
\begin{pmatrix}
Z_3\\
\mathbf1\,c^T
\end{pmatrix},
\qquad
c\in\mathbb R^4.
\]

Solving

\[
\boxed{
\mathscr L(X(c))=0
}
\tag{5}
\]

converged in both parity sectors.

### Even

The root solver converged in 10 function evaluations.

\[
c_e\approx
(
2.4737\times10^{-11},
-1.0241\times10^{-8},
-1.9373\times10^{-6},
-1.19276\times10^{-4}
).
\]

The root residual is

\[
\|\mathscr L(X(c_e))\|_2
=
1.78\times10^{-18}.
\]

After re-Ritz,

\[
\boxed{
\|\mathcal L_{\Theta_4}(Z_4)\|_2
=
5.81\times10^{-16}.
}
\]

### Odd

The root solver converged in 21 function evaluations.

\[
c_o\approx
(
-4.7753\times10^{-10},
-1.1401\times10^{-7},
-1.4448\times10^{-5},
-6.12320\times10^{-4}
).
\]

The root residual is

\[
\|\mathscr L(X(c_o))\|_2
=
9.72\times10^{-17}.
\]

After re-Ritz,

\[
\boxed{
\|\mathcal L_{\Theta_4}(Z_4)\|_2
=
9.43\times10^{-15}.
}
\]

Thus the subspace-invariant formulation works exactly as intended.

---

## 4. Constant-shell realization fails the carrier-quality gate [N/G]

Despite exact moment closure,

\[
\boxed{
\rho_{e,M4}\approx0.746757,
}
\]

\[
\boxed{
\rho_{o,M4}\approx0.749187.
}
\]

These are roughly 29 times the M3 transformed residuals.

The far bounds become small,

\[
1.04\times10^{-5}
\quad\text{even},
\]

\[
5.29\times10^{-5}
\quad\text{odd},
\]

but the local residual dominates.

The odd top Ritz value is also outside the inner window:

\[
\boxed{
\theta_{o,4}^{\max}
\approx
0.0236325
>
0.02.
}
\]

Exact self-consistent moment closure is therefore not sufficient: the correction direction must also approximately solve the local generalized eigen-equation.

---

## 5. Moment-constrained graph-shell construction [D/N]

For one M3 Ritz pair \((q,\theta)\), let

\[
D_\theta=A_{SS}-\theta B_{SS}
\]

be the fresh-shell operator and let \(R_\theta^Tq\) be the ordinary graph right-hand side.

Let \(\ell_\theta\) be the shell vector representing the leading moment functional.

The constrained graph solve is

\[
\boxed{
D_\theta y+\ell_\theta\mu=R_\theta^Tq,
}
\tag{6}
\]

\[
\boxed{
\ell_\theta^Ty=\mathcal L_\theta(q).
}
\tag{7}
\]

With

\[
y_0=D_\theta^{-1}R_\theta^Tq,
\qquad
v=D_\theta^{-1}\ell_\theta,
\]

the scalar multiplier and corrected tail are

\[
\boxed{
\mu
=
\frac{
\ell_\theta^Ty_0-\mathcal L_\theta(q)
}{
\ell_\theta^Tv
},
}
\tag{8}
\]

\[
\boxed{
y=y_0-v\mu.
}
\tag{9}
\]

Thus the moment condition can be imposed by a one-constraint rank-one correction of the audited graph-shell solve.

---

## 6. Moment-constrained graph replay [N]

The moment constraints close to roundoff before re-Ritz in all eight channels.

For the dominant fourth channel:

### Even

\[
\mathcal L_\theta(q)\approx-0.477631,
\qquad
\mu\approx4.19667\times10^{-4}.
\]

The induced shell-equation residual has norm

\[
\boxed{
\|\ell_\theta\mu\|_2
\approx
0.0417398.
}
\]

### Odd

\[
\mathcal L_\theta(q)\approx-2.456639,
\qquad
\mu\approx2.15107\times10^{-3},
\]

with

\[
\boxed{
\|\ell_\theta\mu\|_2
\approx
0.213319.
}
\]

These values quantify the price of forcing the moment constraint inside this finite shell.

After re-Ritz the spectral window is better behaved than for the flat shell:

\[
\theta_{e,\max}\approx0.000489533,
\]

\[
\boxed{
\theta_{o,\max}\approx0.0156990<0.02.
}
\]

But the transformed residuals remain much worse than M3:

\[
\boxed{
0.0258747
\to
0.459350
\quad\text{even},
}
\]

\[
\boxed{
0.0267740
\to
0.468840
\quad\text{odd}.
}
\]

Because equations (6)–(7) use the old individual \(\theta_j\), the moment also returns after re-Ritz:

\[
\|\mathcal L_{\Theta_4}(Z_4)\|_2
\approx
5.805\times10^{-4}
\quad\text{even},
\]

\[
\|\mathcal L_{\Theta_4}(Z_4)\|_2
\approx
1.9623\times10^{-2}
\quad\text{odd}.
\]

---

## 7. Finite-shell obstruction at the present scale [I/G]

The computations separate two issues.

### Invariance

The fixed-\(\theta\) condition is not preserved by re-Ritz. This is solved exactly by

\[
\mathscr L(X)=0.
\]

### Geometric cost

Within the tested finite-shell directions, enforcing the moment condition pushes the span too far from the low-residual generalized eigenspace.

The dominant-channel constrained multipliers quantify this directly.

Therefore the current obstruction is not algebraic impossibility of moment cancellation. It is

\[
\boxed{
\textbf{lack of a low-residual finite-shell direction that also cancels the remote moment.}
}
\]

A richer asymptotic Green-function tail is not ruled out.

---

## 8. Consequence for KKT/Feshbach [G]

Do not rebuild the v13.982/v13.988 KKT payload on any of the three tested M4 carriers:

1. naive fixed-\(\theta\) constant shell;
2. self-consistent constant shell;
3. fixed-\(\theta\) moment-constrained graph shell.

Their full residuals are substantially worse than M3.

The M3 carrier remains the superior numerical carrier among the tested choices.

---

## 9. Correct pivot [O]

v13.991 showed that the near-singular \(6\times6\) inverse cancels from the normalized Xi scalar and phase signs.

The present gate says to push that projective cancellation one level earlier.

The v13.980 arbitrary-carrier reduction introduces the complement inverse

\[
\widehat D^{-1}
\]

through KKT solves before the bordered observable is formed.

But bordered determinants commute with Schur elimination.

Therefore the next gate is

\[
\boxed{
\textbf{derive the bordered determinant before eliminating }\widehat D.
}
\]

If the common complement determinant cancels from the Xi scalar and phase observables, the large KKT inverse-action residuals need not be individually certified.

---

## 10. Result

The v13.990 leading-moment idea survives mathematically in the exact subspace-invariant form

\[
\boxed{
\mathscr L(X)
=
\ell^TX
+
(\mathbf1^TX)
(X^TBX)^{-1}(X^TAX)
=
0.
}
\]

This condition was solved numerically and remains zero after re-Ritz to \(10^{-14}\) or better.

However, the tested finite-shell realizations increase the full transformed residual from roughly

\[
2.6\times10^{-2}
\]

to

\[
4.6\times10^{-1}
\text{--}
7.5\times10^{-1},
\]

despite reducing the far-tail bound by one to two orders of magnitude.

Thus the current finite-shell remote-moment correction is not a proof-grade carrier improvement.

The next nonredundant gate is the pre-elimination projective bordered determinant.
