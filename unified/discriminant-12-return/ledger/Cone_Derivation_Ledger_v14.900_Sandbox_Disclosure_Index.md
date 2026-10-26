# Cone Derivation Ledger v14.900 - Sandbox disclosure index

**Date:** 2026-10-26. **Lane:** Sandbox (little Euler), deposited on Jeremy's
explicit direction. **Status:** disclosure document - an inventory of
sandbox-only material not present in this ledger, with per-item verdicts as
recorded in the sandbox notes. Listing is disclosure, not endorsement; no
item below is promoted to a result by appearing here. **Collision check:**
immediately before writing, live master HEAD `f34eb0631fde60bd4f044809dae6e145a22442df`
(audit liveness v14.899); v14.900 next free.

**Why this entry exists.** The ledger is the only record shared across lanes.
A substantial body of sandbox work (84 run directories, 33 exploration items)
exists only in the sandbox workspace and is invisible to Lane A, External
Audit, and the gravity lane. Cross-lane conversations have repeatedly assumed
shared knowledge of that material (most recently: the Ashtekar/LQG rhyme of
the 2026-10-21 phase-tangent-holonomy run, and the balance-principle /
induced-gravity cluster of 2026-10-21, both SANDBOX-ONLY). This index makes
the hidden layer visible so every lane can tell what the others do and do
not have.

---

# Sandbox Disclosure Index

**What this document is.** An index of the sandbox-only work in Jeremy's
Discriminant-12 / Cone project: the run directories under
`~/workspace/d12/lane_b/sandbox/runs/` and the exploration directories under
`~/workspace/d12/explorations/`, each with a one-line statement of what it is
and the verdict its own notes record.

**What is NOT in the shared record.** The shared cross-lane record for this
project is the ledger (`Cone_Derivation_Ledger`, in the repo
`PrimeEuler/PrimeEuler.github.io`). The ledger is the only record the other
lanes can see. **Lane A, External Audit, and the gravity lane cannot see any
item listed here** unless it is explicitly marked **LEDGERED** with a version —
no exceptions, no partial visibility. If a conversation with another lane
assumes knowledge of an item below that is not marked LEDGERED, that lane does
not have it; it is pattern-matching a summary, not checking a record.

**Disclosure, not endorsement.** Presence in this index is disclosure only.
Verdicts are quoted as recorded in the run notes themselves, including
negatives, corrections, and withdrawals; nothing below is promoted to a
result by being listed. Sandbox notes are exploratory ([I]/[O] unless the
note itself says otherwise) and were written under the standing firewall:
nothing leaves the sandbox for the ledger without Jeremy's per-item approval.
That firewall changed on 2026-10-26: this index was deposited on Jeremy's
direction ("push it, and lets start ledgering everything"), and sandbox work
is ledgered from this entry forward. The backlog below is disclosed by this
index; individual backlog items keep their recorded verdicts and are not
promoted by being listed.

**Status key.** `SANDBOX-ONLY` = exists only in this workspace.
`LEDGERED vX` = the material (or its write-up) was deposited in the ledger
under that version; the directory here remains the sandbox original.
Items prepared as returns to ledger handoffs whose deposit could not be
confirmed from the notes alone are marked SANDBOX-ONLY, with the handoff
named.

**Count.** 117 items: 84 under `runs/` (83 directories + 1 loose file),
33 under `explorations/` (32 directories + 1 loose script).

---

## 1. First probes — helix, standing wave, spectrum (2026-09-27)

- **20260927-175943-standing-wave-embedding** — Faithful staging of Jeremy's standing-wave/helix embedding (SU(2) circle as shared cone base, 12-division, V₄ Fourier tool); a record, not an experiment — nothing failed, five questions left open. `SANDBOX-ONLY`
- **20260927-213532-cluster-at-zero** — Recomputed the corrected compression F_N to N=32 to interrogate the 6-interval Ritz cluster straddling zero; cluster tracked but per-mode signs/simplicity and true-eigenvalue inclusion left open. `SANDBOX-ONLY`
- **20260927-221455-toy-hamiltonian** — Toy rest-seeking Hamiltonian H = p²/2m + V₀(cosh u − 1) tested classically and quantum-mechanically; one expectation corrected in the run: the hyperbolic pendulum *hardens* (period shrinks with amplitude), contrary to the task's parenthetical. `SANDBOX-ONLY`
- **20260927-222549-pendulum-recheck** — Hyperbolic pendulum rechecked against Jeremy's refined picture (max energy cost at turning points, geometric amplitude return under damping); numerics clean, nothing failed. `SANDBOX-ONLY`
- **20260927-230329-resonance-probe** — Tested whether exact √n HO ladder quanta pick out the standing-wave mode — but on the reversed mode count (12 antinodes / 11 nodes); superseded by v2, only its method stands. `SANDBOX-ONLY`
- **20260927-230625-cluster-residuals** — Transfer-spec residuals for the 8 cluster Ritz pairs at N=32: modes 1–6 force a true A1 spectral point into a near-zero inclusion disc (widest half-width 1.76e-4); modes 7–8 residuals too large to be informative. `SANDBOX-ONLY`
- **20260927-230930-resonance-probe-v2** — Re-run on Jeremy's corrected mode (12 nodes, 11 antinodes): the exact ladder hears the mode's wavenumber (11π/2 → n ≈ 149) resonantly, but nothing in the ladder selects the numeral 12 itself; 12 remains selected by the D12 arithmetic. `SANDBOX-ONLY`
- **20260927-235831-amgm-fourier** — Jeremy's definition tested (Fourier analysis = per-frequency geometric mean over the V₄ totient positions {1,5,7,11}); built as a working analysis tool on the 12-point grid; the GR correspondence ("GR comes in as it bends") remains Jeremy's interpretive framing — curvature computed, no field equations derived. `SANDBOX-ONLY`

## 2. Spherical screw / archimedean product form; pronic and V₄ threads (2026-09-28)

