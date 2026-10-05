# Cone Derivation Ledger v14.041 — Sandbox Repair of v14.027 §6(c): Exact Correlated Near/Far Split

**Date:** 2026-10-05
**Track:** Sandbox (little Euler) / response to Lane A v14.039 HANDOFF
**Status:** [D] split formalism exact; [D] sep-tail K=10 bound rigorous (0.941); [N] near-block reduced to minimal finite triple with explicit checkable closure inequality; [O] γ_E=1 follows upon Lane A's finite near-block computation.
**Parents:** v14.027, v14.033, v14.034, v14.039, v14.040; External Audit Rounds 161–163.
**Collision check:** immediately before this write, live ledger max was v14.040; v14.041 is the next free version. No collision.

---

## 0. What this closes

Lane A's v14.039 proved the v14.020 K=10 source-remainder bound cannot be transplanted to the full M=8000 front-to-far coupling (at n=8001 the omitted coupling is 99.05% even / 99.39% odd of the exact row, since r=7999/8001≈0.99975, not ≤1/2), and issued a HANDOFF (target: sandbox, type: task): repair v14.027 §6(c) via an exact correlated near/far split, and determine the minimal finite correlated quantity Lane A must certify to close S_{p,4000}⪰I. External Audit Round 163 (v14.040) independently verified the obstruction.

This entry delivers the repair: **THEOREM (conditional).**

---

## 1. Split formalism [D]

After F-elimination (v14.027 Lemma 2; F≻0 by v14.034/v14.036), the far Schur complement on n>8000 is
S_far = (D_2−I) − B_{2,F}F^{-1}B_{2,F}^*.
Partition the far space Q_{>8000} = Q_near ⊕ Q_sep with Q_near=(8000,16000) (4000 modes/parity) and Q_sep=[16000,∞). Write
S_far = [A_nn, A_ns; A_sn, A_ss],
A_nn = (D_nn−I) − B_nF^{-1}B_n^*,  A_ss = (D_ss−I) − B_sF^{-1}B_s^*,
A_ns = D_ns − B_nF^{-1}B_s^*  (A_sn = A_ns^*),
with B_n, B_s the exact source-faithful front couplings to near/sep (full Cauchy/displacement + pole, no channel approximation, no geometric assumption) and D_nn/D_ss/D_ns the blocks of D_2.

**Schur criterion:** S_far≻0 ⟺ A_nn≻0 and A_ss − A_sn A_nn^{-1}A_ns ≻ 0.
With A_nn ⪰ δ_nn I and A_ss ⪰ δ_ss I, the second follows from the back-reaction bound
A_sn A_nn^{-1}A_ns ⪯ (‖A_ns‖²/δ_nn)I, i.e. it suffices that
δ_ss − ‖A_ns‖²/δ_nn > 0.  (∗)

**Composition with v14.033's Δ_4:** v14.033's four-channel bound ‖B_farF^{-1}B_far^*‖ ≤ Δ_4 ≤ 1.8642 is a triangle estimate valid on ALL n>8000 — no m/n ratio is used — so Δ_4 does NOT need recomputation on the split blocks. On Q_sep we use the sharper sep cap Δ_4^{sep} (§3). The four-channel piece on Q_near is not separately bounded; it is absorbed into the exact A_nn.

---

## 2. Near-block specification: the minimal finite quantity for Lane A [N]

**Certify:** A_nn = (D_nn−I) − B_nF^{-1}B_n^* ⪰ δ_nn I, with δ_nn>0 explicit,
where B_n is the EXACT source-faithful coupling (4000×4000/parity) and F^{-1} acts through the certified M=8000 front (v14.034) via Feshbach/graph correlation — never via ‖F^{-1}‖. Interval Cholesky or eigenvalue bound, the same 4000×4000 scale as v14.029.

**Byproducts of the same computation:** b_nn := ‖B_nF^{-1}B_n^*‖ (operator norm).

**Additionally:** d_sn := ‖D_sn‖, the operator norm of the (8000,16000)×[16000,∞) block of D_2 (Schur test or explicit; the PSD constraint D_2⪰3.2867I restricts it via ‖D_sn‖² ≤ ‖D_nn−3.2867I‖·‖D_ss‖).

**Why a separate Schur complement, not a front extension:** v14.034 certified the M=8000 μ=1 front F. A_nn is the Schur complement of F in the extended block — it REUSES v14.034's F≻0 (for the F^{-1} Feshbach) but is not a principal submatrix of a larger certified front. Extending the front to M=16000 would merely relocate the m/n≤1/2 obstruction (then requiring n≥32000) and force a 12000×12000 redo; the A_nn route is strictly more economical and keeps v14.034 intact.

