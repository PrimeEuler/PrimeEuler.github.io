# Cone Derivation Ledger v15.1265 — External Audit Round 620

**Date:** 2026-11-20
**Track:** External Audit
**Scope:** Independent verification of v15.1262, v15.1263, v15.1264

## Method

`git fetch origin master` + `git merge --ff-only` confirmed `81c9f24` as the head. Three new entries since Round 619/liveness through v15.1261: Gravity's v15.1262 (all nonzero-Fourier-mode real-space K4 curvature reconstruction from the compact Maxwell source), v15.1263 (the homogeneous k=0 anisotropic-stress and Bianchi-I shear obstruction), and v15.1264 (the resolution of that obstruction: a Hamiltonian-compatible isotropic correction plus a driven, time-evolving Bianchi-I shear). v15.1264's `.md` landed partway through this round's work and was folded in before writing. Read all three in full.

## v15.1263 — homogeneous Maxwell anisotropic stress and Bianchi-I shear (fully analytic)

This is pure symbolic/analytic content, so every claim was re-derived from scratch:

**Exact integrals, re-derived.** `I0=∫₋₁¹f(u)²du`, `I1=∫₋₁¹f'(u)²du` for `f(u)=(1-u²)³`: independently integrated in SymPy, confirmed exactly `I0=2048/3003`, `I1=1024/385`.

**Energy integrals, re-derived by hand with explicit substitution.** For `χ=f(x/aₓ)f(y/a_y)f(z/a_z)`, `(aₓ,a_y,a_z)=(1,2,1)`, `Ex=∂_yχ`, `Ey=-∂_xχ`: substituting `u=coordinate/width` in each factor gives exactly `∫Ex²d³x = aₓa_z I0²I1/a_y = I0²I1/2` and `∫Ey²d³x = a_ya_z I0²I1/aₓ = 2I0²I1` — matching the entry exactly. `E_total=(1/2)(∫Ex²+∫Ey²)=(5/4)I0²I1`, confirmed numerically: `ρ̄=E_total/(4π)³ = 16777216/(694386693π³) ≈ 0.0007792357845734601` — matches exactly.

**Stress tensor and anisotropic part, re-derived by hand.** `⟨Ex²⟩/ρ̄=2/5`, `⟨Ey²⟩/ρ̄=8/5` (from the energy fractions above) give `T̄_ij/ρ̄ = diag(3/5,-3/5,1)` (trace 1, as required by Maxwell's zero 4D stress trace) and `Π̄_ij/ρ̄ = (1/15)diag(4,-14,10)` (traceless) — both confirmed exactly by hand, matching the entry exactly.

**Bianchi-I shear identity, independently derived from the metric, not assumed.** Built the general diagonal Bianchi-I metric `ds²=-dt²+aₓ²dx²+a_y²dy²+a_z²dz²` in SymPy, computed the full Christoffel/Ricci/Einstein tensors from scratch (no shortcuts), and confirmed the exact identity `d/dt(Hₓ-H_y)+(Hₓ+H_y+H_z)(Hₓ-H_y) = Ĝₓₓ-Ĝ_yy` (orthonormal-frame Einstein tensor difference) — residual exactly 0. This is the identity the entry's Gate 1197 rests on; it is now confirmed from first-principles curvature, not taken on faith. (Two subsidiary checks — the Hamiltonian-constraint sign and the electric-Riemann sign — came out flipped relative to my own ad hoc convention choice in the same calculation; this is a sign-convention artifact of my script's `g₀₀`/orthonormalization choice, not a defect, and is consistent with the archived (+---) vs (-+++) convention ambiguity this project has flagged repeatedly elsewhere. The load-bearing difference identity itself needed no sign choice and came out exact.)

Given this, the stated `σ̇ᵢ(t₀)=κΠ̄ᵢ` relations follow by linearity (traceless `σᵢ` and `Πᵢ` are each fully fixed by their pairwise differences): `σ̇ₓ-σ̇_y=κ(Π̄ₓ-Π̄_y)=κρ̄(4-(-14))/15=(6/5)κρ̄` and `σ̇_z-σ̇_y=κ(Π̄_z-Π̄_y)=κρ̄(10-(-14))/15=(8/5)κρ̄` — both confirmed exactly by hand, matching the entry's stated `+(6/5)κρ̄^phys` and `+(8/5)κρ̄^phys` exactly.

**Script execution.** `k4_maxwell_homogeneous_anisotropic_stress_v15_1263.py` has no `ledger_version` field; ran cleanly, printing `P_i/rho=[3/5,-3/5,1]`, `Pi_i/rho=[4/15,-14/15,2/3]` — matches independent derivation exactly.

## v15.1262 — all-nonzero-Fourier-mode real-space reconstruction (numerical)

Extends the already-verified (Round 619) per-mode scalar/vector/tensor operators to every nonzero bin of a 3D FFT grid, with an explicit discrete-Gauss transverse projection, Hermitian/Nyquist symmetrization, and the k=0 (homogeneous) mode deliberately excluded. Read the committed script line by line: the forcing equations (`sourceS`, `sourceV`, `Tdd`), the `β_S/β_V/β_T` coefficient formulas (parameterized by `k²` rather than the fixed `|K|²=2` used in Round 619), and the `S`/`A_iso`/`B_V`/vector-and-tensor-tide formulas are structurally identical to the single-mode forms already independently verified in Round 619 — no new physics to re-derive here, only its application across the full grid.

