# Cone Derivation Ledger v13.838 — Sandbox Bucket 2 Gap Characterization: Suzuki's Text Provides No Two Linear Nullspace-Fixing Conditions

Date: 2026-09-28

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation, per the owner's standing instruction:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing exploratory here is certified and nothing here alters a certified result.

Status: **[I]/[O]** report with **[D]** catalog components and **[N]** sandbox numerics. The [N] results are exploratory finite-precision Nyström computations from sandbox scripts (Gauss–Legendre, A ≤ 5, n ≤ 192); they are reported as structural diagnostics, not as proofs and not as [N-cert].

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by explicit request of the project owner, who authorized this entry's promotion from the sandbox. This is the first sandbox-track contribution to enter the ledger. The thread's raw deliverables (scripts, results.json, full reports, STATUS.md) remain in the workspace at `~/workspace/d12/lane_b/sandbox/runs/20260928-120000-bucket2-boundary-constants/`, `.../20260928-150847-bucket2-normalization-audit/`, and `.../20260928-151744-bucket2-extra-conditions/`; they are not part of this repo.

Parents: v13.773, v13.742, v13.779, v13.760, v13.833. Source: Suzuki arXiv v2 (`2606.09096v2`, also present in this repo at `unified/discriminant-12-return/research-notes/2606.09096v2.pdf`), read directly.

Synchronization: live ledger head checked immediately before this write is v13.837 (External Audit Round 113), branch `master`. No collision on the present version number. **This entry does not audit v13.834–837**; that is ordinary audit business.

## 0. What this entry does

It sharpens v13.833's Bucket 2 item from "genuinely open, untouched since v13.779" to a **precisely characterized gap**: Suzuki's text, as written, does not supply two independent linear scalar conditions that fix the \((I_0, I_1)\) boundary-integration constants of the self-consistent first-kind equation (8.5). The exhaustive catalog (§1) is verifiable against the v2 PDF and is tagged [D]; the numerical confirmation of the resulting 2D nullspace (§2) is tagged [N] (sandbox, exploratory). It also records a retraction (§3): an earlier sandbox headline ("\(r_1=-1\) exact under Suzuki's normalization") was circular and is withdrawn here. It recommends one rewording (§5) and states exactly what would close the gate (§6).

## 1. [D] Exhaustive catalog: what Suzuki §§6–8 actually contain

Read directly from the v2 PDF. Every candidate "extra condition" capable of fixing the \((I_0,I_1)\) nullspace of (8.5) is listed; there is no remainder.

**1.1 Theorem 1.5 normalization (§6.4; theorem statement p.6; proof normalization p.22).** [D]

> "Let \(v_\pm(a,x)\) be eigenfunctions of the adjoint operator \(D_a^*\) corresponding respectively to the eigenvalues \(\pm i\), **normalized so that \(\|v_+(a,\cdot)\|_{T_a} = \|v_-(a,\cdot)\|_{T_a}\)**."

> "the deficiency spaces \(\ker(D_a^* \mp i)\) are one-dimensional and are spanned by vectors \(v_\pm = C_\pm v_{\pm i}\) **with the normalization \(\|v_+\|_{T_a} = \|v_-\|_{T_a}\)**."

Assessment: ONE real condition, QUADRATIC in \(v\), COUPLING the \(+\) and \(-\) channels. It fixes the relative scale \(|C_+|/|C_-|\). The ratios \(r_j^\pm = I_j^\pm/C_\pm\) are scale-invariant, so this condition is **irrelevant** to determining them. It cannot fix a 2D *linear* nullspace. Structural; no numerics required.

**1.2 The deficiency eigenvalue equation (8.4) (p.30).** [D]

> "Let \(k(x,y) = g(x-y) - \lambda N(x,y)\). Then the equations \(T_a v_\pm = C_\pm e_{\pm i}\) may be written as \(\int_{-a}^{a} (-k_{xx}(x,y))\, v_\pm(y)\, dy = C_\pm e^{\pm x}\), \(x \in (-a,a)\). **(8.4)**"

