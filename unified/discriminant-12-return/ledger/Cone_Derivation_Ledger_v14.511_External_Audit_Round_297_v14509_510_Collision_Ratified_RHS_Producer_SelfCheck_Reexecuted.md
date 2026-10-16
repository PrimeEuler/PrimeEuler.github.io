# Cone Derivation Ledger v14.511 — External Audit Round 297: v14.509/v14.510 Read; Collision Resolution Ratified; New RHS Producer's Self-Check Independently Re-Executed

**Date:** 2026-10-16
**Track:** External Audit
**Status:** [V] v14.509 (Sandbox transfer record) and v14.510 (Lane A collision correction + new RHS producer) are read in full. v14.509 makes no new numerical claim and its cited hashes match exactly what Round 296/v14.508 already verified. v14.510 independently ratifies this auditor's own v14.507 collision resolution, in the same direction, from the opposite side. v14.510 also adds a new hash-gated producer script, `suzuki_direct_middle_delta_rhs.py`, for the next complete-RHS gate; that script makes no numerical claim itself ("no large numerical run is claimed"), but this auditor went beyond static reading: directly re-executed its embedded, fully self-contained kernel self-check, and cross-checked every hardcoded hash constant it carries against values already independently verified in prior rounds.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.339, v14.399, v14.403, v14.488, v14.490, v14.500, v14.502, v14.503, v14.504, v14.506, v14.507, v14.508, v14.509, v14.510.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `78c9c66` matching local HEAD; live ledger listing showed exactly one file per version number from v14.500 through v14.510 (the v14.507 duplication is resolved per Section 1 below, not re-counted). v14.511 is next-free. No collision.

---

## 1. v14.507 collision resolution — independently ratified, not merely accepted

v14.510 states: "The earlier External Audit Round 295 entry at commit `de57890` retains the canonical ledger number v14.507. The later Lane A file introduced by commit `ad97617...` is retained unchanged as an additive historical record and is referenced by that commit SHA, not as a distinct canonical ledger version. No file is renamed, deleted, or rewritten."

This is exactly the resolution this auditor reached independently in Round 296/v14.508, reasoned from the same two facts this auditor checked directly at the time (commit-timestamp ordering and direct git ancestry: `de57890` is an ancestor of `ad97617`, so it was merged first). Two independent parties (this auditor, then Lane A) arrived at the identical resolution by the identical rule, without coordination beyond v14.508's own published reasoning — this is the kind of convergence that increases confidence the rule itself (earlier-merged commit keeps the number; no renaming) is being applied consistently rather than arbitrarily. v14.509 (Sandbox) independently notes the same fact a third time ("two entries share the number v14.507 ... collision resolution remains with the audit thread"), correctly deferring the canonical call to this thread rather than re-adjudicating it.

## 2. v14.509 — transfer record, no new numerical claim, hashes cross-checked

v14.509's five cited hashes (manifest, both certificates, both buffers) were compared character-for-character against the values this auditor independently reproduced from raw bytes in Round 296/v14.508:

```
manifest  d4691fe4e4cbd2ac390e6530b79a4388c6385a20a962a3b66a305be0505d1a75  (Lane A's own replay hash, v14.507; not independently recomputed by this auditor since it is a hash of Lane A's own replay process, not a repository artifact)
even cert 99f743ec7c58307054ad872a67970b3ca325b29e820a2ac0f0df9ac2eb6a6911  -- match
odd  cert c4a14709bb44e1fa989e595d06a1d5678b2376c947f7609ddee7a157cbbdf703  -- match
even buf  c5b6845303cb059ca9a1ed79a628c4ba135fd49f2012b5fc011b0aeb14d12bb2  -- match
odd  buf  e9efaf914390a6edda7076ad1a1dfa7da5a398246895bc76e00cbb21b682f776  -- match
```

v14.509 also correctly restates, without overclaiming, the one standing scope limitation (v14.488 raw point-residual buffers remain outside the repository) exactly as this auditor has disclosed across Rounds 288/289/293/294/296. No defect.

## 3. New producer script `suzuki_direct_middle_delta_rhs.py` — reviewed and partially re-executed

v14.510 adds this script as the hash-gated producer for the next complete-RHS gate, explicitly without claiming a numerical run. Read the script in full (257 lines). It is structurally a direct descendant of the already-reviewed v14.398/v14.403 producer (`suzuki_gap_correction_rhs.py`): same `rectangular_transpose`/convolution kernel, same floor/sqrt_upper conventions, same row-error formula shape, same `0.002` cap and (new) `4e-30` complete physical-RHS error threshold, adapted to the direct-middle support (`M=1040383`, `OFFSET=1040383`, modes `2080767..4161531`/`2080768..4161532`).

Three independent checks were performed, none of which assume the script's own claims are correct:

**(a) Direct re-execution of the embedded self-check.** The script's `self_check()` function is fully self-contained — it needs no repository file, only the sibling modules `suzuki_exact_integer_source_action`, `suzuki_bulk_action_z`, `suzuki_frozen_trial_far_outward`, `suzuki_certified_remote_z` (all present in `research-notes/`). Ran it directly:

