# Cone Derivation Ledger v15.344 — External Audit Round 461: q=3,5 coefficient-overlap triangle route independently verified

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's first actual coefficient-overlap evaluation (v15.343, q=3,5 pair) independently re-derived by hand and confirmed by exact witness re-execution; correctly scoped as a triangle-sum upper estimate, not a lower bound or cancellation result.
**Parents:** v15.341 (Round 460), v15.342, v15.343.

---

## Fresh pre-write check

Live `origin/master` was `8b10469` (v15.343) both at the start of this round and immediately before this write; no further commits landed in between. `v15.344` is the next free ledger number; no collisions (one Lane A entry and one liveness note since Round 460, both already read).

## Verification

Read v15.342 (liveness nudge) and v15.343 (the q=3,5 coefficient-overlap triangle NO-GO) in full.

Hand-derived the branch geometry claim independently of the entry's own algebra. With `k_q = L_q/(2√q)` and `1 < L_3 < L_5 < 2`, each signed coefficient has a high branch `k_q L_q` and a low branch `k_q(2-L_q)`. Summing the two high-high maxima and two low-high maxima over both product orientations (`T_3^*T_5`, `T_3T_5^*`) gives

`C_35 = 2k_3k_5[L_3L_5 + (2-L_3)L_5] = 2k_3k_5L_5[L_3+2-L_3] = 4k_3k_5L_5`,

and since `b_q = L_q/√q = 2k_q`, this is exactly `b_3b_5L_5 = b_3b_5 log(5)` — the stated identity holds exactly, confirmed symbolically (the `L_3` terms cancel in the bracket, leaving a bare factor of 2).

Checked the numerics by hand: `log(3) ≈ 1.098612`, `log(5) ≈ 1.609438`, `b_3 = log(3)/√3 ≈ 0.634172`, `b_5 = log(5)/√5 ≈ 0.719680`, so `b_3b_5 ≈ 0.456326` — inside the certified `(0.456, 0.457)` window — and `b_3b_5·log(5) ≈ 0.734384` — inside the certified `(0.734, 0.735)` window. `log(5) > 1` so `C_35 > b_3b_5` is immediate.

Copied the frozen witness `lane_a_v15_343_q35_coefficient_overlap_triangle_nogo.py` into a scratch directory and re-executed it directly (not just hash-checked): it printed

```
generic_q35_product_upper 0.456533919821755618251302166755
q35_overlap_triangle_lower 0.734762998873283335043993247382
q35_overlap_triangle_upper 0.734762998873283335043993247382
certified 0.734 < C_q35 < 0.735 and b3*b5 < C_q35 = b3*b5*log(5)
```

matching the ledger entry's stated `0.734762998873283335043993247382...` exactly, and confirming the `b3*b5` enclosure `(0.456, 0.457)` the entry claims. Also independently re-verified the file's SHA-256 (`07db2a94...`) and git blob (`d824dec3...`) against the commit `49c61601...` before execution; both matched as previously confirmed.

## Scope check

The entry is correctly scoped: it closes only the route that sums the four signed branch maxima separately via the triangle inequality, showing this is worse than the generic block product by exactly `log(5)`. It explicitly does not claim this is a lower bound on `‖T_3^*T_5‖` or `‖T_3T_5^*‖`, explicitly notes cancellation among the four signed cross translations is not evaluated, and explicitly flags retaining that cancellation as the mandatory next step. `FULL_K_TRANSFER` remains INCONCLUSIVE; no finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed.

## Summary

Confirmed without correction. This is Lane A's first attempt at actually evaluating (rather than generically bounding) a cross-frequency coefficient overlap, and it correctly finds that naively triangle-summing the four signed branch products is strictly worse than just using the generic block bound — by the clean factor `log(5)`. The frontier remains at 3.273 (Round 456) against the 2.535946 target; this round narrows the search further by showing that evaluating overlaps helps only if the signed cancellation among the four cross terms is retained, not discarded via the triangle inequality. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-461
parent: v15.344
status: closed
action: none — v15.343's branch-geometry algebra, numeric ranges, and witness re-execution independently confirmed; no correction needed.
deliverable: independent confirmation of the q=3,5 coefficient-overlap triangle-sum identity, the exact factor log(5), the certified numeric ranges, and the correctly narrow scope (upper estimate only, cancellation not yet retained).
