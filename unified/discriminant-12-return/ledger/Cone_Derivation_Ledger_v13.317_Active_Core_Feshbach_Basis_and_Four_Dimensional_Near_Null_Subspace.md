# Cone Derivation Ledger v13.317 — Active-Core Feshbach Basis and Four-Dimensional Near-Null Subspace

## Status

This checkpoint continues v13.316 by rotating the low coordinate core

\[
\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\}
\]

into the 60-digit eigenbasis of its 10x10 Suzuki form matrix, then expressing the finite-buffer Schur correction in that basis.

The purpose is not to claim exact zero modes. It is to identify the numerically active near-null subspace before any rigorous infinite-tail closure is attempted.

External audit round 17 is incorporated explicitly: the earlier v13.314 boxed shift formula had a sign error for mixed-parity pairs, but v13.315's cleaner odd-sector joint-prime formula was independently verified. The present checkpoint uses only the v13.315 convention.

No RH/GRH, kernel, or \(\lambda_1(a=1)=0\) conclusion is made.

---

## 1. Finite decomposition

At \(a=1\), even \(v\) corresponds to odd Dirichlet indices. We use

\[
\mathcal C=\operatorname{span}\{\psi_n:n=1,3,\ldots,19\},
\]

and the finite buffer

\[
\mathcal B=\operatorname{span}\{\psi_n:n=21,23,\ldots,399\}.
\]

The odd-mode matrix is assembled as in v13.316:

\[
A=C_{\rm cusp}+B_{\rm prime}+K_{\rm arch}+P_{\rm pole}.
\]

The buffer is eliminated by

\[
\Delta=A_{CB}A_{BB}^{-1}A_{BC}.
\]

Numerically,

\[
\lambda_{\min}(A_{BB})\approx0.267259458.
\]

Thus the finite buffer remains comfortably separated from zero.

---

## 2. High-precision low-core spectrum

The 60-digit eigenvalues of the 10x10 low core are

\[
\begin{aligned}
&1.12389415799\times10^{-20},\\
&9.41881201677\times10^{-16},\\
&1.12143957393\times10^{-11},\\
&4.76556003061\times10^{-8},\\
&7.53001645473\times10^{-5},\\
&3.80452816412\times10^{-2},\\
&1.34217475752,\\
&1.76154867626,\\
&2.05911985935,\\
&2.46994327698.
\end{aligned}
\]

This is a multiscale near-null hierarchy, not evidence for six exact zero modes.

Let \(Q\) denote the corresponding orthogonal eigenvector matrix and write

\[
\widetilde\Delta=Q^T\Delta Q.
\]

---

## 3. Buffer correction in the core eigenbasis

The diagonal entries of \(\widetilde\Delta\) along the first six core eigenvectors are numerically

\[
\boxed{
0,\;
8.14\times10^{-16},\;
9.14\times10^{-12},\;
3.58\times10^{-8},\;
6.34\times10^{-5},\;
3.56\times10^{-2}
}
\]

where the first value is below trustworthy double-precision sign resolution and is therefore recorded as numerical zero at this scale rather than assigned a sign.

The striking point is that the buffer correction follows the same hierarchy as the core eigenvalues themselves. Directions that are tiny in the isolated core remain weakly coupled to the finite buffer.

This makes the correction highly anisotropic. Replacing \(\Delta\) by \(\|\Delta\|I\) destroys the structure relevant to the near-null directions.

---

## 4. Active-subspace dimension

Let \(\mathcal A_r\) be the span of the first \(r\) high-precision core eigenvectors. The norm of the correction coupling between \(\mathcal A_r\) and the remaining low-core eigendirections is

\[
\|\widetilde\Delta_{\mathcal A_r,\mathcal C\ominus\mathcal A_r}\|_2.
\]

Representative numerical values are

\[
\begin{array}{c|c}
r & \text{coupling to remaining low-core directions}\\
\hline
1 & 1.70\times10^{-11}\\
2 & 2.69\times10^{-9}\\
3 & 3.42\times10^{-7}\\
4 & 1.49\times10^{-5}\\
5 & 1.98\times10^{-3}\\
6 & 5.32\times10^{-2}
\end{array}
\]

The jump between \(r=4\) and \(r=5\) is substantial. Numerically, the first four directions therefore form a particularly clean active near-null subspace:

\[
\boxed{\dim \mathcal A=4.}
\]

This is a numerical model-reduction choice, not a theorem that the true nullity is four.

---

## 5. Refined decomposition

The finite geometry now suggests

\[
\boxed{
\mathcal H_{\rm even}
=
\mathcal A_4
\oplus
\mathcal C_{\rm stiff}
\oplus
\mathcal B
\oplus
\mathcal T,
}
\]

where

- \(\mathcal A_4\): first four high-precision low-core eigenvectors;
- \(\mathcal C_{\rm stiff}\): the remaining six low-core eigenvectors;
- \(\mathcal B\): finite modes 21 through 399;
- \(\mathcal T\): remote odd-mode tail beginning at 401.

The finite buffer and stiff low-core sector can now be treated as a matrix-valued complement rather than through scalar norm penalties.

---

## 6. Remaining obstruction

The remote-tail bound from v13.315 is still too coarse if applied to the entire 10-dimensional coordinate core:

\[
\beta_{401}^2/\alpha_{401}\approx2.17\times10^{-2}.
\]

That is enormous relative to the first four active scales.

The next key task is therefore not another finite-buffer calculation. It is to project the exact prime-tail coupling, and then the cusp/arch tail couplings, directly onto the four active eigenvectors. Because those vectors are highly tuned combinations of low odd modes, substantial cancellation is expected beyond the coordinate-core Hilbert-Schmidt bound.

The natural next object is

\[
P_{\mathcal A_4}A P_{\mathcal T},
\]

with a rigorous or at least sharply controlled matrix bound that preserves the four-dimensional active geometry.

---

## 7. Guardrails

- The first finite Feshbach eigenvalues are at or below double-precision resolution; no sign claim is made there.
- The multiscale low-core hierarchy is numerical evidence, not proof of multiple zero modes.
- Buffer positivity is finite-dimensional and does not establish infinite-complement positivity by itself.
- v13.314's exact-formula sign issue is superseded here by the externally verified v13.315 odd-sector formula.
- No RH/GRH conclusion follows.

---

## 8. Next target

Project the exact v13.315 joint-prime sequence factorization onto the first four high-precision core eigenvectors and derive active-to-tail bounds at \(N=401\), \(501\), and beyond.

If the active projected coupling is as small as the finite-buffer anatomy suggests, the global even-sector problem may reduce to a four-dimensional matrix-valued Feshbach enclosure plus explicit positive complement bounds.
