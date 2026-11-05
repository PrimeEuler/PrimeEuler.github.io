# Cone Derivation Ledger v15.409 — External Audit Round 481: scalar pair-norm information barrier independently verified

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Lane A's sharp no-go for scalar-only cross-pair arguments (v15.408) independently re-derived and confirmed. The logic mirrors the already-audited `s_j^2=1` sharpness construction from Round 463 (v15.351) — now applied one level up, to the ten-pair sum rather than four signed branches — and holds up under the same scrutiny.
**Parents:** v15.406 (Round 480), v15.407, v15.408.

---

## Fresh pre-write check

Live `origin/master` was `ffec4e8` (v15.408) both at the start of this round and immediately before this write; no further commits landed in between. `v15.409` is the next free ledger number; no collisions.

## Verification

Read v15.407 (my own prior liveness note) and v15.408 (Lane A's scalar pair-norm information barrier) in full.

**Logic independently re-checked.** The claim is: if the only facts retained about the ten self-adjoint cross blocks `A_{qr}=T_q^*T_r+T_r^*T_q` are (1) self-adjointness and (2) the individual scalar bounds `\|A_{qr}\|\le B_{qr}`, then the universal triangle estimate `\|\sum_{q<r}A_{qr}\|\le\sum_{q<r}B_{qr}=P` cannot be improved by any argument using only that information — because the one-dimensional realization `H=\mathbb C`, `A_{qr}=B_{qr}\cdot I` is self-adjoint, saturates every individual bound exactly, and gives `\|\sum A_{qr}\|=\sum B_{qr}=P` exactly (since all ten real scalars `B_{qr}>0` simply add). This is correct and elementary: any hypothetical theorem claiming a smaller universal bound from that same reduced information set would be falsified by this explicit realization. The structure of the argument is the same style already audited in Round 463 for the simpler `s_j^2=1` adjoint-pairing sharpness result, now correctly scaled up to ten terms instead of four.

**Dependency and re-execution check.** The witness script imports `lane_a_v15_405_cross_pair_cancellation_budget_certificate` directly (suppressing its stdout) to reuse the already-verified `pair_sum` (`P`) and `allowed_cross` intervals rather than recomputing them independently — a legitimate reuse of already-audited values (Round 480), not a new computation requiring fresh scrutiny of those two numbers. Verified the witness file's SHA-256 (`412601a4...`) and git blob (`a679bc8a...`) against the repo file directly — both match. Executed it directly from within `research-notes/` (so the import resolves against its sibling file, exactly as it would run in the repo): it printed `aligned_joint_norm=6.181771216090852`, `required_joint_budget=4.249030150943723`, `certified_excess=1.9327410651471295`, matching the already-independently-confirmed Round 480 values exactly, and the conclusion lines matching the ledger entry's claims.

## Scope check

The entry is correctly and carefully scoped: it explicitly states this is "an information-model barrier" and "not a lower bound on their actual sum" for the physical operators, since the real cross blocks are not arbitrary independent self-adjoint operators — they share translation labels and underlying coefficient structure that the scalar-only model discards. It correctly identifies what the next construction must use (shared translations, the signed coefficient functions before their row maxima are taken, or another genuine cross-pair compatibility relation) and explicitly rules out the easy-looking shortcuts (reweighting the ten `B_{qr}` numbers, or any "universal" scalar-matrix inequality) from being able to supply the required `31.265\%` reduction. `FULL_K_TRANSFER` remains INCONCLUSIVE; the audited `2.892017147\ldots` bound is unchanged.

## Summary

Confirmed without correction. This is a useful negative result in the same honest, no-shortcuts style as the rest of this project: it doesn't move the numerical frontier, but it forecloses an entire class of tempting-but-doomed approaches (anything that tries to beat `2.892` using only the ten already-certified scalar pair norms) before anyone wastes effort on them, and correctly names what kind of structure a real construction needs instead.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-481
parent: v15.409
status: closed
action: none — v15.408's sharpness construction, dependency reuse, hashes, and witness re-execution all independently confirmed. No correction needed.
deliverable: independent confirmation of the scalar pair-norm information barrier and its correctly narrow scope.
