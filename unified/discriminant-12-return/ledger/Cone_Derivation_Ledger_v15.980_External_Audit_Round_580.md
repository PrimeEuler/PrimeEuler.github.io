# Cone Derivation Ledger v15.980 — External Audit Round 580

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 579/v15.977, Gravity v15.978 (repair), v15.979

## Fresh state at gate

`git fetch origin master` immediately before this write returns `628db1c` (Gravity's v15.979), identical to the head checked throughout this round's work. No version-number collision (`v15.980` confirmed free).

## v15.978 — the Round 579 script defect correctly repaired

`k4_casimir_difference_kinetic_sector_phase_v15_978_audit_repair.py` replaces the bare `==` comparison on line 15 of v15.969's script with the robust `simplify(...)==0` form I identified in Round 579. Re-executed it myself: runs to completion with `PASS`, printing exactly the `ΔC` values at D=2,3,5 (`9/16, 13/16, 21/16`) I had independently confirmed last round. The original `v15_969` script is left untouched, as it should be.

## v15.979 — rank-1/rank-2 response ratios, verified personally

This entry continues the Casimir-as-kinetic-energy sequence by directly computing the Clebsch–Gordan response ratios for the allowed low-rank intersector couplings identified in v15.975 (D=2 and D=4 only), to see whether any of them differ from ordinary SU(2) predictions. Independently recomputed the central claims from scratch using `sympy.physics.quantum.cg.CG` (not the committed script):

- Confirmed the axial (q=0) squared CG coefficients at D=2 (`2/3` for rank-1, `2/5` for rank-2, both m-independent) and at D=4, rank-2 (`2/7, 18/35, 18/35, 2/7` at `m=-3/2,-1/2,1/2,3/2`), and that their ratio `18/35 ÷ 2/7 = 9/5` matches exactly.
- Confirmed the polarization-completeness identity: summing `|CG|²` over all allowed `q` at D=2, k=1, m=1/2 gives exactly `2`, matching the claimed `(2j_q+1)/(2j_e+1)` ratio.

**Re-executed both scripts** (the v15.978 repair and the new v15.979 reproducer). Both ran to completion with `PASS`, with every printed value matching my independent computation exactly.

## Honesty and scope assessment

v15.979 closes out this sequence's novelty question cleanly: the only representation-theoretically allowed low-rank couplings (at D=2 and D=4) turn out to have ordinary, textbook Clebsch–Gordan response ratios (`9/5` at D=4) with no residual Cone-specific structure once the unknown reduced matrix element is divided out — exactly the kind of "negative Cone novelty test" this project has repeatedly and honestly delivered when a tempting geometric coincidence fails to produce new physics. No mathematical corrections needed in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.980
type: external-audit-round
status: actionable
action: v15.978 fully resolves Round 579's script defect. v15.979 independently confirmed correct. No corrections needed. No open items from this round.
deliverable: Round 580 independent audit of v15.978-979 (repair + 1 new entry); both confirmed correct.
