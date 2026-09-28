# Cone Derivation Ledger v13.844 — Sandbox Bucket 2: What the Edge Criteria Were For, and What They Should Say Now (R0–R3)

Date: 2026-09-28

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[I]/[O]** analytic report with **[N]** recap of previously reported sandbox numerics (v13.840, v13.842). This is analysis, not a falsification test: there is no pre-registered decision rule; evidence is weighed plainly and uncertainties flagged as such. All ledger citations below are to entries read in full during the sandbox run; quotes are verbatim.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request of the project owner. Sandbox-only raw deliverables (full report with verbatim-quote ledger citations, STATUS.md) at `~/workspace/d12/lane_b/sandbox/runs/20260928-194718-bucket2-edge-criteria-reformulation/`; not part of this repo.

Parents: v13.842 (Horn B verdict this entry builds on), v13.840, v13.838, v13.743, v13.745, v13.757, v13.758, v13.773, v13.774, v13.776, v13.779, v13.843 (Round 116 audit PASS of v13.842), Suzuki arXiv v2.

Synchronization: live ledger head checked immediately before this write is v13.843 (External Audit Round 116). No collision on the present version number. **This entry does not audit v13.843 or earlier.**

## 0. What this entry does

v13.842 established Horn B: the edge criteria (\(r_{1,A} = o(e^A/A)\), \(r_{0,A} = o(e^A)\), \(\alpha_A \to 0\); v13.743 onward) demanded the true solution be asymptotically smaller than its own natural scale (\(\Theta(e^A)\)), so the misformulation is in the criteria, not the computation. The question left open was what the criteria *should* say. This entry answers it in two parts:

1. **Archaeology:** tracing v13.743 onward entry-by-entry, the edge criteria were **never admissibility gates on the deficiency vectors**. They were the vanishing condition for the affine contamination \(b_A(\xi) = \beta_A - \alpha_A\xi\) — the *assumption* that the downstream "pure compensated edge source" model applies. Suzuki's deficiency vectors are unique when \(T_a\) is invertible (Lemma 6.2); there was never anything to select. Horn B falsified the downstream assumption, not the solution.
2. **Reformulation (R0–R3):** replacement statements in the solution's own units — normalized limits exist finite (R1), the cancellation identity \(L_0 + L_1 = 0\) (R2, the sharpest analytic target), the affine-corrected edge source with measured remnant (R3), and a renaming from "criteria/gates" to "edge asymptotics" (R0).

## 1. [D] Archaeology: where each criterion entered and what it was meant to enforce

**v13.742** — established Suzuki's actual deficiency equations with the affine coefficients retained as integration constants/boundary data (not assumed to vanish): the affine coefficients are "boundary/domain data lost by twice differentiating the finite equation."

**v13.743 — "Affine Boundary-Coefficient Scaling and Reflection Gate" (origin).** Derived exact reflection relations (\(A_{A,-} = -A_{A,+}\), \(B_{A,-} = B_{A,+}\)), then introduced the inward-coordinate scaling at the right edge \(x = A - \xi\), dividing by the "natural exponential edge scale" \(C_A e^A\):

\[
\alpha_A := \frac{A_{A,+}}{C_A e^A}, \qquad \beta_A := \frac{A A_{A,+} + B_{A,+}}{C_A e^A},
\]

so the scaled edge source is exactly \(e^{-\xi} + \beta_A - \alpha_A\xi\). Stated verbatim: **"The pure exponential edge source is recovered iff \(\alpha_A \to 0,\ \beta_A \to 0\)."** What it was meant to enforce: that the edge source, viewed in inward coordinates at the scale of its own exponential, is the **pure** exponential \(e^{-\xi}\) — the "pure compensated edge source" the paired-transfer machinery (v13.740) and later the Weyl/HB lane needed as input. It was a requirement on the downstream model's input shape, stated as an asymptotic property the solution had to have. Critically, v13.743 §10 already warned (verbatim): "the deficiency vector itself may carry \(e^A\)-scale boundary mass. Therefore no source-faithful argument currently permits setting \(\alpha_A\) or \(\beta_A\) to zero merely because the affine terms are lower degree in \(x\) than \(e^x\). **The correct comparison is amplitude, not functional type.**" The entry's own author flagged that the criteria might fail for exactly the reason Horn B later confirmed. Its §8 gave sufficient growth conditions (\(|I_{1,A}| + |C_A| = o(|C_A|e^A)\) etc.) under which they would hold — sufficient, never claimed necessary.

