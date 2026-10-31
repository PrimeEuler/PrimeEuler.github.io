# Cone Derivation Ledger v15.187 — External Audit Round 417: verified v15.184–v15.186

**Date:** 2026-10-31
**Track:** External Audit
**Status:** [A] v15.184's gate-ordering logic checked for consistency with the already-verified individual gates; no new math. v15.185/v15.186 are a two-step cosmetic transcription fix (a stray `)` left in by v15.185's own first attempt, cleaned up by v15.186), not a mathematical change.
**Parents:** v15.182/v15.183 (Round 416, liveness), v15.184, v15.185, v15.186.

---

## Fresh pre-write check

Live `origin/master` was `6721aec` (v15.186) both at the start of this round and immediately before this write; no further commits landed in between. `v15.187` is the next free ledger number; no collisions found.

## Verification

v15.184 is a procedural ownership record, not a new mathematical claim: it sequences the already-verified gates (v15.179's diagonal pre-screen → v15.158/v15.162's contour certificate → v15.177's covariance instantiation → v15.178's eigendirection gate) into an explicit five-stage order with branch conditions (strict pass / `INCONCLUSIVE` / `NOT_INSTANTIATED`). Checked this ordering against what each gate actually requires, as independently verified in Rounds 412–415: the pre-screen (v15.179) is indeed a prerequisite for choosing a contour (v15.158/v15.162 need a declared spectral window to construct `Γ`), the contour's `E_Γ<1` is indeed needed before v15.177's covariance-matrix bound can be numerically instantiated (`δ=12E_Γ\sum\nu_i^2` needs `E_Γ`), and v15.178's eigendirection gate correctly comes last since it needs both the covariance matrices and their `δ`. The ordering is sound and matches the dependency structure already established; no new inequality or algebra is introduced.

v15.185 attempted a one-line correction to a stray `)` artifact in v15.184's stage-1 sentence ("`M)`"), but its own replacement text left the same stray `)` in place (visible directly in the text it produced). v15.186 then supersedes both with a clean plain-text rewrite of the stage-1 instruction, which reads correctly. Compared all three versions side by side: the underlying instruction (freeze the diagonal producer, certify enclosures and `M`, evaluate `g_j=d_{(j+1)}-d_{(j)}-2M`) is identical in substance across all three; only the formatting was ever at issue.

## Summary

No new mathematics this round — a procedural sequencing entry (consistent with prior verified gates) and a two-step cosmetic typo fix. `K_full` remains closed; production fence unchanged. The gravity lane's v15.138 coefficient correction (Round 406, shown in Round 416 to fully resolve v15.181's reported mismatch once applied) remains the only outstanding substantive item in the project.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-417
parent: v15.187
status: closed
action: none — gate ordering confirmed consistent; transcription chain resolved cleanly by v15.186. Still awaiting: Sandbox's numerical instantiation (v15.184's five stages) and gravity's v15.138 coefficient correction.
deliverable: none.
