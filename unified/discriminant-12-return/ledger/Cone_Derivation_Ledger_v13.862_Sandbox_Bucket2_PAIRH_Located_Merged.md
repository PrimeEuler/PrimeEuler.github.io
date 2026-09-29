# Cone Derivation Ledger v13.862 — Sandbox Bucket 2: PAIR-H Located — the Bulk Question and the 0.48-Value Problem Are One

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[I]/[O]** sandbox analytic report with **[D]** ledger- and Suzuki-text-derived facts and **[N]** sandbox numerics. No new ledgered numerics in this entry.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request of the project owner. Full analysis (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-pairh-analysis/PAIRH_Analysis_ForReview.md`.

Parents: v13.861 (H1), v13.858 (G1–G3), v13.857 (routes), v13.855 (bulk lemma), v13.854 (W3), v13.853 (W2 convergence), v13.848 (selection), v13.846 (selection identity), v13.785, v13.782, Suzuki arXiv v2.

Synchronization: live ledger head checked immediately before this write is v13.861. No collision on the present version number. **This entry does not audit v13.861 or earlier.**

## 0. What this entry does

Investigates PAIR-H, the bulk pairing hypothesis — the named missing bulk control from W3's verdict (α-odd is R2-edge-tamed but needs bulk control). **Verdict: [O] — obstructed, with the obstruction now named exactly.** The sharpest finding: PAIR-H₀ is analytically equivalent to the edge-integral identity \(E = L_0\) (modulo COMB-H) — the "bulk cancellation mechanism" and "why 0.48 is the same at both scales" are **one question, not two**. The convergence leg's remaining analytic work and the 0.48-value problem have **merged**.

## 1. PAIR-H, precisely (three layers)

- **W2 original:** edge-normalized pairings converge to [bulk macroscopic pairing] + [edge half-line pairing]; the bulk part — the macroscopic limit under \(r_{0,A}/(Ae^A) \to L_0 = +0.48\) — is the named open analytic input; R2 (\(L_0 + L_1 = 0\)) is the consistency condition that the same 0.48 governs both scales.
- **v13.855 refinement (corrects W2's mechanism):** the \(I_0/M_0\)-type pairing is **edge-localized**, not bulk+edge comparable —
  - **(PAIR-H₀):** \(I_{0,A}^{\rm bulk}/(Ae^A) \to 0\) **[N]**: bulk < 0.005·\(Ae^A\) at \(A=6\); 100% of the pairing accumulates in \([A-3,A]\); the extra \(A\) is **test-function growth** (\(g \sim c_1|y|\)), not interval length.
  - **(PAIR-H₁):** \(I_1\) is genuinely two-scale (bulk \(+0.26e^A\), edge \(-0.73e^A\), δ-sensitive).
  - **Lemma A [D|R1/R2]:** \(s_A(\eta A)/(Ae^A) \to L_0(1-\eta)\); the constant \(-0.48\) is the derivative-source limit.
  - Concrete address: \(L_0 = -c_1\int_0^\infty V_\infty^+(\xi)\,d\xi\), \(c_1 \approx -0.154\).
- **W3 consumption point (§4):** \(P(w) = \langle\bar De_w, \bar DR_A(e^x)\rangle\!\bar{} + e^A[\beta_AM_0(w) + \alpha_A(M_1(w) - AM_0(w))]\). The α-odd term \(b(w) = \alpha_Ae^AAM_0(w)\) is \(Ae^A\)-scale and sign-flipping; its **edge** parts are R2-tamed (\((M_1 - AM_0) = \langle\bar De_w, \bar DR_A(x-A)\rangle\!\bar{}\) vanishes at the right edge); its **bulk** part — "the pairing of the global affine against the bulk test function" — is exactly (PAIR-H₀). β cancels solid; α-even survives solid. **W3's verdict stands as stated.**

## 2. Evidence

**[N]:** bulk < 0.005·\(Ae^A\) at \(A=6\); cumulative pairing flat then monotone rise on \([A-3,A]\); R2 table \(L_0 + L_1 \to 0\) across \(A = 3..6\); macroscopic source matches \(L_1\eta + L_0\) to 3 decimals. **[D]:** \(I_{0,A} = 1 + B_{\rm coef}\) **exact** (moment identity) ⇒ \(I_{0,A}/(Ae^A) \to L_0\) given R1; Lemma A(a)(b) exact given R1/R2. **[I]:** oscillatory \(O(e^A)\) bulk \(v_A\) averages to ~0 against slowly-varying even \(g\).

## 3. Analytic attempt — three routes stall

- **Duality:** \(I_{0,A} = -C_+\int (T_A^{-1}g)(y)e^y\,dy\) **[D]** (self-adjointness); \(e^y\) concentrates at the edge, but the crude bulk bound \(O(A^2e^{A-\delta})\) overshoots the \(o(Ae^A)\) target by \(\sim Ae^{-\delta}\) — the gap **is** the oscillatory cancellation; needs resolvent-kernel asymptotics not in the ledger.
- **T-side machinery (G1/G2/H1):** re-grounds the objects (\(w_A = T_A^{-1}e^x\) [D]; pairing = energy form [I]; dual-slot canonization [D/I]) — but all fixed-\(A\) algebra; PAIR-H₀ is an \(A \to \infty\) weak-vanishing statement about the macroscopic profile \(V_A(\eta) = v_{A,+}(\eta A)/e^A\). Necessary, not sufficient.
- **Selection principle (v13.846):** exact but discrete and coefficient-level; v13.848: the continuum needs no selection (unique \(T_A\)-inversion). Doesn't touch the bulk profile.

## 4. The sharpest fact — an equivalence [D/I]

Total \(I_{0,A}/(Ae^A) \to L_0\) **[D|R1]**; edge \(\to E := -c_1\int_0^\infty V_\infty^+\) **[I|COMB-H]**; hence bulk \(\to L_0 - E\) **[D]** (subtraction). Therefore:

\[
\boxed{\text{(PAIR-H₀)} \iff E = L_0 \quad \text{(modulo COMB-H)}.}
\]

Proving the bulk vanishes directly is analytically equivalent to the 0.48 edge-integral identity — the same depth as the 0.48-value problem (needs the W1 profile in closed form; \(c_1\) set by \(-L'/L(1/2,\chi_{12})\)).

## 5. The exact missing estimate [O]

Let \(v_{A,+} = T_A^{-1}(C_+e^x) \in \mathfrak{D}(T_A)\) (true deficiency vector, \(\lambda < \lambda_a\) **[D]**), \(g\) even with \(g(t) = c_1|t| + O(1)\). For each fixed \(\delta > 0\):

\[
\boxed{\left|\int_{|y| \le A-\delta} g(y)\,v_{A,+}(y)\,dy\right| = o(Ae^A)}
\]

— equivalently \(\int_{|\eta| \le 1-\delta/A} |\eta|\,V_A(\eta)\,d\eta \to 0\): a bulk oscillatory-averaging/weak-vanishing bound for the macroscopic \(T_A^{-1}\)-response. This is the single estimate the convergence leg is waiting on.

## 6. What PAIR-H needs next (three routes, unchanged depth)

1. A direct bulk-averaging estimate for \(T_A^{-1}\) (resolvent-kernel asymptotics in the bulk — genuinely new analysis), **or**
2. Via the edge: COMB-H + W1 profile + test-function transport to prove \(E = L_0\) (same depth as the 0.48-value problem), **or**
3. Note: PAIR-H₁ (\(I_1\) two-scale) is δ-sensitive numerically — needs a cleaner ξ-coordinate edge/bulk split before an analytic statement is even well-posed.

## 7. Frontier update

| Item | Status |
|---|---|
| T side at fixed \(A\) (D̄, Route T, G1–G3, H1) | **Closed [D/I]** through v13.861 |
| PAIR-H bulk control (convergence leg) | **[O]** — merged with the 0.48-value problem (§4) |
| 0.48 analytic value | **[O]** — same question as PAIR-H₀, in edge-integral form |
| Identification leg (\(\delta_\infty\) discrepancy) | **[O]** — needs the infinite-volume comparison |
| Standing hypothesis | \(\lambda_a > 0\) (cf. v13.860) |
