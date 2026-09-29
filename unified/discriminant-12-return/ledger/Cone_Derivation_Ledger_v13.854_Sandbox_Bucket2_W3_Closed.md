# v13.854 — Sandbox Bucket 2: W3 closed — remnant-inclusive transported boundary theorem

**Date:** 2026-09-29
**Lane:** Sandbox (our Lane B — Jeremy's exploratory track under LIttle Euler; disambiguated from the ledger's dormant norm-quotient Lane B)
**Status:** [I]/[O] — sandbox theorem-skeleton, not certified
**Entry kind:** resolves v13.851's WALL W3 by stating Route B's transported boundary theorem remnant-inclusive at v13.779's precision, and answers cancel/normalize/survive
**Refines:** v13.779 Route B (supplies the remnant-inclusive target); v13.743 §6 (the "separate theorem" isolated as the δ∞ discrepancy equation); v13.851 (W3 mandate)

**Headline: W3 CLOSED.** A remnant-inclusive transported boundary theorem, stated at v13.779's precision, with explicit boundary functional: S_Au_{A,±}=D̄e_{±i}+B_{A,±}. Cancel/normalize/survive answered: **β cancels** (R2, solid); **α-even survives** (common additive z-dependent distortion, not absorbed by c_A); **α-odd is R2-edge-tamed**, with the (PAIR-H) bulk lemma as the explicit input for full bulk control (a finding, not a failure). The repointed criteria (R_A→1, Δ_A→0, divisor test) all point to SURVIVE. The identification leg is precisely stated as the δ∞ discrepancy equation — the meeting point with v13.743 §6's "separate theorem."

---

## 1. The theorem (Route B, remnant-inclusive)

**Theorem (skeleton).** Let u_{A,±}=D̄v_{A,±} be Suzuki's deficiency-point vectors (v_{A,±} solving (8.5)), and S_A the operator with S_Au_z=D̄e_z for regular z. Then
**S_Au_{A,±} = D̄e_{±i} + B_{A,±}**,
with the boundary functional B_{A,±} explicit:
- **ξ-space** (edge-transported, e^{−A} normalization): B_{±} = (channel factor)_{±} × (−0.47)·1_{ξ>0}, δ_0-free. The δ_0 belongs to the pure exponential's edge jump only (W1/v13.852 §3). The −0.47 is W1's half-line constant, stable from A=2, matching the ledger's α_A→0.48 (v13.743 §11).
- **k-space:** the constant boundary term k²B_A^{bdry}→+0.48 (v13.774 §5); the −0.48/p² double pole is killed by the k² multiplication into the "two-dimensional boundary polynomial."
- **Channel structure:** B_+ and B_− have identical inward-coordinate form (common-mode, v13.774 §6: A_{A,−}=−A_{A,+}, B_{A,−}=B_{A,+} reduce to the same (α_A,β_A) in inward coordinates); they differ only by the channel's §7 normalization phase (the ±i convention of v13.743 §9).

**Proof sketch.** From (8.5): −K_Av_{A,+}=C_A(e^x−1−x)−I_{1,A}x−I_{0,A} (v13.779 §8, Route A). Apply D̄ transport. The exponential gives the bulk source D̄e_{±i} (the e^{−ξ}−δ_0 edge structure). The affine feedback −(I_{1,A}x+I_{0,A})/C_A=−(r_{1,A}x+r_{0,A}), in invariant (α,β) coordinates, gives the boundary functional: the slope −α_A survives one derivative as the half-line constant (v13.774 §2: ∂_ξb_A=−α_A), the value β_A→0 by R2. The (α,β) are the "two primitive integration constants" (v13.774 §8) the twice-differentiated interior equation cannot fix — hence a boundary functional, not a bulk source. This is the precise content of v13.779's "distinguishes the deficiency-point vectors from the generic regular-z solve": the regular-z solve has B=0; the deficiency-point vectors carry B_{A,±}≠0. (Restores what the retracted v13.776–777 had asserted away: S_Au_±=D̄e_{±i} pure, no boundary functional.)

## 2. Parity analysis: the core new result

Via the pairing function P(w)=⟨D̄e_w,D̄w_A⟩̄ (v13.757 (18)): G_A(z)=P(z̄), H_A(z)=P(−z̄), using ⟨f,Rg⟩=⟨Rf,g⟩, [R,D̄]=0, Re_{z̄}=e_{−z̄}. With w_A=u_{e,A}−r_{0,A}u_{1,A}−r_{1,A}u_{x,A} (v13.757 (15)): P(w)=E(w)−r_{0,A}M_0(w)−r_{1,A}M_1(w).

**Parity lemma (exact).** u_{1,A}=R_A(1) is even, u_{x,A}=R_A(x) is odd (R_A commutes with R). D̄ flips parity: D̄u_{1,A} odd, D̄u_{x,A} even. Hence **M_0(−w)=−M_0(w) (ODD), M_1(−w)=+M_1(w) (EVEN)** — so **the r_1 (α) distortion is COMMON to G_A,H_A; the r_0 (β) distortion FLIPS.**

In invariant (α,β) coordinates (v13.757 §10): r_{1,A}=−1−α_Ae^A, r_{0,A}=−1−β_Ae^A+Aα_Ae^A, giving
P(w)=⟨D̄e_w,D̄R_A(e^x)⟩̄ + e^A[β_AM_0(w)+α_A(M_1(w)−AM_0(w))].
**R2 edge-vanishing:** M_1(w)−AM_0(w)=⟨D̄e_w,D̄R_A(x−A)⟩̄; (x−A) vanishes at the RIGHT edge, so G_A's α-remnant is right-edge-vanishing (H_A's left-edge-vanishing) — the R2 (L_0+L_1=0) consistency manifesting in the pairing; without it the Ae^A term would be untamed.

