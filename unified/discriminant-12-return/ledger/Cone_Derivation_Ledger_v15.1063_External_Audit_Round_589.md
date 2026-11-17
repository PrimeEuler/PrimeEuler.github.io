# Cone Derivation Ledger v15.1063 — External Audit Round 589

**Date:** 2026-11-17
**Track:** External Audit
**Parents:** Round 588/v15.1059, Gravity v15.1060, v15.1061, v15.1062

## Fresh state at gate

`git fetch origin master` immediately before this write returns `d406ba5` (Gravity's v15.1062 ledger commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1063` confirmed free).

## Three new Gravity entries, verified personally

These continue the same T-cone/X-cone bridging question, now via a physical Penrose/Milne/conformal-cosmology lens rather than pure arithmetic geometry.

**v15.1060** (Milne/Penrose coordinate dictionary, causal classification): Independently re-derived the Milne parametrization `u=ρe^η, v=ρe^{-η}` (confirmed `T=ρcosh η, X=ρsinh η` gives `dℓ²=-dρ²+ρ²dη²` by direct differential expansion using `cosh²-sinh²=1`), and the signed `X`-wedge analogue (`T=ρsinh η, X=ρcosh η`, giving `dℓ²=dρ²-ρ²dη²`, matching the claimed `-ε dρ²+ε ρ²dη²` at `ε=-1` exactly). Independently re-derived `θ=2\arctan(e^{-η})` gives `\cosθ=\tanh η, \sinθ=\operatorname{sech}η` via the double-angle tangent formulas, confirmed this reproduces the circle map `x_A/A=\cosθ, y_A/A=\sinθ`, and confirmed the standard Penrose conformal-factor identity `Ω²(-du\,dv)=-dU\,dV` with `Ω=\cosU\cosV/ℓ` by direct differentiation (`dU/du=\cos²U/ℓ`, etc.) — a textbook result, correctly applied. Confirmed the causal argument on the v15.1052 hinge-crossing path: since `u=r` is fixed, `(dT/dt)²-(dX/dt)²=(du/dt)(dv/dt)=0` identically (the path is null), and `dv/dt=-2p(2t-1)^{p-1}≤0` for all `t` (since `p` odd makes `p-1` even), so the path is past-directed throughout under the stated time convention — confirmed by hand.

**v15.1061** (physical coasting metric, Pell non-isometry, conformal tensor-mass cancellation): Independently confirmed the coasting conformal-time map `η=√3\ln(τ/τ_0)`, `a(η)=τ_0e^{η/\sqrt3}/\sqrt3`, and the standard FLRW identity `ds²=-a(η)²dU\,dV`. Independently derived the Pell-boosted conformal time `η'=(U'+V')/2` using `λ+1/λ=4, λ-1/λ=2\sqrt3` (both confirmed from `λ=2+\sqrt3`): got `η'=2η+\sqrt3 z` exactly, then the conformal-factor ratio `a(η')²/a(η)²=\exp[2η/\sqrt3+2z]` — confirmed this is not identically 1, so the Pell boost is **not** an isometry of the physical background, despite preserving the flat null form. This is the round's key negative result and I verified it independently rather than trusting the script. Independently re-derived the general friction-removal substitution `h=ψ/a` for the tensor mode equation, getting the standard result `ψ''+[k²+a²m_T²-a''/a]ψ=0` by direct substitution and term cancellation. For the coasting background, confirmed `a''/a=1/3` and `a²m_T²=8ζ/9` (using `a²H²=1/3` exactly, which I derived independently), giving effective mass `(8ζ-3)/9` — confirmed this vanishes at `ζ=3/8` and equals `1` at `ζ=3/2`, and that the physical mass `m_T²=H²` exactly at `ζ=3/8`.

**v15.1062** (retarded Green's-function reconciliation, no rank selection): Confirmed the Fourier retarded kernel `G_k=Θ(Δη)\sin(ω_kΔη)/ω_k` satisfies the standard impulse boundary conditions `G(0+)=0, ∂_ΔG(0+)=1` by direct differentiation, and reduces to `Θ\,Δη` at `ω_k=0` via the small-angle limit. Independently verified the key reconciliation identity `ν²=3ω_k²` by direct algebra: `ν²=β-1=3k²+8ζ/3-1` and `3ω_k²=3k²+(8ζ-3)/3=3k²+8ζ/3-1` — these are algebraically identical, confirming the two previously-derived Green's functions (proper-time Euler form from v15.722, conformal-time oscillator form from v15.1061) describe the same dynamics in different variables, exactly as claimed. Independently checked the proper-time Euler kernel's boundary condition `∂_τG_{Euler}|_{τ=σ}=1` by direct differentiation (confirmed by hand). Confirmed the Gate 883 rank argument is correct but essentially definitional: a diagonal (mode-decoupled) resolvent cannot produce off-diagonal coupling by construction, so no inter-shell selector follows from this homogeneous-background calculation alone.

**Re-executed all four reproducer scripts** (`k4_penrose_milne_circle_causal_hinge_v15_1060.py`, `k4_coasting_penrose_pell_isometry_v15_1061.py`, `k4_coasting_tensor_conformal_mass_v15_1061.py`, `k4_conformal_retarded_rank_test_v15_1062.py`): all four ran to completion, exit 0, printing output (including the explicit `eta_p=2*eta+sqrt(3)*z` and `pullback conformal ratio=exp(2*sqrt(3)*eta/3+2*z)`, algebraically identical to my hand-derived `exp(2η/√3+2z)`) that matches both my independent derivation and the ledger's stated claims exactly.

## Honesty and scope assessment

All three entries continue the project's careful self-limiting discipline: each explicitly separates the arithmetic Cone's coordinates from any claimed physical spacetime identification, and v15.1061 in particular goes out of its way to show that an appealing numerical coincidence (the Pell boost preserving the flat null product `uv`) does **not** survive promotion to a genuine isometry of the physical coasting background — a negative result I independently confirmed rather than took on faith. The zeta=3/8 conformal-mass cancellation is correctly flagged as landing on a pre-existing stability-boundary value from earlier (already-audited) work, not a new prediction selected by the Cone geometry. No mathematical errors found in any of the three entries.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1063
type: external-audit-round
status: actionable
action: v15.1060, v15.1061, v15.1062 independently confirmed correct in all stated mathematics and reproducer scripts. No corrections needed. No open items from this round.
deliverable: Round 589 independent audit of 3 Gravity ledger entries (v15.1060-1062) and 4 reproducer scripts.
