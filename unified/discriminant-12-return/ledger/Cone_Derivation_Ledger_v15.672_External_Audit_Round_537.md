# Cone Derivation Ledger v15.672 — External Audit Round 537

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 536/v15.669, Lane A v15.670 (both numbering uses), v15.671

## Fresh state at gate

`git fetch origin master` immediately before this write returns `d8b6e67` (Lane A's v15.671 ledger), identical to the head checked throughout this round's work. No new activity landed during verification.

## Version-number collision: v15.670

As with the earlier v15.667 collision, two independent writers used `v15.670`:

- This audit's own liveness note, `Cone_Derivation_Ledger_v15.670_External_Audit_Liveness.md`, commit `a953d8c` at `2026-11-11T13:27:29Z`.
- Lane A's `research-notes/lane_a_v15_670_suzuki_r5_weighted_b4_fixed_sample.py`/`.sha256` and ledger entry, commits `9374947`/`4ff7b65`/`8cbf272`, all at `2026-11-11T14:20:55Z`–`14:21:59Z`.

This audit's liveness note is earliest by actual commit timestamp and keeps the `v15.670` slot; Lane A's three `v15.670`-numbered files are flagged as the losing side and left untouched, per the established protocol. Lane A's own v15.670 ledger entry (read in full before this gate) already correctly disclosed and applied the prior v15.667 collision resolution from Round 536 — this round applies the same resolution to the new v15.670 collision and otherwise changes nothing about how either side's content is audited.

## 1. v15.670 (Lane A numbering) — weighted-B4 fixed-sample architecture probe

**Mathematical check of the underlying inequality.** The entry's claimed chain
`||B||^4 = ρ(B^4) ≤ ρ(|B^4|) ≤ max_i (|B^4|w)_i/w_i` for any positive vector `w`
is standard and was verified by hand:
- `B` Hermitian ⟹ `B^4` is PSD with eigenvalues `λ_i(B)^4`, so `ρ(B^4) = max_i λ_i(B)^4 = ||B||^4` exactly (not merely an inequality).
- `ρ(M) ≤ ρ(|M|)` for any square matrix `M` is the standard fact that an eigenvector `v` of `M` satisfies `|M||v| ≥ |λ||v|` entrywise, which forces `ρ(|M|) ≥ |λ|` by the Perron-Frobenius comparison theorem for nonnegative matrices.
- The weighted Collatz-Wielandt bound `ρ(A) ≤ max_i (Aw)_i/w_i` for nonnegative `A` and positive `w` is the standard one-sided Collatz-Wielandt inequality.
This chain is correct for *any* positive `w`, including a poorly-chosen one — a poor `w` only weakens the bound, it cannot invalidate it. That is exactly consistent with this entry's finding: the anchor-derived common weight gives a valid but too-weak (failing) bound on other arcs, not an unsound one.

**End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `b83522dc...18470` [full: `b83522dc3b97b3b17364571d00636958e32bd8f5c2370933648f9cfb42918470`]) reproduced exactly:
- `ANCHOR_INDEX 445`, weight `WEIGHT_MIN=0.0022895377686839623`, `WEIGHT_CONDITION=436.7693836187751`, `WEIGHT_SHA256=bec2ba4c...2a92` (full matches).
- Worst sampled arc: index `8651`, `x=1.0`, `outward_weighted_b4=491.40609272412445`, `outward_fourth_root=4.708256712021633`, `all_sampled_pass=false`.

**Error-transport term check.** The formula `true_upper = stored_upper + weight_condition*(r4+perturb)` was verified by hand to be the correct conversion of the infinity-norm bound `||B4_true - B4_stored||_∞ ≤ r4+perturb` (already independently validated in Round 535) into a bound on the weighted-ratio perturbation: for any row `i`, `(|B4_true|w)_i - (|B4_stored|w)_i ≤ w_max·||B4_true-B4_stored||_∞`, and dividing by `w_i ≥ w_min` gives the `weight_condition = w_max/w_min` factor used.

**Conclusion:** confirmed as stated — a valid but weak (sample-failing) outward bound; not an exhaustive or passing R5 statement, and the entry does not claim otherwise.

## 2. v15.671 — local-weight one-arc pass

**End-to-end re-execution** of the committed script (SHA-256 confirmed equal to `64c3d5be...9bf2c` [full: `64c3d5bebc74ec07ae2cfd68a6dcfa23f3e213fc40bcd4ff69db27d3d909bf2c`]) reproduced exactly:

```
R5_ARC_INDEX 8651 MIDPOINT 1.0
WEIGHT_CONDITION 401.0488867424298 WEIGHT_SHA256 dcdd6128...a74b89d
OUTWARD_WEIGHTED_B4 140.57446294443875 OUTWARD_FOURTH_ROOT 3.443313840589908
TARGET4 282.5761 LOCAL_ARC_PASS True
```

Same error-transport logic as v15.670, same conclusion on soundness. This confirms the weighted-Collatz mechanism genuinely recovers a strong bound at the one arc where both the plain row-sum method (v15.668) and the common-weight method (v15.670) failed — a real demonstration that **local** weight adaptation, not the row-sum functional itself, is the missing ingredient, strengthening the case that a weight-transport or weight-chart construction is the right next step rather than abandoning the signed-B^4 approach.

## Honesty and scope assessment

Both entries are correctly scoped: v15.670 reports its own common-weight strategy failing rather than reframing or suppressing the negative sampled result, and v15.671 explicitly limits its positive result to one arc with no C5/C16 inference. No overclaiming found; no correction to either Lane A entry or to this audit's prior work was needed.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.672
type: external-audit-round
status: actionable
action: v15.670 (Lane A numbering, common-weight probe — fails sampled R5 arcs) and v15.671 (local-weight one-arc pass — succeeds) are both independently confirmed as stated, including the underlying Collatz-Wielandt inequality chain. The next viable gate, per both entries' own notes, is certifying how the positive weight transports across an adjacent v15.650 cut, or a finite weight-chart cover — not a return to the unweighted method, which v15.668 already showed fails, and not abandonment of the signed-B4 mechanism, which v15.671 shows can work locally.
deliverable: Round 537 independent audit of v15.670 (Lane A numbering) and v15.671, including hand-verification of the weighted Collatz-Wielandt inequality itself.
