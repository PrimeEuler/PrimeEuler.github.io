# Cone Derivation Ledger v13.348 — Global Inertia Correction and High-Complement Positivity Target

## Critical structural correction

A six-dimensional positive subspace of an **infinite-dimensional** operator does **not** imply that the nonpositive index is at most four.  That inference is valid only inside a ten-dimensional space.

Therefore the v13.345--347 six-plane bridge, while useful as a positive witness, is not by itself a global inertia certificate.

The correct global decomposition is

\[
\mathcal H_{\rm even}=\mathcal C_{10}\oplus\mathcal D,
\]

where

\[
\mathcal C_{10}=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\}
\]

and

\[
\mathcal D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\text{ odd}\}.
\]

If \(A|_{\mathcal D}>0\), then exact Schur-complement inertia reduction gives

\[
\operatorname{ind}_{\le0}(A)
=
\operatorname{ind}_{\le0}
\left(
A_{CC}-A_{CD}A_{DD}^{-1}A_{DC}
\right),
\]

and the right-hand side is a ten-dimensional problem.  Only at that stage does a six-dimensional positive subspace imply a nonpositive-index bound \(\le4\).

This checkpoint therefore changes the main target from “protect one six-plane against the tail” to “certify the entire high complement \(\mathcal D\) positive.”

## Pole-free monotonicity

Work first with

\[
A_0=C_{\rm cusp}+B_{\rm prime}+K_{\rm arch}.
\]

The pole term is positive semidefinite, so

\[
A=A_0+P_{\rm pole}\succeq A_0.
\]

Thus proving \(A_0|_{\mathcal D}>0\) is sufficient.

## Numerical high-complement anatomy

Fresh pole-free principal-block computations give the lowest eigenvalue

\[
\lambda_{\min}(A_{0,[21,M]})
\]

approximately as follows:

\[
\begin{array}{c|c}
M & \lambda_{\min}\\
\hline
399  & 0.231953166244\\
1001 & 0.229033630597\\
2001 & 0.228022633935\\
4001 & 0.227509839335\\
6001 & 0.227336299782
\end{array}
\]

The high block therefore appears to have a stable positive gap near \(0.227\), not a collapsing one.

This is numerical finite-section evidence only.

## Moving-interface coupling

The noncompact prime operator means the moving finite/tail interface retains \(O(1)\) coupling.  Direct pole-free cross-block diagnostics give approximate operator norms

\[
\begin{array}{c|c|c}
\text{split} & \text{sampled tail} & \|G\|_2\\
\hline
2001/2003 & 2003\ldots6003  & 0.8421\\
4001/4003 & 4003\ldots10003 & 0.8544\\
6001/6003 & 6003\ldots16003 & 0.8836
\end{array}
\]

So the interface coupling does not decay to zero, exactly as diagnosed in v13.313.  The mechanism that eventually wins is the logarithmically growing coercive tail gap.

## Robust analytic tail gaps

Using the deliberately rounded target

\[
\|B_{\rm prime}\|<2.05,
\]

and the analytic localized cusp/arch bounds gives approximately

\[
\alpha_{4003}>3.2872,
\qquad
\alpha_{6003}>3.6926,
\qquad
\alpha_{10003}>4.2033.
\]

This suggests moving the proof interface farther out, near \(N=10003\), where the tail gap is large enough to absorb a moving-interface norm below one.

## Coarse sufficient certificate at N=10003

A particularly simple target is

\[
\boxed{A_{0,[21,10001]}\succeq0.22I},
\]

\[
\boxed{\|A_{0,[21,10001],[10003,\infty)}\|<0.95},
\]

and

\[
\boxed{A_{0,[10003,\infty)}\succeq4.20I}.
\]

Then the Schur correction into the finite high block is bounded by

\[
\frac{0.95^2}{4.20}
\approx0.214881,
\]

so the whole high complement obeys

\[
A_0|_{\mathcal D}
\succeq
\left(0.22-\frac{0.95^2}{4.20}\right)I
>
\boxed{0.0051\,I}.
\]

This would rigorously establish \(\mathcal D>0\).

## Consequence once D>0 is certified

After positivity of the high complement is established, the full infinite inertia reduces exactly to the ten-dimensional low-core Schur complement

\[
S_{10}=A_{CC}-A_{CD}A_{DD}^{-1}A_{DC}.
\]

The final global index problem is then finite and well posed:

- certify \(S_{10}\) has a six-dimensional positive subspace;
- conclude \(\operatorname{ind}_{\le0}(A)\le4\).

This is the correct place to reuse the rational six-dimensional core witness machinery developed in v13.336--343, after updating it to the **full** high-complement Schur solve rather than the earlier finite-buffer solve.

## Guardrails

- The earlier six-dimensional full-tail witness remains a valid positive-subspace construction but does not by itself imply a global index bound.
- The large high-complement computations here are midpoint numerical anatomy only.
- The proposed \(0.22/0.95/4.20\) inequalities are certification targets, not yet proved inequalities.
- No exact zero mode, \(\lambda_1=0\), RH, or GRH conclusion follows.
