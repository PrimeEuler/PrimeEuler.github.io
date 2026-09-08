# Cone Derivation Ledger v13.313 — Core–Buffer–Tail Interface and Fixed-Core Decoupling Audit

## Status

This checkpoint follows v13.312, where the smooth archimedean remainder was tail-localized and the first sufficient odd coercive cutoff was reduced to

\[
N=151.
\]

The immediate question is how to combine this certified positive tail with the low-mode near-null direction observed numerically since v13.291–v13.295.

The main structural conclusion is that a naive two-block decomposition

\[
\text{low modes}\oplus\text{tail}
\]

is not the right geometry for a Schur complement. The prime-shift operator is bounded but noncompact, so modes immediately below and above a hard cutoff can remain strongly coupled.

Instead, the correct architecture is

\[
\boxed{
\text{fixed near-null core}
\oplus
\text{finite high-mode buffer/interface}
\oplus
\text{certified coercive tail}.
}
\]

No RH/GRH, kernel, lambda_1=0, or global positivity conclusion is made.

---

## 1. Why N=151 is not automatically the best Schur split

At the first positive tail cutoff from v13.312,

\[
\alpha_{151}
:=
\log(151/4)-C_{\rm tail}(151)
\approx 3.73\times10^{-3}.
\]

Thus the crude inverse-tail estimate is

\[
\|A_{TT}^{-1}\|\le \alpha_{151}^{-1}\approx 268.
\]

This is far too large for a useful one-shot Schur estimate unless the low-to-tail coupling is extremely small.

The certified gap grows rapidly if the cutoff is moved upward. Using the v13.312 tail formula:

\[
\begin{array}{c|c|c}
N & \alpha_N & \alpha_N^{-1}\\
\hline
151 & 0.00373 & 267.9\\
175 & 0.15286 & 6.54\\
201 & 0.29270 & 3.42\\
237 & 0.45880 & 2.18\\
301 & 0.69944 & 1.43\\
401 & 0.98775 & 1.01\\
501 & 1.21127 & 0.826
\end{array}
\]

So the first positive cutoff is not necessarily the optimal elimination point.

---

## 2. Exact odd-basis representation of the prime shifts

In the even-v sector at a=1, use normalized odd Dirichlet modes

\[
\psi_n(x)=(-1)^{(n-1)/2}\cos\frac{n\pi x}{2},
\qquad n\text{ odd}.
\]

For a shift length \(\ell\), define

\[
(S_\ell f)(x)=f(x-\ell)+f(x+\ell),
\]

with f extended by zero outside [-1,1].

Then

\[
\langle\psi_m,S_\ell\psi_n\rangle
\]

reduces exactly to the sum of two elementary cosine-product integrals over

\[
[-1+\ell,1]
\quad\text{and}\quad
[-1,1-\ell].
\]

The full prime operator is

\[
B_{\rm prime}
=-\sum_{q\in\{2,3,4,5,7\}}
\frac{\Lambda(q)}{\sqrt q}S_{\log q}.
\]

This gives an exact finite formula for every odd-basis prime matrix entry, up to ordinary floating evaluation of the elementary functions.

---

## 3. Fixed near-null core versus remote tail

The numerical near-null vector stabilized overwhelmingly in the first few odd modes. We therefore define a fixed core

\[
\boxed{\mathcal C=\operatorname{span}\{\psi_n:n\le19,\ n\text{ odd}\}.}
\]

For fixed core mode m and n→∞, the exact shift-entry formula gives the expected oscillatory decay

\[
\langle\psi_m,S_\ell\psi_n\rangle=O(1/n).
\]

Hence the prime block from a fixed finite core into a remote tail is Hilbert–Schmidt, with tail norm expected to decay like \(N^{-1/2}\).

A direct numerical audit of the joint prime operator, summing tail modes through n=3001, gives:

\[
\begin{array}{c|c}
N & \|P_{\mathcal C}B_{\rm prime}P_{\ge N}\|_{HS,\,n\le3001}\\
\hline
151 & 0.22414\\
201 & 0.19275\\
237 & 0.17595\\
301 & 0.15417\\
401 & 0.13109\\
501 & 0.11493
\end{array}
\]

These are numerical truncated-tail diagnostics, not certified infinite-tail bounds.

Their role is structural: the fixed low core does decouple from a remote tail.

