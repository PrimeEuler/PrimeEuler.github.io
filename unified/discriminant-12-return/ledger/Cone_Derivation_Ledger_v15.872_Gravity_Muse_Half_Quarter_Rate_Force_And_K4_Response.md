# Cone Derivation Ledger v15.872 — Gravity / Muse: EM half-turn rate crowns, quarter-turn minima, rescaled gravity transition lattice, and actual K4 tensor phase response

**Date:** 2026-11-13 (US Eastern). **Parents:** Muse/Sandbox v15.864 tangency chain, v15.866 gravity tangency circle and h-similar EM/G construction, v15.867 exact node lattice, v15.869 acceleration transition parabola and Airy turning point, earlier lever v15.857–860; Gravity v15.862–865 force/stress and sourced tensor optical comparator; External Audit Round 566/v15.868 with two previously missed v15.864/865 reproducibility defects. **Immediately prewrite live HEAD:** 4172f17a7320f13cd151085b8058c660ece43053. Target path checked absent, strict additive-only, no mutation of Muse/Sandbox, Suzuki, earlier certified ledger/code.

**Categories:** [D] exact half/quarter extremum statements for a specified sine function and sector-dependent phase coordinate, and exact restoring-force/power offsets; [D] exact sourced coasting K4 tensor scalar-mode retarded Green transfer from a *prescribed* phase-tagged source; [N] no new coupling, EM→G source mechanism, sector period selector or new experimental gravity prediction; [O] independent physical derivation that fixes EM and gravitational phase/time relation and supplies complete conserved EM/matter stress to the K4 Einstein–solid system.

## Gate 493 — what the new Muse discussion actually established

Sandbox v15.866 independently constructed **per-sector** transition steps h_EM=1, h_G=1/2, and transition offsets q=h/2, hence q_EM=1/2 and q_G=1/4. It also distinguished EM spectral offset²=1/4 from **gravity** offset²=1/16, and did **not** claim gravity shares the EM 1/4 Casimir. Sandbox v15.867 identified sine sign-changing nodes at every half-turn and cosine nodes at odd quarters; v15.869 showed the fastest *sine displacement rate* crowns at sine nodes, while the corresponding cosine velocity waveform has local osculating quadratic curvature there. The turning-point Airy/WKB matching is an ordinary local transition asymptotic, not an independently determined coupling.

This provides a precise reading of the user's question: on a **fixed EM sine wave** with h_EM=1, x=1/2 is a node with *maximal absolute first derivative*, and x=1/4 is an antinode with *zero absolute first derivative*. But when x refers to the *same numeric coordinate used in two sector-relative phase dictionaries*, x=1/4 means something different in the G sector.

## Gate 494 — exact dual interpretation of the same quarter coordinate

Define a periodic waveform with sector phase step h:

**f_h(x)=A sin(2πx/h)**, **r_h(x)=(h/(2πA)) df_h/dx=cos(2πx/h)**.

Then the *normalized* signed rate is r_h, whose absolute magnitude is 1 at nodes x=nh/2 and 0 at antinodes x=(2n+1)h/4. The second derivative, normalized by A(2π/h)², is −sin(2πx/h).

| sector and coordinate x | normalized sine rate r_h | normalized second derivative | interpretation |
| --- | ---: | ---: | --- |
| EM h=1, x=1/2 | −1 | 0 | maximal EM change rate (sine node) |
| EM h=1, x=1/4 | 0 | −1 | minimal EM change rate (sine antinode) |
| gravity phase dictionary h=1/2, x=1/4 | −1 | 0 | maximal **sector-rescaled** rate (G-phase node) |
| gravity phase dictionary h=1/2, x=1/8 | 0 | −1 | minimal **sector-rescaled** rate (G-phase antinode) |

The **same coordinate value x=1/4** can therefore be an EM sine *rate minimum* and a G-dictionary sine *rate maximum*. This is not a physical contradiction, and is not an interaction: the two phase functions are f_1(x)=A sin(2πx) versus f_(1/2)(x)=A sin(4πx). Their differing periods were *defined* from h, not measured or derived as physical oscillator frequencies. If x is physical time, the rates differ by a factor 2 at matched normalized phase because 2π/h differs; if x is a dimensionless mesh coordinate, actual frequency and phase-locking require a separate physical map x=x(t). The cosine quadrature reverses node-versus-antinode rate extrema, so specifying which waveform's *derivative* is essential.

**Reproducer:** research-notes/k4_half_quarter_transition_rate_dual_phase_v15_871.py, additive commit **8be4203420bf4a77d7a01dd49e82cfb453358240**. Equivalent standalone local SymPy script executed PASS, including full phase/rate/curvature identities.

## Gate 495 — highest displacement rate is NOT highest force or highest power

For a conventional oscillator x(t)=A sin(ωt), its displacement rate is **v=Aω cos(ωt)**, its acceleration and restoring force are **a=−Aω² sin(ωt)** and **F=−mAω² sin(ωt)**, and its instantaneous mechanical work rate is

**P=Fv=−(mA²ω³/2) sin(2ωt)**.

Consequently:

- At sine nodes (the half-turn sign transitions) |v| is maximal, but **F=0 and P=0**.
- At sine antinodes (odd quarters) **v=0**, but |F| is maximal, and **P=0**.
- Between nodes and antinodes (eighth-turn offsets), the magnitude |P| attains its maximum.

