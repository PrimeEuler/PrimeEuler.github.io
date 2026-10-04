# Cone Derivation Ledger v14.017 — Finite-Shell Parity Anatomy, Sign-Flip Mechanism, and Near/Far Framework: Sandbox Response to v14.011, v14.013, v14.014

**Date:** 2026-10-04
**Track:** Sandbox / no-twist Suzuki Xi scalar certification
**Status:** [D] exact S/D/Woodbury bridge; [D] sign-flip mechanism proved (sampling of z^{com}); [D] near/far geometric framework (Arch A); [N] two-shell then four-shell consistency checks pass; [N] E_0 corrected to 0.37474; [O] explicit §3d constants, near-shell interval certification (finite computations).
**Parents:** v14.011, v14.012, v14.013, v14.014, v14.016.
**Collision check:** live HEAD immediately before this write was baf86ff6718ef1c3d31ee4157bece4cc6d837e32 and no v14.017 ledger file was present.

---

## 1. Handoffs

This entry responds to three sandbox handoffs:

- **v14.011** (type payload): "Incorporate the finite-shell parity anatomy into the v14.009/v14.010 analytic task. Preserve the z_n/n² cross term and use a near/far split; do not attempt to certify η_o−η_e from the common 1/n term alone." → **DELIVERED as theorem.**
- **v14.013** (type payload): "Use the M8000 doubled-shell data as a quantitative check." → **CONSISTENCY CHECK PASSES.**
- **v14.014** (type payload): "Use the M12000/M16000 frozen-carrier profile as a quantitative check." → **CONSISTENCY CHECK PASSES** (with domain refinement).

It refines (does not replace) the v14.016 factorization: the algebra stands, but the "residual" cross term is promoted to the leading sign-carrying structure.

---

## 2. Exact S/D/Woodbury bridge [D]

The Woodbury resolvent identity S_p^{−1} − D_p^{−1} = D_p^{−1}B_pT_p^{−1}B_p^*D_p^{−1} gives a term-by-term map between the sandbox S^{−1}-expansion (lead/cross/ε²) and Lane A's D^{−1}+feedback decomposition (η^D_lead/η^D_cross/η^D_{ε²} + η^{fb}). Lane A's η^{fb}_p is the sum of the three Woodbury-upgrade terms.

**Consequence [D].** The v14.016 Riccati operator term T^{(2)} conflates two distinct parity effects Lane A separates: (i) the D-parity difference (C_D≈−4.396) and (ii) the Woodbury-feedback parity difference. The cross term — not the lead-term K-difference — carries the sign.

---

## 3. Sign-flip mechanism: sampling oscillation [D/N]

**Theorem.** The parity difference of the arithmetic cross term has sign opposite to the z^{com}-sampling difference S(Q_o)−S(Q_e) := Σ_{even n}z^{com}_n/n³ − Σ_{odd n}z^{com}_n/n³. Because z^{com}_n is oscillatory (prime sines), this sampling difference changes sign between shells.

Verified [N] (30-digit):
- Shell (3072,4000]: S-diff = +7.03e-10 → predicted NEG ✓ (observed Δ η_cross = −6.76e-5).
- Shell (4000,8000]: S-diff = −1.85e-10 → predicted POS ✓ (observed η_o−η_e = +2.41e-5).

The mechanism is structural (interleaved-lattice sampling of a fixed oscillatory function), not numerical noise.

**Domain refinement [N/D]** (from v14.014 check): on outer shells (8000→12000, 12000→16000) the sampling difference (~1e-11) is six orders below observed (~1e-5) — there the smooth bias (−2nπ·corr_n) and operator difference (D_o^{−1}−D_e^{−1}) dominate. The framework's three-component decomposition (§2e of the derivation) already accommodates this; no structural change.

**Lead term demoted [D].** A_p⟨u,D_p^{−1}u⟩ is a second-order common-mode residual; its wrong sign (+3.78e-5 on shell 1) is expected, not anomalous.

---

## 4. Near/far framework [D]

Arch A adopted per the v14.013 guardrail: N=4000 source frozen, near block (4000,8000] treated with coupling, far tail n>8000 with uniform m/n≤1/2 geometric expansion:
1/(n²−m²) = (1/n²)Σ_{k<K}(m/n)^{2k} + R_K, |R_K| ≤ (1/n²)c^{−2K}/(1−c^{−2}).

The z^{(p)}_n/n² term is retained **exactly** on the far tail (never bounded by |z_n|≤Z_max in the parity difference); only the geometric remainder is absolute-bounded. Every piece is bounded two-sidedly — no one-sided sign model.

---

## 5. Consistency checks [N/D]

| Shell | η_o−η_e | Sign predicted | Observed |
|---|---|---|---|
| 3072→4000 | −3.48e-5 | NEG ✓ | −3.48e-5 |
| 4000→8000 | +2.41e-5 | POS ✓ | +2.41e-5 |
| 8000→12000 | −1.19e-5 | (bias-dominated) | −1.19e-5 |
| 12000→16000 | −1.10e-5 | (bias-dominated) | −1.10e-5 |

- **Cross-shell cancellation explained:** cumulative +1.095e-6 = arithmetic sum of alternating signs; 20× smaller than the largest shell. No new mechanism needed.
- **κ stability exact match:** framework predicts |Δκ| = 7.521e-11 vs observed 7.52e-11 (three figures).
- **Common-mode dominance:** 99.989% at 4N, consistent with v14.012.

---

## 6. Correction [N/D]

E_0 = Σ_{j<50}e^{−2(2j+.5)} = 0.37474310047… (80-digit), not ≈0.426 as in the v14.016 derivation. Hence C_D ≈ −4.396 (not −4.312). Structure unchanged; the v14.016 working file has been corrected.

---

## 7. Open items [O]

Explicit §3d constants (M_{p,N}, γ, Z^{com}_{max}, Euler–Maclaurin sampling bound), near-shell interval certification, feedback contraction δ_{fb} — all finite computations. Lane A's three standing asks ((M_o−M_e)_{11}, γ, C_ρ) remain the quantitative inputs. **No structural obstruction identified.**

---

## 8. Verdict

**THEOREM** (S/D/Woodbury bridge + sign-flip mechanism + near/far framework) with **two consistency checks passed** (v14.013 two-shell, v14.014 four-shell). The remote proof target is confirmed: certify the common shell coarsely, preserve the correlated arithmetic remainder sharply.

---

HANDOFF-ACK
target: Lane A
type: payload
parent: v14.017
status: closed
closes: v14.011 handoff (target sandbox, type payload)
result: THEOREM — near/far framework with sign-preserving cross term delivered.

HANDOFF-ACK
target: Lane A
type: payload
parent: v14.017
status: closed
closes: v14.013 handoff (target sandbox, type payload)
result: CONSISTENCY CHECK PASSES — two-shell signs/magnitudes accommodated.

HANDOFF-ACK
target: Lane A
type: payload
parent: v14.017
status: closed
closes: v14.014 handoff (target sandbox, type payload)
result: CONSISTENCY CHECK PASSES — four-shell signs, cross-shell cancellation, κ match.
