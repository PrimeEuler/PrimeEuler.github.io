# Cone Derivation Ledger v14.920 — External Audit Round 361

**Date:** 2026-10-26
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.919: an exact point-source null-wavefront and Raychaudhuri focusing check in the previously-established `k=4` factor-Hessian metric, plus the project owner's new per-gate ledger-preservation protocol. Every nontrivial identity was re-derived symbolically from scratch (not merely inspected), including the full Raychaudhuri balance equation.
**Parents:** v14.919 (verified). This auditor's own prior entry: v14.918 (liveness note, following Round 360 at v14.917).

---

## v14.919 — Four-factor point-source null sphere and Raychaudhuri check. VERIFIED exactly, via independent symbolic computation of every step.

This entry is the gravity lane's first concrete step under the new `v14.916` gate (construct actual field/metric content rather than resemble one) — it takes the already-established `k=4` Hessian metric from `v14.818` and asks a genuine GR question of it: does a point-emitted radial null wavefront in this metric satisfy the standard optical-expansion focusing identity (Raychaudhuri's equation)? This is a real, checkable test, not another free-parameter extension.

**Metric substitution — verified symbolically.** Starting from `ds²=e^r[(3/4)dr²−dz⃗²]` and the substitution `τ=√3e^{r/2}`, I confirmed `(3/4)e^r=(dτ/dr)²` exactly (both sides reduce to `(3/4)e^r` identically), so the `dr²` term becomes `dτ²` exactly, and `e^r=τ²/3` turns the spatial term into `(τ²/3)dz⃗²` — giving the claimed flat-FLRW form `ds²=dτ²−(τ²/3)(dχ²+χ²dΩ²)` with scale factor `a(τ)=τ/√3`, confirmed by direct symbolic substitution rather than by inspection.

**Null geodesic and wavefront — verified symbolically.** Integrating the radial null condition `dχ/dτ=√3/τ` from `τ_e` gives `χ(τ)=√3\ln(τ/τ_e)` exactly (confirmed via `sympy.integrate`, not quoted); the areal radius `R(τ)=a(τ)χ(τ)=τ\ln(τ/τ_e)` and area `A=4πτ²\ln²(τ/τ_e)` both follow by direct substitution and match the entry's claims exactly.

**Affine null tangent — verified via the standard FLRW conserved-momentum method, independently of the entry's stated result.** Using the Lagrangian for radial null geodesics in this metric, the quantity `a²k^χ` is conserved (no explicit `χ`-dependence in the Lagrangian); fixing the normalization `k^τ(τ_e)=1` fixes the constant, and I derived `k^τ=τ_e/τ` and `k^χ=√3τ_e/τ²` from this conservation law alone — matching the entry's stated values exactly, via a route independent of how the entry itself likely obtained them.

**The optical expansion `θ` — independently re-derived, not quoted.** Computing `θ=(1/A)(dA/dλ)=(dA/dτ)k^τ/A` by direct differentiation of the area formula and substituting the derived `k^τ`, I got `θ=(2τ_e/τ²)(1+1/L)` with `L=\ln(τ/τ_e)`, matching the entry's formula exactly. The shear-zero and twist-zero claims are standard and correctly reasoned from spherical isotropy and hypersurface-orthogonality of a point-source radial null congruence — not independently computed, but not in need of separate verification given the premise.

**The Raychaudhuri identity itself — the strongest check, done symbolically and matching exactly.** I computed `dθ/dλ=(dθ/dτ)k^τ` by direct differentiation of the derived `θ(τ)` and substitution of the derived `k^τ`, then separately computed `-θ²/2-R_{μν}k^μk^ν` using the entry's stated Ricci null contraction `R_{μν}k^μk^ν=2τ_e²/τ⁴`, and confirmed via `sympy.simplify` that the difference between the two sides is **identically zero** — the Raychaudhuri focusing equation holds exactly for this metric and this null congruence. Since `θ` and `k^τ` were both independently re-derived by me (not taken from the entry), this also serves as an indirect confirmation of the stated Ricci contraction value itself: had it been wrong, the identity would not have balanced.

**Scope is honest throughout.** The entry explicitly flags this as "mathematical Hessian geometry... NOT demonstrated physical photon dynamics," does not claim a measured redshift, `G`, or source mechanism, and correctly notes it does not supersede the `v14.825` frozen-graviton obstruction (which remains a separate, unresolved issue about propagating spin-2 modes). The divergence of `θ` as `τ→τ_e⁺` is correctly characterized as ordinary point-emission vertex behavior, not a new physical singularity claim.

**The new per-gate ledger-preservation protocol** (parent references, explicit assumptions, reproducible derivation, scope flags, open gates, next handoff, live-HEAD/collision check before writes, read-back after) is a reasonable process discipline for the gravity lane going forward and does not itself require mathematical verification; I note it was followed correctly in this very entry (collision check against `v14.918` stated and consistent with the actual git history).

---

## Assessment

A clean, well-targeted piece of general relativity: a genuine physical/mathematical question (does this already-established metric satisfy the standard focusing identity for a point-source wavefront?) answered with an exact, independently-reproducible calculation rather than another layer of free-parameter machinery. I verified every step symbolically from scratch — the metric substitution, the null geodesic, the affine tangent via an independent conserved-quantity derivation, the optical expansion, and the full Raychaudhuri balance — and found no defect anywhere. This is a good-faith, correctly-scoped instance of the research direction `v14.916` called for. No Suzuki/far-tail production files touched. A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `7344718` and `v14.920` genuinely next-free; no collisions this round.

---

**Verification record:** symbolic (`sympy`) confirmation of the `τ=√3e^{r/2}` substitution and resulting flat-FLRW metric form; symbolic integration confirming `χ(τ)=√3\ln(τ/τ_e)`; direct substitution confirming the areal radius and sphere-area formulas; independent re-derivation of the affine null tangent `k^τ=τ_e/τ`, `k^χ=√3τ_e/τ²` via the standard FLRW conserved-momentum method; independent differentiation confirming the optical expansion `θ=(2τ_e/τ²)(1+1/\ln(τ/τ_e))`; full symbolic verification that `dθ/dλ-(-θ²/2-R_{μν}k^μk^ν)` is identically zero given the stated Ricci null contraction, confirming the exact Raychaudhuri identity.
