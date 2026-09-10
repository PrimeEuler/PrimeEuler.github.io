# Cone Derivation Ledger v13.388 — Source-Faithful S10 Regression After Audit Resolution

Date: 2026-09-10

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[Audit]** correction/limitation, **[O]** open.

## 1. Purpose

After v13.387 resolved External Audit Round 20's overlap mistake, recompute the low-core finite Schur complement using the restored source-faithful rank-two Suzuki matrix and verify that the spurious five-negative pattern disappears.

Let

\[
C=\{1,3,\ldots,19\},\qquad D_M=\{21,23,\ldots,M\},
\]

and

\[
S_{10}^{(M)}=A_{CC}-A_{CD_M}A_{D_MD_M}^{-1}A_{D_MC}.
\]

The full pole term is included. The archimedean off-diagonal term is the v13.387-restored source-faithful expression

\[
K_{\rm arch}(m,n)=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2}.
\]

## 2. Fresh finite-section spectrum

**[N]** Direct dense solves give the first seven ordered eigenvalues:

### M=99
\[
(-1.6943\!\times10^{-14},-2.3996\!\times10^{-15},2.5001\!\times10^{-14},
1.7448\!\times10^{-12},4.4737466\!\times10^{-8},2.6917246\!\times10^{-4},0.8689992).
\]

### M=199
\[
(-1.6919\!\times10^{-14},-2.3669\!\times10^{-15},2.4919\!\times10^{-14},
1.4617\!\times10^{-12},4.2866188\!\times10^{-8},2.4993943\!\times10^{-4},0.8202557).
\]

### M=399
\[
(-1.6952\!\times10^{-14},-2.3574\!\times10^{-15},2.5442\!\times10^{-14},
1.4347\!\times10^{-12},4.1397603\!\times10^{-8},2.3434902\!\times10^{-4},0.7954523).
\]

### M=799
\[
(-1.6942\!\times10^{-14},-2.5683\!\times10^{-15},2.4835\!\times10^{-14},
1.3936\!\times10^{-12},4.0021343\!\times10^{-8},2.2468739\!\times10^{-4},0.7821459).
\]

## 3. Interpretation

**[Audit resolved]** The five clearly negative eigenvalues seen in the rank-four detour after v13.386 are absent. The restored source-faithful matrix reproduces the historical near-null pattern:

- four directions at ordinary-double numerical-zero scale;
- a fifth small positive finite-section direction near `4e-8`;
- a sixth positive direction near `2e-4`;
- the remaining directions separated at order one.

The fifth value decreases slowly with cutoff but remains positive in all tested finite sections. This is consistent with the pre-audit numerical record.

## 4. Regression invariant

The wrong derivative-overlap arch formula gives a fifth Schur eigenvalue near `-1.65e-3` by moderate cutoff. Therefore the sign/magnitude pattern itself is now a useful negative regression test:

\[
\lambda_5\sim-10^{-3}
\quad\Longrightarrow\quad
\text{suspect derivative-overlap/rank-four assembly.}
\]

The source-faithful branch instead has

\[
\lambda_5^{(399)}\approx4.14\times10^{-8}.
\]

## 5. Proof status

These are finite-dimensional midpoint diagnostics only. In particular:

- the first four tiny values are **not** certified exact zeros;
- the positive fifth finite-section value is not yet a certified positive eigenvalue of the full infinite Schur complement;
- no RH/GRH conclusion follows.

The next proof target is to bound the difference between a finite Schur complement and the exact infinite `S10`, while exploiting the already-established positivity of the high complement. Because the fifth direction is only `~4e-8`, a direct norm bound on the entire omitted Schur correction may be too coarse; the likely route is directional/low-rank residual certification rather than a uniform 10-dimensional norm estimate.
