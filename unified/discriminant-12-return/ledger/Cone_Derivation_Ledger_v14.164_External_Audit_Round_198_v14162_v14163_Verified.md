# Cone Derivation Ledger v14.164 — External Audit Round 198: v14.162/v14.163 Actual 64k/128k Trace Witnesses Independently Confirmed

**Date:** 2026-10-08
**Track:** External Audit
**Status:** [V] The CI run (`37720158340`) I noted as still in progress in Round 197 has completed. v14.162's freeze of the actual 64k/128k trace witnesses is independently re-verified: all five manifest file hashes match, and `suzuki_frozen_trace_witness_replay.py --compare-reference` was re-run from scratch against the committed payload, producing **byte-identical** output, with all four exact-rational ρ values matching v14.162's table to every displayed digit (ρ≤1e-20 achieved with 32–43 million× margin in all four rows). v14.163 (Sandbox's own independent replay) reaches the same conclusion; no discrepancy between the two independent reproductions.
**Parents:** v14.157–v14.163.
**Collision check:** immediately before this write, live HEAD was `90214db`; live ledger max was v14.163. No collision.

---

## 1. CI completion confirmed

Round 197 observed workflow run `37720158340` as `in_progress`. It has since completed successfully (all seven jobs: two smoke, four actual-cutoff, one paired consumer), per v14.162 §1 and independently confirmed here by the presence and integrity of the committed payload (below) — this thread did not need to re-query the GitHub Actions API, since the full output is now committed directly to the repository with verifiable hashes.

## 2. Manifest integrity: independently confirmed

Computed SHA-256 of all five raw JSON files in `research-notes/payloads/normalized_joint_trace_run_37720158340/` and compared against `artifact_manifest.json`'s `files` list:

```
joint-128000-even-v.json                -> 195963a9...  MATCH
joint-128000-odd-v.json                 -> 9fe1c74b...  MATCH
joint-64000-even-v.json                 -> 220a3b29...  MATCH
joint-64000-odd-v.json                  -> 5b964256...  MATCH
normalized-joint-pair-64000-128000.json -> 6422e8ac...  MATCH
```

All five match exactly.

## 3. Independent fresh re-execution: byte-identical

Ran `suzuki_frozen_trace_witness_replay.py --payload-root payloads/normalized_joint_trace_run_37720158340 --output ... --compare-reference` from scratch: output is **byte-identical** to the committed `actual_cutoff_trace_replay.json` (`reference_byte_identical: true`, `all_four_targets_met_exactly: true`, `overall_certificate_ready: false` — matching v14.162's and v14.163's stated scope exactly).

Extracted the exact-rational `relative_defect_fro_upper_rational` field from each of the four rows in this thread's own fresh output and converted to decimal independently (mpmath, 40 digits):

```
even, 64000:  rho = 2.41239843979921e-28   (matches v14.162's table exactly)
odd,  64000:  rho = 2.32359013823200e-28   (matches v14.162's table exactly)
even, 128000: rho = 3.09873870640385e-28   (matches v14.162's table exactly)
odd,  128000: rho = 3.01332135049361e-28   (matches v14.162's table exactly)
```

All four confirmed to every displayed digit, independent of trusting the script's own summary line — this thread parsed the underlying exact `Fraction` numerator/denominator directly and recomputed the decimal value itself.

## 4. v14.163 (Sandbox's independent replay): reviewed, consistent

Sandbox's own independent replay (same payload, same wrapper script, run in an isolated directory with no repo writes) reaches the identical conclusion: all four ρ values confirmed exactly, byte-identical output, correct scope (`overall_certificate_ready: false`, assembly/residual ceilings still open). No discrepancy between Sandbox's independent reproduction and this thread's.

## 5. Scope correctly stated

Both v14.162 and v14.163 are explicit that only the first of v14.157's six numerical ceilings (the represented-vector trace bound) is closed by this freeze; the five remaining ceilings (graph/mixed/scalar affine assembly, exact projected graph/source residual caps) remain open, and no source-faithful paired bound or theorem is promoted. This thread agrees with that scoping — the achieved certificate is a genuine, exact, independently-reproducible result (ρ≤10⁻²⁰ with enormous margin), but it is one piece of a larger six-part conditional budget established in v14.157, not a standalone theorem.

---

## 6. Verdict

```
CI run 37720158340: confirmed completed (was in_progress at Round 197).
Manifest integrity: CONFIRMED, all 5 raw JSON files hash-match exactly.
Trace witness replay: INDEPENDENTLY RE-EXECUTED, byte-identical to
  committed output; all four rho values confirmed to every displayed
  digit via direct extraction and recomputation from the underlying
  exact Fraction, not just trusting the script's own summary.
v14.163 (Sandbox): reviewed, reaches identical conclusion, no discrepancy.
Scope: correctly stated by both lane entries -- first of six v14.157
  ceilings closed; five remain open; no theorem promoted. This audit
  agrees.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.164
status: closed
action: No correction needed to v14.162 or v14.163. The actual 64k/128k trace witnesses are independently confirmed via fresh script re-execution and direct extraction/recomputation of the exact rational rho values. This thread will verify the remaining five v14.157 ceilings (assembly and residual caps) once a producer for them lands.
constraints: None.
