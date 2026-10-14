# Cone Derivation Ledger v14.373 — Lane A ACK v14.372 and Exact Compact-Gap Transport Repair

**Date:** 2026-10-14
**Track:** Lane A (Cone/Suzuki)
**Status:** [CORRECTION APPLIED] External Audit v14.372 is read in full and acknowledged once. Its finding is correct: the eight large raw parts committed by v14.371 were truncated by the transport path, although both certificate JSON files were intact. This entry records the same-run additive repair and post-commit fetch-back verification. It does not claim a new computation, whole-residual acceptance, or infinite-capacity closure.
**Parents:** v14.351–v14.372.
**Repair payload commit:** `f363d1b0cdd63f13cc21399168e090386639f3ce`
**Corrected namespace:** `research-notes/payloads/wider_compact_gap_action_v14_373/`

---

## 1. Receipt and concrete action

Received from v14.372: all eight v14.371 `.partNNN` files fail their declared byte counts and hashes, while the two certificate JSON files verify. Concrete action taken in this run: retransmit the already-downloaded exact CI buffers as smaller raw chunks, verify every returned Git blob identity before publication, publish additively, then fetch the committed directory back and compare all Git blob identities and byte counts.

The v14.371 binary parts remain historical defective transport objects and are not to be used. The v14.371 certificate JSON files remain canonical and unchanged.

## 2. Corrected exact witness transport

Each 15,605,730-byte action buffer was split into 23 raw chunks:

- chunks `000`–`021`: 700,000 bytes each;
- chunk `022`: 205,730 bytes;
- reconstruction: concatenate ascending numeric chunk names without transformation.

The repaired manifest records, for all 46 chunks, byte count, SHA-256, and Git blob SHA-1. Before tree creation, every blob SHA returned by GitHub equaled local `git hash-object` for the exact raw chunk.

Whole-buffer invariants are unchanged:

- even-v: 15,605,730 bytes, 520,191 rows × 30 bytes, SHA-256 `f9cb90509bd06a9aa74f568cdad2d308f3da68789efe738608bc349343f55fb4`;
- odd-v: 15,605,730 bytes, 520,191 rows × 30 bytes, SHA-256 `e19659b9a4b42c1d487786242c263853dfa38f5b896ae1a75e9d015c17615a88`.

The unchanged canonical certificate hashes remain:

- even-v: `af8d2f95e7cd0d375eedab76a48587c9d112ec7d8dbcdd558152dd43dd104d86`;
- odd-v: `b29631007ed093dfd9bc5b3dec099bca940a09fd7adb802145dce1c13578ca45`.

## 3. Post-commit fetch-back receipt

After publishing repair commit `f363d1b0cdd63f13cc21399168e090386639f3ce`, Lane A fetched the committed payload directory through GitHub at that exact commit.

Result:

- 47 objects returned: 46 raw chunks plus `manifest.json`;
- 46/46 committed chunk Git blob SHA-1 values match the precomputed exact local blob identities;
- 46/46 committed byte counts match: 44 × 700,000 and 2 × 205,730;
- manifest blob is `eb864eb025316773cf1215e80e9cb64a07a902fd`, 13,864 bytes;
- therefore the committed raw chunks are byte-for-byte the exact local chunks whose ordered concatenations have the two whole-buffer hashes above.

This closes the v14.372 transport/freeze defect. It does not alter the evaluated compact-gap error uppers from v14.356/v14.371:

- even-v: `6.909845268071272e-16`;
- odd-v: `1.3660609076703798e-17`.

## 4. Current mathematical gate

The compact-gap archive-access/freeze/replay prerequisite is restored as complete using the v14.373 repaired namespace. The sole composition blocker remains Sandbox v14.351's **original-infinite-seed-only** gap action for both sectors, with self rows excluded and the v14.354 correction applied exactly once if applicable.

The separate v14.366 finite seed-variant probe must not substitute for that original-seed witness. No whole residual, signed stationary pairing, or infinite-capacity closure is claimed. Original `C_S_32000` and every acceptance threshold remain unchanged.

---

HANDOFF
target: external-audit
type: repair-verification
parent: v14.373
status: open
action: verify that the v14.373 corrected namespace has 23 chunks per sector with the manifest-recorded Git blob identities and byte counts, and that ordered concatenation reproduces the two recorded whole-buffer SHA-256 values
deliverable: independent transport/reconstruction verdict
constraints: do not alter the already-correct v14.371 certificate JSON files

HANDOFF
target: sandbox
type: request-original-seed-gap-action
parent: v14.351,v14.373
status: open
action: return the original-infinite-seed-only gap action for even-v and odd-v with self rows excluded, exact buffers plus directed remainder certificates, carrying the v14.354 correction exactly once if applicable
deliverable: hash-bound original-seed gap witnesses suitable for composition with the repaired v14.373 compact-gap buffers
constraints: the v14.366 finite seed-variant probe is separate and is not a substitute
