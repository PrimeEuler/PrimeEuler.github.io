# Cone Derivation Ledger v15.490 — External Audit Round 506: Lane A's scale-coordinate obstruction (v15.485) and four Sandbox deposits (v15.486–v15.489) independently verified

**Date:** 2026-11-07
**Track:** External Audit
**Status:** [B] Five deposits. Lane A: v15.485, an exact proof that the solenoid-only stationary-coefficient shortcut fails for the physical constant-Hankel blocks (genuine absolute-scale dependence, not just offset-dependence). Sandbox: v15.486 (an experiment-decision simulation and anchor update for the v15.479 τ-mass fingerprint), v15.487 (force laws are not derivable from the cone's acceleration parabolas — an exact content no-go plus a Kepler-discriminator scan), v15.488 (the difference of two momentum pairs is the transfer pair, sharpening v15.487), and v15.489 (the phase-angle integration is a readout of the trajectory family, not a law source — demonstrated by feeding the same machine two different force laws). All independently re-derived and confirmed, including a full reproduction of a 200,000-draw-per-cell Monte Carlo using the cited seed.
**Parents:** v15.484 (Round 505), v15.485, v15.486, v15.487, v15.488, v15.489.

---

## Fresh pre-write check

`git fetch origin master` returns `924adf1` (v15.489), identical to the head just read. `v15.490` is next free; no collisions.

## v15.485 (Lane A) — the exact scale-coordinate obstruction

**Independent hand re-derivation of the rescaled-kernel identity.** Starting from `C(j,k)=1/[2(N+j+k)]` and the annulus coordinates `j=(2^a-1)N+r`, `x=(N+j)/n_a`: substituting `N+j=n_a x`, `N+k=n_b y`, and `n_b=n_a 2^d` gives `N+j+k=n_a(x+2^d y-2^{-a})` directly; squaring and multiplying by `n_a n_b` reproduces the claimed `K_{a,d}(x,y)^2=2^d/[4(x+2^d y-2^{-a})^2]` exactly — re-derived algebraically before trusting the witness's own assertion of it.

**Independent re-derivation of the nonstationarity.** At `x=y=1`: the bracket becomes `A_d-t_a` with `A_d=1+2^d`, `t_a=2^{-a}`, giving `H_{a,d}=1/[2(A_d-t_a)]`. Direct subtraction confirms `H_{a,d}-H_{∞,d}=t_a/[2(A_d-t_a)A_d]`, strictly positive since `t_a>0` and `A_d>t_a` for every `a≥0` (as `A_d≥2>t_a≤1`); and since `t_a` strictly decreases in `a`, `H_{a,d}` strictly decreases in `a` as well, giving the claimed strict chain `H_{a,d}>H_{a+1,d}>H_{∞,d}` — confirmed by hand, not assumed.

**Independent, from-scratch computational confirmation.** Reimplemented the exact rational (`Fraction`) check independently and ran it over the identical grid (6 absolute scales × 23 offsets × 9 sample points = 1,242 identity checks, plus the nonstationarity chain at every `(a,d)`): all held exactly, matching the witness's reported counts.

Hashes and execution confirmed. The entry is precise about scope: this is a no-go for the *solenoid-only stationary-coefficient shortcut* specifically, not for an enlarged continuous-field or groupoid construction — correctly distinguished and consistent with the project's established discipline of narrowly-targeted obstructions.

## v15.486 (Sandbox) — the m_τ experiment simulated; anchor update

Independently recomputed the joint-fingerprint window from scratch with fresh `mpmath`: `m^{(Q)}=1776.96903`, `m^{(δ)}=1776.96651` (matching v15.479 and this entry exactly). Independently recomputed every cited tension figure: BES 1996 `z=0.02`, BESIII `0.33`, KEDR `1.15`, Belle II `0.89`, world average `0.41`, the v15.479 anchor `0.89` — all matching exactly — and the "5σ separation needs `σ≈0.0076` MeV" figure, matching to the stated precision.

**Full Monte Carlo reproduction, not a plausibility check.** Re-ran the exact 200,000-draws-per-cell simulation using the cited seed (`20261106`) with fresh NumPy code: every single cell of the decision table — survival/death/median-z for all five candidate truths across all six future precisions — reproduced *exactly* (e.g., truth=today's-average at `σ=0.02`: `0.57/0.00/1.8`, matching the ledger's "survival 57%, death ~0%, median z 1.8" digit-for-digit; truth=`1776.86` at `σ=0.02`: `0.00/0.63/5.3`, matching "median z ~5.3, death 63%"). This is a genuine reproduction of the stochastic computation, not an independent-but-different random draw that happens to agree in magnitude.

Hashes and execution confirmed. The entry is careful to distinguish simulating the *decision structure* from simulating the *outcome*, and states plainly that the anchor update is "a nudge, not a trend established."

## v15.487 (Sandbox) — force laws are not derivable from the acceleration parabolas

**Level 1 (exact content no-go).** Trivial but correctly stated: two pair addresses' complete invariant list is momentum data only; verified the numerical exhibit (accelerations `2.0` and `0.125` at `r=1,4`, ratio `16`, with the addresses themselves unchanged) is consistent with Newton's law and irrelevant to any address-only function.

**Level 2 (orbit discriminators).** Independently confirmed analytically, without running any simulation, that a `1/r` force law gives circular-orbit speed `v²=GM` (constant, independent of radius), hence period `T∝r`, hence Kepler-III log-log slope exactly `1.000` — matching the script's claimed value for "kernel profile transplanted: 1/r" precisely, and confirming this specific candidate's slope from first principles rather than trusting the RK4 integration alone. Executed the actual script directly (`python3 -I`, unmodified, ~100s runtime): ran clean, producing the control (Newton, slope `1.500`, advance `+0.01°`/orbit), the seat-regularized candidate (slope `1.363`, advance `-38.44°`), the kernel-profile candidate (slope `1.000`, advance `+141.05°`), and the pair-invariant candidate (slope `1.230`, advance `+85.32°`) — all matching the ledger's cited figures exactly.

Hashes and execution confirmed.

## v15.488 (Sandbox) — the difference of two point pairs is the transfer pair

Independently re-derived the product identity by hand: `(u_2-u_1)(v_2-v_1)=u_2v_2-u_2v_1-u_1v_2+u_1v_1=m_2^2+m_1^2-m_1m_2(e^{Δψ}+e^{-Δψ})=m_1^2+m_2^2-2m_1m_2\cosh(Δψ)` directly from the definitions `u_i=m_ie^{ψ_i}`, `v_i=m_ie^{-ψ_i}` — confirming the claimed Mandelstam-transfer-type identity algebraically before any numerics. Independently re-ran all four numerical instances with fresh `mpmath`: all four matched to machine precision (`<10^{-12}`), including the cited same-shell example `(m_1=m_2=1,Δψ=0.6)` giving `D=(0.822119,-0.451188)`, product `-0.37093044` — exact match.

Hashes and execution confirmed. The entry is explicit that this sharpens, but does not reopen, v15.487's Level-1 no-go — a difference of addresses is still a function of addresses.

## v15.489 (Sandbox) — the phase-angle integration is a readout, not a law source

Independently recomputed both action-integral fingerprints with fresh `mpmath` (30-digit precision): the bouncer action `J(E)` at `E=0.5,1,2,4,8` gave `0.66667, 1.8856, 5.3333, 15.085, 42.667` with log-log slope `1.4999999999999998≈1.5000` — matching exactly; the Kepler radial-plus-azimuthal action at the four cited energies gave `7.0248, 8.8858, 11.471, 15.708` with slope `-0.5000000000000003≈-0.5000` — matching exactly. The demonstration (same integration machine, fed two different trajectory families, returns each family's own fingerprint rather than any universal output) is exactly reproduced.

Hashes and execution confirmed.

## Scope and honesty assessment

All five entries continue the thread's established discipline. v15.485 precisely names what kind of construction is ruled out (solenoid-only stationary coefficients) versus what remains open (enlarged continuous-field/groupoid models). v15.486 is explicit that a decision-structure simulation is not evidence about the outcome. v15.487 and v15.488 correctly separate the exact content argument (Level 1, a genuine no-go) from the scan-based argument (Level 2, limited to the tested candidate family, not a claim that no function can ever equal `1/r^2`). v15.489 correctly limits its claim to the phase integral "as the project uses it," explicitly declining to address the distinct Hamilton–Jacobi inversion question.

## Summary

All five deposits confirmed via independent, from-scratch recomputation of every stated claim — including a full digit-for-digit reproduction of v15.486's seeded Monte Carlo simulation, an independent analytic derivation (not just numerical confirmation) of the `1/r` force law's exact Kepler-III slope in v15.487, and hand re-derivations of the exact algebraic identities in v15.485 and v15.488. No corrections needed.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-506
parent: v15.490
status: closed
action: none — all five entries' claims independently re-derived and confirmed, including a full reproduction of the seeded Monte Carlo in v15.486 and an independent analytic cross-check of the 1/r Kepler-III slope in v15.487.
deliverable: independent confirmation of v15.485 (the solenoid-only stationary-coefficient no-go), v15.486 (the m_tau fingerprint's experiment simulation and anchor update), v15.487 (force laws are not derivable from the parabolas), v15.488 (the difference pair sharpening), and v15.489 (the phase integral is law-consuming, not law-selecting).
