# Cone Derivation Ledger v13.857 — Sandbox Bucket 2: Route T Reaches the Pairings, Route E Blocked (Structural)

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[I]/[O]** sandbox analytic reports with **[D]** ledger-derived identities. No new numerics in this entry.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request of the project owner. Full route reports (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-route-t-pairings/RouteT_Pairing_Identities_ForReview.md`, `~/workspace/d12/lane_b/sandbox/runs/20260929-route-e-edge-energy-limit/RouteE_EdgeEnergyLimit_Report.md`.

Parents: v13.856 (D̄ reconstruction; chartered both routes), v13.785 (T-side parity/Weyl replacement), v13.784, v13.776, v13.757, v13.740, v13.725, v13.854 (W3).

Synchronization: live ledger head checked immediately before this write is v13.856. No collision on the present version number. **This entry does not audit v13.856 or earlier.**

## 0. What this entry does

Reports the outcomes of the two routes chartered in v13.856 §7: **Route T** (upgrade the moment-pairing proxies to the actual \(G_A/H_A\) pairings via the \(T_A^{-1}\) side, without evaluating D̄) and **Route E** (prove the \(A \to \infty\) edge-energy limit promoting the edge profile \(i(e^{-\xi} - \delta_0)\) to the energy space). Verdicts: Route T **reaches** the pairings; Route E **does not go through as stated**, blocked structurally. The entry closes with the three gaps G1–G3 now chartered as the next work on the T side.

## 1. Route T — the pairings, with zero D̄ evaluation [D/I]

**Key ledger find [D]:** v13.785 ("Lane A T-side Parity/Weyl Replacement and Dual Edge-Laplace Reduction") is the ledger's *own* prior execution of this route — it builds the finite Weyl function and the \(r_{0,a}, r_{1,a}\) feedback entirely from \(T_a^{-1}\) responses (\(E_a, O_a\) Fourier transforms; dual-resolvent edge-Laplace formulas), superseding v13.777's D̄-evaluation. The present work connects v13.757's \(G_A/H_A\) pairings to that T-side machinery.

Setup [D]: \(S_A^{-1} = \bar{D}T_A^{-1}\bar{D}^{-1}\) (energy-space, v13.784 §5); D̄ iso \(\mathcal{H}(T_A) \to \mathcal{H}(S_A)\); \(\bar{D}R = -R\bar{D}\) (v13.784 §7); \(u_{A,z} = S_A^{-1}\bar{D}e_z\), \(u_{A,+} = C_A\bar{D}w_A\), \(u_{A,-} = -Ru_{A,+}\) (v13.757).

- **T1 [D]** — v13.740 §2's \(F\) (retracted object; its \(S_Au_\pm = \bar{D}e_{\pm i}\) lacks the W3 boundary functional): \(F_{A,\pm}(z) = \overline{\langle\bar{D}e_{\bar z}, S_A^{-1}\bar{D}e_{\pm i}\rangle} = \overline{\langle\!\langle e_{\bar z}, T_A^{-1}e_{\pm i}\rangle\!\rangle_{T_A}}\). Caveat [I]: \(e_{\pm i}\) are \(\mathcal{H}(T_A)\)-completion elements (approximant limits), *not* \(L^2\) functions — this does not collapse to an elementary integral; the \(\propto e^{\pm x}\) shortcut stays retracted.
- **T2 [D]** — v13.757's true pairings: \(G_A(z) = \bar C_A\cdot\overline{\langle\!\langle e_{\bar z}, w_A\rangle\!\rangle_{T_A}}\), \(H_A(z) = \bar C_A\cdot\overline{\langle\!\langle e_{-\bar z}, w_A\rangle\!\rangle_{T_A}}\), with \(w_A = u_{e,A} - r_{0,A}u_{1,A} - r_{1,A}u_{x,A}\). Derivation uses \(S_A^{-1}\) as Riesz map [D], the D̄-isometry [D], and \(\bar{D}R = -R\bar{D}\) with a double sign cancellation [D].
- **T3 [D]** — \(\rho_A(z) = H_A/G_A = \overline{\langle\!\langle e_{-\bar z}, w_A\rangle\!\rangle_{T_A}}/\overline{\langle\!\langle e_{\bar z}, w_A\rangle\!\rangle_{T_A}}\). \(C_A\) cancels [D]; the \(C_\pm\) convention is irrelevant for \(\rho_A, m_A\).
- **T4 [D]** — parity sectors \(S_A^{(\pm)}u_{e/o} = \bar{D}(\cosh/\sinh)\) (v13.776 §3) ⟺ \(\bar{D}^{-1}u_{e/o} = (T_A^{(\pm)})^{-1}(\cosh/\sinh)\) = v13.785's (1E)(1O), via intertwining + D̄ injectivity; no D̄ evaluation. (The v13.776 \(\propto e^{\pm x}\) *evaluation* is retracted; the parity-sector *intertwining* survives.)
- **T5 [D]** — \(r\)-feedback D̄-free (v13.785 §§5–6): \(r_{j,A} = \langle\psi_{j,A}, \cosh/\sinh\rangle\), \(\psi_{j,A} = T_A^{-1}q_{j,A}\); \(e^{-A}r_{j,A} = \int_0^{2A}e^{-\xi}\psi_{j,A}(A-\xi)\,d\xi\).

**Minor correction [I]:** the W3 report's derivation cites "\([R,\bar{D}] = 0\)"; the correct relation is \(\bar{D}R = -R\bar{D}\) (v13.784 §7). The W3 parity-lemma *conclusion* (\(M_0\) odd, \(M_1\) even; \(H_A(z) = P(-\bar z)\)) is unaffected.

**Verdict [I]:** Route T **reaches** the \(G_A/H_A\) pairings — T1–T5 are exact \(T_A\)-side identities with zero D̄ evaluation. It **does not close** the identification leg. The obstruction, in Route-T form (same content as W3's \(\delta_\infty\) equation, now in \(T_A\)-pairing language): \(\rho_A^{T}(z) \to \rho_\infty^{T}(z) \stackrel{?}{=} \rho_\infty(z) = \frac{z-i}{z+i}\cdot\frac{(a/b)D_\xi/\Xi - 1}{(a/b)D_\xi/\Xi + 1}\), i.e. \([Q_\infty^0 + 2z\delta_\infty^{T} + b\text{-terms}}]/[P_\infty^0 - 2i\delta_\infty^{T} + b\text{-terms}] \stackrel{?}{=} (a/b)D_\xi/\Xi\) with \(\delta_\infty^{T} := 0.48\cdot\lim_{A\to\infty} e^A\cdot\overline{\langle\!\langle e_{\bar z}, u_{x,A}\rangle\!\rangle_{T_A}}/c_A\). Route T + Route E together close only the *convergence* leg (to the distorted limit); *identification* still needs the infinite-volume comparison.

## 2. Route E — blocked, structurally [D/I/O]

**Verdict [O]:** Route E does **not** go through as stated. The ledger gives the exact core-level edge isometry and the distributional profile, but promotion to an energy-space limit is blocked at all three of v13.725 §6's ingredients — with (iii) blocked **structurally**, not technically.

Precise statement attempted: for fixed \(A\), \(\bar{D}e_{+i} := \mathcal{H}(S_A)\text{-}\lim_n Dv_{\varepsilon_n,A}\); edge rescaling \((E_Af)(\xi) = f(A-\xi)\); normalized profile \(F_A := e^{-A}E_A(\bar{D}e_{+i})\); edge form \(s_{\rm edge}(\xi,\eta) = g(\xi-\eta) - \lambda\min(\xi,\eta)\) (\(K_{\rm edge}\) exact and \(A\)-independent, v13.724 §5). Desired: \(\lim_{A\to\infty} F_A = i(e^{-\xi} - \delta_0)\) in the edge energy topology.

What goes through **[D]**:
- **D1 (new, derived from ledger [D] facts):** exact core edge isometry — for \(f\) in the \(S_A\) core, \(\|e^{-A}E_A f\|_{\text{edge-form on }(0,2A)} = \|f\|_{S_A}\) *exactly* (from \(g\) even, v13.724 §4; \(A - \max(x,y) = \min(\xi,\eta)\) under \(x = A - \xi\), v13.724 §3; \(P_A\) trivial on zero-mean inputs). Extends to an isometry \(\mathcal{H}(S_A) \to \mathcal{H}_{\rm edge}^{(A)} \hookrightarrow \mathcal{H}(S_{\rm edge})\). So \(F_A\) is well-defined in \(\mathcal{H}(S_{\rm edge})\) for every \(A\).
- **D2:** the distributional iterated limit for approximants \(= i(e^{-\xi} - \delta_0)\) (v13.725 §§3–5), \(\delta_0\)-coefficient cutoff-independent.
- **D3:** left-edge contamination \(R_{A,\varepsilon}\) exponentially suppressed (\(\sim e^{-2A}\) after normalization).

Per-ingredient verdicts **[O]**:
- **(i) Limit existence — blocked.** (a) \(\mathcal{H}(S_{\rm edge})\) is not constructed: \(s_{\rm edge}\)'s positive-definiteness on the half-line is unproved (v13.724 §5 flags exactly this; \(S_A\)'s positivity comes via transport \(S_A = \bar{D}T_A\bar{D}^{-1}\), which doesn't obviously localize). (b) Boundedness of \(\{F_A\}\) needs \(\sup_A e^{-A}\|e^x\|_{T_A} < \infty\) — [I], plausible, not surveyed. (c) Strong convergence to \(i(e^{-\xi} - \delta_0)\) is impossible as stated: the putative limit isn't in \(\mathcal{H}(S_{\rm edge})\); at most weak subsequential convergence. (d) The double-limit interchange (\(\varepsilon_n \to 0\) defining \(\bar{D}e_{+i}\), then \(A \to \infty\)) needs \(e^{-A}\|v_{\varepsilon,A} - e^x\|_{T_A} \to 0\) uniformly in \(A\) — no such estimate exists.
- **(ii) Testing continuity — blocked.** \(L^2\)/distributional testing converges for approximants [D], but \(\mathcal{H}(S_A) \not\subset L^2\) severs \(L^2\)-testing from \(\mathcal{H}(S_A)\)-convergence. In the (continuous) energy pairing, the formal limit yields \(i\cdot s_{\rm edge}(e^{-\xi},\varphi) - i\cdot\mathbf{(S_{\rm edge}\varphi)(0)}\) — the *energy-dual* boundary functional, **not** the distributional \(\varphi(0)\). **Precise obstruction: the distributional \(\delta_0\) and the energy-dual boundary functional are different objects; nothing identifies them.**
- **(iii) \(\delta_0\) in the dual — blocked, structurally.** The edge form is negative order: \(K_{\rm edge} \sim (-\partial^2)^{-1}\), \(G_{\rm edge}\) has multiplier \(\sim 1/\omega^2\) (sandbox numerics: \(g(t) \sim c_1|t|\), \(c_1 \approx -0.154\); Fourier of \(|t|\) is \(-2/\omega^2\)). So \(\mathcal{H}(S_{\rm edge})\) has a weak norm, its dual is small, and point evaluation \(\varphi \mapsto \varphi(0)\) needs \(H^1\) the energy norm cannot give. Hence \(\delta_0 \notin \mathcal{H}(S_{\rm edge})^*\) — structural, not a gap harder estimates can fill. The IBP rescue (\(\langle e^{-\xi} - \delta_0, \varphi\rangle = \int e^{-\xi}\varphi'\)) needs the same missing \(H^1\) control.

**Reframing [I]:** the \(\delta_0\) is boundary data at \(\xi = 0\), not a bulk source — \(S_{\rm edge}q = i(e^{-\xi} - \delta_0)\) should be read as \(S_{\rm edge}q = ie^{-\xi}\) + boundary condition; needs a trace theorem [O]. **Reconcile with W1/W3:** the remnant-inclusive source \(\psi_A(\xi) = e^{-\xi} - 0.47\cdot\mathbf{1}_{\xi>0}\) is \(\delta_0\)-free — the \(\delta_0\) belongs to the *pure* exponential's edge jump only. Route E's target is superseded for the actual \(G_A/H_A\) pairings; the 0.47 half-line constant, not the \(\delta_0\), is what must survive the edge limit.

**Net [I]:** Route T remains the viable path to the pairings. Route E's honest yield is the exact core edge isometry D1 and a precise map of why the energy promotion fails — any future edge theory must go boundary-data or stay distributional.

## 3. Gaps G1–G3, chartered on the T side (2026-09-29)

- **G1 (analytic):** \(R_A := L_A^{-1}\) (v13.745) vs \(T_A^{-1}\) — no ledger identity; v13.785 supersedes rather than equates. Blocks replacing \(\langle\!\langle e_{\bar z}, u_{\cdot,A}\rangle\!\rangle\) with v13.785's \(E_a/O_a\). Needs: prove \(L_A^{-1}\)-response pairings coincide with \(T_A^{-1}\)-response pairings.
- **G2 (technical):** the "appropriate duality" pairing \(\langle\!\langle\cdot,\cdot\rangle\!\rangle\) is invoked, never constructed in one place. Needs: explicit approximant-limit construction.
- **G3 (bookkeeping):** the \(C_\pm\) convention — cancels in ratios \(\rho_A, m_A\); needed for absolute \(G_A/H_A\).

All conclusions remain conditional on \(\lambda_a > 0\).
