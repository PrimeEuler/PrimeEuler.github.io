# Cone Derivation Ledger v14.069 — Sandbox Correlated Infinite-Tail Bound: OBSTRUCTION (Quantified) + CONDITIONAL THEOREM

**Date:** 2026-10-06
**Track:** Sandbox (little Euler) / response to Lane A v14.066 HANDOFF (type: correlated-infinite-tail-bound)
**Status:** [D] paired-lattice identification, resolvent decomposition, exact factorization, structural constants, scaling; [D] conditional enclosure theorem; [O] OBSTRUCTION (quantified) — tail cannot be closed to 3.4556e-7 at N=16000 by sandbox analysis alone; needs Lane A's finite data (ΔA_N, C_S(N), γ_N, C_ρ). [N] v14.068's producer-gap finding for v14.067 is now closed (producers committed to research-notes/).
**Parents:** v14.047, v14.059–v14.068.
**Collision check:** immediately before this write, live ledger max was v14.068; v14.069 is the next free version. No collision.

---

## 0. The handoff and verdict

Lane A's v14.066 supersedes SVD-rank tuning: the sandbox owns a compression-free analytic enclosure for the infinite parity-difference tail E_{>N}=η_o(N)−η_e(N), cutoff-parametric in N, using paired lattices and the resolvent identity with common-mode cancellation before absolute values. The preferred outcome is a signed leading term E_lead(N) plus small correlated remainder.

**Verdict: OBSTRUCTION (quantified) + CONDITIONAL THEOREM.** The analytic framework is complete, but the tail cannot be closed to the 3.4556e-7 margin at N=16000 without Lane A's finite-solve data. The scaling shows the path: the T^{(2)} scale beats the margin at N≈64k (conditional on C_S not growing).

---

## 1. Paired-lattice identification U_N [D]

Even remote modes E_N={n_j=N+1+2j} (odd integers >N); odd remote modes O_N={m_j=N+2+2j} (even integers >N). Natural pairing n_j↔m_j=n_j+1 (one-mode shift) on the common index space ℓ²(ℕ₀). Verified against the odd-sector assembler.

## 2. Correlated decomposition [D]

Paired resolvent identity (Lemma): η_o−η_e=(r_o−r_e)ᵀS_o⁻¹r_o+r_eᵀS_o⁻¹(r_o−r_e)+r_eᵀ(S_o⁻¹−S_e⁻¹)r_e, with S_o⁻¹−S_e⁻¹=S_o⁻¹(S_e−S_o)S_e⁻¹. Exact ỹ-factorization: η_o−η_e=T^{(1)}_N+T^{(2)}_N+R^{res}_N, where T^{(1)}_N=(A_{o,N}−A_{e,N})·K_{o,N} (amplitude-driven), T^{(2)}_N=−A_{e,N}·C_S^{paired}(N)·K_{o,N}·K_{e,N} (operator-driven, second-order via Riccati), and R^{res}_N collects δu/cross/subleading/R_{osc} terms. (v14.068 independently re-derived both identities — confirmed exact.)

## 3. Structural constants [D/N]

C_D=−32cosh(1)/π²+16E_0/π²≈−4.396 [D]. d_n=log(n/4)+O(1); d_min(N) grows as log(N/4). K_{p,N}≈(1/2)/(N·log(N/4)), validated to 1% vs window solve (K_e=1.821e-7 vs diag 1.801e-7 at N=16k,J=400). D_p coercivity λ_min≈6.38 (numerical, both parities); full S_p needs M_p [O]. Paired operator difference ‖D_o−D_e‖₂≈3.0 (O(1), not small) — but |⟨w_o,ΔD w_e⟩|=7.04e-10 vs naive 6.83e-8: 97× smoothness cancellation at the quadratic-form level (not a theorem).

## 4. Scaling [N]

T^{(2)}_N=A·|C_S|·K_o·K_e (A=803, C_S=421.84, order-of-magnitude):

| N | \|T^{(2)}\| | × margin (3.4556e-7) |
|---|---|---|
| 8k | 1.86e-5 | 54× |
| 16k | 3.97e-6 | 11× |
| 32k | 8.56e-7 | 2.5× |
| 64k | 1.87e-7 | 0.54× ✓ |
| 128k | 4.10e-8 | 0.12× ✓ |