- **20260928-003742-spherical-screw** — Jeremy's spherical envelope A_j = √(36−j²) applied to the helix family: per-helix V₄ product is exactly 385 + 0i for all τ (universal residue 385^{1/4}, phase exactly 1); corrected a brief arithmetic slip (GM of V₄ amplitudes is 385^{1/4}, not √385). `SANDBOX-ONLY`
- **20260928-005525-spherical-archimedean** — Setup brief for writing the archimedean channel as E(t)·P(t) (nonnegative circle envelope × helix overlay phase factor); scaffolding and task definition only, discharged by the follow-up run and Overlay P. `SANDBOX-ONLY`
- **20260928-010240-spherical-archimedean-2** — Exact small-/large-t asymptotics of A₁₂ (Lerch singular expansion, K₀ = 1.7629610990…); correction to the brief: A₁₂ > 0 just right of 0 (bump max 0.4410 at t ≈ 0.7515), one zero at t₀ = 1.9120492808…, then negative linear; the dictionary/helix-representation line later closed in the ledger (v14.592/v14.593). `SANDBOX-ONLY`
- **20260928-022108-pronic-ladders** — Honest negative: pronic ladders do not beat harmonic ladders — pronic conditioning collapses for N ≥ 8 (cond up to 1e16), telescoping hybrid fails flat; both families fail near the log singularity, confirming the analytic obstruction. `SANDBOX-ONLY`
- **20260928-023559-pronic-v4** — Exact V₄ arithmetic: (Z/12)× = {1,5,7,11} ≅ C₂×C₂ coincides with the special antinode labels, χ₁₂ is the conductor-12 character, τ(χ₁₂) = 2√3 supported on the V₄ orbit, amplitude product over V₄ positions = 385; a 3657 = 3·23·53 thread is marked numerology in the report and dropped. `SANDBOX-ONLY`
- **20260928-024247-v4-envelope-construction** — P_{χ₁₂} applied to the 12-point envelope gives exact support on {1,5,7,11} with closed-form values; χ₄, χ₃ channels annihilate the even envelope exactly, leaving χ₁₂ distinguished; the J₁ Airy profile does not survive projection (affine R² = 0.092). `SANDBOX-ONLY`
- **20260928-024806-v4-threads-closeout** — Both open V₄ threads closed: beat structure exact (period 11π, spectral weights 12-periodic with exact zeros at n ≡ 3,9 mod 12) but no structural relation to T's log-blowup found; annihilation theorem proved (joint χ₄/χ₃ annihilation ⟺ s is H-even); conductor↔orbit correspondence only partial. `SANDBOX-ONLY`

## 3. Bucket 2 — boundary constants, edge criteria, the 0.48 arc (2026-09-28–29)

*Section note: this package's deliverables entered the ledger as the Bucket 2
gap-characterization package at **v13.838** (2026-09-28) and in the v13.84x–87x
entries that followed; the run directories below remain the sandbox originals,
and each report describes itself as sandbox-only.*

