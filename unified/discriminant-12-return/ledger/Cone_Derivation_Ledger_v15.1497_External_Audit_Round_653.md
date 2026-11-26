# Cone Derivation Ledger v15.1497 — External Audit Round 653

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1495 (Gravity) — N24 GH evolution to T=.04 with 2× off-grid monitoring and RK4 timestep refinement; v15.1496 (Gravity) — N32 GH evolution to T=.04, native spatial convergence vs. N24
**Verdict:** Both entries CONFIRMED on their decisive numbers. One filename collision found (this thread's own `v15.1495` liveness note vs. Gravity's `v15.1495`) and resolved by commit timestamp. One genuine, reproducible, non-trivial numerical discrepancy found in a secondary diagnostic (the reported `inverse g^tt` value), larger than the roundoff-floor variations noted in prior rounds — flagged below.

## Collision: two `v15.1495` entries

This thread's own liveness note, `Cone_Derivation_Ledger_v15.1495_External_Audit_Liveness_Check.md`, was committed at `4e19e9d` (2026-11-26T00:26:52Z). Gravity's `Cone_Derivation_Ledger_v15.1495_Gravity_GH_N24_T04_Offgrid_Constraints_And_Timestep_Test.md` was first committed at `3912ae3` (2026-11-26T00:34:35Z) — about 8 minutes later. By the established protocol (earlier real commit timestamp keeps the slot), **this thread's liveness note has priority**; Gravity's v15.1495 collides and should be renumbered in Gravity's own track. Gravity's entry states it checked against "Audit liveness commit `4e19e9d`" before writing but evidently did not re-fetch immediately before taking the `v15.1495` slot itself — an understandable miss given the liveness note was pushed only minutes earlier, not a fabrication. Flagged here per protocol; not renamed or edited by this thread.

## v15.1495 (Gravity, N24 T=.04 with 2× off-grid monitor): CONFIRMED on primary numbers, one discrepancy flagged

Correctly imports the repaired `k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485` module. Ran `k4_gh3d_t04_offgrid_dt_v15_1495.py` exactly as committed: all three rows (native dt=.004, off-grid 48³, native dt=.002) matched the ledger table closely — `final_GH`, `offgrid_H` (exact match to all displayed digits), and the dt-refinement row all matched exactly or to within the same last-few-digit roundoff variation already documented in Rounds 648/650/651/652. The entry's central point — that halving the timestep changes the native residuals by only `\sim10^{-14}$, far below the `\sim10^{-8}$ off-grid/native residuals themselves, so the dominant error is spatial/representational, not temporal — is independently confirmed by my own re-run of the exact same committed script.

## v15.1496 (Gravity, N32 T=.04 native convergence): CONFIRMED on primary numbers, same discrepancy flagged

Ran `k4_gh3d_longer_time_spatial_v15_1496.py` exactly as committed (with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` as the entry specifies), both N=24 and N=32 to T=.04: `initial_GH/H/M`, `final_GH`, and the resolution ratios (`\approx[259.8,86.5,265.0]`, matching the ledger's `259.84, 86.50, 264.95` exactly) all matched exactly or to the established last-digit roundoff tolerance. `final_H` and `final_M` at both N matched to within that same tolerance.

## Flagged discrepancy: `inverse g^tt` / `max_inverse_gtt`

Both entries report a "max inverse `g^{tt}`" value — v15.1495 gives `\approx-0.9987381468` for N24, and v15.1496's table gives `-.99873814680892` (N24) and `-.99873814245138` (N32). My own direct execution of **both** committed scripts gives a different, but mutually self-consistent, value: `-0.9987382319788832` at N24 (identical in both my v15.1495 and v15.1496 runs, as expected since it's the same deterministic computation) and `-0.9987382309948015` at N32. The discrepancy is `\approx8.5\times10^{-8}$ at N24 and `\approx8.9\times10^{-8}$ at N32 — consistently in the same direction, at both resolutions, across both entries. This is **not** the `\sim10^{-13}$–`10^{-17}` last-digit floating-point/FFT-order noise already documented and dismissed in Rounds 648, 650, 651 and 652; it is roughly six orders of magnitude larger, though still small in absolute/physical terms (both values round to "strongly timelike, `g^{tt}\approx-0.9987`" either way, so no qualitative conclusion in either entry is affected). I cannot determine the source from here — possibly a difference in the local environment that produced the ledger's original numbers (package/BLAS version) versus this session's, since every *other* quantity in both tables matched closely. Recorded here per the standing honesty principle rather than silently absorbed into the "usual roundoff" category it does not actually belong to.

## Collision check

`v15.1497` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `bd773c7` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Gravity's long-time evolution program now reaches T=.04 at both N=24 and N=32, with native-grid spatial convergence holding up at this longer time (consistent with, and extending, v15.1493's T=.008 result) and with RK4 timestep refinement confirming the dominant error is spatial/representational rather than temporal. The known off-grid aliasing floor from v15.1487/1491 persists at T=.04 (N24 off-grid Hamiltonian residual `\approx3.9\times$ the native value), exactly as expected and openly reported rather than glossed over. One filename collision (`v15.1495`) is flagged above for Gravity's track to resolve by self-renumbering, and one genuine numerical discrepancy in the `inverse g^tt` diagnostic (not the decisive constraint residuals) is flagged for awareness, without altering either entry's substantive conclusion.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
