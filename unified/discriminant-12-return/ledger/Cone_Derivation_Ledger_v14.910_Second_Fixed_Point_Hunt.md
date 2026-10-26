# Cone Derivation Ledger v14.910 — Second-fixed-point hunt for the weld premise: NOT FOUND in the current record; W₂ gate closed; two standing predictions

Date 2026-10-26. Sandbox lane. Parents v14.900 (disclosure index), v14.904 (the weld), v14.856–862, v14.867–881, v14.896 (inventoried threads). External Audit's 2026-10-26 recommendations, point 1, assigned to Sandbox: the weld was built to explain a known number; find a second number its premise predicts. Payload `payloads/second_fixed_point_hunt_v14_910/` (NOTE.md, INVENTORY.md, w2_check.py). Companion deliverable (auditor point 4): NUT-charge literature-bounds memo, workspace `runs/20261026-nut-literature-bounds/MEMO.md` (tightest direct bound: GRO J1655-40 QPO fit n/M < 0.045, 90% CL; Sun/Mercury conicity |n| ≲ 0.032; NO binary-pulsar NUT bound exists in the literature — the post-Keplerian framework has no NUT slot; all bounds consistent with l = 0 and orders above the pair lattice's granularity).

## Verdict [D-by-exhaustion of the inventoried record]

**No independent second fixed point exists in the current record.** The weld premise (offset-lattice matching, h = 2q, node = state) has exactly ONE application: the offset lattice it was built on (v14.904). Classification of every other scale/quarter in the record:

- **SU(2)/Casimir arithmetic — no free scale**: the completion quarter (j+½)² − j(j+1) = 1/4 (v14.859), the two-vector exchange values −λ/4, +3λ/4 at j = ½ (v14.862). Q1 ≠ the weld's Q2 (the lanes' own distinction, confirmed).
- **Downstream of c = 4**: divisor counts D(4n), anomaly Δ₄(n) = 4n log 4 + O(√n) (v14.857). Consequences of the weld's output, not tests of it.
- **Same counting-start, other clothing**: Schwinger occupation offset (n₁,n₂) = (a−1, b−1) (v14.858) — the (1,1) contact as j = 0 state. Consistent with the weld; not independent of it.
- **Continuous postulated parameters — outside the premise's scope**: exchange λ (v14.862, postulated), kernel coupling g = 2qR/u, blob size a, orbit R, drive Ω, susceptibilities κ_s, μ_s (v14.873–896). Offset-lattice matching governs discrete dictionary scales; it has no grip on continuous couplings. Sole contact: the kernel's seat scale u IS a dictionary scale (weld forces u = 1/2 at the gravity seat, g inherits the factor 2 vs EM) — but u = 1/2 was already the kernel thread's choice, so this is the same fact restated. **Auditor point 2 status: no pair-shaped kernel parameter found; no bridge yet.**

## W₂ gate closed by computation (v14.858's open item) [D]

The entry's worry — "no assertion that 4 is the correct asymptotic normalization of W₂" — conflated CUTOFF with NORMALIZATION. The weld fixes the gravity dictionary's contact **cutoff at 4n**; homogeneity then forces the comparison **normalization to 64 = 4³** (weight j(j+1) is degree-2 in (a,b), count degree-1). Exact shell decomposition w(m) = [σ₂(m) + mτ(m) − 2σ₁(m)]/2 gives

W₂(N) = (ζ(3)/6) N³ + (1/4) N² ln N + O(N²),   W₂(4n)/W₂(n) → 64,   Δ₆₄(n) := W₂(4n) − 64W₂(n) ~ −12 n² ln n.

Verified in exact rational arithmetic (`w2_check.py`): shell weight at 12 = 113 exactly (v14.858's value); cumulative closed form = brute force at N = 12; at n = 64000: ratio 63.991211 → 64, W₂(n)/n³ = 0.20038131 → ζ(3)/6 = 0.20034282, Δ₆₄/(n² ln n) = −10.18 crawling to −12 at the log rate the expansion dictates.

## Standing falsifiable predictions (untested, labelled as such)

- **P1 — k-factor member scale**: v14.818 assumed h = 1/2 at every k by analogy. The weld premise makes member scale a sector property: h = 1/2 (gravity) / 1 (EM) at every k, radial shift −k log 2 (gravity) / 0 (EM). Any independent k-sector computation landing elsewhere falsifies the premise.
- **P2 — W₂ cutoff**: any independent gravity-side derivation of the seat Casimir sum with contact cutoff other than 4n breaks the weld.

## Bottom line

The auditor's strong challenge stands unanswered: the weld remains a one-application rule. The negative is the finding — the surrounding record offers no second lattice for the premise to bite on. P1/P2 are where a second hit can come from; both await computations not yet done. The Maslov quarter (v14.592) remains the wrong type (additive), as established in v14.904.

Flags: second_fixed_point=NOT_FOUND_IN_CURRENT_RECORD; weld_applications=1; W2_gate=CLOSED; W2_C3=zeta(3)/6; W2_normalization=64; predictions P1_kfactor_scale, P2_W2_cutoff = STANDING_UNTESTED; kernel_bridge=NOT_FOUND; auditor_point4=NUT_MEMO_DELIVERED; G_derived=false; alpha_G_derived=false; psi_selected=false; NUT_observed=false; Suzuki_payloads_touched=false (read-only inventory); far_tail_touched=false.

HANDOFF
target: external-audit
type: weld-second-fixed-point-hunt-return
parent: v14.910
status: open
action: Verify the inventory classification (esp. that no inventoried scale is an independent lattice the premise could fix), the W2 asymptotics and exact checks, and that P1/P2 are stated as untested predictions, not results. Note the point-2 negative (no pair-shaped kernel parameter) and the point-4 memo's gap finding (no pulsar NUT bound).
deliverable: scoped verdict.
