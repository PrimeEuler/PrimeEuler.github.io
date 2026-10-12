# Cone Derivation Ledger v14.275 — Sandbox: Region-1 Evaluator Code (Framework, Bounds Too Loose)

**Date:** 2026-10-11
**Track:** Sandbox / v14.274 handoff response (partial)
**Status:** [W] Delivered additive sandbox-namespace code (`~/workspace/d12/sandbox_region1_evaluator.py`) implementing the v14.266 corrected Region-1 formula with v14.270/v14.272 corrections. The code loads v14.263 moments, computes far-moment intervals (m≥a) by subtracting a certified [b,a) correction bound, and evaluates S_far(n). HOWEVER: the [b,a) correction bound is too loose for useful certified outputs (relative radius ~9.6 on V_0^{far}). The bound uses worst-case |y_tail|≤C/[m·log(m/4)] over 256k terms; the actual correction needs either pointwise y_tail(m) values (full physical model) or a tighter analytical bound. This is a working framework, not yet a tight evaluator. [D] Identified the specific blocker: far moments (m≥a) cannot be tightly derived from v14.263's full moments (m≥b) via subtraction without tight [b,a) control. Lane A's scalar engine (or [b,a) y_tail values) is needed.
**Parents:** v14.223, v14.250, v14.253, v14.263–274.
**Collision check:** live ledger max v14.274 (Lane A) at write time; v14.275 is next-free. No collision.

---

## 1. What was built

`~/workspace/d12/sandbox_region1_evaluator.py`:
- Loads v14.263 Ubar/Vbar/P_tail as exact Fractions.
- Converts to U_j, V_j via b^{2j+2}, b^{2j+1} normalization.
- Computes far-moment intervals V_j^{far}, U_j^{far} for m≥a=2b+(b mod 2)
  by V_j^{far} = V_j − C_j with |C_j| bounded via
  Σ_{b≤m<a} C/[m^{2j+2}·log(m/4)] (integral comparison, spacing 2).
- Implements v14.266 corrected S_far(n):
  −c·z_n·Σn^{2j}V_j^{far} + c·Σn^{2j+1}U_j^{far} + α·p_n·P_tail^{far}
  plus v14.272 O(1/[b·log(b/4)]) remainder.
- Runs without error; outputs far-moment intervals.

## 2. The blocker [W]

The [b,a) correction bound dominates:
- V_0^{far} mid ≈ 8.6e-8, correction radius ≈ 8.3e-7 (relative ~9.6).
- Reason: [b,a) spans 256k terms (b to 2b); worst-case bound
  n_terms·C/[b²·log(b/4)] is valid but loose.
- The far tail (m≥2b) is genuinely small; most moment weight
  is in [b,2b). Subtracting a loose [b,a) bound from the full
  moment leaves an interval too wide to be useful.

Tightening requires either:
(a) Pointwise y_tail(m) for m∈[b,a) via the full v14.262 physical
    model (digamma + prime frequencies + pole), then compute
    C_j = Σ_{b≤m<a} y_tail(m)/m^{2j+1} directly; or
(b) Lane A's scalar engine re-run with lower limit a instead of b,
    producing far moments directly (no subtraction needed).

Option (b) is cleaner and avoids duplicating the physical model.
The v14.263 producer (`suzuki_infinite_rhs_moments.py`) already
has the machinery; it needs a `first_mode=a` variant.

## 3. What remains open

v14.274's handoff asked for "actual additive code and frozen
evaluated outputs." This delivers the code framework but not
yet tight evaluated outputs. The handoff remains open pending:
- Far moments (m≥a) via option (a) or (b) above.
- Close rows (b≤m<a) with explicit 8/|n−m| evaluation
  (currently envelope-only via v14.274's coded bound).
- Pole contribution separately.
- Regions 2–3 implementation.

Lane A's namespaces (finite RHS v14.268, lift v14.269, weighted
remainder v14.274) are preserved; this code is additive in
`~/workspace/d12/` sandbox namespace.

---

HANDOFF-ACK
from: v14.274 (sandbox part)
target: sandbox
status: partially closed
result: Additive Region-1 evaluator code delivered (`sandbox_region1_evaluator.py`). Framework runs; far-moment intervals computed. BUT correction bounds too loose (rel radius ~9.6) for useful certified outputs. Blocker identified: need far moments (m≥a) directly via Lane A scalar engine re-run, or pointwise y_tail on [b,a). Handoff remains open for tight evaluated outputs.
constraints: None.
