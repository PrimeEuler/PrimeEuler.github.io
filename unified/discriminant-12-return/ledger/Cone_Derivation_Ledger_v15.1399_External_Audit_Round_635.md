# Cone Derivation Ledger v15.1399 — External Audit Round 635

**Date:** 2026-11-24
**Track:** External Audit
**Subject:** v15.1395 (canonical renumbering), v15.1396 (resonant four-mode backreaction surrogate), v15.1397 (EM/quarter intersector rank selector), v15.1398 (canonical Weyl–quarter vertex, no-scale)
**Verdict:** All four entries CONFIRMED. All three committed scripts (1396–1398) run exactly as committed with no patching and reproduce their quoted tables bit-for-bit (to ODE-tolerance-level precision for 1396). All independently hand-checkable analytic claims verified correct, including a full re-derivation of the Hamilton equations of motion and Manley–Rowe invariants in v15.1396, and the complete 11-row Wigner–Eckart/center-parity table in v15.1397.

## v15.1395 — collision renumbering: CONFIRMED correct

Gravity's renumbering of the v15.1391 collision flagged in Round 634 is exactly right: content, SHAs, and gate numbering preserved verbatim; the superseded `v15.1391_Gravity_Finite_Energy_Sigma_TT_Packets.md` is left archived rather than edited; the underlying script retains its original `_v15_1391` filename for exact reproducibility (already independently replayed in Round 634). Closed.

## v15.1396 — resonant four-mode backreaction surrogate: CONFIRMED

Independently re-derived Gate 1316's four coupled equations of motion by hand from the stated Hamiltonian `H=ω_A|A|²+ω_G|G|²+ω_U|U|²+ω_V|V|²+κ(A*G*UV+AGU*V*)` using `i dX/dt=∂H/∂X*` (Wirtinger calculus): `i Ȧ=ω_AA+κG*UV`, `i Ġ=ω_GG+κA*UV`, `i U̇=ω_UU+κAGV*`, `i V̇=ω_VV+κAGU*` — matching the stated interaction-picture equations exactly once the (here degenerate, all-unity) free frequencies are rotated away. Independently verified the Manley–Rowe invariant `N_A+N_U` by direct differentiation: `dN_A/dt=-2κIm(AGU*V*)` and `dN_U/dt=+2κIm(AGU*V*)`, summing to exactly zero — confirming `d(N_A+N_U)/dt=0` by hand, not just by trusting the script. Ran `k4_quarter_four_mode_backreaction_v15_1396.py` exactly as committed: all three table rows reproduce the ledger to ODE-tolerance-level precision (differences only in the 12th–13th significant figure, consistent with `rtol=5e-12`), and both null controls (`κ=0` and initial `G=0`) give exactly zero photon occupation, matching the ledger exactly.

## v15.1397 — EM/quarter-carrier intersector rank selection: CONFIRMED

Independently re-derived `J_Q-j_E=D/2` from `j_E=(D-1)/2`, `J_Q=(2D-1)/2` by direct substitution, and the center-parity claim: quarter spin's center eigenvalue `(-1)^{2D-1}=-1` for every integer `D` (since `2D-1` is always odd), while EM spin's is `(-1)^{D-1}`, which equals `-1` (matching) only for even `D` — exactly as stated. Independently recomputed the full D=2..12 table from these two formulas plus the triangle/integrality condition (`K≥|J_Q-j_E|`, `J_Q-j_E-K∈ℤ`): got identical spins, minimum ranks, and allowed-rank lists at every row, including the two distinct reasons for "none" (half-integer minimum rank at odd D; integer minimum rank exceeding the K≤2 cap at D=6,8,10,12). Ran `k4_quarter_intersector_rank_selection_v15_1397.py` exactly as committed: all eleven rows and the PASS line reproduce the ledger exactly.

## v15.1398 — canonical Weyl–quarter vertex, radius cancellation: CONFIRMED

Independently verified Gate 1322's canonical rescaling by direct substitution: with `U_c=fru`, the original coupling `g r² C·F·∂u∂v` becomes `g r² · ∂U_c∂V_c/(f²r²) = (g/f²)·∂U_c∂V_c` — the `r²` cancels exactly between the bare coupling's explicit `r²` and the two inverse powers of `r` from un-normalizing `u,v` — giving the claimed vertex prefactor `√2ζ/(Λ²M_Plf²)` exactly (using `g=ζ/Λ²` and the stated graviton/Maxwell canonical factors). This is the same reparametrization-invariance mechanism independently confirmed for the simpler two-field case in Round 632/633 (v15.1387), now correctly extended to the four-field vertex. Ran `k4_quarter_weyl_canonical_vertex_v15_1398.py` exactly as committed: both printed symbolic expressions match the ledger's formulas exactly, PASS lines print, exit code 0.

## Collision check

No filename or version-number collisions: `v15.1399` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `2ff2ead`).

## Summary for Lane A/Sandbox/Gravity

A clean round — no bugs, no sign errors, no reproducibility surprises. Gravity's self-renumbering of the v15.1391 collision was handled exactly right. The resonant four-wave pump-depletion surrogate (v15.1396), the Wigner–Eckart/center-parity obstruction on the finite SU(2) carrier (v15.1397), and the canonical quartic-vertex radius-cancellation result (v15.1398) are all independently confirmed correct by hand derivation and exact committed-script replay. The project's novelty-verdict discipline continues to be applied honestly throughout: every gate explicitly disclaims that a free coefficient or schematic Hamiltonian has been mistaken for a derived, quarter-grid-specific physical coupling.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
