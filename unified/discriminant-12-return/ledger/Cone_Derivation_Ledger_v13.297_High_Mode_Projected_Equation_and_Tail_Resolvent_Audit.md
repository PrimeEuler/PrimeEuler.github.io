# Cone Derivation Ledger v13.297

## High-mode projected equation and tail-resolvent audit

**Status:** NUMERICAL FINITE-SECTION RESOLVENT MECHANISM IDENTIFIED — INFINITE-TAIL LOWER BOUND STILL OPEN — RH/GRH NOT PROVED.

This checkpoint follows v13.296.  Rather than extrapolating a fitted coefficient law, it studies the parity-reduced projected equation itself in the even-v sector at a=1.

For the odd Dirichlet modes n=1,3,5,...,19, partition the M=20 Ritz matrix at an odd cutoff N as

\[
A=\begin{pmatrix}A_{LL}&B^T\\ B&T_N\end{pmatrix},\qquad
c=\binom{c_L}{c_T}.
\]

For the lowest finite Ritz pair \(Ac=\lambda c\), the tail equation is

\[
(T_N-\lambda I)c_T=-Bc_L.
\]

Because the observed Ritz value at M=20 is \(\lambda\approx1.1239\times10^{-20}\), the finite calculation is numerically indistinguishable from

\[
T_Nc_T=-Bc_L.
\]

Whenever the finite tail block is invertible,

\[
\boxed{c_T=-T_N^{-1}Bc_L},
\]

and therefore

\[
\boxed{\|c_T\|_2\le \sigma_{\min}(T_N)^{-1}\|Bc_L\|_2}.
\]

This is the first direct resolvent-style mechanism in the audit that can explain rapid tail decay without fitting a phenomenological power or exponential law.

## High-mode row balance

Representative diagonal entries of the parity-reduced projected matrix are

\[
A_{9,9}\approx2.02223,
\quad A_{11,11}\approx0.0670205,
\quad A_{13,13}\approx1.80815,
\]

\[
A_{15,15}\approx1.02011,
\quad A_{17,17}\approx0.823683,
\quad A_{19,19}\approx1.91546.
\]

The anomalously small \(n=11\) diagonal is a concrete structural explanation for the coefficient shoulder found in v13.296.  The row reconstruction

\[
c_n=-\frac{\sum_{m\ne n}A_{nm}c_m}{A_{nn}}
\]

reproduces each finite-section coefficient to the matrix-eigensolver precision.  Selected values are

- \(n=11\): \(c_{11}\approx9.08711\times10^{-4}\), amplified by \(A_{11,11}\approx0.0670\).
- \(n=13\): \(c_{13}\approx-3.08000\times10^{-5}\).
- \(n=15\): \(c_{15}\approx-6.00393\times10^{-6}\).
- \(n=17\): \(c_{17}\approx-8.23825\times10^{-7}\).
- \(n=19\): \(c_{19}\approx1.68759\times10^{-8}\).

Thus the n=11 shoulder is not random numerical noise; it is tied to a genuine near-small diagonal / weak local restoring coefficient in the projected finite matrix.

## Finite tail-block conditioning

The smallest singular values of the finite parity-reduced tail blocks are approximately

| cutoff N | sigma_min(T_N) | condition number |
|---:|---:|---:|
| 9  | 3.02e-5 | 8.15e4 |
| 11 | 3.10e-5 | 7.85e4 |
| 13 | 3.26e-2 | 7.40e1 |
| 15 | 1.19e-1 | 1.93e1 |
| 17 | 5.71e-1 | 3.80 |

The key change occurs after the n=11 shoulder.  The tail block beginning at n=11 is nearly singular, while the blocks beginning at 13, 15, and especially 17 become progressively better conditioned.

## Finite resolvent bounds

For cutoff N=13:

\[
\|Bc_L\|_2\approx5.69\times10^{-5},\qquad
\sigma_{\min}(T_{13})\approx3.26\times10^{-2},
\]

so

\[
\|c_T\|_2\le1.75\times10^{-3}.
\]

The actual finite tail norm is much smaller,

\[
\|c_T\|_2\approx3.14\times10^{-5}.
\]

For cutoff N=15:

\[
\|Bc_L\|_2\approx6.61\times10^{-6},\qquad
\sigma_{\min}(T_{15})\approx1.19\times10^{-1},
\]

hence

\[
\|c_T\|_2\le5.55\times10^{-5},
\]

versus actual finite tail norm \(6.06\times10^{-6}\).

For cutoff N=17:

\[
\|Bc_L\|_2\approx8.05\times10^{-7},\qquad
\sigma_{\min}(T_{17})\approx5.71\times10^{-1},
\]

so the finite resolvent inequality gives

\[
\boxed{\|c_T\|_2\le1.41\times10^{-6}}.
\]

The actual finite tail norm is

\[
\|c_T\|_2\approx8.24\times10^{-7}.
\]

The actual finite weighted derivative tail at this cutoff is

\[
\|Dc_T\|_2\approx2.20\times10^{-5}.
\]

A crude finite-dimensional conversion of the L2 resolvent bound gives roughly \(4.21\times10^{-5}\) for the weighted tail, but this uses the largest frequency present in the finite M=20 block and is **not** an infinite-dimensional H1 bound.

## Interpretation

The new evidence supports the following mechanism:

1. The exceptional n=11 shoulder is associated with a nearly singular local/tail structure in the projected matrix.
2. Once that shoulder is passed, the finite high-mode block becomes substantially more invertible.
3. The forcing \(Bc_L\) from the stabilized low modes simultaneously becomes very small.
4. The projected equation then forces a small tail through
   \[
   c_T=-T_N^{-1}Bc_L.
   \]

This is substantially stronger than observing a good exponential fit: it identifies an operator equation that can, in principle, yield a provable coefficient bound.

## What remains open

The present result is still finite-dimensional.  To turn it into an analytic tail theorem, one must prove an infinite-dimensional statement of the form

\[
\inf_{N\ge N_0}\sigma_{\min}(T_N^{(\infty)})\ge\delta>0
\]

in an appropriate tail space, or an equivalent coercivity / diagonal-dominance / compact-perturbation estimate, together with a quantitative decay bound on the low-to-tail forcing \(B_Nc_L\).

Nothing in this checkpoint proves:

- strong H1 convergence of the full sequence,
- nontriviality of \(\ker G_1\),
- \(\lambda_1=0\),
- RH or GRH,
- or the Section-8 lambda=-5 admissibility condition.

## v13.298 target

Derive asymptotics of the high-mode matrix entries \(A_{mn}\) from the one-dimensional overlap formula, with special attention to:

- diagonal asymptotics \(A_{nn}\),
- off-diagonal decay in \(|m-n|\) and \(m+n\),
- the effect of the \(t\log t\) cusp,
- prime-power kink contributions,
- whether the high-mode tail is a coercive diagonal operator plus a summable/compact perturbation.

That is the natural route to upgrading the finite singular-value pattern into a genuine infinite-tail resolvent estimate.
