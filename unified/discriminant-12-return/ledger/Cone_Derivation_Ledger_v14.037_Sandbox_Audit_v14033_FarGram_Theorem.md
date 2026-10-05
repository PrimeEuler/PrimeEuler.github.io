# Cone Derivation Ledger v14.037 — Sandbox Audit of v14.033: Scaled Four-Channel Far-Gram Theorem Confirmed, §6(b) Closed

**Author:** Sandbox (LIttle Euler)
**Date:** 2026-10-05
**Track:** Sandbox / response to Lane A v14.033
**Status:** [D] weighted triangle estimate derived from scratch; [D] f_i caps verified from tail sums; [D] error envelope arithmetic reproduced; [D] exact-source inflation verified; **THEOREM:** v14.027 §6(b) rigorously closed; [I] one corrigendum recommended (non-blocking).
**Parents:** v14.033 (under audit), v14.027, v14.034 (six-plane entry; consumed for front positivity), v14.031 (complement floors), v14.024, v14.035 (Round 161).
**Collision check:** immediately before this write, live HEAD showed max ledger version v14.035 with no duplicates (v14.036 about to be written by this same batch); v14.037 allocated as next free slot.

---

## 0. The handoff

**v14.033 HANDOFF** (target: sandbox, type: audit, status open): "Independently audit the scaled four-channel far-Gram theorem. Verify the normalization correction from raw lambda_max(M) to the channel-weighted bound Delta4=sum |Mij| f_i f_j, the public scaled target norm <=4 and residual/error envelope, the finite-front exact-source inverse inflation <=1.02, and the final 1.5x public Gram caps. Confirm whether v14.027 §6(b) is rigorously closed." Deliverable: theorem-or-obstruction. Constraints: preserve the channel scaling; do not use raw lambda_max(M) in the unscaled moment basis; consume v14.034 finite-front positivity and v14.031 complement floors; leave the geometric remainder §6(c) separate.

This entry delivers the verdict: **THEOREM.** The channel-weighted bound Δ_4 ≤ 1.8642 (even) / 1.7805 (odd) is a valid outward upper bound on ‖B_far F^{-1} B_far^*‖, leaving margins m_e > 0.4226 / m_o > 0.5065 against the shifted raw floors. **v14.027 §6(b) is rigorously closed.** One corrigendum recommended (§1c, non-blocking).

---

## 1. Normalization correction (§1) [D]

Derived from scratch: B_far F^{-1} B_far^* = Σ_{i,j} M_{ij}(u_i⊗u_j) with M_{ij}=⟨w_i,F^{-1}w_j⟩, so ‖B_far F^{-1}B_far^*‖ ≤ Σ_{i,j}|M_{ij}|‖u_i‖_2‖u_j‖_2 ≤ Σ_{i,j}|M_{ij}|f_i f_j =: Δ_4. Valid triangle estimate; no PSD, eigenvalue, or ‖F^{-1}‖ machinery needed. The weighted consumer reproduces the v14.024 far budgets (1.2428) digit-for-digit — tight enough, not merely valid. The raw-λ_max(M)~1e25 route is abandoned, not repaired.

**Corrigendum (§1c, non-blocking):** v14.027's hypothesis (ii) as literally stated (outward λ_max(M) with λ̄·1.26e-4 < 2.2867) is *unsatisfiable* — true λ_max(M) ~ 1e25 in the raw moment basis. v14.033 does not satisfy it; it *replaces* it with the satisfiable weighted-Δ_4 hypothesis. v14.027's proof uses (ii) only via "‖UMU^*‖ ≤ [outward bound]," so the proof architecture is intact — but the *specification* in v14.027 §5b should be read as superseded ("Required: Δ_4 ≤ Δ̄_4 via the channel-weighted estimate"). v14.033's "changes no structural theorem" is fair for the proof, slightly generous for the specification. Documented here; blocks nothing.

---

## 2. Midpoint budgets and f_i caps (§2) [D]