---

## 4. Why the whole finite block does not decouple the same way

The previous decay statement does **not** apply uniformly when the low index m moves with the cutoff.

For modes immediately across the interface,

\[
m=N-2,
\qquad n=N,
\]

the truncated-shift matrix elements can remain O(1). This is the Fourier-space expression of the fact that the prime operator is bounded but noncompact.

Therefore a hard split

\[
\{n<N\}\oplus\{n\ge N\}
\]

cannot be expected to have a small cross-block norm merely because N is large.

This is exactly why a crude estimate

\[
\|B^*A_{TT}^{-1}B\|
\le
\frac{\|B\|^2}{\alpha_N}
\]

is too pessimistic when B is taken as the full finite-to-tail block.

---

## 5. Correct three-block architecture

The natural decomposition is

\[
\boxed{
\mathcal H
=
\mathcal C\oplus\mathcal B_N\oplus\mathcal T_N,
}
\]

where

- \(\mathcal C\): fixed near-null core, e.g. odd n≤19;
- \(\mathcal B_N\): finite buffer/interface, 21≤n<N;
- \(\mathcal T_N\): certified positive tail, n≥N.

The point is not that \(\mathcal B_N\) is weakly coupled to \(\mathcal T_N\). It need not be.

The point is that the near-null core \(\mathcal C\) couples weakly to a sufficiently remote \(\mathcal T_N\), while the strongly coupled interface modes are retained explicitly in the finite problem.

Thus the eventual elimination should proceed in stages rather than by a single crude norm estimate.

---

## 6. Schur/Feshbach form

With blocks ordered as \(\mathcal C\oplus\mathcal B\oplus\mathcal T\), write

\[
A=
\begin{pmatrix}
A_{CC} & A_{CB} & A_{CT}\\
A_{BC} & A_{BB} & A_{BT}\\
A_{TC} & A_{TB} & A_{TT}
\end{pmatrix}.
\]

Since

\[
A_{TT}\ge \alpha_N I>0,
\]

the exact tail elimination gives the finite operator

\[
\boxed{
A_{\rm eff}^{(C\oplus B)}
=
\begin{pmatrix}
A_{CC} & A_{CB}\\
A_{BC} & A_{BB}
\end{pmatrix}
-
\begin{pmatrix}
A_{CT}\\A_{BT}
\end{pmatrix}
A_{TT}^{-1}
\begin{pmatrix}
A_{TC}&A_{TB}
\end{pmatrix}.
}
\]

A crude global bound on the second term is not sufficient. The next useful step is to exploit its block structure:

1. tightly bound \(A_{CT}A_{TT}^{-1}A_{TC}\), which should be small because C is fixed;
2. retain the buffer-facing correction explicitly or bound it using high-mode positivity of the buffer itself;
3. study the resulting finite matrix near the known numerical near-null direction.

---

## 7. Strategic consequence

The v13.312 result reduced the infinite problem to 75 odd modes below n=151 only in the sense of a **tail positivity threshold**.

v13.313 clarifies that the correct finite-to-infinite proof strategy is subtler:

\[
\boxed{
\text{tail positivity alone is not enough; interface geometry matters.}
}
\]

The fixed low core is the part that genuinely decouples from a remote tail. The moving high-mode boundary does not.

This prevents an overoptimistic claim that a 75×75 finite matrix plus a scalar tail gap would automatically settle the even sector.

---

## 8. Next target

The highest-leverage next step is a **fixed-core certified coupling bound**.

For each prime shift and each fixed core mode m≤19, derive an explicit bound

\[
|\langle\psi_m,S_\ell\psi_n\rangle|
\le \frac{C_{m,\ell}}{n},
\qquad n\ge N,
\]

then sum analytically over odd n≥N to obtain a rigorous infinite-tail Hilbert–Schmidt bound for

\[
P_{\mathcal C}B_{\rm prime}P_{\mathcal T_N}.
\]

The Hilbert, cusp-correction, and smooth-arch core-to-tail blocks can be treated similarly and are easier because their matrix entries already have explicit decaying formulas.

Once the fixed-core tail correction is rigorously bounded, the near-null core can be insulated from the infinite tail while the finite buffer carries the noncompact prime interface explicitly.

This is the natural next bridge from the current numerical near-null evidence to a controlled finite-dimensional sign problem.
