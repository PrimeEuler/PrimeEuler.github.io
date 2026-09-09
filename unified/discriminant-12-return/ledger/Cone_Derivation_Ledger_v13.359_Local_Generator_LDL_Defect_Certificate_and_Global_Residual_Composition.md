# Cone Derivation Ledger v13.359
## Local Generator-LDL Defect Certificate and Global Residual Composition

### Status
This checkpoint advances the pole-free Suzuki high-complement certification at the working split

\[
D=\overline{\mathrm{span}}\{\psi_n:n\ge21,\ n\text{ odd}\},
\]

with finite high block \(21\le n\le16001\), tail beginning at \(16003\), and finite shifted target

\[
B=A_{0,[21,16001]}-0.22I.
\]

Earlier checkpoints established the exact displacement-rank-two structure, the point generator-LDL recurrence, midpoint minimum pivot \(\approx0.25429962365\), and an a-posteriori total factor-residual allowance of about \(3.15\times10^{-6}\).

The remaining issue was how to validate the arithmetic without propagating interval generator states through all 7991 Schur steps. Naive interval propagation suffers dependency inflation.

### Local exact-state comparison
At one point-arithmetic elimination state define

\[
M_{ij}=\frac{2}{\pi}\frac{u_iv_j-v_iu_j}{x_i-x_j},\qquad i\ne j,
\]

with diagonal \(d\), \(x_i=n_i^2\), pivot \(a=d_1\), exact first column \(b_*\) reconstructed from the current point generators, and

\[
\ell_*=b_*/a.
\]

The exact Schur state represented from the current point state is

\[
d_*'=d_2-b_*^2/a,
\]

\[
u_*'=u_2-\ell_*u_1,
\qquad
v_*'=v_2-\ell_*v_1.
\]

Suppose the factorization stores finite-precision point values

\[
\hat\ell,\ \hat d',\ \hat u',\ \hat v'.
\]

Treat those stored numbers as exact dyadic inputs to a higher-precision checker and define

\[
e_\ell=\hat\ell-\ell_*,\quad
e_d=\hat d'-d_*',\quad
e_u=\hat u'-u_*',\quad
e_v=\hat v'-v_*'.
\]

### Local Frobenius defect bound
Let \(\widehat M'\) be the matrix represented by \((\hat d',\hat u',\hat v')\), and let

\[
\Delta=M-L(\hat\ell)\operatorname{diag}(a,\widehat M')L(\hat\ell)^T.
\]

Then

\[
\boxed{
\|\Delta\|_F
\le
\sqrt2|a|\|e_\ell\|_2
+\|e_d\|_2
+\delta_{\mathrm{off}}
+|a|\|e_\ell\|_2\bigl(\|\ell_*\|_2+\|\hat\ell\|_2\bigr)
}
\]

with

\[
\boxed{
\delta_{\mathrm{off}}
\le
\frac{2c}{D_{\min}}
\left(
\|e_u\|_2\|v_*'\|_2
+
\|\hat u'\|_2\|e_v\|_2
\right),
\qquad c=2/\pi.
}
\]

Here

\[
D_{\min}=\min_{i\ne j}|x_i-x_j|.
\]

For the odd Fourier modes, adjacent trailing values differ by

\[
(n+2)^2-n^2=4n+4,
\]

so \(D_{\min}\) is explicit at every elimination step.

The off-diagonal estimate uses

\[
B(u,v)=uv^T-vu^T,
\qquad
\|B(p,q)\|_F\le2\|p\|_2\|q\|_2,
\]

plus \(|x_i-x_j|^{-1}\le D_{\min}^{-1}\).

### Global residual composition
If \(\Delta_k\) denotes the local defect at step \(k\), then the final factor residual has the exact telescoping form

\[
E=\sum_k P_k\Delta_kP_k^T,
\]

where \(P_k\) is the accumulated prefix lower factor.

Therefore

\[
\boxed{
\|E\|_2
\le
\||L|\|_2^2\sum_k\|\Delta_k\|_2
\le
\||L|\|_1\||L|\|_\infty
\sum_k\|\Delta_k\|_F.
}
\]

This is the key certification simplification. The verifier need not propagate interval generator states. It needs only:

1. the 512-bit point generator-LDL pass;
2. a higher-precision, outward-rounded local replay of each step;
3. the accumulated scalar \(\sum_k\|\Delta_k\|_F\);
4. the row and column sums of \(|L|\).

### Independent algebra test
A generic displacement-rank-two prototype deliberately carried out one Schur update in float32 and evaluated the dense local reconstruction defect in float64. Representative results were

\[
\begin{array}{c|cc}
N & \|\Delta\|_F\text{ measured} & \text{derived bound}\\
\hline
5  & 2.19\times10^{-7} & 5.09\times10^{-7}\\
10 & 2.87\times10^{-7} & 8.22\times10^{-7}\\
20 & 3.31\times10^{-7} & 4.30\times10^{-6}
\end{array}
\]

The bound covered the measured defect in each test. This validates the algebra/prototype implementation only; it is not the 7991-mode Suzuki certificate.

### Certification target
The established total residual allowance remains approximately

\[
\|B-LDL^T\|_2<3.15\times10^{-6}.
\]

The arithmetic-only design target remains

\[
\boxed{\|E_{\mathrm{arith}}\|_2<10^{-8}}.
\]

The exact-vs-nominal matrix uncertainty from v13.357 is \(\lesssim2\times10^{-13}\), negligible on this scale.

### Guardrail
This checkpoint provides a rigorous local-defect formula and exact global composition identity, but the full 7991-step directed-rounded replay has not yet been executed. Therefore positivity of \(B\), positivity of the full high complement, exact zero modes, RH, or GRH are **not** claimed here.

### Next target
Implement the full replay using 512-bit point states and a higher-precision outward-rounded checker. Record:

- minimum point pivot;
- \(\||L|\|_1\) and \(\||L|\|_\infty\);
- accumulated \(\sum_k\|\Delta_k\|_F\);
- resulting certified \(\|E_{\mathrm{arith}}\|_2\).

If the last quantity is below \(10^{-8}\), the finite high-block positivity certificate should close with a large residual margin.
