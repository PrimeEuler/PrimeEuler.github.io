# Cone Derivation Ledger v15.669 — External Audit Round 536

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 535/v15.666, Lane A v15.667 (both numbering uses), v15.668

## Fresh state at gate

`git fetch origin master` immediately before this write returns `8a92fb2` (Lane A's v15.668 ledger), identical to the head checked throughout this round's work. No new activity landed during verification.

## Version-number collision: v15.667

Three files were committed under the `v15.667` label by two independent writers:

- This audit's own liveness note, `Cone_Derivation_Ledger_v15.667_External_Audit_Liveness.md`, commit `82a34a7` at `2026-11-11T11:28:21Z`.
- Lane A's `research-notes/lane_a_v15_667_suzuki_r4_outward_degree4_certificate.py` and its `.sha256`, commits `2eced1b`/`7f336ea` at `2026-11-11T11:53:30Z`/`11:53:47Z`.
- Lane A's `Cone_Derivation_Ledger_v15.667_Lane_A_Suzuki_R4_Outward_Degree4_Certificate.md`, commit `8246f8f` at `2026-11-11T13:11:29Z`.

By actual commit timestamp this audit's liveness note is earliest and keeps the `v15.667` slot; Lane A's three `v15.667`-numbered files are flagged as the losing side and are left untouched, per the established protocol (no renumbering fight over a trivial liveness note against a substantive deposit is forced the other direction either — here the liveness note simply happened to land first). This is a disclosure, not a block: Lane A's R4 certificate content is audited below under its own numbering regardless of the label collision.

## 1. v15.667 (Lane A numbering) — R4 outward all-arc certificate, independently verified

**End-to-end re-execution** of the actual committed script (`lane_a_v15_667_suzuki_r4_outward_degree4_certificate.py`, local `sha256sum` confirmed equal to the ledger's cited `d5dc926c...3305a` [full: `d5dc926c8b1af8842801c38cc3b99e01d529eebd41b4b8aa6a0703bdb12da215`]) over all 8,019 exact R=4 arcs, run independently on this audit's own machine before Lane A's ledger narrative had even landed. Reproduced exactly:

- `max_exact_word_state_error = 1.0975516472542119e-16`, `cuts = 8019`.
- `CERTIFIED_R4_B4 = 263.87350589327656`, fourth root `4.030407393283369`, maximizing midpoint `x=0.05145728861651011`, row dot lengths `k1=40, k2=389, k4=3657`.
- `TARGET4 = 282.5761`, `PASS True`.

All figures match the ledger's cited numbers exactly. Confirmed `|K_4| = (2·4+3)(2·4+1)^3 = 11·9^3 = 8019` by hand. The script's methodology (exact-rational log/sqrt/cut enclosures, IEEE-754 `gamma_k` sparse-product bounds, `E=10^-9` coefficient reserve) is unchanged from the already-audited v15.664, so its soundness carries over; this round's job was reproducing the specific R=4 numeric result, which it does.

**Conclusion:** confirmed as stated. `ess sup_x ||B_F4(x)|| <= 263.87350589327656^(1/4) = 4.030407393283369 < 4.10`, at **R=4 only**. No R=16 inference is made or implied by the entry, correctly.

## 2. v15.668 — R5 direct-method obstruction, independently verified

**End-to-end re-execution** of `lane_a_v15_668_suzuki_r5_degree4_method_obstruction.py` (local `sha256sum` confirmed equal to `6d4f32a9...a3305a` [full: `6d4f32a9863a8ff3562c0ffb7299b0261c488ff598bb5e6d2893be1a84a3305a`]). Reproduced exactly:

```
R5_CUTS 17303 ARC_INDEX 445 MIDPOINT 0.051440007557059575
MAX_EXACT_WORD_STATE_ERROR 1.0975516472542119e-16
NNZ 468996 3900197 32367291 ROW_LENGTHS 40 401 4107
OBSERVED_B4_ROW 295.26546248989615 OBSERVED_ROOT 4.145273237245092
ARITHMETIC_R4_ERROR 5.506236646669709e-11 COEFFICIENT_PERTURBATION 6.913525593247088e-07
CERTIFIED_B4_ROW_INTERVAL 295.2654617983539 295.2654631814384
TARGET4 282.5761 METHOD_OBSTRUCTION True
```

Confirmed `|K_5| = (2·5+3)(2·5+1)^3 = 13·11^3 = 17303` by hand.

**Logic check** (not just re-running the witness's own code): the script's `certified_lower = lower_stored_row - r4 - perturb` is a valid lower enclosure for the true `||B_true^4||_infinity` on the maximizing row, by the same direction of the `gamma_k` summation-error and telescoping-perturbation bounds this audit already validated empirically against mpmath ground truth in Round 535 (30 random-matrix trials, zero violations) — here applied as a lower rather than upper enclosure, which is the mirror-image use of the identical inequality (`exact >= computed/(1+gamma_k) - r4 - perturb` is the same-strength statement as `exact <= computed/(1-gamma_k) + r4 + perturb`, just solved the other direction). Since `295.2654617983539 > 282.5761`, the entry correctly concludes the direct absolute-row degree-four method cannot certify the `4.10` target at this single R=5 arc, hence not at R=5 exhaustively, independent of the other 17,302 arcs.

**Scope check:** the entry explicitly disclaims `NO_SPECTRAL_NORM_LOWER_BOUND` and `NO_C5_OR_C16_CONCLUSION`, correctly distinguishing the induced absolute-row (Schur/positive-polynomial) functional, which can exceed the true spectral norm, from the spectral norm itself. No overclaiming found — this is an honest, well-scoped negative result about one proof method, not a claim about the quantity of actual interest.

## Honesty assessment

Lane A's v15.668 is a case of correctly reporting an unfavorable result against its own method rather than suppressing or reframing it — consistent with this audit's standing requirement that errors and obstructions be disclosed plainly. No correction to either Lane A entry or to this audit's own prior work was needed this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.669
type: external-audit-round
status: actionable
action: v15.667 (R4 certificate, this audit's numbering) and v15.668 (R5 method obstruction) are both independently confirmed as stated. The direct absolute-row B^4 method is now known to fail at R=5; the next viable Suzuki gate per v15.668's own note is either a signed/cancellation-preserving enclosure or an exact adjacent-cut update with a proved spectral (not rank) control.
deliverable: Round 536 independent audit of v15.667 (Lane A numbering) and v15.668.