**v13.745 — "Closed Scalar Moment System."** Translated the criteria into the moment-system/Schur-ratio language (\(M_{1e}/(1+M_{1x}) = o(e^A)\) etc.). Same purpose, new language. (This whole apparatus was retracted by v13.773 §3–4 as incompatible with the source-faithful primitive operator — the "moment closure equations" were basepoint tautologies and the ratios became 0/0.)

**v13.757 — "Corrected Finite Weyl Function as Two Scalar Transforms": the criteria weaken on their own.** Two findings that matter for the reformulation: (i) the Weyl lane's own gate needed only **bounded limits** — §9: "A sufficient route to Weyl convergence is therefore: 1. establish asymptotic limits or controlled expansions \(r_{0,A} = r_{0,\infty} + o(1),\ r_{1,A} = r_{1,\infty} + o(1)\)." Not vanishing relative to \(e^A\) — just stabilization. (ii) The \(o(e^A/A)\) form was introduced as the *weaker sufficient* condition — §10: "any bounded limits \(r_{0,A} = O(1), r_{1,A} = O(1)\) immediately imply \(\alpha_A,\beta_A \to 0\). More generally it suffices that \(r_{1,A} = o(e^A/A),\ r_{0,A} = o(e^A)\)." And: "**the same two scalar feedback ratios control both the affine contamination and the corrected deficiency shape.**" By v13.757 the criteria were explicitly the hinge between the edge-source question and the Weyl-shape question.

**v13.758 — "Boundary Functional Obstruction."** Gave the minimal valid sufficient norm bounds and identified the obstruction: the moments are boundary-functional evaluations, so bulk helix/Weil spectral control alone cannot determine \(r_{0,A}, r_{1,A}\) — "bulk explicit-formula current + two boundary constants are both required." Purpose here: reduce the pure-edge limit to "subcritical growth of these two boundary-response quotients."

**v13.773 — the retraction that kept the criteria.** Retracted the Schur-denominator program (the ratios \(M_{0e}/(1+M_{00})\) are 0/0 under the source-faithful operator) but §5 restored the direct ratios \(r_{0,A} := I_{0,A}/C_A,\ r_{1,A} := I_{1,A}/C_A\) with the exact identities \(\alpha_A = -e^{-A}(1 + r_{1,A})\), \(\beta_A = -e^{-A}[A(1 + r_{1,A}) + 1 + r_{0,A}]\), and §7 item 5 kept "only then test \(r_{1,A} = o(e^A/A),\ r_{0,A} = o(e^A)\) or the sharper combined v13.743 edge criterion" — to be applied AFTER determining the ratios "from Suzuki's actual deficiency-domain normalization/global endpoint conditions" (§7 item 4), the item v13.838 recommended rewording because Suzuki's text provides no such conditions.

**v13.774 — the affine-corrected edge equation (completion retracted, [D] parts retained).** The structurally important parts, never retracted: §2 — under the inward derivative, "the slope constant \(\alpha_A\) survives one derivative as a constant source; both affine constants disappear from the twice-differentiated interior current; \(\beta_A\) survives only as primitive value/boundary data." §3 — the source-faithful edge problem with the affine remnant explicit: **"The pure compensated problem of v13.733 is the special case \(\alpha_A = \beta_A = 0\)."** §4 — the two constants enter the half-line problem through the zero-frequency principal parts \(\beta_A/p,\ -\alpha_A/p^2\). **v13.774 already built the slot the reformulation needs: the corrected edge equation takes \((\alpha_A,\beta_A)\) as input data; purity was always a special case.**

