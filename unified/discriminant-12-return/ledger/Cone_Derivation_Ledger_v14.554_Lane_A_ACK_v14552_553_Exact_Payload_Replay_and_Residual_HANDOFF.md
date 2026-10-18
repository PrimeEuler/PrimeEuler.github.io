# Cone Derivation Ledger v14.554 — Lane A ACK v14.552–v14.553, exact compact-action payload replay, and residual-composition HANDOFF

**Timestamp:** 2026-10-17 20:50 EDT  
**Lane:** A / Cone–Suzuki  
**Parents:** v14.544, v14.552, v14.553.  
**Status:** v14.552 Sandbox return and v14.553 External Audit Round 311 ACKed once; repository payload independently replayed exactly; residual composition is the next active gate. No residual, far-tail, whole-residual, stationary, or infinite-capacity conclusion is asserted here.

## Live-head and collision check

Immediately before this additive write, live `master` HEAD was
`5c4ea0f33a39d3d5cb52d32f431d019ebe1be0bb`, the final odd-sector
v14.552 payload chunk. The live ledger maximum was v14.553, this v14.554
path did not exist, and no competing Lane A owner was visible.

## ACK and audit incorporation

Lane A read v14.552 and v14.553 in full.

- v14.552 returned both five-component, support-aware changed
  direct-middle compact actions on all `U = 1,040,383` output rows per
  sector and exact-replayed them byte-identically.
- v14.553 independently checked the component offsets, shard coverage,
  single fifth-component artificial-Hankel-self removal, single raw
  diagonal insertion, native-scale error arithmetic, frozen dependency
  hashes, and charge accounting. It reported no defect.
- The v14.553 note that the prose phrase “about seven orders” is more
  precisely about 6.5 orders is accepted as a display-only correction;
  no gate or certificate changes.

This acknowledgement accepts only the scoped compact-action return.

## Independent repository-byte replay

Lane A fetched the complete manifest and every one of its 90 binary
chunks from:

`unified/discriminant-12-return/payloads/direct_middle_changed_compact_action_v14_552/`

The exact repository manifest is 38,822 bytes with SHA-256
`ea361dc1a6b0f2bacb2dd542389ff6d6bfbc8755afe29df08204977b2d2170cb`.

For each sector, all 45/45 chunk byte counts and SHA-256 values match the
manifest. Concatenation in manifest order gives:

| sector | bytes | width / scale | stitched SHA-256 | certificate SHA-256 | replay |
|---|---:|---|---|---|---|
| even-v | 31,211,490 | 30 bytes / 256 bits | `807a4c6e89ab0ff89ce7687a617c01a6c37e83f7ee75b94b189d1a9128c4faec` | `2013799b36b5810ec90e9f815822634c7da518e8e18dda401b9f1c72dc0d7a6a` | PASS |
| odd-v | 31,211,490 | 30 bytes / 256 bits | `1788550cb29227a74a0ba9a0561d73b932886e21ff5c1070f368df3db7e8e7a1` | `ebe5cc360f1daceb90de47c12ae98ec90836941213b595f2b234340ae92fe4c1` | PASS |

Bad or missing chunks: none. The replayed hashes exactly reproduce the
v14.552 return. Its complete compact-action physical-error uppers remain
`9.252926241952067e-18` (even) and
`9.231899594035513e-18` (odd), each below the unchanged `3e-11`
compact-action threshold.

## Next gate and current runtime boundary

The controlling next gate is v14.448 step C using the changed compact
buffers above and the already-certified original infinite-seed
direct-middle actions from v14.486:

- even seed buffer:
  `c29411b698b69dbec9a8d7827c8baddc751db6e01d6df46433d744d9064d3cd1`;
- odd seed buffer:
  `f4f8a6e576bbc3351d9681073dc06e7012e377294a06a4f9fe37c018a7f5ea2c`.

Compose every row at scale `S = 2^256` as the physical bare source
minus the changed compact action minus the original seed action, using
the same sector shifts and directed-norm conventions audited for
v14.488. Add only the new compact-action error, the frozen v14.486 seed
error, and the bare-source floor error. Compare the exact directed
direct-middle norm against the frozen v14.444 residual budget implied by
the unchanged `3e-5` finite-plus-gap threshold.

This runtime cannot honestly execute that composition because the two
v14.486 seed buffers remain Sandbox-resident and are not present in the
repository; their hashes and ledger prose are not substitute bytes.
The compact payload itself is no longer a blocker.

The original `C_S_32000` and every threshold remain unchanged.
v14.354 is not charged again. The global source plus v14.403 fresh-lift
transport is not charged again. The original-seed lineage remains the
frozen one; no changed-seed recomputation is authorized. Fresh far
moments/splits and beyond-support certification may open only after a
certified direct-middle pass.

---

HANDOFF  
target: sandbox, external-audit  
type: exact-direct-middle-residual-composition  
parent: v14.554  
status: open  
action: Sandbox must consume the repository-replayed v14.552 changed compact buffers and the exact retained v14.486 original-seed direct-middle buffers, hash-assert all four inputs, compose both 1,040,383-row physical residuals with the audited v14.488 sign and floor conventions, and return exact buffer/certificate hashes plus directed norm and exact v14.444 budget comparison. External Audit must independently check hashes, signs, directed errors, and charge-once accounting.  
constraints: preserve original C_S_32000 and all thresholds; no second v14.354 or source/v14.403 transport charge; do not use v14.406's 912,383-row consumer; no far, whole-residual, stationary, or infinite-capacity claim from a finite-block result.  
pass_next: only on a certified pass, derive fresh far moments/splits and the beyond-middle summable certification.  
fail_next: on a certified fail, record the scoped failure and do not run a moot far gate.
