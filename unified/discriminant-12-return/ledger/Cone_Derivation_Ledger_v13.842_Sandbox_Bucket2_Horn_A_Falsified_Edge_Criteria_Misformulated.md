# Cone Derivation Ledger v13.842 — Sandbox Bucket 2: Horn A Falsified — Natural-BC Rerun Reproduces the Θ(e^A) Growth; Edge Criteria Misformulated (Horn B)

Date: 2026-09-28

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[I]/[O]** report with **[N]** sandbox numerics. The [N] results are exploratory finite-precision computations; they are reported as structural diagnostics, not as proofs and not as [N-cert].

Author: the project owner's sandbox track (autonomous thread under the owner's assistant). This entry is the result of a falsification test designed by the project owner together with the audit thread, executed under a **pre-registered decision rule** quoted verbatim in §0.

Parents: v13.840 (the distributional \(T_a\) realization whose ratios and edge-failure this entry re-tests), v13.838, v13.773, v13.743, Suzuki arXiv v2. Raw deliverables (scripts, results.json, refine_check.json, atrack_lsq.json, full report, STATUS.md) remain in the workspace at `~/workspace/d12/lane_b/sandbox/runs/20260928-165927-bucket2-natural-bc/`; they are not part of this repo.

Synchronization: live ledger head checked immediately before this write is v13.841 (External Audit Round 115). No collision on the present version number. **This entry does not audit v13.841 or earlier.**

## 0. The pre-registered decision rule and the verdict

The project owner, jointly with the audit thread, endorsed **Horn A** (the \(H^1_0\) Dirichlet constraint \(v(\pm A) = 0\) manufactures an \(O(e^A)\) boundary-layer artifact against the exponentially large source \(e^{\pm x}\)) and commissioned this rerun with the falsification criterion stated **verbatim**:

- *If the \(\Theta(e^A)\) growth VANISHES under natural BCs (ratios settle, edge criteria hold): Horn A CONFIRMED — corrected ratios and edge-criteria verdict reported.*
- *If the SAME \(\Theta(e^A)\) growth with the SAME constant \(|c| \approx 0.48\) persists under natural BCs: flips toward Horn B — report plainly as the falsification outcome, do not explain it away.*

**Outcome: Horn A is falsified.** Under natural boundary conditions (full trial space, no forced \(v(\pm A) = 0\)), the computation reproduces the Dirichlet ratios to 1–2% at every \(A\) and shows the same \(\Theta(e^A)/\Theta(Ae^A)\) growth with the same \(|c| \approx 0.46\)–\(0.48\). Per the pre-registered rule, the evidence flips to **Horn B: the edge criteria (v13.743 onward) are misformulated, not the computation.**

## 1. [D] Form-domain evidence (Round 101 + direct PDF verification)

External Audit Round 101 (ledger v13.796) established, verified by the auditor directly against Suzuki's PDF; the sandbox thread re-verified each point against `~/workspace/d12/cache/research-notes/2606.09096v2.pdf`:

- v13.784 caught this track's own earlier error (v13.779 §4): assuming the deficiency vectors \(v_\pm\) lie in \(H^1_0(-a,a)\) (hence vanish at \(\pm a\)) to justify an endpoint-integral reconstruction.
- Suzuki's construction: \(\mathfrak{D}(D_a^*) \subset \{v \in H(T_a) \mid v \in H^1(-a,a),\; A_a v \in H^1(-a,a)\}\) (**p.21 — no Dirichlet condition**).
- \(\mathfrak{D}(A_a) \supsetneq \mathfrak{D}(B_a) = H^1_0(-a,a)\), **containing constants** (p.4, verbatim: "strictly larger than \(\mathfrak{D}(B_a) = H^1_0(-a,a)\) and contains functions such as constants").
- **Theorem 1.1:** \(A_a\) is the **Friedrichs extension** of \(B_a\); (1.6): \(B_a := D^* G_a D\), \(\mathfrak{D}(B_a) = H^1_0(-a,a)\).
- Lemma 3.1 proof: the form domain \(\mathfrak{D}(Q)\) is the \(Q\)-norm closure of \(C_c^\infty\), shown to contain all Fourier exponentials \(e_n(x) = e^{i\pi n x/a}\) (hence constants) via a cutoff argument — strictly larger than \(H^1_0\).
- **Lemma 6.2:** \(T_a = A_a - \lambda I\) is **invertible for \(\lambda < \lambda_a\)**; the equations \((T_a v)(x) = C_\pm e^{\pm x}\) then admit **unique** solutions spanning the deficiency eigenspaces.
- (8.4)/(8.5) (pp.29–30) with \(k(x,y) = g(x-y) - \lambda N(x,y)\), where \(N(x,y) = (x^2+y^2)/(4a) - |x-y|/2 + a/6\) — the Neumann Green's function \(K_a = (-\Delta_N)^{-1}\) (p.29); the thread verified \(\partial^2_x N = 1/(2a) - \delta(x-y)\) by finite-difference check (\(N_{xx} = 1/(2A)\) to \(10^{-4}\)).
- **p.30:** *"Since the kernel in (8.5) is continuous, it is an ordinary Fredholm integral equation of the first kind. This observation suggests a numerical approach. One may compute \(v_\pm(a,x)\) by solving this Fredholm equation numerically."*

