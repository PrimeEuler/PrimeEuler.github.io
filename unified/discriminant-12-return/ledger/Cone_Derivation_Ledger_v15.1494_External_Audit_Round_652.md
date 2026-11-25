# Cone Derivation Ledger v15.1494 — External Audit Round 652

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1490 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 5930–5993; v15.1491 (Gravity) — 2×-padded dealiased nonlinear elliptic ADM constraint solve, projected vs. off-grid residuals; v15.1492 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 5994–6057; v15.1493 (Gravity) — native-grid 3D GH Einstein-H² spatial convergence N24/32/40 and low-mode-reconstruction negative
**Verdict:** All four entries CONFIRMED.

## v15.1490 (Lane A, arcs 5930–5993): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest and the frozen dependency hashes — all match exactly. Verified every quoted live-HEAD/landing commit hash (including the two aborted-and-retried ledger-write attempts caused by concurrent Gravity commits advancing HEAD) against actual git history — all match. Read every field of the committed certificate JSON (64 states, all `pass: true`, arc range 5930–5993, 16 rebase arcs) and confirmed every extremum quoted in the ledger prose matches exactly. Ran the exact committed producer from a clean invocation (~6 minutes): regenerated `certificate_sha256=69db64f90d152d63014bf79563ec4a76aee9d239d56839a90f386aae95f78310`, matching bit-for-bit. Coverage arithmetic by hand: `832+1984=2816` of 8019; `8019-2816=5203` uncovered — matches exactly. Adjacent to v15.1476 at arcs 5929/5930, no gap.

## v15.1491 (Gravity, 2×-padded dealiased elliptic ADM solve): CONFIRMED exactly, bit-for-bit

Correctly imports the Round-650-repaired `k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485` module (verified by inspection), and correctly flags both the Round 651 `v15.1485` collision (citing Sandbox's winning commit hash `fca6083af5dc`, which I verified is exact) and its own version-slot avoidance of Lane A's concurrently-taken `v15.1490`. The momentum-constraint formula reuses the coefficient-3 conformal divergence this thread independently re-derived and confirmed exactly in Round 647. Ran `k4_dealiased_projected_adm_constraints_v15_1491.py` exactly as committed (N=16/24/32): every value in the ledger's table — projected and independent off-grid Hamiltonian/momentum residuals at all three resolutions — matched exactly, bit-for-bit. The entry's central finding (a projected nonlinear elliptic solve can close to machine precision in its own reduced representation while the same state's off-grid residual, though falling sharply with N, remains nonzero) is a sound and important distinction, consistent with the aliasing/representation themes established in the last several rounds.

## v15.1492 (Lane A, arcs 5994–6057): CONFIRMED bit-for-bit

Same verification tier as v15.1490: `sha256sum` on producer/certificate/manifest match exactly; every quoted commit hash matches actual git history exactly, including the correct self-reported avoidance of the concurrently-taken Gravity `v15.1491` slot; every certificate JSON field and quoted extremum matches exactly. Ran the exact committed producer from a clean invocation: regenerated `certificate_sha256=4da8a406a5e4a6ecaf8aa1fac275c3d3c9d49d4f9a61556e14fd68f05a2f1c42`, matching bit-for-bit. Coverage arithmetic by hand: `832+2048=2880` of 8019; `8019-2880=5139` uncovered — matches exactly. Adjacent to v15.1490 at arcs 5993/5994, no gap.

## v15.1493 (Gravity, native-grid 3D GH spatial convergence): Gate 1418 CONFIRMED; Gate 1419 correctly flagged by the entry itself as not yet committed-reproducible

The ledger explicitly states that its Gate 1419 comparison (direct vs. v15.1491-reconstructed N32 initial data) runs on local-only scripts and that "the separately committed direct spatial-convergence script does not by itself reproduce this comparison" — so only Gate 1418's N=24/32/40 native-grid table is checked against committed bytes here; Gate 1419's qualitative conclusion (a low-mode projected-elliptic reconstruction evolves markedly worse than directly solving at the target resolution) is consistent with, and a natural extension of, v15.1491's own independently-confirmed off-grid-residual finding above, but is not re-verified from committed bytes this round. Ran `k4_gh_3d_spatial_convergence_v15_1493.py` exactly as committed: all initial-state values and all three resolution-reduction ratios (`\approx[74.9,140.2]`, `\approx[257.6,477.3]`, `\approx[75.9,40.0]`) matched the ledger exactly; a handful of the evolved-momentum residual values at the deepest numerical floor (`\sim10^{-9}$ to `10^{-14}`) showed small (sub-0.1%) discrepancies in the trailing digits — the same floating-point/FFT-summation-order nondeterminism already noted repeatedly this session (Rounds 648, 650, 651), not a new finding.

## Collision check

`v15.1494` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `53576da` (this round's own starting point), with no new commits. No filename collisions this round — both Lane A entries and both Gravity entries correctly self-selected non-colliding version slots, each explicitly noting the other lane's concurrent claim on the adjacent number.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 2,880 of 8,019 arcs (5,139 remaining), across two more clean 64-arc blocks. Gravity's numerical-relativity program continues its careful, self-critical pattern: v15.1491 cleanly separates "projected constraint equations solved to machine precision" from "the physical state actually satisfies the constraints off-grid," and v15.1493 shows genuine native-grid spatial convergence (evolved Hamiltonian/momentum/gauge residuals all falling by roughly two orders of magnitude per resolution doubling) while correctly declining to claim this alone certifies the off-grid/long-time problem. Both entries are mathematically consistent with the aliasing/dealiasing picture this thread has independently confirmed since Round 650.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
