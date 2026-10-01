# Cone Derivation Ledger v13.915 — Sandbox Handoff: Odd-Sector Analytic Narrowing and Compression/Cone Bundle

Date: 2026-10-01. Track: our Lane B (sandbox exploratory), NOT the ledger's Lane B.
Status discipline: [D] derived, [N] numerical/provisional, [I] interpretation, [O] open.

## Purpose

This is a handoff entry, not a claim entry. It packages two sandbox work products
for two workers and points to the posted files under
`unified/discriminant-12-return/research-notes/`:

- **§1 — for the audit thread:** the analytic attack on the parked de Branges
  odd-sector question (v13.912 §5, route 1), run while Round 134 reproduced the
  §4 numerics. It answers the exact open question Round 134 left standing.
- **§2 — for the Lane A worker:** the binary-compression framework bundle for the
  prime-ordinates-on-the-cone program.

Nothing in this entry is new mathematics; every result below carries the status
tag it held in its sandbox report.

## 1. Odd-sector analytic narrowing (for the audit thread)

Full report: `research-notes/odd_sector_analytic.md` (sandbox only until this
entry; λ = −1 throughout, Suzuki v2 sign convention, no λ = 0 solves, §4's
numerical table not re-verified — that was the audit thread's job, now closed
by Round 134).

**The question reframed [D].** 0 ∈ σ(L_A^{(-)}) is trivially true: L_A^{(-)} is
Hilbert–Schmidt, hence compact, on infinite-dimensional L², and a compact
operator cannot be surjective. The substantive dichotomy was always (a) 0 is an
eigenvalue vs (b) L_A^{(-)} is injective with unbounded inverse — and Galerkin
divergence is consistent with *both*, so §4 alone could not decide it.

**New analytic infrastructure [D].** The odd sector on (−A,A) is exactly T₋ on
(0,A) with kernel k₋(x,y) = [g(x−y) − g(x+y)] + min(x,y), verified pointwise to
2.2e−16. Moreover min(x,y) is the Green's function of −d²/dx² with Dirichlet at
0, Neumann at A — so T₋ = G₋ + M with M's sine eigensystem fully explicit.

**No null mode [N].** Odd-projected Galerkin, A = 2, N = 400→3200: zero negative
eigenvalues; μ_min → 0 at ~m^{−1.74} (compact tail); decisively, the smallest
eigenvector's dominant Fourier mode tracks the mesh (78→168→358→646, ~0.4×
Nyquist at every N) — it becomes *more* oscillatory, never converging to a fixed
L² shape. This is the compact tail, not a resolving eigenfunction.

**The obstruction, precisely [N].** The Picard series Σ|⟨x,ψⱼ⟩|²/μⱼ² diverges
(4.5e+4 → 2.5e+8, still growing at the last mode): **x ∉ Ran(T₋)**. The formal
solution of T₋u = x is not an L² function. Round 133's analytic identity
(M_{1x} = 1) is therefore vacuous in the precise sense — its hypothesis ("u =
L_A^{-1}x exists in L²") fails. The r₁ half of the v13.757 gate is not merely
untestable with the current discretization; on the present evidence the moments
it needs **do not exist** as L² moments.

**Verdict: NARROWED.** 0 is in the spectrum (trivially) but is not an eigenvalue
[N]; the §4 divergence is Picard failure / unbounded inverse, not a null mode
and not a λ-resonance. The missing ingredient was never 0 ∈ σ_p but x ∈ Ran.

**What would close it [O], in dependency order:** (1) prove G₋ ≥ 0 analytically
(Krein screw-function territory — ĝ ≥ 0 via the explicit formula); this single
step promotes injectivity from [N] to [D]; (2) prove the Picard divergence with
two-sided eigenfunction bounds; (3) reformulate the v13.757 r₁ gate with the
pseudoinverse / range-projected sources. Routes that did not pay: naive
Birman–Schwinger (S = M^{−1/2}G₋M^{−1/2} is not bounded on L² — G₋ gains only
one derivative; the (G₋,M) generalized pencil is the right proxy) and the
deficiency vectors v_{A,±} (their equation already assumes R_A exists — no
independent leverage).

## 2. Compression/cone bundle (for the Lane A worker)

Index: `research-notes/compression_cone_handoff_README.md`. The bundle contains
`selector_theory_derivation.md` (the [D] Guinand–Weil frequency-selection
derivation — start here) and `selector_principle_exploration.md` (the
"positivity selects" heresy — a *different* selector selecting a *different*
object; do not conflate).

Recap of the chain being handed over: v13.882 (binary wave) → v13.883 (mod-24) →
v13.884 (twisted binary) → v13.885 (twisted explicit loop) → v13.887 (two
selection axes) → v13.888 (χ₃/χ₄/χ₅ universality) → v13.889 (β loop) → v13.890
(5/5 loops closed [N]: ζ 0.9995, χ₄ 0.9976, χ₃ 0.9959, χ₅ 0.9925, χ₁₂ 0.9840) →
v13.891 (selector principle derived [D]) → v13.892 (quantization map, not flag) →
v13.894 (Suzuki stability decisive negative — the spring-through-Suzuki
positivity bridge is closed).

The worker's program [O]: the compression detects ordinates as frequencies on
log scale (selector principle, [D], RH-agnostic); the cone's helices lift via
x + it. Why does the cone geometry realize the selector? Put the prime-side
ordinates onto the cone — nodes, helices, the 12-node/V₄ apparatus — and find
the geometric form of the selection. The ψ = log lcm identity (v13.895, Λ as
the jump function) is the natural arithmetic input.

## 3. Posted files

All under `unified/discriminant-12-return/research-notes/`, posted 2026-10-01
at the project owner's direction:

- `odd_sector_analytic.md` — §1's full report (filenames kept identical to
  sandbox provenance).
- `selector_theory_derivation.md`, `selector_principle_exploration.md`,
  `compression_cone_handoff_README.md` — §2's bundle.
- (Previously posted for Round 134: `r_gate.py`, `sweep_r.py`, `diag_r.py`,
  `fem_screw.py`, `r_ratios_sweep.json`, both plots, `r_gate_README.md`.)

## Scoping

Not an RH claim. §1 is a finite-dimensional Fredholm question narrowed, not a
statement about zeta zeros. §2 hands over derived and numerical results with
their tags intact; the cone program is [O]. The even half of the v13.757 gate,
the finite HB theorem (v13.673), and the Λ-rigidity arc are untouched.