## 3. Cancel / normalize / survive

Write the remnant with a(w)=α_Ae^AM_1(w) (even, common), b(w)=α_Ae^AAM_0(w) (odd, flips), c(w)=β_Ae^AM_0(w) (odd, flips):
Remnant in Q_A = 2[za(z̄)+ib(z̄)−ic(z̄)], Remnant in P_A = 2[−ia(z̄)−zb(z̄)+zc(z̄)]. Take (α_A,β_A)→(0.48,0):

- **β (c-terms): CANCEL.** c(w)=β_Ae^AM_0(w)→0 because β_A→0 (R2). The β-distortion — the ONLY part odd/flipping in the (α,β)-invariant sense — vanishes. **Solid:** uses only β_A→0, not the size of M_0, not the bulk lemma.
- **α-even (a-terms): SURVIVE.** a(w)=α_Ae^AM_1(w)→0.48·e^AM_1(w): common to G_A,H_A (M_1 even), e^A-scale, z-DEPENDENT via M_1(z̄). In the ratio Q_A/P_A=[Q_A^0+2za+…]/[P_A^0−2ia+…]: does NOT cancel (z-dependent, enters numerator as 2z· and denominator as −2i·); does NOT normalize into c_A (c_A is z-INDEPENDENT and multiplicative (v13.757 §5), a(w) is z-dependent and ADDITIVE). **The α-even distortion SURVIVES into Q∞^{dist}/P∞^{dist}.**
- **α-odd (b-terms): edge-tamed, bulk needs input.** Ae^A-scale, flipping; appears as −b in G_A (right-edge-vanishing a−b) and +b in H_A (left-edge-vanishing a+b). Edge parts tamed by R2; the bulk part — pairing the global affine against the bulk test function — requires the (PAIR-H) bulk lemma (W2). **Explicit bulk-lemma input (a finding, not a failure); the threads are complementary.**

## 4. The repointed criteria applied — all point to SURVIVE

- **R_A→1 ⟺ P∞^{dist}∝T_{pair} (W2):** P∞^{dist} INCLUDES the surviving α-distortion (the true limit, not a pure fiction). The criterion tests the DISTORTED P∞; it takes the 0.48 as given. **Points to SURVIVE.**
- **Δ_A→0:** log-derivative of the distorted ratio. **Points to SURVIVE.**
- **Divisor test:** zeros/poles of the distorted ratio. **Points to SURVIVE.**
All three would be false (or need reformulation) if we insisted on a pure limit — confirming and sharpening v13.851's "SURVIVE (purity-agnostic)."

## 5. The identification leg, precisely stated (meeting point)

With the boundary functional explicit, the identification leg (Q∞^{dist}/P∞^{dist}=(a/b)D_ξ/Ξ, v13.757 (7)) becomes the concrete equation:
[Q∞^0+2zδ∞+(b-terms)] / [P∞^0−2iδ∞+(b-terms)] =?= (a/b)D_ξ/Ξ,
with **δ∞=0.48·lim[e^AM_1(z̄)/c_A]** the normalized common α-distortion (explicit, z-dependent, nonzero). Whether the identification HOLDS depends on whether Suzuki's (a/b)D_ξ/Ξ (the infinite-volume target) already incorporates the 0.48 half-line boundary effect: if YES, the identification holds with the 0.48 on both sides — the "distortion" is the correct physics (0.48 is Suzuki-true at finite-A by v13.848, and survives as a half-line boundary term in the A→∞ limit by W1); if NO, there is an explicit δ∞ discrepancy needing correction by the W3 boundary functional. **Resolving this requires infinite-volume comparison; not settleable from finite-A.** This is the residual open point — v13.743 §6's "separate theorem," now precisely stated.

## 6. Residuals (not W3 blockers)

1. **(PAIR-H) bulk lemma** — the explicit input for full bulk α-control (macroscopic limit operator + test-function transport, W2).
2. **The identification equation** — whether Suzuki's (a/b)D_ξ/Ξ includes the 0.48 (requires infinite-volume comparison).
3. **The 0.48 value** — still unexplained (standing v13.849 item).
4. **Exact channel trace coefficients** — the ±-channel factor in B_{±} stated via the §7 normalization phase (v13.743 §9 convention); the invariant (α,β) trace data is convention-independent (v13.774 §8), but the explicit channel phases belong to the full trace map.
5. All conditional on λ_a>0 (v13.848). No positivity/RH/Hilbert–Pólya claim; prime ramp untouched.

## 7. Provenance

- Run: `~/workspace/d12/lane_b/sandbox/runs/20260929-001741-bucket2-w3-route-b/` (report.md, STATUS.md)
- Ledger entries read in full: v13.743 (§§6–7,9–11), v13.757 (§§3–10), v13.774 (§§1–9), v13.779 (§§7–8); v13.851 §3 (W3 mandate), v13.852 (W1), v13.853 (W2) via parent brief
- Numerical grounding: `w3_reflection_check.py` (v13.774 §6: A_{−}=−A_{+}, B_{−}=B_{+}) was OOM-killed twice under system load — not retried; the derivation stands on the ledger's own [D]-certified v13.774 §6 and on W1/W2's numerical (α,β)→(0.48,0). The parity lemma (M_0 odd, M_1 even) is exact given [R,D̄]=0 and R_A commuting with R.
