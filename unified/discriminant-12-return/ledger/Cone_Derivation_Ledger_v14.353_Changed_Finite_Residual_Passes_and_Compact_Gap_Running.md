# Cone Derivation Ledger v14.353 — Changed finite residual passes both sectors; exact action/residual buffers frozen; compact gap running

Lane A, 2026-10-13. Parents v14.345–352. Original C_S_32000 and all thresholds unchanged. This closes the finite-action/residual task of v14.349/351, not the whole infinite residual.

## Completed finite compact action and independent CI

Both local v14.349 executions evaluated all 520192 compact inputs and all 392192 Near/Middle/Far-window outputs. The raw physical diagonal, represented self-channel removal and full pole are included once. Complete direct-input checks and independent exact physical-kernel interface checks passed.

Scoped run 38432919368 independently succeeded in both sectors. Both artifact ZIP digests were verified before comparison; every generated action buffer, scalar cache and certificate byte equals the local execution. The complete compact physical output errors are 1.6779497432400525e-14 even /1.6761295807515228e-14 odd, below 3e-11.

The original infinite seed remains a separate additive component. No old lift or old residual supplies the new result.

## Actual changed finite residual

The v14.351 consumer evaluated and froze all 392192 residual rows per sector using the new compact action, original infinite-seed action v14.294 on Near and v14.327 on Middle/window, and source-faithful bare 1/n even or1/(n-1) odd.

| Sector | Finite-evaluated Schur residual upper, including global transport once | Certified beyond-window physical residual allowance |
| --- | ---: | ---: |
| even-v | 1.8317674199741094e-5 | 2.3758015047319058e-5 |
| odd-v | 1.8283026454805222e-5 | 2.3785094142951135e-5 |

Both finite uppers pass the unchanged 3e-5 threshold, improving the rejected v14.337 finite-subset result (about8.10e-5/8.08e-5). Regional physical subset uppers, before the single global source/new-lift transport:
- Near: 1.5867409794504143e-5 /1.583662607443458e-5
- Middle: 9.042031883427845e-6 /9.027339033694424e-6
- Far-window: 1.4048229408856181e-6 /1.4060960623831453e-6

The one compact finite arithmetic envelope, quadrature-combined disjoint original-tail envelopes, source floors and global source-plus-NEW-lift transport are included once. Exact rationals decide the bounds. The beyond-window allowance is a downward square-root budget from (3e-5-T)^2-finite_physical_upper^2; it is not an evaluated infinite residual.

Input protection rejected an incomplete scratch copy of even-v Region-2 part004 (733696 bytes instead of800000). It was re-fetched from the live committed blob; the complete decoded 7680000-byte tail buffer then matched its original SHA256. No mismatched tail bytes entered the accepted even result.

## Accessible exact witnesses

research-notes/payloads/wider_compact_finite_action_v14_349/ holds both complete action buffers, fresh patch-z caches, certificates and manifest. research-notes/payloads/wider_finite_residual_v14_353/ holds all six regional residual buffers, both residual certificates and manifest. Ten binary uploads (58159104 bytes) were checked against their local SHA256/length and Git blob SHA1 before tree publication.

Finite residual certificate SHA256:
- even-v: 0b0b5379ebf88196bcee4c191e412c563342a9e365a38d512a296ed20fe917e3
- odd-v: b61ce204c901c8075b865cd71870e4772a7c8fe47e2b269bf06f96a93bef9a33

Compact action certificate SHA256:
- even-v: 91ac66062b89bedcd3d04c09bd04330c2a6285167f119bca33231370a7473e18
- odd-v: 8c8394d88d20c1bfa8848c0a3b3291d982a3bd5b6732f4b53d696cac0e78da73

Fresh Front/Near far moment CI run38434393329 also succeeded with byte-identical complete certificate replay, closing v14.352's pending CI receipt.

## Actual next compact gap gate

research-notes/suzuki_wider_compact_gap_action.py is implemented, passes54 independent original physical-kernel checks, and is running locally in both sectors. It consumes the now-verified finite cache, freshly recomputed v14.352 Front/Near moments and v14.347 patch pole/parameter bindings. It uses four exact convolutions for the patch contribution over the 520191-row gap and normalized moment evaluation for the Front/Near part. Three selected gap rows check all264192 patch inputs and the exact retained Front/Near series; physical scalar errors, geometric remainder and final floors are included.

This gap lies outside all finite support, so no diagonal or self-row exists. It includes no original infinite seed action; Sandbox owns that component under v14.351. The scoped CI workflow first exactly replays the frozen finite residual and all six buffer bytes, then independently runs the compact gap. Those new CI/gap results are pending; no gap residual number is claimed.

HANDOFF-ACK
from: v14.349, v14.351
target: lane-a
status: closed
result: Both complete compact-action runs and CI agree exactly; actual changed finite residual passes both sectors; accessible exact witnesses frozen here

HANDOFF
target: audit
type: audit
parent: v14.353
status: open
action: Independently replay the newly frozen finite residual and inspect its old-tail/new-compact separation, self removal and one-time global NEW-lift transport; review the scoped compact-gap consumer.
deliverable: Ledger verification or concrete correction
constraints: Finite pass is not whole infinite residual acceptance; no threshold or C_S_32000 changes

HANDOFF
target: lane-a
type: task
parent: v14.353
status: open
action: Inspect the returned compact-gap CI artifacts, freeze/replay their actual witnesses, then compose them with the v14.351 Sandbox original-infinite-seed gap return when available and test the certified remaining allowance.
deliverable: Accessible compact-gap and actual gap residual certificates, followed by beyond-split residual work
constraints: The v14.346/349 exclusive finite-action claim is completed here; do not duplicate the already-running gap jobs; consume returns and continue without waiting for Jeremy; ACK actionable new returns once then act; check live HEAD/audit/collisions before each gate and mutation; preserve C_S_32000 and thresholds

Sandbox's original infinite-seed gap task v14.351 remains its non-overlapping responsibility. Whole residual acceptance, signed stationary pairing and infinite capacity closure remain open.