**v13.776 → v13.779 — bypass claimed, then retracted.** v13.776 claimed finite Weyl data bypass the primitive constants entirely; v13.779 (Round 98 HOLD resolution) retracted that claim as statements about Suzuki's actual finite deficiency vectors. The remaining routes (§8): **Route A** — stay primitive, solve the parity first-kind equations (E),(O) "subject to the actual deficiency normalization/domain conditions"; **Route B** — derive a genuine transported boundary theorem. Consequence: the primitive problem is unavoidable for the finite Weyl lane, so the edge asymptotics are live data the program needs — in corrected, nonzero form.

**The single most important archaeological finding:** at no point were the edge criteria conditions for the *admissibility* of the deficiency vectors in Suzuki's construction. Suzuki's deficiency vectors are unique when \(T_a\) is invertible (Lemma 6.2) — there is nothing to select. The criteria asked whether the unique solution's affine contamination vanishes, because a downstream model (pure compensated edge → paired transfer → Weyl) had been built on the assumption that it does. The Horn B verdict falsified the assumption, not the solution.

## 2. [N] What the numerics establish (recap of v13.840/v13.842, both runs)

- \(r_1^+/e^A \to -c,\ r_0^+/(Ae^A) \to +c\), \(c \approx 0.46\)–\(0.48\): two discretizations (weak-form Dirichlet; (8.5)-LS Dirichlet and natural), two trial spaces, two \(\lambda\) values (0 and −1, full \(N(x,y)\) kernel). Exact reflection symmetry \(r_1^- = -r_1^+\), \(r_0^- = r_0^+\).
- \(\alpha_A^+ \to +0.48 \neq 0\); \(\beta_A^+ \to 0\) (\(-0.641, -0.251, -0.141, -0.087, +0.009\) across \(A = 2\ldots 6\)).
- \(v(+A) \sim 0.65\,e^A\): the solution genuinely lives at \(e^A\) scale at the boundary.
- Gates: (8.5) residual mod affine \(10^{-5}\)–\(10^{-4}\), collapsing under refinement — the discretizations solve Suzuki's equation; the affine fit is intrinsic to (8.5).

## 3. The reformulation: R0–R3

### R1 — existence of normalized limits (replaces both \(o(\cdot)\) conditions)

\[
\boxed{
L_1 := \lim_{A\to\infty}\frac{r_{1,A}^+}{e^A}\ \text{exists and is finite}, \qquad
L_0 := \lim_{A\to\infty}\frac{r_{0,A}^+}{Ae^A}\ \text{exists and is finite}
}
\]

Numerically \(L_1 \approx -0.48,\ L_0 \approx +0.48\). This is the criteria stated in the solution's own units: strictly weaker than \(r_{1,A} = o(e^A/A)\), strictly stronger than nothing — it asserts the solution has a definite asymptotic shape rather than vanishing contamination. Support: v13.743 §10 anticipated "\(e^A\)-scale boundary mass"; the numerics confirm convergence, not just boundedness. (Note: even v13.757's weaker Weyl gate, \(r_{j,A} \to r_{j,\infty}\), fails for the computed object since \(r_1 = \Theta(e^A)\); R1 is its correct analogue at the true scale.)

### R2 — the cancellation identity (the surviving content of the \(\beta\)-criterion)

\[
\boxed{
L_0 + L_1 = 0 \qquad\Longleftrightarrow\qquad \beta_A^+\ \text{stays finite (numerically }\to 0\text{)}
}
\]

Derivation: \(\beta_A = -e^{-A}[A(I_{1,A} + C_A) + I_{0,A} + C_A]\); with \(I_{1,A} \sim L_1 e^A,\ I_{0,A} \sim L_0 Ae^A\), finiteness of \(\beta_A\) is exactly \(L_0 + L_1 = 0\). The old \(\beta\)-criterion conflated "the constant term is small" with what is really a precise structural identity between the two leading exponential coefficients. The numerics support it (\(\beta_A^+ \to 0\) through five A-values), but the equality \(c_1 = c_0\) is unexplained — **it is the sharpest analytic target to come out of this reformulation.** If \(L_0 + L_1 \neq 0\), then \(\beta_A \sim -(L_0 + L_1)A \to \pm\infty\) and the edge source has no finite affine limit (weaker fallback: \(\beta_A/A\) converges). Note the normalization asymmetry the sandbox tables flagged: the \(\beta_A^-\) computed with the \(-\)channel's own normalization diverges \(\sim -0.95A\), but per v13.743 §5 the left edge in inward coordinates carries the *same* \((\alpha_A,\beta_A)\) as the right edge — the divergent \(\beta^-\) is the wrong normalization applied to the wrong channel, not a second independent fact.

