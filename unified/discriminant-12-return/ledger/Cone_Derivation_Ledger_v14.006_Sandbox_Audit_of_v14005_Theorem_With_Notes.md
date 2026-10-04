# Cone Derivation Ledger v14.006 — Sandbox: Audit of v14.005 Frozen-P4 Guardrail (Theorem-with-Notes)

**Date:** 2026-10-04
**Track:** Sandbox (our Lane B), audit deliverable
**Status:** [D] partition-invariance proof verified analytically and numerically; [N] principal angles recomputed to 10 digits; [N] complement floors verified; [G] key question answered: evidence sufficient for the test decision as framed; [C] N=192 kept distinct from theorem-scale; no KKT rebuild.
**Parents:** v14.005, v14.003–004, v13.982, v13.988
**Authorization:** Jeremy, 2026-10-04 (pre-authorized: "go ahead and ledger when they come back, Lane A is waiting")
**Collision check:** live HEAD immediately before this write was v14.005; no v14.006 entry was present.
**Handoff protocol:** research-notes/CROSS_LANE_HANDOFF_PROTOCOL.md.

---

## 0. Purpose

Close the v14.005 HANDOFF block (target: sandbox, type: audit, deliverable: theorem-or-obstruction): independently audit the frozen-P4 basis-freezing decision, especially the partition-invariance guardrail and whether the principal-angle/complement-floor evidence justifies testing the same frozen carrier at M3999/4000 without regenerating a new basis. Constraints honored: capacity equality not used as alignment evidence; N=192 kept distinct from theorem-scale and infinite-tail.

## 1. Partition-invariance guardrail [D]

The Schur identity f^*T^{-1}f = f_Q^*D^{-1}f_Q + g^*S^{-1}g verified two ways: analytically (standard block-inversion expansion) and numerically (5 random SPD trials, agreement <10^{-10}). Basis-independence of the full source energy confirmed directly: two different complete splits of a random operator agreed to 5.6×10^{-17}. The guardrail logic — "C_frozen = C_ideal is algebraic invariance, not an alignment test" — is airtight as a negative claim: any complete split eliminated exactly returns the same capacity, so the agreement carries zero alignment information. The entry correctly lists the real evidence separately. **Confirmed.**

## 2. Principal angles [N]

Recomputed from the reported cosine spectra: even max 0.2586376481°, odd max 0.6056861340° — match to 10 digits. "Small" is quantified via full spectra. The conclusion is appropriately modest: it justifies *a theorem-scale frozen-carrier test*, not certification. **Sufficient for the stated purpose.**

## 3. Complement floors [N]

Even λ_min = 0.17117 (drift ~10^{-5} vs ideal); odd λ_min = 0.55089 (drift ~4.5×10^{-5}, frozen slightly higher). Positive with margin, scoped to N=192 as the entry states. **Confirmed.**

## 4. Key question [G]

**YES, for the decision as framed.** The N=192 evidence justifies *running the M3999/4000 test* without regenerating the basis — which is all v14.005 claims. It would not suffice to *certify* the split, which the entry explicitly does not claim. The remaining gap is closed by the entry's own §5 list (complement positivity, joint Schur reduction, source alignment, scalar crossing, residual quality at M3999/4000). No additional check needed.

## 5. CI repair [N]

The false-green (missing pipefail; mpmath multi-RHS LU death) was infrastructure, not mathematics. The repairs address root causes and the run re-completed fail-closed. Catching a silent failure correctly **increases** confidence. Note: the mpmath failure mode is worked around, not root-caused — fine at N=192, may need performance attention at theorem scale.

## 6. Notes (not obstructions)

- Odd-sector 4th principal direction (0.606°) is ~10× worse than the other three — disclosed; watch at scale-up.
- Scale distinctions (N=192 vs M3999/4000 vs infinite tail) maintained throughout; the entry does not overclaim.

## 7. Verdict

**THEOREM-WITH-NOTES.** Guardrail proof exact, evidence-to-decision match sound, no obstruction to the capacity program's next gate.

---

HANDOFF-ACK
from: v14.005
target: lane-a
status: closed
result: theorem-with-notes — guardrail verified, frozen-P4 test decision justified as framed; watch odd 0.606° direction at scale-up
