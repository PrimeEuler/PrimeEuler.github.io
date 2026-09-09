# Cone Derivation Ledger v13.378
## Corrected Rank-4 Cross Reconstruction and Centered Arch Channel

### Status
Audit repair continues from v13.373--v13.377.  The corrected archimedean off-diagonal formula is now used throughout.  This checkpoint rebuilds the finite-to-tail cross geometry from that intended operator.  All cross norms below are midpoint diagnostics unless explicitly stated otherwise.

### Exact corrected cross formula
For odd finite-side mode m and tail mode n,

\[
G_{mn}=\frac{2}{\pi}\frac{nU_m-mU_n}{m^2-n^2}
+\pi mn\frac{Y_n-Y_m}{m^2-n^2},
\]
with
\[
U_j=\operatorname{Si}(j\pi)+2A_j,\qquad Y_j=jH_j.
\]

The asymptotic center from v13.377 is
\[
c_\infty=\frac{2}{\pi}\frac{e^{-1}}{1-e^{-4}}\approx0.23856886732122662.
\]
Since only differences \(Y_n-Y_m\) occur, replacing \(Y_j\) by
\[
\widetilde Y_j=Y_j-c_\infty
\]
is exact.  Two integrations by parts give \(\widetilde Y_j=O(j^{-2})\).  Hence the second displacement pair can be written using
\[
P_j=j,\qquad Q_j=j\widetilde Y_j=O(j^{-1}),
\]
instead of the badly conditioned raw generator \(jY_j=O(j)\).

### Independent scalar reconstruction used for midpoint cross tests
The arch sine transform was evaluated without oscillatory quadrature using
\[
h(t)=\sum_{k\ge0}e^{-(2k+1/2)t}-\frac1{2t},
\]
which gives
\[
H_n=b\sum_{k\ge0}\frac{1+e^{-2a_k}}{a_k^2+b^2}-\frac12\operatorname{Si}(n\pi),
\quad a_k=2k+\frac12,\ b=\frac{n\pi}{2}.
\]
The non-exponential sum was evaluated by the complex-digamma identity and the exponential correction by a rapidly convergent direct sum.  Spot checks at n=21 and n=101 agreed with direct adaptive quadrature at approximately 5e-16 and 2e-15 respectively.

### Corrected near-band midpoint norm
A fresh matrix-free power iteration was applied to the actual corrected formula on
\[
F=\{21,23,\ldots,16001\},\qquad
T_{\rm near}=\{16003,16005,\ldots,60003\}.
\]
The iterates were
\[
0.86319,\ 0.91753,\ 0.93181,\ 0.93811,\ 0.94104,\ 0.94239,\ 0.94300,\ldots
\]
so the corrected near norm is targeting
\[
\boxed{\|G_{F,T_{\rm near}}^{\rm corr}\|\approx0.9432.}
\]
This is essentially the same scale as the superseded legacy diagnostic 0.9432312, but it is now obtained from the corrected operator.

### Corrected first remote-band midpoint norm
For
\[
T_{\rm rem,1}=\{60005,60007,\ldots,120003\},
\]
the same matrix-free iteration converged rapidly to
\[
\boxed{\|G_{F,T_{\rm rem,1}}^{\rm corr}\|\approx0.28024594.}
\]
The first iterates after the random start were 0.28022268, 0.28024594, 0.28024594.

### Combined finite band diagnostic
A combined iteration on
\[
16003\le n\le120003
\]
reached approximately 0.94532 after two power steps following the random start.  This is not yet converged enough to record as the final midpoint full-band norm, but it shows that the corrected remote block is strongly aligned with the same low-dimensional channel structure rather than adding in quadrature at its standalone norm.

### Consequence for certification architecture
The old v13.364/v13.365 single-Z cross certificate is superseded.  The repaired certificate should use two exact Cauchy channels:

1. cusp+prime pair \((U,n)\), coefficient \(2/\pi\);
2. centered arch pair \((n,n\widetilde Y)\), coefficient \(\pi\).

For separated m<n,
\[
\frac1{m^2-n^2}=-\frac1{n^2}\sum_{k\ge0}(m/n)^{2k},
\]
so each channel has the same admissible low-rank far-field expansion.  The centered arch generator improves the tail because \(n\widetilde Y_n=O(n^{-1})\).

### Finite-block status carried forward
The corrected 7991-mode factor remains numerically strong:
\[
\min d_j\approx0.25547908458536,
\]
with streaming midpoint
\[
y_{\max}\approx18.13687509296,
\]
and crude a-posteriori residual allowance approximately
\[
9.72\times10^{-8}.
\]
The proof-grade directed-rounded residual replay is still required before reinstating
\[
A_{0,[21,16001]}\succeq0.22I.
\]

### Next target
1. Re-run the local-defect arithmetic certificate in the centered rank-4 gauge and produce a new validated finite-block transcript.
2. Build the corrected remote Cauchy expansion with both generator pairs and an explicit geometric remainder.
3. Re-certify a rounded full cross target, preferably \(\|G\|<1\).
4. Combine with a robust analytic tail gap, preferably \(\alpha_{16003}\ge4.65\), to restore positivity of the entire high complement.
5. Only then return to the full 10-dimensional Schur core and any global inertia statement.

### Guardrail
No exact-zero, RH, GRH, or global-index conclusion follows from this checkpoint.  The cross values are numerical midpoint diagnostics, not interval-certified bounds.