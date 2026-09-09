# Cone Derivation Ledger v13.365 — Six-Plane Full Cross Certificate and Global High-Complement Closure

## Status

This checkpoint closes the remaining high-complement cross inequality under the same validated-computational model used for v13.362–v13.363.

The valid global split remains

\[
\mathcal H_{\rm even}=\mathcal C_{10}\oplus\mathcal D,
\qquad
\mathcal D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\ \text{odd}\}.
\]

The three high-complement ingredients are now:

\[
A_{0,[21,16001]}\succeq0.22I,
\]

\[
\|A_{0,[21,16001],[16003,\infty)}\|<0.994<1,
\]

and

\[
A_{0,[16003,\infty)}\succeq \alpha_{16003}I,
\qquad \alpha_{16003}>4.6732.
\]

The robust tail gap uses the separately certified prime bound

\[
\|B_{\rm prime}\|<2.05.
\]

## Exact compressed cross sequence

With

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n,
\]

and the accelerated archimedean representation, the sine-integral terms cancel exactly:

\[
\boxed{
Z_n=2A_n+\Im\psi\!\left(\frac14+i\frac{n\pi}{4}\right)
+n\pi\sum_{k\ge0}\frac{e^{-2a_k}}{a_k^2+(n\pi/2)^2}
},
\qquad a_k=2k+\frac12.
\]

The cross entries remain

\[
(A_0)_{mn}=-\frac2\pi\frac{nZ_m-mZ_n}{n^2-m^2}.
\]

## Six-dimensional dominant subspace

A six-dimensional left subspace \(Q\) generated from the near tail captures the coherent dangerous channel.  Near-tail singular values in this subspace are approximately

\[
0.94351618,\ 0.77275372,\ 0.55774063,\ 0.46523877,\ 0.24530487,\ 0.19852204.
\]

The domain is split into

- \(N_0=[16003,60003]\),
- \(N_1=[60005,120003]\),
- \(N_2=[120005,4000003]\),
- \(N_3=[4000005,\infty)\).

For \(N_2\), a rank-8 Cauchy expansion through \(k=3\) is used.  Since

\[
\frac{16001}{120005}<0.134,
\]

the exact omitted Cauchy tail from \(k\ge4\) has operator norm below

\[
2.4\times10^{-9}.
\]

The untouched remote block obeys the crude direct estimate

\[
\|G_{N_3}\|<0.05.
\]

## Block certificate

The projected Gram through \(N_2\) has midpoint top eigenvalue about

\[
0.98377533.
\]

Charging the entire \(N_3\) PSD contribution against the six-plane gives the rounded upper target

\[
\boxed{a<0.987}.
\]

The invariance residual through \(N_2\) is about \(0.01924\).  Charging the entire \(N_3\) Gram contribution and the Cauchy truncation gives

\[
\boxed{r<0.022}.
\]

Frobenius complement controls are approximately

\[
0.13086,\quad0.03459,\quad0.03588,\quad0.05
\]

for \(N_0,N_1,N_2,N_3\) respectively.  Orthogonality of the domain blocks permits squared addition, yielding the rounded target

\[
\boxed{d<0.025}.
\]

Thus the block norm is controlled by

\[
\begin{pmatrix}
0.987&0.022\\
0.022&0.025
\end{pmatrix}.
\]

Its largest eigenvalue is below

\[
0.987503,
\]

hence

\[
\boxed{
\|A_{0,[21,16001],[16003,\infty)}\|<0.994<1.
}
\]

## Global high-complement positivity

The infinite Schur complement on the finite high block therefore satisfies

\[
A_{0,[21,16001]}-G A_{0,[16003,\infty)}^{-1}G^T
\succeq
\left(0.22-\frac{0.994^2}{4.6732}\right)I.
\]

Numerically the rounded lower margin is

\[
\boxed{>8\times10^{-3}}.
\]

In particular,

\[
\boxed{A_0|_{\mathcal D}>0}.
\]

Since the pole contribution is PSD in the even sector,

\[
A=A_0+P_{\rm pole}\succeq A_0,
\]

so also

\[
\boxed{A|_{\mathcal D}>0}.
\]

This is the key correction required by v13.348.  The infinite operator inertia may now be reduced exactly to the ten low modes through the Schur complement

\[
S_{10}=A_{CC}-A_{CD}A_{DD}^{-1}A_{DC}.
\]

## What is now closed

The earlier six-dimensional positive finite witness is no longer being used as a shortcut.  The correct entire high complement \(\mathcal D\) is positive first, and only then may global inertia be read from \(S_{10}\).

## Next target

Construct and certify the full ten-dimensional Schur complement \(S_{10}\), including the infinite high-complement solve.  Then certify six positive directions in \(S_{10}\) to obtain the global nonpositive-index bound.

## Guardrail

This is not an RH/GRH proof and does not establish an exact zero eigenvalue.  It closes the high-complement positivity step under the stated validated-computational and analytic-tail model only.
