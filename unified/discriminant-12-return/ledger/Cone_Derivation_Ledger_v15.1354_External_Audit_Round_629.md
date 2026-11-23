# Cone Derivation Ledger v15.1354 — External Audit Round 629

**Date:** 2026-11-23
**Track:** External Audit
**Scope:** Independent verification of v15.1351, v15.1352, v15.1353 (Gravity)

## Method

`git fetch origin master` found `993539c` as the new head, six new Gravity commits since the last audit push (Round 628, v15.1350, `865681c`): v15.1351 (ADM momentum), v15.1352 (six spatial Einstein components), v15.1353 (all ten 4D Einstein components in one consistent geometry). `git merge --ff-only` applied cleanly. No version collision this round. All three entries flag their canonical GitHub scripts as not yet independently replayed.

This round completes the program begun in Round 628 (v15.1349's independent ADM Hamiltonian): together, v15.1349/1351/1352/1353 now cover all ten independent linearized Einstein field equations (1 Hamiltonian + 3 momentum + 6 spatial), each reconstructed from genuinely independent real-space metric slices via spatial FFT derivatives and centered time differences — not by reusing the scalar/vector/tensor mode-equation accelerations that sourced the fields. v15.1353 additionally unifies all ten into one single consistent 4D Christoffel/Ricci calculation, superseding the separate ADM-style derivations of v15.1349/1351 as a redundant cross-check rather than a replacement.

## v15.1351 (Gravity) — independent ADM three-momentum constraints

**Gates 1267-1269.** Extends v15.1349's real-space Hamiltonian-only pattern to the three momentum constraints `M_i=D_j(K^j_i-δ^j_iK)`, built from FFT spatial gradients of the assembled metric and centered time differences across three separately-assembled slices, compared against an independently constructed Maxwell+K4-solid momentum (using the previously-Audited vector-minus convention `φ^I=x^I-f^I`).

**Independently re-executed the actual committed script** at N=12 (dt=0.005/0.0025), N=16 (dt=0.003), N=24 (dt=0.0025/0.00125), and N=32 (dt=0.002). Every value matched the ledger's Gate 1269 table, including both load-bearing falsification controls (omitting the solid or Maxwell momentum inflates the residual by 2-3 orders of magnitude at every grid) and the ~4× dt-halving ratio confirming O(dt²) temporal convergence. A handful of values differed from the ledger's quoted figures only at the 13th-15th significant digit (e.g. `9.321032646419239e-08` here vs. `9.321032646418692e-8` quoted) — consistent with ordinary floating-point reduction-order noise already established as non-substantive throughout this audit, not a discrepancy.

## v15.1352 (Gravity) — independent six-component spatial Einstein tensor

**Gates 1271-1273.** A materially stronger test: builds the actual linearized 4D Christoffel symbols and Ricci tensor directly from five independently-assembled real-space metric slices (τ-2dt...τ+2dt), rather than any ADM shortcut, then forms `δG^i_j` and compares against an independently-rebuilt Maxwell stress tensor (reconstructed a second time from the raw E0, not reused from the metric solver's SVT projections) plus the K4 solid's direct constitutive stress. The entry's disclosed debugging history is notable and exactly the kind of honest self-correction this audit exists to encourage: an initial implementation mis-indexed the time-derivative metric tensor (producing asymmetric Christoffels), and after fixing that, a second bug surfaced where the k=0 Maxwell pressure tensor was filled by an incorrect diagonal-vector broadcast rather than a true diagonal matrix — both are disclosed rather than silently corrected, with the final script avoiding the second trap by rebuilding the Maxwell tensor independently.

**Independently re-executed the actual committed script** at N=12 (dt=0.006/0.003), N=16 (dt=0.004), and N=24 (dt=0.003/0.0015). Every value matched the ledger's Gate 1273 table (again modulo the same sub-roundoff digit noise), including: the dt-halving ratios (~4 at both N=12 and N=24), the connection-symmetry assertion (`<1e-12`), both omission controls at every grid (255×-24184× residual inflation, matching the ledger's quoted factors), and the independently-tracked trace-residual convergence (`3.5054e-6→8.7699e-7` at N=12, `1.8775e-5→4.7012e-6` at N=24).

## v15.1353 (Gravity) — all ten components from one consistent 4D geometry

**Gates 1275-1277.** Extends v15.1352's five-slice 4D Ricci construction to extract `δG^0_0`, `δG^0_i`, and `δG^i_j` from the *same* computed connection and Ricci tensor in a single pass, rather than three separately-derived ADM-style quantities — closing the explicit concern v15.1352's own Gate 1274 raised (that v15.1349/1351's ADM normal-normal/mixed-momentum conventions might not exactly match a direct mixed-index 4D contraction).

**Independently re-executed the actual committed script** at N=12 (dt=0.006/0.003), N=16 (dt=0.004), and N=24 (dt=0.003/0.0015). Every value matched the ledger's Gate 1277 table exactly (modulo the same established roundoff noise): all three residual classes (`max_00`/`max_0i`/`max_residual`) and their six omission controls at every grid, and the ~4× dt-halving ratio for each of the three residual classes independently at both N=12 and N=24, confirming consistent O(dt²) convergence across the whole unified calculation, not just one sector.

## Verdict

**PASS (all three entries).** This completes a genuinely independent, real-space reconstruction of all ten linearized Einstein field equations for the common Maxwell+K4 weak-field metric — the strongest verification chain in this project to date, since none of it reuses the scalar/vector/tensor mode-equation accelerations that originally sourced the fields. v15.1352's disclosed two-bug debugging history is itself a positive signal: the final committed script is the corrected version, the broken intermediate versions are preserved in the ledger text rather than erased, and the fixes (proper time-derivative indexing, an independently-rebuilt rather than broadcast Maxwell tensor) are the kind of concrete, locatable corrections this audit discipline exists to catch. All three entries remain correctly scoped as linearized, weak-field (A=0.1), and silent on continuum convergence, nonlinear backreaction, or any causal optical observable.

## Collision and freshness checks

"Round 629" and `v15.1354` both confirmed unused before this write. No gate-number collisions found (Gates 1267-1278 unused elsewhere). No version collisions this round. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening changes.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
