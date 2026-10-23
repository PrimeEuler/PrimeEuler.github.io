# Cone Derivation Ledger v14.785 — External Audit Round 343

**Date:** 2026-10-23
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.770–v14.784 (large gravity-lane batch: radial-shift no-go chain, loop/holonomy gates, Dirichlet-to-Neumann boundary-response series, intrinsic Cone-metric signature check) plus the v14.768 LaTeX repair.
**Parents:** v14.770–v14.784 (all verified). This auditor's own prior entry: v14.769 (R342).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `de45c5d` (v14.784), matching local HEAD after fast-forward; live ledger max was v14.784. v14.785 is next-free. Every version number 770–784 appears exactly once in the ledger directory — no collisions.

---

## LaTeX repair (v14.768)

The two commits fixing v14.768's stripped-backslash formatting (flagged in R342) touch the ledger entry and its research note exactly once each — not a duplicate. Re-read both: content is unchanged from what I already verified in R342, now rendering correctly.

## v14.770–772 — radial-shift spectral no-go, anchored-wall covariance, local boundary response. VERIFIED.

All three are consequences of the single fact `r_G(n)=r_EM(n)-log4`, propagated through different observables. Checked by hand/symbolically: `H_G=H_EM-(log4)I` under a shared interaction `K`; `tr(e^{-tH_G})=4^t·tr(e^{-tH_EM})` (direct from `e^{-tH_G}=e^{-tH_EM}·e^{t log4}`); the homogeneous-functional ratio `4^{-p}`. For the divisor-count series: confirmed the exact asymptotic expansion `N_G(L)-N_EM(L)=t[3log t+4log4+3(2γ-1)]+O(√t)` by direct symbolic expansion of `D(4t)-D(t)` using the classical hyperbola-method asymptotic; confirmed the **exact** wall-cancellation identity `N_{1/2}(L-log4)=N_1(L)` numerically with the real divisor-summatory function at `L=2,3.5,5` (all matched exactly, e.g. `16=16`, `123=123`, `766=766`); confirmed the ratio trending toward 4 numerically as `L` grows (`5.06→4.68→4.55→4.42` at `L=5,8,10,13`, consistent with the slow `O(1/log t)` convergence implied by the stated error term). The Mellin identity `Z_G(s)=4^s Z_EM(s)` and the local-response covariance `𝓡_{1/2}(L,ε)=𝓡_1(L+log4,ε)` both follow by direct substitution, confirmed by hand. All three entries correctly and repeatedly flag that none of this is a coupling ratio, only a coordinate-translation identity — appropriately cautious.

## v14.773 — invariant areal wall, embedding non-identifiability. VERIFIED.

The `ℓ_G=2ℓ_EM ⟹ a_G=a_EM` cancellation is immediate substitution, confirmed. The entry correctly flags that using a G-dependent Planck length as the "independent" reference length would be circular — appropriate guardrail, not a math claim to check further.

## v14.774–777 — unit-circle/holonomy gates. VERIFIED.

Checked symbolically: `|z_{n,k}|=1` and `z_{λn,λk}=z_{n,k}` for `z_{n,k}=(n-k+2i√(nk))/(n+k)`, confirmed exactly; the two algebraic forms of `z_{n,k}` agree exactly; `(j+½)²=j(j+1)+¼` confirmed exactly. The physics statements (`pR=mħ` from single-valuedness, `pR+qΦ/2π=mħ` with flux, twisted-boundary eigenvalues `J_m=ħ(m+α)`) are standard textbook quantization results, correctly applied, and each entry explicitly and correctly declines to over-identify the "quarter vertex" (a grid coordinate) with a "quarter holonomy" (a phase) — a distinction worth having drawn explicitly, since conflating the two would have been an easy mistake.

## v14.778–780 — symplectic/susceptibility/bulk-integration no-gos. VERIFIED.