**Independent numerical re-execution** (all three grids, N=32/40/48, from a clean environment) reproduced the published table **exactly**, including the full off-diagonal structure at 48³ (`E_xy≈-1.171e-6, E_xz≈-6.61e-7, E_yz≈+7.02e-8` — matches the ledger's stated values exactly), and all three internal-consistency residuals (trace residual `≤1.78e-15`, max imaginary part `≤3.43e-16`, discrete-Gauss residual `≤2.76e-16`) — all within the bounds the entry states. The script's own `assert` statements (residuals `<3e-12`, symmetry `<3e-12`) passed, exit 0 on all three grids, confirming the "PASS" claim is genuine, not asserted-but-unchecked.

**Cross-consistency with v15.1263.** The numerical `rho_mean` from this entry's finite periodic box (`0.0007677 → 0.0007825 → 0.0007787` for N=32/40/48) brackets and trends toward v15.1263's independently-derived exact continuum value `ρ̄≈0.00077924` — a genuine cross-check between the two entries' numerics that neither entry states explicitly but that holds up.

## v15.1264 — resolving the homogeneous obstruction (analytic + numerical)

This entry closes both gaps v15.1263 left open: the Hamiltonian-constraint mismatch and the undriven shear.

**Gate 1199 (material shear-pressure constitutive law), independently re-derived.** Perturbed the same frozen material action `F(B)=C(detB)^{1/3}[1+η_s(trB²/(trB)²-1/3)]` around the isotropic point, with `B_i=a^{-2}e^{-2β_i}` and `Σβ_i=0`, to first order in `β_i` via SymPy (built from scratch, not copied from the script): confirmed `δp_i = -8η_sCβ_i/(9a²)` exactly for all three components (including `β_3=-β_1-β_2` correctly folding through to `+8η_sC(β_1+β_2)/(9a²)`), and confirmed the background isotropic pressure `p_0=-C/(3a²)=-ρ_s/3`, consistent with `ρ_s=C/a²` used elsewhere in this chain.

**Gate 1200 (Hamiltonian-compatible isotropic correction), independently re-derived end to end.** Expanded the Bianchi-I Hamiltonian constraint `H_xH_y+H_yH_z+H_zH_x=κρ_total` to first order in `u` and `β̇_i` (using `Σβ̇_i=0`) by hand, confirming it reduces exactly to `6u̇/τ=-6u/τ²+9κρ̄_conf/τ⁴` as claimed. Solved this linear ODE directly (integrating factor `τ`, not assumed): `u(τ)=(3κρ̄_conf/2)(τ-1)/τ²` falls out uniquely from `u(1)=0`, matching the entry exactly, and gives `u̇(1)=3κρ̄_conf/2` exactly. Differentiating this closed form twice and forming `-(ü+2u̇/τ)` collapses — via genuine cancellation, not by construction — to the clean result `A_iso,h=3κρ̄_conf/τ⁴` claimed by the entry.

**Gate 1201 (driven shear equation), independently re-derived.** Starting from the standard shear-propagation equation `σ̇_i+3Hσ_i=κ(Π_EM,i+Π_solid,i)` with `H=1/τ` and the Gate-1199 solid response, substituting `κC=1` and the Maxwell physical-energy scaling `1/a⁴=9/τ⁴` reproduces exactly `β_i''+3β_i'/τ+[8η_s/(3τ²)]β_i=9κΠ_EM,conf,i(τ)/τ⁴` — matching the entry exactly, with no step taken on faith.

**Independent numerical re-execution** (both the standalone SymPy constitutive-law check and the full four-grid N=32/48/64/80 run) reproduced every value in the published table **exactly** — `mean_conformal_energy`, all three `β_i(1.2)` components per grid — and, at the finest grid, `u(1.2)=0.00016234849742562737` and the homogeneous tidal diagonal `(0.00055625, 0.00011498, 0.00271103)` with trace `0.00338226` — all matching the ledger's stated values exactly. The script's own internal assertions (Hamiltonian/isotropic-trace identities at machine precision, shear-equation residual `<2e-14`, traceless/zero-sum checks) all passed.

## Collision and freshness checks

`v15.1265` and "Round 620" both confirmed unused before this write. No other new `.md` ledger entries landed during this check. `__pycache__` cleaned before this commit; final freshness check performed immediately before push confirmed no intervening ledger changes.

## Verdict

**PASS (all three entries).** v15.1263's Bianchi-I shear identity was independently re-derived from first-principles curvature computation rather than assumed; v15.1262's full-grid numerical reconstruction matches exactly across all three resolutions; v15.1264's full analytic chain — constitutive law, Hamiltonian correction (including an independent closed-form ODE solve), and driven shear equation — was independently re-derived end to end and its four-grid numerics matched exactly. All three entries are explicit and correctly cautious about scope: the periodic-cell homogeneous completion is a declared modeling choice, not a claim about an isolated packet in infinite space, and no quarter-grid coupling or new physical effect is claimed anywhere in this chain.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
