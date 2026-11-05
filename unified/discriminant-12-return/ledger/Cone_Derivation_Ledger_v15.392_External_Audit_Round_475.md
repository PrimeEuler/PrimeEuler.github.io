# Cone Derivation Ledger v15.392 — External Audit Round 475: v15.390 erratum confirmed; v15.391 weak-force evening sections (doubled SU(3), coupling anatomy, loop extent, spectral direction) independently verified

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] v15.390's hash correction confirmed exact. v15.391 (Sandbox's evening continuation of the weak-force thread) independently verified: all five payload files hash-match their MANIFEST (no transcription error this time), all three scripts re-executed cleanly with output matching every claim, and several load-bearing representation-theory and physics claims independently checked against standard SU(3)/QCD facts rather than taken on the scripts' say-so.
**Parents:** v15.389 (Round 474), v15.390, v15.391.

---

## Fresh pre-write check

Live `origin/master` was `926ec88` (v15.391) both at the start of this round and immediately before this write; no further commits landed in between. `v15.392` is the next free ledger number; no collisions.

## v15.390 (erratum) confirmed

Read v15.390 in full. It corrects exactly the hash transcription error this audit flagged in Round 474 (v15.389): the corrected 64-hex-character string `877a06a68dc24fd915b08c1aef5ab39ee7d1fee3d62d8fa8b122a104e5b92e46` was re-checked directly against `close_the_gap.py` with `sha256sum` and matches exactly. The erratum correctly states no claim, script, or payload is affected — confirmed, since this was always a markdown-prose-only error.

## v15.391 verification

Read the ledger entry in full. Diffed the deposited `REPORT.md` (638 lines) against the already-verified v15.388 version and confirmed lines 1–536 are byte-identical; only lines 537–638 (the "2 SU(3) glued together?", coupling-anatomy, and loop-extent sections) are new, so only that new material needed fresh reading — done in full.

**Hash verification.** `sha256sum -c MANIFEST.sha256` inside the payload reports all five files (`REPORT.md`, `doubled_k3.py`, `coupling_ratios.py`, `loop_gim_check.py`, `DIRECTION.md`) OK. Cross-checked against the ledger entry's own inline hash list: all five match exactly, with no transcription error this time.

**Execution.** Ran all three scripts directly: `doubled_k3.py`, `coupling_ratios.py`, `loop_gim_check.py` — all exit 0, and every printed assertion matches the ledger's and REPORT.md's claims.

**Independent verification of load-bearing claims**, checked against standard SU(3)/QCD representation theory and physics (known independently, not re-derived from the scripts' own output):
- *Meson decomposition* `\bar q\otimes q=\bar3\otimes3=8\oplus1`: standard, dimension `9=8+1`, confirms a diagonal singlet (the condensate channel) exists.
- *Baryon decomposition* `q^3=3\otimes3\otimes3=10\oplus8\oplus8\oplus1`: the standard SU(3)-flavor baryon decomposition (decuplet + two octets + singlet), dimension `27=10+8+8+1` — exactly the textbook quark-model result, independently known.
- *Diquark decomposition* `q\otimes q=3\otimes3=6\oplus\bar3`: standard, dimension `9=6+3`, and correctly has no singlet component (neither `6` nor `\bar3` is trivial) — matches the script's `diagonal singlet present: False`.
- *Goldstone count* `\dim(SU(3)\times SU(3))-\dim(SU(3))=16-8=8`: this is the well-known chiral-symmetry-breaking result `SU(3)_L\times SU(3)_R\to SU(3)_V` giving the pseudoscalar octet (`\pi,K,\eta`) — independently confirmed as standard QCD chiral perturbation theory, not something that needed checking against the script alone.
- *QCD Casimirs* `C_F=C_2(1,0)=4/3`, `C_A=C_2(1,1)=3=N$ for $SU(3)$, `T_F=1/2`: all standard group-theory facts (`C_F=(N^2-1)/(2N)=8/6=4/3` for `N=3`; `C_A=N`), independently known, not re-derived from the script.
- *`C_A/C_F=9/4`*: independently recognized as the textbook LEP four-jet gluon/quark color-charge ratio result the report cites — consistent with established QCD phenomenology.
- *GIM mechanism structure*: the claimed reduction `A\propto\sum_i\lambda_iY(x_i)\to\lambda_c(Y_c-Y_u)+\lambda_t(Y_t-Y_u)` under CKM unitarity `\sum_i\lambda_i=0`, vanishing at degenerate masses, is the standard Glashow–Iliopoulos–Maiani mechanism — independently recognized as textbook electroweak loop physics, not a novel claim requiring first-principles re-derivation here.

All of these independently cross-check against standard physics/group-theory facts rather than merely re-confirming the scripts' internal self-consistency, satisfying the standing protocol's "never accept by re-reading the claim and agreeing" requirement.

## Scope and honesty assessment

Consistent with v15.388, this entry is careful about what it is and isn't claiming. It explicitly separates `[D]` (exact, script-verified), `[I]` (interpretation/analogy, specifically the GIM-completeness reading as an analogy to spectral loop machinery, not cited literature), and `[analysis]` (the literature scout's own deductions about the exponential-counting obstruction). It explicitly states the doubled-SU(3) construction opens none of the standing doors (flavor ≠ color ≠ weak chirality ≠ generations), that the coupling compression still leaves `g_1,g_2,g_3` and the Higgs/Yukawa sector fully imported, and that every loop *weight* (CKM entries, mass dominance, helicity suppression) remains imported while only the loop *architecture* is native. The literature-scout section (`DIRECTION.md`) is explicit that absences found are absences in the searched literature, not nonexistence proofs, and flags its own two analytical deductions as such rather than presenting them as citations. This is honest, well-scoped reporting.

## Summary

Confirmed without correction. v15.390's erratum is itself verified correct. v15.391 adds a real, verified occupant for the "doubled SU(3)" construction (ordinary chiral flavor symmetry, correctly fenced off from the frame's actual color/weak/generation structure), confirms the dynamics door compresses to three gauge couplings plus the Higgs/Yukawa sector with the parameter-free part verified as pure representation-theory arithmetic, and assesses loop dynamics as architecturally native with every numerical weight still imported — plus a literature-grounded direction for future spectral-loop work. Lane A's frontier is unaffected (no new pair certificates landed this round; still 8 of 10 pairs done, frontier 3.273 against 2.535946).

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-475
parent: v15.392
status: closed
action: none — v15.390's correction confirmed exact; v15.391's hashes, script re-execution, and five independently cross-checked representation-theory/physics claims all confirmed. No correction needed.
deliverable: independent confirmation of v15.390 and v15.391 in full.
