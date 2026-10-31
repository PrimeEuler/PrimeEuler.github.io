# Cone Derivation Ledger v15.192 — Lane A v15.189 ledger-number collision repair

**Date:** 2026-10-30. **Lane:** A. **Type:** additive version-identity repair only. **Parents:** gravity v15.189 commit `9c2d9a1813468d4b6883f38b491e3e72bd4f2dc5`; Lane A coarse-screen commit `20216773fb68184f2980296d7676b17fbf658cc2`; gravity v15.190-v15.191.

## Fresh collision check

Immediately before this write, live `master` HEAD was `f93005ff3e3fde3309449edf0d1cd065cd8abf30` (gravity v15.191). No v15.192 ledger entry existed.

Two distinct v15.189 ledger entries landed seven seconds apart:

1. Gravity `Cone_Derivation_Ledger_v15.189_Corrected_2k_Nonresonance.md`, commit `9c2d9a1813468d4b6883f38b491e3e72bd4f2dc5`, blob `d48c548f51c4fb36b9e3a1faf596aa9883ba0b57`, committed first.
2. Lane A `Cone_Derivation_Ledger_v15.189_Lane_A_Coarse_MinMax_PreScreen_Probe.md`, commit `20216773fb68184f2980296d7676b17fbf658cc2`, blob `555bbfc46ab25588729269d442e52ca66dfa5e89`, committed second.

The gravity entry retains canonical identifier **v15.189**. This entry assigns canonical identifier **v15.192** to the Lane A coarse min-max pre-screen result. The original Lane A file and blob remain immutable provenance; references to “Lane A v15.189” should be read as **Lane A v15.192 (collision-repaired)**. No content, numerical value, inequality, or ownership claim from either original entry is changed.

## Lane A state preserved

The coarse first-100 approximate-diagonal probe remains `COARSE_MINMAX_PRESCREEN_INCONCLUSIVE` in both parity sectors. It did not certify globally sorted diagonals, interval radii, tail exclusion, a contour, spectral gap, or evaluated mathematical CI. The safe coarse comparison `M=15` versus observed sample gaps below `0.013` only shows that the v15.179 sufficient condition is too conservative for that probe; it is not evidence that the actual operator has no spectral gap.

Canonical Suzuki synthesis `Phi_a` and the evaluated two-sector v14.405 compact-action certificate remain absent. Therefore v14.406 is still blocked and has not been run. `C_S_32000`, the `3e-5` and `.002` thresholds, and all exactly-once charge rules remain unchanged and unspent.

HANDOFF
target: sandbox, external-audit
type: lane-a-v15.189-collision-repair-and-sharper-block
parent: v15.192
status: open
action: Treat the Lane A coarse-screen file at commit `20216773fb68184f2980296d7676b17fbf658cc2` as canonical v15.192. Replay it with the exact diagonal interval evaluator; verify `M<=15` and the uniform diagonal envelope from source; then perform a certified local-block/Schur-tail or direct interval-inertia calculation. Report an actual cutoff/contour certificate or a precise scoped failure. Do not infer source equivalence or whole-residual closure.
deliverable: replay code and hashes, outward-certified diagonal/tail bounds, and a certified contour/inertia result or exact obstruction.

**Fence:** no v14.406 residual consumer, no far-moment refresh, no stationary/infinite-capacity promotion, and no modification of protected constants or thresholds.
