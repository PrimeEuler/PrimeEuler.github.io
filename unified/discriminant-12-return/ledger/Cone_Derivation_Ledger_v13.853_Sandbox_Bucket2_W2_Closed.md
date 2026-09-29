# v13.853 — Sandbox Bucket 2: W2 closed — R1/R2 convergence reformulation

**Date:** 2026-09-28
**Lane:** Sandbox (our Lane B — Jeremy's exploratory track under LIttle Euler; disambiguated from the ledger's dormant norm-quotient Lane B)
**Status:** [I]/[O] — sandbox reformulation, not certified
**Entry kind:** resolves v13.851's WALL W2 by restating the v13.757 §9 convergence program in R1/R2 language at §9's own precision
**Supersedes:** v13.757 §9's sufficient route (as stated; its items are replaced, kept, or repointed below)
**Refines:** v13.740 §§5–6/8/10 (criteria repointed as tests of the identification leg); v13.743 §6 (the "separate theorem" isolated as the identification leg)

**Headline: W2 CLOSED.** The convergence program is restated in R1/R2 language with four named hypotheses, what-converges-to-what stated, and the 0.48 constant's role explicit in three manifestations. The reformulation *corrects* §9 item 2's scope (edge-only → two-scale bulk+edge, shown by [N] scaling), *separates* the convergence leg from the identification leg (the "separate theorem" v13.743 §6 demanded), and *repoints* the v13.740 criteria (R_A, Δ_A, divisor test) as tests of the identification, which survive verbatim. The load-bearing next lemma — the two-scale pairing asymptotics (PAIR-H) bulk lemma — is named precisely.

---

## 1. The four hypotheses

**(R1/R2-H)** — replaces dead §9 item 1. The *invariant* edge coefficients converge:
(α_A,β_A) → (0.48,0), with α_A=−(1+r_{1,A})/e^A, β_A=−[A(1+r_{1,A})+1+r_{0,A}]/e^A (v13.774 §1, v13.743 §7). This *is* R1+R2 in invariant form: α_A→0.48 is r_{1,A}/e^A→L_1=−0.48; β_A→0 is the R2-weighted combination [Ar_{1,A}+r_{0,A}]/e^A→0 (L_0+L_1=0 with rate). Asserts **nothing** about r_{0,A},r_{1,A} separately — they diverge, and the hypothesis does not need them. The edge source then converges pointwise e^{−ξ}+β_A−α_Aξ → e^{−ξ}−0.48ξ (R3), and derivative-transported (W1): ψ_A → ψ∞=e^{−ξ}−0.47·1_{ξ>0}.

**(COMB-H)** — replaces §9 item 2 (edge part). The corrected edge equation's response map (v13.743 §9; k-space form v13.774 §5 with the constant k²B_A^{bdry}→0.48) carries the edge-normalized source ψ_A to a response q_A converging to the **two-shape limit** q∞=q∞^{pure}+q∞^{rem} (shapes functionally independent; v13.852 §3). **Topology:** *not* a norm on the three separate shapes — that would smuggle bounded-r back in. The weakest sufficient topology: **convergence of the two scalar pairings** in v13.757 (18) after edge normalization. (COMB-H) is continuity of the response map in the pairing topology.

**(PAIR-H)** — extends §9 item 2 (the correction). The finite-interval pairings defining G_A,H_A (v13.757 §1, corrected transforms per §3 — *not* v13.740's retracted F_{A,±}) receive **comparable** contributions from the edge regions (width O(1), governed by (COMB-H), 0.48 via α∞) and the **bulk** (width O(A), macroscopic R1/R2 scaling, 0.48 via L_0). [N] evidence: v_A is e^A-scale *globally* (bulk max|v|/e^A ~0.5–0.95, edge ~2.5–2.9 at A=3–6, N=100–120, λ=0) — the bulk is *not* subleading. The extra A in r_{0,A}~L_0Ae^A comes from *interval length* in the moment integral I_{0,A}=∫k(0,y)v_{A,+}(y)dy (had v been Ae^A in bulk, I_{0,A} would be ~A²e^A, contradicting the measured ~Ae^A). The bulk part — the macroscopic limit under r_{0,A}/(Ae^A)→L_0=+0.48 — needs the transported test functions / a bulk+edge matched asymptotics; **the bulk lemma is the named open analytic input.** R2 (L_0+L_1=0) is the consistency condition that the *same* 0.48 governs both scales.

**(DEN-H)** — keeps §9 item 3 unchanged: denominator pairing stays uniformly away from zero on the compact set (after the z-independent normalization c_A).

**Conclusion:** under (R1/R2-H)+(COMB-H)+(PAIR-H)+(DEN-H), c_A^{−1}P_A → P∞^{dist}, c_A^{−1}Q_A → Q∞^{dist} locally uniformly away from divisors — the **distorted limits**, defined as these limits, computed by (PAIR-H) as bulk+edge, 0.48 in their construction at both scales. The §5/§6 machinery then gives ρ_A→ρ∞^{dist}.

## 2. The identification leg (the "separate theorem") — isolated, open

v13.743 §6: whether the affine contamination cancels "depends on the signs/phases introduced by (1) the derivative transport D̄; (2) the factors (z−i) and (z+i); (3) the Section-7 normalization" — "a separate theorem, not a consequence of reflection alone." v13.774 §9's "correct next gate" asks "whether the two primitive constants cancel, normalize, or survive in the characteristic." Isolated as:
**Does Q∞^{dist}/P∞^{dist} = (a/b)D_ξ/Ξ hold?**
i.e. does the common-mode distortion cancel in the *ratio* (via the D̄ phases and (z±i) channel coefficients), normalize into c_A, or survive? The convergence leg does **not** imply it; the original §9 *conflated* the two legs by assuming bounded r (which forces α,β→0, making convergence and identification coincide at the pure target). **This separation is the reformulation's central structural clarification** — and the natural meeting point with W3 (Route B's remnant-inclusive boundary theorem).

