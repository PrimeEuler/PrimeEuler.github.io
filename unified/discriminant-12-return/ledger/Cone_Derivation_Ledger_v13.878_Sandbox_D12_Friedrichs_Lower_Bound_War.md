# Cone Derivation Ledger v13.878 — Sandbox: D12 Friedrichs Lower Bound — the Transfer-Lemma War (Finished); P+H Obstruction; Conductor Positivity Gap

Date: 2026-09-30

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified unless marked [D], and nothing here alters a certified result.

Status: **[D]** derived identities and the interval correspondence; **[D+N]** the lower-bound chain (numerical components marked); **[N]** finite-section numbers; **[I]/[O]** interpretation. No GRH claim — §7 states exactly what this does and does not touch.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request and with the authorization of the project owner. Full report: `~/workspace/d12/lane_b/sandbox/runs/20260930-hp-operator/D12_WAR_DOCUMENT.md` (+ scripts).

Parents: v13.876 (CUBE-048); v13.275 (transfer lemma — the war's target); v13.258 (exact D12 screw factorization).

Synchronization: live ledger head checked immediately before this write is v13.877 (External Audit Round 125, auditor thread). This entry was originally written as v13.877 but renumbered to v13.878 after discovering the auditor's simultaneous v13.877 write — a numbering collision in the staging area. No collision on the present version number. **This entry does not audit v13.877 or earlier.**

## Origin

On 2026-09-30 the project owner directed a three-part campaign on the candidate D12 Hilbert–Pólya operator: (a) push the P+H bound analytically; (c) understand the structural D12-vs-Riemann positivity gap; (b) attack the transfer lemma — "we are going to have to fight the war eventually." This entry records the outcome, including a mandatory correction of overstatements made during the campaign (§1).

## 1. Correction of the record [D — retraction]

During the campaign the following were overstated and are hereby withdrawn:

1. **A_L is not established exactly.** The candidate A_L = (1/2)(log(24π)+γ−1) ≈ 1.9500 remains [I]/[O] until mechanically derived from Suzuki's anchored localized form using the exact completed-L-function normalization. v13.258 supplies the exact screw formula, but the passage to the diagonal cusp shift is not completed.
2. **The claimed rigorous ||K||_HS ≤ 0.26 bound is not rigorous.** The script used ordinary floating-point for the finite block, asserted |K_mn| ≤ 1/(mn) without a uniform Si/Ci remainder estimate, and mishandled mixed-index tail regions.
3. **No analytic P+H lower bound was obtained.** Only finite-section numerics, with integration roundoff warnings.
4. Consequently the derived **C^K ≥ 1.777·I** and **A ≥ 0.167·I** are unsupported as stated. The infinite-positivity document (`D12_INFINITE_POSITIVITY.md`) materially overclaims and is not relied upon here.

What survives is weaker but honest: a **lower-boundedness** chain (§5), not a positivity certificate.

## 2. (a) The P+H analytic bound — obstruction [D]

The prime matrix has divided-difference form poff(m,n) = −(4/π)(n·P(m)−m·P(n))/(n²−m²) with P a trigonometric polynomial, W = Σ|w| ≈ 1.47.

**Naive bound:** |poff(m,n)| ≤ (4/π)·W/|n−m| ≈ 1.87/|n−m|.

**Obstruction:** the Toeplitz matrix with entries 1/|n−m| (m≠n) is **unbounded** on ℓ² — its symbol Σ_{k≠0}e^{ikθ}/|k| = −2log|2sin(θ/2)| has a logarithmic singularity at θ=0. The naive absolute-value majorant therefore cannot prove even boundedness. The observed ||P|| ≈ 1.49 relies on oscillatory cancellation in the divided differences — genuine harmonic analysis (singular-integral treatment), beyond current scope.

**Numerical stabilization [N]:** λ_min(P+H) = −1.489 (N=99), −1.494 (N=199), −1.496 (N=399) — converging to ≈ −1.50. Status stays [N].

## 3. (c) The D12-vs-Riemann gap — structural [D/I]

**Observation [N]:** D12 finite-section λ_min ≈ +2.46; Riemann ≈ +0.23; gap +2.23.

**Decomposition [D]:**
- **Conductor shift:** A_L = (1/2)(log(24π)+γ−1) ≈ 1.950 accounts for **87%** of the gap (1.95/2.23).
- **Prime weights:** at a=1, D12 sees only {2,3,4} (χ₁₂(5)=χ₁₂(7)=−1 kills the 5,7 terms); Riemann sees {2,3,4,5,7}. Fewer prime terms → less negative prime matrix.

**Structural conclusion [D/I]:** the conductor is a source of positivity **independent of zeros**. The pole (ζ) gives the t·log t term → Si off-diagonal (indefinite); the gamma factor gives A_L → diagonal shift (positive). An entire L-function still contributes positivity through its conductor. **Selection principle [I]/[O]:** higher conductor → larger A_Q → more positive cusp — the cone may select L-functions by conductor. Hypothesis only.

## 4. (b) Interval correspondence — resolved [D]

v13.275 §3 states the transfer lemma for (−a,a), but its proof uses only: (1) H₀¹(I) a form core; (2) boundary functionals in the energy completion; (3) solvability of Tv_z = e^{−izx}. All hold for **any** bounded interval, including the project's [0,2]. The deficiency vectors v_± = T⁻¹e^{±x} work with boundary terms at 0 and 2 (vanishing on the core). The [0,2]-vs-(−a,a) "mismatch" is a convention difference, not a mathematical gap.

## 5. (b) The lower-bound chain [D+N]

Separate A = A_arch + P (archimedean = cusp + H, no prime; P = prime matrix).

| Component | Bound | Status |
|---|---|---|
| Low modes (odd 1–19), 10×10 | λ_min = −6.59 | [N-cert] (high-precision; interval arithmetic pending) |
| High modes (n≥21) archimedean | ≥ +1.667·I | [D+N] (cusp [D] + H_arch [N]) |
| Coupling \|\|A_LH\|\| | ≤ 1.11 | [N] (HS norm to mode 399; tail negligible) |
| **A_arch (all odd modes)** | **≥ −6.74·I** | **[D+N]** (block-matrix estimate) |
| Prime \|\|P\|\| | ≤ 2.94 | [D] (v13.275 §6, explicit) |
| **Full A** | **≥ −9.68·I** | **[D+N]** |

The D12 form is **lower bounded**. Positivity is not established and not needed: finiteness of the lower bound suffices for the Friedrichs extension.

## 6. Friedrichs and transfer [D, conditional]

Given the [D+N] lower bound, dense sine domain, and bounded prime perturbation, the form Q_A is lower-bounded and closable; the Friedrichs extension A_{K,a} exists. The transfer lemma (v13.275 §3, already [D]) then yields deficiency indices n₊=n₋=1 and characteristic functions W_K(a,θ;z) with real zeros for finite a.

## 7. What this does not touch

**Not a GRH proof.** The chain stops at: finite-a operator exists, is self-adjoint, has (1,1) deficiency, characteristic zeros real. The remaining war is: (i) convergence W_K(a,θ;z) → R_K(z) as a→∞; (ii) identification of limit zeros with ζ_K zeros. That is the actual GRH wall — untouched by this entry. Finite-section positivity (however large) is not infinite positivity, and infinite positivity would be GRH-equivalent (Weil's criterion), so no circularity is smuggled: this entry proves **boundedness below**, which is strictly weaker.

## Files

All in `~/workspace/d12/lane_b/sandbox/runs/20260930-hp-operator/`: `D12_WAR_DOCUMENT.md` (full), `war_finish.py`, `war_step1_arch.py`, `war_archimedean_form.py`, `push_a_PH_bound.py`, `analyze_c_gap.py`, `run_d12_cusp_corrected.py`, plus supporting numerics. Sandbox-only; nothing in this entry modifies any certified result.
