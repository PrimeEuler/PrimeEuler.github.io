# Cone Derivation Ledger v13.861 — Sandbox Bucket 2: H1 Closed via Dual-Slot Canonization

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[I]/[O]** sandbox analytic report with **[D]** ledger- and Suzuki-text-derived facts. No new numerics in this entry.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request of the project owner. Full report (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/h1_general_z_membership_vs_dualslot.md`.

Parents: v13.858 (G1–G3 closure; left H1 open), v13.857, v13.856, v13.784, v13.757, v13.740, v13.725, v13.667, Suzuki arXiv v2 §6.3.

Synchronization: live ledger head checked immediately before this write is v13.860 (External Audit Round 120 at v13.859; strategic note on \(\lambda_a > 0\) at v13.860). No collision on the present version number. **This entry does not audit v13.859, v13.860, or earlier.**

## 0. What this entry does

Closes H1, the last open hazard from G2 (v13.858 §2): whether \(e_z \in \mathcal{H}(T_A)\) for general regular \(z\), needed for the first slot of the duality pairing \(\langle\!\langle e_{\bar z}, w_A\rangle\!\rangle_{T_A}\). **Verdict: prong (a) (direct membership) bypassed as unnecessary [O]; prong (b) (dual-slot canonization) closed [D/I].** The entry also records two hygiene flags: v13.725's "\(e^x \in \mathcal{H}(T_A)\)" premise is itself [O], and v13.740 §2's pairing notation needs an annotation.

## 1. Prong (a) — direct \(e_z \in \mathcal{H}(T_A)\): bypassed as unnecessary [O]

Verified directly against Suzuki's text: §6.3 proves \(v_z = T_a^{-1}e_z \in \mathfrak{D}(T_a)\) and \(D_a^*v_z = zv_z\) **[D]** — but this places \(e_z\) in \(\mathrm{Ran}(T_a) = L^2\), **not** in \(\mathcal{H}(T_A)\). The exact missing estimate is named: \(\|\cdot\|_{T_a}\)-Cauchyness of cutoff approximants to \(e_z\), i.e. a \(G_a\)-weighted boundary-layer bound showing the \(T_a\)-energy doesn't blow up on the \(O(\varepsilon^{-1/2})\) cutoff derivatives. No such \(G_a\) estimate exists in Suzuki or the ledger. Prong (a) remains a standalone analytic gap if anyone ever wants it — it is **not needed** for the T-side program.

**Hygiene flag [O]:** v13.725 line 69's "\(e^x \in \mathcal{H}(T_A)\) as a Suzuki deficiency/source vector" is itself [O] — Suzuki only gives \(T_av_\pm = C_\pm e^{\pm x}\) (range, not form domain), so v13.725's \(\bar De_{+i}\) (defined as the \(\mathcal{H}(S_A)\)-limit of core approximants to \(e^x\)) inherits that hazard. **Recommendation:** rebase the approximant construction on \(u_{A,+i} = \bar DT_A^{-1}e_{+i} \in \mathcal{H}(S_A)\) **[D]**, which needs only \(e^{+x} \in L^2\) [D].

## 2. Prong (b) — dual-slot canonization: closed [D/I]

The rule, fixed once for all \(z \in \mathbb{C}\) and \(\Psi \in \mathcal{H}(S_A)\):

\[
\boxed{\langle\bar De_{\bar z}, \Psi\rangle := \langle u_{A,\bar z}, \Psi\rangle_{S_A} = \langle e_{\bar z}, \bar D^{-1}\Psi\rangle_{L^2}}, \qquad u_{A,z} := \bar DT_A^{-1}e_z.
\]

Every step is [D] (D̄-isometry, \(S_A^{-1} = \bar DT_A^{-1}\bar D^{-1}\) energy-space, \(e^{zx} \in L^2\) for all \(z\)); the identification itself is definitional [I], forced by three [D] facts.

**Deciding finding [D/I]:** the ledger's \(F_{A,\pm}\) admits two rigorous readings —
- **(β)** the literal energy reading, giving \(\overline{\langle e_{\bar z}, e_{\pm i}\rangle_{L^2}}\) — which is **\(T_A\)-independent** (the single \(T_A^{-1}\) is undone by the energy inner product) and therefore **structurally wrong** for Weyl data;
- **(α)** the \(u_{A,\bar z}\) reading, giving \(\overline{\langle e_{\bar z}, v_{\pm i}\rangle_{L^2}}\) — \(T_A\)-dependent, entire in \(z\), matching Suzuki's \(\langle v_z, v_\pm\rangle\).

The ledger's own v13.757 already uses \(u_{A,\bar z}\) as primary ((17), §2), so **(α) is the consistent canonization**; v13.740 §2's notation should be annotated as formal shorthand for it.

**Hygiene flag [I]:** v13.740 §2 deserves an annotation making the \(u_{A,\bar z}\) reading explicit — it is now specified as "the appropriate form/duality interpretation" that entry invoked.

## 3. General \(z\) genuinely required [D]

\(m_A, P_A, Q_A, \rho_A\) are functions on \(\mathbb{C}_+\); the canonized pairings are entire Fourier-\(L^2\) integrals delivering exactly that. This is not a technicality: the (β) reading would have made the Weyl data \(T_A\)-independent, i.e. wrong.

## 4. T-side final scorecard

| Item | Verdict |
|---|---|
| D̄ definition/action (v13.856) | **[D]** isometric transport; no closed-form evaluation |
| Route T pairings (v13.857) | **[D]** T1–T5, zero D̄ evaluation |
| G1 (v13.858) | **[D]** ratio/shape identities; operator identity obstructed, not needed |
| G2 pairing construction (v13.858) | **[I]** closed at fixed \(A\) |
| G3 \(C_\pm\) (v13.858) | **[D]** canonical explicit form |
| H1 general-\(z\) (this entry) | **[D/I]** dual-slot canonization; direct membership bypassed [O] |
| Route E edge-energy limit (v13.857) | **[O]** blocked structurally (\(\delta_0 \notin \mathcal{H}(S_{\rm edge})^*\)) |

The T side is now fully rigorous at fixed \(A\) with zero D̄ evaluation and zero hand-waving about membership. What remains: the **convergence leg** (PAIR-H, R1/R2 — v13.853's four-hypothesis reformulation) and the **identification leg** (the \(\delta_\infty\) discrepancy equation — needs the infinite-volume comparison against Suzuki's construction). All conclusions remain conditional on \(\lambda_a > 0\).
