# Cone Derivation Ledger v13.795 — Lane A First Source-Faithful Form-Core Schur Diagnostics and Near-Null Conditioning Barrier

Date: 2026-09-25

Lane: A.

Status: [N] reproducible high-precision finite-section diagnostics; [D] implementation uses the source-faithful form-core route of v13.794; [N] \(a=1,\lambda=0\) exhibits severe near-null conditioning and nonmonotone Schur parameters; [N] \(a=0.5\) control remains stable and inside the Schur disk; [G] no positivity, RH, or finite-to-infinite conclusion.

Parents: v13.291, v13.786, v13.790–794.

Research artifact:
\[
\texttt{research-notes/suzuki\_form\_core\_schur\_parameter\_diagnostic.py}
\]
(commit \`c21fe88002f1640ad175583d91de5f73753a9883\`).

## 0. Synchronization

Immediately before this write the live ledger head is v13.794. No collision is present.

## 1. Numerical realization [D/N]

Use the orthonormal Dirichlet form-core basis
\[
\psi_n(x)
=
a^{-1/2}
\sin\!\left(\frac{n\pi(x+a)}{2a}\right)
\]
already audited in the source-level matrix work.

The direct Weil form matrix is
\[
A_N=(Q_W^a(\psi_m,\psi_n))_{m,n\le N}.
\]

For the present diagnostic,
\[
\lambda=0,
\]
so the Galerkin equation is
\[
\boxed{
A_Nc_N=f_N,
}
\tag{1}
\]
where
\[
(f_N)_n
=
\langle\psi_n,e^x\rangle.
\]

No endpoint row is added. The Dirichlet conditions belong only to the form-core trial basis.

The source overlaps are evaluated exactly as
\[
\boxed{
\langle\psi_n,e^{\alpha x}\rangle
=
\frac{k_n}{\sqrt a}
\frac{
e^{-\alpha a}-(-1)^n e^{\alpha a}
}{
\alpha^2+k_n^2
},
\qquad
k_n=\frac{n\pi}{2a}.
}
\tag{2}
\]

The \(x e^{\alpha x}\) moments used for \(\kappa_1\) are obtained by differentiating (2) with respect to \(\alpha\).

## 2. Scalar diagnostics [D]

After parity splitting,
\[
E_{e,N}
=
f_{e,N}^{T}(A_N^{(+)})^{-1}f_{e,N},
\]
\[
E_{o,N}
=
f_{o,N}^{T}(A_N^{(-)})^{-1}f_{o,N}.
\]

The first Schur diagnostic is
\[
\boxed{
\kappa_{0,N}
=
\frac{E_{e,N}-E_{o,N}}
{E_{e,N}+E_{o,N}}.
}
\tag{3}
\]

The second is evaluated from the one-source moment formula of v13.793:
\[
\boxed{
\kappa_{1,N}
=
-\frac{2}{
1-\kappa_{0,N}^2
}
\left[
\frac{M_{-,N}}{H_N}
+
\kappa_{0,N}\frac{M_{+,N}}{H_N}
\right],
}
\tag{4}
\]
with
\[
H_N=E_{e,N}+E_{o,N}.
\]

For the exact operator, \(\kappa_0,\kappa_1\in[-1,1]\). A finite-section value outside this interval is interpreted only as a truncation/conditioning diagnostic.

## 3. \(a=1,\lambda=0\): near-null barrier [N]

The matrix was assembled at 60 decimal digits with the source-faithful archimedean series through \(n_{\max}=90\).

\[
\begin{array}{c|c|c|c|c|c}
N&
\lambda_{\min}^{(+)}&
\lambda_{\min}^{(-)}&
\kappa_{0,N}&
\kappa_{1,N}&
E_o/E_e
\\ \hline
4&
2.174988838249273\times10^{-8}&
4.306955306690991\times10^{-6}&
0.9982006287200390&
-0.9871872087034810&
9.00495803123417\times10^{-4}
\\
6&
3.237654258905388\times10^{-11}&
2.118622354113837\times10^{-8}&
0.9995475308335461&
-0.9983177672656112&
2.262857768953646\times10^{-4}
\\
8&
1.416731657079546\times10^{-12}&
1.381679887454618\times10^{-10}&
0.9973480360201262&
-1.0008360669332220&
1.327742552649007\times10^{-3}
\\
10&
1.232158117461073\times10^{-13}&
8.191578585042144\times10^{-13}&
0.9678386278047132&
-0.9952531351027641&
1.634350080380598\times10^{-2}
\\
12&
1.822752686728062\times10^{-15}&
6.203768857719305\times10^{-14}&
0.9938958532214508&
-0.9973015543295958&
3.061417058813291\times10^{-3}
\end{array}
\tag{5}
\]

The linear solves themselves have tiny algebraic residuals at the working precision. The instability is instead caused by the rapidly collapsing low eigenvalues of the Galerkin blocks.

In particular,
\[
\boxed{
\lambda_{\min}^{(+)}(N=12)
\approx1.82\times10^{-15}.
}
\tag{6}
\]

Thus the unshifted resolvent is already an extreme inverse problem at \(a=1\) in these low-dimensional sections.

## 4. Interpretation of the \(N=8\) Schur overshoot [N/G]

At \(N=8\),
\[
\kappa_{1,8}
\approx-1.0008360669.
\]

This lies slightly outside the exact Schur disk.

This is **not** a contradiction of v13.790–793.

The truncated Galerkin vector
\[
v_N\in V_N
\]
is not itself the exact Riesz vector
\[
A_a^{-1}e^x,
\]
so the function formed from its Fourier transform need not satisfy the exact finite boundary-triple Schur inequality at every truncation.

Accordingly,
\[
\boxed{
|\kappa_{1,N}|>1
}
\]
is a useful a posteriori warning that the Ritz inverse is not yet accurate enough for the second Schur step.

## 5. Small-\(a\) control: \(a=0.5,\lambda=0\) [N]

The same code was run at 50 decimal digits.

\[
\begin{array}{c|c|c|c|c}
N&
\lambda_{\min}^{(+)}&
\lambda_{\min}^{(-)}&
\kappa_{0,N}&
\kappa_{1,N}
\\ \hline
4&
9.7131633276757\times10^{-5}&
1.7107521878834\times10^{-3}&
0.9927722754414743&
-0.9961273357779538
\\
6&
5.5260234106583\times10^{-6}&
2.9907586488043\times10^{-4}&
0.9976086404962850&
-0.9990324724858609
\\
8&
3.3795155678172\times10^{-6}&
2.7707419495915\times10^{-4}&
0.9984304453731560&
-0.9989392263555954
\\
10&
1.7319360146299\times10^{-6}&
2.6481324795790\times10^{-4}&
0.9991587928451872&
-0.9989788593733522
\\
12&
1.2918009278279\times10^{-6}&
2.5446719505260\times10^{-4}&
0.9993466652149114&
-0.9990739004783831
\end{array}
\tag{7}
\]

All displayed Schur diagnostics remain inside \((-1,1)\), and the sequence is substantially smoother than at \(a=1\).

This control strongly suggests that the \(a=1\) Schur overshoot is a conditioning/truncation effect rather than a sign or source-vector error in the implementation.

## 6. Relation to the infinite targets [G]

The Section-7 \(\lambda=0\) targets are
\[
\kappa_{0,\infty}
\approx0.9968019520324009,
\]
\[
\kappa_{1,\infty}
\approx-0.9954804115180577.
\]

The \(a=1\) finite-section values should **not** be expected to equal these asymptotic \(a\to\infty\) targets.

The useful observation is only that the scalar diagnostic architecture is numerically accessible and that the second Schur parameter detects inadequacy of a truncation much earlier than a raw solve residual.

## 7. Numerical bottleneck isolated [N/C]

At \(a=1\), the dominant difficulty is now:
\[
\boxed{
\text{accurate inversion on the near-null parity subspaces of }A_a.
}
\]

The next numerical route should therefore reuse the project's existing high-precision / protected-subspace / Feshbach machinery rather than simply increasing the dense Galerkin cutoff.

In particular, the desired quantities are only the source quadratic forms
\[
f_e^TA_e^{-1}f_e,
\qquad
f_o^TA_o^{-1}f_o,
\]
and the associated first moments.

A full inverse matrix is unnecessary.

This makes the existing low-rank protected-subspace machinery directly relevant.

## 8. Reproducibility

The committed script
\[
\texttt{suzuki\_form\_core\_schur\_parameter\_diagnostic.py}
\]
imports the audited source matrix assembly, evaluates the source and moment vectors analytically, reports parity-block minima, condition numbers, residuals, energy ratio, \(\kappa_0\), and \(\kappa_1\), and supports both \(\lambda=0\) and shifted control runs.

## Result

The first source-faithful form-core Schur experiment is successful as a diagnostic but not yet converged at \(a=1\).

\[
\boxed{
a=0.5:\ \text{stable in-disk control};
}
\]
\[
\boxed{
a=1:\ \text{near-null inverse conditioning dominates by }N\approx8\text{--}12.
}
\]

The next useful computation is a **protected-subspace evaluation of the two parity source resolvent quadratic forms**, not a larger naive dense inverse.
