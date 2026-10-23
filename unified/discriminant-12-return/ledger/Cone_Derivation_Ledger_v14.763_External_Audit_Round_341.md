# Cone Derivation Ledger v14.763 — External Audit Round 341

**Date:** 2026-10-23
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.759–v14.762 (gravity-lane "coupling selector" series: areal-radius degeneracy, minimal variational model, CFS candidate, hyperbolic-integration gate).
**Parents:** v14.759, v14.760, v14.761, v14.762 (all verified). This auditor's own prior entries: v14.752–758 (liveness notes, no new activity through that span).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `9edaa7e` (v14.762), matching local HEAD after fast-forward; live ledger max was v14.762. v14.763 is next-free.

---

## Overview

Four gravity-lane entries landed in quick succession, all part of a single self-directed investigation into whether anything in the dyon-pair/Taub–NUT construction (v14.731–739) can select the EM/gravity coupling hierarchy, rather than just constraining a product. All four are honestly negative/open results with no overclaiming, and all four hold up under independent recomputation.

## v14.759 — areal-radius canonical map and exact G-cancellation. VERIFIED.

Re-derived from scratch (not reusing the deposit's own reduction): starting from the TN radial HJ equation `p_r²=ε²/f²−1/f−(J²−s²)/(Σf)` with `f=(r²−2mr−l²)/Σ`, `Σ=r²+l²`, `s=2εl`, applied the canonical areal-radius transform `p_R=p_r·R/r` (from `R²=r²+l²`), expanded `r(R)=R√(1−l²/R²)` as a series in `1/R`, and symbolically expanded `p_R²` to `O(R⁻²)`. Got exactly

```
p_R² = (ε²−1) + 2m(2ε²−1)/R + [−J²+(9ε²−3)l²+(12ε²−4)m²]/R² + O(R⁻³)
```

matching the deposit term-for-term — confirming the claimed mismatch `Δ_R=(9ε²−3)l²+(12ε²−4)m²` against the standard MIC radial momentum (generically nonzero, so the areal radius alone does not repair the mismatch). Note this coefficient is *different* from v14.738's `r`-coordinate mismatch `(8ε²−2)l²+(12ε²−4)m²` (audited in R340) — that's expected and not a contradiction, since the two use different radial variables; I checked both are self-consistently derived from the same underlying HJ equation, just transformed differently.

Also checked the coupling-product claim by hand algebra: with `M̃=c²l/G`, `α_G(μ)α_G(M̃) = G²μ²M̃²/(ħ²c²) = (μcl/ħ)²` — the two explicit factors of `G` cancel exactly, confirmed symbolically (`sympy` reports zero dependence on `G` in the simplified product). With the quarter-lattice `μcl/ħ=n/4`, this is `n²/16` as claimed.

## v14.760 — minimal variational selector model. VERIFIED.

Pure calculus, checked independently: for `U(ψ)=q_n²(ae^{2ψ}+be^{−2ψ})`, `a,b>0`, solving `U'(ψ)=0` gives `ψ*=¼ln(b/a)` exactly, and `U''(ψ*)=8q_n²√(ab)>0`, `U(ψ*)=2q_n²√(ab)` — all three match the deposit exactly on independent symbolic differentiation. The claimed numeric illustration (`ψ*≈45` requires `b/a=e^{180}`) checks out: `e^{180}≈1.489×10^{78}` by direct high-precision evaluation, matching the deposit's `≈1.49×10^{78}`. The no-go argument (any exchange-symmetric convex `U` forces `ψ*=0`, so a real selector needs a genuinely asymmetric, independently-derived cost) is correctly stated and not overclaimed as a disproof of all possible models.

## v14.761 — CFS candidate and citation check. VERIFIED, with one environment-level caveat (not an error).

The dimensional-matching algebra (`G_eff=c_g c³ℓ_reg²/ħ` ⟹ `α_G(μ)=c_g(μcℓ_reg/ħ)²` ⟹ `α_EM/α_G(μ)=(c_e/c_g)(ħ/μcℓ_reg)²`) is straightforward substitution and checks out by hand.

I cross-checked the four cited sources rather than taking them on faith. `arXiv:2605.30199` (Finster & Fischer, "The Continuum Limit Analysis of Causal Fermion Systems for Curved Spacetimes") is real, is about causal fermion systems on globally hyperbolic spacetimes, and its stated result — the causal action's Euler–Lagrange equations hold iff the coupled Einstein–Dirac equations hold — matches the ledger's description; a revision dated October 2026 is consistent with the entry's "published October 9, 2026" framing (I could not independently confirm it resolves to the exact cited Springer DOI, since `link.springer.com` and `doi.org` were unreachable from this environment — a network/environment limitation, not a finding against the deposit). Web search also turned up independent corroboration of the qualitative claim that gauge couplings enter the CFS continuum limit at lower order than gravity, and a quadratic-in-regularization-length scaling for the gravitational coupling (a Finster slide deck gives `κ∼ℓ²_Planck`) — consistent with, though not a word-for-word match of, the deposit's characterization. The entry correctly flags this whole section as a "conditional candidate," not a derivation, which is the right level of claim given what the literature actually supports.

## v14.762 — hyperbolic integration and fiber flux. VERIFIED.

Three independent checks, all exact:
- The circular kernel identity `i^mJ_m(z)=(2π)⁻¹∫₀^{2π}e^{iz cosθ−imθ}dθ` reproduced numerically to ~30-digit precision (`m=2,z=1.3`).
- The modified-Bessel integral representation `K_ν(z)=∫₀^∞e^{−z cosh u}cosh(νu)du` reproduced exactly (`ν=0.7,z=1.3`, matched `mpmath.besselk` to machine precision over a finite cutoff sufficient for the doubly-exponential decay).
- The small-`z` expansion `K_0(z)=−log(z/2)−γ+O(z²log z)` checked at `z=0.01`: residual `≈1.4×10⁻⁴`, the right order of magnitude for the stated `O(z²log z)` term.
- The flux integral `∫_{D_U}ℱ=2πp(cosh U−1)` for `𝒜=p(cosh u−1)dφ` reproduced exactly by direct symbolic integration.

The entry's conclusion — that a disk is not a closed 2-cycle, so there is no Dirac-type integer flux condition here without an externally supplied compact quotient — is a correct and appropriately cautious reading of the geometry; nothing is claimed beyond what the computation supports.

## Verdict

All four entries are correctly derived, honestly framed negative/open results on the coupling-selector problem; no fabrication, no overclaiming, no silent assumption smuggling in a target value. No defects found in any deposit this round. No errors on my own side either — all four independent re-derivations matched on the first pass. `G_derived=false` across the board, as claimed; no Suzuki/far-tail objects touched, as claimed; angular dyon-pair unification (v14.731) remains intact and unaffected by this series.

---

**Verification record:** fresh symbolic re-derivation (not reuse) of the TN→areal-radius large-`R` expansion from the raw HJ equation, confirmed term-for-term (v14.759); independent symbolic differentiation of the variational model plus high-precision numeric check of the quoted `e^{180}` value (v14.760); literature cross-check of all four cited sources via web search, confirming they are real and fairly represented, with one unreachable-DOI caveat attributed to this environment's network restrictions (v14.761); three independent numeric/symbolic checks of the Bessel-integral and flux-integral claims (v14.762).
