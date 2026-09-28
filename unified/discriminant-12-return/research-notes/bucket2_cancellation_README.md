# Bucket 2 cancellation-mechanism scripts (L₀+L₁=0)

Sandbox tools behind ledger v13.846 (Sandbox Bucket 2). Status: **[I]/[O] exploratory — not certified.**

## What this is

These scripts dissect *why* the Tikhonov-regularized (8.5) least-squares solve picks
affine coefficients satisfying the cancellation \(\ell(A)=A\cdot A_{\mathrm{coef}}+B_{\mathrm{coef}}=o(e^A)\),
i.e. the empirical \(L_0+L_1=0\) with \(|L_0|=|L_1|\approx0.48\).

Core finding (v13.846): eliminating \(v\) gives
\((A^*,B^*)=\arg\min\,\|P_{\ker(K^T)}(e^x+Ax+B)\|^2\) — the affine minimizing the
unresolvable ker-component. Parity makes \(M_{\ker}=X^TP_{\ker}X\) diagonal, so
\(\ell^*(A)=-\langle w_A,P_{\ker}e^x\rangle\) exactly
(\(w_A\) = minimal-norm "evaluate at \(x=A\)" representer in \(\ker(K^T)\));
the cancellation is asymptotic orthogonality \(w_A \perp P_{\ker}e^x\).

## Files

| file | role |
|---|---|
| `bucket2_cancellation_screw.py` | `D12Screw` — D12 screw kernel, kink-faithful `g_fast` (never differentiates `g`), from the natural-BC run |
| `bucket2_cancellation_lsq85.py` | `Lsq85` — regularized least-squares discretization of Suzuki (8.5), \(K v = -e^x - Ax - B\) |
| `bucket2_cancellation_anatomy1_ls_dissection.py` | dissect the discrete (8.5)-LS problem; verify \(\ell(A)=o(e^A)\) |
| `bucket2_cancellation_anatomy2_preimages.py` | where \(v_*\) lives; preimages \(p_0=K^\dagger e^x,\ p_1=K^\dagger x,\ p_2=K^\dagger 1\) |
| `bucket2_cancellation_anatomy3_preimage_shapes.py` | shapes of \(p_0,p_1,p_2\); projection of \(p_0\) onto span\(\{p_1,p_2\}\) |
| `bucket2_cancellation_anatomy4_optimality.py` | optimality condition for \(\ell_A=A\cdot A_{\mathrm{coef}}+B_{\mathrm{coef}}\) |
| `bucket2_cancellation_anatomy5_singular_vectors.py` | small-\(\sigma\) singular vector anatomy (boundary layers?) |
| `bucket2_cancellation_anatomy6_ker_selection.py` | \(\arg\min_a\|P_{\ker}(Xa+f)\|^2\) vs the full solve; \(W_\alpha\) objective across \(\sigma\) |
| `bucket2_cancellation_anatomy7_ker_concentration.py` | where \(P_{\ker}\) concentrates; the \(2\times2\) ker system \(M_{\ker}a+b_{\ker}=0\) |
| `bucket2_cancellation_anatomy8_a_scaling.py` | \(A\)-scaling of the ker mechanism; corr\((w,P_{\ker}f)\); (−)-channel parity check |

## Running

All eleven files must sit in the **same directory**; each `anatomy*` script adds its own
directory to `sys.path` and imports the two library modules by their posted names.
Dependencies: `numpy`, `scipy` only. No data files.

Example: `python bucket2_cancellation_anatomy6_ker_selection.py`

Typical cost: the `D12Screw(tmax=12.0)` kernel build dominates (tens of seconds);
`anatomy8` sweeps \(A=2,3,4,5\) and takes several minutes.

## Provenance

Adapted from the sandbox run `20260928-200000-bucket2-cancellation-mechanism`
(`anatomy1–8.py`), whose library code came from the natural-BC run
`20260928-165927-bucket2-natural-bc` (`screw.py`, `lsq85.py`).
Only the `sys.path` inserts and module import names were changed for portability;
the numerics are untouched. Full narrative: the run's `report.md` (sandbox only).
