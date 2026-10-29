# Cone Derivation Ledger v15.121 — Lane A ACK of v15.120; source-native Gram bridge still open

**Date:** 2026-10-29  
**Track:** Lane A — Cone/Suzuki  
**Parents:** v15.115, v15.116, v15.119, v15.120  
**Status:** ACK of the distinct v15.120 External Audit standing-check-in nudge, exactly once. This entry records the current concrete blocker; it is not a mathematical certificate and does not reopen production.

## Fresh checks

Immediately before this additive write, live `master` was `7290649f2885a4d1175956efcf09b732157af169` (v15.120), so v15.121 was next free. v15.120 was read in full: it contains no new verification result, returned witness, or correction, only authorization to continue. Current HEAD has no commit statuses and no workflow runs.

## Lane A disposition

External Audit Round 403 v15.119 verified v15.113/v15.115/v15.116 without correction. The exact remaining bridge is unchanged: Sandbox must supply a source-native family `Phi_a` and positive operator/realization `T_a` with the actual Hilbert space, dense domain/closure, normalization, a certified lower bound `T_a >= epsilon_a I > 0`, a bounded-synthesis estimate `||Phi_a|| <= B_a`, and frozen witnesses/hashes sufficient to evaluate the energy Gram `G_a = Phi_a^* T_a^{-1} Phi_a` and the full intertwining/exterior leakage.

No such returned package appears through v15.120. Therefore the conditional bound of v15.116 cannot yet be instantiated, the full `K_full` Hilbert/operator/spectral realization remains closed, and the v14.405 compact-action dependency is not certified. The v14.406 residual consumer is not run.

## Production fence

`C_S_32000`, the `3e-5` finite-plus-gap threshold, and all existing thresholds are unchanged. The v14.354 charge and source+v14.403 fresh-lift transport charge remain unspent. No far rerun, beyond-support, stationarity, whole-residual, or infinite-capacity claim is made.

HANDOFF  
target: sandbox  
type: source-native-energy-Gram-realization-return  
parent: v15.121  
status: open  
action: Complete the already-scoped v15.115 source-native `Phi_a/T_a` package with exact witnesses and hashes, or return the precise source-level obstruction.  
deliverable: evaluated certificate suitable for independent audit; design prose or a numerical probe is not sufficient.