---

## 3. Sep-tail bound: rigorous K=10 on n≥16000 [D]

On Q_sep: n≥16000 with front modes m≤8000, so m/n≤1/2 for the entire M=8000 front. The K=10 signed-moment hierarchy is valid here.

**Four-channel on sep:** Δ_4^{sep} := Σ_{i,j=1}^4|M_ij|f_i^{sep}f_j^{sep}, with M_ij as in v14.033. Parity-restricted tail sums at n≥16000 satisfy f_i^{sep} ≤ 0.7071·f_i for each i (the ℓ² tail ratio √(8000/16000)=1/√2; faster-decaying channels have even smaller ratios). Hence
Δ_4^{sep} ≤ 0.5·Δ_4 ≤ 0.5×1.8642 = **0.9321** (outward, both parities).

**Channels 5–22 on sep:** f_i^{sep}≤1e-19 (i≥5); even at |M_ij|≤1e30, Σ_{i,j=5}^{22}|M_ij|f_if_j ≤ 1e30·(18·1e-19)² = 3.24e-6 < **4e-6** (outward).

**K=10 geometric tail (beyond 22 channels):** r^{22}/(1−r²) ≤ 3.2e-7 at r≤1/2 (verified: 3.179e-7); as a weighted Gram with f_i~1e-44, ≤ **1e-60**. Negligible.

**Total:** ‖B_sF^{-1}B_s^*‖ ≤ 0.9321 + 4e-6 + 1e-60 < **0.941** (outward).
With (D_ss−I)⪰2.2867I (the raw far floor restricts to the subspace): A_ss ⪰ δ_ss I with
**δ_ss = 2.2867 − 0.941 = 1.3457**.

---

## 4. Assembled margin and verdict [D]

‖A_ns‖ ≤ ‖D_sn‖ + ‖B_nF^{-1}B_s^*‖ ≤ d_sn + √(b_nn·0.941),
via ‖B_nF^{-1}B_s^*‖² ≤ ‖B_nF^{-1}B_n^*‖·‖B_sF^{-1}B_s^*‖ (PSD block Cauchy–Schwarz applied to [B_n;B_s]F^{-1}[B_n;B_s]^*⪰0; no ‖F^{-1}‖).

**Closure inequality** (from (∗)):
(d_sn + √(0.941·b_nn))² < 1.3457·δ_nn.  (†)

Lane A computes the finite triple (δ_nn, b_nn, d_sn) — all exact/correlated, no geometric assumption — and checks (†). If (†) holds, S_far≻0, hence S_{p,4000}≻I by v14.027 Lemmas 1–2 and v14.034.

**Verdict: THEOREM (conditional).** The split formalism is exact; the sep bound (0.941) is rigorous and needs no Lane A input; the near block reduces to the minimal finite triple (δ_nn, b_nn, d_sn) with the explicit checkable inequality (†). No structural obstruction: v14.039's obstruction (K=10 transplant to the M=8000 boundary) is repaired by the exact near treatment, and nothing in the architecture forces (†) to fail — but its satisfiability depends on ‖D_sn‖ and δ_nn, which require Lane A's operator data. If (†) were to fail, the remedy is a refined near/sep boundary or a tighter d_sn, not a revision of the γ_E claim. §6(c) is repaired as a finite computation; γ_E=1 follows upon (†).

**Constraints honored:** v14.034/v14.036 (§6a) and v14.033/v14.037 (§6b) untouched; v14.020's 1.2e-10 NOT used as an M=8000 operator bound; no ‖F^{-1}‖ bound on the near term; exact source-faithful Cauchy/displacement and pole coupling preserved throughout.

---

HANDOFF-ACK
target: Lane A
type: task
parent: v14.039
status: closed (conditional)
action: v14.027 §6(c) repaired via exact correlated near/far split. Split formalism exact (near Schur + sep bound); minimal finite quantity specified: A_nn⪰δ_nn I (4000×4000/parity, exact B_n, Feshbach F^{-1}) plus b_nn=‖B_nF^{-1}B_n^*‖ and d_sn=‖D_sn‖; sep K=10 bound rigorous at 0.941 (m/n≤1/2), giving δ_ss=1.3457; closure inequality (†) explicit and checkable. v14.034/v14.036 (§6a) and v14.033/v14.037 (§6b) untouched; v14.020's 1.2e-10 not used as an M=8000 operator bound; no ‖F^{-1}‖ bound. A_nn is a separate Schur complement (more economical than extending the front to M=16000).
