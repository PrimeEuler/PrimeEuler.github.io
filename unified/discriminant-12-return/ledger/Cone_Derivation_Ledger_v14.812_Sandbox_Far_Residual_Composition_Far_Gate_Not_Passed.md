# Cone Derivation Ledger v14.812 — Sandbox: far-residual composition for the v14.585 handoff (actions 3–4) — evaluated F1/F2 classes exceed the far headroom in both sectors; the far gate is NOT passed and the scoped v14.583 delivery stands

**Date:** 2026-10-24 EDT. **Lane:** sandbox (our Lane B). **Parents:** v14.442 (budget), v14.444 (allowances), v14.447 (freeze), v14.583 (residual composition pass), v14.584 (seed payload), v14.585 (Lane A handoff opening the far gate), v14.586 (Audit R320), v14.589 (handoff actions 1–2 closed).
**HANDOFF ANSWERED:** v14.585 actions (3)–(4) — construct and evaluate the two-sector far residual from modes 4161533/4161534 through infinite support on the frozen v14.447 moments, and compare DM + far against the budget in exact ℓ² quadrature. This entry discharges the construction and the exact comparison. **The comparison fails**; the infinite-support certificate is therefore not issued, and the F3 tail construction is moot for this trial/seed pair (§4).
**Collision check:** live HEAD checked immediately before this deposit (commits API): max ledger version v14.811; v14.812 free.
**Deposits:** `research-notes/payloads/sandbox_far_residual_composition_v14_812/` — `far_compose.py` (producer), `run_far_compose.sh`, the four class certificates `far-residual-{even,odd}-v-{F1,F2}.json`, the two sector summaries `far-residual-{even,odd}-v-summary.json`, and `RESULTS.md` (full analysis record). Residual buffers are referenced by SHA-256 from the class certificates (even F1 `4682c363591f5f27…`, even F2 `11a331d1c8ebfe5f…`, odd F1 `5c709572c51c6bcd…`, odd F2 `dfbbece8d7d414a4…`); input buffers are the hash-pinned certificates of the far compact producer and the v14.584 seed assembly.

Conventions: identical to the audited v14.583 composition. Per row, residual_i = S // (first + 2i − shift) − compact_i − seed_i at S = 2^256 (bare source 1/n even, 1/(n−1) odd); directed sqrt at the S grid; physical error = compact ℓ² error + seed ℓ² error + bare floor error upper(count)/S. Transport charges were each charged exactly once in v14.442 and are not charged again. Classes: F1 = modes [4161533, 8323063) even / [4161534, 8323064) odd, 2,080,765 rows; F2 = [8323063, 16646127) / [8323064, 16646128), 4,161,532 rows.

## §1 Composition and verification [D, N]

The composer streams both sectors' classes against the hash-pinned compact buffers (widths 30 on F1, 29 on F2, per their certificates) and seed buffers (width 30), accumulating the exact integer sum of squares per class. Verification, three independent routes: (i) smoke runs on the first 8,192 rows of F1 in each sector cross-check every row against an exact Fraction evaluation of the defining formula (agreement inside the 2/S floor window); (ii) per class, 23 rows (edges, thirds, 16 fixed pseudo-random rows) are re-read by independent seeks and satisfy residual + compact + seed = S // (first + 2i − shift) exactly; (iii) a separate re-decode of the four written residual buffers reproduces the certificate point norms to all printed digits. Error terms are negligible throughout (largest: seed F1 ℓ² error 9.06e-12 even / 9.16e-12 odd; compact errors ≤ 8.15e-21): the physical uppers below are the evaluated point norms to seven digits.

## §2 Evaluated far classes [D]

Physical residual uppers (point norm in parentheses):

- even F1: **4.1440528e-05** (4.1440519e-05); even F2: **3.2606786e-05** (3.2606786e-05).
- odd F1: **4.1366390e-05** (4.1366381e-05); odd F2: **3.2550819e-05** (3.2550819e-05).

Finite far total (exact ℓ² quadrature of the two class uppers): even **5.2730635e-05**, odd **5.2637762e-05**.

## §3 Exact budget comparison [D]

Against the frozen v14.442 budget q and the v14.583 DM physical uppers (exact Fractions in the sector summaries):

- even: q = 4.9513108e-10, DM upper 4.8145856e-06, far headroom √(q − DM²) = 2.1724430e-05. F1² + F2² = 5.8915 × headroom²; headroom² − (F1² + F2²) = **−2.3085690e-09**.
- odd: q = 4.9673591e-10, DM upper 4.8057856e-06, far headroom = 2.1763279e-05. F1² + F2² = 5.8499 × headroom²; headroom² − (F1² + F2²) = **−2.2970936e-09**.

The evaluated finite far classes alone exceed the entire far headroom in both sectors, before any F3 contribution. DM² + F1² + F2² ≤ q fails exactly. **Far gate: NOT PASSED.**

## §4 Mechanism [N, empirical]

The miss is structural, not numerical noise. On the evaluated rows (even sector; odd agrees to ~1%): the seed cancels the bare source to ‖bare − seed‖ = 1.994e-05 (F1) / 1.413e-05 (F2), about 8% relative; the changed compact action's far tail contributes ‖compact‖ = 4.370e-05 / 3.137e-05. The full residual carries a clean persistent 1/n term: block means of residual_n · n (2^16-row blocks) over each class's top octave are +0.1596 ± 0.0008 (even F1), +0.1771 ± 0.0005 (even F2), +0.1593 ± 0.0008 (odd F1), +0.1768 ± 0.0005 (odd F2), with slightly positive per-block slope — ρ(n) is flat-to-rising across n = 4.16e6…1.66e7 and does not decay toward zero. On DM rows the same machinery cancels the source to 1.4%; on far rows only to ~17%.

This is the failure branch pre-registered in the sandbox derivation notes (2026-10-19): the F3 bound was to be assembled on channel coefficients whose total 1/n coefficient must vanish as a certified identity; the evaluated rows show it does not vanish for this trial/seed pair, so no F3 envelope on this pair can close the bound, and constructing one is moot. The exact attribution of ρ(n) among the seed's affine-model defect (W₀ vs 1), the compact coefficient −(c·Z₀^trial − d^trial), and the seed channel coefficients is left open; the verdict in §3 does not depend on it.

## §5 Scope and standing results

Nothing here touches the v14.583 scoped delivery: the DM composition passes inside its allowance with positive far headroom, exactly as certified and as Audit R320 confirmed. What fails is only the extension of the same frozen approximant (changed compact trial + noncompact seed) to the far rows at the frozen budget. Whole-residual acceptance remains uncertified; the remaining global items (whole infinite action, represented residual, stationary pair, capacity closure) are unaffected in status. Closing the far gate would require an approximant whose total far 1/n coefficient vanishes; no such trial/seed pair is frozen, and proposing one is Lane A's geometry, not this handoff.

Flags: `far_residual_composition_complete=true`, `far_finite_classes_evaluated=true`, `f3_tail_evaluated=false_moot_for_this_pair`, `far_gate_passed=false`, `whole_residual_acceptance_certified=false`, `scoped_v14_583_delivery_stands=true`, `global_transport_charged_again=false`, `papers_modified=false`.
