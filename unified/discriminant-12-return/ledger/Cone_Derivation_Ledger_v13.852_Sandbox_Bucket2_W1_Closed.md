# v13.852 — Sandbox Bucket 2: W1 closed — remnant-inclusive transported profile

**Date:** 2026-09-28
**Lane:** Sandbox (our Lane B — Jeremy's exploratory track under LIttle Euler; disambiguated from the ledger's dormant norm-quotient Lane B)
**Status:** [I]/[O] — sandbox re-derivation, not certified
**Entry kind:** resolves v13.851's WALL W1 by re-deriving v13.740 §4's transported profile remnant-inclusive
**Supersedes:** v13.740 §4's pure profile (as the applicable transported profile; the pure special case stands as the α=β=0 instance)
**Refines:** v13.743 §9 (determines B_{0.48,0,±}, which §9 left undetermined)

**Headline: W1 CLOSED.** The remnant-inclusive transported profile is cleanly derived at source level (v13.740 §4's object): ψ∞(ξ) = e^{−ξ} − 0.47·1_{ξ>0} — the pure i(e^{−ξ}−δ_0) plus an additive half-line constant −0.47. The remnant boundary functional B_{0.48,0,±} is determined as a δ_0-free half-line constant; functional independence is proved analytically and quantified numerically (pure-only fit leaves 97.7% residual; two-shape fit exact at 2×10^{−15}); the normalization question is answered (exists, but the limit is two-shape — v13.740's hedge strengthened and repointed at the remnant-inclusive source theorem).

---

## 1. The re-derivation (v13.740 §4's object, remnant-inclusive)

The §4 object transports the **source** (not the solution). From the (8.5)-LS solver (posted `lsq85.py`, natural BCs, N=120, λ=0), the finite-A source is s(x)=e^x+A_coef x+B_coef. Edge transport ξ=A−x with e^{−A} normalization is **exact algebra** (no discretization of the affine part): the derivative-transported source (the §4 object) is ψ_A(ξ)=e^{−ξ}+A_coef e^{−A}.

| A | c₂ (ξ-coeff of s_A) | c₃ (const of s_A) | d₂ (const of ψ_A) | ledger α_A | ledger β_A |
|---|---|---|---|---|---|
| 2 | +0.4723 | −0.171 | −0.4723 | +0.202 | −0.641 |
| 3 | +0.4784 | −0.145 | −0.4784 | +0.379 | −0.253 |
| 4 | +0.4691 | −0.036 | −0.4691 | +0.432 | −0.147 |
| 5 | +0.4695 | −0.002 | −0.4695 | +0.456 | −0.079 |
| 6 | +0.4741 | −0.051 | −0.4741 | +0.469 | +0.016 |

(Fit windows ξ∈[0.3,3]; the A=6 c₃ wobble is the known fixed-N noise, cf. v13.849.) The remnant coefficient is **stable at 0.47±0.01 from A=2**, consistent with α∞=0.48 (v13.844 R3); the ledger's α_A (v13.743 §11) climbs 0.20→0.47 toward the same value — the two differ only by the conventional 2e^{−A} from the I_1+C_A bookkeeping, vanishing as A→∞. (Sign of the ξ-term differs by convention between the direct fit and v13.743 §11; magnitudes agree at 0.47–0.48.)

**R2 is load-bearing for W1's existence.** c₃→0 (−0.17→−0.002) **is** the L_0+L_1=0 cancellation at source level (β_A=−e^{−A}[A(I_1+C)+I_0+C], v13.844); without it, c₃ would grow ~A and **no** finite e^{−A}-normalized profile would exist.

## 2. B_{0.48,0,±} determined (refines v13.743 §9 without contradicting it)

v13.743 §9 left B_{α,β,±} as "a boundary/domain functional which cannot be determined by the twice-differentiated interior equation alone." The R1 asymptotics determine it: the affine −0.48ξ is **continuous at ξ=0** (value 0), so derivative transport produces **no δ_0** — just the half-line constant: **B_{0.48,0,±} = (channel factor) × (−0.47)·1_{ξ>0}, no δ_0.** The δ_0 in the pure profile comes solely from the exponential's edge jump — a clean separation. §9's interior claim stands; the (8.5) affine asymptotics (the §11 gate) fix what the interior equation cannot.

