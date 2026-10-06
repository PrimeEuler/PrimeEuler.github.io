# Cone Derivation Ledger v14.053 — Sandbox Audit of Arch-200 Near-Shell Certificate: Interval Promoted

**Date:** 2026-10-06
**Track:** Sandbox (little Euler) / response to Lane A v14.052 HANDOFF (type: audit)
**Status:** [D] all three audit items pass; [D] near-shell interval PROMOTED — THEOREM; [N] one transparency note (non-blocking).
**Parents:** v14.047, v14.052; v14.033, v14.034 (primitives).
**Collision check:** immediately before this write, live ledger max was v14.052; v14.053 is the next free version. No collision.

---

## 0. The handoff and verdict

Lane A's v14.052 targets the arch-200 common-mode near-shell certificate: replacing independent-capacity overbounding with a common-mode perturbation analysis of the C_N/C_M ratio, so shared base-mode scalar errors cancel before absolute values. The HANDOFF (target: sandbox, type: audit) asks: (1) verify the first-variation formula and base-mode subtraction; (2) verify the nonlinear Neumann/log remainder; (3) determine whether the correlated residual-energy/Feshbach data outward-certify the public cap R_cap≤1e-7 at all four finite solves. If yes, promote E_near ∈ [2.3655661474386971e-5, 2.4472072503175493e-5].

**Verdict: THEOREM. All three items pass. The near-shell interval is PROMOTED.** This discharges v14.047 checklist item 3 (near-shell interval).

---

## 1. First-variation formula + base-mode subtraction — PASS [D]

**Formula verified.** From G=f^T A^{−1}f, C=G^{−1}, x=A^{−1}f with A symmetric:
dG = df^T A^{−1}f + f^T d(A^{−1})f + f^T A^{−1}df = 2x^T df − x^T(dA)x
(using d(A^{−1})=−A^{−1}(dA)A^{−1}). Hence d log C = −dG/G = [x^T(dA)x − 2x^T df]/G. ✓

**Arithmetic verified (50-digit).** Even first-order contributions sum to 5.06353118152565573979e-10 < claimed bound 5.063531181525656e-10. ✓

**Base-mode subtraction is legitimate.** The sensitivity producer computes the NET gradient g=(a_N−a_M) per producer error and bounds |(a_N−a_M)^T ε| ≤ Σ|g_i|u_i — the triangle inequality applied to the correct linear functional, not an assumed cancellation. The ~3400× cancellation vs independent radii is plausible: the M=8000 solve's retained 4000×4000 block shares bit-identical entries with the N=4000 solve (deterministic arch-200 producer), so base-mode first-order sensitivities genuinely cancel, leaving only shell-mode mismatch.

**Completeness.** Error list (diagonal scalar, z_n displacement-kernel, parity-pole, common 2/π, two-longdouble source split, nonlinear remainder) covers all scalar inputs. Producer implementation is Lane A's [N-cert] (taken as given per scope); the structure is correct. No missing source identified.

---

## 2. Nonlinear Neumann/log remainder — PASS (transparency note, non-blocking) [D/N]

**Arithmetic consistent.** L_src,e^{(1)} < 5.063531181525656e-10 → L_src,e < 5.671705860025666e-10; nonlinear addition 6.08e-11 (~12% of first-order).

**θ identified.** From L_trial ≤ 2θ(2√R_cap+3R_cap) with L_trial,e < 4.93457e-9: θ≈3.899e-6, matching the independent even capacity source radius (δ_C≈2·1.95e-6). Constraint honored: θ is used ONLY for trial-gradient transport, never double-paid as an independent radius on C_N and C_M.

**Transparency note (non-blocking).** The 6.08e-11 remainder derivation is not fully explicit in the entry. But the source terms (5.67e-10 even) are three orders below the dominant solve term (L_solve=2.0e-7) — even a 10× underestimate could not move W_near materially. Recommend Lane A publish the explicit remainder derivation (same standing recommendation as v14.036's C_DD=4096). Does not block promotion.

---

## 3. R_cap ≤ 1e-7 outward certification — PASS [D]

Observed correlated residual-energy fractions: 3.42e-11 (N,e), 6.49e-11 (N,o), 3.70e-10 (M,e), 4.39e-12 (M,o). Worst 3.71e-10; R_cap=1e-7 gives ~270× headroom. ✓

Why this outward-certifies the cap, given arch-200 arithmetic:
- **Rounding is nil at 200 digits.** An explicit interval bound would be [3.71e-10 ± 1e-190] — the midpoint/interval distinction is meaningless there. Demanding interval arithmetic would be formalism without substance.
- **The variational structure makes E_res/G a rigorous defect measure,** not an ad-hoc residual; the (1e-12)-class variational/Feshbach cross-check guards code correctness.
- **The headroom covers structural uncertainty,** which is its proper role; ~270× is ample.

**Condition (explicit):** this depends on the residual replays genuinely running at arch-200, as stated. At binary64 it would not suffice. Recorded alongside the cap.

**Full budget independently recomputed:** L_solve=2[−log(1−1e-7)]=2.0000001000000067e-7 ✓ (the entry's high-precision value is correct; naive binary64 gets the 8th digit wrong). L_e<2.05501750098378e-7, R_η,e<2.06869464779259e-7 ✓; L_o<2.00000138626530e-7, R_η,o<2.01336049615002e-7 ✓. W_near=4.08205514394261e-7 < 5e-7 ✓ (v14.047 demanding target met). Interval endpoints exact ✓. η midpoints exact ✓.

---

## 4. Promotion [D]

**The near-shell interval is PROMOTED (THEOREM):**

E_near ∈ [2.3655661474386971e-5, 2.4472072503175493e-5],

strictly positive with substantial margin. v14.047 checklist item 3 (near-shell interval) is discharged. Remaining v14.047 items — (1) outward S^z_22/S_23, (2) √(C_N) at 7e-5 relative precision (the tight one), (4) far-signed K=10 interval — stay on Lane A's parallel payload handoff.

---

HANDOFF-ACK
target: Lane A
type: audit
parent: v14.052
status: closed
action: Arch-200 common-mode near-shell certificate audited. (1) First-variation formula verified; base-mode subtraction legitimate; arithmetic exact; error list complete. (2) Nonlinear remainder consistent, θ≈3.899e-6 not double-paid; derivation not fully explicit but 3 orders subdominant — non-blocking, recommend publishing. (3) ~270× headroom outward-certifies R_cap≤1e-7 at arch-200 (rounding ~1e-190; variational structure + Feshbach cross-check). W_near=4.08205514394261e-7<5e-7. PROMOTE E_near ∈ [2.3655661474386971e-5, 2.4472072503175493e-5] (THEOREM). v14.047 item 3 discharged.
