# Cone Derivation Ledger v14.705 — Sandbox deposit (Jeremy-directed): the expanded bath-note results — hot-bath fixed point is a cone ray pair (√3:1:2, e₀ = √(2/3)); the G lever as pure T-axis rotation (Mercury 42.98″/cy reproduced)

**Timestamp:** 2026-10-22 (EDT)
**Lane:** Sandbox (little Euler), deposited on Jeremy's explicit line ("we need to ledger the expanded bath note results," 2026-10-22). Not a Lane A handoff response.
**Parents / provenance:** the bath note is Jeremy's Kepler/cone EFT draft v3.4 (`Kepler_Cone_Revised_EFT_Draft_v3_4_Elevated_Hot_Benchmark`, August corpus; workspace `explorations/kepler-eft/` — the draft itself is **not** part of this deposit and was never previously moved into this repo or a foundations folder; a repo-wide check at deposit time found no Kepler/bath/EFT file in `research-notes/` and no bath entry in the ledger). The expansion results were produced in sandbox run `20261021-eft-play/` (2026-10-21, workspace-only until now) and were **re-run from the deposited producer files at deposit time** (2026-10-22), reproducing every number below. The deposit was prompted by the gravity-lane discussion of 2026-10-22 (v14.700–704), in which Jeremy recalled — correctly — that the ray result "handled eccentricity"; §4 states precisely in what sense it does and does not.

## 1. The cone dictionary for the bath's shape coordinate [D/N]

From the corpus's epicycle radii A = √x, B = √y with x = T+X, y = T−X, Y = √(xy), the ellipse semi-axes are a = A+B, b = |A−B|, and

\[
e^{2}=\frac{4AB}{(A+B)^{2}}=\frac{2Y}{T+Y},\qquad q^{2}=1-e^{2}=\frac{T-Y}{T+Y},\qquad q=\sqrt{\frac{T-Y}{T+Y}}.
\]

So v3.4's bath shape coordinate q is a cone function. Machine-verified against direct ellipse geometry on 2,000 random ellipses: max error **6.11×10⁻¹⁶** (producer `play.py`, re-run at deposit).

## 2. The hot-bath fixed point is a ray pair [D]; the flow attracts to e₀ = √(2/3) [N]

v3.4's hot-bath attractor is q₀ = 1/√3 (q₀² = 1/3). In cone coordinates, (T−Y)/(T+Y) = 1/3 ⟺ **Y = T/2**: the attractor is the cone direction

\[
X : Y : T = \sqrt{3} : 1 : 2,
\]

two generators of the cone (X = ±(√3/2)T, Y = T/2), with null-coordinate ratio on the ray (T+X)/(T−X) = (2+√3)/(2−√3) = **7 + 4√3 ≈ 13.92820323**. The bath selects no point and no scale — T stays free — it selects a **direction**: one ray pair, the cone's spin-0-shaped locus (fixed direction, free scale; Jeremy's "a scalar would just be a ray," in dynamical form). The reduced hot-limit shape flow dq/dt = −C(3q²−1)/q (the sign structure of v3.4's ⟨L s⟩, s = 1−q) attracts from every tested start — e = 0.9968, 0.9539, 0.8167, 0.5268, 0.1411 all converge to **e₀ = √(2/3) = 0.816497**. Figure `fig_eft_play.png` (flow + cone, canonical parabola mesh) is in the payload.

## 3. The G lever [D/N]: a central perturbation is a pure rotation about the T axis

Completing the EFT note's unfinished averaging for a **central** perturbation: energy and L are conserved and e is secularly fixed, so on the cone the point can only **rotate about the T axis** — and the Lie–Poisson bracket generates exactly that motion from H = εT (dX/dt = εY, dY/dt = −εX; the producer's bracket flow is a pure rotation, T fixed, radius² conserved to integrator accuracy). The GR 1/r³ term is such a perturbation: its entire secular effect is that rotation, at per-orbit angle Δϖ = 6πμ/(c²p), with the semi-latus rectum in cone coordinates p = (2T−2Y)/√(2T+2Y) and the time average ⟨1/r³⟩ = 1/(a³(1−e²)^{3/2}) verified numerically against the cone form at three test points (exact agreement at producer precision). **Mercury through the cone formula: 5.0187×10⁻⁷ rad/orbit = 42.98 arcsec/century** — the standard GR value, reproduced as a consistency check of the cone form (not new physics). Honest split, as recorded in the run: astronomy's rotation lever measures GM (the product); a lever on G itself remains the lab hardware of the rotor/seat line (v14.630, v14.700, v14.702). The lever's *shape* exists in the EFT: a motion that does nothing but turn, whose rate is the coupling.

## 4. Claim discipline, and the relation to v14.701/v14.703

This is **classical dynamical selection**: kinematics (the cone) plus contents (the Maxwellian bath) strike a balance at a pure number, and the eccentricity is handled by an explicit drift with a stable fixed point. It is a template with a worked example — **not** a fundamental constant, and it does not touch the quantum-side results of the same day: v14.701/v14.703 concern the phase-integral *lobe family* I_jm(ρ), which carries no bath, no drift, and no ρ-selecting operator; nothing here supplies one. The two results are complementary bookkeeping on the same word: eccentricity *can* be selected where contents push on it (this entry, classical), and is *not* selected by the bare phase construction (v14.703, quantum profiles). The bath note's own remaining open items (the detailed secular phase analysis, cold-bath sign structure) are the draft's, not this deposit's.

## Verification

Producers `play.py` and `lever.py` were re-executed from the exact deposited bytes at deposit time; outputs match the run's recorded `play.out`/`lever.out` and the payload `RESULTS.md` (dictionary 6.11×10⁻¹⁶; fixed point and null ratio to the digits shown; five flow starts → 0.816497; ⟨1/r³⟩ three-point agreement; Mercury p from cone coordinates equal to the direct a(1−e²) to all shown digits, 5.546039×10¹⁰ m). Payload `research-notes/payloads/sandbox_bath_note_expansion_v14_705/` carries both producers, `RESULTS.md`, the figure producer `fig_eft_play.py`, the figure `fig_eft_play.png` (canonical mesh), and `MANIFEST.sha256`.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `exploratory_deposit_on_jeremy_line = true`; `far_tail_touched = false`; `papers_modified = false`; `bath_note_draft_deposited = false (expansion results only)`; `G_derived = false`; `fundamental_constant_claimed = false`; `selection_type = CLASSICAL_DRIFT_FIXED_POINT`; `hot_bath_fixed_point = q0 = 1/sqrt(3), ray X:Y:T = sqrt(3):1:2, e0 = sqrt(2/3)`; `mercury_check = STANDARD_GR_VALUE_REPRODUCED`.
