# Cone Derivation Ledger v14.001 — Sandbox: Parity Source-Energy Numerical Route Verdict (Direct Inversion Non-Viable; Bracket-Check Design)

**Date:** 2026-10-04
**Track:** Sandbox (our Lane B), Lane-A support task
**Status:** [N] 100×100 even-sector probe; [D] fundamental ill-conditioning diagnosis; [I] bracket-check cross-check design; [O] odd-sector assembler mirror in build.
**Parents:** v13.994, v13.997, v13.782
**Authorization:** Jeremy, 2026-10-04 ("hit all 4" support tasks)
**Collision check:** live HEAD immediately before this write was v13.999; no v14.001 entry was present.

---

## 0. Purpose

Lane A's capacity program will produce certified brackets μ_- < C < μ_+ for the parity capacities. The sandbox investigated computing G_e = ⟨cosh,(T_a^{(+)})^{-1}cosh⟩, G_o = ⟨sinh,(T_a^{(−)})^{-1}sinh⟩ numerically as an independent cross-check. This entry records the verdict.

## 1. Numerical probe [N]

A correct even-sector T_a discretization exists (`finite_matrix` in research-notes/suzuki_feshbach_buffer_anatomy.py: C+B+K+P with the essential rank-one pole term 2ccᵀ; the pole-free A0 variant is indefinite on low modes, λ_min ≈ −4.25, and must not be used). A 100×100 even-sector probe found **four numerical null modes at ~−1.5×10^{-12}** with **~10% source-overlap²** of cosh on them. Direct solve returned **G_e = −5.9×10^{12}** — negative, physically impossible, pure noise. The KKT/Feshbach payload is likewise unusable here (v13.987's singular 6×6).

## 2. Diagnosis [D]

This is **fundamental, not a bug**: T_a's genuine near-null space combined with significant source overlap makes G_e/G_o ill-conditioned as quadratic forms. It is the same obstruction, in numerical form, as v13.987's inverse-stability failure — and an independent confirmation of why Lane A abandoned the inverse route for inertia thresholds. Direct double-precision computation of the parity source energies is **not viable**.

## 3. Viable alternative: bracket-check design [I]

Do not compute G_e. Instead, when Lane A publishes certified endpoints μ_±, independently **sign-count (eigencount) T − μ_±ff*** at those endpoints: opposite inertia at the two endpoints confirms the bracket. This is cheap (one eigendecomposition per endpoint per parity), honest (it checks exactly what Lane A claims), and matched to their deliverable. Missing piece: a standalone odd-sector assembler mirror of `finite_matrix` — in build in the sandbox workspace now.

## 4. Consequence

The κ_a-vs-a trend mapping is blocked until a value route exists; it is parked, not dropped. The sandbox's numerical role in the capacity program is bracket-checking, not value computation.

---

*Staged builder's note: the odd-sector assembler and its sanity checks live in the sandbox workspace until reviewed.*
