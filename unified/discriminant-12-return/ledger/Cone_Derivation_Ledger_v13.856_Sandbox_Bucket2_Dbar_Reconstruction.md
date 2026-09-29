# Cone Derivation Ledger v13.856 — Sandbox Bucket 2: D̄ Reconstruction and the Two Routes Forward

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[D]** ledger-archaeology report (every formula below is cited to the ledger version where it appears; quotations verbatim) with **[I]** reconciliation and **[O]** open items. No new numerics in this entry.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request of the project owner. Full reconstruction note (for-review, not part of this repo) at `~/workspace/d12/lane_b/sandbox/runs/20260929-dbar-reconstruction/Dbar_Reconstruction_ForReview.md`.

Parents: v13.855 (bulk lemma refined), v13.854 (W3 Route-B skeleton, which invokes D̄), v13.784, v13.776, v13.777, v13.785, v13.725, v13.740, v13.757, v13.667, v13.732, v13.721, v13.724, v13.779, v13.282, v13.278, v13.279.

Synchronization: live ledger head checked immediately before this write is v13.855. No collision on the present version number. **This entry does not audit v13.855 or earlier.**

## 0. What this entry does

1. **Reconstruction.** Pins down, from the ledger record alone, the exact definition and boundary/distributional action of the transport operator D̄ ("Dbar", written `\bar{D}` / `\bar D`) that the W3 Route-B skeleton (v13.854) invokes as \(S_A u_{A,\pm} = \bar{D}e_{\pm i} + \mathcal{B}_{A,\pm}\). The reconstruction separates what the ledger establishes **[D]** from interpretation **[I]** and what remains open **[O]** — including one live contradiction and one false-friend naming collision.
2. **Verdict.** The ledger gives D̄'s definition and action completely but provides **no closed-form evaluation** of \(\bar{D}e_{\pm i}\); every quantitative use must go through the approximant limit or the conditional edge profile. The \(\propto e^{\pm x}\) shortcut is exactly the retracted move.
3. **Charter.** The project owner has authorized pursuing **both** routes simultaneously: **(Route E)** proving the \(A \to \infty\) edge-energy limit, and **(Route T)** upgrading the moment-pairing proxies to \(G_A/H_A\) pairings via the \(T_a^{-1}\) side per v13.785.

## 1. [D] What D̄ is

Suzuki's **isometric transport**: the unique continuous extension of \(D = i\,d/dx\) (core \(C_c^\infty(-a,a)\), i.e. \(H_0^1 \to L_0^2\)) to an isometric isomorphism

\[
\boxed{\bar{D}:\mathcal{H}(T_a)\overset{\sim}{\longrightarrow}\mathcal{H}(S_a)}
\]

between the \(T_a\)-energy and \(S_a\)-energy completions, where \(T_a = A_a - \lambda I\) (\(\lambda < \lambda_a\)), \(S_a = G_a - \lambda K_a\), \(K_a = (-\Delta_N)^{-1}\). (v13.667 §1; v13.784 §1 after Audit Round 100.)

The audit's disambiguation (v13.732, verified directly against the Suzuki PDF pp. 28–30): D̄ is an isomorphism *between two different Hilbert completions*, not a differential operator within one space. The latter is the distinct \(\tilde{D}_a := DD_aD^{-1}\), which acts as \(i\,d/dx\) only on the core domain \(C_c^\infty(-a,a) \cap L_0^2(-a,a)\).

**Constructive form** (v13.725 §1): for cutoff approximants \(v_{\varepsilon,A}(x) = e^x\chi^R_{\varepsilon,A}(x)\chi^L_{\varepsilon,A}(x) \in C_c^\infty(-A,A)\) with \(v_{\varepsilon_n,A} \to e^x\) in \(\mathcal{H}(T_A)\),

\[
\boxed{\bar{D}e_{+i} = \lim_{n\to\infty} Dv_{\varepsilon_n,A}\quad\text{in }\mathcal{H}(S_A)}
\]

"by definition of the isometric extension." Parallel K-version (v13.282): \(\bar{D}:\mathcal{H}(T_{K,a}) \xrightarrow{\sim} \mathcal{H}(S_{K,a})\).