Equivalently (§6.2): \(D_a^* v_\pm = \pm i v_\pm\), i.e. \((T_a v_\pm)(x) = C_\pm e^{\pm x}\). Lemma 6.2 proves \(T_a\) invertible for \(\lambda < \lambda_a\), so (8.4) determines \(v_\pm\) — hence \(I_0^\pm = (K_A v_\pm)(0)\), \(I_1^\pm = (K_A v_\pm)'(0)\), and the ratios \(r_j^\pm = I_j^\pm/C_\pm\) — **fully**, up to the free scale \(C_\pm\).

Assessment: this is the TRUE defining equation, but it is the *whole equation* with a *distributional* kernel \(-k_{xx} = -g''(x-y) + \lambda/(2a) - \lambda\delta(x-y)\) (\(g'\) has jump discontinuities at prime-power logs, §2.1: "its first derivative is piecewise continuous with only a discrete set of discontinuities"). It is not "two scalar conditions," and using it as two collocation rows is an invented discretization choice, not Suzuki's (tested in §2; fails).

**1.3 The first-kind equation (8.5) (p.30).** [D]

The self-consistent equation \(-K_A v = C(e^x - 1 - x) - I_1 x - I_0\) with \(M_A v := -(K_A v)(x) + x(K_A v)'(0) + (K_A v)(0)\). Its basepoint evaluations determine \(I_0, I_1\) from \(v\) by *tautology* (v13.773 §2) — they add no information about which \(v\) is selected.

**1.4 Boundary form (6.1)/(8.3) and self-adjoint extensions (§6.4, §8.3).** [D]

\(W(u,v) = \langle D_a^* u, v\rangle_{T_a} - \langle u, D_a^* v\rangle_{T_a}\); \(v \in \mathcal{D}(D_{a,\theta})\) iff \(W(v, w_\theta) = 0\) for \(w_\theta = v_+ + e^{i\theta} v_-\). This characterizes the *extension domain* \(\mathcal{D}(D_{a,\theta})\), not the deficiency vectors \(v_\pm\) themselves. Not applicable.

**1.5 Minimal-domain endpoint data (1.10).** [D]

\(\mathcal{D}(D_a) := C_c^\infty(-a,a)\). The deficiency vectors satisfy \(v_\pm \in \mathcal{D}(D_a^*)\) but \(v_\pm \notin \mathcal{D}(D_a)\). No endpoint values for \(v_\pm\) are stated anywhere. None exist.

**1.6 \(\theta\)-selection (p.30).** [D]

"Our numerical experiments provide evidence supporting (1.12) for the choice \(\theta = \pi\)." Selects the self-adjoint *extension parameter*; says nothing about \((I_0, I_1)\). Not applicable.

**1.7 Searched and absent.** [D]

Full-text search of §§6–8 confirms: **no** endpoint conditions on \(v_\pm\), **no** decay conditions (finite interval), **no** second normalization, **no** linear functional of \(v_\pm\) prescribed to a specific value.

**1.8 No ledger-vs-v2 mismatch.** [D]

Equation (8.5) is present **verbatim** at v2 p.30, with the identical \(A_\pm/B_\pm\) kernel-integral formulas and the identical disclaimer ("(8.5) is different from \(S_a u_\pm = C_\pm \bar{e}_{\pm i}\)"). The ledger (v13.742 §2, v13.282 §6, v13.773 §1) records it faithfully. The reference PDF the project owner uploaded is this same v2 document. There is no competing source.

## 2. [N] Numerical confirmation of the nullspace (sandbox, exploratory)

Finite-A Nyström discretization of the source-faithful (8.5) with the v13.772 kernel (two independent discretizations agreeing to all digits; relative residuals ~1e-12 on the compatibility subspace):

- **Affine functions lie in \(\operatorname{Ran}(K_A)\) to machine precision:** \(K_A v = 1\) solved to \(7\times 10^{-16}\), \(K_A v = x\) to \(2\times 10^{-13}\), at \(A = 1, 2, 3\). Hence \(M_A\) has a genuine 2D near-nullspace and \((I_0, I_1)\) are **undetermined by (8.5) alone** — structural, not a solver artifact. This numerically confirms v13.773 §5 verbatim and explains *why* Bucket 2 is the gate.
- The nullspace persists across \(\lambda \in \{-2, -1, -0.5, 0, +0.5, +1\}\) (affine-in-range residuals 1e-15–1e-13 throughout): not a \(\lambda = 0\) artifact.
- Ledger-faithful self-consistent re-run (\(M_A v = C(e^x-1-x)\), \(A = 2\), \(n = 48 \to 192\)): **\(r_1 \approx +0.47\)–\(0.69\)** (drifting upward with A: \(0.12 \to 10.3\) for \(A = 1 \to 5\)); **\(r_0\) sign-flipping and undetermined** (\(10^4\)–\(10^5\) across refinement); \(\alpha_A \approx -0.2\); \(\beta_A \sim 10^3\).
- Arbitrary collocation fixers (the "two extra conditions" as two rows of (8.4) at \(x_j = \pm A/2\)): 2×2 invertible (det \(1.76\times 10^4\), cond 445, clean even/odd structure) — but the global (8.4) residual is **\(3.0\times 10^3\)**; perturbing the arbitrary collocation points swings \(r_1 \in [-202, +6]\), \(r_0 \in [-450, +1780]\). Algebraically solvable, mathematically meaningless: arbitrary knobs, not a determination.
- Least-squares (8.4) fit over the full (8.5) affine family: residual \(47 \to 7390\) for \(A = 1 \to 5\) — the spline-discretized (8.5) family contains no (8.4) solution.
- Direct spline-(8.4) solve succeeds (cond \(9.3\times 10^3\), residual \(7\times 10^{-14}\)) but violates spline-(8.5) with residual **2.26**: the two discretizations are mutually inconsistent. The kinks in \(g'\) carry the distributional \(-g''\) content linking (8.4)⇔(8.5); spline smoothing destroys it. Suzuki's "formal equivalence" (p.30: "the above argument ignores domain issues") does not survive kink-free discretization — the domain issues are load-bearing.
- One-sided screw treatment (v13.258's screw is one-sided, not even): zero-extension makes the system numerically singular (cond ~\(10^{22}\)); a 1% odd perturbation swings the min-norm \(r_1\) by O(10). The evenness question is only well-posed after the nullspace is fixed.

## 3. Retraction: the earlier sandbox "exact" headline was circular

An earlier sandbox run reported "\(r_1 = -1\), \(r_0 = -(1+i)\) exact under Suzuki's normalization." That headline is **withdrawn**. The run solved \(-K_A v = e^x + i\), which **assumes** \(A_1 = 1\), \(B_1 = 1+i\) — i.e. assumes \(I_1 = -1\), \(I_0 = -(1+i)\) — in the right-hand side. Per (8.5), \(A_\pm/B_\pm\) are *outputs* (functionals of \(v\)), not inputs; the "exact" ratios were baked into the assumed RHS. The run's "+i" justification (a purported §8 equation "\(S_a v_\pm = e^{\pm x} \pm i\)") does not exist in the PDF — a fictitious citation, caught by the follow-up audit. The ledger-faithful re-run's numbers are those of §2. This retraction is recorded here so the circular headline is not quoted back into the project.

## 4. Precise gap statement

\[
\boxed{
\begin{array}{l}
\textbf{Bucket 2, sharpened (2026-09-28):} \text{ Suzuki's text as written does not} \\
\text{determine } (I_0, I_1) \text{ via two independent linear conditions. It provides:} \\
\text{(a) the full deficiency equation (8.4), which determines the ratios } r_j = I_j/C \\
\text{given } T_a \text{ invertible but is not "two conditions" and has a distributional} \\
\text{kernel;} \\
\text{(b) a quadratic inter-channel norm equality (Thm 1.5), irrelevant to the} \\
\text{scale-invariant ratios;} \\
\text{(c) nothing else in §§6–8. The (8.4)⇔(8.5) "formal equivalence" ignores the} \\
\text{kink/domain issues that are load-bearing: the kinks in } g' \text{ at prime-power} \\
\text{logs carry the distributional } -g'' \text{ content linking the two equations.}
\end{array}
}
\]

The [N] contribution of this entry: the 2D near-nullspace of the (8.5) operator is real, \(\lambda\)-robust, and no linear selector exists in §§6–8 — so Bucket 2 is a genuine gap in the *text*, not an oversight in the reading.

## 5. Recommendation: reword v13.773 §7 item 4

v13.773 §7's "correct next gate" — "use Suzuki's actual deficiency-domain normalization/global endpoint conditions to determine \(I_0/C, I_1/C\)" — should be reworded. As written it reads as if the text hands you two linear equations; per §1, it does not. The faithful reading is: **use the full deficiency equation (8.4) with a faithful distributional discretization** — the text supplies the equation, not the two conditions.

## 6. What would actually close the gate

1. **Numerical route:** a faithful *distributional* realization of \(T_a\) — implementing \(-g''\) with its kink deltas (jumps \(\pm c_m\) at \(t = \pm\log m\), \(c_m = \Lambda(m)\chi_{12}(m)/\sqrt{m}\)) instead of spline smoothing — then solving (8.4) directly for \(v_\pm\) and reading off \(I_j = (K_A v_\pm)^{(j)}(0)\). A substantial numerical-analysis project, not a two-line fix.
2. **Analytic route:** prove \(T_a\) invertible at \(\lambda = 0\) (needs \(\lambda_a > 0\), i.e. \(A_a\) positive — the §7 RH-adjacent statement) and characterize the (8.5)→(8.4) selection with the kink structure retained (Wiener–Hopf). [I]

Either route must also control the selector-sensitivity demonstrated in §2 (collocation knobs swinging \(r_1\) over \([-202,+6]\)): whatever fixes the nullspace must be shown to be *the* condition the theory selects, not an arbitrary one.

## 7. Consequences and guardrails

- The edge criteria \(r_{1,A} = o(e^A/A)\), \(r_{0,A} = o(e^A)\) (v13.773 §7) are **untestable** until \((I_0, I_1)\) are determined. They remain untested. The \(\alpha_A, \beta_A\) formulas (v13.743) stand *conditional* on the ratios; no numbers can be attached.
- Nothing in this entry bears on RH, GRH, or Weil/Suzuki positivity (v13.833 Bucket 1); nothing bears on the finite-section certificate program (Bucket 3), whose results stand exactly as stated by their own entries.
- History of the gate, extended by one line: obstruction found (v13.761, v13.765) → partly diagnosed as self-inflicted (v13.773) → "completion" claimed (v13.774) → retracted/bypassed (v13.776) → HOLD (v13.778) → resolved by retraction, not repair (v13.779) → **gap precisely characterized (this entry)**. The problem remains open; it is now open with its missing piece identified.
- All [N] numbers above are sandbox exploratory; the ledger's [N-cert] pipeline has not touched them. The [D] catalog (§1) is checkable by anyone against the v2 PDF in this repo.

## Result

\[
\boxed{
\textbf{Bucket 2 is a genuine gap in Suzuki's text, not in the reading of it: no two linear conditions there fix the 2D nullspace of (8.5); the (8.4)⇔(8.5) link is carried by kink/distributional data that smoothing destroys. The edge criteria are untestable until a distributional realization of } T_a \textbf{ or an analytic selection principle closes the nullspace.}
}
\]

This entry supersedes no proof and blocks no work; it exists so the Bucket 2 gate can be attacked with its actual missing piece — the kink-faithful \(T_a\) — named.
