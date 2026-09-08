# Cone Derivation Ledger v13.315 — Exact Joint-Prime Sequence Factorization and Sharpened Core–Tail Schur Bound

## Status

This checkpoint sharpens v13.314 by retaining the exact oscillatory structure of the five prime shifts instead of taking absolute values shift-by-shift before summation.

The key new fact is that the entire off-diagonal prime matrix in the a=1 even-v odd-Dirichlet sector factors through a single scalar sequence \(A_n\). This yields a substantially sharper rigorous fixed-core to remote-tail bound and identifies a practical Schur-elimination scale near \(N\approx 400\)–\(500\), rather than the first positive coercive cutoff \(N=151\).

No RH/GRH, kernel, or \(\lambda_1(a=1)=0\) conclusion is made.

---

## 1. Exact truncated-shift matrix element

For odd Dirichlet modes

\[
\psi_n(x)=\sin\frac{n\pi(x+1)}2,
\qquad n\text{ odd},
\]

and the two-sided truncated translation

\[
(S_\ell f)(x)=\mathbf 1_{[-1,1]}(x-\ell)f(x-\ell)
+\mathbf 1_{[-1,1]}(x+\ell)f(x+\ell),
\]

direct integration gives, for odd \(m\ne n\),

\[
\boxed{
\langle \psi_m,S_\ell\psi_n\rangle
=
\frac4\pi\,
\frac{n\sin(m\theta)-m\sin(n\theta)}{n^2-m^2},
\qquad
\theta=\frac{\pi\ell}{2}.
}
\]

This is equivalent to the v13.314 formula but with the parity phases simplified completely in the Dirichlet convention.

---

## 2. Collapse of the five prime shifts to one sequence

For

\[
B_{\rm prime}=-\sum_q w_q S_{\log q},
\qquad
w_q=\frac{\Lambda(q)}{\sqrt q},
\qquad
q\in\{2,3,4,5,7\},
\]

define

\[
\theta_q=\frac\pi2\log q,
\qquad
\boxed{
A_j=\sum_q w_q\sin(j\theta_q).
}
\]

Then, for odd \(m\ne n\),

\[
\boxed{
(B_{\rm prime})_{mn}
=-\frac4\pi\,
\frac{nA_m-mA_n}{n^2-m^2}.
}
\]

Thus the joint prime matrix does not need to be estimated as five independent shift matrices at the fixed-core/remote-tail interface. All five shifts combine into the single oscillatory scalar sequence \(A_j\).

For the near-null core

\[
\mathcal C=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\},
\]

the values are approximately

\[
\begin{array}{c|r}
m&A_m\\\hline
1& 1.8224834670\\
3& 0.3367680241\\
5& 0.1005237988\\
7& 0.0900498324\\
9& 0.1805890479\\
11&0.4057919522\\
13&1.5777840463\\
15&1.3380841076\\
17&-0.8133732815\\
19&1.0849347074
\end{array}
\]

and

\[
W:=\sum_q w_q=2.9262341821764086.
\]

---

## 3. Rigorous fixed-core tail estimate

For fixed odd \(m\) and odd \(n\ge N>m\),

\[
\left|(B_{\rm prime})_{mn}\right|
\le
\frac4\pi\,
\frac{1}{1-(m/N)^2}
\left(
\frac{|A_m|}{n}
+\frac{mW}{n^2}
\right).
\]

Using

\[
\sum_{\substack{n\ge N\\n\text{ odd}}}\frac1{n^2}
\le \frac1{N^2}+\frac1{2N},
\]

and

\[
\sum_{\substack{n\ge N\\n\text{ odd}}}\frac1{n^4}
\le \frac1{N^4}+\frac1{6N^3},
\]

Minkowski gives the row bound

\[
\|P_{\ge N}B_{\rm prime}\psi_m\|_2
\le
\frac4\pi\,
\frac{1}{1-(m/N)^2}
\left[
|A_m|\sqrt{S_2(N)}
+mW\sqrt{S_4(N)}
\right].
\]

Summing these squared row bounds over \(m\in\{1,3,\ldots,19\}\) yields a rigorous Hilbert–Schmidt upper bound

