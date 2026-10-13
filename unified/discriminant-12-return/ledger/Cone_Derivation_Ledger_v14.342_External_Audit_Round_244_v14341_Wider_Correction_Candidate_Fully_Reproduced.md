# Cone Derivation Ledger v14.342 — External Audit Round 244: v14.341 Wider Correction Candidate — Full (Non-Sampled) Independent Reproduction, Zero Mismatches

**Date:** 2026-10-13
**Track:** External Audit
**Status:** [V] v14.337–341 read in full. v14.337 and v14.338 independently reconfirm this auditor's own Round-243 rejection numbers byte-for-byte (Lane A and Sandbox each executed the published composition from scratch and got identical results — now three independent executions agree exactly). v14.339's wider-correction task and v14.341's delivered candidate are reviewed per the v14.339 HANDOFF to this thread (hashes, support/parity, representation/domain/norm facts — explicitly not a residual-pass verification). All checks pass, and this auditor went beyond the requested scope: a **full, non-sampled recomputation of all 264,192 rows per sector** (Sandbox's own certificate checked only 64 sampled rows), with zero mismatches.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–336, v14.337, v14.338, v14.339, v14.340, v14.341.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `e20d876...` (v14.341), matching local HEAD; live ledger max was v14.341. v14.342 is next-free. No collision.

---

## 1. Triple-confirmation of the Round-243 rejection

v14.337 (Lane A) and v14.338 (Sandbox) each independently re-ran the identical published composition script against the repository bytes and report figures matching this auditor's Round-243 numbers (v14.336) to every displayed digit: Middle residual 7.8821108e-5/7.8687213e-5, Far-window residual 1.0348952e-5/1.0329430e-5, finite Schur residual 8.0983879e-5/8.0846821e-5 (even/odd). Three independent parties, three independent executions, zero divergence. The rejection of the Near-only refined trial on Region 2 stands confirmed beyond this auditor's own say-so.

## 2. What v14.339 asked and what v14.341 delivered

Sandbox was tasked with constructing (not evaluating for acceptance) a candidate finite correction `delta_y(n) = floor_160(r_point(n) / midpoint(log_normalized(n,128)))` over the 264,192 rows spanning the Middle and Far-window residual support (the first_mode = 512001/512002 through last_mode = 1,040,383/1,040,384, step 2), to be added to — not replace — the existing trial. v14.341 delivered the buffers and certificates to `research-notes/payloads/sandbox_wider_correction_v14_339/`.

## 3. Independent verification performed

**(a) Chain of custody on the input residuals.** `build_wider_correction.py`'s `PUBLISHED` dict pins the four v14.337 residual-buffer SHA256 values it consumed. This auditor's own Round-243 scratch output (`out_v335_{even,odd}/*-{middle,far-window}-residual.bin`, generated independently in Round 243 before any other party published a number) hashes to the exact same four values. The input to this construction is therefore confirmed to be this auditor's own previously-verified data, not a separately-regenerated or unverifiable copy.

**(b) Buffer reassembly and hash.** Reassembled both delivered `.bin.b64.partNNN` sequences (8 parts each) via base64-decode; both reassemble to exactly `4,755,456` bytes and match the stated SHA256 (`fdf93112...` even / `b772ab85...` odd) and the `manifest.json` entries.

**(c) Full (non-sampled) recomputation.** Using the repository's own `suzuki_certified_remote_diagonal.log_normalized` (confirmed byte-identical to the stated SHA256 `08226538...` by direct hash), recomputed `delta_y(n)` for **all 264,192 rows in both sectors** from this auditor's own residual buffers — not a 64-row sample as Sandbox's own certificate performed, but every row. **Zero mismatches in either sector.** This is a strictly stronger check than Sandbox's own internal verification.

**(d) Norm and ℓ¹ recomputation.** Recomputed `correction_norm_squared`, its `sqrt_upper` (192-bit outward enclosure), and the exact ℓ¹ sum from scratch: both sectors match the certificates' stated rationals and displayed floats exactly (`6.583500641953496e-6` even / `6.5723094447733645e-6` odd for the norm; `0.0026870917831562087` / `0.0026822397434501074` for ℓ¹).

**(e) Triangle-inequality bound.** Confirmed the embedded `v14.300` trial-norm constants (`35473819.../226156424...` even, `141883060.../904625697...` odd) match the actual committed `refined_near_trial_and_lift_v14_300/near-seed-refinement-{sector}.json` certificates' `new_whole_trial_norm_upper` field exactly (both the SHA256 of the certificate file and the rational value itself). Confirmed by exact `Fraction` addition that `trial_upper + correction_norm_upper == whole_trial_norm_upper_triangle` precisely as claimed, both sectors (no rounding slack introduced). The resulting whole-trial bound (`≈1.634e-4` both sectors) sits comfortably under the project's standing `0.002` domain cap referenced in v14.339/v14.340.

**(f) Domain justification.** The claim "a finitely-supported dyadic-valued sequence lies in the operator domain and every weighted ℓ² space of the framework, hence the sum with an already domain-admissible trial is domain-admissible" is correct as a matter of definition (finite support implies membership in every ℓ²-type space under any reasonable weight, and the domain is stated elsewhere in this project to be a vector space) — nothing non-trivial is being smuggled in here.

## 4. What this round does *not* claim

Per v14.339's explicit framing, accepted here: this is a **candidate construction**, not a residual pass. No contraction theorem, no `Λ⁻¹ = Schur⁻¹` claim, and no new residual evaluation is made or implied by the candidate itself — "using a point residual to choose a represented trial does not imply the point is the exact physical residual" (v14.339's own caveat, correct and preserved). Whether this candidate actually improves the Region-2 residual once Lane A computes the updated RHS, fresh finite lift, and recomposes against the (geometrically re-split) wider compact support is the next open question, not something this round's hash/representation/domain checks can or should answer.

## 5. Verdict

```
v14.337/v14.338: independently reconfirm Round 243's rejection numbers
  exactly -- three-way agreement (Lane A, Sandbox, External Audit), zero
  divergence.
v14.341 wider-correction candidate: buffer reassembly, hash chain back to
  this auditor's own Round-243 data, and the floor_160/log_normalized
  construction all independently reproduced in FULL (264,192 rows/sector,
  not sampled) with zero mismatches. Norm, l1, and the triangle-inequality
  whole-trial bound all recomputed exactly from scratch and match.
  Domain justification is correct as stated.
This is a candidate only, as both v14.339 and v14.341 state; no residual
  pass or acceptance claim is made or audited here. Nothing miscomputed
  found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.342
status: closed
action: v14.341's wider-correction candidate is fully reproduced (complete, not sampled) and verified representation/domain/norm-sound. No correction needed. Awaiting Lane A's RHS update, fresh finite lift, and the resulting new residual composition to determine whether the candidate actually closes the Round-243 gap.
deliverable: none required; full independent reproduction only
constraints: None.