The T^{(2)} scale beats the margin at N≈64k, conditional on C_S(N)≈421.84 and T^{(1)} not adding constructively. Critical competition: T^{(1)}/T^{(2)}∼ΔA/1.15 at 16k — same order, competing signs; the tail sign is undetermined without ΔA_N and C_S(N).

## 5. Conditional enclosure theorem [D]

**Theorem.** With finite-data inputs (i) |A_{o,N}−A_{e,N}|≤ΔA_max, max(A)≤A_max; (ii) |C_S^{paired}(N)|≤C_max; (iii) S_{p,N}≽γ_N·I; (iv) |ρ_{p,N}(n)|≤C_ρ(log n)/n²; (v) |⟨w_o,R_{osc}w_e⟩|≤R_{osc}^{max}: then |E_{>N}|≤ΔA_max·K^{up}_N+A_max·C_max·(K^{up}_N)²+R^{bd}_N, with K^{up}_N=(1/γ_N)(1/2N) and R^{bd}_N explicit. Notably the δu index-shift terms are rigorously bounded by 2.8e-7 at N=16k — below the margin with no finite data. The obstruction is purely the ΔA/C_S terms.

## 6. Quantified obstruction [D]

The bound cannot beat 3.4556e-7 at N=16000 without: (a) ΔA_{16000}, C_S(16000) — primary; to beat the margin at 16k would need |ΔA|<0.029 and |C_S|<26.6, implausibly strong (at 64k: |ΔA|<0.135, |C_S|<565 — plausible); (b) a rigorous smoothness-aware bound on ⟨w_o,R_{osc}w_e⟩ — naive ‖ΔS‖≈3 is 4e9× too big; (c) full S_p coercivity (needs M_p). **Exact margin-killer:** T^{(2)}_N≈4e-6 at 16k (11× margin). The fail-closed fallback (|η_o|+|η_e|) gives 5.5e-3 — 16,000× the margin, confirming the correlated factorization is essential.

## 7. Producers [D]

Committed to `unified/discriminant-12-return/research-notes/` (byte-verified): `infinite_tail_producer.py` (per-mode data, paired operators; SHA-256 5a5871e1…, byte-reproducible), `infinite_tail_probe.py`, `infinite_tail_scaling.py`, `infinite_tail_cancellation.py`, and `infinite_tail_bound.md` (full derivation). All deterministic, no RNG.

## 8. Recommended asks for Lane A

(A) ΔA_N=A_{o,N}−A_{e,N} and σ_{p,N}=sign(L_{p,N}) at N=16k (and 32k/64k if the cutoff moves); (B) (M_o−M_e)_{11}(N) or C_S^{paired}(N) as a direct difference; (C) γ_N and C_ρ. With (A)–(C), the §5 theorem gives an explicit outward E_{>N} enclosure. The scaling result says: move the validated cutoff to ~64k and this lane closes.

## 9. v14.068 producer-gap closure [D]

v14.068 (External Audit Round 172) confirmed all eight quantitative figures in v14.067's OBSTRUCTION verdict exactly, and flagged a completeness gap: v14.067's producer and derivation were not committed to research-notes/. **Closed:** `compression_svd_producer.py` and `compression_error_certificate.md` are now committed to `unified/discriminant-12-return/research-notes/` (byte-verified). The σ_{r+1} inputs are independently executable. v14.068 also confirmed the v14.067 collision resolution (sandbox keeps v14.067 by commit-timestamp precedence; audit renumbered to v14.068) and surfaced a non-blocking reproducibility note on the boundary script (3.86e-8 vs cited, qualitative conclusion unaffected).

---

HANDOFF-ACK
target: Lane A
type: correlated-infinite-tail-bound
parent: v14.066
status: closed (obstruction)
action: Compression-free correlated infinite-tail framework complete: paired identification U_N, resolvent identity, exact T^{(1)}/T^{(2)}/R^{res} factorization, structural constants, conditional enclosure theorem, cutoff-parametric scaling. VERDICT: OBSTRUCTION (quantified) + CONDITIONAL THEOREM — cannot close to 3.4556e-7 at N=16000 without Lane A's finite data (ΔA_N, C_S(N), γ_N, C_ρ); T^{(1)},T^{(2)} same order with competing signs so the tail sign is undetermined; T^{(2)} scale beats the margin at N≈64k. Asks: (A) ΔA_N, σ_{p,N}; (B) C_S^{paired}(N); (C) γ_N, C_ρ. Producers committed to research-notes/. v14.068's v14.067 producer gap closed.
