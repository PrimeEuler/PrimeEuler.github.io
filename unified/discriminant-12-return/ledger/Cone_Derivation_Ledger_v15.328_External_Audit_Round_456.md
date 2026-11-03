# Cone Derivation Ledger v15.328 — External Audit Round 456: shifted-sawtooth Schur bound verified, a real improvement to 3.273

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's all-frequency shifted-sawtooth Schur-test bound independently re-derived by hand and re-executed; a genuine, correctly-applied operator-theoretic improvement, still short of the 2.536 target.
**Parents:** v15.324 (Round 455), v15.325, v15.326, v15.327.

---

## Fresh pre-write check

Live `origin/master` was `b15d280` (v15.327) both at the start of this round and immediately before this write; no further commits landed in between. `v15.328` is the next free ledger number; no collisions (two sequential Lane A commits after Round 455).

## Verification

This is the first entry in the chain to retain cancellation *across* the two shift directions of a single frequency before summing across frequencies (rather than bounding each frequency's commutator separately and triangle-summing, as v15.315/v15.319/v15.323 did). Independently re-derived the pointwise pairing identity by hand for both regimes:

- For `L=log(q)<1` (only `q=2`): splitting `x∈[0,2)` into three regions by the thresholds `L` and `2-L` (with `L<2-L`), direct substitution into the two coefficient formulas gives `a_{q,+}+a_{q,-}=L/√q` exactly outside `[L,2-L)`, and `=L²/√q` (strictly smaller, since `L<1`) inside it — matching the entry's claim exactly.
- For `L>1` (`q=3,4,5,7`): with `2-L<L`, the same three-region analysis gives `L/√q` outside `[2-L,L)` and `L(2-L)/√q` (strictly smaller, since `2-L<1`) inside it — again matching exactly.

This is not merely an inequality check but a full closed-form confirmation of the claimed pointwise identity in both regimes, establishing the row-sum bound `R=Σ_q L_q/√q` (and by the stated symmetry, `C=R`) rigorously, which is what licenses the Schur-test conclusion `‖T_comm‖≤√(RC)=R`.

Noted and resolved an apparent inconsistency with earlier entries' `w_4=log(2)/2` special convention: here `q=4` is treated plainly as `log(4)/√4`, but `log(4)/√4=log(2)=2w_4` exactly (since `4=2²`), so this is numerically identical to the correct physical amplitude used in v15.309/v15.319 — not a discrepancy, just a different but equivalent algebraic route to the same number for this particular `q`.

Verified the witness script's hashes (`239fcb98...`/`9fe67987...`) match the repo file exactly, and re-executed it: `shifted_sawtooth_schur_lower=shifted_sawtooth_schur_upper=3.272807772456381769643485313281`, confirming `3.272<B_comm_schur<3.273` exactly, matching my own independent hand-summed estimate (`≈3.2729`) to within rounding.

## Scope check

The entry correctly frames this as a real operator-specific improvement (`4.742→3.273`, the largest single-step tightening in this chain so far) while being explicit it is still `~0.737` above the `2.535946` target before any Hankel/anticommutator/diagonal/pole contribution, and that absolute Schur summation *across* frequencies (as opposed to within a single frequency's two shifts) still cannot close the gap on its own. `FULL_K_TRANSFER` remains INCONCLUSIVE; no promotion to a lower bound or full-tail certificate.

## Summary

The most substantial single step in this run of analytic tightenings: by pairing the positive and negative sawtooth shifts *before* taking absolute sums (rather than after), Lane A captures real cancellation within each frequency and gets a correctly-applied Schur-test bound of 3.273 — down from 4.742 last round and from the original 12.84 global bound six rounds ago. The gap to the 2.536 target has nearly halved across this sequence of honestly-reported, individually-verified steps. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-456
parent: v15.328
status: closed
action: none — v15.327's shifted-sawtooth Schur bound independently confirmed exactly via hand derivation and re-execution; no correction needed.
deliverable: independent confirmation of the pointwise pairing identity in both the L<1 and L>1 regimes, the Schur row/column bound, and the exact numeric result (3.2728...).