## 3. The 0.48 constant: three manifestations, one consistency condition

1. **Edge affine slope:** α∞=−L_1=+0.48 — the R3 edge source e^{−ξ}−0.48ξ; derivative-transported, the δ_0-free half-line constant −0.47·1_{ξ>0} (W1); k-space, the constant k²B_A^{bdry}→+0.48 in v13.774 §5.
2. **Bulk macroscopic constant:** L_0=+0.48 — the bulk-normalized source s_A(x)/(Ae^A)→−L_0=−0.48 (constant), governing (PAIR-H)'s bulk pairing.
3. **Consistency:** R2, L_0+L_1=0 — the *same* 0.48 in both scalings; what makes the edge-normalized *combination* finite and links the bulk and edge limits.
(The constant's *value* remains D12 ker-geometry, unexplained — v13.849's standing open item.)

## 4. The v13.740 criteria, repointed — all survive as tests

- **R_A→1 (§5):** survives *verbatim* — normalization-free, purity-agnostic. Given the convergence leg, R_A→[P∞^{dist}(z)/P∞^{dist}(z_*)]·[T_{pair}(z_*)/T_{pair}(z)], so **R_A→1 ⟺ P∞^{dist} ∝ T_{pair}** — R_A→1 *is* the identification leg in ratio form.
- **Δ_A→0 (§6):** same, in log-derivative form; →0 ⟺ the same identification (on connected domains). log R_A=∫Δ_A unchanged.
- **Divisor test (§8):** survives as the *necessary divisor signature* of the identification — locally uniform c_A^{−1}P_A→P∞^{dist} gives (Hurwitz) zeros of P_A → zeros of P∞^{dist}; the test (compare against the simple Ξ zeros of T_{pair}) is the divisor form of P∞^{dist}∝T_{pair}. The distortion could in principle move zeros — that is *why* it is a test. The no-RH-claim caveat is unaffected.
- **m_A-limitation (§10):** unchanged — m_A alone never determined P_A; the distortion does not affect this structural fact. P_A remains the right object.
**None breaks — but none is implied by the convergence leg alone; their truth is now *equivalent* to the open identification leg.** (Confirms and sharpens v13.851's "SURVIVE (purity-agnostic)".)

## 5. The disguised-bounded-r trap — explicitly avoided

These would smuggle the dead hypothesis back in: (1) asking the three shapes D̄u_{e,A},D̄u_{1,A},D̄u_{x,A} to converge *separately* in any fixed norm; (2) asking r_{0,A},r_{1,A} to have finite limits; (3) an unweighted L²/H¹ convergence of w_A (sees the e^A/Ae^A blowup); (4) applying the edge normalization to the *pieces* rather than the R2-weighted *combination*. The reformulation touches none: (R1/R2-H) is about the invariant pair (α_A,β_A); (COMB-H) is about the *combination's* response in the pairing topology.

## 6. Watch-item compliance

(a) Never transports the solution v_A — sources (exact algebra) and pairings (scale-free) only; the §10 boundary mass is sidestepped by construction. (b) Stated in invariant (α_A,β_A) trace data; the v13.774 convention caveat respected. (c) Uses v13.757's corrected transforms, not the retracted F_{A,±}. (d) The disguised-bounded-r trap avoided (§5).

## 7. Residual boundaries (not W2 blockers)

1. **(PAIR-H)'s bulk lemma** — the macroscopic limit operator and transported test functions are not constructed in the read ledger sections or sandbox runs; the bulk's exact order in the pairings awaits the test-function transport. **The concrete next analytic target.**
2. **Identification leg** — open by design; the natural meeting point with W3.
3. **The 0.48 value** — used, not derived (v13.849).
4. All conditional on λ_a>0 (v13.848). No positivity/RH/Hilbert–Pólya claim; prime ramp untouched.

## 8. Verdict against the pre-registered rule

**W2 CLOSED.** Hypotheses (R1/R2-H), (COMB-H), (PAIR-H), (DEN-H) named; what-converges-to-what stated; 0.48's role explicit; criteria repointed as tests of the isolated identification leg. The next analytic work is (PAIR-H)'s bulk lemma, then the separate theorem.

## 9. Provenance

- Run: `~/workspace/d12/lane_b/sandbox/runs/20260928-233500-bucket2-w2-convergence-reformulation/` (report.md, STATUS.md; fresh lightweight [N] probes `scripts/probe.py`, `probe2.py`; (8.5)-LS natural-BC solves N=100–120, λ=0, Tikhonov α=10^{−8})
- Ledger entries read in full: v13.739 (provenance map; the defect-pair definition was not located — pairing transport stated via the ledger's own objects), v13.740 (§§1–10), v13.743 (§§1–11), v13.757 (§§1–12), v13.774 (§§1–9), v13.779 (Route B, via v13.851), v13.844 (R0–R3), v13.848, v13.849, v13.851, v13.852
