# Cone Derivation Ledger v13.864 — Sandbox Bucket 2: IDENT — the Identification Leg Dissolves

Date: 2026-09-29

Lane: B (sandbox exploratory track, chartered by the project owner). **Lane disambiguation:** this is NOT the ledger's Lane B (the norm-quotient/idele-class representation track, dormant since v13.736 per v13.760). The sandbox track consumes Lane A's certified results and reports exploratory diagnostics back; nothing here is certified and nothing here alters a certified result.

Status: **[I]/[O]** sandbox analytic report with **[D]** ledger- and Suzuki-text-derived facts. No new numerics in this entry.

Author: the project owner's sandbox track (autonomous thread under the owner's assistant), by request of the project owner. Full analysis (for-review, not part of this repo): `~/workspace/d12/lane_b/sandbox/runs/20260929-ident-analysis/IDENT_Analysis_ForReview.md`.

Parents: v13.863 (External Audit Round 121), v13.862 (PAIR-H), v13.861 (H1), v13.858 (G1–G3), v13.856 (D̄), v13.854 (W3), v13.848 (selection), v13.789 (Vitali framework), v13.757, v13.670, Suzuki arXiv v2 §§1, 3.2, 6.3–6.4, 7.8, Cor. 1.6.

Synchronization: live ledger head checked immediately before this write is v13.863 (External Audit Round 121). No collision on the present version number. **This entry does not audit v13.863 or earlier.**

## 0. What this entry does

Investigates IDENT, the identification leg — whether the surviving α-even distortion identifies with Suzuki's infinite-volume target, formulated as the \(\delta_\infty\) discrepancy equation. **Verdict: [I] — the identification leg dissolves as an independent leg.** The \(\delta_\infty\) equation reduces to (CONV) ∧ (SUZ-LIM) and has no independent content. Finite-\(A\) identification is closed [D/I]; Suzuki's (1.12) limit is conjectural in his own text and RH-hard by his Corollary 1.6 — beyond Bucket 2's scope. W3 §6's "If NO" branch should be retired from the ledger's framing.

## 1. The \(\delta_\infty\) discrepancy equation, exactly

**Finite-\(A\) objects** (all rigorous at fixed \(A\) after v13.856–v13.861): \(G_A, H_A\) via Route T T1–T5 + H1 dual-slot canonization; \(P_A(z) = (z-i)G_A(z) - (z+i)H_A(z)\); \(Q_A(z) = (z-i)G_A(z) + (z+i)H_A(z)\); \(m_A(z) = -iQ_A(z)/P_A(z)\); \(c_A\) the \(z\)-independent normalization (v13.757 §5).

**W3's limit form** (v13.854): with \(M_1(w) = \overline{\langle\bar De_w, \bar Du_{x,A}\rangle}\) (even), the α-even remnant \(a(w) = \alpha_Ae^AM_1(w)\) survives as \(\delta_\infty(z) = 0.48\cdot\lim_{A\to\infty}[e^AM_1(\bar z)/c_A]\) — explicit, \(z\)-dependent, non-zero [I]; β cancels (R2); α-odd is R2-edge-tamed + PAIR-H bulk.

**The equation** (W3 §6):

\[
\frac{Q_\infty^0(z) + 2z\delta_\infty(z) + b_Q(z)}{P_\infty^0(z) - 2i\delta_\infty(z) + b_P(z)} \overset{?}{=} \frac{a}{b}\frac{D_\xi(z)}{\Xi(z)},
\]

\(a = \xi(3/2),\; b = \xi'(3/2),\; \Xi(z) = \xi(1/2-iz),\; D_\xi(z) = \xi'(1/2-iz)\). "Identification" means \(Q_A/P_A \to (a/b)D_\xi/\Xi\) locally uniformly on zero-free compacta (v13.757 (8)).

## 2. Suzuki's infinite-volume target, in three layers (verified against his text directly)

- **[D] Finite-\(a\) (proved):** deficiency (1,1), \(v_\pm(a,\cdot)\) with \(D_a^*v_\pm = \pm iv_\pm\) (§6.4), \(W(a,\theta;z)\) entire with real zeros (Theorem 1.5). §6.3: Riesz representer \(v_z = T_a^{-1}e_z \in \mathfrak{D}(T_a)\), \(\langle v, v_z\rangle_{T_a} = \hat v(\bar z)\). §3.2: Friedrichs extension of \(B_a\) equals \(A_a\).
- **[D|RH] Infinite-volume exact (conditional):** in \(\mathcal{B} = \mathcal{H}(A_\infty)\) (identification via [14, Thm 1.1] — **requires RH**), the boundary-form computation gives \(B_0/B_\pi = (a/b)(D/\Xi)\) (Suzuki §7.8), hence \(m_\infty = -i(a/b)D/\Xi\) (v13.670 algebra).
- **[O] The limit (1.12) (conjectural in Suzuki):** \(\lim_{a\to\infty}e^{\phi}W = \Xi/(\Xi+D)\) — "expected", "heuristics", "we do not pursue". **Corollary 1.6 (textual fact): (1.12) ⟹ RH.**

