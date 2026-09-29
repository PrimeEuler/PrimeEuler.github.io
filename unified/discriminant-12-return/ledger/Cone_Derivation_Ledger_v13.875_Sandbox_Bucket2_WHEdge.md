# Cone Derivation Ledger v13.875 — Sandbox Bucket 2: WH-EDGE — 0.970 Characterized, Not Derived; Exact Edge Equation; Moment-Hierarchy Explanation; Factorization Obstruction Named

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[D]** for the exact edge equation and IBP identity; **[N]** for the verified numbers; **[I]/[O]** for interpretation. No RH/positivity/Hilbert–Pólya claim.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request and with the authorization of the project owner. Full report (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-whedge/WHEDGE_Report_ForReview.md` (+ scripts, data).

Parents: v13.874 (SUCCESSOR-048 — the 0.970 this entry characterizes), v13.872 Part B, v13.774 §7 (the analytic wall).

Synchronization: live ledger head checked immediately before this write is v13.874. No collision on the present version number. **This entry does not audit v13.874 or earlier.**

## Verdict: the 0.970 is characterized, not derived

Full Wiener–Hopf factorization is a **clean negative** — intractable, with the exact obstruction identified. The deliverable is an exact edge identity plus a verified moment-hierarchy explanation.

## 1. The exact half-line edge equation [D]

From the odd-channel second-kind equation \((I+L_A)w_o = \sinh\) with \(L_A = (-d^2/dx^2)G_A\), edge variable \(\xi = A - x\), normalized profile \(\Phi_A(\xi) = w_o(A-\xi)/\sinh A\):

\[
\Phi(\xi) + \int_0^\infty k(\eta-\xi)\,\Phi(\eta)\,d\eta = e^{-\xi}, \qquad \xi \ge 0,
\]

\[
k(t) = -g''(t) = -g''_{\mathrm{reg}}(t) - \sum_m c_m\,[\delta(t-t_m) + \delta(t+t_m)],
\]

\(t_m = \log m\), \(c_m = \Lambda(m)\chi_{12}(m)/\sqrt{m}\). The moment link is exact:

\[
R = m_3/m_3^{\sinh} \;\longrightarrow\; \int_0^\infty \Phi(\xi)\,d\xi .
\]

## 2. The factorization obstruction, named [N/I]

\(\sigma(\omega) = 1 + \widehat{(-g'')}(\omega) = 1 - \widehat{g''_{\mathrm{reg}}}(\omega) + (L'/L)(\tfrac12+i\omega,\chi_{12}) + (L'/L)(\tfrac12-i\omega,\bar\chi_{12})\). The \((L'/L)\) terms put poles at **every** \(L(s,\chi_{12})\) zero, so \(\sigma\) is a tempered explicit-formula distribution, not a factorizable scalar function. **Same analytic wall as v13.774 §7** ("ordinary scalar Wiener–Hopf factorization is still blocked") — verified that v13.774 concerns a different problem (Lane A, symbol \(\mathcal D = \widehat{-g''}-\lambda\), two boundary constants), but the obstruction mechanism transfers exactly. No contradiction, no duplication: the wall is structural, not problem-specific.

## 3. The moment hierarchy — the analytic core [D/N]

**Exact finite-\(A\) IBP identity:**

\[
\langle y^3, L_A w_o\rangle = -2A^3(G_Aw_o)'(A) + 6A^2(G_Aw_o)(A) - 6\langle y, G_Aw_o\rangle .
\]

The last two terms are \(O(1/A)\) (bulk vanishes since \(\|G_Aw_o\|_\infty = O(e^A)\)), so the dressing is **edge-dominated**:

\[
R = 1 + 2\lim_{A\to\infty}\frac{(G_Aw_o)'(A)}{e^A} = 1 + \int_0^\infty g'(\eta)\,\Phi(\eta)\,d\eta \qquad \text{(formal limit)}.
\]

Verified numerically with a direct second-kind solver (residual \(7\times10^{-10}\)): the edge term dominates the next by ~10× and the bulk by ~100×.

**Why <0.1% vs 3% — answered:** \(S_g\) sees \(g\) at **zero** derivatives (\(M_g(y) = \int x\,g(x-y)\,dx\) is killed by evenness, \(|M_g|_{\max} \approx 0.28\)); the dressing sees \(g\) at **two** derivatives — the kink deltas, net \(O(1)\) after \(\sum|c_m| \approx 2188\) cancels to \(\sum c_m \approx -1.06\). **The cubic moment is selected by the observable (the first-moment identity), not by \(g\).** The arithmetic enters only through the kink strengths at two derivatives — which is why MECH-048's "g is invisible" and SUCCESSOR-048's "3% persists" are both true.

**Numerical cross-check [N]:** second-kind moment \(0.987\,(N{=}240) \to 0.978\,(N{=}480)\) converges toward the LSQ 0.970; its edge profile is clean and decaying (\(\Phi(0) \approx 0.90\), \(\Phi(1) \approx 0.40\), \(\Phi(3) \approx -0.02\)), unlike the LSQ's artifact-laden pointwise profile. Not fully closed — the refinement discipline still applies.

## 4. The creed, applied [I]

The cone **selects** the cubic moment via the first-moment identity (shown: the IBP identity is exact at finite \(A\), and the edge-domination is verified). The 3% value itself is **permitted** by kink arithmetic, not further selected — the selection principle is exhibited, the residual value is marked "permitted, not selected." Hence: characterized, not derived. This is the entry's honest stopping point.

## Honest gaps [O]

No two-sided bound on \(R\); the \(\Phi_A \to \Phi\) interchange is formal; the reflected-edge term needs the differentiated form for rigor. The \(A\to\infty\) Wiener–Hopf edge problem stands formulated with its obstruction named — the precise address of whatever comes next.
