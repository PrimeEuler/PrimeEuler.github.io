# Cone Derivation Ledger v14.000 — Sandbox: Audit of v13.997 Direct Relative-Border Invertibility (Theorem, No Obstruction)

**Date:** 2026-10-04
**Track:** Sandbox (our Lane B), audit deliverable
**Status:** [D] operator-domain argument verified step by step; [D] rank-one Fredholm determinant evaluation verified; [D] parity reduction verified; [D] capacity-bridge identification verified against v13.994 §1; [N] N^{-1/2} tail formulas independently recomputed; [G] finite-a vs a→∞ kept distinct; [C] no KKT rebuild used.
**Parents:** v13.997, v13.782, v13.791, v13.994–995
**Authorization:** Jeremy, 2026-10-04 (v13.997 HANDOFF block, type: audit, deliverable: theorem-or-obstruction)
**Collision check:** live HEAD immediately before this write was v13.999; no v14.000 entry was present.
**Handoff protocol:** research-notes/CROSS_LANE_HANDOFF_PROTOCOL.md.

---

## 0. Purpose

Close the v13.997 HANDOFF block (target: sandbox, type: audit): audit the operator-domain argument that the full −i border is boundedly invertible from source-level T_a^{-1} and F_a(−i)>0, and audit the resulting direct rank-one Fredholm determinant identity without assuming complement D invertibility, checking v13.782 and v13.791 explicitly and keeping finite-a distinct from a→∞.

## 1. Source assumptions [D]

- **v13.782** (read directly): for λ < λ_a, T_a = A_a − λI invertible on L²(−a,a) with bounded inverse; T_a commutes with reflection R. Confirmed.
- **v13.791** (read directly): F_a(−i) = ⟨v_{a,+i}, T_a v_{a,+i}⟩ = ‖v_{a,+i}‖²_{T_a} > 0, strictly positive (stronger than the ≠0 needed). Confirmed.
- **v13.994 §1** (read directly): C(T,f) = 1/⟨f,T^{-1}f⟩ is exactly the rank-one positivity-loss threshold. The v13.997 §9 identification C_p = G_p^{-1} is exact, not formal. Confirmed.

## 2. Operator-domain argument (§5) [D]

𝔅_- = [[T_a,b],[−p_-^*,0]] on D(T_a)⊕ℂ, b = p_- = e^x ∈ L²(−a,a). The solve x = T_a^{-1}y − cT_a^{-1}b, c = (η+⟨b,T_a^{-1}y⟩)/F_a(−i) was verified equation by equation: x ∈ D(T_a) since Ran(T_a^{-1}) = D(T_a); T_a x + cb = y; −⟨b,x⟩ = η using ⟨b,T_a^{-1}b⟩ = F_a(−i) (T_a self-adjoint); the inverse is bounded ℋ⊕ℂ → ℋ⊕ℂ. **No domain gap; complement D never enters.** Confirmed.

## 3. Determinant identity (§6–9) [D]

𝔅_+ − 𝔅_- rank one ⟹ trace class independent of tail speed; det_F(I+K_rel) exists as ordinary Fredholm determinant; the 1+⟨v,u⟩ evaluation gives F_a(i)/F_a(−i); parity reduction gives (G_e−G_o)/(G_e+G_o) = (C_o−C_e)/(C_o+C_e) with cross-parity terms vanishing by R-commutation. **Confirmed step by step.**

## 4. Tail numerics (§1–3) [N]

Independently recomputed from the exact coefficient formula: Δp_n = 0 on odd n exactly; n·Δp_n → 8sinh(1)/π = 2.992625265534507 (16 digits); two-sided ℓ² bound holds at N = 10, 100, 1000; trace-norm constant 4√2 sinh(1)/π = 2.1161056188096423 (16 digits). The v13.995 faster-tail hope is refuted as stated — but the determinant never needed it. Confirmed.

## 5. Constraints

No KKT machinery used. No a→∞ limit taken anywhere in §5–9; the entry keeps exact finite-a distinct from the asymptotic program. Minor notes only: the P_N⊕I convention in the trace-norm identity could be stated; the ψ_n basis absorbs a (−1)^{(n−1)/2} phase — neither affects any conclusion.

## 6. Verdict

**Theorem — no obstruction.** The v13.995 hypotheses (H1)/(H4) are discharged exactly as v13.997 claims. The remaining work is Lane A's §12 inertia program, outside this audit's scope. (External Audit Round 153 independently re-derived v13.997 eq1–27 the same day and concurs.)

---

HANDOFF-ACK
from: v13.997
target: lane-a
status: closed
result: theorem — operator-domain argument and determinant identity verified; no obstruction found; tail formulas independently recomputed
