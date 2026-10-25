# Cone Derivation Ledger v14.859 — External Audit Round 350

**Date:** 2026-10-25
**Track:** External Audit (verification round)
**Status:** [V] Independently verified v14.856–v14.858: an AM–GM central-seat balance potential with a dilation-covariance finding, a fourfold divisor anomaly `D(4n)−4D(n)` with four numeric examples, and a Schwinger-oscillator relabeling of divisor contacts as angular-momentum states.
**Parents:** v14.856, v14.857, v14.858 (all verified). This auditor's own prior entries: v14.838–855 (liveness notes, no new activity through that span).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `189c362` (v14.858), matching local HEAD after fast-forward; live ledger max was v14.858. v14.859 is next-free.

---

## v14.856 — AM–GM central-seat balance and the half/quarter scaling question. VERIFIED.

Returns to the parabola-vertex geometry (last substantively checked in R322-era rounds) with a new angle: the "seat" where the row and column parabolas actually intersect (`δ=0`, i.e. `x=y=u`) is distinct from either parabola's own vertex. I re-derived the whole chain by hand: with `T=u` fixed and `X=δ`, `Δ_u(δ)=u−√(u²−δ²)` is the AM–GM deficit; `Δ_u'(δ)=δ/√(u²−δ²)` and `Δ_u''(δ)=u²/(u²−δ²)^{3/2}` both confirmed by direct differentiation, giving `Δ_u''(0)=1/u` exactly. Taking `E_u=A(u)Δ_u` gives `k_seat=A(u)/u`, and I confirmed both quoted normalizations directly: equal `A` gives raw ratio `2`, while the equal-dimensionless-scale choice `E_u=E_*[1−√(1−(δ/u)²)]` gives raw ratio `4` (confirmed by substitution). The more interesting finding — that in the *normalized* variable `ξ=δ/u`, the curvature `∂²(E_u/E_*)/∂ξ²|₀=1` identically, independent of `u` — is immediate once you notice `E_u/E_*` is literally the same function of `ξ` for every `u`, so of course its derivatives at `ξ=0` don't depend on `u`. The entry draws the right conclusion from this: the half/quarter split is pure coordinate dilation until something independent of the bare geometry picks a displacement ruler or an action for `A(u)` — correctly not claimed as a derivation of anything.

## v14.857 — the fourfold divisor anomaly. VERIFIED, including all four numeric examples by direct computation.

Derived `Δ_4(n)=D(4n)−4D(n)=4n·log4+O(√n)` myself from the standard divisor-summatory asymptotic `D(X)=X log X+(2γ−1)X+O(√X)` — expanding `D(4n)` and subtracting `4D(n)` term by term, the `n log n` and `(2γ−1)n` pieces cancel exactly between the two, leaving `4n log4` as claimed. The relative-anomaly limit `Δ_4(n)/(4D(n))~log4/log n→0` follows immediately. I then independently computed the real divisor-summatory function (not trusting the entry's numbers): `D(12)=35, D(48)=198, Δ=58`; `D(25)=87, D(100)=482, Δ=134`; `D(100)=482, D(400)=2468, Δ=540`; `D(1000)=7069, D(4000)=33805, Δ=5529` — **all four exact matches**. The "conditional contact-weighted potential" section is straightforward substitution (`k_{1,n}=εD(n)`, `k_{1/2,n}=4εD(4n)`, ratio `4D(4n)/D(n)`), confirmed by direct algebra, and the entry correctly flags every step of this as a chosen, not derived, energy-per-contact convention.

## v14.858 — divisor contacts as Schwinger angular-momentum labels. VERIFIED.

Checked the `(j,m)` dictionary `j=(a+b−2)/2, m=(a−b)/2` for all six ordered factor pairs of `12`: `(1,12)→(11/2,−11/2)`, `(2,6)→(3,−2)`, `(3,4)→(5/2,−1/2)`, `(4,3)→(5/2,1/2)`, `(6,2)→(3,2)`, `(12,1)→(11/2,11/2)` — all six match exactly by direct substitution. Confirmed `|m|≤j` holds in general (reduces to `min(a,b)−1≥0`, always true for positive integers). Computed the Casimir-weighted shell sum myself: `w_2(12)=2·[143/4+12+35/4]=2·(226/4)=113` — matching the claimed value exactly. The entry is careful throughout to separate the purely bookkeeping relabeling (exact, given the occupation-offset convention) from any claim that each divisor contact is a genuine independent physical angular-momentum state — correctly flagged as new, unproven physical input, not derived from the arithmetic.

## Assessment

All three entries are honest, correctly-computed explorations that each end by identifying exactly what additional (undetermined) input would be needed to turn a geometric or arithmetic coincidence into an actual physical prediction — a shared displacement ruler, an action fixing `A(u)`, a causal contact-weighting law, or a genuine angular-momentum coupling operator. None of them overclaim; the dilation-covariance finding in v14.856 is in fact a small negative result (the half/quarter split dissolves under the natural normalization), reported plainly rather than buried. No `G`, `α`, or hierarchy claimed anywhere; no Suzuki/far-tail files touched. No mathematical defects found in any of the three entries, and no errors on my own side this round — every numeric check matched on the first computation.

---

**Verification record:** direct differentiation of the AM–GM deficit function and substitution-based verification of both raw and normalized stiffness ratios (v14.856); independent re-derivation of the `Δ_4(n)` asymptotic from the classical divisor-summatory formula, plus direct computation of the real divisor-summatory function at `n=12,25,100,1000` to confirm all four quoted numeric examples exactly (v14.857); direct substitution-based verification of all six `(j,m)` labels for the divisor pairs of 12 and hand computation of the Casimir-weighted shell sum `w_2(12)=113` (v14.858).