**Finite-\(A\) identification closed [D/I]:** \(G_A(z) = \int_{-A}^{A}v_{+i}(x)e^{izx}\,dx\) (H1 α-reading); \(v_{+i} = T_A^{-1}e_{+i}\) satisfies \(D_A^*v_{+i} = +iv_{+i}\) (Suzuki §6.3) — i.e. it **is** Suzuki's deficiency vector up to the G3 normalization; with reflection, Suzuki's \(W(a,\pi;z) \propto P_A(z)\) and \(Q_A/P_A\) kills \(C_+\). v13.848: Galerkin → Suzuki's true deficiency vector **[D|\(\lambda_a > 0\)]**. There is no "our vs Suzuki's construction" gap at finite \(A\).

## 3. Verdict: [I] — the \(\delta_\infty\) equation reduces to (CONV) ∧ (SUZ-LIM)

- **(a)** Finite-\(A\) identification is closed (above).
- **(b)** The 0.48 is Suzuki-true, not our artifact: \(\alpha_A \to 0.48\) is a property of the **true** deficiency vectors (v13.848; W1's \(-0.47\) half-line constant in the true \(S_Au_{A,\pm} = \bar De_{\pm i} + B_{A,\pm}\)). Any correct \(A \to \infty\) limit of Suzuki's finite-\(a\) Weyl data automatically "incorporates" it — \(\delta_\infty\) is part of the limit's explicit form, not a deviation from it.
- **(c)** The closed form \((a/b)D/\Xi\) is exact in \(\mathcal{B}\)|RH (Suzuki §7.8 + v13.670). It cannot "fail to incorporate" a boundary term. A failed identification would be a failed limit interchange, not a \(\delta_\infty\) discrepancy.
- **(d)** W3 §6's "If NO" branch (explicit \(\delta_\infty\) discrepancy needing boundary correction) is **incoherent as stated**: one cannot "correct" an exact de Branges identity by adding a boundary functional, and the "pure" objects \(Q_\infty^0/P_\infty^0\) aren't Suzuki's objects (the pure source is our analytic fiction; his true vectors include the affine feedback) — a category error already foreclosed by W3's SURVIVE verdict. **This branch should be retired from the ledger's framing.**
- **(e)** (SUZ-LIM) is RH-hard: (1.12)⟹RH is Suzuki's own Corollary 1.6. It cannot be closed within Bucket 2's finite-\(A\) scope.

**Exact location of non-closure:** not at the \(\delta_\infty\) equation itself — it is well-formed but not independently decidable (\(Q_\infty^0, P_\infty^0, \delta_\infty\) aren't independently accessible). The chain is: (1) our = Suzuki's finite-\(a\) [closed] → (2) limit exists with \(\delta_\infty\) explicit [O = CONV] → (3) limit = \((a/b)D/\Xi\) [O = SUZ-LIM]. The \(\delta_\infty\) equation is (2)+(3) written out: it closes automatically when they hold (becoming a constraint on the pure/distortion split) and cannot fail while they hold.

**Topology check [D]:** v13.757 (9)'s framework (\(c_A^{-1}P_A \to P_\infty\), \(c_A^{-1}Q_A \to Q_\infty\) locally uniform, entire; ratio locally uniform on zero-free compacta) matches the target's meromorphic topology. The framework is sound; only the two prior opens block.

## 4. What IDENT needs next

1. **(CONV)** — the convergence leg (PAIR-H/R1/R2/COMB-H + the merged 0.48-value problem): for the limit, hence \(\delta_\infty\), to exist at all.
2. **(SUZ-LIM)** — Suzuki's (1.12): beyond Bucket 2's scope; RH-hard by his Corollary 1.6; its heuristic proof assumes RH.
3. Optional numerical joint test [N]: \(s_a(iy) \to s_\infty(iy)\) pointwise on an interval ⟹ full local-uniform Weyl limit by Vitali (v13.789 (17)) — a 1D test of (CONV)+(SUZ-LIM) jointly.
4. Explicitly **not**: \(\delta_\infty\)-correcting the target; pure-vs-distorted as a fork. No RH/positivity/Hilbert–Pólya claim made.

## 5. Frontier update

| Item | Status |
|---|---|
| T side at fixed \(A\) (D̄, Route T, G1–G3, H1) | **Closed [D/I]** through v13.861 |
| PAIR-H bulk control | **[O]** — merged with the 0.48-value problem (v13.862) |
| 0.48 analytic value | **[O]** — the live analytic question |
| Identification leg | **Dissolved** — reduces to (CONV) ∧ (SUZ-LIM); "If NO" branch retired |
| (SUZ-LIM) | **[O]** — RH-hard, outside Bucket 2 |
| Standing hypothesis | \(\lambda_a > 0\) (cf. v13.860) |
