# Cone Derivation Ledger v13.318

## Active prime-tail rank-one asymptotic and matrix Feshbach channel

This checkpoint continues v13.317's four-dimensional active-core reduction for Suzuki's a=1 even-v sector.

### Setup

Let the low coordinate core be the odd Dirichlet modes

\[
\mathcal C_{19}=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\},
\]

and let \(q^{(1)},\ldots,q^{(4)}\) be the first four high-precision eigenvectors of its 10x10 matrix.  Their eigenvalues are approximately

\[
1.12389415799\times10^{-20},\quad
9.41881201677\times10^{-16},\quad
1.12143957393\times10^{-11},\quad
4.76556003061\times10^{-8}.
\]

The joint prime matrix uses the corrected v13.315 formula (externally rechecked in audit round 17):

\[
(B_{\rm prime})_{mn}
=-\frac4\pi\frac{nA_m-mA_n}{n^2-m^2},
\qquad
A_j=\sum_{q\in\{2,3,4,5,7\}}
\frac{\Lambda(q)}{\sqrt q}\sin\!\left(\frac{j\pi}{2}\log q\right).
\]

The superseded v13.314 sign convention is not used.

## Exact fixed-active asymptotic

For an active vector \(q^{(j)}=(q_m^{(j)})\), define

\[
L_j=\sum_{m\le19,\;m\;{\rm odd}}q_m^{(j)}A_m.
\]

Then its prime coupling to tail mode \(n\) is

\[
g_j(n)=\sum_m q_m^{(j)}(B_{\rm prime})_{mn}.
\]

Using

\[
\frac{1}{n^2-m^2}=\frac1{n^2}\left(1+O_m(n^{-2})\right),
\]

one obtains the exact asymptotic structure

\[
\boxed{
 g_j(n)=-\frac4\pi\frac{L_j}{n}+O(n^{-2})
}
\]

for each fixed active direction.

At 60-digit core precision,

\[
\boxed{
L\approx
(1.346563376261008,
-0.922660608056208,
-0.716115296391596,
-0.370500756277872).
}
\]

Thus the leading coefficient does not vanish direction-by-direction.  The gain is instead matrix-valued.

## Rank-one tail Gram channel

Let \(G_N\) denote the prime map from the four-dimensional active subspace into odd tail modes \(n\ge N\).  Then

\[
G_N^*G_N
=
\frac{16}{\pi^2}
\left(\sum_{\substack{n\ge N\\n\;{\rm odd}}}\frac1{n^2}\right)
LL^T
+\text{lower-order terms}.
\]

Therefore

\[
\boxed{
\text{the leading remote prime-tail correction on }\mathcal A_4
\text{ has rank one.}
}
\]

Only the active combination parallel to \(L\) carries the leading \(N^{-1/2}\) prime-tail coupling.  Three orthogonal active combinations have no leading \(1/n\) channel and begin at lower order.

This is stronger structural information than a single scalar bound \(\|G_N\|\): the matrix geometry of the tail is highly anisotropic, just as the finite-buffer Feshbach correction was in v13.316-v13.317.

## Exploratory direct projected-tail sums

A direct finite-tail summation through mode 50001, with only the leading rank-one asymptotic appended beyond that point, gives the following descriptive operator norms:

\[
\begin{array}{c|c}
N & \|G_N\|\\ \hline
237 & 0.10670\\
301 & 0.09464\\
401 & 0.08196\\
501 & 0.07330\\
701 & 0.06195\\
1001 & 0.05183
\end{array}
\]

At \(N=401\), the projected prime-tail Gram eigenvalues are numerically of the scale

\[
\sim 5\times10^{-14},\qquad
5\times10^{-11},\qquad
6.7\times10^{-3},
\]

with the fourth numerical eigenvalue at roundoff scale.  Hence the leading channel dominates overwhelmingly.

These direct-sum decimals are exploratory and not interval-certified.  The rank-one leading asymptotic itself is analytic.

## Consequence for the Feshbach strategy

The active-space reduction should no longer subtract a scalar remote-tail penalty from all four directions.  Instead, the proof architecture should retain a 4x4 matrix correction whose leading prime part is explicitly rank one:

\[
\mathcal A_4
\oplus
\mathcal C_{\rm stiff}
\oplus
\mathcal B
\oplus
\mathcal T.
\]

The next target is to derive an explicit rigorous remainder matrix bound for

\[
G_N^*G_N-
\frac{16}{\pi^2}
\left(\sum_{n\ge N,\;n\;{\rm odd}}n^{-2}\right)LL^T,
\]

and then add the cusp and archimedean active-tail corrections.  If those remainder matrices are small in the three directions orthogonal to \(L\), the infinite complement will reduce to one dominant tail channel plus three much more strongly protected active directions.

## Proof status and guardrails

- v13.315's joint-prime matrix formula is the formula used here; external audit round 17 independently verified it.
- The rank-one leading asymptotic is analytic for the fixed four-dimensional active space.
- The displayed projected-tail Gram eigenvalues and norms are ordinary floating diagnostics, not interval enclosures.
- No exact zero mode, spectral multiplicity, \(\lambda_1=0\), RH, or GRH conclusion is made.
- The four-dimensional active subspace remains a numerical/model-reduction choice, not a claim of four-dimensional kernel.

## Files

- `research-notes/suzuki_active_prime_tail_rank_one.py`
- `ledger/Cone_Derivation_Ledger_v13.318_Active_Prime_Tail_Rank_One_Asymptotic_and_Matrix_Feshbach_Channel.md`
