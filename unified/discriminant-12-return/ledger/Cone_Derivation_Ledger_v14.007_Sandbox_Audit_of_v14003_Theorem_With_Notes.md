# Cone Derivation Ledger v14.007 — Sandbox: Audit of v14.003 Scalar Capacity Crossing (Theorem-with-Notes)

**Date:** 2026-10-04
**Track:** Sandbox (our Lane B), audit deliverable
**Status:** [D] scalar reduction re-derived; [D] augmented-Schur identity re-derived; [D] PSD quadratic error verified; [D] form-domain survival answered YES; [N] all §6–8 diagnostic numbers independently recomputed (16 digits); [G] no a→∞ smuggling; [C] no 6×6 rebuild.
**Parents:** v14.003, v13.994, v13.997, v13.999
**Authorization:** Jeremy, 2026-10-04 (pre-authorized: "go ahead and ledger when they come back, Lane A is waiting")
**Collision check:** live HEAD immediately before this write was v14.006; no v14.007 entry was present.
**Handoff protocol:** research-notes/CROSS_LANE_HANDOFF_PROTOCOL.md.

---

## 0. Purpose

Close the v14.003 HANDOFF block (target: sandbox, type: audit, deliverable: theorem-or-obstruction): audit the source-aligned scalar crossing theorem and the augmented-Schur identity, including whether the PSD quadratic error formulation survives the exact form-domain implementation of the outward M3999/4000 split. Constraints honored: no 6×6 inverse rebuilt; exact algebra separated from the N=192 diagnostic and from any a→∞ claim.

## 1. Scalar reduction (§1–2) [D]

Re-derived via block inversion: f^*T^{-1}f = g^*S^{-1}g + h with S = A−E^*D^{-1}E, g = f_P−E^*D^{-1}f_Q, h = f_Q^*D^{-1}f_Q; C = α_*/(1+α_*h) with α_* = 1/r. Householder alignment U^*g = βe_1 gives g^*S^{-1}g = β²/s, α_* = s/β²; Schur PSD criterion yields S−αgg^* ⪰ 0 ⟺ α ≤ s/β². **All steps verified.**

## 2. Augmented-Schur identity and PSD quadratic error (§3–4) [D]

Completing the square: J−s = e^*D_⊥^{-1}e ≥ 0 with J the computable surrogate — error genuinely quadratic in e. Joint elimination: K̃−K = R^*D^{-1}R with R = C−DY, verified term by term; ⪰ 0 since D ≻ 0; ‖K̃−K‖_2 ≤ ‖R‖_2²/γ. The "correlated errors" claim is sound: one Y for all blocks gives a single PSD error form — exactly what one-sided certification needs. **Verified.**

## 3. Key question: form-domain survival at M3999/4000 [D]

**YES.** The identity survives iff (a) D_Q ⪰ γI > 0 self-adjoint — the entry's own stated stiff-floor requirement, backed by outward tail floors (v13.810, v13.443); and (b) Ran(Y) ⊂ D(D_Q) — **not explicitly flagged in the entry, but automatically satisfied by any truncated/finite-mode Y**, which is what the §11 joint solve produces. Minor note, not an obstruction. The far-tail completion is the entry's own named missing item (§11), honestly flagged as future work.

## 4. Diagnostics (§6–8) [N]

Every printed number independently recomputed: α_* = s/β² both parities, λ_min(D_⊥)/s ratios (6.48045×10⁵, 4.55095×10⁴), C_e/C_o, κ_192 = 0.9999295337492166 — all match to 16 digits. Marked [N] throughout with explicit disavowal of finite-a Xi and a→∞ promotion. The §10 precision argument checks out: ‖R‖ ≲ 10^{-15} ⟹ ‖K̃−K‖ ≲ 10^{-30} via the quadratic identity — which is exactly why the quadratic (not first-order) formulation is the enabler.

## 5. Other checks

Old reconstruction failure (§5): correctly diagnosed (σ_min ≈ 2×10^{-16}, coefficients ~10^{15} — consistent with v13.987 and our independent G_e = −5.9×10^{12}). No a→∞ limit taken anywhere. Parents used correctly (v13.994, v13.997, v13.999 integrated accurately; v13.980 citation plausible but not independently verified).

## 6. Notes (not obstructions)

- §2 tacitly needs g ≠ 0 and s > 0 — natural for a source-active block, unstated.
- v13.980 citation not independently verified.

## 7. Verdict

**THEOREM-WITH-NOTES.** Every algebraic step re-derives cleanly; the PSD formulation survives the M3999/4000 form-domain implementation under the entry's own stiff-floor requirement; diagnostics honestly marked and internally consistent. No obstruction.

---

HANDOFF-ACK
from: v14.003
target: lane-a
status: closed
result: theorem-with-notes — scalar reduction, augmented-Schur identity, and PSD quadratic error all verified; form-domain survival confirmed under stated stiff-floor requirement