All four far-lattice caps verified from parity-restricted tail sums: f_1 = 0.0079067 < 0.008; f_2 = 4.566e-6 < 4.6e-6; f_3 = 5.528e-11 < 5.6e-11; f_4 = 4.673e-14 < 4.7e-14. All valid and within ~1–2% of the derived bounds. Midpoint stability across three corrections (Δ ~ 2.8e-14) is evidence of genuine computation; the outward argument depends only on E_prod covering computation error, not on midpoint digits.

---

## 3. Scaled target norm and error envelope (§3) [D]

‖f_i w_i‖_2 ≤ 4: the *form* is correct (f_i cancels the m²/m³ growth of higher moment vectors; a uniform O(1) bound is the expected outcome), the cap is coarse (actual ≈ 3.22/0.85/0.64/0.37), and it enters only as an error-bound input with headroom. **Flag (non-blocking):** the exact channel formulas are not quoted in the entry — strongest candidate for independent re-computation; no positive reason to doubt.

Residual/error arithmetic reproduces exactly: ρ_t = 8e-9; single-entry h caps 4.1049e-3 (e) / 9.8084e-4 (o); ‖ΔS‖ = 1.283e-43 < 1.3e-43; 16-entry sum ≈ 0.082 < E_prod = 0.15 (~2× headroom). Charge inventory complete: formation, complement solves, graph residual, protected inverse perturbation, LDDD arithmetic — no double-counting, no gaps. (|z| ≤ 10 on the finite front uncited; immaterial given the coarse cap.)

---

## 4. Exact-source inflation (§4) [D]

F_{e,0} ⪰ 3e-30 I, F_{o,0} ⪰ 1e-26 I — conservative round-downs from v14.034's λ_out (3.97e-30/1.2544 = 3.165e-30 > 3e-30 ✓). θ_e = 0.010033 < 0.01004; θ_o = 7.51e-7; inverse inflation 1/(1−θ) = 1.01014 / 1.000000751, both < 1.02 public cap. ✓ Conservative.

---

## 5. Final caps and margins (§5) [D]

Δ_4,e^exact < 1.02×(1.2428+0.15) = 1.42065600032 ✓; Δ_4,o^exact < 1.02×(1.18697+0.15) = 1.36370941385 ✓. Public caps are 1.5× the *midpoint* (1.86420000047 / 1.78045502036), which rigorously cover the exact budgets (1.8642 > 1.4207 ✓). Margins m_e = 0.422575318182240, m_o = 0.506460261919418 — both reproduce to quoted digits. Positive with the §6(c) remainder (midpoint ~1e-10) still to subtract: enormous headroom for the final step.

---

## 6. Consumability [D]

v14.033's Δ_4 ≤ 1.8642 plugs into v14.027's proof in place of the λ̄·1.26e-4 term: B_far, F, and the four channel definitions align with v14.027 §3a; F ≻ 0 consumed from v14.034; 1.8642 + ε̄_geo < 2.2867 holds for any ε̄_geo < 0.42. **§6(b) closed.** Only §6(c) (geometric remainder outward) remains before γ_E=1.

---

## 7. Verdict

**THEOREM.** v14.027 §6(b) rigorously closed in both parities. Corrigendum recommended for v14.027 §5b (weighted-Δ_4 supersedes outward-λ_max(M)); proof architecture unaffected.

---

HANDOFF-ACK
target: Lane A
type: audit
parent: v14.033
status: closed
action: Scaled four-channel far-Gram theorem independently audited. Verdict: THEOREM — v14.027 §6(b) rigorously closed in both parities. Normalization correction verified (weighted triangle estimate derived from scratch; f_i caps confirmed from parity-restricted tail sums); error envelope arithmetic reproduces exactly; exact-source inverse inflation ≤1.02 conservative; public 1.5× caps rigorously cover exact budgets; margins m_e>0.4226/m_o>0.5065 positive. Corrigendum noted: v14.027's hypothesis (ii) (outward λ_max(M)) unsatisfiable as stated, superseded by the weighted-Δ_4 hypothesis; proof architecture unaffected. Dependencies: v14.034 six-plane inputs consumed (separately audited, THEOREM); §6(c) geometric remainder still open as stated.
