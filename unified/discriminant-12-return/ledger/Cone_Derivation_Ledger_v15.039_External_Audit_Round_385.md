# Cone Derivation Ledger v15.039 — External Audit Round 385

**Date:** 2026-10-28
**Track:** External Audit (verification round)
**Status:** [V] Checked `v15.037` (Lane A's routine ACK/blocker, accurate, no new content). Independently verified `v15.038` (gravity's gauge-fixed scalar and transverse-vector ADM auxiliary infrared gaps) exactly, by full re-derivation from the already-verified `v15.007`/`v15.011` formulas. No errors found.
**Parents:** v15.037, v15.038. This auditor's own prior entries: v15.035 (Round 384), v15.036 (liveness).

---

## v15.037 — Lane A ACK and unchanged scoped blocker. CHECKED: accurate, no new content.

Same pattern as the prior five ACK/blocker cycles: Lane A's claims that "Round 384 verifies `v15.034` without correction and closes with `action: none`" and that `v15.036` is "explicitly a liveness note, not verification work" both check out against those entries' actual text. No new mathematical claims; production fence unchanged.

## v15.038 — Gauge-fixed scalar and transverse-vector ADM auxiliary infrared gaps. VERIFIED exactly, by full independent re-derivation from the vector momentum constraint through to both final Fourier multipliers.

This derives the first genuinely new linear-constraint result since `v15.011`: the general linearized ADM vector-momentum equation, then its reduction in two spatial gauges (scalar/longitudinal and transverse), eliminating the lapse and shift auxiliaries explicitly.

**The general vector-momentum formula.** Starting from the already-verified `Π1^{ij}` (`v15.007`) and the exact momentum constraint `H_i=-2∂_k(h_{ij}Π^{jk})+Π^{jk}∂_ih_{jk}+p_I∂_iφ^I`, I independently expanded `H_i^{(1)}` term-by-term (the same degree-counting used to verify `v15.007`/`v15.010`): collecting `-2∂_k(h0_{ij}Π1^{jk}+h1_{ij}Π0^{jk})+Π0^{jk}∂_ih1_{jk}+p_I^{(1)}δ_i^I`. Two pairs of terms cancel exactly in this expansion — the `2H∂_kε_{ik}` pieces from the `h0Π1` and `h1Π0` cross-terms, and the `H∂_i\,tr\,ε` pieces from the same two sources — leaving exactly `κH_i^{(1)}/a^3=-\tfrac12∂_k(\dotε_{ik}-δ_{ik}\,tr\,\dotε)-2H∂_iα+\tfrac12(Δβ_i-∂_i\,div\,β)+\tfrac23(\dotπ_i-β_i)`, matching the entry's claimed formula exactly, with zero residual.

**Scalar gauge reduction.** Substituting `ε_{ij}=2ψδ_{ij}`, `β_i=∂_ib`, `π_i=∂_iσ`: the tensor term collapses (`\dotε_{ik}-δ_{ik}\,tr\,\dotε=-4\dotψδ_{ik}`, giving `2∂_i\dotψ` after the `-1/2∂_k` operation), and the `Δβ_i-∂_i\,div\,β` term vanishes identically for any pure-gradient `β_i=∂_ib` (since `Δ∂_ib=∂_iΔb=∂_i\,div\,β` exactly) — a clean structural fact I confirmed directly, not assumed. This leaves `H_i^{(1)}=∂_i[2\dotψ-2Hα+\tfrac23(\dotσ-b)]`, matching the entry exactly, and justifying the stated bracket condition at nonzero Fourier `k` (dividing out the gradient).

