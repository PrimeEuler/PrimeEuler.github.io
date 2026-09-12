# Cone Derivation Ledger v13.403 — Odd-Parity Source Validation and Finite Schur Diagnostic

Date: 2026-09-12

Status labels: **[D]** exact derived, **[N]** numerical, **[O]** open.

## 1. Purpose

After v13.402 transferred the certified ten-mode Schur index bound to the full even-v sector, begin an independent audit of the odd-v parity sector at a=1.

The Dirichlet basis is

\[
\psi_n(x)=\sin\frac{n\pi(x+1)}2.
\]

Odd functions about x=0 correspond to even mode number n.

## 2. Pole channel in odd parity

For n even, write k_n=n\pi/2.  Up to a basis sign,

\[
\psi_n(x)=\sin(k_n x).
\]

The pole channel is now the sinh channel. Direct integration gives

\[
\int_{-1}^1 \sin(kx)\sinh(x/2)\,dx
=
\frac{2[(1/2)\sin k\cosh(1/2)-k\cos k\sinh(1/2)]}{k^2+1/4}.
\]

For k=n\pi/2 with n even, \(\sin k=0\), so after absorbing the basis sign the coefficient magnitude is

\[
\boxed{
 d_n=\frac{2k_n\sinh(1/2)}{k_n^2+1/4}.
}
\]

Therefore the odd-sector pole contribution is again positive rank one:

\[
\boxed{P_{\rm pole}^{\rm odd}=2dd^T\succeq0.}
\]

The sign assigned to each d_n depends on basis convention and does not affect the rank-one operator.

## 3. Source-faithful smooth block transfers to same-parity even indices

The source-faithful post-integration-by-parts archimedean block remains

\[
K_{\rm arch}(m,n)
=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2},
\qquad m\ne n,
\]

for same-parity even indices as well.

As a direct source-level regression, numerical double integration of

\[
-\iint_{[-1,1]^2}h(|x-y|)\psi_m(x)\psi_n(y)\,dx\,dy
\]

was compared with the closed form. Representative values:

- (m,n)=(2,4): direct -0.01385262473258, closed -0.01385262473216;
- (2,6): direct -0.00914408910579, closed -0.00914408933448;
- (4,8): direct -0.00323486066029, closed -0.00323486065903.

The residual in the (2,6) pair is consistent with the deliberately ordinary adaptive double quadrature tolerance; the sign and scale agree, and the other pairs agree at ~1e-12.

The cusp and prime same-parity formulas are unchanged structurally; the only parity-specific low-rank change is the pole cosh/sinh channel.

## 4. Odd-sector finite Schur setup

Use

\[
C_{\rm odd}=\{2,4,\ldots,20\},
\qquad
D_M=\{22,24,\ldots,M\}.
\]

Define

\[
S_{10}^{\rm odd}(M)
=A_{CC}-A_{CD_M}A_{D_MD_M}^{-1}A_{D_MC}.
\]

The full odd-sector pole term 2dd^T is included.

## 5. Numerical diagnostics

Fresh dense source-faithful calculations give the following first Schur levels.

### M=100

\[
(5.23\times10^{-15},
2.31\times10^{-14},
2.00\times10^{-10},
3.96\times10^{-6},
1.026\times10^{-2},
0.653,
1.517,\ldots)
\]

with finite-high gap

\[
\lambda_{\min}(A_{D_MD_M})\approx0.5562.
\]

### M=200

\[
(4.69\times10^{-15},
2.30\times10^{-14},
1.84\times10^{-10},
3.78\times10^{-6},
9.35\times10^{-3},
0.652,\ldots)
\]

and high gap ~0.5451.

### M=400

\[
(4.75\times10^{-15},
2.26\times10^{-14},
1.79\times10^{-10},
3.60\times10^{-6},
8.79\times10^{-3},
0.652,\ldots)
\]

and high gap ~0.5393.

### M=800

\[
\boxed{
(4.11\times10^{-15},
2.28\times10^{-14},
1.74\times10^{-10},
3.47\times10^{-6},
8.49\times10^{-3},
0.652,\ldots)
}
\]

with high gap ~0.5364.

## 6. Interpretation

These are finite-section midpoint diagnostics only.

The odd sector appears structurally easier than the even sector:

- two directions remain at ordinary-double numerical-zero scale;
- the third is small but positive at ~1.7e-10;
- the fourth is already ~3.5e-6;
- the fifth is ~8e-3;
- the finite high block is strongly positive, with gap above 0.53 throughout the tested range.

A plausible next certification target is therefore an odd-sector finite-index theorem with a terminal obstruction dimension no larger than 2 or 3. This is not yet proved.

## 7. Guardrails

- The first two tiny values are not called exact kernels.
- The third positive finite-section value is not yet an infinite-dimensional theorem.
- No odd-sector inertia theorem is claimed in this checkpoint.
- No combination with v13.402 is yet used to state a full-parity index bound.
- No RH, GRH, exact-zero, or lambda_1=0 claim follows.

## 8. Next target

Exploit the much larger odd-sector high-block gap to certify a low-dimensional positive subspace using the same fixed-dyadic / residual-Gram architecture as v13.399-v13.401. A seven- or eight-dimensional positive frozen subspace should be tested first; if successful it would give an odd-sector nonpositive index bound of at most three or two, respectively.