This is ordinary harmonic response. The user's “minimum EM rate of change at 1/4” is exact for the chosen **sine displacement** (or whichever physical field is mapped to it), but **does not mean minimum force, minimum acceleration, minimum field strength, minimum curvature, or minimum power**. One must identify the physical EM observable (charge displacement, electric field, current, energy, etc.) and its clock before carrying the phase statement into a new EM/G force prediction.

## Gate 496 — actual coasting K4 tensor Green response to quarter-cycle displaced driving

Take the original source-driven coasting K4 tensor Euler equation, for each mode:

**γ''(τ)+(3/τ)γ'(τ)+(β_T/τ²)γ(τ)=−2 Π_TT(τ)**,

with **β_T=3K²+8η_s/3**. Set s=lnτ and γ(τ)=τ^(-1)u(s). The exact transformed equation is

**u_ss+ν²u=−2 τ³Π_TT**, **ν²=β_T−1**.

To *test solely the linear transition-phase transfer* prescribe a source history **Π_TT(τ)=τ^(-3) sin(Ωs+φ)**, with homogeneous propagating data u(0)=u_s(0)=0. This source is a **phenomenological prescribed forcing**, not a conserved positive-energy EM or canonical matter source and not a Cone-derived EM→gravity coupling.

At nonresonant ν²≠Ω² the exact retarded initial-value solution is

**u(s;φ) = −2/(ν²−Ω²) { cosφ[sin(Ωs)−(Ω/ν)sin(νs)] + sinφ[cos(Ωs)−cos(νs)] }**.

The sine-phase and cosine-phase source responses are two quadratures of the same retarded Green function. Their initial-value *transient samples* differ, but the magnitude of the periodic particular-solution gain is **2/|ν²−Ω²|** for either phase. No independent enhancement of physical coupling follows from using an EM half-turn or quarter-turn label. At **solid η_s=3/4, K²=4**, β_T=14 and ν²=13; with Ω=2 the gain is **2/9**. At s=1 the zero-data responses are **u_sine≈−0.2572269310** versus **u_cosine≈−0.1062536049**, reflecting initial-source phase and causal transient, not a new amplitude scale. At resonance, the familiar secular growth must be treated separately; no resonance is selected by mesh offsets alone.

**Reproducer:** research-notes/k4_tensor_phase_rate_response_v15_872.py, additive commit **4172f17a7320f13cd151085b8058c660ece43053**. Exact local SymPy algebra checks the forcing equation, zero initial data, linear phase superposition and the stated gain; numerical specializations reproduced locally. The committed script awaits independent execution audit.

## Gate 497 — separate prior code repair from new physics

External Audit Round 566/v15.868 independently verified Muse/Sandbox v15.864/866/867 and Gravity v15.862/863. It found two original gravity v15.864/865 issues: first, an already disclosed bare SymPy matrix-equivalence assertion; second, a previously undisclosed use of **v=s.Function('v')(tau)** followed by **v(tau)** that makes the v15.865 wrapper crash with TypeError, plus a ledger claim that a “Minkowski L=5 oscillator benchmark” existed in the committed program when it did not. The auditor's independent scratch copy with the two code repairs reproduced the physical numerical coasting results; the original and v15.865 committed programs were not fully executable as-is.

New additive **research-notes/k4_force_agent_v15_870_full_audit_repair.py**, commit **c1bcef03c7ba5faf6b61507b206988b1b5624738**, makes both changes **in memory against the unchanged v15.864 original source** and executes its actual source tests; it does **not** claim to implement a Minkowski L=5 oscillator benchmark. This entry explicitly withdraws that unsupported v15.865 ledger-prose claim. The underlying full coasting matter-source/tensor/optical results were independently confirmed by Round 566 using the exact two fixes in a scratch copy. The new additive v15.870 wrapper itself awaits external audit. No edits to Sandbox-owned v15.857 NumPy portability issue.

## Gate 498 — next genuine EM/G selector test

The EM maximum-rate half-turn and minimum-rate quarter-turn are exact within a sine-phase definition, while the G mesh rescales a transition-offset coordinate, and the ordinary K4 tensor transfer responds to phase-tagged forcing according to a conventional Green function. At this point no independent law fixes (i) which EM observable is sinusoidal, (ii) the physical clock mapping x(t) for EM and gravity, (iii) the EM-to-K4 conserved stress coupling, or (iv) why gravity should pump the EM oscillator preferentially at the quarter coordinate rather than the half coordinate. The mesh q_G=1/4 is also not the electromagnetic Casimir correction, as explicitly distinguished in Sandbox v15.866.

A defensible next experiment is to supply one **explicit conserved electromagnetic or charge-current source and a time-dependent physically justified coupling mechanism** (rather than using mesh offsets as a drive by declaration), identify the phase of *charge displacement, current, electric field and instantaneous power separately*, then compare the induced K4 scalar/vector/tensor full optical output with matched GR+ordinary elasticity and EM. Any nonzero Cone-only residual must survive a physically derived coupling and gauge-controlled subtraction.

**HANDOFF — external audit/Muse:** reexecute v15.870 corrected old force-agent script, v15.871 phase/rate/force SymPy checks and v15.872 K4 forced-mode exact Green identity; confirm phase labels, sector-local mesh normalization, amplitude-vs-first-derivative-vs-force/power maxima, and that **no new force or frequency was selected**. Preserve all historical records, honor the distinct EM 1/4 Casimir correction and gravity 1/16 offset², avoid treating the nonlocal TT sector as a remote causal signal.
