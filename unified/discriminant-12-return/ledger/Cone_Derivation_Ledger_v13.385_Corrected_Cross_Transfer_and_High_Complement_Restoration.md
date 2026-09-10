# Cone Derivation Ledger v13.385 — Corrected Cross Transfer and High-Complement Restoration

Date: 2026-09-10

Status labels: **[D]** exact derived, **[N-cert]** validated computational under stated arithmetic model, **[O]** open, **[Audit]** correction/limitation.

## 1. Purpose

Audit Rounds 20-21 invalidated the use of the legacy archimedean off-diagonal formula as the intended Suzuki operator.  This checkpoint restores the global pole-free high-complement positivity argument without reusing that formula as though it were correct.

The key observation is that the old `N=16003` cross computation remains a legitimate validated-computational certificate for the *legacy matrix that it actually assembled*.  We transfer that bound to the corrected matrix by analytically bounding the operator difference.

## 2. Corrected and legacy cross blocks

Write

\[
G_{\rm corr}=G_{\rm cp}+G_{\rm arch}^{\rm corr},\qquad
G_{\rm legacy}=G_{\rm cp}+G_{\rm arch}^{\rm legacy},
\]

where `cp` denotes the common cusp+prime contribution on

\[
F=\operatorname{span}\{\psi_n:21\le n\le16001,\ n\ \text{odd}\},
\]

and

\[
T=\overline{\operatorname{span}}\{\psi_n:n\ge16003,\ n\ \text{odd}\}.
\]

Hence

\[
\|G_{\rm corr}\|
\le \|G_{\rm legacy}\|
   +\|G_{\rm arch}^{\rm corr}\|
   +\|G_{\rm arch}^{\rm legacy}\|.
\]

## 3. Global centered-arch input

From v13.380,

\[
\widetilde Y_n:=nH_n-c_\infty,
\qquad
|\widetilde Y_n|<\frac{1.27}{n^2},
\]

for every odd positive `n`, with

\[
c_\infty=\frac{2}{\pi}\frac{e^{-1}}{1-e^{-4}}.
\]

This estimate was derived from the underlying kernel by integration by parts and is independent of the legacy off-diagonal reconstruction.

## 4. Corrected arch cross bound

The corrected arch entry is

\[
K^{\rm corr}_{mn}
=\pi mn\frac{\widetilde Y_n-\widetilde Y_m}{m^2-n^2}.
\]

For `n>m`,

\[
\frac{mn(m^{-2}+n^{-2})}{n^2-m^2}
=\frac{n^2+m^2}{mn(n^2-m^2)}
\le \frac1{m(n-m)}.
\]

Therefore

\[
|K^{\rm corr}_{mn}|
\le \frac{1.27\pi}{m(n-m)}.
\]

Write

\[
m=16003-2J,\qquad J=1,\dots,7991.
\]

Then

\[
\sum_{n\ge16003\atop n\,\rm odd}\frac1{(n-m)^2}
=\frac14\sum_{j\ge J}\frac1{j^2}
\le \frac14\left(\frac1{J^2}+\frac1J\right).
\]

The explicit finite sum gives

\[
\boxed{\|G_{\rm arch}^{\rm corr}\|_{HS}<0.003563.}
\]

## 5. Legacy arch cross bound

Using

\[
H_n=\frac{c_\infty+\widetilde Y_n}{n},
\]

the legacy arch formula decomposes as

\[
K^{\rm legacy}_{mn}
=-\frac4\pi\frac{c_\infty}{mn}+R_{mn}.
\]

The centered remainder satisfies

\[
|R_{mn}|
\le \frac{8(1.27)}{\pi}\frac1{m^3(n-m)}.
\]

The constant rank-one-like component is bounded with the odd-tail estimate

\[
\sum_{n\ge N\atop n\,\rm odd}\frac1{n^2}
\le \frac1{N^2}+\frac1{2N},
\]

and the remainder with the same `J`-sum as above.  The result is

\[
\boxed{\|G_{\rm arch}^{\rm legacy}\|_{HS}<2.78\times10^{-4}.}
\]

## 6. Transfer of the old validated cross certificate

The old cross verifier established, under its stated validated-computation arithmetic model,

\[
\|G_{\rm legacy}\|<0.99918.
\]

This statement is retained only as a bound on the legacy matrix.  It is **not** treated as a certificate for the intended corrected operator.

By triangle inequality,

\[
\|G_{\rm corr}\|
<0.99918+0.003563+0.000278
<\boxed{1.00303}.
\]

Thus the corrected cross clears the relaxed target `1.01` without requiring a new giant Gram calculation.

## 7. Restored high-complement positivity

From v13.382,

\[
A_{0,F}\succeq0.22I.
\]

From v13.383,

\[
A_{0,T}\succeq4.6733I.
\]

For the block operator on `F\oplus T`, Schur positivity follows if

\[
0.22-\frac{\|G_{\rm corr}\|^2}{4.6733}>0.
\]

Using the transferred bound `1.00303`,

\[
0.22-\frac{1.00303^2}{4.6733}
>\boxed{0.0047}.
\]

Therefore, under the same validated-computational model used for the finite block and the legacy auxiliary cross certificate,

\[
\boxed{A_0|_{\mathcal D}>0,\qquad
\mathcal D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\ \rm odd\}.}
\]

This restores the premise needed for exact Schur-complement inertia reduction to the ten low modes `n=1,3,...,19`.

## 8. Audit status

**[Audit→resolved]** The v13.365 theorem-level overclaim is not reinstated by pretending the legacy formula was correct.  Instead:

1. the finite high block was rebuilt with the corrected rank-four operator (v13.382);
2. the tail coercivity bound was rechecked at kernel level (v13.383);
3. the old cross result is used only for the matrix it actually certified;
4. an analytic Hilbert-Schmidt transfer bound carries that auxiliary result to the corrected matrix.

This is the first post-audit checkpoint at which the global pole-free high complement is again closed on the corrected operator.

## 9. Next target

Return to the exact inertia decomposition

\[
A_0\sim S_{10}\oplus A_{0,\mathcal D},
\qquad
S_{10}=A_{CC}-A_{C\mathcal D}A_{\mathcal D\mathcal D}^{-1}A_{\mathcal D C},
\]

with `C=span{psi_1,psi_3,...,psi_19}`.

The previous v13.366 numerical Schur target must be recomputed using the corrected operator and the newly restored high-complement inverse bound.  No exact-zero, RH, or GRH conclusion follows from this checkpoint.
