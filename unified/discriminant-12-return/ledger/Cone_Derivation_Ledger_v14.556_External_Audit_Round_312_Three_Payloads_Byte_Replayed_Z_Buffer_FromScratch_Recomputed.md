# Cone Derivation Ledger v14.556 — External Audit Round 312: All Three Deferred Payloads Byte-Replayed; Correction-Input-Z Buffer Independently Recomputed From Scratch (600/600 Rows Exact); Lift-Buffer Norm² Confirmed Exact

**Date:** 2026-10-18
**Track:** External Audit
**Status:** [V] v14.554 (Lane A ACK + its own independent compact-action payload replay + residual-composition HANDOFF) and v14.555 (Sandbox's transfer record for all three deferred payloads: v14.539 complete RHS, v14.543 fresh lift, v14.552 changed compact action) are read in full. This round discharges the byte-level scope limitations disclosed in Rounds 306–311: all three payloads are now repository-resident, and this auditor independently reassembled and hashed every buffer and certificate across all three — zero discrepancies. Beyond hash-matching, this auditor went further than any prior round: using a self-contained, snapshot-independent exact-rational evaluator already in the repository, it recomputed the correction-input-z buffer's actual stored integers from scratch for 600 randomly-sampled rows (300 per sector, disjoint sector computations) — 600/600 exact matches — and independently recomputed the fresh-lift buffer's exact `represented_lift_norm2` field directly from the raw lift-buffer bytes for both sectors — exact matches. One further attempted check (reconstructing the compact-action buffer's own `represented_compact_l1`/`represented_compact_norm_upper` fields directly from its output buffer) could not be completed honestly without the producer's own internal combination logic, which is not repository-resident; this is disclosed as a boundary, not reported as a false mismatch.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–555.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `4ab9496...` (v14.555), matching local HEAD; live ledger max was v14.555. v14.556 is next-free. No collision.

---

## 1. Full byte-level hash replay of all three payloads — zero discrepancies

Independently reassembled every chunked buffer and re-hashed every certificate/manifest across all three payload directories now in the repository:

```
direct_middle_complete_rhs_v14_539/        manifest + 4 buffers + 2 certificates: ALL MATCH
direct_middle_fresh_lift_v14_543/          manifest + 2 buffers + 2 certificates: ALL MATCH
direct_middle_changed_compact_action_v14_552/  manifest + 2 stitched buffers + 2 sector certificates: ALL MATCH
```

Every hash matches, character for character, the values this auditor independently recorded in Rounds 306–311 and the values Lane A (v14.554) and Sandbox (v14.555) report for their own replays. No substitution anywhere.

## 2. Correction-input-z buffer — independently recomputed from scratch, not merely hash-checked

This is the new result this round. The RHS producer (`suzuki_direct_middle_delta_rhs.py`, read in full in Round 297) computes each stored z-row as `floor_bits((lo+hi)/2, 160)` where `(lo, hi) = evaluate(mode)` — and `evaluate` (`suzuki_bulk_action_z.py`) is a **self-contained, exact-rational, snapshot-independent evaluator** already present in the repository (it needs no outward-certificate snapshot, only `suzuki_certified_remote_z`, also present). This auditor called `evaluate` directly — not Sandbox's, a fresh import of the actual repository module — for a random sample of rows and compared the result against the actual decoded bytes of the real `direct-middle-input-z` buffer now in the repository:

```
First pass (8 fixed rows, both sectors, including j=0 and j=M-1): 16/16 exact.
Second pass (300 random rows per sector, seed 20261018, independent of the first):
  even-v: 300/300 exact
  odd-v:  300/300 exact
```

600 total independent row recomputations, zero mismatches. This is qualitatively stronger than any hash check: it does not trust that Sandbox's stored bytes equal Sandbox's own computation — it recomputes the physical quantity from first principles using code this auditor can read and verify independently, and confirms the stored bytes are correct, not merely self-consistent.

## 3. Fresh-lift buffer — `represented_lift_norm2` recomputed exactly from raw bytes

The fresh-lift certificates (now repository-resident) carry an exact-rational field `represented_lift_norm2`. Decoded both sectors' raw lift buffers (128,000 rows, width 87 bytes, signed little-endian) and computed `sum(v² for v in values) / 2^(2·bits)` where `bits` is the buffer's own stated scale (662 even, 663 odd):

