# Cone Derivation Ledger v13.310 — V4 Four-Channel Shell-Defect Transform

## Scope

This checkpoint extends v13.309 from a local/global V4 overlay to an exact four-character transform of the divisor shell-defect field

\[
\delta_k(n)=\left\{\frac nk\right\}=\frac{n-Y_k^2}{k}.
\]

The four real characters modulo 12 are

\[
1,\ \chi_{-4},\ \chi_{-3},\ \chi_{12}=\chi_{-4}\chi_{-3}.
\]

Companion note:

`research-notes/V4_Four_Channel_Shell_Defect_Transform.md`

No RH/GRH, spectral, Fredholm, positivity, or new primality claim is made.

---

## 1. Four arithmetic shell-defect channels

Define

\[
E_\chi(n)=\sum_{k\le n}\chi(k)\delta_k(n)
=\sum_{k\le n}\chi(k)\frac{n-Y_k^2}{k}.
\]

For the trivial character,

\[
\boxed{E_1(n)=nH_n-D(n).}
\]

The three nontrivial channels are

\[
E_{-4}(n),\qquad E_{-3}(n),\qquad E_{12}(n).
\]

The pre-existing discriminant-12 twisted sawtooth is therefore the mixed channel of a full four-character transform, rather than an isolated twisted sum.

---

## 2. Exact Hadamard reconstruction on U(12)

Define the unit-residue defect totals

\[
R_r(n)=\sum_{\substack{k\le n\\ k\equiv r\pmod{12}}}\delta_k(n),
\qquad r\in\{1,5,7,11\}.
\]

On \(U(12)\), the character table is

\[
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\qquad H_4^2=4I.
\]

Writing \(E_1^\times\) for the trivial-channel sum restricted to \(\gcd(k,12)=1\),

\[
\boxed{
\begin{pmatrix}
E_1^\times\\E_{-4}\\E_{-3}\\E_{12}
\end{pmatrix}
=
H_4
\begin{pmatrix}
R_1\\R_5\\R_7\\R_{11}
\end{pmatrix}.}
\]

Hence

\[
\boxed{
\begin{pmatrix}
R_1\\R_5\\R_7\\R_{11}
\end{pmatrix}
=
\frac14H_4
\begin{pmatrix}
E_1^\times\\E_{-4}\\E_{-3}\\E_{12}
\end{pmatrix}.}
\]

Thus the four unit-residue totals and four V4 character channels are exactly equivalent descriptions of the same unit-supported shell-defect data.

Guardrail: \(E_1(n)=nH_n-D(n)\) contains nonunit residue classes as well.  The Hadamard inversion applies to \(E_1^\times\), not to the full untwisted discrepancy.

---

## 3. Generator directions

With

\[
1\leftrightarrow(0,0),\quad
5\leftrightarrow(1,0),\quad
7\leftrightarrow(0,1),\quad
11\leftrightarrow(1,1),
\]

the four channels are the mean, two one-generator imbalances, and the mixed/checkerboard imbalance.  The mixed character is

\[
\chi_{12}=\chi_{-4}\chi_{-3}.
\]

This is the exact same Walsh/V4 sign algebra used locally in v13.309, where the mixed factor-cell coefficient is \(\delta^2/4\).

The carriers remain distinct.

---

## 4. Quotient-block compression commutes with the V4 transform

For a constant quotient block

\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad L_q\le k\le R_q,
\]

we have \(\delta_k=n/k-q\).  Define

\[
H_\chi(N)=\sum_{k\le N}\frac{\chi(k)}{k},
\qquad
C_\chi(N)=\sum_{k\le N}\chi(k).
\]

Then

\[
\boxed{
E_{\chi,q}(n)
=n\left[H_\chi(R_q)-H_\chi(L_q-1)\right]
-q\left[C_\chi(R_q)-C_\chi(L_q-1)\right].}
\]

Therefore

\[
\boxed{E_\chi(n)=\sum_{q\in Q(n)}E_{\chi,q}(n)},
\qquad |Q(n)|=O(\sqrt n).
\]

So all four arithmetic character channels inherit the same hyperbola/quotient-block compression.

Because both block decomposition and character projection are linear finite sums, they commute exactly.

---

## 5. Two-axis organization of the divisor shell

The shell-defect data now admits two independent exact decompositions:

\[
\boxed{
\text{geometry: columns}\to\text{quotient blocks}}
\]

and

\[
\boxed{
\text{arithmetic: residue classes}\to\text{V4 character channels}}.
\]

These give a two-axis organization:

\[
\boxed{
\text{quotient-run index }q
\quad\times\quad
\text{character }\chi.}
\]

Each matrix entry is the exact block/channel contribution \(E_{\chi,q}(n)\).

The row sum over \(q\) gives a global character channel; the character reconstruction on unit-supported terms gives the residue-class defect totals.

---

## 6. Prime-contact guardrail

The exact prime criterion remains a support statement:

\[
\delta_k(n)=0\iff k\mid n,
\]

\[
\tau(n)=\#\{k:\delta_k(n)=0\},
\]

and for \(n>1\),

\[
\boxed{n\text{ prime}\iff\tau(n)=2.}
\]

The character transform reorganizes defect amplitudes; it does not replace or strengthen this zero-set criterion.

## Interpretation

v13.309 identified the same V4 character algebra locally on a four-vertex factor cell and globally on the mod-12 divisor twist.  v13.310 completes the global side: the entire unit-supported shell-defect field has an exact four-channel Hadamard transform, while quotient-block compression acts independently and commutes with it.  The result is a clean factorization of the arithmetic data into geometric quotient runs and V4 character channels, with the mixed channel connecting back to the local quarter-shift mode only at the level of shared representation structure.