These are ledger/audit-established and PDF-verified; the domain mismatch the Horn A test was built on is confirmed as fact, which is what makes the falsification meaningful rather than a setup error.

## 2. [N] Honest negative: the natural-BC weak form is P1-unstable; pivot to Suzuki's (8.5)

The task's originally specified method — the P1 weak form with the trial space enlarged to include constants — **does not work**:

1. **\(\lambda = 0\) is singular in the correct space** (proof, not numerics): constants satisfy \(a(c,\cdot) = 0\) (since \(c' = 0\)), so \(S\mathbf{1} = 0\) exactly (measured \(\|S\mathbf{1}\|/\|S\| = 2.5\times 10^{-17}\)), while \((e^{\pm x}, 1) = \pm 2\sinh(A) \neq 0\). The discrete system is inconsistent at \(\lambda = 0\). (The prior \(H^1_0\) build's \(\lambda = 0\) was well-posed only because Dirichlet excludes constants — the wrong space regularizing the wrong regime.)
2. **The P1 discretization of the natural-BC weak form is unstable.** The discrete form matrix has a negative generalized eigenvalue blowing up like \(-2.42/h\) under refinement (\(-30.5\) at \(N=50\) → \(-121.1\) at \(N=200\), \(A=2\)) — the signature of a discretization artifact, not a continuum eigenvalue. The mode is high-frequency oscillatory (19 sign changes) with endpoint concentration; a well-resolved \(H^1_0\) test function gives \(a(u,u) = +1.616 > 0\), confirming the continuum form is positive on resolved functions and the negative mode is spurious (P1's piecewise-constant derivatives interacting pathologically with the nonlocal kernel at the endpoints).

This is reported as what it is: the weak-form route is not a viable numerical method here, and naive full-\(H^1\) P1 ("just deleting the Dirichlet rows") is exactly what fails. The computation **pivots to (8.5) directly** — the Fredholm equation Suzuki himself proposes for numerics — via regularized least squares on the full P1 (natural) trial space: \(\min \|Kv_h + e^{\pm x} + Ax + B\|^2 + \alpha\|v_h\|^2_{L^2}\) with \(k = g - \lambda N\) (\(N\)-term via per-element Gauss quadrature split at \(y = x\) for the \(|x-y|\) kink; \(g\)-term via the kink-faithful \(g_{\text{fast}}\) from v13.840). The affine fit is intrinsic to (8.5)'s structure (integration constants), unchanged; \(I_1^\pm = A_\pm \pm 1\), \(I_0^\pm = B_\pm + 1\) per the PDF's definitions.

**Gate validation** ((8.5) residual mod affine): refinement at \(A=3\), \(\lambda=-1\), natural: \(1.38\times 10^{-3} \to 2.35\times 10^{-4} \to 4.12\times 10^{-5} \to 8.13\times 10^{-6}\) (\(N=30\to 240\), ~\(N^{-2}\)); at \(\lambda=0\), natural: \(2.09\times 10^{-3} \to 3.82\times 10^{-4} \to 7.69\times 10^{-5} \to 1.5\times 10^{-5}\). A-track gates: \(10^{-5}\)–\(10^{-4}\) throughout. The discretization is self-consistent.

**\(\lambda = 0\) subtlety resolved:** (8.5) at \(\lambda = 0\) uses the integral operator \(K_0 = G_a\) (compact), **not** the singular Friedrichs \(A_a\). There is no contradiction in (8.5) being solvable at \(\lambda = 0\) while \(A_a v = e^{\pm x}\) is not — they are different operators. The (8.5)-at-\(\lambda=0\) computation is legitimate, and its convergence under refinement confirms it.

## 3. [N] The falsification: natural vs Dirichlet A-track (\(\lambda = 0\))

| A | natural \(r_1^+\) | natural \(r_0^+\) | \(\|r_1\|/(e^A/A)\) nat / dir | \(\|r_0\|/e^A\) nat / dir |
|---|---|---|---|---|
| 2 | −2.490 | +6.717 | 0.674 / 0.667 | 0.909 / 0.900 |
| 3 | −8.609 | +26.909 | 1.286 / 1.279 | 1.340 / 1.325 |
| 4 | −24.611 | +101.474 | 1.803 / 1.777 | 1.859 / 1.838 |
| 5 | −68.682 | +349.180 | 2.314 / 2.281 | 2.353 / 2.335 |

The natural-BC ratios agree with Dirichlet to **1–2%** at every \(A\); the normalized growth curves are indistinguishable. **Removing the Dirichlet constraint changes essentially nothing.** The normalized ratios \(r_1^+/e^A \to -0.46\), \(r_0^+/(Ae^A) \to +0.47\) — the same constant magnitude as the Dirichlet build.

**The mechanism test, directly.** The owner's hypothesized mechanism: Dirichlet forces \(v(\pm A) = 0\) while the source is \(\sim e^A\) at the boundary, creating an \(O(e^A)\) boundary layer. The natural solution's actual endpoint values:

| A | \(v(-A)\) | \(v(+A)\) | \(e^A\) |
|---|---|---|---|
| 2 | −0.07 | +4.32 | 7.39 |
| 3 | +2.49 | +10.80 | 20.09 |
| 4 | −4.64 | +39.58 | 54.60 |
| 5 | −24.76 | +96.80 | 148.41 |

\(v(+A)\) is indeed exponentially large (\(\sim 0.65\cdot e^A\)) — the solution genuinely lives at \(e^A\) scale at the right endpoint, exactly as the owner intuited. **But forcing it to zero (Dirichlet) does not create the \(\Theta(e^A)\) growth in the ratios** — the natural solution, free to be large at the endpoint, produces the same ratios. The boundary layer is not the cause; the \(e^A\) scale is intrinsic to the solution of the equation with an \(e^A\)-scale source.

**\(\lambda\)-robustness.** A-track at \(\lambda = -1\) (natural, full kernel with \(N(x,y)\) properly implemented): \(r_1/e^A = -0.349 \to -0.436 \to -0.460 \to -0.469\); \(r_0/(Ae^A) = +0.396 \to +0.389 \to +0.405 \to +0.405\). Same \(\Theta(e^A)/\Theta(Ae^A)\) growth, same constant magnitude. The falsification is not a \(\lambda = 0\) fluke.

## 4. Interpretation: what Horn B means

The falsification is clean and specific:

1. **The \(\Theta(e^A)\) growth is intrinsic to (8.4)/(8.5), not a BC artifact.** Two independent discretizations (weak-form Dirichlet from v13.840; (8.5)-LS Dirichlet and natural here), two trial spaces, two \(\lambda\) values — all give \(r_1 = \Theta(e^A)\), \(r_0 = \Theta(Ae^A)\) with \(|c| \approx 0.46\)–\(0.48\).
2. **The edge criteria as stated (\(r_{1,A} = o(e^A/A)\), \(r_{0,A} = o(e^A)\), \(\alpha_A \to 0\)) cannot hold for the true solution** — if the true solution is what these discretizations converge to. Twenty-plus ledger entries of edge-criteria analysis (v13.743 onward) were testing a property the solution does not have.
3. **Why the criteria fail is now understandable:** the source \(e^{\pm x}\) is \(O(e^A)\) at the boundary, the operator is nonlocal, and the solution \(v_\pm\) is genuinely \(O(e^A)\) (witness \(v(+A) \sim 0.65\,e^A\)). The moments \(I_j = (Kv)^{(j)}(0)\) inherit this scale. Demanding \(o(e^A/A)\) was demanding the solution be asymptotically smaller than its own natural scale.

**What would still rescue Horn A:** nothing in these numerics — the test was pre-registered as falsifying, and it falsified. A rescue would require showing the (8.5)-LS converges to the wrong object in *both* trial spaces, which the gate convergence and the 1–2% Dirichlet/natural cross-validation make implausible.

## 5. Caveats and guardrails

1. **Scope of the numerics:** [I]/[O] sandbox [N], not [N-cert]; the (8.5)-LS solution's uniqueness is via Tikhonov minimum-norm — the 1–2% Dirichlet/natural agreement and refinement convergence are the evidence it is the right object.
2. **D12 twist:** the computation uses the \(\chi_{12}\)-twisted D12 screw, not Suzuki's untwisted \(\zeta\) screw.
3. **No claims beyond the sandbox:** no RH, GRH, positivity, or Hilbert–Pólya content.
4. The natural-BC weak-form instability (§2) is itself a caution: the form \(Q\) on the true form domain is not directly accessible to P1; the (8.5) route is the viable numerical path.
5. The withdrawn circular result (\(r_1 = -1\), \(r_0 = -(1+i)\)) stays withdrawn; nothing here touches it.

## Result

\[
\boxed{
\textbf{Horn A falsified (2026-09-28):} \text{ the natural-BC (8.5) computation (gate } 10^{-5}\text{--}10^{-4}\text{, convergent) reproduces the Dirichlet ratios to 1--2\% at every } A \text{ and shows the same } \Theta(e^A)/\Theta(Ae^A) \text{ growth with the same } |c|\approx 0.48. \text{ The edge criteria fail for the true solution, not for a BC artifact. Horn B: the criteria (v13.743+) are misformulated. The next analytic question is what the edge criteria should be, given } \Theta(e^A) \text{ is the solution's natural scale.}
}
\]

This entry supersedes no proof and blocks no work. It records a falsification test run exactly to its pre-registered rule and its verdict, with all honest negatives preserved.