### R3 — the affine-corrected edge source (replaces "pure compensated edge")

\[
\boxed{
\text{inward-coordinate edge source} \longrightarrow e^{-\xi} + \beta_\infty - \alpha_\infty\xi, \quad
(\alpha_\infty,\beta_\infty) = (-L_1,\ \text{finite}) = (0.48,\ 0)
}
\]

The corrected edge equation already exists (v13.743 §9): \(S_{\text{edge}}q_\pm = \pm i(e^{-\xi} - \delta_0) + \mathcal{B}_{\alpha,\beta,\pm}\). The reformulation feeds it the measured pair instead of \((0,0)\). Via v13.774 §4, the boundary data then reduce to a single zero-frequency principal part \(-\alpha_\infty/p^2 = -0.48/p^2\) (the \(\beta_\infty/p\) term vanishes). The downstream question becomes whether the paired-transfer/Weyl machinery can absorb a known linear remnant — a concrete analytic task, not a vanishing assumption.

### R0 — rename: from "criteria" to "edge asymptotics"

The old language ("criteria," "gates") framed the statements as conditions the solution must pass. Since the solution is unique (Lemma 6.2, where applicable) and the statements are properties to be proven about it, the honest name is **edge asymptotics**: conjectured (numerically supported) asymptotic data \((L_0, L_1)\), equivalently \((\alpha_\infty,\beta_\infty)\), that the corrected edge equation takes as input.

## 4. Directed evaluations

**(a) Boundedness of normalized ratios as the admissibility test.** Right form, wrong noun: the numerics show convergence, and nothing is being "admitted." v13.757's Weyl gate itself asked only for bounded limits; R1 is its correct analogue at the true scale. Nothing in v13.743+ contradicts R1; v13.743 §10 anticipates exactly this scale. Suzuki's text is silent on the asymptotics ("ignores domain issues," p.30) — no contradiction, but no support either: R1 is a conjecture about the true solution, numerically supported for the computed selection (see §5).

**(b) Does the \(\alpha/\beta\) language survive?** Yes, but with limits instead of vanishing: \((\alpha_A,\beta_A) \to (\alpha_\infty,\beta_\infty) = (0.48, 0)\). The \(\alpha\)-criterion as stated (\(\to 0\)) is simply false and should be retired. The \(\beta\)-criterion survives in transmuted form as R2, the cancellation identity — arguably the deepest of the three, since it equates the two leading coefficients.

**(c) Residue vs. growth: what was the growth criterion buying?** They answer different questions, and the residue cannot substitute. The gate ((8.5) residual mod affine, \(10^{-5}\)–\(10^{-4}\)) tests whether a *computed* \(v\) satisfies Suzuki's equation — a check on the numerics, satisfiable by any correct solve regardless of its \((\alpha,\beta)\). The growth criteria tested a property of the *continuum* solution, and what they were buying was **license to drop the \(\mathcal{B}_{\alpha,\beta,\pm}\) remnant** from the corrected edge equation. Under the reformulation that license is replaced by the measured remnant: the corrected edge equation needs \((\alpha_\infty,\beta_\infty)\) as input data, and the new criterion is that these limits exist and are finite (R1+R2). The residue keeps its job (validating solves); it never had the growth criteria's job.