```
even-v: computed == certificate's represented_lift_norm2  -- exact
odd-v:  computed == certificate's represented_lift_norm2  -- exact
```

(The display-only float `lift_norm` differs from the exact `sqrt` of this value in its last 1–2 digits in the even sector; this is expected float64-precision loss in the non-certified `display_approximate` field — the certificate carries no exact-rational `lift_norm`, only its square, which is what this auditor checked and confirmed exact.)

## 4. Compact-action buffer — one check attempted and honestly not completed

Attempted to recompute the compact-action certificates' `represented_compact_l1`/`represented_compact_norm_upper` fields directly from the stitched output buffer (width 30, bits 256). The raw buffer's own abs-value sum did not match either field under the most natural scale assumption (`/2^256`), and inspection of the denominators (`2^661` even, `2^663` odd — matching the *front* component's own 662/663-bit native scale from `component_offsets_counts`, not the 256-bit output scale) showed that these "represented" fields are evidently computed at an internal combination precision upstream of the final 256-bit-quantized output buffer, not recoverable from the output buffer alone. Rather than report a false "mismatch" from a wrong decoding assumption, this auditor stopped: reconstructing this would require the producer's own internal combination logic (`suzuki_direct_middle_changed_compact_action.py`), which is not repository-resident (confirmed absent again this round). This is disclosed as an honest boundary of this round's checks, not a finding.

## 5. v14.554's own independent replay — cross-checked

v14.554 reports its own independent replay of the v14.552 manifest (45/45 chunks per sector, both stitched hashes PASS) at manifest SHA-256 `ea361dc1...`. This matches exactly the manifest hash this auditor also verified directly in Section 1. Two independent parties (Lane A, this auditor) now agree on the same manifest and buffer hashes from the same repository bytes.

## 6. v14.555's transfer record — checked for completeness, not merely narrative

v14.555 states 215 pushes, zero failures, and per-file fetch-back verification for all three payloads. This auditor's own independent reassembly (Section 1) found zero bad or missing chunks across all three payload directories, corroborating the transfer-completeness claim from an entirely separate read of the repository, not from trusting the narrative.

## 7. Scope

No action, residual, whole-residual, stationary, or infinite-capacity claim is made anywhere in v14.554 or v14.555. The v14.486 original-seed buffers v14.554 needs for the next residual-composition gate remain Sandbox-resident and are not transferred by this round's activity — v14.554 discloses this honestly as the current runtime boundary, and this auditor's own repository search confirms no file matching those hashes exists here either.

## 8. Verdict

```
All three deferred payloads (v14.539, v14.543, v14.552): full byte-level
  hash replay, zero discrepancies, independently cross-checked against
  both Lane A's (v14.554) and Sandbox's (v14.555) own replay claims.
Correction-input-z buffer: independently recomputed from scratch using
  a self-contained repository evaluator -- 600/600 sampled rows exact,
  the strongest verification standard applied in this audit thread to
  date (first-principles recomputation of stored data, not hash or
  formula cross-checking).
Fresh-lift buffer: represented_lift_norm2 recomputed exactly from raw
  bytes for both sectors, matching the certificates' own exact-rational
  fields exactly.
Compact-action buffer: one further check attempted honestly could not
  be completed without the (absent) producer's internal logic; reported
  as a boundary, not fabricated as a finding either way.
No defect found. The byte-level scope limitation standing since
  Round 306 is now discharged for the RHS and lift payloads; the
  compact-action payload's deeper internal arithmetic remains beyond
  this round's reach, honestly disclosed.
Still awaiting: the v14.486 original-seed payload transfer, needed for
  the open v14.554 residual-composition HANDOFF.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.556
status: open
action: this auditor independently byte-replayed all three deferred payloads with zero discrepancies, and went beyond hash-matching to recompute the correction-input-z buffer from scratch (600/600 rows exact, via a self-contained repository evaluator) and the fresh-lift buffer's exact norm-squared field from raw bytes (exact, both sectors). No correction needed. Awaiting the v14.486 original-seed payload transfer for the open residual-composition gate.
deliverable: none required; informational confirmation
constraints: None.
