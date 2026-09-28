# Cone Derivation Ledger v13.840 — Sandbox Bucket 2: Kink-Faithful Distributional \(T_a\) Realization; Ratios Determined Numerically; Edge Criteria Fail Cleanly

Date: 2026-09-28

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[I]/[O]** report with **[N]** sandbox numerics. The [N] results are exploratory finite-precision computations (P1 Galerkin, A ≤ 6, N ≤ 800); they are reported as structural diagnostics, not as proofs and not as [N-cert].

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by explicit request of the project owner, who authorized this entry's promotion from the sandbox. Second sandbox-track contribution to the ledger, following v13.838.

Parents: v13.838 (the gap characterization this entry's construction answers), v13.773, v13.743, v13.839 (Round 114 audit of v13.838), Suzuki arXiv v2 (2606.09096v2), v13.258/v13.772 (D12 screw construction, prime ramp untouched). Raw deliverables (scripts, results.json, full report, STATUS.md, phase1_kinks.json) remain in the workspace at `~/workspace/d12/lane_b/sandbox/runs/20260928-155806-bucket2-distributional-ta/`; they are not part of this repo.

Synchronization: live ledger head checked immediately before this write is v13.839 (External Audit Round 114), branch `master`. No collision on the present version number. **This entry does not audit v13.834–839**; that is ordinary audit business.

## 0. What this entry does

v13.838 §6 named two routes that could close the Bucket 2 gate; this entry executes the **numerical** one: a faithful *distributional* realization of Suzuki's \(T_a\) — implementing \(-g''\) with its kink deltas instead of spline smoothing — then solving the deficiency equation (8.4) directly for \(v_\pm\) and reading off \(I_j = (K_A v_\pm)^{(j)}(0)\). Three findings, all [N]:

1. **The construction is self-consistent.** A falsifiable validation gate — the (8.5) residual mod affine — collapses from the spline benchmark of 2.26 to **\(1.47\times 10^{-6}\)**, decreasing monotonically under refinement (~\(N^{-2.3}\)). The distributional \(-g''\) is handled correctly.
2. **The ratios are determined (numerically):** \(r_1^+ \approx -8.75 \pm 0.01\), \(r_0^+ \approx +27.28 \pm 0.05\) at \(A=3\) (Richardson-extrapolated), with exact reflection symmetry between channels.
3. **The edge criteria FAIL — cleanly and robustly:** \(r_{1,A} = \Theta(e^A)\) not \(o(e^A/A)\); \(r_{0,A} = \Theta(Ae^A)\) not \(o(e^A)\). Both normalized ratios converge to the *same* constant \(|c| \approx 0.475\)–\(0.48\).

Finding 3 sharpens Bucket 2 from "we cannot determine the ratios" to a precise fork (§4): either the computed object is not Suzuki's \(v_\pm\) (domain issues), or the edge criteria themselves are misformulated. The withdrawn circular headline (\(r_1=-1\), \(r_0=-(1+i)\)) stays withdrawn; nothing here resuscitates it.

## 1. [N] The construction: weak form, kinks derived not guessed

The prior spline attempts failed structurally: \(g'\) has jump discontinuities at \(t = \pm\log m\) (prime powers \(m\)), so \(-g''\) carries delta lines, and any \(C^2\) smoothing severs the (8.4)⇔(8.5) link (v13.838 §2). This build **never differentiates \(g\)**. It discretizes the weak form

\[
a(u,v) = \int_{-A}^{A}\!\!\int_{-A}^{A} g(x-y)\, u'(y)\, v'(x)\, dy\, dx = (f, v), \qquad v \in H^1_0(-A,A),\; f(x) = e^{\pm x},
\]

with P1 finite elements at \(\lambda = 0\) (Suzuki's intended case, \(T_a = A_a\)). Integration by parts gives \(a(u,v) = \langle -DG_aDu, v\rangle = \langle T_a u, v\rangle\) (\(v(\pm A) = 0\) kills the boundary terms), so the kink deltas and the diagonal singularity of \(-g''\) are handled **implicitly** by integrating the *continuous* kernel \(g\) against test-function derivatives.

**Phase 1 — kink data derived source-faithfully** (from v13.258's archimedean \(A_{12}\) closed form and v13.772's prime ramp \(R_{12}\), untouched): \(R_{12}'(t) = \sum_{\log m \le t} c_m\) is an exact step function (\(c_m = \Lambda(m)\chi_{12}(m)/\sqrt{m}\)); \(A_{12}\) is smooth on \((0,\infty)\). Hence for the even extension, at **both** \(t = +\log m\) and \(t = -\log m\):

\[
\text{jump of } g' = +c_m \quad \text{(both sides — not }\pm c_m\text{)},
\]

verified numerically to \(9.3\times 10^{-10}\) over the first 8 kinks. Consequently \(-g''_{\text{dist}} = -g''_{\text{reg}} - \sum_m c_m\,[\delta(t-\log m) + \delta(t+\log m)]\). The diagonal singularity was also characterized: \(t\cdot A_{12}''(t) \to -1/2\) (verified \(-0.500250\)), i.e. \(-g''(t) \sim -1/(2t)\) — the "regular part" is itself non-integrable at the diagonal, resolved here by Duffy-transform splitting of diagonal element pairs.

**Implementation fix found during the build:** a single global \(C^2\) spline of \(g\) Gibbs-overshoots at genuine kinks (measured \(5\times 10^{-6}\) glitch near \(t = 7.53513\), next to the real kink at \(\log 1873 = 7.5352967\)). Fixed structurally: \(g_{\text{fast}}(t) = R_{12}(t) - \text{spline}(A_{12})(t)\) — exact step-function ramp via searchsorted/cumsum, spline only of the smooth part. Result: \(|g_{\text{fast}} - \text{mpmath (dps=30)}| \le 9.0\times 10^{-15}\); kink-faithful by construction.

**Discrete spectrum (numerical fact only):** the assembled stiffness \(S\) is real symmetric with **zero negative eigenvalues at every \((A,N)\) tested**, cond \(\approx 35\)–\(43\). This is an observation about this discretization, not a positivity certificate about \(G_a\); no RH content is claimed.

## 2. [N] Validation gate — PASS

The gate is falsifiable and needs no external truth: in the continuum, (8.4) and (8.5) are formally equivalent, so a correct distributional (8.4) solution must satisfy (8.5) modulo the affine nullspace. The spline benchmark violated it at 2.26. Here, with \(H(x) = (K_A(-v))(x) - e^{\pm x}\) fit to \(Ax + B\):

| N | gate (+) | gate (−) | \(I_1^+\) | \(I_0^+\) |
|---|---|---|---|---|
| 50 | 9.26e-04 | 9.26e-04 | −8.385 | 25.857 |
| 100 | 1.79e-04 | 1.79e-04 | −8.545 | 26.655 |
| 200 | 3.94e-05 | 3.94e-05 | −8.646 | 26.962 |
| 400 | 7.03e-06 | 7.03e-06 | −8.715 | 27.158 |
| 800 | **1.47e-06** | **1.47e-06** | −8.737 | 27.233 |

Monotone decrease ~\(N^{-2.3}\); the 2.26 benchmark beaten by six orders of magnitude. The (+) and (−) channels agree to all printed digits; the reflection symmetry \(I_1^- = -I_1^+\), \(I_0^- = I_0^+\) is exact to machine precision. A-track of the gate (N=200): 2.1e-05 (A=2), 3.9e-05 (A=3), 6.6e-05 (A=4), 9.2e-05 (A=5) — small and controlled.

**The gate demonstrably rejects wrong answers:** the first full run misread Suzuki's \(z\)-convention and solved \(T_a v = e^{\pm ix}\) (\(e_z(x) = e^{-izx}\) gives the *real* exponential \(e^{+x}\) at \(z = +i\), not \(e^{ix}\)). That run returned gate ~O(1) and was correctly rejected; after fixing to Suzuki's real right-hand side the gate collapsed. The wrong-RHS run is discarded, not reported as a result.

## 3. [N] Ratios and the edge criteria

\(r_j = I_j/C\), \(C = 1\); \(A_3\) values Richardson-extrapolated, rest N=400 direct:

| A | \(r_1^+\) | \(r_0^+\) | \(r_1^+/e^A\) | \(r_0^+/(Ae^A)\) | \(\alpha_A^+\) | \(\beta_A^+\) | \(\alpha_A^-\) | \(\beta_A^-\) |
|---|---|---|---|---|---|---|---|---|
| 2 | −2.486 | 6.708 | −0.336 | 0.454 | 0.201 | −0.641 | −0.472 | −1.987 |
| 3 | −8.747 | 27.28 | −0.436 | 0.453 | 0.386 | −0.251 | −0.485 | −2.864 |
| 4 | −24.929 | 102.437 | −0.457 | 0.469 | 0.438 | −0.141 | −0.475 | −3.794 |
| 5 | −69.464 | 354.154 | −0.468 | 0.477 | 0.461 | −0.087 | −0.475 | −4.767 |
| 6 | −193.092 | 1147.834 | −0.479 | 0.474 | 0.476 | +0.009 | −0.481 | −5.734 |

The normalized ratios converge: **\(r_1^+/e^A \to -c\), \(r_0^+/(Ae^A) \to +c\)** with \(c \approx 0.475\)–\(0.48\) — the same constant on both ratios. Hence:

- \(r_{1,A} = \Theta(e^A)\): **not** \(o(e^A/A)\). FAIL.
- \(r_{0,A} = \Theta(Ae^A)\): **not** \(o(e^A)\). FAIL.
- \(\alpha_A^+ \to +0.48 \ne 0\); \(\alpha_A^- \to -0.48 \ne 0\).
- \(\beta_A^+ \to 0\) only through the cancellation \(c_1 \approx c_0\) (not through the edge criteria holding); \(\beta_A^- \sim -0.95\cdot A \to -\infty\).

The failure is a statement about **growth rates**, visible across \(A = 2\ldots 6\) with converging normalized ratios and gate \(\le 3\times 10^{-5}\) throughout the A-track — not a discretization artifact.

## 4. Interpretation: the fork

The edge criteria (\(r_{1,A} = o(e^A/A)\), \(r_{0,A} = o(e^A)\), \(\alpha_A \to 0\); v13.773 §7, v13.743) were the test for whether the boundary constants are "admissible." They fail for the computed object. Two horns:

**Horn A — wrong object.** The numbers above are the ratios for the **\(H^1_0\) weak solution** of \(T_a v = e^{\pm x}\) at \(\lambda = 0\). The weak solution equals \(A_a^{-1}e^{\pm x}\) *provided* Suzuki's form domain is \(H^1_0\) and \(A_a\) is invertible at \(\lambda = 0\). Suzuki proves invertibility only for \(\lambda < \lambda_a\) with the sign of \(\lambda_a\) unknown (Lemma 6.2), and the paper flags domain issues explicitly ("ignores domain issues," p.30). If Suzuki's form domain is larger than \(H^1_0\) (cf. the ledger note that \(\mathrm{Dom}(A_a)\) is "larger than \(H^1_0\), containing constants"), these need not be Suzuki's ratios, and the edge criteria may still hold for the true \(v_\pm\).

**Horn B — wrong test.** If \(\Theta(e^A)\) growth with a clean structural constant is what the true solution actually does — and the convergence of both normalized ratios to the same \(|c| \approx 0.48\) suggests the growth is intrinsic to the equation, not numerical noise — then the edge criteria as stated can **never** be satisfied by the true solution, and they need rethinking rather than the solution needing repair. There is a plausible mechanism: with \(g\) growing exponentially, the solution of \(T_a v = e^x\) plausibly inherits \(e^A\)-scale boundary behavior that the moments \(I_j = (K_A v)^{(j)}(0)\) pick up.

This entry does not pick a horn; the numerics cannot. But Bucket 2 has moved: from "the ratios cannot be determined" (v13.838) to **"the ratios are \(\Theta(e^A)\) with constant \(0.48\) for the \(H^1_0\) realization — is that the true \(v_\pm\) behavior?"** Distinguishing the horns is now the analytic question, and it is sharper than the one we started with.

## 5. Caveats and guardrails

1. **\(\lambda = 0\) only.** A \(\lambda = -1\) spot check was attempted but is **invalid**: the weak operator was assembled correctly (\(S + M\)) while the moments code evaluates \((K_A v)\) with the \(\lambda = 0\) kernel \(g(x-y)\) only — the \(-\lambda N(x,y)\) term was never derived/implemented. Its gate (0.499) tests the wrong identity. Deriving \(N(x,y)\) source-faithfully is a separate task; \(\lambda\)-sensitivity remains **open and is not claimed**.
2. **What the numbers are** (§4, Horn A): \(H^1_0\) weak-solution ratios at \(\lambda = 0\). Whether they equal Suzuki's \(v_\pm\) depends on the form domain and on invertibility at \(\lambda = 0\) — analytic gaps the numerics cannot close.
3. **No claims beyond the sandbox:** no RH, GRH, positivity, or Hilbert–Pólya content. The observed positive-definiteness of the discrete \(S\) is a numerical fact about this discretization.
4. Scripts live outside this repo; the [N] numerics are honestly scoped as exploratory and have not been independently re-executed.
5. The edge-criteria failure does not touch Bucket 1 (RH-equivalent positivity) or Bucket 3 (finite-section certificates), whose results stand exactly as stated by their own entries.

## Result

\[
\boxed{
\textbf{Bucket 2, numerical half (2026-09-28):} \text{ a kink-faithful distributional realization of } T_a \text{ passes a falsifiable self-consistency gate (2.26 } \to 1.5\times 10^{-6}\text{) and determines the boundary ratios numerically: } r_1^+ \approx -8.75,\ r_0^+ \approx +27.28 \text{ (}H^1_0\text{ weak solution, }\lambda=0\text{). The v13.773 edge criteria FAIL for this object: } r_1 = \Theta(e^A),\ r_0 = \Theta(Ae^A) \text{ with a common structural constant } |c| \approx 0.48. \text{ Open fork: wrong object (domain issues) or wrong test (criteria misformulated).}
}
\]

This entry supersedes no proof and blocks no work. The analytic half of Bucket 2 — the form domain, invertibility at \(\lambda = 0\), and the Horn A/B fork — remains open, now with the numerical target precisely specified.
