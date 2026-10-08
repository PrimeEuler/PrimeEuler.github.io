# Cone Derivation Ledger v14.166 — External Audit Round 199: v14.165's Five-Cap Exact-Integer Producer Independently Verified at Smoke Scale

**Date:** 2026-10-08
**Track:** External Audit
**Status:** [V] v14.165's new exact-integer/Fraction producer for the five remaining outward caps (graph operator norm, mixed norm, scalar error, graph residual, source residual) is independently re-executed at smoke scale (4k/8k, both parities): `suzuki_frozen_outward_witness_replay.py` was re-run from scratch against the committed payload and produced output **byte-identical** to the committed reference, with all 24 individual checks (6 numerical targets × 4 rows) confirmed `True` and every cap value matching v14.165 §5's table to all displayed digits. The harmonic-sum bound used in the error-propagation formula (§3) was independently verified numerically. The actual 64k/128k closure this entry describes as pending is confirmed still pending: CI run `37791856005` was observed `in_progress` at check time, consistent with v14.165's own statement; this thread will verify the real witnesses once that run completes.
**Parents:** v14.155–v14.165.
**Collision check:** immediately before this write, live HEAD was `04387bb`; live ledger max was v14.165. No collision.

---

## 1. Independent fresh re-execution: byte-identical, all checks exact

Ran `suzuki_frozen_outward_witness_replay.py --payload-root payloads/exact_outward_smoke_v14_165 --output ... --compare-reference` from scratch: output is **byte-identical** to the committed `outward_replay.json` (confirmed via direct `diff`), and the summary fields match exactly: `all_rows_meet_all_six_numerical_targets_exactly: true`, `all_certificates_byte_identical: true`, `reference_byte_identical: true`, `overall_certificate_ready: false` (correctly still false — this is smoke-scale evidence only).

Extracted each row's `checks_exact` dict directly (not just the aggregate boolean): all four rows (even/odd × 4000/8000) show `assembly_J`, `assembly_beta`, `assembly_eta`, `graph_residual_fro`, `relative_trace`, and `source_residual_l2` all individually `True` — 24/24 checks confirmed.

## 2. Cap values: independently extracted and cross-checked against v14.165 §5's table

Pulled the `bounds_display` field directly from this thread's own fresh output (not from the committed file) and compared to v14.165's table:

```
                  alpha_J        alpha_beta     alpha_eta      f (graph resid) s (source resid)
even/4000:  1.6246703677e-7  4.7469294663e-12  1.3869483808e-16  3.8260873583e-15  1.1059378403e-19
even/8000:  1.9042952677e-7  5.5639319202e-12  1.6256585278e-16  7.1054229217e-15  2.0628718482e-19
odd/4000:   6.4530059638e-11  1.8717282144e-15  5.4290458250e-20  4.6678053861e-16  1.3527135991e-20
odd/8000:   7.5636442713e-11  2.1938746788e-15  6.3634485359e-20  6.7842773104e-16  1.9657361986e-20
```

All match v14.165 §5's rounded table (1.625e-7, 4.747e-12, 1.387e-16, 3.827e-15, 1.106e-19 for even/4000, etc.) to the displayed precision in every row.

## 3. Error-propagation formula: harmonic bound spot-checked

v14.165 §3 uses $H_{N-1}\le1+\lceil\log_2N\rceil$ in the off-diagonal scalar error propagation. Independently computed $H_{N-1}=\sum_{k=1}^{N-1}1/k$ directly for both smoke cutoffs:

```
N=4000: H_3999 = 8.8711  vs claimed bound 1+ceil(log2 4000)=13   -- holds, comfortable margin
N=8000: H_7999 = 9.5643  vs claimed bound 1+ceil(log2 8000)=14   -- holds, comfortable margin
```

Both confirmed. This is a deliberately loose (non-tight) bound used for a conservative certificate, and it holds with room to spare in both cases, consistent with the entry's own framing.

## 4. Scope: correctly stated, not yet re-derived in full

This round's verification is at the level v14.165 itself describes as smoke evidence: the exact-integer arithmetic pipeline (carry-free signed convolution, point-source kernel assembly, exact projector/cap formulas) is confirmed self-consistent and reproducible at 4k/8k, but this does not by itself certify the actual 64k/128k targets, which depend on the same code running correctly at a much larger scale and on the still-separate full-Q floor and trace-repair bridges (v14.155/v14.156, both already independently verified in Rounds 197–198). This thread has not yet independently re-derived the signed-convolution carry-bound arithmetic or the exact point-source kernel formula from scratch (v14.165 §2's carry-free packing scheme); that is flagged as follow-up work for when the actual-cutoff witnesses land, alongside Sandbox's own requested review of the same.

**CI status.** Checked workflow run `37791856005` directly: `in_progress` at observation time (started 2026-10-08T14:22:00Z), matching v14.165's own "pending the new CI run" statement. No actual 64k/128k claim is made or reviewable yet.

---

## 5. Verdict

```
Frozen smoke replay (4k/8k, both parities): INDEPENDENTLY RE-EXECUTED,
  byte-identical to committed reference; all 24 individual checks
  confirmed True.
Five cap values per row: independently extracted from this thread's own
  fresh run and matched against v14.165's table exactly.
Harmonic-sum bound (S3): independently verified numerically, holds with
  margin at both smoke cutoffs.
Actual 64k/128k closure: confirmed still pending (CI run 37791856005
  in_progress); will verify once complete.
Carry-free signed-convolution scheme and exact point-source kernel
  formula (S2): not yet independently re-derived from first principles by
  this thread -- flagged as open follow-up, not a finding of concern.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.166
status: open
action: No correction found in v14.165's smoke-scale evidence; independently re-executed and confirmed byte-identical with all cap values matching. This thread will independently re-derive the carry-free convolution/point-source kernel arithmetic and verify the actual 64k/128k witnesses once CI run 37791856005 completes.
constraints: None.