**(d) Does Lemma 6.2 uniqueness make the criteria redundant?** No — but it reclassifies them. Uniqueness (where \(T_a\) is invertible, \(\lambda < \lambda_a\)) means there is exactly one candidate, so the criteria were never selecting among solutions; they were asserting a property (vanishing contamination) of the unique solution. The assertion is false, but the *question* — what is the unique solution's edge shape? — is not redundant; it is answered (numerically) by R1–R3. One caveat: Lemma 6.2's invertibility is proven only for \(\lambda < \lambda_a\) with the sign of \(\lambda_a\) unknown, so uniqueness at the computed \(\lambda = 0\) is itself unproven — the reclassification as "properties of the unique solution" is conditional on closing that gap (see §5).

## 5. Judgment calls vs. what is determined

**Determined (text or numerics):**

1. [D, v13.743] The edge criteria as stated (\(\alpha_A,\beta_A \to 0\); \(r_{1,A} = o(e^A/A)\); \(r_{0,A} = o(e^A)\)) were the pure-compensated-edge condition — a downstream modeling assumption, never an admissibility condition on the deficiency vectors.
2. [D, v13.773] The Schur-ratio route to the criteria is retracted; the direct ratios \(I_j/C\) are the correct objects.
3. [D, v13.774 retained parts] The corrected edge equation has an explicit \((\alpha_A,\beta_A)\) slot; purity was always the special case.
4. [D, v13.779] The v13.776 bypass is retracted; the primitive route (Route A) is unavoidable for the finite Weyl lane — the edge asymptotics are live data, not separable.
5. [N, two runs] \((L_0,L_1) \approx (+0.48,-0.48)\); \(\beta_A^+ \to 0\); gates \(10^{-5}\)–\(10^{-4}\) collapsing under refinement; exact reflection symmetry.
6. [D, v13.743 §10] The \(e^A\)-scale possibility was anticipated in the ledger before any numerics.

**Judgment calls / open analytic items:**

1. **Selection.** The quoted \((L_0,L_1)\) are for the Tikhonov minimum-norm selection of the (8.5)-LS solve; affine functions lie in \(\mathrm{Ran}(K_A)\) to machine precision (2D near-nullspace), so (8.5) alone does not fix \((I_0,I_1)\). Whether minimum-norm equals Suzuki's \(v_\pm\) is exactly the v13.773 §7-item-4 program ("Suzuki's actual deficiency-domain normalization"), for which v13.838 found the text provides no conditions. The reformulation is conditional on this identification.
2. **\(L_0 + L_1 = 0\).** Numerically supported through five A-values; analytically unexplained. The sharpest single target: prove the cancellation or find the mechanism.
3. **\(\lambda_a\) sign.** Lemma 6.2 uniqueness at \(\lambda = 0\) unproven; the \(\lambda = -1\) A-track (same growth) mitigates but does not close it.
4. **D12 twist.** All numerics use the \(\chi_{12}\)-twisted screw, not Suzuki's untwisted \(\zeta\) screw; the constants' values may be twist-dependent even if the \(\Theta\)-scale is not.
5. **Downstream absorption.** Whether the paired-transfer/Weyl machinery can carry the \(-0.48/p^2\) remnant (v13.774 §4) is the concrete next analytic task; this entry does not attempt it.

## Result

\[
\boxed{
\textbf{Reformulation (2026-09-28):} \text{ retire } r_{1,A} = o(e^A/A),\ r_{0,A} = o(e^A),\ \alpha_A \to 0 \text{ as stated. Replace with: (R1) the normalized limits } L_1 = \lim r_{1,A}^+/e^A,\ L_0 = \lim r_{0,A}^+/(Ae^A) \text{ exist finite } (\approx -0.48,+0.48); \text{ (R2) the cancellation identity } L_0 + L_1 = 0 \text{ (the surviving content of the } \beta\text{-criterion);} \text{ (R3) the inward edge source tends to } e^{-\xi} + \beta_\infty - \alpha_\infty\xi \text{ with } (\alpha_\infty,\beta_\infty) = (0.48,0), \text{ fed into the already-existing corrected edge equation (v13.743 §9) instead of the pure special case.} \text{ Rename "criteria/gates" to "edge asymptotics": they describe the unique solution, they never selected it.}
}
\]

This entry supersedes no proof and blocks no work. It records the archaeology (entry-by-entry, verbatim quotes) and the candidate reformulation, with all judgment calls preserved as open.
