# Cone Derivation Ledger v13.858 — Sandbox Bucket 2: G1–G3 Closed on the T Side

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[I]/[O]** sandbox analytic reports with **[D]** ledger-derived identities. No new numerics in this entry.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request of the project owner. Full gap reports (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-g1-identity/G1_Ra_vs_Ta_ForReview.md`, `~/workspace/d12/lane_b/sandbox/runs/20260929-g2-duality-pairing/G2_Duality_Pairing_ForReview.md`.

Parents: v13.857 (Route T verdict; chartered G1–G3), v13.856, v13.785, v13.784, v13.782, v13.773, v13.757, v13.745, v13.740, v13.725, v13.667.

Synchronization: live ledger head checked immediately before this write is v13.857. No collision on the present version number. **This entry does not audit v13.857 or earlier.**

## 0. What this entry does

Closes the three gaps G1–G3 chartered in v13.857 §3 on the T side of Route T. **G1 closed [D]** (ratio/shape identities, not the obstructed operator identity). **G2 closed [I] at fixed \(A\)** (explicit duality-pairing construction; one hazard H1 remains [O]). **G3 closed [D]** (bookkeeping: the \(C_\pm\) convention fixed). The \(G_A/H_A\) pairings are now rigorous \(T_A\)-side objects at fixed \(A\).

## 1. G1 — the \(R_A^{-1}\) vs \(T_A^{-1}\) identity [D]

**Verdict: closed — as ratio/shape identities already in the ledger, not as an operator identity.**

The two operators side by side:
- **\(L_A = -K_A\)** (Level III, raw primitive first-kind): \((K_Av)(x) = \int_{-A}^{A}k_A(x,y)v(y)\,dy\); formally inverts \(L_Av_A = C_A(e^x-1-x) - I_{1,A}x - I_{0,A}\) (v13.745 (1)); \(R_A := L_A^{-1}\) formal; responses \(u_{e,A} = R_A(e^x-1-x)\), \(u_{1,A} = R_A1\), \(u_{x,A} = R_Ax\) (v13.745 §2). **[D]** (v13.773 §3): any formal inverse satisfies \(\ell_{0,A}(R_Af) = -f(0)\), \(\ell_{1,A}(R_Af) = -f'(0)\); hence \(M_{00} = M_{1x} = -1\), \(M_{0e} = M_{1e} = 0\), and the ratios \(M_{0e}/(1+M_{00})\), \(M_{1e}/(1+M_{1x})\) are **0/0**. **[D]** (v13.773 §4): the \(R_A\) moment program is retracted; \(1, x\) are not independently admissible sources.
- **\(T_A = A_A - \lambda I\)** (Level I, source-level): self-adjoint (via \(S_a = \bar{D}T_a\bar{D}^{-1}\)); \(\mathfrak{D}(A_a) \supsetneq H_0^1\), contains constants (v13.784 §2); invertible for \(\lambda < \lambda_a\) (standing hypothesis). Inverts \(T_Av_\pm = C_\pm e_{\pm i}\) (v13.784 §1); \(T_av_{+i} = e^x\) (v13.785 §1). Responses \(w_e = (T_A^{(+)})^{-1}\cosh\), \(w_o = (T_A^{(-)})^{-1}\sinh\) (v13.785 (1E)(1O)); \(\psi_{j,A} = (T_A^{(\pm)})^{-1}q_{j,A}\) (v13.785 (10)).

What holds **[D]** — the identities Route T needs (v13.782 (6)–(8), v13.785 §§5–6):
- **(a)** \(r_{0,A} := I_{0,A}/C_A = \ell_{0,A}((T_A^{(+)})^{-1}\cosh) = \langle q_{0,A}, w_e\rangle\)
- **(b)** \(r_{1,A} := I_{1,A}/C_A = \ell_{1,A}((T_A^{(-)})^{-1}\sinh) = \langle q_{1,A}, w_o\rangle\)
- **(c)** \(w_A := v_A/C_A = T_A^{-1}e^x = w_e + w_o\) (v13.784 Level I + v13.785 (1E)(1O))

i.e. the *true* boundary ratios (as \(I_j/C\) from the Level-I solution — **not** the 0/0 moment ratios) coincide exactly with v13.785's \(T_A^{-1}\) dual-resolvent pairings, and the corrected shape \(w_A\) **is** the \(T_A^{-1}\)-response to \(e^x\).

What fails **[D]** — the operator identity, precisely obstructed: \(R_A = T_A^{-1}\) has no ledger basis. v13.773's trace identities are *necessary* for any inverse of \(-K_A\); the ledger never identifies \(-K_A\) with \(T_A\). v13.784 §§4,6: the three-level hierarchy explicitly separates Level I (\(T_A\)) from Level III (\(-K_A\)); "the raw Fredholm operator in (8.5) is not literally \(S_a\)" — and by the same token not literally \(T_A\). v13.785 *supersedes* v13.745's \(R_A\) construction rather than equating it. On "the precise difference operator": there isn't a computable correction term — the gap is well-posedness, not a missing summand. \(R_A\) is formal (0/0 on the ratios); \(T_A^{-1}\) is rigorous. The relationship is **replacement, not identity** [I]. What this does to \(\rho_A\): the \(R_A\)-side ratios would leave \(\rho_A\) undefined (0/0); the \(T_A\)-side ratios give a well-defined \(\rho_A\). G1's resolution *saves* \(\rho_A\) by re-grounding it.

Consequence for Route T's \(G_A/H_A\): read \(w_A\) as \(T_A^{-1}e^x = w_e + w_o\) **[D]**, never via the ill-posed \(R_A\) decomposition (v13.757 §7's \(w_A\) must be re-grounded this way — the \(R_A\)-decomposition is superseded, the object \(w_A = v_A/C_A\) survives). Read \(r_{0,A}, r_{1,A}\) as v13.785's \(T_A^{-1}\) pairings **[D]**. Then \(\langle\!\langle e_{\bar z}, w_A\rangle\!\rangle = \langle\!\langle e_{\bar z}, w_e\rangle\!\rangle + \langle\!\langle e_{\bar z}, w_o\rangle\!\rangle\), which — modulo G2's pairing construction — are the \(E_a/O_a\) Fourier pairings. **The G1 block on replacing the abstract pairings with \(E_a/O_a\) is removed.**

Ledger-hygiene note [I]: v13.757 §7's \(w_A\) via \(R_A\)-responses should be annotated as superseded in *construction* but valid in *object* (\(w_A = T_A^{-1}e^x\)); no single ledger entry states (a)–(c) together — this entry now does.

## 2. G2 — the duality pairing, explicitly constructed [I/O]

**Verdict: closed as a fixed-\(A\) construction.** The pairing the ledger invokes but never defines is the **\(T_A\) energy form**.

Ledger collection [D]: every invocation found — v13.740 §2 (\(F_{A,\pm}\)) and §9 (\(P_A(z) = (z-i)\overline{\langle\bar De_{\bar z}, S_A^{-1}\bar De_{+i}\rangle} - (z+i)\overline{\langle\bar De_{\bar z}, S_A^{-1}\bar De_{-i}\rangle}\)); v13.757 §8 (18) (the \(\rho_A\) ratio, "in the appropriate form/duality interpretation") and §9(2) ("a topology strong enough to pass the two scalar pairings"); v13.785 §5 dual-resolvent formulas and §2 Fourier pairings \(E_a(z) = \widehat{w_e}(z)\); Route T T1–T5 (v13.857 §1).

Construction. Imported [D]: \(T_A\) self-adjoint invertible for \(\lambda < \lambda_A\) (v13.784 §1); \(\mathcal{H}(T_A)\) = form-core completion with \(\mathcal{H}(T_A) \hookrightarrow L^2\) continuously (v13.784 §1); \(e^{\pm x} \in \mathcal{H}(T_A)\) with \(C_c^\infty\) approximants \(v_{\varepsilon_n,A} \to e^{\pm x}\) in \(\mathcal{H}(T_A)\) (v13.725 §1); core isometry \(\|Dv\|_{S_A} = \|v\|_{T_A}\) (v13.667 §1); \(S_A^{-1} = \bar{D}T_A^{-1}\bar{D}^{-1}\) energy-space (v13.784 §5).
- **Core [D/I]:** for \(f, g \in C_c^\infty(-A,A)\), \(\langle\!\langle f, g\rangle\!\rangle_{T_A} := t_A(f,g)\), the \(T_A\) energy form.
- **Extension [I]:** \(|t_A(f,g)| \le \|f\|_{T_A}\|g\|_{T_A}\) [D, Cauchy–Schwarz] extends uniquely to \(\mathcal{H}(T_A) \times \mathcal{H}(T_A)\); for the deficiency sources \(\langle\!\langle e_{\pm i}, w\rangle\!\rangle_{T_A} = \lim_n t_A(v^{(\pm)}_{\varepsilon_n,A}, w_n)\).
- **Convention [I]** (fixed once): linear in the second slot, conjugate-linear in the first.
- **\(S_A\)-side "duality" reading [I]:** \(\langle\!\langle\Phi, \Psi\rangle\!\rangle_{S_A} := s_A(\Phi,\Psi)\) with \(\Phi\) viewed in \(\mathcal{H}(S_A)^*\) via the form; then \(\langle S_A^{-1}\Phi, \Psi\rangle_{S_A} = \langle\!\langle\Phi, \Psi\rangle\!\rangle_{S_A}\) [D, Riesz]. **This is what "the appropriate form/duality interpretation" means.**
- **\(\bar{D}\)-transport [I] from [D]:** \(\langle\!\langle\bar Df, \bar Dw\rangle\!\rangle_{S_A} = \langle\!\langle f, w\rangle\!\rangle_{T_A}\) by continuous extension of the core isometry — the identity moving every pairing to the \(T_A\) side with zero \(\bar{D}\) evaluation.

Properties. **(a) Well-definedness [I, proved]:** approximant-independence from form continuity; for \(e_{\pm i}\) the limit element is uniquely pinned because any \(\mathcal{H}(T_A)\)-convergent approximant sequence has \(L^2\)-limit \(e^{\pm x}\) [D, embedding]. **(b) Continuity [D/I, proved]:** \(|\langle\!\langle f, w\rangle\!\rangle| \le \|f\|\|w\|\). This **is** v13.757 §9(2)'s "topology strong enough to pass the two scalar pairings" — G2 supplies exactly what that item asks for. **(c) \(T_A^{-1}\) compatibility [I, proved; instantiates [D] v13.785 §5]:** \(\langle\!\langle f, T_A^{-1}q\rangle\!\rangle_{T_A} = (f, q)_{L^2}\), an honest \(L^2\) integral — the abstract content of the dual-resolvent/edge-Laplace formulas.

Hazards, flagged honestly:
- **H1 [O]:** \(e_z \in \mathcal{H}(T_A)\) for general regular \(z\) is unproved — only \(\pm i\) [D]. Partial dissolve [I]: \(e^{zx} \in L^2\) for **all** \(z\) [D], so the **dual-slot reading** \(\mathcal{H}(T_A)^* \times \mathcal{H}(T_A)\) is rigorous for every \(z\) in the first slot; what remains [O] is identifying that dual functional with the ledger's \(\bar De_{\bar z}\) for regular \(z\) (v13.784 §1 asserts \(S_au_z = \bar De_z\) "for regular \(z\)" without the membership lemma).
- **H2 — resolved by G1 [D]:** \(w_A = T_A^{-1}e^x \in \mathfrak{D}(T_A) \subset \mathcal{H}(T_A)\) since \(e^x \in L^2(-A,A)\).
- **H3 [O, standing]:** \(\lambda_a > 0\) (RH-adjacent); needed for energy-norm equivalence, not for the construction's form.
- **H4 [G]:** the retracted shortcut's exact boundary — SAFE [D]: using \(e_{\bar z}\) as an \(L^2\) function via the embedding (§(c)). UNSAFE (retracted): \(\bar{D}\) as \(i\,d/dx\) on completion elements, \(\bar De_z = ze_z\).
- **H5/H6 [O]:** PAIR-H, R1/R2, DEN-H and the \(A \to \infty\) limit are convergence-leg issues, not needed for the fixed-\(A\) pairing.

## 3. G3 — the \(C_\pm\) convention [D] (bookkeeping)

v13.740 §2 states \(S_Au_z = \bar{D}e_z,\ S_Au_\pm = \bar{D}e_{\pm i}\) "**up to the fixed deficiency normalizations**" — i.e. it absorbs \(C_\pm\) by normalizing \(u_\pm\) (the \(C_\pm = 1\) choice). v13.784 §4 keeps it explicit: \(T_av_\pm = C_\pm e_{\pm i}\), \(S_au_\pm = C_\pm\bar{D}e_{\pm i}\), "with the chosen deficiency normalization". **Canonical choice going forward:** v13.784's explicit form, with \(C_\pm\) fixed by the equal-norm condition \(\|v_\pm\|_{T_A} = \|u_\pm\|_{S_A} = \sqrt{h_a}\) (v13.667 §2; D̄ is an isometry), i.e. \(|C_\pm| = \sqrt{h_a}/\|T_A^{-1}e_{\pm i}\|_{T_A}\) with the phase set by the \(e_{\pm i}\) phase convention. No ledger entry assigns \(C_\pm\) a numerical value; none is needed: \(C_\pm\) cancels in \(\rho_A = H_A/G_A\) and in \(m_A\) (v13.857 T3 [D]) — it is required only for absolute \(G_A/H_A\).

## 4. T-side scorecard and what remains

| Gap | Verdict |
|---|---|
| G1 \(R_A^{-1}\) vs \(T_A^{-1}\) | **Closed [D]** — ratio/shape identities (a)–(c); operator identity obstructed, not needed |
| G2 duality pairing | **Closed [I] at fixed \(A\)** — energy-form construction; H1 open [O] |
| G3 \(C_\pm\) convention | **Closed [D]** — canonical explicit form fixed |

The \(G_A/H_A\) pairings are now rigorous \(T_A\)-side objects at fixed \(A\), with zero D̄ evaluation anywhere in the chain. What remains: **H1** (\(e_z \in \mathcal{H}(T_A)\) for general regular \(z\), or canonize the dual-slot reading — analytic, bounded); the **convergence leg** (PAIR-H, R1/R2 — v13.853's four-hypothesis reformulation); the **identification leg** (the \(\delta_\infty\) discrepancy equation — needs the infinite-volume comparison against Suzuki's construction). All conclusions remain conditional on \(\lambda_a > 0\).
