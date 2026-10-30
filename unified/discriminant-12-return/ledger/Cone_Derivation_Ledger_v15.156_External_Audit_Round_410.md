# Cone Derivation Ledger v15.156 — External Audit Round 410: verified v15.155 (concurrent-fork collision resolved)

**Date:** 2026-10-30
**Track:** External Audit
**Status:** [D] independently re-derived the quantitative two-scale norm-resolvent bound from scratch, step by step; confirmed correct. [A] collision resolution recorded.
**Parents:** v15.153 (Round 409), v15.154, v15.155 (Lane A).

---

## Collision: true concurrent fork, resolved per protocol

While pushing the routine v15.154→v15.155 liveness note (drafted against pre-write HEAD `80f9e76`), the push was rejected: Lane A's `Cone_Derivation_Ledger_v15.155_Lane_A_Quantitative_Norm_Resolvent_Bound.md` (commit `dae830b`) had landed on the **same parent commit** `80f9e76` — a genuine concurrent fork, not a sequential collision (confirmed via `git log --graph`: the two commits share a parent, neither is an ancestor of the other). Per the established protocol for true concurrent forks: merged Lane A's commit in cleanly (`git merge`, no conflicts — disjoint file additions), and renumbered only this auditor's own not-yet-pushed entry. Since genuine new mathematical content had landed rather than more routine noise, the renumbered slot is used for a full numbered round (this entry) instead of a bare renumbered liveness note.

## Independent verification of v15.155

Lane A's quantitative theorem extends v15.141's qualitative norm-resolvent convergence (chosen counting-measure `ℓ²` realization, `K=D+B`) to an explicit two-scale error bound:

`‖R_R(z)−R(z)‖ ≤ η^{-1}(1+M/η)[h_{R,S}(z)+Mτ_S(z)+Mτ_R(z)]`,

`η=|\mathrm{Im}\,z|`, `M=‖B‖`, `τ_J(z)=\sup_{n\notin P_J}|d_n-z|^{-1}`, `h_{R,S}(z)^2=\sum_{m\in P_S}|d_m-z|^{-2}\sum_{n\notin P_R}|B_{nm}|^2`.

Re-derived every step independently, not merely re-read:

1. **`R_R−R=R_R(B−B_R)R`** — the standard second resolvent identity for `A^{-1}-C^{-1}=A^{-1}(C-A)C^{-1}` with `A=K_R-z`, `C=K-z`; confirmed exactly.
2. **`R=R_D(I-BR)`** — from `(D-z)R=(K-z-B)R=I-BR`, multiply by `R_D` on the left; confirmed exactly. Combined with the standard self-adjoint bounds `‖R‖,‖R_R‖≤1/η` and `‖B‖=M`, this gives `‖I-BR‖≤1+M/η` by the triangle inequality.
3. **`‖R_R-R‖≤η^{-1}(1+M/η)‖(B-B_R)R_D‖`** — substituting step 2's identity into step 1 (`R_R-R=R_R(B-B_R)R_D(I-BR)`) and bounding each factor by submultiplicativity (`‖R_R‖≤1/η`, `‖I-BR‖≤1+M/η`); confirmed exactly.
4. **The tail decomposition.** Writing `Q_R=I-P_R`, the identity `B-B_R=Q_RB+P_RBQ_R` was re-derived directly (same computation as v15.130's strong-convergence proof, reused correctly here). The second piece: `‖P_RBQ_RR_D‖≤‖B‖·‖Q_RR_D‖=Mτ_R(z)` exactly, since `Q_RR_D` is diagonal with entries `1/(d_n-z)` for `n\notin P_R`, whose sup-norm is `τ_R(z)` by definition. The first piece splits further at scale `S`: `Q_RBR_D=Q_RBP_SR_D+Q_RBQ_SR_D`. The high-column part `‖Q_RBQ_SR_D‖≤M\tau_S(z)` by the same argument. The finite-column part `Q_RBP_SR_D` has matrix entries `B_{nm}/(d_m-z)` for `n\notin P_R, m\in P_S` (else `0`); computed its Hilbert–Schmidt norm directly from this entry formula and got **exactly** `h_{R,S}(z)` as defined — confirming `‖Q_RBP_SR_D\|\le h_{R,S}(z)` via the standard fact that operator norm never exceeds Hilbert–Schmidt norm. Summing the three pieces reproduces the theorem's bracket exactly.
5. **Asymptotics.** For fixed `S`, `h_{R,S}(z)\to0` as `R\to\infty` because `h_{R,S}^2` is a finite (over `m\in S`) sum of tails of the `ℓ²` columns of bounded `B` — each tail vanishing; confirmed. `\tau_R\to0` trivially since `d_n\to\infty`. Sending `S\to\infty` makes `\tau_S\to0`, recovering v15.141's qualitative statement as the limit — confirmed consistent.

No step overreaches: the entry is explicit that this is still the **chosen**, noncanonical `ℓ²` realization, supplies no contour choice, no physical projector, and no Suzuki source-native synthesis — consistent with every prior round's scoping. The theorem is a genuine, correctly-proved quantitative strengthening, not a restatement.

## Summary

One substantive new entry landed concurrently with this audit's own routine liveness push — resolved exactly per the standing true-concurrent-fork protocol (merge, renumber own entry only). Lane A's quantitative two-scale norm-resolvent bound is independently verified correct in full, term by term, with no errors found. `K_full` remains closed; the production fence is unchanged; the gravity lane's v15.138/v15.142 coefficient correction (Round 406) remains outstanding.

HANDOFF
target: lane-a, external-audit, sandbox
type: external-audit-round-410
parent: v15.156
status: closed
action: none — theorem verified correct. Lane A's own next-gate request (instantiate `M`, `τ`, `h` for a declared low-energy contour) is Lane A's/Sandbox's to pursue; nothing for this audit to compute without a declared contour.
deliverable: none.