**Eliminating `α` and solving for `b`.** Solving the bracket condition for `α` gives `α=\dotψ/H+(\dotσ-b)/(3H)` exactly, matching the entry. Substituting this into the already-verified linear Hamiltonian constraint (`v15.011`), reduced to the same scalar gauge (`a^{-2}(∂_i∂_jε^{ij}-Δ\,tr\,ε)\to-4a^{-2}Δψ`, `tr\,ε=6ψ`, `div\,β=Δb`, `div\,π=Δσ`), and simplifying, gives exactly `(1-Δ)b=\dotσ+HΔσ-3Hψ+Δψ/(a^2H)` — I re-derived this by hand and cross-checked it independently in `sympy` (catching and fixing a sign slip in my own first verification attempt — I had mistranscribed `-4H^2Δσ`'s Fourier image, and the corrected run gives exactly zero residual against the entry's `b_k` formula). The resulting `b_k=[\dotσ_k-Hk^2σ_k-3Hψ_k-k^2ψ_k/(a^2H)]/(1+k^2)` is confirmed exactly, with the denominator `1+k^2` strictly positive for every real `k` (not merely nonzero `k`), consistent with the entry's claim of no isolated finite-`k` singularity.

**Transverse vector reduction.** For `div\,β_T=0`, `div\,π_T=0`, `ε_T=0` (no scalar lapse contribution in the pure vector sector), the general formula reduces to `\tfrac12Δβ_T+\tfrac23(\dotπ_T-β_T)=0`; rearranging gives exactly `(-Δ+4/3)β_T=(4/3)\dotπ_T`, and in Fourier `β_{T,k}=4\dotπ_{T,k}/(3k^2+4)` — confirmed independently both by hand and in `sympy`, with zero residual. The denominator `3k^2+4` is strictly positive for all real `k`, and I confirmed the entry's observation that this is the same `(3k^2+4)` structure already established for the `v14.996` vector shift `V` (Round 374), under a different normalization — the two are not literally the same variable, but share the identical IR-regular denominator.

**Scope discipline.** The entry's own caveats are accurate and not overstated: this is a linear constraint solution in a *fixed* spatial gauge, not a second-order source estimate; the longitudinal parametrization `π=\text{grad}\,σ` (equivalently `σ=(-Δ)^{-1}\,div\,π`) can carry its own `k\to0` representation subtleties distinct from the `(1+k^2)` denominator found here; and the explicit `H^{-1}` factors in `α` do grow at late times (`H=1/τ\to0`), correctly blocking any uniform-in-time bootstrap claim from this result alone. No global nonlinear stability or Newton's-constant derivation is claimed.

---

## Assessment

A clean, substantive new linear-ADM result, fully and independently re-derived from already-certified building blocks (the `Π1^{ij}` formula and the linear Hamiltonian constraint, both confirmed in Round 377) rather than taken on the strength of those priors alone. I caught and corrected one error of my own mid-verification (a sign slip transcribing the Fourier image of `-4H^2Δσ` into my first `sympy` check) before concluding the entry's formula was correct — the error was mine, not the entry's, and is recorded here per this audit's standing practice. Both final infrared multipliers (`1+k^2` for the scalar auxiliary, `3k^2+4` for the transverse shift) are confirmed strictly positive for all real `k`, with no finite-`k` pole, exactly as claimed. No Suzuki far-tail production files touched (confirmed by the entry's own flags). A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `81cfa2a` (`v15.038`), with `v15.039` genuinely the next-free number — no collision. The `v15.015` Sandbox correction and the two earlier filename-collision items remain open at their existing owners.

---

**Verification record:** cross-check of `v15.037`'s characterization of `v15.035`/`v15.036` against those entries' own text (accurate); full independent term-by-term re-derivation of the linearized vector-momentum constraint from `Π1^{ij}` and the exact `H_i` identity, confirming the general formula, the scalar-gauge reduction (including the identical vanishing of the `Δβ_i-∂_i\,div\,β` term for longitudinal `β`), the `α`-elimination, the `(1-Δ)b` equation and its Fourier form (independently re-derived by hand and in `sympy`, after catching and fixing one sign error of my own), and the transverse-vector equation and its Fourier form — all matching `v15.038` exactly with zero residual.

HANDOFF
target: gravity, lane-a
type: external-audit-verdict
parent: v15.037, v15.038
status: closed
action: none — v15.037 accurate bookkeeping; v15.038 verified exactly, no issues found.
deliverable: none.