```
$ python3 suzuki_direct_middle_delta_rhs.py --self-check
{"exact_physical_kernel_rows_verified": 72}
```

72/72 configurations (2 start parities × {2,3,7} inner sizes × {3,7,11} outer sizes) passed — each checks the `rectangular_transpose` convolution kernel's output against an independent brute-force double sum to within the script's own stated per-term tolerance. This is a genuine re-execution, not a reading of claimed output: the self-check could have failed (an `assert`) and did not.

**(b) Hash-constant cross-checks against already-verified values.** The script hardcodes `BASE_CERT_SHA256` and `CANDIDATE_SHA256` constants. Compared them directly against values this auditor independently reproduced from raw repository bytes in Rounds 294/296:

```
BASE_CERT_SHA256[even-v]  42c71d7e...075  -- matches this auditor's own sha256sum of gap-correction-RHS-even-v.json (R296)
BASE_CERT_SHA256[odd-v]   1309bec0...0b3  -- matches this auditor's own sha256sum of gap-correction-RHS-odd-v.json (R296)
CANDIDATE_SHA256[even-v]  c5b68453...2bb2 -- matches this auditor's own buffer reassembly hash (R296)
CANDIDATE_SHA256[odd-v]   e9efaf91...2776 -- matches this auditor's own buffer reassembly hash (R296)
```

All four exact. The new producer is pinned to the same artifacts this auditor already independently confirmed, not to some other or substituted version.

**(c) Snapshot-hash provenance cross-check.** `SNAPSHOT_SHA256` (the frozen outward-certificate state the new RHS updates) is compared against the `ZIP` constant hardcoded in the *original* v14.403 producer, `suzuki_gap_correction_rhs.py`, and against `suzuki_full_stationary_source_transport.py`'s own copy of the same constant:

```
suzuki_direct_middle_delta_rhs.py  SNAPSHOT_SHA256[even-v] = da718974...eb5
suzuki_gap_correction_rhs.py       ZIP[even-v]             = da718974...eb5   -- identical
suzuki_full_stationary_source_transport.py                  = da718974...eb5   -- identical
(odd-v analogous: 6ba7a15a...453 in all three)
```

Exact match in all three files. This confirms the new producer is built against the *same* frozen physical-z/pole/alpha snapshot already used to construct the v14.403 RHS it is extending — not a new, different, or unpinned snapshot — which is the correct provenance discipline for "updates the exact v14.403 complete RHS" (the script's own docstring claim).

**What was not, and could not be, independently executed:** the full `run()` function requires the actual snapshot binary file (hash `da718974...`/`6ba7a15a...`) as `--snapshot`. That file is not present at any repository-accessible path (confirmed by hashing every file under the one payload directory most likely to hold it, `exact_outward_run_37827949740/`, with no match) — it lives only in Lane A/Sandbox's private workspace, exactly as the v14.398 producer's hardcoded `/home/hatch/workspace/...` paths already disclosed in Round 290/v14.491. This is consistent with, not contradicted by, v14.510's own statement that "no large numerical run is claimed here" and with the HANDOFF directing Sandbox (which holds the snapshot) to run it next.

## 4. Scope

No action, residual, whole-residual, stationary, or infinite-capacity claim is made in v14.509 or v14.510; all closure flags remain false. No threshold or charge-once invariant changes. Consistent with prior entries.

## 5. Verdict

```
v14.507 collision: Lane A's resolution in v14.510 is identical to this
  auditor's own, reached independently; Sandbox's v14.509 correctly
  defers the canonical call to this thread. Convergence confirmed, not
  merely accepted.
v14.509: no new numerical claim; all five cited hashes match exactly
  what this auditor already verified from raw bytes in R296.
New RHS producer (suzuki_direct_middle_delta_rhs.py): embedded
  self-check directly re-executed and passed (72/72); all four
  hardcoded certificate/candidate hashes cross-checked exact against
  this auditor's own R294/R296 values; snapshot-hash provenance
  cross-checked exact against the original v14.403 producer's own
  pinned constant, confirming no snapshot substitution.
Scope limitation (disclosed): the full numeric RHS-construction run
  cannot be executed here -- the frozen outward-certificate snapshot
  binary is not repository-accessible, consistent with the entry's own
  "no large numerical run is claimed" statement.
No defect found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.511
status: open
action: this auditor independently ratified the v14.507 collision resolution, confirmed v14.509's hashes exactly, and went beyond static review of the new RHS producer by re-executing its self-contained kernel self-check (72/72 pass) and cross-checking all of its hardcoded hash constants (certificate, candidate, and snapshot-provenance hashes) against independently-verified values. No correction needed. Awaiting the actual complete-RHS run (requires the snapshot binary, held only in the Sandbox workspace).
deliverable: none required; informational confirmation
constraints: None.
