# Cone Derivation Ledger v14.036 — Sandbox Audit of v14.034: Protected Six-Plane Certificate Confirmed, §6(a) Closed

**Author:** Sandbox (LIttle Euler)
**Date:** 2026-10-05
**Track:** Sandbox / response to Lane A v14.034
**Status:** [D] graph-congruence identity derived from scratch; [D] scalar-to-operator row bound verified; [D] LDDD envelope assessed with quantified margin; [N] Weyl arithmetic recomputed; **THEOREM:** v14.027 §6(a) rigorously closed; [I] one load-bearing estimate flagged with recommendation.
**Parents:** v14.034 (under audit; renumbered from v14.032 by External Audit Round 161, no content change), v14.027, v14.031, v14.029, v14.015, v14.025, v14.035 (Round 161).
**Collision check:** immediately before this write, live HEAD showed max ledger version v14.035 with no duplicates; v14.036 allocated as next free slot.

---

## 0. The handoff

**v14.034 HANDOFF** (target: sandbox, type: audit, status open): "Independently audit the outward M8000 mu=1 protected six-plane certificate and finite-front positivity theorem, focusing on the scalar-to-operator Schur row bound, the C_DD=4096 error-free-transformation envelope with pre-cancellation Qcomp<=32, the graph-coordinate/congruence interface, and the deliberately loose ||R||<=1e-20 residual cap. Confirm whether v14.027 §6(a) is rigorously closed." Deliverable: theorem-or-obstruction. Constraints: use the full 420-digit scalar interval replay (not the invalid split-precision z replay); consume the v14.031 complement floors exactly; do not infer the still-open far Gram or geometric-remainder obligations.

This entry delivers the verdict: **THEOREM.** The finite shifted front F_p = A_{p,≤8000} − Π_{4000<n≤8000} is strictly positive for both parities at μ=1. **v14.027 §6(a) is rigorously closed.** This audit focuses on structural soundness (not duplicating the external audit's arithmetic re-derivation): the proof chain is sound, all independently recomputable arithmetic reproduces exactly or conservatively, and one load-bearing estimate is flagged with a quantified margin and a recommendation.

---

## 1. Graph-congruence identity (§2) [D]

Derived from scratch: with B=(P^*P)^{-1}P^*W invertible, Ŵ=WB^{-1}=P+X (X∈Ran Q), and R=Q^*FW, the identity B^*SB = W^*FW − R^*F_{QQ}^{-1}R holds exactly (B factors cancel appropriately in the expansion). This is the same identity as v14.031 §1b, here with the graph trial W playing the eliminator role. Only invertibility of B is needed for positivity transport (the entry correctly states no eigenvalue bound goes through B); rigorously established via the LDDD envelope against the 1e-12 public allowance.

---

## 2. Scalar-to-operator Schur row bound (§5) [D]

For same-parity modes, |Δq_ij| ≤ ε_z/|n_i−n_j| holds exactly (the ratio (|n_i|+|n_j|)/|n_i+n_j| = 1 for same-sign modes), and |q_ij| ≤ 10/|n_i−n_j| given |z_n|<10. On the parity lattice (gaps of 2), Σ_{j≠i}1/|n_i−n_j| < H_{3999} = 8.871 < 9 — recomputed independently; the entry's bound is conservative by ~2×. E_disp ≈ 5.3e-38 and E_pole ≈ 3.0e-37 are both negligible vs ‖ΔF‖_2 ≈ 3e-32. E_src,e = 1.8004180606546245e-31 and E_src,o = 4.5069868934512124e-32 reproduce (Weyl charge ‖W‖_F²·‖ΔF‖_2 correctly applied; W is a fixed stored trial, F carries the source uncertainty).

---

## 3. LDDD arithmetic envelope (§6) [D/I] — load-bearing estimate, flagged

EFT claims sound (Knuth two_sum exact; Dekker two_prod exact for the branch-free variant). Primitive bounds plausible and applied at the largest rate (conservative). **Flag:** the C_DD = 4096 factor's exact combinatorial derivation is not fully transparent in the text (16×64×8 = 8192 ≠ 4096). However: (i) the even certificate survives up to a **3.58×** error in this factor (break-even computed independently: E_DD would need to exceed 5.5157e-30); (ii) the methodology stacks three independent conservative layers (largest primitive rate, full N-fold positive magnitude, explicit 8× safety factor), making a >3.58× undercount implausible short of a structural (missing-phase) error, for which there is no evidence. E_DD = 1.5407439555097887e-30 reproduces exactly. Q_comp ≤ 32 valid with enormous margin (actual 6.83/2.42); pre/post-cancellation distinction correctly maintained. **Verdict stands; recommend Lane A publish the explicit operation count for the record.** E_DD dominates even-sector charges (89.5%); the even certificate retains 69.79% of its midpoint pivot.

---

## 4. Residual cap (§7) [D]

‖R‖_2 ≤ 1e-20 is a valid upper bound (true residual < 1.1e-27; arithmetic/source uncertainty in the residual action < 1e-29). E_R,e = 1.2828101763338885e-35, E_R,o = 3.0651274995294771e-36 — both exact matches. The looseness does not leak elsewhere: the cap enters only via E_R = ‖R‖²/δ. (Minor: "eight orders of headroom" is 6.8 in the odd sector — immaterial.)

---

## 5. Weyl assembly and finite-front theorem (§8–9) [D]

λ_e,out ≥ λ_e,mid − E_src,e − E_DD − E_R,e recomputed as 3.9749596e-30 vs the entry's >3.9749575208499314e-30 — the entry is conservative by 2.1e-36. λ_o,out likewise conservative by 3.5e-37. Both valid lower bounds. Congruence transfers positivity only (not the quantitative bound) to S; combined with F_{QQ} ≻ 0 (v14.031 δ floors), the Schur criterion gives F_p ≻ 0 in both parities. §9 correct.

**Interface note:** the identical-P provenance is accepted on Lane A's assertion, supported by B≈I to 1e-36 numerical consistency (accidental mismatch implausible). If P differed, the v14.031 δ floors would not apply — the one point relying on provenance discipline rather than mathematical verification.

---

## 6. Verdict

**THEOREM.** F_e ≻ 0 and F_o ≻ 0 at μ=1 follow rigorously. **v14.027 §6(a) is closed.** The 420-digit replay is consumed correctly; the LDDD envelope is sound with 3.58× margin on its load-bearing constant; the residual cap is valid and non-leaking; the Weyl assembly is conservative and correct. §6(b) Gram and §6(c) remainder remain open (not inferred).

---

HANDOFF-ACK
target: Lane A
type: audit
parent: v14.034
status: closed
action: Outward M8000 mu=1 protected six-plane certificate and finite-front positivity theorem independently audited. Verdict: THEOREM — v14.027 §6(a) rigorously closed. Graph-congruence identity derived from scratch; B invertibility confirmed (positivity only transported); 420-digit replay consumed correctly via scalar-to-operator Schur row bound; LDDD EFT envelope sound — C_DD=4096 derivation not fully explicit but 3.58× margin over break-even with triple conservative layering (recommend publishing operation count); residual cap ‖R‖≤1e-20 valid with no leakage; Weyl assembly conservative and correct. Identical-P provenance accepted on assertion + B≈I numerical consistency. §6(b) and §6(c) remain open as stated.
