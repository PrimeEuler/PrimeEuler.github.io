# Cone Derivation Ledger v13.872 — Sandbox Bucket 2: LAMBDA-TWIST (Three Objects, Hypothesis Disambiguated) + MECH-048 (the −0.48 Mechanism: Bare −1/2 × 0.955 Dressing)

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[D]** for the textual/analytic verdicts and the exact bare-kernel result; **[N]** for the dressed numbers; **[I]/[O]** for interpretation. No RH/positivity/Hilbert–Pólya claim.

Author: the project owner's sandbox track (autonomous threads under the owner's assistant), by request and with the authorization of the project owner. Full reports (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-lambda-twist/` (analytic; the evidence is in the ledger text and `screw_corrected.py`) and `~/workspace/d12/lane_b/sandbox/runs/20260929-mech048/MECH048_Report_ForReview.md` (+ JSON data, scripts).

Parents: v13.871 (RERUN-048 verdicts), v13.870, v13.868 (one-way implication), v13.848 (SELECTS), v13.794, v13.274–v13.282 (Suzuki source resolution).

Synchronization: live ledger head checked immediately before this write is v13.871. No collision on the present version number. **This entry does not audit v13.871 or earlier.**

## PART A — LAMBDA-TWIST: the twisted object is not Suzuki's object [D]

**Three distinct objects** (ledger-text-verified):
- (i) **Suzuki's \(A_a\)** — the Riemann-zeta object: untwisted, conductor 1, from the localized Weil quadratic form \(Q_W^a\); \(B_a = D^*G_aD\), \(A_a\) its Friedrichs extension (v13.274). The object of Lemma 6.2, Theorem 1.1/1.5, v13.860's Lane A target, v13.868's one-way implication.
- (ii) **The full D12/Dedekind analog \(A_{K,a}\)** — for \(\zeta_K = \zeta\cdot L(\chi_{12})\), degree 2. Introduced in the ledger **under supposition** ("Suppose the D12 localized Weil form \(Q_{W,K}^a\) is closed and lower bounded…", v13.275:214).
- (iii) **Our sandbox numerical object** — the \(\chi_{12}\)-twisted summand alone (\(L(\chi_{12})\) screw, conductor 12; \(g_{12} = R_{12} - A_{12}\) with the twisted prime ramp \(c_m = \Lambda(m)\chi_{12}(m)/\sqrt{m}\)). v13.275:330 warns explicitly "not to infer positivity of the quadratic-character summand" from the field-coefficient identity.

The transfer of Suzuki's finite-interval theory (lower-boundedness, closability, Lemma 6.2) to (ii)/(iii) is **open**: "The bottleneck is establishing the D12 analogue of Suzuki's localized Weil-form/Friedrichs theorem" (v13.275:284). Consequence: **"\(\lambda_a > 0\)" was three hypotheses wearing one name**, and v13.848's SELECTS theorem cited Suzuki's Lemma 6.2 (about object i) while computing with object iii — the transfer was smuggled inside the application:

- **(H-Suz):** \(\inf\sigma(A_a^{\mathrm{Suz}}) > 0\) — Suzuki's operator; the RH-adjacent object.
- **(H-tw):** the twisted analog's form is closed/lower-bounded **and** \(\lambda_a^{\mathrm{tw}} > 0\) — needed for the sandbox \(\lambda = 0\) track; provisionally contradicted at the numerical level (RERUN-048: \(n_{\mathrm{neg}}\) 2→19), open at the analytic level.
- **(H-tw⁻):** \(\lambda_a^{\mathrm{tw}} > -1\) — needed for the sandbox \(\lambda = -1\) track, where every lifted RERUN-048 result lives; compatible with \(\lambda_a^{\mathrm{tw}} \le 0\); currently unthreatened.

**RH-inference, with extreme care:** the twisted \(\lambda = 0\) indefiniteness says **nothing** about RH-for-\(\zeta\) — wrong object ([D] different L-function, different conductor, different arithmetic data). The only coherent analog — "GRH(\(L(\cdot,\chi_{12}\))) ⟹ \(\lambda_a^{\mathrm{tw}} > 0\ \forall a\)" — is itself unproved (part of the same open transfer). No RH/GRH inference may be drawn from provisional [N] numerics; engaging any contrapositive requires jointly (1) the one-way implication proved for the relevant object, (2) a certified negative certificate (interval-enclosed trial function or rigorous eigenvalue enclosure), (3) the object pinned down exactly. None is in hand.

**Standing rules adopted:** retire bare "\(\lambda_a > 0\)" from sandbox writing — use the disambiguated (H-Suz)/(H-tw)/(H-tw⁻); the \(\lambda = -1\) track is the viable track; the \(\lambda = 0\) track is parked (revive only on certified refutation/confirmation of the indefiniteness or the analytic lower-boundedness proof); the D12 transfer is promoted to an explicit **[O]** line item (load-bearing and previously unnamed); **hard rule — the twisted \(\lambda = 0\) indefiniteness is never cited as RH/GRH evidence.**

## PART B — MECH-048: what sets −0.48 [D/N/I]

**The number is set by the universal \(\lambda = -1\) N-kernel, not by the corrected screw \(g\).** The dead \(c_1\) story had it backwards: it made the arithmetic the whole explanation, when the arithmetic is a ~4.5% correction to a number the free kernel already determines.

**[D] Bare \(-\tfrac12\), exact.** Solving (8.5) with \(g = 0\) (\(K = N\) only): \(w_o = \sinh(x)\) exactly, \(A_+ = -\cosh(A)\) exactly (verified to \(10^{-6}\) at \(N = 120\), error shrinking with \(N\)). Analytically: the N-kernel's \(-|x-y|/2\) is the Green's function for \(-d^2/dx^2\), which inverts to the identity on odd functions; hence \(A_+/e^A \to -1/2\) exactly.

**[N] Dressed \(-0.48\).** With the full D12 screw, the first-moment identity gives \(A_+\) from \(S = \int w_o\cdot M_N\), and the \(g\)-term is **< 0.1%** of the controlling moment — \(g\) is invisible to it. The \(g\)-convolution dresses \(w_o \approx 0.955\cdot\sinh\) via \(w_o = (I+L)^{-1}\sinh\), shifting \(-1/2\) to \(-0.4775 \approx -0.48\). Dressing factor stable at \(A = 2\ldots6\), \(N = 120 \to 240\).

**Probes:** the half-line model fails ([I] — the affine term \(A_+x\) diverges; the mechanism is the first-moment equation, not a half-line constant); kink anatomy ([O] — 93,339 kinks in \(t \in [0,14]\), \(\sum c_m = -1.06\), no simple sum rule; kinks enter only indirectly via the global \((I+L)^{-1}\)); the \(-\pi/2\) coincidence is coincidence ([I] — a P1 endpoint artifact vs a converged BC-independent LS moment, different objects); the independent-route cross-check (bare \(g = 0\) test, BC-independence, N-convergence, \(\alpha\)-insensitivity, 4-digit moment self-consistency, W1 cross-check) confirms it is **not** a second bug artifact — with one **[O] numerical-analysis caveat**: properly-square collocation agrees at \(A = 6\) (\(-0.474\) vs \(-0.476\)) but disagrees at \(A = 4\) (\(-0.518\) vs \(-0.458\), overshooting bare \(-1.0\)); (8.5) is first-kind (ill-posed), so square collocation is the less reliable regularization here.

## The precise successor problem (chartered)

> Determine \(\displaystyle\lim_{A\to\infty}\frac{\text{dressed cubic moment}}{\text{bare cubic moment}}\) for \(w_o = (I+L)^{-1}\sinh\) on the \(\lambda = -1\) odd branch. Bare limit \(-1/2\) [D]; observed \(-0.4775\) [N]; open whether the ratio \(\to 1\) (dressing vanishes as \(A \to \infty\)) or \(\to 0.955\) (dressing persists) [O]. Data at \(A \le 6\) cannot discriminate — needs larger-\(A\) (\(7, 8\)) and higher-\(N\) runs, plus resolution of the square-collocation \(A = 4\) discrepancy.

**Structural moral [I]:** the 0.48 is **universal \(-1/2\) (free resolvent) × 0.955 (screw dressing)**. The D12 arithmetic contributes under 0.1% to the controlling moment. Whatever the dressed limit proves to be, the number's address is the N-kernel's Green's-function identity — the deepest exact foothold the Bucket 2 program has produced.