⚠️ **False friend.** `Dbar_{a,theta}` (no bar, subscripted) in v13.278/279 is a **different object**: the self-adjoint extension in Suzuki's von Neumann parameterization ("Its zeros are exactly the eigenvalues of the self-adjoint extension `Dbar_{a,theta}`, hence all zeros are real" — v13.278). Near-identical names, unrelated objects. Every `\bar D` below is the transport map.

## 2. [D] What D̄ does

- **Deficiency transport** (v13.667 §2; v13.784 §1): \(u_\pm = \bar{D}v_\pm\); \(\widetilde{\mathscr D}_a^*u_\pm = \pm i u_\pm\); \(\|u_+\|_{S_a} = \|u_-\|_{S_a} = \sqrt{h_a}\).
- **Defect equation** (v13.784 §4, reinstated after Round 100; v13.667 §4; v13.797): \(\boxed{S_au_\pm = C_\pm\bar{D}e_{\pm i}}\) — "exact at the abstract/projected transported-operator level," from \(S_a = \bar{D}T_a\bar{D}^{-1}\) and \(T_av_\pm = C_\pm e_{\pm i}\). Also \(S_au_z = \bar{D}e_z\) for regular \(z\). ⚠️ **Normalization conflict:** v13.740 states \(S_Au_z = \bar{D}e_z,\ S_Au_\pm = \bar{D}e_{\pm i}\) **without** \(C_\pm\) ("up to the fixed deficiency normalizations"); v13.740 line 145 flags this as convention-sensitive.
- **Boundary-triple transport** (v13.667 §§2–3): \(\widetilde\Gamma_j = \Gamma_j\bar{D}^{-1}\); \(\boxed{\widetilde\gamma_a(z) = \bar{D}\,\gamma_a(z)}\); Weyl function exactly invariant, \(\widetilde m_a(z) = m_a(z)\); \(\widetilde{\mathscr D}_a = \bar{D}\mathscr D_a\bar{D}^{-1}\).
- **Parity** (v13.784 §7): \(\boxed{\bar{D}R = -R\bar{D}}\) — extends by continuity from \(DR = -RD\) on the core; D̄ reverses parity abstractly, no endpoint calculus needed.
- **Inverse** (v13.784 §5): \(S_a^{-1} = \bar{D}T_a^{-1}\bar{D}^{-1}\) on the energy-space realization; \(u_\pm = C_\pm S_a^{-1}\bar{D}e_{\pm i}\) valid **only** in this sense — not raw kernel inversion, not deletion of (8.5)'s affine terms.
- **Pairing formulas:** \(F_{A,\pm}(z) = \overline{\langle\bar{D}e_{\bar z}, S_A^{-1}\bar{D}e_{\pm i}\rangle}}\) (v13.740 §2); v13.757 uses \(\overline{\langle\bar{D}e_{\bar z}, R\mathcal{U}_A\rangle}\), \(\overline{\langle\bar{D}e_{\bar z}, \mathcal{U}_A\rangle}\) with \(\mathcal{U}_A := \bar{D}w_A\); parity sectors \(S_A^{(+)}u_e = \bar{D}(\cosh x),\ S_A^{(-)}u_o = \bar{D}(\sinh x)\) (v13.776 §3).

## 3. [D] Negative characterization — what D̄ is not