## 3. Functional independence: proved and quantified

**Analytic (convention-free).** In the Laplace domain (Re p>0, v13.774 §4): the pure compensated term 1/(1+ik)−1 is **analytic at k=0** (value 0); the remnant is −α/(ik)²=+α/k², a **double pole**. A scalar multiple of an analytic-at-zero function is analytic at zero — never a double pole. Hence **no** N_A-style scalar normalization can absorb the remnant. At solution level: if S_{edge} is injective, S_{edge}^{−1}s_{rem}≠0 and it is not a scalar multiple of q^{pure} — the two-shape limit is structural, using only linearity + injectivity, no Green details. (Injectivity is part of the same limiting-H(S_{edge}) source theorem v13.740 already hedged on; no new assumption.)

**Numeric.** Two-shape fit ψ_A=d_1e^{−ξ}+d_2: relative residual ~2×10^{−15} (exact — ψ_A is analytically two-shape). Pure-only fit ψ_A=d_1e^{−ξ}: relative residual **0.974–0.979**. Quantified independence.

## 4. Normalization verdict

**Exists, but the limit is two-shape.** The e^{−A} normalization still gives finite nonzero limits (d_2≈−0.47 bounded, c_3→0 — no new divergence; R2 guarantees it). But N_A normalizes scale, not shape: the scalar c_A in P_A=c_A T_{pair}(1+o(1)) cannot absorb a shape distortion (§3's argument). The R_A/Δ_A tests (v13.740 §§5–6) survive **as tests**, but their target must be the distorted P∞ — which is W2's reformulation task. **v13.740's hedge is strengthened and repointed:** the limiting H(S_{edge}) source theorem must now be proved for the **remnant-inclusive** source, and N_A re-derived from the two-shape limit. The v13.774 convention caveat was respected throughout (invariant 2D boundary trace data never reallocated between B_A^{bdry} and R_{A,−}).

## 5. Residual boundaries (not W1 blockers)

1. **q-level explicit form.** S_{edge}^{−1}B_{0.48,0,±} is characterized structurally (nonzero Green potential of a half-line constant, independent shape) but not in closed form — S_{edge}'s explicit Green structure is in none of the ledger sections read or the posted scripts. In k-space the remnant enters v13.774 §5 as the constant k²B_A^{bdry}→0.48 — the bridge to W2.
2. **Solution-side transport does not settle at A≤6.** e^{−A}(dv/dx)(A−ξ) shows a boundary spike (−25.4 at ξ=0, A=5) plus interior oscillations — the v13.743 §10 e^A-scale boundary mass manifesting. This confirms the ledger's architecture: work at the source/edge-equation level, do not transport v directly. Downstream-relevant (W2/W3).

## 6. Verdict against the pre-registered rule

**W1 CLOSED.** Remnant-inclusive transported profile cleanly derived; B_{0.48,0,±} determined as a δ_0-free half-line constant; independence proved analytically and quantified numerically; normalization question answered. The δ_0 belongs to the pure exponential's edge jump only.

## 7. Provenance

- Run: `~/workspace/d12/lane_b/sandbox/runs/20260928-225734-bucket2-w1-remnant-profile/` (report.md, STATUS.md; scripts: `scripts/w1_source_profiles.py`, data: `w1_source_profiles.json`, `profiles_A5.npz`; edge-transport step is exact algebra on (A_coef,B_coef) from posted `lsq85.py`/`screw.py`, natural-BC run 20260928-165927)
- Ledger sections read in full: v13.740 §4 (+§§5–6), v13.743 §§9–11, v13.757 §3, v13.774 §§4–5, v13.851 §§1–4
- Mid-course correction logged: first attempt profiled v (the solution); caught from the fits, restarted on the source — the right object per R3/§4
- All conditional on λ_a>0 (v13.848). No positivity/RH/Hilbert–Pólya claim; prime ramp untouched.
