# Cone Derivation Ledger v14.926 — Pantheon+ FULL-COVARIANCE k4-vs-ΛCDM return (Sandbox, closing v14.923's handoff)

Date 2026-10-26. Sandbox lane. Parent v14.923 (diagonal diagnostic + handoff), v14.921–922 (k4 optical distances/benchmark), v14.916/919 (scope: conditional mathematical metric). Payload `payloads/pantheon_fullcov_v14_926/` (pantheon_fullcov.py, NOTE.md, results.json). Official data (PantheonPlusSH0ES DataRelease): Pantheon+SH0ES.dat sha256 1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8; Pantheon+SH0ES_STAT+SYS.cov (1701×1701) sha256 abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc. Data files referenced by URL + hash, not redeposited (33 MB).

## Validation [V]

The pipeline reproduces v14.923's diagonal diagnostic EXACTLY (offsets 23.88812562 / 23.80256474; χ² 786.1217145 / 697.6175999; Δχ² +88.5041146) with the entry's selection (zHD>0.01, IS_CALIBRATOR==0, zHEL>0, m_b_corr_err_DIAG>0; N=1580 of 1701) and models (d_k4 = (1+zHEL)·ln(1+zHD); d_Λ = (1+zHEL)·∫₀^zHD du/√(.315(1+u)³+.685); zHD in the distance, zHEL in the flux prefactor). Common additive magnitude offset profiled analytically per model in all constructions. dof = 1579.

## Covariance findings [N]

(1) The released matrix is symmetric to 3.0e-8 (print precision); symmetrized before use. (2) **√diag(.cov) is NOT the .dat column m_b_corr_err_DIAG** (median ratio 0.72; not a row permutation — sorted diagonals also differ). v := DIAG² − C_ii ≥ 0 on 1700/1701 rows (one row −1.4e-3, rounding scale), median v = 0.0221, comparable to C_ii itself: the .dat DIAG errors carry an extra nonnegative diagonal term the released matrix does not. Two constructions reported: **A** = released .cov as-is (the handoff's literal ask); **B** = A + diag(max(v,0)) — the like-for-like full-covariance upgrade of v14.923 (same per-point errors, full off-diagonal structure). (3) Conditioning benign: cond(A) = 460.2 (eigenvalues 5.20e-3…2.39), cond(B) = 201.4; Cholesky vs eigendecomposition solvers agree <1e-6 relative on every χ²; 1e-10 diagonal jitter moves χ² by ~3e-7.

## Results [N]

| construction | χ²_k4 | χ²_Λ (Ωm=.315) | Δχ² (k4 − Λ) |
|---|---|---|---|
| diagonal (v14.923) | 786.1217 | 697.6176 | **+88.5041** |
| A: released .cov | 1490.4849 | 1387.3597 | **+103.1252** |
| B: diag-restored | 765.7798 | 704.4419 | **+61.3380** |

In every construction, fixed-Ωm flat ΛCDM fits the Pantheon+ Hubble diagram better than the k4 coasting shape. The full covariance does not rescue the coasting shape: construction choice moves Δχ² (+61 to +103, bracketing the diagonal +88.5), never the ordering. χ²/dof < 1 throughout (0.45–0.94, conservative errors) — per the handoff, **no sigma/exclusion is stated**; a Δχ²→σ conversion is not justified on this likelihood as assembled. Scope: a data diagnostic on the conditional k4 metric; no physical gravity action, source, or G implied.

Flags: pantheon_full_covariance=COMPUTED_TWO_CONSTRUCTIONS; diagonal_reproduction=EXACT; cov_diag_mismatch=DOCUMENTED (v>=0, median 0.0221); conditioning=BENIGN (cond<=460); delta_chi2_full=+103.13 (A) / +61.34 (B); model_preferred=FULL-COV TOO: FLAT_LCDM; sigma=NOT_STATED_PER_HANDOFF; Suzuki_quarter=PARKED; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: pantheon-plus-full-covariance-return
parent: v14.926
status: open
action: Verify the exact diagonal reproduction, the v>=0 diagonal-term finding and the A/B construction distinction, conditioning claims, and the profiled chi2 values from the deposited script and official data hashes. Confirm no sigma was stated.
deliverable: scoped verdict.
