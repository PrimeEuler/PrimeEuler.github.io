# Cone Derivation Ledger v13.871 — Sandbox Bucket 2: RERUN-048 Verdicts — Bug Footprint [D]; 0.48 Survives in the Odd Channel; Per-Claim Lifting of v13.870

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[D]** for the bug footprint (exact fit); **[N]** for the re-measured numbers; **[I]/[O]** for interpretation. No RH/positivity/Hilbert–Pólya claim.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request and with the authorization of the project owner. Full report (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-rerun048/RERUN048_Report_ForReview.md`; data as JSON in the run dir.

Parents: v13.870 (provisional-status rule), v13.867 (the PSI_Q bug), v13.840, v13.842, v13.848, v13.852–v13.855, v13.862, v13.868 (one-way implication note).

Synchronization: live ledger head checked immediately before this write is v13.870. No collision on the present version number. **This entry does not audit v13.870 or earlier.**

## 0. The bug's causal footprint [D]

On the corrected kernel (`screw_corrected.py`, import-time assertions installed — the guardrail caught two further transcription errors during setup):

\[
g_{\mathrm{buggy}} - g_{\mathrm{true}} = -0.15537\cdot|t| + 0.186 \qquad \text{(exact; fit residual } 2\times10^{-11}\text{)}.
\]

Because the \(|\cdot|\) weak form is negative definite, this single term did two things: (a) manufactured the \(c_1 = -0.154\) linear growth (the old 0.48 mechanism, now dead); (b) added a positive-definite contribution that made v13.840's Dirichlet weak form look positive-definite (reconstructed \(S_{\mathrm{buggy}}\): \(n_{\mathrm{neg}} = 0\), min eig \(+1.802\times10^{-2}\) — digit-identical to the old report). The true form is indefinite (\(n_{\mathrm{neg}}\): \(2 \to 19\) under refinement). **The bug changed the operator's definiteness, not just its numbers.** Correlated finding: the old \(\lambda = 0\) runs were secretly at \(\lambda_{\mathrm{eff}} \approx +0.31\) — the bug had masked the §2a.1 analytic proof that the \(\lambda = 0\) (8.5) system is singular.

## 1. Per-claim verdicts (lifting v13.870 claim-by-claim, as the rule requires)

**LIFTED [N]** (reproduced on the corrected kernel):
- Odd channel, \(\lambda = -1\): \(r_1/e^A \to -0.48\), \(\alpha_A \to +0.48\). \(I_1\): \(-24.37 \to -25.00 \to -25.07\) under N-refinement at \(A = 4\); gates collapse \(\sim N^{-2}\); \(\alpha\)-insensitive (Tikhonov \(10^{-8}/10^{-10}/10^{-12}\) agree). **0.48 survives — but the \(c_1\) mechanism is dead; what sets \(-0.48\) with bounded \(g\) is now the top open question [O].**
- W1 remnant (v13.852): \(-0.48\), rock-stable \(A = 2\ldots6\); two-shape fit residual \(2\times10^{-15}\) vs pure-only \(0.97\).
- v13.842 §2 instability, in character: same \(-1/h\) blow-up; constant \(-2.42 \to \mathbf{-1.57 \approx -\pi/2}\) ([N] measurement; the \(-\pi/2\) coincidence is [O]).
- v13.842 §3 Horn A falsification, via the \(\lambda = -1\) leg: natural vs Dirichlet agree to 1–2% in the odd channel, both \(\to -0.48\).

**REFUTED** (not merely provisional):
- The \(\lambda = 0\) (8.5)-LS system is singular on the corrected kernel, natural and Dirichlet BCs (gates 0.46–0.51, no refinement collapse).
- v13.840 §2 validation gate (\(1.47\times10^{-6}\)): was a bug artifact — manufactured by the same term that manufactured \(c_1\).
- v13.840 §3 ratios and edge verdict, as stated: no converged \(\lambda = 0\) solution exists to evaluate them on.
- PAIR-H's "edge-localized" picture (v13.855/v13.862), as stated: \(I_0 = \Theta(Ae^A)\) persists, but bulk and edge contribute comparably (bulk 4.27 vs edge 2.29 in \(Ae^A\) units at \(A = 6\)).

**NOT LIFTED — still provisional** (v13.870 continues to apply):
- The entire even channel: \(\beta_A \approx -6A \to -\infty\) (contradicting the old \(\beta_A \to 0\)); \(I_0\) unconverged (\(\sim\)40% growth per N-doubling at \(A = 5\); beyond P1 discretization). W2/W3's numerics depend on \(I_0/L_0\) and wait on a better discretization.

## 2. Flags and open questions [I/O]

- **0.48 splits by channel.** Odd: survives, converged [N]. Even: the old cancellation picture is dead; \(I_0\) unconverged [O]. Do not collapse into one headline. The 0.48-value problem is restated: with bounded \(g\) and no linear growth, what sets \(-0.48\) in the odd channel?
- **\(\lambda_a \le 0\) flag for the twisted object [O].** The D12 \(\chi_{12}\)-twisted analog is indefinite at \(\lambda = 0\) in both weak forms. The standing hypothesis "\(\lambda_a > 0\)" (v13.848) must be re-examined **for the twisted object specifically**; the \(\lambda = -1\) work is unaffected (\(T_{a,-1} = A_a + I\) stays positive). Connection to v13.868 handled with care: whether Suzuki's \(A_a\) (whose positivity follows from RH) is the same object as the twisted analog is itself the question — no RH inference is drawn here. Chartered as the next investigation.
- **Analytic-only results stand** (v13.870 §1 carve-outs unaffected): selection theorems, G1–G3, H1, IDENT, Wiener–Hopf.
