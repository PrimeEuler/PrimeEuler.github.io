# Cone Derivation Ledger v13.912 — Sandbox de Branges Odd-Sector Question: Is 0 in the Spectrum of L_A^{(-)}?

Date: 2026-10-01

Author: LIttle Euler (sandbox track). Authorization: project owner, 2026-10-01 ("lets ledger the parked de Branges odd-sector question").

Predecessors: ledger v13.757 (feedback ratios r_{0,A}, r_{1,A}; sufficient criteria for the de Branges operator limit), v13.758 (the moment system M_{00}, M_{1x}, M_{0e}, M_{1e} and the boundary-functional obstruction). Sandbox reports: `debranges_scope.md` (scoping study, §5.1 proposed the gate), `r_ratios_gate.md` (the gate expedition — first ledger record of its verdict is this entry). This material has not appeared in the ledger or the audit thread before.

Status: **[D]** for the analytic identity (§3) and the sign-convention verification; **[N]** for the gate numerics (divergence, near-null modes, λ-independence); **[O]** for the invertibility question itself and the proposed follow-ups. No RH/GRH claim — this is finite-interval operator theory. Sandbox scope only.

## 1. The question, precisely stated [O]

Let L_A be Suzuki's finite operator on (−A, A) with kernel k(x, y) = g(x−y) − λN(x, y) at λ = −1, and let L_A^{(−)} be its restriction to the odd sector (odd functions). **Is L_A^{(−)} boundedly invertible on L² — equivalently, is 0 ∉ σ(L_A^{(−)})?**

This is **parked, not closed**: a precisely posed operator-theoretic question, with an analytic identity on one side and divergent numerics on the other, and no resolution yet. It is upstream of everything in v13.758's moment system: that system *assumes* the odd inverse R_A^{(−)} = (L_A^{(−)})^{−1} exists boundedly. If 0 ∈ σ(L_A^{(−)}), the odd moments M_{1x}, M_{1e} — and hence the feedback ratio r_1 = M_{1e}/(1+M_{1x}) — may not exist as formulated, and the r_1 = o(e^A/A) half of the v13.757 convergence gate cannot even be posed, let alone tested.

## 2. Where the question came from [N]

The de Branges scoping study (`debranges_scope.md`, Jeremy-authorized 2026-10-01) proposed a falsifiable numerical gate on the ledger's operator-limit program: evaluate the feedback ratios r_{0,A} = M_{0e}/(1+M_{00}) and r_{1,A} = M_{1e}/(1+M_{1x}) at increasing A and test the sufficient criteria r_{0,A} = o(e^A), r_{1,A} = o(e^A/A) from v13.757 §10. Jeremy authorized dispatching it immediately ("its running long so lets go ahead and dispatch that now"). The expedition (`r_ratios_gate.md`, P1 Galerkin, λ = −1, sign convention re-verified [D] against Suzuki v2 §§8.2–8.3 directly) returned an **AMBIGUOUS** verdict — and the ambiguity is the subject of this entry.

The even half is healthy [N]: |r_0| ~ e^{0.92A} over A = 0.5…5 (local exponential rate declining 1.06 → 0.87; |r_0|/e^A peaking at 0.128, declining to 0.098), d_0 = |1+M_{00}| ∈ [0.85, 0.99] bounded away from zero, moments converging under N-refinement. Weak GO for r_0 = o(e^A), thin margin, sieve-capped at A ≈ 5.7. The odd half is the problem.

## 3. The analytic identity [D]

**Identity.** If u = L_A^{−1}x exists in L² (odd sector), then M_{1x} := ℓ_1(u) = 1 exactly, where ℓ_1(v) = ∫k_x(0,y)v(y)dy.

*Proof.* L_Au = x means F(x) := ∫k(x,y)u(y)dy = x for all x. Differentiating under the integral (dominated convergence; g Lipschitz on compacta, ∂_xN bounded) gives F'(x) = ∫k_x(x,y)u(y)dy, hence at x = 0: M_{1x} = ℓ_1(u) = F'(0) = 1. ∎

So **bounded invertibility of the odd sector implies M_{1x} = 1 exactly** — a sharp, parameter-free prediction the numerics can be held to.

## 4. The numerical evidence against [N]

Odd-sector moments at A = 2 under N-refinement (400 → 800 → 1600 → 3200):

| N | M_{1x} (analytic: 1) | M_{1e} |
|---|---|---|
| 400 | 28.5 | 21.8 |
| 800 | 45.6 | 35.8 |
| 1600 | 74.3 | 59.2 |
| 3200 | 123.6 | 99.3 |

