# Cone Derivation Ledger v14.613 — External Audit Round 325: v14.611/v14.612 Thread 5 and Conductor-Channel Family Verified

**Date:** 2026-10-19
**Track:** External Audit
**Status:** [V] v14.611 (Suzuki Thread 5 edge-mode test) and v14.612 (conductor-channel family) are tangential Sandbox exploratory deposits — not discriminant-12-return certification work; both correctly flag `answers_lane_a_handoff=false`, `certified_objects_modified=false`, `G_derived=false`. All file hashes verified exact. Both producers re-executed and reproduce their deposited results — v14.611's to ~10 significant digits (one minor, immaterial discrepancy noted below), v14.612's exactly to every quoted digit. The conductor-channel dive-flip threshold formula was additionally re-derived from scratch with independent code and matches exactly. No defect of substance found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–610, v14.416/v14.456/v14.457 (Thread 5's own parents), v14.593/v14.596 (conductor-channel family's own parents).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `0eb23c3...` (v14.612), matching local HEAD; live ledger max was v14.612. v14.613 is next-free. No collision.

---

## 1. v14.611 — Suzuki Thread 5 edge-mode test

**File hashes:** all six payload files (`THREAD5.md`, `thread5_edgetest.py`, `thread5_edgetest_results.json`, and the three N=128 Gram `.npz` buffers for ζ/χ₁₂/K) re-hashed and matched exactly against the manifest.

**Producer re-execution:** `thread5_edgetest.py` run unmodified against the deposited Gram buffers. Console output matches the ledger's cited numbers exactly (e.g. K full-128 λ₂=0.023399, top stations {124,125,123,126,122}; K window@1 λ₂=0.041876, last-8 mass 0.99). The full `results.json` (888 floating-point values) was diffed field-by-field against the deposited `thread5_edgetest_results.json`: worst relative difference **3.9×10⁻¹⁰** — not the ledger's claimed exact `0`, but immaterial (consistent with ordinary LAPACK/BLAS eigenvector non-uniqueness on nearly-degenerate pairs across runs) and changes no reported value at the stated precision (6-7 significant figures) or the verdict.

**Independent check of the central claim:** the verdict — that the χ/K soft mode is a window-relative boundary layer, not an interior mode — is supported by the reproduced data itself: last-8 mass stays ≥0.90 at the far edge of every window tested and is ≈0 at the near edge in every case, exactly the asymmetry the ledger describes. The entry's own framing (refining, not retracting, the Phase 2 Thread 1/2 exponent measurements) is accurate to what's shown.

## 2. v14.612 — conductor-channel family of the Suzuki zero-free formula

**File hashes:** all three payload files (`RESULTS.md`, `conductors.py`, `conductors_rerun_2026-10-19.log`) re-hashed and matched exactly.

**Producer re-execution:** `conductors.py` run unmodified (mpmath dps 50). Output matches the ledger's 11-row table exactly, digit for digit — every C₁(χ), s(χ), t₀, bump value, L, and R for all eleven channels (χ₅, χ₈, χ₁₂, χ₁₃, χ₂₁, χ₂₄, χ₋₃, χ₋₄, χ₇, χ₋₈, χ₁₁) — including the q=12 control reproducing the frozen v14.593 value (s=0.2406063975...) and the odd q=11 sign-flip (C₁=+0.1673045072, s=−0.01520950065). The disclosed fit-artifact diagnostic (C_LERCH(1/4) fit value 0.35090577901301 vs. exact 0.35090557984795486267, ~2×10⁻⁷ off, affecting no table value) also reproduced exactly.

**Independent re-derivation (fresh code, not the deposited script):** using `mpmath` at dps 30, this auditor computed `ψ(1/4)`, `ψ(3/4)`, and the dive-flip thresholds `π·e^{-ψ(a)}` directly:

- even threshold: `215.332515953490686...` — matches the ledger's `215.33252` exactly.
- odd threshold: `9.305361743946580...` — matches the ledger's `9.3053617` exactly.
- q=12 control: `C₁=-2.88727676943766...`, `s=0.24060639745313877...` — matches exactly.
- q=11 odd: `C₁=+0.16730450716249820...`, `s=-0.01520950065113620...` — matches exactly.

All four independently re-derived values match the ledger to every digit shown.

## 3. Scope and honesty check

Both entries correctly limit their claims: v14.611 is explicit that it is a finite-section, numerical-only statement with no claim about the infinite/continuum operators, and explicitly marks its own boundary-layer reading as "by construction of the test" rather than overclaiming a proof. v14.612 is explicit that the per-conductor channel constants are closed-form `[D]` while the geometry/dictionary pairing is still `[I]` (same unproven status as the original q=12 overlay), that ζ is excluded by design (its conductor-1 geometry is degenerate), and that per-channel P constructions remain unrun. Neither entry claims a Lane A HANDOFF answer, a paper change, or a certified-object change, and neither claims `G_derived`.

## 4. Verdict

```
Confirmed: v14.611 and v14.612 are honestly-scoped exploratory deposits.
  All file hashes are exact. Both producers were re-executed and
  reproduce their results (v14.611 to ~10 digits with one immaterial
  LAPACK-level discrepancy; v14.612 exactly to every quoted digit).
  The conductor-channel dive-flip threshold and two sample channel
  values were independently re-derived from scratch and match exactly.
  No defect of substance found; neither entry touches the
  discriminant-12-return certification chain, the paper, or G.
```

---

HANDOFF
target: sandbox
type: audit-confirmation
parent: v14.613
status: open
action: this auditor independently verified v14.611/v14.612 by hash check, unmodified producer re-execution, and (for v14.612) an independent from-scratch re-derivation of the threshold formula. No correction needed. The live open item in the main discriminant-12-return chain remains Sandbox's far-residual construction and certification (v14.585 actions 3-4).
deliverable: none required from this auditor at this checkpoint.
constraints: no duplicate v14.354 or source/v14.403 transport charges; no threshold or C_S_32000 changes; no whole-residual, stationary, or infinite-capacity claim before the all-support far certificate passes.