- **20260928-120000-bucket2-boundary-constants** — First numerical exploration of Suzuki's source-faithful first-kind equation and the boundary ratios r₀, r₁; produced the "r₁ = −1, r₀ = −(1+i) exact" reading that the next run retracted. `SANDBOX-ONLY`
- **20260928-150847-bucket2-normalization-audit** — Self-correction: the ledger and arXiv v2 *agree* on eq. (8.5) (the previous run misread the source), and its "r₁ = −1, r₀ = −(1+i) exact" result does **not** survive — it was circular (it assumed the boundary constants it derived); structural finding: affine functions lie in Ran(K_A), so (I₀, I₁) are genuinely undetermined by (8.5) alone. `SANDBOX-ONLY`
- **20260928-151744-bucket2-extra-conditions** — Exhaustive catalog of Suzuki §§6–8: the text provides **no** two independent linear scalar conditions fixing the (I₀, I₁) nullspace; only the full deficiency equation (8.4) (given T_a invertible) and the quadratic norm equality of Thm 1.5. `SANDBOX-ONLY`
- **20260928-155806-bucket2-distributional-ta** — Faithful distributional realization of T_a: validation gate passes ((8.5) residual mod affine 2.26 → 1.5e-06), ratios r₁ = ∓8.75, r₀ = +27.28 at A=3 — and the edge criteria **fail** cleanly: r₁ = Θ(e^A), α_A → ±0.48, not 0. `SANDBOX-ONLY`
- **20260928-165927-bucket2-natural-bc** — Jeremy's pre-registered falsification test: **Horn A is falsified** — the Θ(e^A) growth persists under natural boundary conditions with the same constant |c| ≈ 0.48; evidence flips to Horn B (the edge criteria as admissibility gates are the problem). `SANDBOX-ONLY`
- **20260928-194718-bucket2-edge-criteria-reformulation** — Analytic follow-up: the edge criteria were never admissibility gates on the deficiency vectors — they were the vanishing condition for the affine contamination b_A(ξ) of the transported edge source; reformulated accordingly. `SANDBOX-ONLY`
- **20260928-200000-bucket2-cancellation-mechanism** — Mechanism behind L₀+L₁ = 0 found: the Tikhonov-regularized (8.5) solve selects (A,B) by an exact projection principle onto ker(Kᵀ) (proven exactly); the cancellation reduces to an asymptotic orthogonality with strong numerical evidence — its analytic proof remains open. `SANDBOX-ONLY`
- **20260928-210000-bucket2-selection-identity** — Selects, conditionally: Suzuki's text determines its deficiency vectors by exact T_a-inversion (Lemma 6.2), and the kink-faithful weak-form realization provably computes exactly those vectors (λ < λ_a), so the reported numbers (0.48, L₀+L₁ = 0) are Suzuki's true numbers; the continuum (8.5) problem needs no selection — the 2D near-nullspace is a discretization artifact. `SANDBOX-ONLY`
- **20260928-215739-bucket2-wiener-hopf-lemma** — Obstacle, precisely characterized: the lemma as literally stated is trivially true (Cauchy–Schwarz); the meaningful correlation version reduces to a delicate O(1) cancellation of opposite signs, not a structural orthogonality; a full Wiener–Hopf proof is blocked on analytic control of the discrete minimizer for a growing kernel. `SANDBOX-ONLY`
- **20260928-223634-bucket2-downstream-absorption** — Wall at the transfer steps: the −0.48 remnant is absorbed cleanly by the corrected edge equation and the Wiener–Hopf completion, but the handoff to the paired-transfer/Weyl criteria stops at three named points (W1–W3), each then attacked by the following runs. `SANDBOX-ONLY`
- **20260928-225734-bucket2-w1-remnant-profile** — W1 closed: remnant-inclusive transported profile derived, the remnant boundary functional B_{0.48,0,±} determined as a half-line constant, functional independence proved analytically and quantified numerically. `SANDBOX-ONLY`
- **20260928-233500-bucket2-w2-convergence-reformulation** — W2 closed: the v13.757 §9 convergence program restated in R1/R2 language, correcting §9's scope (the pairings are two-scale — bulk and edge contribute comparably) and naming the load-bearing next lemma (PAIR-H, two-scale pairing asymptotics). `SANDBOX-ONLY`
- **20260929-001330-bucket2-pairh-bulk-lemma** — Empty directory; no note was ever written (superseded the same night by the 001603 run). `SANDBOX-ONLY — uncharacterized (empty)`
- **20260929-001603-bucket2-pairh-bulk-lemma** — Bulk lemma refined (not proved as conceived): the W2 picture is **refuted** by direct bulk/edge splitting — the I₀ pairing is edge-localized (bulk contributes ≈ 0; the full Θ(Ae^A) comes from the right edge layer), and R2 (L₀ + L₁ → 0) is confirmed with the same 0.48 governing both scales. `SANDBOX-ONLY`
- **20260929-001741-bucket2-w3-route-b** — W3 closed: remnant-inclusive transported boundary theorem stated at v13.779's precision (β cancels via R2; α-even survives as a common additive distortion); the identification leg stated precisely as the δ∞ discrepancy equation. `SANDBOX-ONLY`
- **h1_general_z_membership_vs_dualslot.md** *(loose file in runs/)* — Read-only investigation (2026-09-29): direct e_z ∈ H(T_A) membership attempt plus dual-slot canonization for Route T / G2-H1; determines whether downstream genuinely needs general z. `SANDBOX-ONLY`
- **20260929-dbar-reconstruction** — Ledger archaeology pinning down D̄ exactly: Suzuki's isometric transport H(T_a) →∼ H(S_a), an isomorphism *between* two completions, not a differential operator in one space; flags the false friend `Dbar_{a,θ}` (v13.278/279), an unrelated self-adjoint extension. `SANDBOX-ONLY`
- **20260929-g1-identity** — G1 verdict: the needed R_A⁻¹ vs T_A⁻¹ ratio identities (r₀, r₁ as T_A-side pairings) already **hold** at ratio/shape level in the ledger (v13.782 (6)–(8)); the R_A moment program itself stays retracted. `SANDBOX-ONLY`
- **20260929-g2-duality-pairing** — G2: explicit construction of the duality pairing ⟪·,·⟫_{T_A} that the ledger invokes in five places without defining in one; assembled from [D] parts under one fixed convention. `SANDBOX-ONLY`
- **20260929-ident-analysis** — The identification leg analyzed: the δ∞ discrepancy equation written exactly, with δ∞(z) = 0.48·lim[e^A M₁(z̄)/c_A] a normalized, z-dependent, non-zero common α-distortion that any identification m_A → −i(a/b)D_ξ/Ξ must absorb. `SANDBOX-ONLY`
- **20260929-pairh-analysis** — PAIR-H stated in three layers with the v13.855 refinement correcting W2's mechanism: the I₀ bulk does *not* contribute comparably (the extra A is test-function growth, not interval length); I₁ is genuinely two-scale (bulk +0.26e^A, edge −0.73e^A). `SANDBOX-ONLY`
- **20260929-route-e-edge-energy-limit** — Route E: the edge-energy limit theorem stated precisely and attempted; the distributional profile i(e^{−ξ} − δ₀) is cutoff-independent, and the remaining work is the energy-topology limit itself (obstruction stated, not closed in the note's opening). `SANDBOX-ONLY`
- **20260929-route-t-pairings** — Route T: T_a⁻¹-side pairing identities for G_A/H_A that avoid evaluating D̄, via S_A⁻¹ = D̄T_A⁻¹D̄⁻¹; corrects the W3 report's "[R, D̄] = 0" slip (the parity conclusion is unaffected — the sign cancels doubly). `SANDBOX-ONLY`
- **20260929-cube048** — Jeremy's "rest square/cube" geometric thread plus an exact anchor, corrected: the twisted-convolution identity as tasked is **false** (numerics refuted it, residual 1.4e5); the corrected identity with the character summatory M(y) in place of ⌊x/d⌋ verifies to 3.6e-12. `SANDBOX-ONLY`
- **20260929-factor048** — Code-and-output run only (edge-integral scripts, logs, profiles); no prose note exists, so no verdict can be quoted — its subject (the ψ(1/4) transcription bug in the 048 arc) is documented in rerun048/mech048. `SANDBOX-ONLY — uncharacterized (no prose note)`
- **20260929-lambda-twist** — Empty directory; the LAMBDA-TWIST worker's result is reported inside mech048: [D] **different** — Suzuki's A_a, the full D12 A_{K,a}, and the sandbox χ₁₂-twisted object are three distinct objects. `SANDBOX-ONLY — uncharacterized (empty; result recorded in mech048)`
- **20260929-mech048** — What sets the odd-channel −0.48: **not** the corrected screw g — it is set almost entirely by the universal λ = −1 polynomial/|x−y| kernel N acting on an odd solution it forces to be ≈ sinh; for the N-kernel alone the slope is exactly −1/2 (A₊ = −cosh A). The FACTOR-048 ψ(1/4) transcription bug that manufactured false linear growth is documented here. `SANDBOX-ONLY`
- **20260929-rerun048** — Corrected-kernel numerical recovery (the lifting instrument for all provisional Bucket 2 [N] claims): corrected constants (ψ(1/4), log(12/π), ζ(2,1/4)); the corrected screw is bounded with g(t)/t → 0 — the c₁ = −0.154 linear-growth mechanism is **dead**. `SANDBOX-ONLY`
- **20260929-successor048** — Complete: the dressed/bare cubic-moment ratio is ≈ 0.970 — the earlier 0.955 was **overstated** (largely discretization error, refuted as N grows) and 1.0 is not achieved either; a genuine persistent ≈ 3% screw dressing survives A → ∞, revising the −0.48 factorization to −0.489 ≈ (−0.5)(0.978). `SANDBOX-ONLY`
- **20260929-whedge** — Half-line Wiener–Hopf edge problem for the 0.970 ratio: factorization attempt a clean negative (blocked by the distributional explicit-formula symbol — the same analytic wall as v13.774 §7); exact finite-A moment identity derived with edge domination proved, and the solver verifies the moment numerically. `SANDBOX-ONLY`

## 4. Positivity, FEM and number-pattern probes (2026-09-30 – 10-02)

- **20260930-divisor-tension** — FEM/ablation anatomy of the full-A_a form: full Λ keeps λ₁ ≥ 0 (unresolvable, ~1e-25) while primes-only, indicator and no-prime variants go negative (−1.07, −4.24, −4.97) — dissects which prime powers ≤ e⁴ carry the positivity load; no RH claims. `SANDBOX-ONLY`
- **20260930-hp-operator** — Construction notes for two finite-section Suzuki-type matrices: the χ₁₂-twisted A₁₂ (sees only 5, 7, both negative) and the full D12 A_K for ζ_K = ζ·L(s, χ₁₂) (5, 7 cancel exactly; sees only 2, 3, 4). `SANDBOX-ONLY`
- **20260930-lqg-select** — LQG selection-principle computation (parabola–circle intersections, SU(2) tetrahedra at R=6, V₄/QR(12) filter selecting 30 tetrahedra, gluing graph); parked per Jeremy 2026-09-30. `SANDBOX-ONLY`
- **20261001-circle-hyperbola** — Jeremy's construction built and analyzed: circle x² + y² = n² + 1 through the edge lattice points, hyperbola arc xy = n, divisor spread in the centered coordinate u = ln x − ½ ln n, arc-length asymptotics; a visualization/analysis coordinate. `SANDBOX-ONLY`
- **20261001-close-the-if** — The v13.910 continuum "if" cannot be closed by soft methods: inf ≤ 0 is numerically settled (inf ≤ 1.7e-9) but inf ≥ 0 is **RH-hard** — the conditional is, modulo the upper bound, equivalent to a weak form of RH; the task's suggested soft close is blocked at the sign-structure level. (See the next run for the sharper numerical refutation.) `SANDBOX-ONLY`
- **20261001-continuum-if** — Sharper verdict: **refuted** numerically — the infimum is ≈ 1.83×10⁻⁸ > 0, N-stable and O(h²)-converged; v13.910's hypothesis is false, and what holds instead is a V of slope c_m shifted up by 10⁻⁸–10⁻⁷. `SANDBOX-ONLY`
- **20261001-m7-ratio** — The m=7 ratio s₇/c₇ ≈ 1.21103 explained: it is the null-cluster-restricted KK[7] norm (fiber dilution), nothing else — with the refinement that the V is two-sided asymmetric (plus-side slope ≈ 1.35654, unreported in v13.902); the global norm √2 is the wrong object for the V-slope. `SANDBOX-ONLY`
- **20261001-miss-pattern** — First look at Jeremy's 2016 symmetry coordinate s_k = (n−k²)/(2k): exact toolkit in integer arithmetic — the miss value v_k = (n mod k)/(2k), hit ⟺ k | n, and D(n) = n·H_n − Σ{n/k}, so the misses literally are the fractional parts. `SANDBOX-ONLY`
- **20261001-tda-filter** — T/D/A partition and the maximal-miss prime filter verified exactly to n = 200,000 (π(n) = #{k : e(k) = 0}); the asymptotic candidates are mostly killed — the e=0 atom's mass *is* the PNT restated, and no moment of the miss distribution can cap π(n) from above; no bypass found. `SANDBOX-ONLY`
- **20261002-sieve-renorm** — Sieve renormalization flow: the sieve lift is exact (168 primes ≤ 1000 regenerate the full 10⁶-bit pattern bit-for-bit) and the zero-ordinate content is scale-free under the flow — the same ordinates appear in the seed region and the emergent region alone. `SANDBOX-ONLY`

## 5. Conductor channels and Overlay P (2026-10-18)

- **20261018-conductor-channels** — Other conductors get their own channels and constants: every primitive degree-1 channel shares Suzuki's ramp shape with a = 1/4 or 3/4 by parity, the conductor entering only through log(q/π); dive iff C₁(χ) < 0, with q=12 control reproducing s = 0.2406063975. `LEDGERED v14.612`
- **20261018-overlay-P** — Overlay P discharged **in the distribution class**: P is the measured 1/n tempered distribution with the 1/n part resummed in closed form (P(x) = a₀/2 + s·log(2 sin(πx/(2L))) + Σ rₙ cos(πnx/L)), s = 0.24060639745313878; the finite/ℓ¹ versions were already proved impossible by the prior run. `LEDGERED v14.596`

## 6. Selector hunts (2026-10-19–20)

- **20261019-chain-selector** — Chain scans for a reason/action behind ψ_D = 45.310004305: **negative** — uniform chains miss (best (4/3)³¹⁵ at 7.8×10⁻⁵, 7× outside the window and physically excluded), EM-step chains miss by orders more; a single repeated action does not select the chain. `SANDBOX-ONLY`
- **20261020-amgm-selector** — AM/GM-product selector test: it **hits everything, therefore selects nothing** — the 13-smooth log lattice has 2.47M points in the depth range with mean spacing *smaller* than the hit window, so all three depths "hit" at exactly chance density. `SANDBOX-ONLY`
- **20261020-dynamical-selector** — Dynamical selector probes: most candidates dead at screening (bath balance unfalsifiable as posed; Mathieu/commensurability/climb candidates range-dead); the bath steady state has the right *form* (it selects the consecutive ladder split (n̄+1, n̄)) but not the depth. `SANDBOX-ONLY`
- **20261020-phase-selector** — Phase/occupant selector probe: the p–e pair phase φ_pe is a function of R only, so a phase selector must name it independently; no root of unity with q ≤ 36 comes near it (best q ≤ 144 misses by ~8 orders of magnitude against the mass ratio's precision). `SANDBOX-ONLY`
- **20261020-position-selector** — Position scan: are the *depths* (not the gap) selected by chains? **Negative**, all families, all three positions — uniform chains, EM steps, regulator chains and two-regulator mixes all land chance-consistent or orders outside the window. `SANDBOX-ONLY`
- **20261020-quantized-inertia** — Sewing up McCulloch's QI/MiHsC loose ends: the quoted a′ = 2×10⁻¹⁰ follows *only* under the particle-horizon-diameter reading of Θ (the other definition in the same papers gives 3.3× more, nowhere near the fits); the sampling function's linear law fails in §2 of the note. `SANDBOX-ONLY`

## 7. Rotor anatomy and the duck test (2026-10-19)

- **20261019-rotor-coupling** — The paraboloids-on-a-fiber anatomy: cos θ coupling weights w_j = (j+1)/√((2j+1)(2j+3)) are exact and maximally democratic (every rung → 1/2, no rung singled out); the forced climb telescopes to a Wallis ratio ~ √(π/2)·2^{−J} — a pure per-rung halving with J unselected. `LEDGERED v14.626`
- **20261019-duck-test** — Jeremy's device↔model "deep rhyme" bet, tested in the rotor sector against a pre-stated criterion (identity iff forced — same equations, no free parameter in the map): the two weight systems obey one exact relation at every rung — the rotor sector is **identity**, not analogy. `LEDGERED v14.628`
- **20261019-duck-test-rest** — The rest of the duck test: shaping sector **not forced** (analogy by design — a single center loop's |B| level set deviates +64% at X=2 and ceases to exist beyond |X| ≈ 2–3; the totient ring set does better but is fitted, not forced); acoustics splits and the Suzuki side likewise not forced. `LEDGERED v14.631`

## 8. The Oct 21 physics cluster (2026-10-21)

*The most cross-referenced sandbox material in conversation — and, except as
noted, none of it has ever been visible to the other lanes.*

### 8a. The Balance Principle and induced gravity

- **20261021-balance-principle** — Jeremy's Balance Principle, stated in his words ("the constants are the numbers that keep everything in balance"): kinematics determines everything it determines *exactly*; every residue it leaves is a dimensionless constant struck as a balance between structure and contents, never a property of the structure alone. Carries his Sciama stance (G as the cosmic-inventory balance constant). Sandbox statement, explicitly not ledgered. `SANDBOX-ONLY`
- **20261021-induced-program** — The Sakharov induced-gravity program run as an audit: the bill is M̄_Pl² = 5.9308e36 GeV² and the SM pays ~1.96e-33 of it (vacuum m⁴ terms don't pay; the m² curvature response does). **Correction carried in the companion run: this run's species screen contains the rungs-vs-dof counting bug — its tower self-consistency reading is superseded/withdrawn (see thick-tower-model).** `SANDBOX-ONLY`
- **20261021-thick-tower-model** — Thick-tower model **plus the owned correction**: the induced-program screen counted rungs instead of total degrees of freedom; with correct counting a full-bill payer overshoots its species cutoff by √12π (degenerate) or √36π (tower) at *every* thickness — the earlier "thick tower d ≳ 113 self-consistent / SM thickness 107 within 3%" headline is **withdrawn** as a counting-bug artifact. Substantive residue: a tower pays exactly 1/(36π) = 0.88% of the bill below its species scale — it locates where gravity completes; it does not pay for it. `SANDBOX-ONLY`
- **20261021-tower-bill** — Tower-bill check on the action side: the tower check closes into species bookkeeping (M̄² ≈ (Nd/36π)M_top²); a tower pays exactly when its top is the species scale, and nothing in the sum selects the split — induced gravity trades one number for two. `SANDBOX-ONLY`
- **20261021-payer-scalar** — Payer portrait as a spec sheet: a heavy dark spin-0 sector paying the induced bill (D copies at M_X = M̄_Pl√(12π/D)); D = 1, 2 payers are hole-like (r_s > λ_C), D ≥ 3 particle-like; in all cases the payer sits at the shallow end of the depth axis, ~47–53 units above the electron — it is never a deep object. `SANDBOX-ONLY`

### 8b. Selector-adjacent audits

- **20261021-factorization-audit** — Two-leg factorization audit of the target depths through 14 named stations × 114 named candidates: **negative** — the only in-window hits are tautologies (routing through the pair-GM station returns the pair depth by construction); no intermediate station splits any depth into two already-meaningful legs. `SANDBOX-ONLY`
- **20261021-flavor-fn** — Froggatt–Nielsen check on the electron Yukawa: FN compresses the hierarchy *pattern* (9 Yukawas → ε + charges + O(1) coefficients; the half-integer grid noticed from the data is suggestive only) but does **not** select y_e; the RG fixed point is closed by inspection (β(y_e) ∝ y_e, only fixed point 0). `SANDBOX-ONLY`
- **20261021-tick-resonances** — Compton-tick resonance scan over 23 PDG masses (253 pairs): the naive rational scan is artifact (below the Monte Carlo null); the honest restricted scan is **exactly chance** — the real spectrum produces no more genuine small-integer commensurabilities than random masses. `SANDBOX-ONLY`
- **20261021-two-bath** — Two-bath balance probe: **negative** — no declared (reservoir, coupling) pair, single- or two-bath, lands any target depth (nearest miss residual 2.596, a factor ~180 in ratio); baths select splits, not depths — the missing ordered pair remains missing. `SANDBOX-ONLY`
- **20261021-eft-play** — EFT play on the Kepler note's machinery: the dictionary is machine-verified (e² = 2Y/(T+Y), q² = (T−Y)/(T+Y)) and v3.4's hot-bath fixed point q₀ = 1/√3 is exactly a ray pair on the cone (X : Y : T = √3 : 1 : 2) — the bath selects a direction, not a point or scale; the G lever exercise shows central perturbations only rotate the cone point, and Mercury's 42.98″/century is reproduced with the cone as frame and Einstein's term as credit. `SANDBOX-ONLY`

### 8c. Anomalies and the strong force

- **20261021-neutron-anomaly** — Neutron lifetime anomaly bookkeeping: beam (888.0 s) vs bottle (877.75 s) forces Γ_invisible = 1.31504e-5/s (1.15% branch) if both are right; the Fornal–Grinstein n → χγ branch is **closed** by direct line searches across essentially the whole mass window; the fully invisible n → χφ branch remains open (neutron-star constrained). `SANDBOX-ONLY`
- **20261021-more-anomalies** — Flyby anomaly: Anderson's formula fits Galileo I/NEAR, then **failed forward prediction** (Rosetta II/III, Juno showed nothing) — closed toward tracking/modeling systematics. Lunar eccentricity anomaly: **open** — LLR eccentricity grows at ė ≈ 9e-12/yr beyond tidal models, a residual in the shape (eccentricity) channel specifically. `SANDBOX-ONLY`
- **20261021-a0-bite** — Biting a₀ vs cH₀: every candidate identity (cH₀/2π, cH₀/6, de Sitter form) sits inside a₀'s own systematic band, so the exact identity is **not selected** — but the structural bite is real: the deep-MOND limit of the RAR is a geometric mean, g_obs = √(g_bar·a₀), an AM/GM balance curve. `SANDBOX-ONLY`
- **20261021-strong-force** — Dimensional transmutation is nature's one working selector (depth 2π/(β₀α_s) = 6.945 mints a scale from a pure number); the proton's depth audited: 44.011 = 39.436 unexplained desert leg + 4.577 QCD leg that running + lattice *do* explain; the proton itself is the payer portrait measured (99% of its mass is field energy, not quark masses). `SANDBOX-ONLY`
- **20261021-monopole-question** — Output-only run (no prose note): GUT monopole bookkeeping — SM couplings miss unification at 2e16 GeV (37.45, 46.24, 45.26) while MSSM couplings meet (~24.3); monopole mass ~5e17–8e17 GeV, Dirac charge 68.5e, α_m = 1/(4α) = 34.259; against gravity's ask (desert depth 33.02 vs ψ_D = 45.31) the dyon running falls short and in the wrong column. `SANDBOX-ONLY — characterized from its output file (no prose note)`

### 8d. Holonomy

- **20261021-phase-tangent-holonomy** — Phase-tangent transport checked as a would-be selector: bare cone holonomy gives the universal deficit 2π(1 − 1/√2) = 1.840302 rad — G-free but pair-*independent*, so it cannot select R; gravitational holonomy is pair-dependent in the wrong way (it presupposes G). The selector slot stays empty. Contains **Jeremy's LQG rhyme** (his observation, labeled structural in the note): LQG's variables are Ashtekar-connection holonomies and its area spectrum A_j = 8πγℓ_P²√(j(j+1)) uses exactly the GM Casimir √(j(j+1)) — recorded as a rhyme, "including the disease," not a theorem about the grid. `SANDBOX-ONLY`

## 9. Lorentzian shell gate (2026-10-24)

- **20261024-lorentzian-shell-test** — Sandbox test of v14.807's open gate: the canonical fixed-shell generating polynomial is M-convex only for n = 1, 2 (F₂ = xy(x+y)); every shell n ≥ 3 **fails** by the extreme-pair/exchange obstruction (minimal witness at n=3), so the Hessian test is moot there and Lorentzian structure in this family would have to mix shells. `LEDGERED v14.810`

## 10. Payload machinery

- **p4-payload** — Payload-freeze machinery (KKT/residual-cross freeze scripts and logs) for the Bucket 2-era deliverable pipeline; code and logs only, no prose note. `SANDBOX-ONLY — uncharacterized (no prose note)`

---

## 11. Foundations explorations — hydrogen, the bicone, and the cone dictionary (2026-10-05–06 and after)

- **hydrogen-radial** — The cone gets hydrogen's radial *kinematics* exactly (fixed-l radial states = SU(1,1) discrete series with K₀ = T as operators) but the 1/n² energetics are not derived — the unexplained input shrinks to flux conservation / the Fock S³; the bicone appendix (two cones glued at a common T₀ circle, su(2)⊕su(2), gluing = the KS constraint) is machine-verified as a proposal, not a derived structure. `SANDBOX-ONLY`
- **fock-s3-cone** — Fock S³ → Hopf → cone shell map made explicit and machine-verified, but full hydrogen SO(4) does **not** descend to the shell: only U(2) ⊂ SO(4) preserves the Hopf fibration, and Paper C has su(2)⊕su(1,1), not the required su(2)⊕su(2) — the cone contains the states and the radial ladder, not the SO(4) generators explaining degeneracy. `SANDBOX-ONLY`
- **ks-constraint** — The KS bridge worked explicitly in (T,X,Y): the quantum Hopf identity x_op² = N(N+2) (with its +2N ordering correction) machine-verified; the win is the explicit translation and derived-vs-input accounting, not a rediscovery of KS. `SANDBOX-ONLY`
- **omega-e-link** — The KS ω–E link reconstructed: ω² = |E|/(2m) is a *matching condition* of the KS map (the analytic heart is the cited lemma r∇² = (1/4)Δ_u, a calculus fact, not cone geometry); the quantization condition is where the coupling enters. `SANDBOX-ONLY`
- **lobes-coulomb** — Coulomb wrap-up: **closed** up to the single coupling — the ω² = |E|/(2μ) link is not an input but an identity of the Levi-Civita/KS regularization map (verified symbolically, P² = 4r p² exactly); Part 1 stages Jeremy's Larmor-orbit-projection prompt for the orbital lobes. `SANDBOX-ONLY`
- **bicone-dipole** — Hydrogen dipole from the bicone: structure yes, scale no — the bicone yields the selection-rule pattern and |⟨R₁₀|r|R₂₁⟩| = √3·|C| purely algebraically, but |C|/a₀ = 256/(243√2) is *not* derived here; it is stated as a checkable prediction for the Barut construction (discharged by parabolic-dipole). `SANDBOX-ONLY`
- **parabolic-dipole** — The prediction discharged: Barut–Kleinert's parabolic SO(4,2) construction computes |C|/a₀ = 256/(243√2) ≈ 0.7449 exactly (⟨000|z|100⟩ = −128/243), so bicone form × parabolic scale reproduces the Gordon number 768/(243√6) with no spherical radial integral. `SANDBOX-ONLY`
- **bicone-scaling** — Radial su(1,1) *is* bicone scaling: the ε-pairing (SU(2)-singlet) generators S±, S₀ close su(1,1) machine-verified, dilating T₀ → T₀ ± 1/2 while preserving the j₁ = j₂ gluing and l — between-shell and within-shell dynamics unified on one object. `SANDBOX-ONLY`
- **so42-casimir** — Can e² live in an SO(4,2) Casimir? **No**, for a precise structural reason: the Casimirs in hydrogen's representation are pure numbers (W₂ = 3, W₃ = 0, W₄ = −18) labeling the representation, and every e² > 0 gives the same irrep — e² is a coupling, not a representation label; the natural slot for it is a modulus, not a Casimir. `SANDBOX-ONLY`
- **so42-vector-scale** — SO(4,2) vector generators constructed: the algebra fixes |C|/a₀ to a specific pure number and [W_j, W_k] = 0 for W = V − U is proved from the commutators (W behaves as a position operator); the explicit number itself requires the Barut–Kleinert construction (supplied by parabolic-dipole). `SANDBOX-ONLY`
- **conserved-current** — Can 1/T² be derived from Gauss? Missing-ingredient verdict: the Gauss *form* is forced (a conserved central charge in the (X,Y,W) embedding gives a 1/T² shell field, verified), but no suitable conserved charge exists in the program's structures, and Jeremy's q_eff ∼ γY hypothesis fails quantitatively as a Gauss source; the minimal missing ingredient is named. `SANDBOX-ONLY`
- **u1-charge** — The charge hunt, continued: **confirmed with calibrations** — the Hopf fiber S¹ is a genuine U(1) already in the program's structures and sources an exact shell Gauss law (∮F = −2π, B_r = −1/(2T²)); the charge is topological and magnetic (the Dirac monopole bundle), static — a geometric home for a U(1) charge, not a dynamical derivation of Coulomb's law. `SANDBOX-ONLY`
- **stark-revivals** — Two threads: the bicone **exactly** reproduces the parabolic basis and Stark k-dependence (A_z = J_z^a − J_z^b eigenvalues = n₁ − n₂, counts n² at n = 2, 3, 4); Paper C's revival identity (A² = −ab·I₄ for the quantum generator) machine-verified. `SANDBOX-ONLY`
- **bloch-driver** — Bloch-sphere extension of the magnetic driver theory: the exact dictionary is that the cone is the PSD cone (rebit disk) — cone coordinates are the j = 1/2 state's (Tr ρ, Tr ρσ_z, Tr ρσ_x); supplies the state-space geometry the ledger's driver entries lack. (One inference in this note is corrected by rabi-y-driver.) `SANDBOX-ONLY`
- **rabi-y-driver** — "Rabi frequency equals Y": partially verified, partially **killed as stated** — Ω_{R,q} = |γ|B₁Y_q is exact, but "real symmetric H ⟹ edge dynamics live on the cone" is false (a real symmetric H generates a complex unitary and drives the state off the real disk); the fix is a basis rephasing / drive along J_y; the error is in the bloch-driver note's inference, not in ledger v13.595. Also flags a sign discrepancy in the ledger's Δ vs the standard rotating-frame derivation. `SANDBOX-ONLY`
- **ads2-cft1** — Does the program already contain AdS₂/CFT₁? The kinematic skeleton, not the correspondence: the cone is the AdS₂ embedding null cone and Paper C's su(1,1) discrete series is exactly the irrep ladder the JT Wilson-line calculus uses — but there is no Schwarzian dynamics, dilaton, or bulk↔boundary dictionary; the alphabet, not the language. `SANDBOX-ONLY`
- **rindler** — Rindler embedding hypothesis **false as stated**: fixed-X sections are spacelike, not observer worldlines; the true statement is sharper — the program's hyperbolas uv = +c² are the exact sign-flip mirror of Rindler's uv = −ρ², and the genuine Rindler structure (Bisognano–Wichmann modular flow) lives in the bulk wedges; a genuine connection, not an identity. `SANDBOX-ONLY`
- **twistor** — Spinor/twistor reading of the cone: what's standard is separated from what's new — real 2-spinors in 2+1 (Spin(2,1) ≅ SL(2,R), null ⟺ rank-1 spinor square), mini-twistor space TℂP¹; a claim/verdict table closes the note. `SANDBOX-ONLY`
- **twistor-bqf** — Twistor–BQF joint session: the discriminant-12 Fuchsian automorphs written in 2-spinor language and acted on the unit-shell spinors ξ_r (r ∈ {1,5,7,11}), machine-checked; narrow class number 2, genus character χ₁₂ = +1 on {1,11}, −1 on {5,7}. `SANDBOX-ONLY`
- **fuchsian-lorentz** — The arithmetic subgroup made explicit: 3×3 SO(2,1) matrices for the automorph group of x² − 3y² (Pell a² − 3b² = 1, Γ = {±M₀^k}), the precise classical identification, and the translation into Paper B's orbit language — every matrix machine-verified. `SANDBOX-ONLY`
- **music-12tet** — Is 12-TET a deep embedding of the program's mod-12 structure? The link decomposes into pieces none of which needs the cone — genuinely shared Z/12 group theory (including the multiplicative V₄ with Lewin inversion) plus standard transformational theory; a shared cyclic group, not a cone embedding. `SANDBOX-ONLY`
- **casimir-cutting-planes** — Casimir plates as cone cutting planes: the dictionary is real as far as it goes (plates ↔ parallel null planes X + T = u; patch area ∝ (u₂² − u₁²) with the same IR divergence structure) and clears its first quantitative bar — but the charge must be imported (the same obstruction as e² in a Casimir) and the physical-plane anchor is asserted, not derived; not a new route to α or the force. Report not to be updated until validated and Jeremy approves. `SANDBOX-ONLY`
- **screw-stations** — Suzuki screw × unit-circle dictionary: station-sampling the screw kernel at u_n = log n makes every Gram entry a function of a pair rapidity ψ_{n,k}; numerically the full station Gram (N=32) is positive (λ_min = 0.0, no negative eigenvalues) while the pole-only and prime-only pieces are separately indefinite — positivity is a property of the assembled kernel. `SANDBOX-ONLY`
- **unit-circle-secant** — Sandbox staging of the Airy-comb addendum to the diameter–secant machine: the neutron quantum bouncer's transition comb is computed from constants and Airy zeros alone (ν_1→7 = 1120.5 Hz, ν_2→9 = 1141.7 Hz, against the reported ~1120 / ~1142 Hz) — measured gravitational spectroscopy already has the (pure-number factor) × (scale) shape. `LEDGERED v14.592` (addendum; parent diameter–secant note LEDGERED v14.550)

## 12. Handoff-return and device explorations (2026-10-21–25)

- **bath-drift-coefficients** — Sandbox return to the v14.708 handoff: the hot-limit drift ⟨Ls⟩ = (5D₀T/2μq)(3q² − 1) derived from the deposited EFT v3.4 (not hand-fit), with the numerator attributed channel-by-channel (the "−1" comes entirely from the L-curvature drift via ⟨r²⟩) and an independent Hamilton–Modak route giving the identical absolute coefficient. `LEDGERED v14.710`
- **bath-joint-generator** — Joint (T, ε) bath generator, return to v14.713/v14.714: cross-covariance cancellation derived independently in (T, ε) coordinates (the note itself records that v14.714 holds deposited priority for the hot cancellation and Audit R334 for the escape answer; this work contributes the finite-temperature cross-covariance, an independent BESQ escape route, and the survival-conditioned ε marginal). `LEDGERED v14.716` (collision-aliased v14.717)
- **phase-response-operator** — Operator search, return to the v14.701 handoff: **negative** for an eccentric selector — the Gram defect vanishes uniquely at ρ = 1 (any Gram-native variational selector selects the *standard* theory), and the Favard/weight test obstructs exactly: the j=3 residual vanishes iff ρ = 1. `SANDBOX-ONLY` (prepared as the return to HANDOFF v14.701)
- **rotor-xi-feasibility** — Xi feasibility, return to the v14.700 handoff: bench numbers for the paraboloid-pair rotor G-meter (2 kg source at 0.10 m) — q/I_kin = 0.500 exactly at the design point (calibrating q as I_kin would bias Xi by a factor 2); quantum spectroscopy of the macro rotor is **not** a readout (negative sub-verdict); the classical torques sit 4–6 orders above torsion floors, so the design is not readout-limited. `SANDBOX-ONLY` (prepared as the return to HANDOFF v14.700)
- **gravity-monopole-pair** — Sandbox test (2026-10-21) of Jeremy's sketch (gravity as e's monopole partner): the EM pair locks α·α_m = 1/4 exactly, but the (e, G) pair as measured locks nothing small (α/α_G,e = 4.166e42 — if gravity is e's partner, the pair's "n" is the hierarchy itself); the shell Larmor phase budget partitions exactly into e-side (pointing) and G-side (holonomy) fractions. `SANDBOX-ONLY`
- **nut-pair-test** — Gravity's own dyon: Taub–NUT's (m, l) pair closes on **1/16**, by two independent routes that agree exactly — gravity's pair quantum is ħ/4, not ħ/2 (the SU(2)×U(1) Killing triad solved and verified symbolically). This is the quarter-lattice partner to EM's half-lattice; it is *not* the parabolic-grid interlay of v14.768 and does not derive it. `LEDGERED v14.731` (the exploration's note, updated and deposited on Jeremy's line)
- **larmor-pole880** — Finite-Larmor retarded Maxwell seat pole sweep, return to v14.880/v14.881: first converged finite-rotation complex poles of the causal Maxwell seat kernel, continued from v14.874's frozen pole; across the swept range the pole stays in the damped half-plane (rotation softens the mode; no upper-half-plane zero). `LEDGERED v14.884`
- **kepler-eft** — TeX drafts only (no prose note): the Kepler–oscillator EFT note ("Fast Phase, Slow Moment Map," v3.4 elevated hot benchmark) — drafts copied from Jeremy's Mac; the §5 averaged coefficients were left uncomputed in the note and are the subject of the eft-play and bath runs above. `SANDBOX-ONLY — uncharacterized (drafts only)`
- **label_only_dipole.py** *(loose script in explorations/)* — A standalone script with no accompanying note; not characterized. `SANDBOX-ONLY — uncharacterized (no note)`

---

*Draft assembled 2026-10-26 from the run/exploration notes themselves.
Deposit (ledger or research-notes) only on Jeremy's line.*
