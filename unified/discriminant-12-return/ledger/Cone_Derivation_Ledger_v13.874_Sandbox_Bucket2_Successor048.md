# Cone Derivation Ledger v13.874 — Sandbox Bucket 2: SUCCESSOR-048 — 0.955 Was Discretization Error; N-Converged Ratio ≈ 0.970; Square Collocation Unreliable

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[N]** for the re-measured numbers; **[I]/[O]** for interpretation. No RH/positivity/Hilbert–Pólya claim.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request and with the authorization of the project owner. Full report (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-successor048/SUCCESSOR048_Report_ForReview.md` (+ JSON data, scripts).

Parents: v13.872 Part B (MECH-048 — the quantitative claim this entry revises), v13.871, v13.870.

Synchronization: live ledger head checked immediately before this write is **v13.873** (External Audit Round 124 — PASS on v13.870–v13.872; the audit thread moved the head again, and the check caught it). No collision on the present version number. **This entry does not audit v13.873 or earlier.**

## Verdict [N]: the 0.955 dressing factor was overstated — largely discretization error

The precise problem chartered in v13.872 asked whether \(\lim_{A\to\infty} [\text{dressed cubic moment}]/[\text{bare cubic moment}]\) is \(1\) (dressing vanishes) or \(0.955\) (dressing persists). The answer is **neither exactly**: the N-converged ratio is **≈ 0.970**.

- Runs at \(A = 7, 8\) with \(N = 120 \to 240 \to 480 \to 960\) (α-scan 10⁻⁸/10⁻¹⁰/10⁻¹², α-insensitive to 5 digits; gates \(\sim N^{-1.6} \to 0\)): at fixed \(A\), \(r_1/e^A\) marches \(-0.474 \to -0.484 \to -0.488 \to -0.489\); \(m_3/m_3^s \to 0.970\). Four extrapolation models agree; A=7 and A=8 extrapolations agree within 0.001.
- **The confounder was N, not A.** At fixed N, A=7→8 changes \(r_1/e^A\) by ~3×10⁻⁴ (flat). MECH-048's "stability" at N=120→240 was a **false plateau**; the real movement happened at N=480→960.
- The ratio moves *away* from 0.955 as N increases (0.968 at N=960 → 0.970) but robustly stops below 1.0 — a genuine ≈3% persistent screw dressing survives. "→1" is closer to the truth.

**MECH-048's quantitative headline is revised:** \(-0.48 = (-0.5)\times0.955\) becomes \(\mathbf{-0.489 \approx (-0.5)\times0.979}\). The qualitative story (universal \(-1/2\) from the free resolvent × a small persistent screw dressing) stands; the quantitative dressing factor does not. The "uniform 0.955 dressing" picture is withdrawn: \(w_o/\sinh\) is wildly non-uniform pointwise (ratios in \([-111, +141]\) at \(A = 8\)) — the dressing is a *moment* phenomenon, not a scalar multiplier.

## Square collocation is unreliable [N, with a cautionary moral]

At \(A = 8, N = 120\), properly-square collocation returns \(-0.334\) with a **tiny** residual gate (7.6×10⁻⁶) — a small-residual **wrong** answer on a spurious branch; the discrepancy worsens with A. The overdetermined LSQ remains trustworthy (smooth N-convergence, α-insensitive, BC-independent). **Small residuals do not certify a first-kind equation's discretization.** (This is the same lesson as the ψ(1/4) bug, one level subtler: the machinery that catches errors must distrust its own green lights.)

## Open [O]: the analytic derivation of 0.970

No analytic derivation of the exact 0.970 exists. The \(A \to \infty\) limit is a half-line Wiener–Hopf edge problem — **formulated but not solved** in this run (the worker's analytic probe: exact y-IBP shows the dressing operator's action is far from scalar; a \(C_-(\infty) \approx -0.322 \ne 0\) plausibility stands at [N], not proof). Chartered as the next investigation.

## Methodological ledger note [I]

Two false-convergence events in one day, same shape: the ψ(1/4) transcription bug survived because its outputs looked converged and well-behaved; the 0.955 survived because N=120→240 looked stable. Both were caught only by pushing one refinement axis further than "looks stable" required. Standing practice going forward: a numerical claim is not lifted until it survives refinement **past** the first plateau.