- D̄ is **not** ordinary differentiation on the completion: \(\bar{D}(\mathbf{1}_{[-a,a]}) \neq 0\) with \(\mathbf{1}_{[-a,a]} \in \mathcal{H}(T_a) \setminus \mathfrak{D}(D_a)\) — both verbatim in Suzuki per v13.732.
- \(\mathcal{H}(S_a) \not\subset L^2\), whereas \(\mathcal{H}(T_a) \hookrightarrow L^2(-a,a)\). (v13.784 §1)
- \(\bar{D}v_\pm \neq iv_\pm'\) without independent \(H_0^1\) regularity.
- \(\bar{D}e_z = z e_z\) is **not established** — v13.721's claim was **retracted** by v13.724; audit v13.732 independently confirmed against the Suzuki PDF and disclosed Round 85's pass as a verification gap.
- Ordinary \(x\)-differentiation of (8.5) \(\neq\) application of D̄ (v13.784 eq. 2); raw Fredholm (8.5) \(\neq\) \(S_a\) as operator realizations.

## 4. [D, conditional] Distributional edge profile (v13.725 §§3–7)

Right edge, \(e^{-A}\) normalization, inward coordinate \(\xi\):

\[
\boxed{F_{+,{\rm dist}}^{\rm edge} = i(e^{-\xi} - \delta_0)} \qquad\text{left edge: } -i(e^{-\xi} - \delta_0).
\]

Zero total mass \(\int_0^\infty (e^{-\xi} - \delta_0) = 1 - 1 = 0\); the \(\delta_0\) coefficient is cutoff-independent (depends only on \(\chi(\infty) - \chi(0) = 1\)). **Conditional** on three missing ingredients (v13.725 §6): existence of the \(A \to \infty\) edge-energy limit, continuity of distributional testing, \(\delta_0\)'s membership in the dual/completion.

**[I]** reading: the \(\delta_0\) is the analytic content of "not ordinary differentiation" at the edge — the approximants' cutoff derivatives concentrate into \(-i\delta_0\), compensating bulk \(ie^{-\xi}\) to preserve the core derivatives' zero mean. Dropping it (treating \(\bar{D}e_{\pm i}\) as plain \(e^{\pm x}\)) is exactly the error v13.785 supersedes; the dropped boundary term is what the W3 \(\mathcal{B}_{A,\pm}\) functional reconstructs.

## 5. [O] Open items

1. **No closed-form evaluation of \(\bar{D}e_z\) anywhere** — only the approximant limit of §1.
2. The \(A \to \infty\) edge-energy limit's existence (v13.725 §6's three ingredients).
3. The \(C_\pm\) convention across versions (v13.740 drops it, v13.784 keeps it).
4. **Live contradiction, unresolved in-ledger:** v13.776 §3 "[D] \(\bar{D}e_{+i} \propto e^x\)" vs v13.785 §9's supersession of "treating \(\bar{D}e_{\pm i}\) as ordinary scalar multiples of \(e^{\pm x}\)". Both cannot stand.
5. The \(\delta_\infty\) identification leg itself.

## 6. Retraction/conflict trail (audit record)

- v13.721's \(\bar{D}e_z = z e_z\) → **retracted** by v13.724.
- v13.742's retraction of \(S_au_\pm = C_\pm\bar{D}e_{\pm i}\) → **itself partially retracted** by v13.784 §4 / Round 100: identity reinstated as exact at projected level; only the raw-(8.5)-as-\(S_a\) reading stays retracted.
- v13.779 §4 endpoint reconstruction (\(v_\pm(\pm a) = 0\) etc.) → **superseded** by v13.784 §2 (\(\mathfrak{D}(A_a) \supsetneq H_0^1\), contains constants).
- v13.777's pointwise \(f_\pm(x) := \bar{D}e_{\pm i}(x)\) and scalar-multiple treatment → **superseded** by v13.785 §9 (Möbius algebra retained, operator realization replaced by rigorous \(T_a^{-1}\) responses).
- W3 sandbox note: retracted v13.776–777 asserted \(S_Au_\pm = \bar{D}e_{\pm i}\) with **no** boundary functional; the sandbox skeleton restores \(S_Au_{A,\pm} = \bar{D}e_{\pm i} + \mathcal{B}_{A,\pm}\) — consistent with the ledger's D̄ as the bulk-source term and \(\mathcal{B}\) as the sandbox-added remnant functional ([I]/[O], not ledger).

## 7. The two routes (chartered by the project owner, 2026-09-29)

**Route E — the edge-energy limit.** Prove the \(A \to \infty\) edge-energy limit whose absence conditions §4: (i) existence of the limit in the edge-energy topology, (ii) continuity of distributional testing under the limit, (iii) \(\delta_0\)'s membership in the dual/completion. Success promotes the edge profile \(i(e^{-\xi} - \delta_0)\) from conditional to derived and gives the first quantitative handle on \(\bar{D}e_{\pm i}\).

**Route T — the \(T_a^{-1}\) side.** Upgrade the moment-pairing proxies to the actual \(G_A/H_A\) pairings **without** evaluating D̄, via rigorous \(T_a^{-1}\) responses per v13.785's replacement of the retracted operator realization: use \(S_a^{-1} = \bar{D}T_a^{-1}\bar{D}^{-1}\) and the pairing formulas of §2 with \(\mathcal{U}_A := \bar{D}w_A\) kept on the \(T_a\)-side. This is the route the ledger's own retraction trail points to.

Both routes are live as of this entry. All conclusions remain conditional on \(\lambda_a > 0\).
