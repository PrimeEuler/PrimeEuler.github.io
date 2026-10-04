# Cone Derivation Ledger v13.999 — Sandbox: Outward-Machinery Scout for the Capacity Program (Relay to Lane A)

**Date:** 2026-10-04
**Track:** Sandbox (our Lane B), Lane-A support task
**Status:** [D] identification of the M3999/4000 cutoff; [D] three-layer outward architecture mapped; [I] adaptation analysis for the v13.994 §13 / v13.997 §12 capacity program; [O] central build task named (μ-interval inertia bracket); [N] two unreferenced N=192 capacity prototypes located in research-notes/.
**Parents:** v13.994, v13.997, v13.401, v13.443, v13.555, v13.809–810
**Authorization:** Jeremy, 2026-10-04 ("yes" — relay outward-scout findings to Lane A via the ledger channel)
**Collision check:** live HEAD immediately before this write was v13.998 (External Audit Round 153); no v13.999 entry was present.
**Handoff protocol:** research-notes/CROSS_LANE_HANDOFF_PROTOCOL.md.

---

## 0. Purpose

At Jeremy's direction ("hit all 4" support tasks, 2026-10-04), the sandbox scouted the "theorem-scale M3999/4000 outward machinery" that v13.994 §13 and v13.997 §12 prescribe adapting for the protected-core source-capacity inertia certification. This entry relays the findings to Lane A. Full scout report (16-script inventory, per-entry technique notes) was staged in the sandbox workspace; this entry carries the decision-relevant content.

## 1. What M3999/4000 is [D]

A **mode-index cutoff**, not an entry number. The finite block F holds modes ≤3999 (odd modes, even sector; v13.401 §1, v13.809 §3) or ≤4000 (even modes, odd sector; v13.443 §0); modes ≥4001/4002 form the "stiff remote complement." This is exactly the split v13.994 §13 step 2 / v13.997 §12 step 2 require.

## 2. The machinery: three layers [D]

1. **Frozen finite side** (v13.809): exact-dyadic 10×6 bases Q_± + 6×6 preconditioners L_0,±; structured pole-free LDL^T with outward residuals <5.5×10^{-11}; Sherman–Morrison pole update; six-RHS solves (residuals <2×10^{-15}); v13.357 source budget ε=2×10^{-13}. Output: C_± > 0.9999992I. Held fixed — "no basis regeneration."
2. **Tail floors** (v13.810): mpmath 80-digit intervals; γ_e(4001) > 2.75305442, γ_o(4002) > 2.75316939; combined γC bounds >2.75305I both sectors.
3. **Remote-Gram ceilings** (v13.401: explicit 4001→2M accumulation h=0.17821… + far tail <4×10^{-4} → ind_{≤0}(S_10)≤4; v13.443: ‖A_FT‖<1.015 → δ_odd>0.637). Dependency DAG frozen in v13.555 (M16001 scale — not to be confused with M3999/4000).

Per v13.994 §5, this architecture was built to prove **inertia statements without ever bounding a large indefinite inverse** — the same property the capacity program needs.

## 3. Adaptation: what transfers, what changes [I]

**Transfers directly:** the entire tail layer — tail floors bound exactly the h = f_Q^*D^{-1}f_Q and coupling g entering v13.994 eq (12), S_μ = S − μ/(1−μh)·gg*; the frozen-core discipline and exact-dyadic technique; all outward arithmetic infrastructure; the Schur-elimination algebra itself. No new tail analysis needed in principle.

**Changes:** the protected block must be selected by **source activity** (diagnostic: 2 source-active modes + 4 near-zero tail resonances — again 6D, different 6-plane), not positivity; the certified object becomes a **μ-bracket** μ_- < C < μ_+ via opposite inertia, not a fixed inequality; O(1) normalization is new (diagnostic suggests α_* = C/(1−Ch) = 1/r as the dimensionless variable).

## 4. Gaps [O]

1. **No μ-interval inertia certificate exists** — the LDL-with-certified-pivots machinery (v13.809 §3–4) yields pivot signs but was never run on S_μ over a μ-interval. **This is the central build task.**
2. μ-interval propagation through μ/(1−μh) needs an outward h^U with μ_+·h^U < 1.
3. Theorem-scale freezing of the source-active six-plane is open (only N=192 diagnostic exists).
4. If building on the ρ=0.10 endpoint line, note v13.810 §6's still-open remote-Gram replay gate; the ρ=0 line (v13.401) is fully closed.

## 5. Headline find: unreferenced prototypes [N]

Two research-notes scripts already implement the capacity architecture diagnostically and are **not referenced** in v13.994/v13.997's text:

- `suzuki_protected_sixplane_capacity_decomposition.py` — "the architecture intended for the theorem-scale M3999/4000 gate: only the stiff complement is inverted. The dangerous six-plane is never treated perturbatively." N=192.
- `suzuki_source_capacity_core_crossing_diagnostic.py` — rewrites the v13.801 high-precision source/Feshbach output in v13.994's rank-one variables (G = h + r, C = 1/G, α_* = 1/r). N=192.

These are the natural starting point for the build (recommended order: promote N=192 prototype to M3999/4000 midpoint → outward-enclose h, g with existing tail bounds → build the μ-interval inertia bracket → propagate [C_e], [C_o] through κ).

---

HANDOFF
target: lane-a
type: task
parent: v13.999
status: open
action: Consider the two unreferenced N=192 capacity prototypes and the adaptation analysis (§3–§5) when building the μ-interval inertia certificate for the v13.994/v13.997 capacity program.
deliverable: diagnostic
constraints: Read-only use of sandbox findings; no sandbox repo writes requested.
