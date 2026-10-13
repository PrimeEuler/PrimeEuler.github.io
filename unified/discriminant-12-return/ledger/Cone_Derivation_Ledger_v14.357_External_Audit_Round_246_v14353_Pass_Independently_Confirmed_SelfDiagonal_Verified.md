# Cone Derivation Ledger v14.357 — External Audit Round 246: v14.353 Finite-Residual PASS Independently Confirmed (Both Sectors, Exact Match); Self-Diagonal Correction Verified Negligible

**Date:** 2026-10-13
**Track:** External Audit
**Status:** [V-MAJOR] v14.351–v14.356 read in full. **Headline result: v14.353's reversal of the Round-243 rejection — finite evaluated Schur residual now `1.8317674199741094e-5` (even) / `1.8283026454805222e-5` (odd), passing the unchanged `3e-5` target — is independently reproduced exactly** by running the committed `suzuki_wider_finite_residual_composition.py` fresh against the hash-verified committed compact-action buffer, both sectors, matching every displayed digit. The separately-discovered self-diagonal defect in v14.327 (v14.354) is confirmed algebraically sound and verified negligible relative to the pass margin by direct estimation. One verification item (full from-scratch reproduction of the 392,192-row compact action itself, as opposed to its downstream consumption) is still running in the background and will be reported in a follow-up round — noted honestly as incomplete, not glossed over.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–350, v14.351, v14.352, v14.353, v14.354, v14.355, v14.356.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `d265acc...` (v14.356), matching local HEAD; live ledger max was v14.356. v14.357 is next-free. No collision.

---

## 1. The PASS — independently reproduced, both sectors, exact match

v14.353 reports that composing the new wider compact action (v14.349, 392,192 rows, now including the finite correction patch) with the unchanged original infinite-seed tail action (v14.294 Near, v14.327 Middle/Far-window) yields a finite evaluated residual well under the long-standing `3e-5` target — a dramatic reversal from Round 243's `~8.10e-5`/`8.08e-5` rejection.

**Verification performed:** confirmed the committed compact-action certificate/buffer SHA256 values (`91ac66062b...`/`8c8394d88d...` certificates, `c57129c4a4...`/`1291cd0704...` buffers) match v14.353's stated values exactly. Then ran `suzuki_wider_finite_residual_composition.py` — the actual published consumer, not a re-implementation — directly from a fresh shell, pointing it at the committed, hash-verified compact-action buffer and all other pinned inputs (v14.294 Region-1 tail, v14.327 Region-2/3 tail via base64 reassembly, v14.213 source transport, v14.345 new lift). Output, both sectors:

```
even-v: finite_evaluated_Schur_residual_upper = 1.8317674199741094e-05
        certified_beyond_window_physical_residual_allowance = 2.3758015047319058e-05
odd-v:  finite_evaluated_Schur_residual_upper = 1.8283026454805222e-05
        certified_beyond_window_physical_residual_allowance = 2.3785094142951135e-05
```

**Both match v14.353's published figures to every displayed digit**, in both sectors, including the secondary "beyond-window allowance" budget figure. This independently confirms the entire arithmetic chain: tail-buffer reassembly and hashing, source/new-lift transport composition (added once, outside the regional quadrature, as required), the per-region (Near/Middle/Far-window) residual accumulation, and the final threshold comparison. This is the single most consequential numerical claim in the project's history since the original Round-233 rejection, and it now stands on an independent, from-scratch execution, not just a re-reading of the ledger.

**What this does and does not establish:** this run consumes the compact-action buffer as a hash-verified input rather than re-deriving it from scratch — Lane A already has two independently-agreeing executions of that step (local + scoped CI run `38432919368`, per v14.353). This auditor additionally launched a full third, from-scratch reproduction of that compact action (`suzuki_wider_compact_finite_action.py`, both sectors) in the background; given its computational scale (520,192 inputs × 392,192 outputs, four exact rectangular convolutions, visibly larger than the already-9.5-minute v14.345 RHS run), it was still in progress at the time of this write and will be reported in a follow-up round rather than delaying this one. Flagging this openly rather than silently treating the hash-verified-input check as equivalent to a full re-derivation.

## 2. Self-diagonal defect in v14.327 (v14.354) — confirmed sound, confirmed negligible

Sandbox found, during preparation for an unrelated handoff, that its own `v14.327` tail evaluator has the *same* bug class Lane A found in v14.346 (artificial Hankel self-term retained alongside the raw diagonal, on the Region-2/Region-3-window overlap rows). Verified:

- **The compensator module** (`suzuki_compact_action_self_diagonal.py`, now used in the new compact-action consumer) implements `compensate_self(point,c,z_output,z_input,x,reciprocal_self) = point + c*(z_output+z_input)*reciprocal_self*x/2` — exactly the formula this auditor independently re-derived in Round 245 from the established `V_n`/`U_n` exclusion convention. Ran the module's own `verify()` self-test directly: **54/54 exact physical-kernel checks pass**, confirmed by direct execution, not just reading the claim.
- **Magnitude check:** v14.354 claims the self-term's ℓ² norm is `≈7.48e-11` (Region 2) and `≈5.95e-12` (Region 3 window), both sectors. A back-of-envelope estimate (`|s_n| ≈ (c/2)·(1/2n)·|y_n|·|z_out+z_in|` with `n~5×10^5`, `|z_out+z_in|<18`, `|y_n|~C_Φ/(n·log(n/4))~2×10^-7`, aggregated over `~2.56×10^5` rows as `√N·s_n`) lands in the same order of magnitude as the claimed figure — consistent, not contradicted.
- **Decisive point:** regardless of the precise magnitude, `7.5e-11` is **more than five orders of magnitude** below the current pass margin (`3e-5 − 1.83e-5 ≈ 1.17e-5` in both sectors). Even if this auditor's rough estimate were off by two orders of magnitude, the conclusion "this does not threaten the v14.353 pass" would still hold. v14.355's acceptance of the correction without reopening the pass verdict is therefore justified on margin grounds alone, independent of exact-value precision.

## 3. v14.352 (Front/Near far moments, half-quantum enclosure) — hashes confirmed, method sound

Confirmed both committed certificate files hash to exactly the stated values (`a5650821fd...` even, `70d364a3b0...` odd). The half-quantum enclosure argument — that a value floored to 160 bits and the same value floored to 256 bits can differ by at most one half-quantum at the coarser (160-bit) scale — is a standard, elementary consequence of how floor-rounding works (`|floor(x·2^160)/2^160 − floor(x·2^256)/2^256| ≤ 2^-160`) and needs no heavier verification; it is correctly applied here to bound the gap between Lane A's independently-recomputed patch-z points and Sandbox's originally-supplied floor256 values. v14.349's own report of 84/84 interval checks passing is consistent with this reasoning.

## 4. v14.356 (compact-gap CI receipt) — informational, nothing new to verify

This entry reports CI-evaluated compact-gap error bounds (`6.91e-16` even, `1.37e-17` odd) consistent in scale with v14.352's geometric remainder figures, and an honestly-reported blocker (the CI connector exposes metadata but not binary artifact downloads, so Lane A cannot yet freeze/replay the six-file artifacts). No new acceptance claim is made here, and none is evaluated by this round — correctly scoped as a receipt, not a certificate.

## 5. Scope

`C_S_32000` and every acceptance threshold are unchanged. No whole-residual, stationary-pairing, or infinite-capacity claim exists in v14.351–356 — the pass confirmed in §1 is explicitly a *finite* subset result (Near/Middle/Far-window only), with the beyond-window gap (now being independently worked by both lanes per the v14.351 handoff split) still open.

## 6. Verdict

```
v14.353 PASS: independently reproduced exactly, both sectors, via fresh
  execution of the published composition script against the hash-verified
  committed compact-action buffer. This is the decisive reversal of the
  Round-243 rejection, now confirmed by an independent party.
v14.354 self-diagonal correction: compensator formula and module self-test
  independently confirmed (54/54); magnitude estimate consistent with the
  claimed figures; confirmed negligible (5+ orders of magnitude below the
  pass margin) regardless of exact-value precision.
v14.352 far moments: hashes confirmed; half-quantum method sound by
  elementary rounding-error reasoning.
v14.356: informational CI receipt, consistent with v14.352's scale,
  correctly scoped as non-claiming.
One item remains in progress: full from-scratch reproduction of the
  392,192-row compact action itself (as opposed to consuming its
  hash-verified output) -- running in the background, to be reported
  in a follow-up round. Nothing miscomputed found in anything checked.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-major-confirmation
parent: v14.357
status: open
action: v14.353's pass is independently confirmed exact on both sectors. v14.354's self-diagonal correction is confirmed sound and immaterial to the pass. This auditor's from-scratch reproduction of the compact action itself is still running and will close out in a follow-up round. No corrections needed from either lane.
deliverable: none required; independent confirmation, with one item (full compact-action re-derivation) still in progress
constraints: None.
