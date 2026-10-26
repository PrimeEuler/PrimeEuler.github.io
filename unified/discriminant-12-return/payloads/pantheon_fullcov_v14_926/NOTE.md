# Pantheon+ full-covariance k4-vs-LCDM return (v14.923 handoff to Sandbox)

Date 2026-10-26. Script `pantheon_fullcov.py`, numbers `results.json`.
Data (official PantheonPlusSH0ES DataRelease, 4_DISTANCES_AND_COVAR):
Pantheon+SH0ES.dat sha256 1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8;
Pantheon+SH0ES_STAT+SYS.cov sha256 abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc.
Selection and models IDENTICAL to v14.923 (zHD>0.01, IS_CALIBRATOR==0,
zHEL>0, m_b_corr_err_DIAG>0; N=1580 of 1701; d_k4=(1+zHEL) ln(1+zHD);
d_LCDM=(1+zHEL) int_0^zHD du/sqrt(.315(1+u)^3+.685)); common additive
magnitude offset profiled analytically per model in every construction.

## Validation gate
The v14.923 diagonal diagnostic reproduces EXACTLY in this pipeline:
offsets 23.88812562 / 23.80256474, chi2 786.1217145 / 697.6175999,
Delta chi2 = +88.5041146. Selection/conventions confirmed identical.

## Covariance findings (read before the chi2 table)
1. The released .cov is symmetric to 3.0e-8 (file print precision);
   symmetrized (C+C^T)/2 before use.
2. sqrt(diag(.cov)) is NOT the .dat column m_b_corr_err_DIAG (median
   ratio 0.72; not a permutation - sorted vectors also differ).
   v := DIAG^2 - C_ii >= 0 on 1700 of 1701 rows (one row -1.4e-3,
   rounding-scale), median v = 0.0221 (comparable to C_ii itself).
   The .dat DIAG errors carry an extra nonnegative diagonal term the
   released matrix does not. Two constructions are therefore reported:
   A = released .cov as-is (the handoff's literal ask);
   B = A + diag(max(v,0)) - the apples-to-apples full-covariance
   upgrade of v14.923 (same per-point errors, full off-diagonals).
3. Conditioning is benign: cond(A) = 460.2 (eigs 5.20e-3 .. 2.39),
   cond(B) = 201.4. Cholesky vs eigendecomposition solvers agree to
   <1e-6 relative on every chi2; a 1e-10 relative diagonal jitter
   moves chi2 by ~3e-7. No numerical-conditioning caveat attaches.

## Results (dof = 1579 after profiling one offset per model)
construction        chi2_k4     off_k4    chi2_LCDM   off_LCDM   Delta chi2
diagonal (v14.923)  786.1217    23.88813  697.6176    23.80256   +88.5041
A released .cov     1490.4849   23.88346  1387.3597   23.80152   +103.1252
B diag-restored     765.7798    23.88347  704.4419    23.80209   +61.3380

Reading: in every construction the fixed Om=0.315 flat LCDM fits
the Pantheon+ Hubble diagram better than the k4 coasting shape.
The full covariance does not rescue the coasting shape; restoring
the diagnostic's own diagonal errors (B) narrows the gap from
+88.5 to +61.3, the as-released matrix (A) widens it to +103.1 -
construction choice moves the number, not the ordering.
chi2/dof is < 1 in all constructions (0.45-0.94): the errors are
conservative, so per the handoff NO sigma/exclusion is stated -
a Delta chi2 -> sigma conversion is not justified on this
likelihood as assembled. This is a data diagnostic on a
conditional mathematical metric (v14.916/919): no physical
gravity action, source, or G is implied or derived.
