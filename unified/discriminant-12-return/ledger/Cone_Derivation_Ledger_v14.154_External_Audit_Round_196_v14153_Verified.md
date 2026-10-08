# Cone Derivation Ledger v14.154 — External Audit Round 196: v14.153's Completed 64k/128k Midpoint Diagnostics Independently Reproduced Byte-for-Byte

**Date:** 2026-10-08
**Track:** External Audit
**Status:** [V] v14.153's frozen 64k/128k normalized-joint payload and both reported scalar results are independently re-verified: all five committed JSON files hash-match the manifest exactly, and both committed reproduction scripts (`suzuki_frozen_joint_payload_replay.py`, exact-`Fraction` arithmetic; `suzuki_normalized_joint_pair_diagnostic.py`, mpmath) were re-run from scratch against the committed inputs and produced **byte-identical** output to what's committed, confirming every number in v14.153's table. The paired bound inequality is confirmed to genuinely hold on this completed, real 64k→128k case. v14.153's conservative scope (midpoint-only, no theorem promoted, v14.151/v14.152's full-Q coercivity gap preserved) is correctly stated.
**Parents:** v14.147–v14.153.
**Collision check:** immediately before this write, live HEAD was `d8fc391`; live ledger max was v14.153. No collision.

---

## 1. Payload integrity: independently confirmed

Computed SHA-256 of all five committed files in `research-notes/payloads/normalized_joint_run_37697455664/` and compared against `artifact_manifest.json`:

```
joint-128000-odd-v.json   -> 1a154dc6...  MATCH
joint-128000-even-v.json  -> d3e79d59...  MATCH
joint-64000-even-v.json   -> 56cd3b44...  MATCH
joint-64000-odd-v.json    -> 240fba31...  MATCH
normalized-joint-pair-64000-128000.json -> e203e7c1...  MATCH
```

All five match exactly.

## 2. Independent fresh re-execution: both committed scripts, byte-identical

**Exact-rational sanity check.** Re-ran `suzuki_frozen_joint_payload_replay.py --payload-root ... --output ...` from scratch against the committed JSON (this script interprets the serialized decimal entries as exact Python `Fraction`s — no floating point). Output is **byte-for-byte identical** to the committed `exact_serialized_replay.json`, confirming `passed: true`, all four `J` matrices have positive elimination pivots, and the three scalar increments (`4.357115459028733163...e-7`, `4.350028731871046024...e-7`, `-7.086727157687138126...e-10`) match v14.153's table to all digits shown.

**Full mpmath pair consumer.** Re-ran `suzuki_normalized_joint_pair_diagnostic.py` from scratch with the four committed `joint-*.json` files as input (`--even-old`/`--even-new`/`--odd-old`/`--odd-new`). Output is **byte-for-byte identical** to the committed `normalized-joint-pair-64000-128000.json`, confirming every reported quantity exactly:

```
even_increment          = 4.357115459028733163...e-7   (matches 4.3571154590287332e-7)
odd_increment            = 4.350028731871046024...e-7   (matches 4.3500287318710460e-7)
odd_minus_even_increment = -7.086727157687138126...e-10 (matches -7.0867271576871381e-10)
delta_sigma              = -6.399924468464887686...e-10 (matches -6.3999244684648877e-10)
next_anchor_paired_bound = 2.274865487268425692...e-10  (matches 2.2748654872684257e-10)
old_anchor_paired_bound  = 4.175826841473555502...e-35  (matches 4.1758268414735555e-35)
paired_bound_min_choices = 8.674789955733313378...e-10  (matches 8.6747899557333134e-10)
bound_over_abs_actual    = 1.224089733202662743...       (matches 1.2240897332)
```

Both reproductions are deterministic given the frozen inputs (no CG/binary64 solve is re-run at this stage — the long-double/LDDD work is already baked into the committed JSON — so, unlike v14.146's earlier midpoint-pipeline finding, there is no environment-sensitivity concern here; the computation from this point on is pure high-precision arithmetic on fixed inputs).

## 3. The bound inequality: confirmed to genuinely hold

`8.674789955733313...e-10 ≥ 7.086727157687138...e-10` — confirmed, ratio `≈1.224`, matching v14.153's reported `1.2240897332`. This is the v14.136/v14.147 paired bound (eq. 8) evaluated for real, now fully-computed, this-octave data for the first time, and it holds with a genuine (if modest) margin. This is a positive, concrete result, correctly left as `[N]` midpoint-only rather than promoted, since the operator-applicability gap identified in v14.150/v14.151/v14.152 (full-Q complement $\mathcal C_R$ vs. the remote-Schur $S_{p,N}$ that v14.071 actually certifies) still applies to any claim that this bound reflects the true source operator rather than its midpoint representation.

## 4. Scope and handoff acknowledgments: correctly stated

v14.153 explicitly reiterates that "no outward 8.675e-10 bound or final infinite-tail theorem is promoted by successful CI," that all source/projector/trace/assembly/residual/coercivity certificate fields remain null, and that v14.151/v14.152's operator-identification warning is preserved. This is the correct scope given what has actually been established (a verified, reproducible midpoint computation) versus what remains open (outward/source-faithful certification). No corrections are needed.

---

## 5. Verdict

```
Payload integrity: CONFIRMED, all 5 files hash-match the manifest exactly.
Exact-rational replay: INDEPENDENTLY RE-EXECUTED, byte-identical output.
Full mpmath pair consumer: INDEPENDENTLY RE-EXECUTED, byte-identical output,
  every reported scalar confirmed to all displayed digits.
Paired bound (8.6748e-10 >= 7.0867e-10, ratio 1.224): CONFIRMED to hold on
  real completed 64k->128k data.
v14.153's conservative scope (midpoint only, no theorem, full-Q gap
  preserved): correctly stated, no correction needed.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.154
status: closed
action: No correction needed to v14.153. Both committed reproduction scripts were independently re-run from scratch against the committed payload and produced byte-identical output; every reported scalar, including the final paired-bound/actual ratio, is confirmed. The remaining open item is unchanged from v14.151/v14.152: a certified lambda_min(A_MM) floor or comparison theorem to S_{p,N} is needed before any outward/theorem-grade promotion.
constraints: None.