`Ω=√(ab)` from `H=½(ap²+bq²)` is immediate from Hamilton's equations. The pinned-interval variational problem: confirmed `κθ'(L)=j cosθ(L)` as the natural boundary condition, confirmed `χ=L/κ` by implicit differentiation of `(κ/L)Θ=j cosΘ` at `j=0`, and confirmed `d²E_min/dj²|_0=-L/κ` via the envelope relation `dE_min/dj=-sinΘ`. The closed-ring winding energy `E_m=2π²κm²/L` checked directly from `∫(θ')²ds` with `θ(s)=2πms/L`. The flat-annulus Dirichlet problem: confirmed the harmonic solution `θ(r)=Θ log(r/a)/log(b/a)` solves the radial Laplace equation, and confirmed the on-shell energy `E=πKΘ²/log(b/a)` by direct integration — all exact matches.

## v14.781–783 — hyperbolic-annulus Dirichlet-to-Neumann series. VERIFIED, with one fresh independent derivation.

This is the most technically involved sub-series, so I re-derived it independently rather than just checking the stated formulas. Confirmed symbolically that `dt/dρ=1/(ℓ sinh(ρ/ℓ))` for `t=log tanh(ρ/2ℓ)` exactly. Using this, I solved the radial Laplace equation from scratch (not reusing the deposit's reduction) and confirmed the metric is exactly conformal to a flat cylinder in `(t,φ)`, that the radial harmonic solution is linear in `t`, and that the resulting on-shell energy is `E=πKΘ²/Δ` — matching v14.781 exactly. For the Fourier modes (v14.782), I independently solved the mode-`m` ODE with the stated boundary data and got the Dirichlet-to-Neumann eigenvalue `λ_m=|m|coth(|m|Δ)` exactly, confirmed symbolically, including the small-`Δ` expansion `λ_m~1/Δ+m²Δ/3` (also confirmed via direct series expansion) and the correct `m→0` limit matching the Gate-A zero mode. The scale-invariance claim in v14.783 (`Δ` depends only on `ρ_i/ℓ, ρ_o/ℓ`, hence invariant under common dilation) is immediate from the formula for `Δ`. All of this is correctly and repeatedly caveated as a model geometry, not yet shown to be the Cone's actual metric — which turns out to matter, per the next entry.

## v14.784 — intrinsic Cone metric is Lorentzian, not elliptic. VERIFIED; this is a genuine and valuable self-correction.

I independently re-derived every pullback in this entry from scratch via `sympy`. With `x=Ye^β, y=Ye^{-β}`: the natural bilinear form `dx·dy` pulls back to exactly `dY²-Y²dβ²` (Lorentzian signature, confirmed symbolically to zero residual) — i.e., `e^r(dr²/4-dβ²)` after the `r=2logY` substitution. By contrast the Euclidean quadrant form `dx²+dy²` pulls back to the claimed `e^r[(cosh2β/2)dr²+2sinh2β dr dβ+2cosh2β dβ²]` (confirmed exactly, once a spurious unsimplified-trig residual was checked numerically and found to vanish), and the separately-chosen positive polar form `g_+=dY²+Y²dβ²` pulls back to `e^r(dr²/4+dβ²)` (confirmed exactly) — conformal to a flat strip, giving the stiffness `k_+=KB/(u_o-u_i)=2KB/(r_o-r_i)` by the same interval-stiffness logic as v14.780, confirmed by direct re-derivation.

This entry is important: it shows that the entire v14.780–783 elliptic Dirichlet-to-Neumann series was built on an *auxiliary chosen* positive-definite metric, not the Cone's own intrinsic quadratic form `dx dy`, which is actually Lorentzian. The gravity lane caught this itself and flagged it plainly rather than quietly continuing to build on an unexamined assumption — exactly the kind of self-check this process should reward. No physical conclusion from v14.780–783 is retracted (none of them claimed to have derived `G` or the hierarchy), but their domain of applicability to the "real" Cone is now correctly marked as conditional on a metric choice that has not been physically justified.

## Verdict

Fifteen entries this round (v14.770–784), the largest single batch so far. Every checkable algebraic, asymptotic, and differential-geometric claim verified exactly, several via fresh independent derivation rather than reuse of the deposit's own reduction (notably the hyperbolic-annulus DtN eigenvalues and the full Cone metric-pullback computation). No mathematical defects found. No G, α, or coupling hierarchy is claimed derived anywhere in this batch — every single entry says so explicitly, and the chain's own internal logic (culminating in v14.784's signature check) is tightening rather than loosening its own standards as it goes. No Suzuki/far-tail files touched anywhere in this batch, consistent with every entry's own flags. No errors on my own side this round.

---

**Verification record:** symbolic/numeric reproduction of the spectral-shift, trace, and Mellin identities (v14.770–771) plus real divisor-summatory-function numeric checks of the exact wall-cancellation and asymptotic-ratio claims; hand algebra for the areal-wall and holonomy/winding gates (v14.773–777); direct variational re-derivation of the pinned-interval and flat-annulus boundary problems (v14.778–780); fresh from-scratch solution of the hyperbolic-annulus radial and Fourier boundary-value problems, independent of the deposit's own derivation (v14.781–783); full independent `sympy` re-derivation of all three Cone metric pullbacks, with one trig-identity residual confirmed to vanish numerically (v14.784).
