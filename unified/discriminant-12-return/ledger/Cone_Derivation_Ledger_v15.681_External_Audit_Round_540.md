# Cone Derivation Ledger v15.681 — External Audit Round 540

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 539/v15.676 (this thread's numbering), Lane A v15.676 (gravity), v15.677 (Suzuki), v15.678, v15.679, v15.680 (all gravity)

## Fresh state at gate

`git fetch origin master` immediately before this write returns `2e80484` (Lane A's v15.680), identical to the head checked throughout this round's work. No new activity landed during the (lengthy) verification of this batch.

## Version-number collision: v15.676

A fourth instance of the by-now-established pattern:

- This audit's own Round 539, `Cone_Derivation_Ledger_v15.676_External_Audit_Round_539.md`, commit `a077b00` at `2026-11-11T16:30:27Z`.
- Lane A's gravity LC-pump entry, commits `b73dc56`/`7615352`, at `2026-11-11T16:31:40Z`/`16:33:05Z`.

This audit's Round 539 is earlier by 73 seconds and keeps the `v15.676` slot; Lane A's two `v15.676`-numbered files are flagged as the losing side and left untouched. Content audited below under its own numbering regardless.

## 1. v15.676 (Lane A numbering) — gravity quarter-grid EM parametric-pump gate

This entry responds to a user proposal that the gravity quarter-grid might act as a free parametric energy source for EM waves, and correctly shows it cannot: any pump requires externally supplied mechanical/electrical work, and the quarter/half grid labels do not themselves select a coupling constant.

**Independent hand derivation**, not just re-running the script:
- Confirmed by direct differentiation that `Ė_EM = -R_s I² - Q²Ċ/(2C²)` for the stated series RLC with time-varying `C(t)`.
- Confirmed the Hamiltonian energy-exchange identity: for `H = p_Q²/(2L) + (1+κx)Q²/(2C0) + P_x²/(2M) + MΩ_G²x²/2`, Hamilton's equations give `dE_EM/dt = +κQ²ẋ/(2C0)` exactly (the two other terms cancel), confirming `dH/dt=0` and that energy moves between the EM and mechanical sectors rather than being created, and that `κ=0` (compatible with existing grid identities) gives zero coupling.
- Confirmed the standard Floquet threshold `h > 4γ/ω0 = 2/Q` at exact 2:1 resonance.

**Re-executed** `research-notes/gravity_em_parametric_pump_v15_676.py` directly (confirmed unchanged since its cited commit `b73dc56` via `git show`); reproduced all 8 cited `(h, Ω/ω0, σ_max/ω0)` table rows exactly.

**Scope assessment:** correctly concludes no energy-from-geometry-alone is possible and that the Cone grid does not select the coupling `κ`; explicitly flags this against future overclaiming. No issue found.

## 2. v15.677 — Suzuki R5 adaptive weight-chart window benchmark

**End-to-end re-execution** of `lane_a_v15_677_suzuki_r5_adaptive_weight_chart_window.py` (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `d53997f3...700f9` [full: `d53997f31224ac5af93d4a8ff919e80642563e6d211d22431bbaf55bd34700f9`]). Reproduced exactly: 7 charts over the 33-arc window `[8635,8667]`, chart widths `1, 10, 5, 3, 1, 8, 5` in order, anchor fourth roots matching to full float precision (e.g. `3.4441371951557507`, `3.4442041448795364`, ..., `3.4435567563883476`), `39` total evaluations, `locally_certified_cover=true`, `local_anchor_failure=null`. All figures match the ledger's cited table exactly.

**Scope assessment:** the entry correctly declines to extrapolate the sampled widths to a whole-R5 or R16 chart count, explicitly flagging the ~20,450-evaluation/~35-hour projection as uncertified. No overclaiming found.

## 3. v15.678 — anisotropic shear Maxwell pump and K4 tensor mode

**Independent hand derivation** of the full Gate 197-200 chain from the metric `ds²=-dt²+e^{2b}dx²+e^{-2b}dy²+dz²`:
- Derived `L_EM=(1/2)e^{-2b}[Ȧ_x²-k²A_x²]+(1/2)e^{2b}[Ȧ_y²-k²A_y²]` directly from `-1/4√-g F²` (confirmed `√-g=1` for this metric).
- Derived the canonical transform result `ü_x+[k²+b̈-ḃ²]u_x=0` (and the mirror-image `y` equation) by hand via `A_x=e^b u_x` substitution.
- Derived the energy-balance identity `Ḣ_EM = ḃ[e^{2b}p_x²-e^{-2b}k²A_x²-e^{-2b}p_y²+e^{2b}k²A_y²]` by hand from the two polarization Hamiltonians.
- Derived the K4 coasting-mode solution `b(τ)=τ^{-1}[C1 cos(ν ln τ)+C2 sin(ν ln τ)]`, `ν=√(8η/3-1)`, by substituting `b=τ^p` into `b̈+3Hḃ+(8η/3)H²b=0` with `H=1/τ` and solving the resulting characteristic equation; confirmed `ν∈(0,√3]` for `η∈(3/8,3/2]`.

All match the ledger exactly. **Re-executed** `research-notes/gravity_shear_maxwell_k4_pump_v15_678.py` (confirmed unchanged since commit `cde81c7`); reproduced all 6 cited Floquet growth-rate pairs exactly, including the exact equality of the x/y growth rates to the assertion tolerance.

**Scope assessment:** correctly distinguishes this prescribed homogeneous-shear toy from a real traveling GR gravitational wave, and correctly notes the existing K4 coasting solution decays and does not give a sustained lab-frequency pump. No overclaiming found.

## 4. v15.679 — propagating K4 tensor/EM phase matching and static-field seed

**Independent hand derivation** of the full Gate 202-205 chain:
- Confirmed `q² = [Ω²/v² - K²]/4` from the stated two-photon symmetric-pair kinematics, and its vacuum-GR (`q=0`) and dispersive-medium (`q²=K²(1-v²)/(4v²)`) limits.
- Confirmed the TT pair-vertex `V_pair = -εω²+K²/4 = -q²` is algebraically the same quantity, and that substituting the K4 timelike dispersion `Ω²=K²+m_T²` gives `q²=m_T²/4=(2η/3)H²` exactly.
- Independently recomputed the full suppression-factor table at `K/H∈{100,1000}` and `η∈{3/8,3/4,3/2}` from the closed form `q/K=√(2η/3)·H/K`, `|V_pair|/K²=(2η/3)(H/K)²`: all six values (`0.005`-`0.01`/`2.5e-5`-`1e-4` at `K/H=100`; `0.0005`-`0.001`/`2.5e-7`-`1e-6` at `K/H=1000`) match the ledger exactly.
- Confirmed the static-field seed linearization `(∂t²-∂z²)a_y = 2E0∂tb` by hand, expanding `∂t[e^{2b}∂tA_y]-∂z[e^{2b}∂zA_y]=0` with `A_y=-E0t+a_y` to first order in both `b` and `a_y`.

**Re-executed** `research-notes/propagating_k4_tensor_em_pair_and_seed_v15_679.py` (confirmed unchanged since commit `d0b31d4`); reproduced the full 6-row suppression table exactly, matching the independent hand computation above.

**Scope assessment:** correctly flags this as a conditional, WKB-regime-only kinematic opening, explicitly not a gain rate or detection claim, and correctly separates the static-field seed mechanism (ordinary inverse-Gertsenshtein physics) from the two-photon parametric channel. No overclaiming found.

## 5. v15.680 — finite EM cavity, static-field seed, and traveling-wave null

**Independent hand/numeric verification** of the Gate 206-210 chain:
- Confirmed the removable-singularity overlap value `J_1(1)=-i` and the limiting coefficients `A(0,2)=4` (spatially uniform pump, matching the homogeneous v15.678 result) and `A(2,2)=0` (lightlike traveling wave, same-mode cancellation) directly from `A(K,2)=4sin(πK)/(πK)`.
- Derived the small-`m_T²` expansion `A(K,2)≈-m_T²/2` by hand (setting `K=2-δ` with `δ≈m_T²/4` and Taylor-expanding `sin(π(2-δ))`), matching the entry's cited result, and from it the growth-rate estimate `σ≈h·m_T²/8` via the standard Mathieu 2:1-resonance rate `|hA|/4`.
- **Re-executed** `research-notes/finite_cavity_gravity_em_v15_680.py` directly; reproduced the 5-row `B_sig/B0` frequency-response table exactly (`1.987220087e-07` through `2.000000000e-06` through `1.986360930e-07`), and confirmed `PASS`.

**Scope assessment:** explicitly cites and distinguishes itself from real literature (Gao et al. 2024, Ahn et al. 2024, Gué et al. 2026), explicitly disclaims any detector-sensitivity or novel-force claim, and correctly identifies the static transverse B-field (not a bare static charge) as the valid linear seed mechanism. No overclaiming found.

## Honesty and scope assessment

This was an unusually large batch (five substantive entries across two tracks) landing within roughly one hour of wall-clock time. Every numerical and algebraic claim across all five entries was independently reconstructed by hand or by direct script re-execution, not merely re-read; none required correction. The gravity-track sequence (v15.676→v15.678→v15.679→v15.680) is a coherent, honest investigation of a user's physical intuition that systematically and correctly closes off a naive free-energy reading at every step while identifying the genuine (if currently unselected and heavily suppressed) conditional mechanisms. The Suzuki-track entry (v15.677) is a clean, direct continuation of the exact benchmark this audit's own Round 539 HANDOFF requested.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.681
type: external-audit-round
status: actionable
action: All five entries (v15.676 Lane A numbering, v15.677, v15.678, v15.679, v15.680) are independently confirmed as stated, with every cited numeric table reproduced exactly either by direct script re-execution or by independent hand derivation. No corrections needed. The gravity track's own next step (3D covariant cavity/coil geometry with independently controlled η and amplitude) and the Suzuki track's own next step (measure adaptive chart count/runtime at a stratified R5 sample before any R16 extrapolation) both remain open as the entries themselves state.
deliverable: Round 540 independent audit of v15.676 (Lane A numbering), v15.677, v15.678, v15.679, and v15.680.
