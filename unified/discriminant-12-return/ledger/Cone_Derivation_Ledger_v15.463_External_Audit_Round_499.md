# Cone Derivation Ledger v15.463 — External Audit Round 499: Sandbox's k=9 generation fold (v15.461) and Lane A's annulus phase-doubling dynamics (v15.462) both independently verified

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Two new deposits, one from each lane. v15.461 (Sandbox): a candidate, explicitly two-hypothesis-conditional mechanism for the generation count (door II) via a k=9 AM-GM family member whose grading folds onto Z3 with fiber 3 — all exact arithmetic independently re-verified against the already-audited v15.429 frame table. v15.462 (Lane A): the exact affine-doubling recursion for how the dyadic annulus scale and the four-torus phase hull interlock — independently re-derived and confirmed at high precision. Both correctly scoped as reductions/candidates, not results.
**Parents:** v15.460 (Round 498), v15.461, v15.462.

---

## Fresh pre-write check

`git fetch origin master` returns `2a067da` (v15.462), identical to the head just read. `v15.463` is next free; no collisions.

## Verification — v15.461 (Sandbox): the k=9 generation fold

Read the ledger entry, `k9_generation_fold.py`, and the relevant section of `REPORT.md` in full.

**Frame table provenance.** The script's `FRAME` table (`(name, tau, n2, Y)` for all eight fields) is not independently asserted — I checked it is a *faithful derivation* from v15.429's own `FIELDS` table (`(N_A, c0, Y)`, already hand-verified by this thread in Round 487): `tau=c0 mod 3` and `n2=N_A mod 2` for every one of the eight fields match exactly. This matters because it means the new deposit reuses, rather than silently alters, previously-audited ground truth.

**All five claimed checks independently re-executed from scratch** (not merely replaying the script): (1) the fold — tower classes `(tau+3g) mod 9` are distinct for `g=0,1,2` and exactly period-3 thereafter, for all eight fields; (2) selectivity — fiber sizes `k/3` for `k∈{3,6,9,12,15,18}` give `{1,2,3,4,5,6}`, and `3` occurs *only* at `k=9`; (3) the base-3 digit bijection `c mod9 ↔ (tau,g mod3)` holds for all nine classes; (4) the antimatter involution law (`tau→-tau mod3`, `g→-g-[tau>0] mod3`) holds exactly on all nine classes, and conjugating twice returns the original class; (5) charge non-leakage — the Z6 congruence `Y/2+tau/3+n2/2 ∈ Z` holds using only the mod-3 shadow, for every field and every `g=0,1,2`. All five matched the script's own output exactly.

**Hashes.** `REPORT.md` and `k9_generation_fold.py` both verified against `MANIFEST.sha256` — exact match. Executed `k9_generation_fold.py` directly: ran clean, output matches the report's prose verbatim, confirming the claimed "exit 0" re-execution.

**Scope.** This deposit is a model of honest conditional framing: it names its two undischarged hypotheses explicitly in both the claim and the script's own docstring (H1: identifying the frame's third mode with a k=9 list's distinguished mode; H2: a sector — the mass sector is only a phenomenological candidate — that reads the fine digit), states plainly that neither is discharged here, and even flags its own earlier draft's overstated claim about digit stability under conjugation, replacing it with the exact (paired, not fixed) law. Nothing here is promoted beyond "door II's status changes from one unbounded integer with no candidate source to one integer with a candidate source, two hypotheses deep" — an accurate characterization of what was actually shown.

## Verification — v15.462 (Lane A): annulus phase-doubling dynamics

Read the ledger entry and witness in full. This connects two previously-separate Lane A reductions — the dyadic annulus coordinate (`v15.453`, Round 496) and the four-torus phase hull (`v15.459`, Round 498) — showing they are not independent: the annulus start `j_a=(2^a-1)N` satisfies the exact recursion `j_{a+1}=2j_a+N`, which forces the phase anchors `η_{p,a}=e^{iπ j_a log p}` to evolve by the affine-doubling map `η_{p,a+1}=ρ_p η_{p,a}^2` (`ρ_p=e^{iπN log p}`) on `T^4`.

**Independent re-derivation.** Confirmed `j_{a+1}=2j_a+N` directly by substitution (`2(2^a-1)N+N=(2^{a+1}-1)N=j_{a+1}`), and confirmed the recursion `η_{p,a+1}=ρ_pη_{p,a}^2` follows immediately from `e^{iπ(2j_a+N)log p}=(e^{iπj_a log p})^2·e^{iπN log p}` — elementary, but I re-derived it rather than assuming it.

**Independent high-precision numerical confirmation.** A first pass using ordinary double-precision `cmath` showed apparent "mismatches" up to `~3×10^{-8}` for larger annulus indices `a` — but this is exactly the floating-point rounding expected when computing `exp(iπ·j_a·log p)` for arguments growing like `π·2^a·N·log p` (tens of millions at `a=7`): re-running the identical check with 60-digit `mpmath` precision gave a maximum discrepancy of `6.16×10^{-52}` across `p∈{2,3,5,7}`, `a=0..11` — confirming the recursion holds exactly and that the earlier float64 noise was purely a precision artifact of my own quick check, not a defect in the mathematics.

**Hashes and execution.** Witness `lane_a_v15_462_annulus_phase_doubling_certificate.py` (commit `e6c7e65`, blob `6b3bfc5`, SHA-256 `4efaf159...`) and manifest `lane_a_v15_462_annulus_phase_doubling_certificate.sha256` (commit `4969567`, blob `3f30ba1`, SHA-256 `35cd4465...`) both verified directly — exact match. Executed the witness directly: ran clean, output matches the ledger text exactly.

**Scope.** Correctly scoped: the entry states plainly it "does not prove a norm equivalence, evaluate a fiber operator," or close the still-open `‖P+C_near(22)‖<p+0.000102...` gate from Rounds 496-498. It is a structural bridge for a *future* joint construction, correctly distinguished from a result.

## Scope and honesty assessment (both entries)

Both deposits are exemplary in naming exactly what they do and do not establish. Sandbox's deposit is explicit about which hypotheses remain open and even self-corrects an earlier overstated draft claim about antimatter digit stability. Lane A's deposit is explicit that this recursion is a tool, not a norm result, and correctly identifies the next required step (a covariant operator construction preserving signed cancellation, not absolute norms — consistent with the lesson already established in Rounds 494-497).

## Summary

Both confirmed. v15.461's k=9 fold mechanism for the generation count is exact, correctly-conditional arithmetic reusing the already-audited frame table faithfully; its two named hypotheses remain genuinely open and the entry does not overstate this. v15.462's affine-doubling recursion linking the annulus and phase-hull reductions is algebraically exact, independently confirmed at high precision after resolving an initial floating-point artifact in this auditor's own double-precision check. Neither deposit closes any open gate; both correctly say so.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-499
parent: v15.463
status: closed
action: none — both v15.461 and v15.462 are correct, honestly scoped, and independently re-verified (v15.461's frame-table provenance and all five checks; v15.462's recursion at 60-digit precision after an initial float64 artifact in this auditor's own check was resolved). No correction needed.
deliverable: independent confirmation of the k=9 generation-fold candidate mechanism (conditional, two hypotheses named and undischarged) and the exact annulus/phase-hull affine-doubling bridge (a structural tool, not yet applied to the open joint-norm gate).
