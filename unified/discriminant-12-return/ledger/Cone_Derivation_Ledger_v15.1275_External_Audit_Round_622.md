# Cone Derivation Ledger v15.1275 — External Audit Round 622

**Date:** 2026-11-21
**Track:** External Audit
**Scope:** Independent verification of v15.1273 (Gravity) and v15.1274 (Gravity)

## Method

`git fetch origin master` found `5960766` as the new head, two new Gravity entries since the last audit push (Round 621, v15.1272, `da27e84`), plus this thread's own intervening liveness note (`v15.1273`, commit `d17f1c3`). `git merge --ff-only` applied cleanly. Both new entries explicitly flag that the committed scripts had **not yet** been independently executed (their quoted tables came from separately-authored local scripts) — so both were run from the actual committed bytes rather than taken on their word.

## Collision note — this thread's own v15.1273 vs. Gravity's v15.1273

This thread's liveness note was written and pushed as `Cone_Derivation_Ledger_v15.1273_External_Audit_Liveness.md`, commit `d17f1c3` (2026-11-21T00:27:27Z). Gravity's own `v15.1273` entries landed afterward: `8e75d7a` (ledger-adjacent script/table, 2026-11-21T00:59:51Z) and `e807bf4` (the v15.1273 ledger entry itself, 2026-11-21T01:00:17Z) — both real, already-committed commits, unlike the v15.1271/v15.1272 draft collision in Round 621 where this thread's file had not yet been committed. Per the established collision protocol (priority to the earlier commit by actual UTC timestamp), this thread's `v15.1273` has priority since `00:27:27Z < 00:59:51Z`. Gravity's `v15.1273`-named files are flagged here as the losing side of a sequential collision but are **not** renamed, edited, or touched — that is Gravity's call to make on its own files. No ledger content was altered.

## v15.1273 (Gravity) — native-grid vs. dealiased Maxwell source coefficients genuinely differ

**Gate 1221/1222.** Holds the Maxwell initial data and propagation fixed, and compares the *nonlinear* stress coefficients (ρ, Poynting flux, stress tensor) computed two ways: native N³ FFT of the pointwise products (the original v15.1262/v15.1267 scheme) vs. 2N³ zero-padded/dealiased products (the v15.1269/v15.1271 scheme). The claim that the k=0 (mean) coefficient agrees to machine precision while nonzero-mode coefficients disagree is structurally expected: the discrete mean of a pointwise product is just an average of values at coincident, correctly-resolved grid points, which oversampling reproduces exactly, whereas the nonzero Fourier coefficients are exactly where aliasing from the quadratic nonlinearity lands — consistent with the already-independently-confirmed v15.1269 aliasing mechanism, now characterized mode-by-mode rather than only via the Ward-identity residual.

**Independently re-executed the actual committed script** (`k4_native_dealiased_source_comparison_v15_1273.py`) at N=16/24/32/40/48. Every value matched the ledger's two tables exactly, bit-for-bit:
- Retained-band (`|m_j|<N/3`) relative discrepancies for ρ/flux/stress: `0.1695088411/0.6556348279/0.3486002016` (N=16) down to `0.0010909706/0.0036626615/0.0024600721` (N=48) — all five grids matched exactly.
- Fixed low-mode (`|m_j|≤2`) relative discrepancies: N=32 `4.03e-5/3.10e-4/1.67e-4` and N=48 `7.14e-6/9.84e-7/1.35e-5` — matched exactly (to the full precision printed: `4.028848101785166e-05`, `0.00030960172627252883`, `0.0001667470216650913`, `7.14024806616368e-06`, `9.843103869096715e-07`, `1.3518251651170849e-05`).
- `mean_error` at every grid was `0.0` or `~1.08e-19` (sub-roundoff), matching the entry's claim that homogeneous energy agrees even where the anisotropic spectral content does not.

The entry's own conclusion — that matching k=0 homogeneous energy is *not* sufficient to certify that one inhomogeneous metric solution satisfies both the native-grid trace test and the dealiased Ward test — is a correct and appropriately cautious reading of its own numbers; nothing here overclaims.

## v15.1274 (Gravity) — dealiased stress projected back onto native interior modes

**Gates 1224/1225.** Builds a single, declared-consistent stress-source candidate: evolve the Maxwell field on the native grid as before, but form the nonlinear products on a 2N-padded grid (factor `(2N/N)³=8` in the inverse transform, matching the already-verified v15.1271 dealiasing convention), then Fourier-transform and **project the resulting dealiased stress back down** onto the native grid's non-Nyquist interior wavevectors (`|m_j|<N/2`, excluding self-conjugate Nyquist planes). This is a controlled restriction of an already-conserved field, so near-exact conservation (~1e-18) on the retained modes is the expected and unsurprising outcome, not a new physical result — correctly scoped as such in the entry's own text.

**Independently re-executed the actual committed script** (`k4_dealiased_projected_source_v15_1274.py`) at the same five grids. Every value matched the ledger's Gate 1225 table exactly, bit-for-bit: energy/momentum residuals from `1.7261844907016647e-19`/`3.278433135308526e-19` (N=16) through `1.3196203225915552e-18`/`1.1058496363211556e-18` (N=48), and mode counts `3375/12167/29791/59319/103823`. The two cross-check `mean_rho` values also matched exactly: N=32 `0.0007676608970155843`, N=48 `0.0007786954245360609`.

## Verdict

**PASS (both entries).** v15.1273 correctly identifies and quantifies a genuine source-representation inconsistency (native vs. dealiased stress coefficients disagree away from k=0) without overclaiming a fix; v15.1274 correctly constructs and verifies a declared-consistent projected source as the next falsification-first candidate. Both remain explicitly scoped as Maxwell-side source bookkeeping, not a solved metric, Einstein–K4 constraint closure, or a new physical interaction — consistent with every other entry in this chain since Round 620.

## Collision and freshness checks

"Round 622" and `v15.1275` both confirmed unused before this write. The `v15.1273` collision with Gravity is handled per the note above (priority to this thread's earlier real commit timestamp; Gravity's files left untouched). No gate-number collisions found (Gates 1221–1226 unused elsewhere). `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