\[
\boxed{
\beta_N:=\|P_{\ge N}B_{\rm prime}P_{\mathcal C}\|
\le
\|P_{\ge N}B_{\rm prime}P_{\mathcal C}\|_{HS}
=O(N^{-1/2}).
}
\]

This keeps the full joint-prime cancellation in the leading \(1/n\) coefficient. It is substantially sharper than v13.314's shiftwise absolute-value bound.

---

## 4. Sharpened core-to-tail constants

The resulting bounds are approximately

\[
\begin{array}{c|c}
N&\beta_N\text{ upper bound}\\\hline
151&0.25594\\
237&0.19588\\
301&0.17119\\
401&0.14628\\
501&0.12981
\end{array}
\]

For comparison, the previous v13.314 bound at \(N=151\) was about \(1.13\). The new analytic value is already close to the direct numerical fixed-core tail norms from v13.313, which were around \(0.22\) at the first cutoff and around \(0.11\)–\(0.13\) by \(N=500\), depending on truncation.

The displayed decimals are ordinary floating evaluations of exact analytic formulas, not interval-certified enclosures.

---

## 5. Schur-elimination scale

Retain the v13.312 certified tail gap

\[
\alpha_N
=
\log(N/4)
-\left[
\frac\pi2
+C_{\rm prime}
+C_{\rm cusp}(N)
+C_{\rm arch}(N)
\right],
\]

with

\[
C_{\rm prime}\approx2.044764260347282.
\]

The associated crude core-only Schur penalty is

\[
\frac{\beta_N^2}{\alpha_N}.
\]

Representative values are

\[
\begin{array}{c|c|c|c}
N&\alpha_N&\beta_N&\beta_N^2/\alpha_N\\\hline
151&0.00373&0.25594&17.55\\
201&0.29270&0.21548&0.15863\\
237&0.45880&0.19588&0.08363\\
301&0.69944&0.17119&0.04190\\
401&0.98775&0.14628&0.02166\\
501&1.21127&0.12981&0.01391\\
701&1.54817&0.10873&0.00764\\
1001&1.90516&0.09036&0.00429
\end{array}
\]

Therefore the first positive cutoff \(N=151\) is a poor inversion point even though it proves tail positivity. A practical core-to-remote-tail Schur scale begins around \(N\approx400\)–\(500\), where the certified tail gap is order one and the prime core-tail coupling has already fallen below \(0.15\).

---

## 6. Structural interpretation

The operator picture is now sharper:

\[
\boxed{
\text{near-null core}
\oplus
\text{finite buffer/interface}
\oplus
\text{remote coercive tail}.
}
\]

The remote tail can be eliminated with a quantitatively small correction to the fixed near-null core once the split is moved away from the barely-positive threshold. The remaining difficulty is the finite buffer/interface, where the noncompact prime shifts can still produce \(O(1)\) coupling across nearby modes.

This checkpoint therefore does **not** prove positivity of the full even sector. It proves that the genuinely infinite remote-tail effect on the fixed near-null core is now under useful explicit control.

---

## 7. Audit continuity

The round-15 v13.302 Hilbert–Schmidt proof gap remains superseded by the revised v13.303 estimate and round-16 independent confirmation. The present checkpoint uses only that corrected cusp-tail lineage.

Parallel ledger activity through the defect-descent / stable-closure-strata updates was checked before this commit; no conflict with the Suzuki branch was found.

---

## 8. Next target

The highest-leverage next step is a finite buffer Schur/Feshbach audit. Suggested split:

\[
\mathcal C=\{1,3,\ldots,19\},
\]

\[
\mathcal B=\{21,23,\ldots,N-2\},
\]

\[
\mathcal T=\{N,N+2,\ldots\},
\]

with \(N\) initially around \(401\) or \(501\).

The goal is to compute the finite core+buffer matrix accurately and then use the certified tail gap plus explicit core-to-tail bound to control the Feshbach correction. A separate bound for buffer-to-tail coupling will still be needed; it should not be replaced by a false compactness assumption because the prime operator remains noncompact.