**Diverging ~ N^{0.7}, two orders of magnitude above the analytic value, with no sign of turning.** The discrete odd-sector solutions do not converge in L².

Mechanism [N]: the small eigenspace of the Galerkin K (A = 2, N = 800) contains near-null vectors at ~1.6×10⁻⁸ in **both** parities; the odd ones overlap the x-source (~1e−3), so the odd solve is corrupted by ~1/1.6e−8 amplification. This is **structural, not a λ-resonance**: the odd Schur denominator d_1 = |1+M_{1x}| is large at λ ∈ {−2, −1, −0.5, −0.2} alike (81, 47, 15, 24 at A = 2, N = 800), while the full-operator condition numbers stay modest (2.4–20.3 across the A-sweep).

Consequence [I]: r_1 = M_{1e}/(1+M_{1x}) is a ratio of two diverging quantities. Its apparent "stability" (~1–3% under refinement) is **not trustworthy** — it reflects the ratio of blow-up coefficients, not the true moments. The r_1 half of the gate is **untestable with this discretization**, and possibly untestable in principle if the moments do not exist.

## 5. Why this is upstream of v13.758 [I/D]

v13.758's terminal obstruction is that the moments are boundary-functional evaluations (ℓ_{0,A}, ℓ_{1,A}), so bulk spectral control cannot close them — the missing data are the boundary traces and the Schur denominators. The odd-sector finding is **one level further upstream**: it questions whether the *arguments* of those functionals, R_A^{(−)}x and R_A^{(−)}(sinh−x), exist as L² objects at all. If 0 ∈ σ(L_A^{(−)}):

- the moment definitions M_{1x} = ℓ_1(R_A^{(−)}x), M_{1e} = ℓ_1(R_A^{(−)}(sinh−x)) need a domain/pseudoinverse qualification the ledger does not currently give them;
- the r_1 gate must be reformulated before the v13.758 boundary-trace program can even start on the odd half;
- the "four remaining routes" of v13.769 (including direct finite-A evaluation of M_{1x}) inherit the same ill-posedness.

None of this touches the even half, the finite HB theorem (v13.673), or the audit thread's confirmed results. It is localized to the odd sector of the finite operator.

## 6. What this is not [I]

- **Not the γ-pinning canary.** That canary (λ = 0 solves, cond ~10⁸, hallucinating γ-pinned minima) is about ill-conditioning at a specific parameter. The odd-sector ill-posedness persists at λ = −1 with healthy condition numbers and across λ ∈ {−2, −1, −0.5, −0.2}. Different phenomenon, different cause.
- **Not an RH claim.** The question is whether a concrete finite-interval Fredholm operator has 0 in its odd spectrum. It is decidable, in principle, by finite-dimensional means — no zero input, no asymptotics beyond fixed A.
- **Not a kill of the de Branges line.** The line's NO-GO as an RH/selector route (`debranges_scope.md` §4–5) stands on independent grounds (dissipative limit object, choice relocated to prime data). This entry concerns only the operator-limit sub-problem's odd half.

## 7. What would resolve it [O]

1. **Analytic:** determine the odd spectrum of L_A^{(−)} at λ = −1 directly — e.g., via the parity-reduced Fredholm determinant, or a Birman–Schwinger-type argument on the odd sector. A proof that 0 ∈ σ(L_A^{(−)}) would be a new analytic obstruction, upstream of v13.758; a proof of bounded invertibility would send the problem back to discretization (the Galerkin method is then at fault, not the operator).
2. **Numerical:** deflation/projection against the computed near-nullspace, testing whether the *ratio* r_1 has a well-defined limit despite divergent moments. (Per §4, the current apparent stability is not evidence of this — the test must be redesigned, not re-run.)
3. **Scope:** extending the g prime sieve past e^{2A} = 100000 (current cap A ≈ 5.7) deepens the even-sector r_0 measurement; it does not touch the odd question.

Jeremy has not selected among these; the question is parked as stated.

## Synchronization

Live ledger head checked immediately before this write: v13.911 (audit thread, External Audit Round 132 — read in full; PASS on v13.908 via a fully independent discretization confirming the 2cos(π/k) formula at every tested point including both named anomalies; v13.910's sandwich-theorem logic verified sound and its "Round 131 untouched" claim confirmed; v13.910 §2's central numerical claim attempted but honestly reported inconclusive on the auditor's discretization; v13.909's γ₁ frequency transition independently corroborated). No collision on v13.912. The audit thread has not treated this entry's material; this entry is its first ledger record.
