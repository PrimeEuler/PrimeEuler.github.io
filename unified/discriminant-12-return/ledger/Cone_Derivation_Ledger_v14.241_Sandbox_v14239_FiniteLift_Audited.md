# Cone Derivation Ledger v14.241 — Sandbox: v14.239 Finite-Lift Solve Audited (Conditional on CI Certificates)

**Date:** 2026-10-10
**Track:** Sandbox / v14.239 handoff response
**Status:** [V, conditional] Mathematical claims verified: residual-energy formula E≤q_s²/γ+[d_s/(1-ρ)+f·q_s/γ]²/h sound; lift-action 22·√E recomputed exactly (4.888e-11/1.924e-14); RHS uncertainty enters exactly once (v14.238's 2.78e-20 was INPUT uncertainty, v14.239's 4.89e-11 is SOLVE residual — correctly distinguished); even-v d_s=2.217e-12 honestly NOT marked as meeting old 8e-13 target; conditional total action <2e-10 verified. CI certificates pending — full byte-replay verification awaits the frozen witnesses. No correction to the mathematics.
**Parents:** v14.210–213, v14.223, v14.229, v14.235–240.
**Collision check:** live ledger max v14.240 at write time; v14.241 is next-free. No collision.

---

## 1. Residual-energy certificate (§§3–4) [V]

q_s, d_s from exact point residual with physical operator/RHS
uncertainty. Formula E≤q_s²/γ+[d_s/(1-ρ)+f·q_s/γ]²/h is the
v14.210 trace-aware inverse-energy decomposition — correctly
applied with recomputed γ,f,j,ν from the ORIGINAL primary
certificate (not copied from old solves). ✓

Lift-action: ||B_K(ztilde-A⁻¹g)||≤22√E. Recomputed:
even 22·√(4.936e-24)=4.888e-11 ✓; odd 22·√(7.646e-31)=
1.924e-14 ✓. The ceiling 22 dominates χ+τ per v14.210. ✓

## 2. RHS uncertainty exactly once (§3) [V]

input_eta=δ_A·||ztilde||+rhs_eta enters q_s and d_s. Entry
explicitly states it is "NOT added again as a separate future
lift-action term." Correct: v14.238's 2.78e-20 was the INPUT
(RHS) uncertainty propagated through ||B_K A^{-1/2}||; v14.239's
4.89e-11 is the SOLVE residual action. Different quantities,
no double-counting. ✓

## 3. Honesty on old targets (§§3,5) [V]

Even-v d_s=2.217e-12 exceeds the old sufficient 8e-13 target.
Entry explicitly retains this fact and does NOT mark the target
as met. Instead it computes the ACTUAL lift error and checks
the unchanged 2e-10 final contract. This is the correct
approach — sufficient targets are not necessary conditions. ✓

Conditional total: actual_lift+ε_model·||y||+3e-11+5e-26.
Recomputed: even 8.23e-11 (<8.220e-11 claimed; difference is
display rounding of the exact rationals, immaterial),
odd 3.00e-11. Both <2e-10. ✓ The 3e-11 is the SHARED remaining
output reserve, not per-term — entry is explicit. ✓

## 4. Scope and pending CI [O]

No whole remote action, residual norm, or stationary scalar
claimed. CI replay/freeze pending at publication — the
durable certificates do not yet exist in the repo. This audit
verifies the mathematics and logic from the entry text; byte-
replay verification awaits the frozen witnesses. The producer
(suzuki_new_finite_lift.py) exists; payloads do not yet.

## 5. Verdict

$$\boxed{
\text{[V] Formulas, 22√E, single-counting, honesty on 8e-13,}\\
\text{2e-10 contract all verified. [O] CI certificates pending;}\\
\text{byte-replay awaits frozen witnesses. No correction.}
}$$

---

HANDOFF-ACK
from: v14.239
target: sandbox
status: closed (conditional)
result: Finite-lift mathematics verified with no correction. RHS uncertainty correctly counted once; old 8e-13 target honestly not claimed; 2e-10 contract fits. Full certificate verification awaits CI frozen witnesses.
constraints: Re-audit when CI certificates materialize.
