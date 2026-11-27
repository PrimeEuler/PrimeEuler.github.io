# Cone Derivation Ledger v15.1575 — External Audit Round 673

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** Gravity v15.1574 (focusing/clock budgets bounding optical rotation)
**Verdict:** CONFIRMED. Every inequality and the sharp-equality case independently rederived by hand; the committed script's numerical check reproduced to the ledger's stated precision.

## v15.1574 — CONFIRMED

**Gate 1501** (length bound): confirmed `L≤2√(Ξ(1)log(1/ε))` directly by Cauchy–Schwarz: writing `L=∫(w√v)(1/√v)dv` and applying CS with `Ξ(v)=¼∫vw²dt` gives exactly `L≤√(4Ξ(1))·√(log(1/ε))=2√(Ξ(1)log(1/ε))`, with equality iff `w√v∝1/√v`, i.e. `w∝1/v` — matches exactly.

**Gate 1502** (isoperimetric bound and sharp semicircle equality): confirmed the standard unit-H² (curvature `-1`) isoperimetric inequality `P²≥4πA+A²` holds with equality for a circle (checked directly: circle of radius `ρ` has `A=2π(cosh ρ-1)`, `P=2π sinh ρ`, and `P²` and `4πA+A²` both reduce to `4π²(cosh ρ-1)(cosh ρ+1)`). Applying this to the reflected closed curve (perimeter `2L`, area `4ψ` — using Gate 1501's `ψ=`half the original enclosed area, so the doubled/reflected region has area `2×(2ψ)=4ψ`) and solving the resulting quadratic in `ψ` gives exactly `|ψ|≤(√(π²+L²)-π)/2`, matching the ledger. Independently verified the stated equality case for a geodesic semicircle of radius `R`: arc length `L=π sinh R` (half the full circle's circumference `2π sinh R`), enclosed half-disk area `π(cosh R-1)` giving `ψ=π(cosh R-1)/2`; substituting `L=π sinh R` into the bound gives `(π√(1+sinh²R)-π)/2=π(cosh R-1)/2` (using `√(1+sinh²R)=cosh R`), exactly equal to `ψ` — confirming the semicircle saturates the bound exactly, as claimed.

**Gate 1503** (clock-budget bound): numerically verified the closed-form integral `W=√b·log(1+D/b)+2√D·atan√(b/D)` against direct numerical quadrature of `∫₀ᵇ ½x^{-1/2}log(1+D/x)dx` across four `(b,D)` pairs — matched to ~`1e-12` or better in every case, confirming the closed form. Confirmed the algebraic reduction to the `d=D/b`-normalized form `8b/ε[log(1+d)+2√d·atan(1/√d)]` is exact. Independently rederived the auxiliary "coarse bound" `|a|=(1/2)tanh(r/2)`: computing the connection one-form directly from `(T,X,Y)=(cosh r,sinh r cosφ,sinh r sinφ)` gives `a=\frac{\cosh r-1}{2}dφ` (the `dr` part vanishes identically), and its metric-dual norm against the H² metric `dr²+sinh²r\,dφ²` is `\frac{\cosh r-1}{2\sinh r}=\frac{1}{2}\tanh(r/2)` (via the standard half-angle identity) — exactly matching the stated bound, and confirming the resulting `|ψ|≤\log\cosh(L/2)` follows by direct integration given `r≤s` along any path from the origin.

Ran the actual committed `research-notes/k4_optical_clock_area_bound_v15_1574.py` from a clean scratch copy: reproduced the six semicircle numeric-vs-analytic comparisons with maximum discrepancy `≈1.15e-14` (matching the ledger's "about 1.2e-14"), and `PASS 6 semicircles and 27 clock histories` exactly.

## Collision check

`v15.1575` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `de792b9` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

v15.1574's focusing/clock-budget bounds on optical rotation are fully confirmed: the length Cauchy–Schwarz bound, the hyperbolic isoperimetric bound (including its sharp semicircle-equality case, checked exactly by hand), the closed-form clock-budget integral (checked numerically), and the coarse connection-norm bound (rederived independently from the connection one-form and the H² metric) all check out. The committed script's numerical regression matches the ledger to its stated precision. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
